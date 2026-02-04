"""
Tests for MNEMIS memory store operations.
"""

import pytest
import tempfile
from pathlib import Path

from mnemis.core.memory_store import MnemisStore
from mnemis.core.contracts import MemoryAccessController
from mnemis.models.memory_models import (
    MemoryAccessLevel,
    MemoryScope,
    MemoryAccessViolation,
)


class TestMnemisStore:
    """Test memory store operations."""

    @pytest.fixture
    def temp_store(self):
        """Create temporary memory store."""
        with tempfile.TemporaryDirectory() as tmpdir:
            store = MnemisStore(base_path=Path(tmpdir))
            yield store

    @pytest.fixture
    def access_controller(self):
        """Create access controller."""
        return MemoryAccessController()

    def test_write_gaia_memory(self, temp_store, access_controller):
        """Test writing GAIA-level memory."""
        contract = access_controller.register_agent(
            agent_id="gaia_agent",
            access_level=MemoryAccessLevel.GAIA
        )
        scope = access_controller.create_gaia_scope()

        memory_id = temp_store.write(
            content={"pattern": "test_pattern"},
            scope=scope,
            contract=contract,
            tags=["test"]
        )

        assert memory_id is not None
        assert memory_id in temp_store.gaia_memory

    def test_write_project_memory(self, temp_store, access_controller):
        """Test writing PROJECT-level memory."""
        contract = access_controller.register_agent(
            agent_id="project_agent",
            access_level=MemoryAccessLevel.PROJECT,
            project_id="test_project"
        )
        scope = access_controller.create_project_scope("test_project")

        memory_id = temp_store.write(
            content={"data": "test_data"},
            scope=scope,
            contract=contract,
            tags=["project"]
        )

        assert memory_id is not None
        assert "test_project" in temp_store.project_memory
        assert memory_id in temp_store.project_memory["test_project"]

    def test_write_agent_memory(self, temp_store, access_controller):
        """Test writing AGENT-level ephemeral memory."""
        contract = access_controller.register_agent(
            agent_id="test_agent",
            access_level=MemoryAccessLevel.AGENT,
            project_id="test_project"
        )
        scope = access_controller.create_agent_scope(
            agent_id="test_agent",
            project_id="test_project",
            ttl_seconds=3600
        )

        memory_id = temp_store.write(
            content={"temp": "data"},
            scope=scope,
            contract=contract
        )

        assert memory_id is not None
        assert memory_id in temp_store.agent_memory

    def test_read_with_permission(self, temp_store, access_controller):
        """Test reading memory with correct permissions."""
        # Write as GAIA
        gaia_contract = access_controller.register_agent(
            agent_id="gaia_agent",
            access_level=MemoryAccessLevel.GAIA
        )
        scope = access_controller.create_gaia_scope()
        memory_id = temp_store.write(
            content={"data": "test"},
            scope=scope,
            contract=gaia_contract
        )

        # Read as GAIA (should work)
        memory = temp_store.read(memory_id, gaia_contract)
        assert memory.content["data"] == "test"

    def test_read_without_permission(self, temp_store, access_controller):
        """Test reading memory without permission raises error."""
        # Write as GAIA
        gaia_contract = access_controller.register_agent(
            agent_id="gaia_agent",
            access_level=MemoryAccessLevel.GAIA
        )
        scope = access_controller.create_gaia_scope()
        memory_id = temp_store.write(
            content={"data": "test"},
            scope=scope,
            contract=gaia_contract
        )

        # Try to read as AGENT (should fail)
        agent_contract = access_controller.register_agent(
            agent_id="test_agent",
            access_level=MemoryAccessLevel.AGENT,
            project_id="test_project"
        )

        with pytest.raises(MemoryAccessViolation):
            temp_store.read(memory_id, agent_contract)

    def test_write_without_permission(self, temp_store, access_controller):
        """Test writing to wrong tier raises error."""
        # AGENT trying to write GAIA-level memory
        agent_contract = access_controller.register_agent(
            agent_id="test_agent",
            access_level=MemoryAccessLevel.AGENT,
            project_id="test_project"
        )
        gaia_scope = access_controller.create_gaia_scope()

        with pytest.raises(MemoryAccessViolation):
            temp_store.write(
                content={"data": "test"},
                scope=gaia_scope,
                contract=agent_contract
            )

    def test_update_memory(self, temp_store, access_controller):
        """Test updating existing memory."""
        contract = access_controller.register_agent(
            agent_id="gaia_agent",
            access_level=MemoryAccessLevel.GAIA
        )
        scope = access_controller.create_gaia_scope()

        memory_id = temp_store.write(
            content={"data": "original"},
            scope=scope,
            contract=contract
        )

        temp_store.update(
            memory_id=memory_id,
            content={"data": "updated"},
            contract=contract
        )

        memory = temp_store.read(memory_id, contract)
        assert memory.content["data"] == "updated"

    def test_delete_memory(self, temp_store, access_controller):
        """Test deleting memory."""
        contract = access_controller.register_agent(
            agent_id="gaia_agent",
            access_level=MemoryAccessLevel.GAIA
        )
        scope = access_controller.create_gaia_scope()

        memory_id = temp_store.write(
            content={"data": "test"},
            scope=scope,
            contract=contract
        )

        temp_store.delete(memory_id, contract)

        with pytest.raises(KeyError):
            temp_store.read(memory_id, contract)

    def test_cleanup_expired_agent_memory(self, temp_store, access_controller):
        """Test cleanup of expired agent memory."""
        contract = access_controller.register_agent(
            agent_id="test_agent",
            access_level=MemoryAccessLevel.AGENT,
            project_id="test_project"
        )
        scope = access_controller.create_agent_scope(
            agent_id="test_agent",
            project_id="test_project",
            ttl_seconds=0  # Immediate expiration
        )

        memory_id = temp_store.write(
            content={"temp": "data"},
            scope=scope,
            contract=contract
        )

        # Memory should exist
        assert memory_id in temp_store.agent_memory

        # Cleanup expired
        cleaned = temp_store.cleanup_expired_agent_memory()
        assert cleaned == 1
        assert memory_id not in temp_store.agent_memory

    def test_get_all_gaia_memory(self, temp_store, access_controller):
        """Test retrieving all GAIA memory."""
        contract = access_controller.register_agent(
            agent_id="gaia_agent",
            access_level=MemoryAccessLevel.GAIA
        )
        scope = access_controller.create_gaia_scope()

        # Write multiple memories
        temp_store.write(
            content={"data": "1"},
            scope=scope,
            contract=contract
        )
        temp_store.write(
            content={"data": "2"},
            scope=scope,
            contract=contract
        )

        gaia_memories = temp_store.get_all_gaia_memory()
        assert len(gaia_memories) == 2

    def test_get_project_memory(self, temp_store, access_controller):
        """Test retrieving project memory."""
        contract = access_controller.register_agent(
            agent_id="project_agent",
            access_level=MemoryAccessLevel.PROJECT,
            project_id="test_project"
        )
        scope = access_controller.create_project_scope("test_project")

        temp_store.write(
            content={"data": "project"},
            scope=scope,
            contract=contract
        )

        project_memories = temp_store.get_project_memory("test_project")
        assert len(project_memories) == 1
        assert project_memories[0].content["data"] == "project"
