"""
Tests for LOOM agent models and workflows.
"""

import pytest
from datetime import datetime

from loom.models.agent_models import (
    AgentType,
    AgentInputSchema,
    AgentOutputSchema,
    AgentNode,
    AgentWorkflow,
    AgentConnection,
    GovernanceRule,
)


class TestAgentNode:
    """Test agent node definition."""

    def test_agent_node_creation(self):
        """Test creating agent node."""
        agent = AgentNode(
            id="agent_001",
            name="Test Agent",
            agent_type=AgentType.EXECUTOR,
            description="Test agent",
            input_schema=[
                AgentInputSchema(
                    name="input1",
                    type="str",
                    required=True,
                    description="Test input"
                )
            ],
            output_schema=[
                AgentOutputSchema(
                    name="output1",
                    type="str",
                    description="Test output"
                )
            ],
            implementation="test.agent_impl"
        )

        assert agent.id == "agent_001"
        assert agent.agent_type == AgentType.EXECUTOR
        assert len(agent.input_schema) == 1
        assert len(agent.output_schema) == 1

    def test_input_validation(self):
        """Test agent input validation."""
        agent = AgentNode(
            id="agent_001",
            name="Test Agent",
            agent_type=AgentType.EXECUTOR,
            description="Test",
            input_schema=[
                AgentInputSchema(
                    name="required_input",
                    type="str",
                    required=True
                ),
                AgentInputSchema(
                    name="optional_input",
                    type="str",
                    required=False,
                    default="default_value"
                )
            ],
            output_schema=[],
            implementation="test.impl"
        )

        # Valid input
        errors = agent.validate_input({
            "required_input": "value"
        })
        assert len(errors) == 0

        # Missing required input
        errors = agent.validate_input({
            "optional_input": "value"
        })
        assert len(errors) == 1
        assert "required_input" in errors[0]

    def test_governance_rules(self):
        """Test adding governance rules to agent."""
        agent = AgentNode(
            id="agent_001",
            name="Test Agent",
            agent_type=AgentType.EXECUTOR,
            description="Test",
            input_schema=[],
            output_schema=[],
            implementation="test.impl"
        )

        rule = GovernanceRule(
            rule_id="cost_limit",
            rule_type="cost_limit",
            constraint={"max_cost": 1.0},
            action_on_violation="halt"
        )

        agent.add_governance_rule(rule)
        assert len(agent.governance_rules) == 1
        assert agent.governance_rules[0].rule_id == "cost_limit"

    def test_serialization(self):
        """Test agent serialization."""
        agent = AgentNode(
            id="agent_001",
            name="Test Agent",
            agent_type=AgentType.EXECUTOR,
            description="Test",
            input_schema=[],
            output_schema=[],
            implementation="test.impl"
        )

        serialized = agent.to_serializable()
        assert serialized["id"] == "agent_001"
        assert serialized["agent_type"] == "executor"


class TestAgentWorkflow:
    """Test workflow definition."""

    def test_workflow_creation(self):
        """Test creating workflow."""
        agent1 = AgentNode(
            id="agent_001",
            name="Agent 1",
            agent_type=AgentType.EXECUTOR,
            description="First agent",
            input_schema=[],
            output_schema=[
                AgentOutputSchema(name="output1", type="str")
            ],
            implementation="test.impl1"
        )

        agent2 = AgentNode(
            id="agent_002",
            name="Agent 2",
            agent_type=AgentType.EXECUTOR,
            description="Second agent",
            input_schema=[
                AgentInputSchema(name="input1", type="str", required=True)
            ],
            output_schema=[],
            implementation="test.impl2"
        )

        connection = AgentConnection(
            id="conn_001",
            source_agent_id="agent_001",
            source_output="output1",
            target_agent_id="agent_002",
            target_input="input1"
        )

        workflow = AgentWorkflow(
            id="workflow_001",
            name="Test Workflow",
            description="Test workflow",
            agents=[agent1, agent2],
            connections=[connection],
            entry_points=["agent_001"]
        )

        assert len(workflow.agents) == 2
        assert len(workflow.connections) == 1
        assert "agent_001" in workflow.entry_points

    def test_get_agent(self):
        """Test retrieving agent by ID."""
        agent = AgentNode(
            id="agent_001",
            name="Test Agent",
            agent_type=AgentType.EXECUTOR,
            description="Test",
            input_schema=[],
            output_schema=[],
            implementation="test.impl"
        )

        workflow = AgentWorkflow(
            id="workflow_001",
            name="Test Workflow",
            description="Test",
            agents=[agent],
            connections=[],
            entry_points=["agent_001"]
        )

        retrieved = workflow.get_agent("agent_001")
        assert retrieved is not None
        assert retrieved.id == "agent_001"

        not_found = workflow.get_agent("agent_999")
        assert not_found is None

    def test_get_downstream_agents(self):
        """Test finding downstream agents."""
        agent1 = AgentNode(
            id="agent_001",
            name="Agent 1",
            agent_type=AgentType.EXECUTOR,
            description="First",
            input_schema=[],
            output_schema=[AgentOutputSchema(name="out", type="str")],
            implementation="test.impl1"
        )

        agent2 = AgentNode(
            id="agent_002",
            name="Agent 2",
            agent_type=AgentType.EXECUTOR,
            description="Second",
            input_schema=[AgentInputSchema(name="in", type="str", required=True)],
            output_schema=[],
            implementation="test.impl2"
        )

        connection = AgentConnection(
            id="conn_001",
            source_agent_id="agent_001",
            source_output="out",
            target_agent_id="agent_002",
            target_input="in"
        )

        workflow = AgentWorkflow(
            id="workflow_001",
            name="Test",
            description="Test",
            agents=[agent1, agent2],
            connections=[connection],
            entry_points=["agent_001"]
        )

        downstream = workflow.get_downstream_agents("agent_001")
        assert "agent_002" in downstream

    def test_workflow_validation(self):
        """Test workflow validation."""
        agent = AgentNode(
            id="agent_001",
            name="Test Agent",
            agent_type=AgentType.EXECUTOR,
            description="Test",
            input_schema=[],
            output_schema=[],
            implementation="test.impl"
        )

        # Valid workflow
        workflow = AgentWorkflow(
            id="workflow_001",
            name="Test",
            description="Test",
            agents=[agent],
            connections=[],
            entry_points=["agent_001"]
        )

        errors = workflow.validate_workflow()
        assert len(errors) == 0

        # Invalid entry point
        workflow.entry_points = ["agent_999"]
        errors = workflow.validate_workflow()
        assert len(errors) > 0
        assert "agent_999" in errors[0]

    def test_workflow_serialization(self):
        """Test workflow serialization."""
        agent = AgentNode(
            id="agent_001",
            name="Test Agent",
            agent_type=AgentType.EXECUTOR,
            description="Test",
            input_schema=[],
            output_schema=[],
            implementation="test.impl"
        )

        workflow = AgentWorkflow(
            id="workflow_001",
            name="Test Workflow",
            description="Test",
            agents=[agent],
            connections=[],
            entry_points=["agent_001"]
        )

        serialized = workflow.to_serializable()
        assert serialized["id"] == "workflow_001"
        assert len(serialized["agents"]) == 1
