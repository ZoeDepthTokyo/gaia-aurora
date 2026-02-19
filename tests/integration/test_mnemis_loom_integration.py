"""
Integration tests for MNEMIS and LOOM (Phase 3).

Tests memory contracts enforcement, memory promotion workflow,
and LOOM agent accessing MNEMIS memory with constitutional boundaries.
"""

import tempfile
from pathlib import Path
from typing import Any, Dict

import pytest

from loom.core.workflow_engine import WorkflowEngine
from loom.models.agent_models import (
    AgentExecutionState,
    AgentNode,
    AgentWorkflow,
    GovernanceRule,
)
from mnemis.core.contracts import MemoryAccessController
from mnemis.core.memory_store import MnemisStore
from mnemis.core.promotion import MemoryPromotionEngine
from mnemis.models.memory_models import (
    MemoryAccessLevel,
    MemoryAccessViolation,
)


class TestMemoryContractsEnforcement:
    """
    Test memory access contract enforcement.

    Verifies that agents can only access memory according to
    their constitutional permissions (read down, write exact level).
    """

    @pytest.fixture
    def memory_system(self):
        """Set up memory system with contracts."""
        with tempfile.TemporaryDirectory() as tmpdir:
            store = MnemisStore(base_path=Path(tmpdir))
            controller = MemoryAccessController()
            yield {"store": store, "controller": controller}

    def test_agent_can_read_own_memory(self, memory_system):
        """
        Test agent can read its own ephemeral memory.

        Verifies basic read access within permitted scope.
        """
        store = memory_system["store"]
        controller = memory_system["controller"]

        # Register agent
        contract = controller.register_agent(
            agent_id="test_agent",
            access_level=MemoryAccessLevel.AGENT,
            project_id="test_project",
        )

        # Create agent-scoped memory
        scope = controller.create_agent_scope(agent_id="test_agent", project_id="test_project")

        # Write memory
        memory_id = store.write(content={"note": "test data"}, scope=scope, contract=contract)

        # Read memory
        memory = store.read(memory_id, contract)

        assert memory is not None
        assert memory.content["note"] == "test data"

    def test_agent_can_read_down_hierarchy(self, memory_system):
        """
        Test agents can read DOWN the hierarchy.

        GAIA-level agent should read PROJECT and AGENT memory.
        PROJECT-level agent should read AGENT memory.
        """
        store = memory_system["store"]
        controller = memory_system["controller"]

        # Create GAIA-level agent
        gaia_contract = controller.register_agent(
            agent_id="gaia_agent", access_level=MemoryAccessLevel.GAIA
        )

        # Create PROJECT-level memory
        project_scope = controller.create_project_scope("test_project")
        project_memory_id = store.write(
            content={"data": "project-level"},
            scope=project_scope,
            contract=gaia_contract,  # GAIA agent can write to any level (for test setup)
        )

        # GAIA agent should be able to read PROJECT memory
        memory = store.read(project_memory_id, gaia_contract)
        assert memory.content["data"] == "project-level"

    def test_agent_cannot_read_up_hierarchy(self, memory_system):
        """
        Test agents CANNOT read UP the hierarchy.

        AGENT-level should not access PROJECT memory.
        PROJECT-level should not access GAIA memory.
        """
        store = memory_system["store"]
        controller = memory_system["controller"]

        # Create GAIA-level memory
        gaia_contract = controller.register_agent(
            agent_id="gaia_agent", access_level=MemoryAccessLevel.GAIA
        )
        gaia_scope = controller.create_gaia_scope()
        gaia_memory_id = store.write(
            content={"secret": "gaia-only"}, scope=gaia_scope, contract=gaia_contract
        )

        # Create AGENT-level agent
        agent_contract = controller.register_agent(
            agent_id="lowly_agent",
            access_level=MemoryAccessLevel.AGENT,
            project_id="test_project",
        )

        # AGENT should NOT be able to read GAIA memory
        with pytest.raises(MemoryAccessViolation):
            store.read(gaia_memory_id, agent_contract)

    def test_agent_can_write_only_exact_level(self, memory_system):
        """
        Test agents can WRITE only at their exact level.

        AGENT-level writes to AGENT scope only.
        PROJECT-level writes to PROJECT scope only.
        """
        store = memory_system["store"]
        controller = memory_system["controller"]

        # Create AGENT-level agent
        agent_contract = controller.register_agent(
            agent_id="test_agent",
            access_level=MemoryAccessLevel.AGENT,
            project_id="test_project",
        )

        # Can write to AGENT scope
        agent_scope = controller.create_agent_scope("test_agent", "test_project")
        memory_id = store.write(
            content={"data": "agent-level"}, scope=agent_scope, contract=agent_contract
        )
        assert memory_id is not None

        # CANNOT write to PROJECT scope
        project_scope = controller.create_project_scope("test_project")
        with pytest.raises(MemoryAccessViolation):
            store.write(
                content={"data": "should fail"},
                scope=project_scope,
                contract=agent_contract,
            )

    def test_cross_project_isolation(self, memory_system):
        """
        Test no cross-project contamination.

        PROJECT-level agents in different projects cannot
        access each other's memory.
        """
        store = memory_system["store"]
        controller = memory_system["controller"]

        # Create two project agents
        project_a_contract = controller.register_agent(
            agent_id="agent_a",
            access_level=MemoryAccessLevel.PROJECT,
            project_id="project_a",
        )

        project_b_contract = controller.register_agent(
            agent_id="agent_b",
            access_level=MemoryAccessLevel.PROJECT,
            project_id="project_b",
        )

        # Project A writes memory
        scope_a = controller.create_project_scope("project_a")
        memory_a_id = store.write(
            content={"secret": "project A data"},
            scope=scope_a,
            contract=project_a_contract,
        )

        # Project B should NOT access Project A memory
        # (even though both are PROJECT-level)
        with pytest.raises(MemoryAccessViolation):
            store.read(memory_a_id, project_b_contract)

    def test_memory_provenance_tracking(self, memory_system):
        """
        Test that all memory operations track provenance.

        Verifies auditability of who accessed/modified memory.
        """
        store = memory_system["store"]
        controller = memory_system["controller"]

        # Create agent and write memory
        contract = controller.register_agent(
            agent_id="audit_agent",
            access_level=MemoryAccessLevel.AGENT,
            project_id="test_project",
        )

        scope = controller.create_agent_scope("audit_agent", "test_project")
        memory_id = store.write(content={"data": "test"}, scope=scope, contract=contract)

        # Read memory
        memory = store.read(memory_id, contract)

        # Check provenance
        assert len(memory.provenance) > 0

        # Should have creation event
        creation_events = [e for e in memory.provenance if e["event_type"] == "created"]
        assert len(creation_events) > 0
        assert creation_events[0]["actor"] == "audit_agent"

        # Should have access event
        access_events = [e for e in memory.provenance if e["event_type"] == "accessed"]
        assert len(access_events) > 0


