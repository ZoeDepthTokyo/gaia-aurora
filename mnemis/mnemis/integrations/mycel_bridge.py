"""
Integration bridge between MNEMIS and MYCEL.

Allows MYCEL-based agents to access MNEMIS memory with contract enforcement.
"""

from typing import Dict, Any, List, Optional
from datetime import datetime

from mnemis.core.memory_store import MnemisStore
from mnemis.core.contracts import MemoryAccessController
from mnemis.models.memory_models import (
    MemoryAccessLevel,
    MemoryEntry,
    MemoryContract,
)


class MycelMemoryBridge:
    """
    Bridge for MYCEL agents to access MNEMIS memory.

    Provides simplified interface for common memory operations
    while enforcing access contracts.
    """

    def __init__(
        self,
        memory_store: MnemisStore,
        access_controller: MemoryAccessController
    ):
        """
        Initialize memory bridge.

        Args:
            memory_store: MNEMIS memory store
            access_controller: Access controller
        """
        self.memory_store = memory_store
        self.access_controller = access_controller

    def create_agent_session(
        self,
        agent_id: str,
        project_id: str,
        ttl_seconds: int = 3600
    ) -> MemoryContract:
        """
        Create memory session for MYCEL agent.

        Args:
            agent_id: Agent identifier
            project_id: Project context
            ttl_seconds: Session TTL (default: 1 hour)

        Returns:
            Memory contract for this session
        """
        # Register agent with AGENT-level access
        contract = self.access_controller.register_agent(
            agent_id=agent_id,
            access_level=MemoryAccessLevel.AGENT,
            project_id=project_id
        )

        return contract

    def store_agent_memory(
        self,
        agent_id: str,
        project_id: str,
        content: Dict[str, Any],
        tags: Optional[List[str]] = None,
        ttl_seconds: int = 3600
    ) -> str:
        """
        Store ephemeral agent memory.

        Args:
            agent_id: Agent identifier
            project_id: Project context
            content: Memory content
            tags: Optional tags
            ttl_seconds: Time-to-live

        Returns:
            Memory ID
        """
        contract = self.access_controller.get_contract(agent_id)

        scope = self.access_controller.create_agent_scope(
            agent_id=agent_id,
            project_id=project_id,
            auto_expire=True,
            ttl_seconds=ttl_seconds
        )

        memory_id = self.memory_store.write(
            content=content,
            scope=scope,
            contract=contract,
            tags=tags
        )

        return memory_id

    def retrieve_agent_memory(
        self,
        agent_id: str,
        memory_id: str
    ) -> MemoryEntry:
        """
        Retrieve agent memory.

        Args:
            agent_id: Agent identifier
            memory_id: Memory identifier

        Returns:
            Memory entry
        """
        contract = self.access_controller.get_contract(agent_id)
        return self.memory_store.read(memory_id, contract)

    def search_project_patterns(
        self,
        agent_id: str,
        project_id: str,
        tags: List[str]
    ) -> List[MemoryEntry]:
        """
        Search for project-level patterns by tags.

        Args:
            agent_id: Agent identifier
            project_id: Project context
            tags: Tags to search for

        Returns:
            List of matching memories
        """
        # Agent can read project-level memory
        from mnemis.core.search import MemorySearchEngine

        contract = self.access_controller.get_contract(agent_id)
        search_engine = MemorySearchEngine(self.memory_store)

        return search_engine.search_by_tags(
            tags=tags,
            contract=contract,
            match_all=False
        )

    def cleanup_expired_sessions(self) -> int:
        """
        Clean up expired agent memory sessions.

        Returns:
            Number of sessions cleaned up
        """
        return self.memory_store.cleanup_expired_agent_memory()
