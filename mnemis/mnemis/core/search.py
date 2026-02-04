"""
Memory search and retrieval for MNEMIS.

Provides search across memory tiers with respect for access contracts.
"""

from typing import List, Optional, Dict, Any
from datetime import datetime

from mnemis.models.memory_models import (
    MemoryEntry,
    MemoryContract,
    MemoryAccessLevel,
)
from mnemis.core.memory_store import MnemisStore


class MemorySearchEngine:
    """
    Search and filter memory across tiers.

    Respects access contracts - agents can only search
    memory they have read permission for.
    """

    def __init__(self, memory_store: MnemisStore):
        """
        Initialize search engine.

        Args:
            memory_store: Memory store instance
        """
        self.memory_store = memory_store

    def search_by_tags(
        self,
        tags: List[str],
        contract: MemoryContract,
        match_all: bool = False
    ) -> List[MemoryEntry]:
        """
        Search memory by tags.

        Args:
            tags: Tags to search for
            contract: Memory access contract
            match_all: If True, require all tags; if False, any tag matches

        Returns:
            List of matching memory entries
        """
        results = []

        # Search across accessible tiers
        all_memories = self._get_accessible_memories(contract)

        for memory in all_memories:
            if match_all:
                if all(tag in memory.tags for tag in tags):
                    results.append(memory)
            else:
                if any(tag in memory.tags for tag in tags):
                    results.append(memory)

        return results

    def search_by_content(
        self,
        query: str,
        contract: MemoryContract,
        field: Optional[str] = None
    ) -> List[MemoryEntry]:
        """
        Search memory content.

        Args:
            query: Search query (simple substring match)
            contract: Memory access contract
            field: Optional specific field to search in content dict

        Returns:
            List of matching memory entries
        """
        results = []
        query_lower = query.lower()

        all_memories = self._get_accessible_memories(contract)

        for memory in all_memories:
            if field:
                # Search specific field
                if field in memory.content:
                    value = str(memory.content[field])
                    if query_lower in value.lower():
                        results.append(memory)
            else:
                # Search all fields
                content_str = str(memory.content).lower()
                if query_lower in content_str:
                    results.append(memory)

        return results

    def search_by_creator(
        self,
        creator_agent_id: str,
        contract: MemoryContract
    ) -> List[MemoryEntry]:
        """
        Search memory by creator.

        Args:
            creator_agent_id: Agent that created the memory
            contract: Memory access contract

        Returns:
            List of memory entries created by this agent
        """
        all_memories = self._get_accessible_memories(contract)
        return [
            memory for memory in all_memories
            if memory.created_by == creator_agent_id
        ]

    def search_by_date_range(
        self,
        start_date: datetime,
        end_date: datetime,
        contract: MemoryContract
    ) -> List[MemoryEntry]:
        """
        Search memory by creation date range.

        Args:
            start_date: Start of date range
            end_date: End of date range
            contract: Memory access contract

        Returns:
            List of memory entries in date range
        """
        all_memories = self._get_accessible_memories(contract)
        return [
            memory for memory in all_memories
            if start_date <= memory.created_at <= end_date
        ]

    def search_promoted_memories(
        self,
        contract: MemoryContract
    ) -> List[MemoryEntry]:
        """
        Find all memories that were promoted from lower tiers.

        Args:
            contract: Memory access contract

        Returns:
            List of promoted memory entries
        """
        all_memories = self._get_accessible_memories(contract)
        return [
            memory for memory in all_memories
            if memory.promoted_from is not None
        ]

    def get_memory_provenance_chain(
        self,
        memory_id: str,
        contract: MemoryContract
    ) -> List[MemoryEntry]:
        """
        Get full provenance chain for a memory (all versions across promotions).

        Args:
            memory_id: Memory identifier
            contract: Memory access contract

        Returns:
            List of memory entries in provenance chain
        """
        chain = []

        # Get starting memory
        try:
            memory = self.memory_store.read(memory_id, contract)
            chain.append(memory)
        except Exception:
            return chain

        # Follow promoted_from chain backwards
        current_id = memory.promoted_from
        while current_id:
            try:
                ancestor = self.memory_store.read(current_id, contract)
                chain.insert(0, ancestor)  # Insert at beginning for chronological order
                current_id = ancestor.promoted_from
            except Exception:
                break

        # Find any memories promoted from this one
        all_memories = self._get_accessible_memories(contract)
        descendants = [
            m for m in all_memories
            if m.promoted_from == memory_id
        ]
        chain.extend(descendants)

        return chain

    def advanced_search(
        self,
        contract: MemoryContract,
        tags: Optional[List[str]] = None,
        content_query: Optional[str] = None,
        creator: Optional[str] = None,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
        levels: Optional[List[MemoryAccessLevel]] = None
    ) -> List[MemoryEntry]:
        """
        Advanced search with multiple filters.

        Args:
            contract: Memory access contract
            tags: Optional tag filter
            content_query: Optional content search query
            creator: Optional creator filter
            start_date: Optional start date
            end_date: Optional end date
            levels: Optional filter by memory access levels

        Returns:
            List of matching memory entries
        """
        results = self._get_accessible_memories(contract)

        # Apply tag filter
        if tags:
            results = [
                m for m in results
                if any(tag in m.tags for tag in tags)
            ]

        # Apply content filter
        if content_query:
            query_lower = content_query.lower()
            results = [
                m for m in results
                if query_lower in str(m.content).lower()
            ]

        # Apply creator filter
        if creator:
            results = [
                m for m in results
                if m.created_by == creator
            ]

        # Apply date range filter
        if start_date:
            results = [
                m for m in results
                if m.created_at >= start_date
            ]
        if end_date:
            results = [
                m for m in results
                if m.created_at <= end_date
            ]

        # Apply level filter
        if levels:
            results = [
                m for m in results
                if m.scope.level in levels
            ]

        return results

    def _get_accessible_memories(
        self,
        contract: MemoryContract
    ) -> List[MemoryEntry]:
        """
        Get all memories accessible by this contract.

        Args:
            contract: Memory access contract

        Returns:
            List of accessible memory entries
        """
        memories = []

        # GAIA tier (if permitted)
        if MemoryAccessLevel.GAIA in contract.read_permissions:
            memories.extend(self.memory_store.get_all_gaia_memory())

        # PROJECT tier (if permitted)
        if MemoryAccessLevel.PROJECT in contract.read_permissions:
            if contract.project_id:
                memories.extend(
                    self.memory_store.get_project_memory(contract.project_id)
                )

        # AGENT tier (if permitted)
        if MemoryAccessLevel.AGENT in contract.read_permissions:
            if contract.agent_id:
                memories.extend(
                    self.memory_store.get_agent_memory(contract.agent_id)
                )

        return memories
