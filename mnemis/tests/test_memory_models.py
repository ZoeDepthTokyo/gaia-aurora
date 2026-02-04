"""
Tests for MNEMIS memory models and contracts.
"""

import pytest
from datetime import datetime

from mnemis.models.memory_models import (
    MemoryAccessLevel,
    MemoryScope,
    MemoryEntry,
    MemoryContract,
    MemoryPromotionProposal,
    MemoryAccessViolation,
)


class TestMemoryScope:
    """Test memory scope validation."""

    def test_gaia_scope_creation(self):
        """Test GAIA-level scope creation."""
        scope = MemoryScope(level=MemoryAccessLevel.GAIA)
        assert scope.level == MemoryAccessLevel.GAIA
        assert scope.project_id is None
        assert scope.agent_id is None
        assert scope.auto_expire is False

    def test_project_scope_requires_project_id(self):
        """Test PROJECT-level scope requires project_id."""
        with pytest.raises(ValueError):
            MemoryScope(level=MemoryAccessLevel.PROJECT)

        scope = MemoryScope(
            level=MemoryAccessLevel.PROJECT,
            project_id="test_project"
        )
        assert scope.project_id == "test_project"

    def test_agent_scope_auto_expire(self):
        """Test AGENT-level scope always auto-expires."""
        scope = MemoryScope(
            level=MemoryAccessLevel.AGENT,
            project_id="test_project",
            agent_id="test_agent",
            auto_expire=False,  # Should be overridden
            ttl_seconds=3600
        )
        assert scope.auto_expire is True  # Force enabled for AGENT


class TestMemoryEntry:
    """Test memory entry provenance tracking."""

    def test_memory_entry_creation(self):
        """Test creating memory entry."""
        scope = MemoryScope(level=MemoryAccessLevel.GAIA)
        entry = MemoryEntry(
            id="mem_001",
            content={"key": "value"},
            scope=scope,
            created_by="agent_001"
        )
        assert entry.id == "mem_001"
        assert entry.content["key"] == "value"
        assert len(entry.provenance) == 0

    def test_provenance_tracking(self):
        """Test provenance event tracking."""
        scope = MemoryScope(level=MemoryAccessLevel.GAIA)
        entry = MemoryEntry(
            id="mem_001",
            content={"key": "value"},
            scope=scope,
            created_by="agent_001"
        )

        entry.add_provenance_event(
            event_type="accessed",
            actor="agent_002",
            details={"reason": "test"}
        )

        assert len(entry.provenance) == 1
        assert entry.provenance[0]["event_type"] == "accessed"
        assert entry.provenance[0]["actor"] == "agent_002"

    def test_memory_expiration(self):
        """Test ephemeral memory expiration."""
        scope = MemoryScope(
            level=MemoryAccessLevel.AGENT,
            project_id="test_project",
            agent_id="test_agent",
            ttl_seconds=0  # Immediate expiration
        )
        entry = MemoryEntry(
            id="mem_001",
            content={"key": "value"},
            scope=scope,
            created_by="test_agent"
        )

        assert entry.is_expired() is True


