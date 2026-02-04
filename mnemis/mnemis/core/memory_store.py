"""
Core memory storage and retrieval engine for MNEMIS.

Enforces access contracts and tracks provenance for all memory operations.
"""

import json
from typing import Dict, List, Optional
from pathlib import Path
from datetime import datetime
import uuid

from mnemis.models.memory_models import (
    MemoryEntry,
    MemoryContract,
    MemoryScope,
    MemoryAccessLevel,
    MemoryAccessViolation,
)


class MnemisStore:
    """
    Cross-project memory store with enforced access contracts.

    Stores three tiers of memory with different persistence guarantees:
    - GAIA: Eternal, ecosystem-wide (stored in _gaia/mnemis/)
    - PROJECT: Persistent, project-scoped (stored in project/memory/)
    - AGENT: Ephemeral, auto-expire (in-memory with optional persistence)

    All operations enforce memory contracts to prevent unauthorized access.
    """

    def __init__(self, base_path: Optional[Path] = None):
        """
        Initialize memory store.

        Args:
            base_path: Base directory for persistent storage
                      (defaults to X:/Projects/_gaia/mnemis/)
        """
        if base_path is None:
            base_path = Path("X:/Projects/_gaia/mnemis/shared_memory")

        self.base_path = Path(base_path)
        self.base_path.mkdir(parents=True, exist_ok=True)

        # In-memory caches
        self.gaia_memory: Dict[str, MemoryEntry] = {}
        self.project_memory: Dict[str, Dict[str, MemoryEntry]] = {}
        self.agent_memory: Dict[str, MemoryEntry] = {}

        # Load persistent memory
        self._load_persistent_memory()

    def _load_persistent_memory(self) -> None:
        """Load GAIA and PROJECT tier memory from disk."""
        # Load GAIA tier
        gaia_file = self.base_path / "gaia_memory.jsonl"
        if gaia_file.exists():
            with open(gaia_file, 'r', encoding='utf-8') as f:
                for line in f:
                    if line.strip():
                        entry_dict = json.loads(line)
                        entry = MemoryEntry(**entry_dict)
                        self.gaia_memory[entry.id] = entry

        # Load PROJECT tier (organized by project)
        project_dir = self.base_path / "projects"
        if project_dir.exists():
            for project_file in project_dir.glob("*.jsonl"):
                project_id = project_file.stem
                self.project_memory[project_id] = {}

                with open(project_file, 'r', encoding='utf-8') as f:
                    for line in f:
                        if line.strip():
                            entry_dict = json.loads(line)
                            entry = MemoryEntry(**entry_dict)
                            self.project_memory[project_id][entry.id] = entry

    def _persist_gaia_memory(self) -> None:
        """Persist GAIA tier memory to disk."""
        gaia_file = self.base_path / "gaia_memory.jsonl"
        with open(gaia_file, 'w', encoding='utf-8') as f:
            for entry in self.gaia_memory.values():
                f.write(entry.model_dump_json() + '\n')

    def _persist_project_memory(self, project_id: str) -> None:
        """
        Persist PROJECT tier memory to disk.

        Args:
            project_id: Project identifier
        """
        project_dir = self.base_path / "projects"
        project_dir.mkdir(parents=True, exist_ok=True)

        project_file = project_dir / f"{project_id}.jsonl"
        if project_id in self.project_memory:
            with open(project_file, 'w', encoding='utf-8') as f:
                for entry in self.project_memory[project_id].values():
                    f.write(entry.model_dump_json() + '\n')

    def read(
        self,
        memory_id: str,
        contract: MemoryContract
    ) -> MemoryEntry:
        """
        Read memory with contract enforcement.

        Args:
            memory_id: Memory identifier
            contract: Memory access contract

        Returns:
            Memory entry

        Raises:
            MemoryAccessViolation: If contract doesn't allow read
            KeyError: If memory not found
        """
        # Locate memory
        memory = self._locate_memory(memory_id)

        # Enforce read contract
        if not contract.can_read(memory.scope):
            raise MemoryAccessViolation(
                f"Agent {contract.agent_id} at {contract.access_level} level "
                f"cannot read {memory.scope.level} memory"
            )

        # Track access in provenance
        memory.add_provenance_event(
            event_type="accessed",
            actor=contract.agent_id,
            details={"access_level": contract.access_level.value}
        )

        return memory

    def write(
        self,
        content: Dict,
        scope: MemoryScope,
        contract: MemoryContract,
        tags: Optional[List[str]] = None,
        metadata: Optional[Dict] = None
    ) -> str:
        """
        Write memory with contract enforcement.

        Args:
            content: Memory content
            scope: Memory scope
            contract: Memory access contract
            tags: Optional tags for searchability
            metadata: Optional metadata

        Returns:
            Memory ID

        Raises:
            MemoryAccessViolation: If contract doesn't allow write
        """
        # Enforce write contract
        if not contract.can_write(scope):
            raise MemoryAccessViolation(
                f"Agent {contract.agent_id} at {contract.access_level} level "
                f"cannot write to {scope.level} memory"
            )

        # Create memory entry
        memory_id = str(uuid.uuid4())
        memory = MemoryEntry(
            id=memory_id,
            content=content,
            scope=scope,
            created_by=contract.agent_id,
            tags=tags or [],
            metadata=metadata or {}
        )

        # Add creation provenance
        memory.add_provenance_event(
            event_type="created",
            actor=contract.agent_id,
            details={
                "access_level": contract.access_level.value,
                "scope_level": scope.level.value
            }
        )

        # Store in appropriate tier
        self._store_memory(memory)

        return memory_id

    def update(
        self,
        memory_id: str,
        content: Dict,
        contract: MemoryContract,
        tags: Optional[List[str]] = None,
        metadata: Optional[Dict] = None
    ) -> None:
        """
        Update existing memory with contract enforcement.

        Args:
            memory_id: Memory identifier
            content: Updated content
            contract: Memory access contract
            tags: Optional updated tags
            metadata: Optional updated metadata

        Raises:
            MemoryAccessViolation: If contract doesn't allow write
            KeyError: If memory not found
        """
        # Locate memory
        memory = self._locate_memory(memory_id)

        # Enforce write contract
        if not contract.can_write(memory.scope):
            raise MemoryAccessViolation(
                f"Agent {contract.agent_id} cannot update {memory.scope.level} memory"
            )

        # Update memory
        memory.content = content
        if tags is not None:
            memory.tags = tags
        if metadata is not None:
            memory.metadata = metadata

        # Add update provenance
        memory.add_provenance_event(
            event_type="updated",
            actor=contract.agent_id,
            details={"updated_fields": ["content", "tags", "metadata"]}
        )

        # Persist if not ephemeral
        if memory.scope.level == MemoryAccessLevel.GAIA:
            self._persist_gaia_memory()
        elif memory.scope.level == MemoryAccessLevel.PROJECT:
            self._persist_project_memory(memory.scope.project_id)

    def delete(
        self,
        memory_id: str,
        contract: MemoryContract
    ) -> None:
        """
        Delete memory with contract enforcement.

        Args:
            memory_id: Memory identifier
            contract: Memory access contract

        Raises:
            MemoryAccessViolation: If contract doesn't allow write
            KeyError: If memory not found
        """
        # Locate memory
        memory = self._locate_memory(memory_id)

        # Enforce write contract (delete requires write permission)
        if not contract.can_write(memory.scope):
            raise MemoryAccessViolation(
                f"Agent {contract.agent_id} cannot delete {memory.scope.level} memory"
            )

        # Remove from appropriate tier
        if memory.scope.level == MemoryAccessLevel.GAIA:
            del self.gaia_memory[memory_id]
            self._persist_gaia_memory()
        elif memory.scope.level == MemoryAccessLevel.PROJECT:
            project_id = memory.scope.project_id
            del self.project_memory[project_id][memory_id]
            self._persist_project_memory(project_id)
        elif memory.scope.level == MemoryAccessLevel.AGENT:
            del self.agent_memory[memory_id]

    def cleanup_expired_agent_memory(self) -> int:
        """
        Remove expired ephemeral agent memory.

        Returns:
            Number of memories cleaned up
        """
        expired_ids = [
            memory_id
            for memory_id, memory in self.agent_memory.items()
            if memory.is_expired()
        ]

        for memory_id in expired_ids:
            del self.agent_memory[memory_id]

        return len(expired_ids)

    def _locate_memory(self, memory_id: str) -> MemoryEntry:
        """
        Locate memory across all tiers.

        Args:
            memory_id: Memory identifier

        Returns:
            Memory entry

        Raises:
            KeyError: If memory not found
        """
        # Check GAIA tier
        if memory_id in self.gaia_memory:
            return self.gaia_memory[memory_id]

        # Check PROJECT tier
        for project_memories in self.project_memory.values():
            if memory_id in project_memories:
                return project_memories[memory_id]

        # Check AGENT tier
        if memory_id in self.agent_memory:
            return self.agent_memory[memory_id]

        raise KeyError(f"Memory {memory_id} not found")

    def _store_memory(self, memory: MemoryEntry) -> None:
        """
        Store memory in appropriate tier.

        Args:
            memory: Memory entry to store
        """
        if memory.scope.level == MemoryAccessLevel.GAIA:
            self.gaia_memory[memory.id] = memory
            self._persist_gaia_memory()

        elif memory.scope.level == MemoryAccessLevel.PROJECT:
            project_id = memory.scope.project_id
            if project_id not in self.project_memory:
                self.project_memory[project_id] = {}
            self.project_memory[project_id][memory.id] = memory
            self._persist_project_memory(project_id)

        elif memory.scope.level == MemoryAccessLevel.AGENT:
            self.agent_memory[memory.id] = memory

    def get_all_gaia_memory(self) -> List[MemoryEntry]:
        """
        Get all GAIA tier memory.

        Returns:
            List of GAIA-level memory entries
        """
        return list(self.gaia_memory.values())

    def get_project_memory(self, project_id: str) -> List[MemoryEntry]:
        """
        Get all memory for a specific project.

        Args:
            project_id: Project identifier

        Returns:
            List of project memory entries
        """
        return list(self.project_memory.get(project_id, {}).values())

    def get_agent_memory(self, agent_id: str) -> List[MemoryEntry]:
        """
        Get all memory for a specific agent.

        Args:
            agent_id: Agent identifier

        Returns:
            List of agent memory entries
        """
        return [
            memory
            for memory in self.agent_memory.values()
            if memory.scope.agent_id == agent_id
        ]