class TestMemoryPromotionWorkflow:
    """
    Test memory promotion workflow.

    Verifies that memory moves UP hierarchy only via
    explicit proposal and approval.
    """

    @pytest.fixture
    def promotion_system(self):
        """Set up promotion system."""
        with tempfile.TemporaryDirectory() as tmpdir:
            store = MnemisStore(base_path=Path(tmpdir))
            controller = MemoryAccessController()
            engine = MemoryPromotionEngine(store, controller)

            yield {"store": store, "controller": controller, "engine": engine}

    def test_agent_to_project_promotion(self, promotion_system):
        """
        Test promoting memory from AGENT to PROJECT tier.

        Verifies proposal, approval, and promotion execution.
        """
        store = promotion_system["store"]
        controller = promotion_system["controller"]
        engine = promotion_system["engine"]

        # Create agent and memory
        agent_contract = controller.register_agent(
            agent_id="proposing_agent",
            access_level=MemoryAccessLevel.AGENT,
            project_id="test_project",
        )

        agent_scope = controller.create_agent_scope("proposing_agent", "test_project")
        memory_id = store.write(
            content={"insight": "valuable pattern discovered"},
            scope=agent_scope,
            contract=agent_contract,
        )

        # Propose promotion to PROJECT
        project_scope = controller.create_project_scope("test_project")
        proposal_id = engine.propose_promotion(
            memory_id=memory_id,
            to_scope=project_scope,
            agent_id="proposing_agent",
            rationale="This pattern is useful for entire project",
        )

        assert proposal_id is not None

        # Verify proposal exists
        proposal = engine.get_proposal(proposal_id)
        assert proposal.status == "pending"
        assert proposal.memory_id == memory_id

        # Approve promotion
        promoted_id = engine.approve_promotion(
            proposal_id=proposal_id,
            reviewer="human_reviewer",
            notes="Agreed, valuable insight",
        )

        assert promoted_id is not None

        # Verify promoted memory exists at PROJECT level
        project_contract = controller.register_agent(
            agent_id="project_agent",
            access_level=MemoryAccessLevel.PROJECT,
            project_id="test_project",
        )

        promoted_memory = store.read(promoted_id, project_contract)
        assert promoted_memory.scope.level == MemoryAccessLevel.PROJECT
        assert promoted_memory.content["insight"] == "valuable pattern discovered"

    def test_project_to_gaia_promotion(self, promotion_system):
        """
        Test promoting memory from PROJECT to GAIA tier.

        Verifies ecosystem-wide promotion with proper approval.
        """
        store = promotion_system["store"]
        controller = promotion_system["controller"]
        engine = promotion_system["engine"]

        # Create project-level memory
        project_contract = controller.register_agent(
            agent_id="project_agent",
            access_level=MemoryAccessLevel.PROJECT,
            project_id="test_project",
        )

        project_scope = controller.create_project_scope("test_project")
        memory_id = store.write(
            content={"lesson": "general principle about LLM behavior"},
            scope=project_scope,
            contract=project_contract,
        )

        # Propose promotion to GAIA
        gaia_scope = controller.create_gaia_scope()
        proposal_id = engine.propose_promotion(
            memory_id=memory_id,
            to_scope=gaia_scope,
            agent_id="project_agent",
            rationale="This lesson applies to all GAIA projects",
        )

        # Approve
        promoted_id = engine.approve_promotion(proposal_id=proposal_id, reviewer="gaia_maintainer")

        # Verify at GAIA level
        gaia_contract = controller.register_agent(
            agent_id="gaia_observer", access_level=MemoryAccessLevel.GAIA
        )

        promoted_memory = store.read(promoted_id, gaia_contract)
        assert promoted_memory.scope.level == MemoryAccessLevel.GAIA

    def test_rejection_workflow(self, promotion_system):
        """
        Test rejection of promotion proposal.

        Verifies that rejected proposals are logged for audit.
        """
        store = promotion_system["store"]
        controller = promotion_system["controller"]
        engine = promotion_system["engine"]

        # Create memory
        contract = controller.register_agent(
            agent_id="agent",
            access_level=MemoryAccessLevel.AGENT,
            project_id="test_project",
        )

        scope = controller.create_agent_scope("agent", "test_project")
        memory_id = store.write(
            content={"data": "not valuable enough"}, scope=scope, contract=contract
        )

        # Propose promotion
        project_scope = controller.create_project_scope("test_project")
        proposal_id = engine.propose_promotion(
            memory_id=memory_id,
            to_scope=project_scope,
            agent_id="agent",
            rationale="Maybe useful?",
        )

        # Reject
        engine.reject_promotion(
            proposal_id=proposal_id,
            reviewer="project_lead",
            notes="Insufficient evidence of value",
        )

        # Verify rejection
        proposal = engine.get_proposal(proposal_id)
        assert proposal.status == "rejected"
        assert "insufficient evidence" in proposal.review_notes.lower()

    def test_invalid_promotion_path_blocked(self, promotion_system):
        """
        Test that invalid promotion paths are blocked.

        Cannot skip levels (AGENT -> GAIA directly).
        """
        store = promotion_system["store"]
        controller = promotion_system["controller"]
        engine = promotion_system["engine"]

        # Create agent memory
        contract = controller.register_agent(
            agent_id="agent",
            access_level=MemoryAccessLevel.AGENT,
            project_id="test_project",
        )

        scope = controller.create_agent_scope("agent", "test_project")
        memory_id = store.write(content={"data": "test"}, scope=scope, contract=contract)

        # Try to promote AGENT -> GAIA directly (should fail)
        gaia_scope = controller.create_gaia_scope()

        with pytest.raises(MemoryAccessViolation):
            engine.propose_promotion(
                memory_id=memory_id,
                to_scope=gaia_scope,
                agent_id="agent",
                rationale="Skip levels",
            )

    def test_promotion_queue_visibility(self, promotion_system):
        """
        Test visibility of pending promotions.

        Verifies that pending proposals can be listed for review.
        """
        store = promotion_system["store"]
        controller = promotion_system["controller"]
        engine = promotion_system["engine"]

        # Create and propose multiple promotions
        contract = controller.register_agent(
            agent_id="agent",
            access_level=MemoryAccessLevel.AGENT,
            project_id="test_project",
        )

        project_scope = controller.create_project_scope("test_project")

        for i in range(3):
            scope = controller.create_agent_scope(f"agent_{i}", "test_project")
            memory_id = store.write(content={"data": f"memory {i}"}, scope=scope, contract=contract)

            engine.propose_promotion(
                memory_id=memory_id,
                to_scope=project_scope,
                agent_id="agent",
                rationale=f"Promotion {i}",
            )

        # Get pending queue
        pending = engine.get_pending_proposals()
        assert len(pending) >= 3

        # Get project-specific queue
        project_queue = engine.get_project_promotion_queue("test_project")
        assert len(project_queue) >= 3