class TestMemoryContract:
    """Test memory access contracts."""

    def test_gaia_level_contract_read_permissions(self):
        """Test GAIA-level contract can read all tiers."""
        contract = MemoryContract(
            agent_id="gaia_agent",
            access_level=MemoryAccessLevel.GAIA
        )

        assert MemoryAccessLevel.GAIA in contract.read_permissions
        assert MemoryAccessLevel.PROJECT in contract.read_permissions
        assert MemoryAccessLevel.AGENT in contract.read_permissions

    def test_project_level_contract_read_permissions(self):
        """Test PROJECT-level contract can read PROJECT and AGENT."""
        contract = MemoryContract(
            agent_id="project_agent",
            access_level=MemoryAccessLevel.PROJECT,
            project_id="test_project"
        )

        assert MemoryAccessLevel.GAIA not in contract.read_permissions
        assert MemoryAccessLevel.PROJECT in contract.read_permissions
        assert MemoryAccessLevel.AGENT in contract.read_permissions

    def test_agent_level_contract_read_permissions(self):
        """Test AGENT-level contract can only read AGENT tier."""
        contract = MemoryContract(
            agent_id="test_agent",
            access_level=MemoryAccessLevel.AGENT,
            project_id="test_project"
        )

        assert MemoryAccessLevel.GAIA not in contract.read_permissions
        assert MemoryAccessLevel.PROJECT not in contract.read_permissions
        assert MemoryAccessLevel.AGENT in contract.read_permissions

    def test_write_permissions_same_level_only(self):
        """Test agents can only write at their exact level."""
        contract = MemoryContract(
            agent_id="project_agent",
            access_level=MemoryAccessLevel.PROJECT,
            project_id="test_project"
        )

        assert contract.write_permissions == [MemoryAccessLevel.PROJECT]

    def test_can_read_validation(self):
        """Test read permission validation."""
        contract = MemoryContract(
            agent_id="project_agent",
            access_level=MemoryAccessLevel.PROJECT,
            project_id="test_project"
        )

        gaia_scope = MemoryScope(level=MemoryAccessLevel.GAIA)
        project_scope = MemoryScope(
            level=MemoryAccessLevel.PROJECT,
            project_id="test_project"
        )

        assert contract.can_read(gaia_scope) is False
        assert contract.can_read(project_scope) is True

    def test_can_write_validation(self):
        """Test write permission validation."""
        contract = MemoryContract(
            agent_id="project_agent",
            access_level=MemoryAccessLevel.PROJECT,
            project_id="test_project"
        )

        gaia_scope = MemoryScope(level=MemoryAccessLevel.GAIA)
        project_scope = MemoryScope(
            level=MemoryAccessLevel.PROJECT,
            project_id="test_project"
        )
        other_project_scope = MemoryScope(
            level=MemoryAccessLevel.PROJECT,
            project_id="other_project"
        )

        assert contract.can_write(gaia_scope) is False
        assert contract.can_write(project_scope) is True
        assert contract.can_write(other_project_scope) is False

    def test_promotion_proposal_authority(self):
        """Test promotion proposal authority."""
        project_contract = MemoryContract(
            agent_id="project_agent",
            access_level=MemoryAccessLevel.PROJECT,
            project_id="test_project"
        )
        agent_contract = MemoryContract(
            agent_id="test_agent",
            access_level=MemoryAccessLevel.AGENT,
            project_id="test_project"
        )

        project_scope = MemoryScope(
            level=MemoryAccessLevel.PROJECT,
            project_id="test_project"
        )
        agent_scope = MemoryScope(
            level=MemoryAccessLevel.AGENT,
            project_id="test_project",
            agent_id="test_agent"
        )

        # PROJECT agent can propose PROJECT -> GAIA
        assert project_contract.can_propose_promotion(project_scope) is True

        # AGENT agent can propose AGENT -> PROJECT
        assert agent_contract.can_propose_promotion(agent_scope) is True

        # AGENT agent cannot propose PROJECT -> GAIA
        assert agent_contract.can_propose_promotion(project_scope) is False


class TestMemoryPromotionProposal:
    """Test memory promotion proposals."""

    def test_proposal_creation(self):
        """Test creating promotion proposal."""
        from_scope = MemoryScope(
            level=MemoryAccessLevel.PROJECT,
            project_id="test_project"
        )
        to_scope = MemoryScope(level=MemoryAccessLevel.GAIA)

        proposal = MemoryPromotionProposal(
            id="prop_001",
            memory_id="mem_001",
            from_scope=from_scope,
            to_scope=to_scope,
            rationale="Useful pattern for all projects",
            proposed_by="project_agent"
        )

        assert proposal.status == "pending"
        assert proposal.reviewed_by is None

    def test_proposal_approval(self):
        """Test approving proposal."""
        from_scope = MemoryScope(
            level=MemoryAccessLevel.PROJECT,
            project_id="test_project"
        )
        to_scope = MemoryScope(level=MemoryAccessLevel.GAIA)

        proposal = MemoryPromotionProposal(
            id="prop_001",
            memory_id="mem_001",
            from_scope=from_scope,
            to_scope=to_scope,
            rationale="Test",
            proposed_by="project_agent"
        )

        proposal.approve(reviewer="human", notes="Approved")

        assert proposal.status == "approved"
        assert proposal.reviewed_by == "human"
        assert proposal.review_notes == "Approved"
        assert proposal.reviewed_at is not None

    def test_proposal_rejection(self):
        """Test rejecting proposal."""
        from_scope = MemoryScope(
            level=MemoryAccessLevel.PROJECT,
            project_id="test_project"
        )
        to_scope = MemoryScope(level=MemoryAccessLevel.GAIA)

        proposal = MemoryPromotionProposal(
            id="prop_001",
            memory_id="mem_001",
            from_scope=from_scope,
            to_scope=to_scope,
            rationale="Test",
            proposed_by="project_agent"
        )

        proposal.reject(reviewer="human", notes="Not useful")

        assert proposal.status == "rejected"
        assert proposal.reviewed_by == "human"
        assert proposal.review_notes == "Not useful"