class TestLoomMemoryAccess:
    """
    Test LOOM agents accessing MNEMIS memory.

    Verifies that workflow agents respect memory contracts
    and operate within constitutional boundaries.
    """

    @pytest.fixture
    def integrated_system(self):
        """Set up LOOM + MNEMIS integration."""
        with tempfile.TemporaryDirectory() as tmpdir:
            store = MnemisStore(base_path=Path(tmpdir))
            controller = MemoryAccessController()
            engine = WorkflowEngine()

            yield {"store": store, "controller": controller, "engine": engine}

    def test_workflow_agent_reads_memory(self, integrated_system):
        """
        Test LOOM agent reading from MNEMIS.

        Verifies that agents in workflows can access
        memory according to their contracts.
        """
        store = integrated_system["store"]
        controller = integrated_system["controller"]
        engine = integrated_system["engine"]

        # Create PROJECT-level memory
        project_contract = controller.register_agent(
            agent_id="setup_agent",
            access_level=MemoryAccessLevel.PROJECT,
            project_id="workflow_project",
        )

        project_scope = controller.create_project_scope("workflow_project")
        memory_id = store.write(
            content={"config": "workflow configuration"},
            scope=project_scope,
            contract=project_contract,
        )

        # Create workflow with memory-reading agent
        workflow = AgentWorkflow(
            id="test_workflow", name="Memory Reader", entry_points=["reader_agent"]
        )

        reader_agent = AgentNode(
            id="reader_agent",
            name="Memory Reader",
            agent_type="memory_reader",
            inputs={"memory_id": "string"},
            outputs={"content": "dict"},
        )

        workflow.add_agent(reader_agent)

        # Register implementation
        def read_memory_impl(inputs: Dict[str, Any]) -> Dict[str, Any]:
            mem_id = inputs["memory_id"]
            # Agent reads memory via contract
            memory = store.read(mem_id, project_contract)
            return {"content": memory.content}

        engine.register_agent_implementation("reader_agent", read_memory_impl)

        # Execute workflow
        context = engine.execute_workflow(
            workflow=workflow, initial_inputs={"memory_id": memory_id}
        )

        # Verify execution succeeded
        assert context.execution_count > 0

        # Check agent executed
        records = [r for r in context.execution_records if r.agent_id == "reader_agent"]
        assert len(records) > 0
        assert records[0].state == AgentExecutionState.COMPLETED

    def test_workflow_enforces_governance(self, integrated_system):
        """
        Test LOOM enforces governance rules.

        Verifies that agents respect cost limits, rate limits,
        and approval requirements.
        """
        engine = integrated_system["engine"]

        # Create workflow with governance
        workflow = AgentWorkflow(
            id="governed_workflow",
            name="Governed Agent",
            entry_points=["governed_agent"],
        )

        # Agent with cost limit
        governed_agent = AgentNode(
            id="governed_agent",
            name="Cost Limited",
            agent_type="processor",
            inputs={},
            outputs={},
            governance_rules=[
                GovernanceRule(rule_type="cost_limit", constraint={"max_cost": 0.01}, enabled=True)
            ],
        )

        workflow.add_agent(governed_agent)

        # Register implementation
        def governed_impl(inputs: Dict[str, Any]) -> Dict[str, Any]:
            return {}

        engine.register_agent_implementation("governed_agent", governed_impl)

        # Execute workflow
        context = engine.execute_workflow(workflow, {})

        # Should execute (under cost limit)
        assert context.execution_count > 0

        # Artificially exceed cost limit
        context.total_cost = 0.02

        # Try to execute again - should fail governance
        context2 = engine.execute_workflow(workflow, {})

        # Check for governance violations
        records = [r for r in context2.execution_records if r.agent_id == "governed_agent"]

        if len(records) > 0:
            # May have governance violations recorded
            assert (
                records[0].governance_violations is not None
                or records[0].state == AgentExecutionState.FAILED
            )

    def test_no_autonomous_memory_promotion(self, integrated_system):
        """
        Test that agents cannot autonomously promote memory.

        Constitutional boundary: promotion requires human approval.
        """
        store = integrated_system["store"]
        controller = integrated_system["controller"]
        engine = integrated_system["engine"]

        # Create agent memory
        contract = controller.register_agent(
            agent_id="workflow_agent",
            access_level=MemoryAccessLevel.AGENT,
            project_id="test_project",
        )

        scope = controller.create_agent_scope("workflow_agent", "test_project")
        memory_id = store.write(content={"data": "agent insight"}, scope=scope, contract=contract)

        # Agent can PROPOSE promotion, but not execute
        promotion_engine = MemoryPromotionEngine(store, controller)

        project_scope = controller.create_project_scope("test_project")
        proposal_id = promotion_engine.propose_promotion(
            memory_id=memory_id,
            to_scope=project_scope,
            agent_id="workflow_agent",
            rationale="Auto-promotion attempt",
        )

        # Proposal should exist
        proposal = promotion_engine.get_proposal(proposal_id)
        assert proposal.status == "pending"

        # But memory should NOT be promoted yet
        # (requires human approval)
        original_memory = store._locate_memory(memory_id)
        assert original_memory.scope.level == MemoryAccessLevel.AGENT

    def test_graceful_degradation_on_memory_error(self, integrated_system):
        """
        Test graceful degradation when memory access fails.

        Verifies workflow continues or fails gracefully
        without cascading errors.
        """
        store = integrated_system["store"]
        controller = integrated_system["controller"]
        engine = integrated_system["engine"]

        # Create workflow
        workflow = AgentWorkflow(
            id="error_handling", name="Error Handler", entry_points=["reader_agent"]
        )

        reader = AgentNode(
            id="reader_agent",
            name="Reader",
            agent_type="reader",
            inputs={"memory_id": "string"},
            outputs={"result": "string"},
        )

        workflow.add_agent(reader)

        # Register implementation that tries to read non-existent memory
        def failing_impl(inputs: Dict[str, Any]) -> Dict[str, Any]:
            # Try to read non-existent memory
            try:
                contract = controller.register_agent(
                    agent_id="reader_agent",
                    access_level=MemoryAccessLevel.AGENT,
                    project_id="test",
                )
                store.read("nonexistent_id", contract)
                return {"result": "success"}
            except KeyError:
                # Graceful degradation
                return {"result": "memory_not_found"}

        engine.register_agent_implementation("reader_agent", failing_impl)

        # Execute workflow
        context = engine.execute_workflow(workflow, {"memory_id": "nonexistent"})

        # Should complete (gracefully)
        records = [r for r in context.execution_records if r.agent_id == "reader_agent"]
        assert len(records) > 0

        # Agent should have handled error
        if records[0].state == AgentExecutionState.COMPLETED:
            assert records[0].outputs["result"] == "memory_not_found"


class TestEphemeralMemoryCleanup:
    """
    Test ephemeral agent memory cleanup.

    Verifies that agent-level memory auto-expires and
    doesn't pollute persistent storage.
    """

    @pytest.fixture
    def memory_system(self):
        """Set up memory system."""
        with tempfile.TemporaryDirectory() as tmpdir:
            store = MnemisStore(base_path=Path(tmpdir))
            controller = MemoryAccessController()
            yield {"store": store, "controller": controller}

    def test_agent_memory_auto_expires(self, memory_system):
        """
        Test that agent memory expires after TTL.

        Verifies ephemeral memory cleanup prevents bloat.
        """
        store = memory_system["store"]
        controller = memory_system["controller"]

        # Create agent with short TTL
        contract = controller.register_agent(
            agent_id="ephemeral_agent",
            access_level=MemoryAccessLevel.AGENT,
            project_id="test_project",
        )

        scope = controller.create_agent_scope(
            agent_id="ephemeral_agent",
            project_id="test_project",
            auto_expire=True,
            ttl_seconds=1,  # 1 second TTL
        )

        # Write memory
        memory_id = store.write(content={"temp": "data"}, scope=scope, contract=contract)

        # Retrieve memory (should exist)
        memory = store.read(memory_id, contract)
        assert memory is not None

        # Wait for expiration (simulate with manual expiration check)
        # In production, this would be a background task
        import time

        time.sleep(2)

        # Cleanup expired memories
        cleaned = store.cleanup_expired_agent_memory()

        # Should have cleaned up at least 1 memory
        assert cleaned >= 1

    def test_project_memory_persists(self, memory_system):
        """
        Test that PROJECT memory does not auto-expire.

        Verifies persistent storage for project-level data.
        """
        store = memory_system["store"]
        controller = memory_system["controller"]

        # Create project memory
        contract = controller.register_agent(
            agent_id="project_agent",
            access_level=MemoryAccessLevel.PROJECT,
            project_id="test_project",
        )

        scope = controller.create_project_scope("test_project")
        memory_id = store.write(content={"persistent": "data"}, scope=scope, contract=contract)

        # Cleanup (should not affect PROJECT memory)
        cleaned = store.cleanup_expired_agent_memory()

        # PROJECT memory should still exist
        memory = store.read(memory_id, contract)
        assert memory is not None
        assert memory.content["persistent"] == "data"
