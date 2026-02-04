"""
Memory access control and contract enforcement.

Ensures agents respect constitutional boundaries on memory access.
"""

from typing import Dict, Optional
from mnemis.models.memory_models import (
    MemoryContract,
    MemoryAccessLevel,
    MemoryScope,
    MemoryAccessViolation,
)


class MemoryAccessController:
    """
    Centralized access control for memory operations.

    Enforces constitutional principles:
    - Read down the hierarchy (GAIA can read PROJECT/AGENT, etc.)
    - Write only at exact level
    - No cross-project contamination
    - Explicit promotion required for tier changes
    """

    def __init__(self):
        """Initialize access controller."""
        self._contracts: Dict[str, MemoryContract] = {}

    def register_agent(
        self,
        agent_id: str,
        access_level: MemoryAccessLevel,
        project_id: Optional[str] = None
    ) -> MemoryContract:
        """
        Register agent and create memory contract.

        Args:
            agent_id: Agent identifier
            access_level: Agent's access tier
            project_id: Project context (required for PROJECT/AGENT level)

        Returns:
            Memory contract for this agent

        Raises:
            ValueError: If project_id missing for PROJECT/AGENT level
        """
        if access_level in [MemoryAccessLevel.PROJECT, MemoryAccessLevel.AGENT]:
            if not project_id:
                raise ValueError(
                    f"{access_level} level agent requires project_id"
                )

        contract = MemoryContract(
            agent_id=agent_id,
            access_level=access_level,
            project_id=project_id
        )

        self._contracts[agent_id] = contract
        return contract

    def get_contract(self, agent_id: str) -> MemoryContract:
        """
        Get memory contract for agent.

        Args:
            agent_id: Agent identifier

        Returns:
            Memory contract

        Raises:
            KeyError: If agent not registered
        """
        if agent_id not in self._contracts:
            raise KeyError(f"Agent {agent_id} not registered with access controller")
        return self._contracts[agent_id]

    def validate_read(
        self,
        agent_id: str,
        memory_scope: MemoryScope
    ) -> None:
        """
        Validate if agent can read memory at given scope.

        Args:
            agent_id: Agent identifier
            memory_scope: Memory scope to read

        Raises:
            MemoryAccessViolation: If read not allowed
        """
        contract = self.get_contract(agent_id)
        if not contract.can_read(memory_scope):
            raise MemoryAccessViolation(
                f"Agent {agent_id} at {contract.access_level} level "
                f"cannot read {memory_scope.level} memory"
            )

    def validate_write(
        self,
        agent_id: str,
        memory_scope: MemoryScope
    ) -> None:
        """
        Validate if agent can write memory at given scope.

        Args:
            agent_id: Agent identifier
            memory_scope: Memory scope to write

        Raises:
            MemoryAccessViolation: If write not allowed
        """
        contract = self.get_contract(agent_id)
        if not contract.can_write(memory_scope):
            raise MemoryAccessViolation(
                f"Agent {agent_id} at {contract.access_level} level "
                f"cannot write to {memory_scope.level} memory"
            )

    def validate_promotion_proposal(
        self,
        agent_id: str,
        from_scope: MemoryScope,
        to_scope: MemoryScope
    ) -> None:
        """
        Validate if agent can propose memory promotion.

        Args:
            agent_id: Agent identifier
            from_scope: Source memory scope
            to_scope: Target memory scope

        Raises:
            MemoryAccessViolation: If promotion proposal not allowed
        """
        contract = self.get_contract(agent_id)

        # Validate promotion path
        if not self._is_valid_promotion_path(from_scope, to_scope):
            raise MemoryAccessViolation(
                f"Invalid promotion path: {from_scope.level} -> {to_scope.level}"
            )

        # Validate agent authority
        if not contract.can_propose_promotion(from_scope):
            raise MemoryAccessViolation(
                f"Agent {agent_id} at {contract.access_level} level "
                f"cannot propose promotion from {from_scope.level}"
            )

    def _is_valid_promotion_path(
        self,
        from_scope: MemoryScope,
        to_scope: MemoryScope
    ) -> bool:
        """
        Check if promotion path is valid.

        Valid paths:
        - AGENT -> PROJECT (within same project)
        - PROJECT -> GAIA

        Invalid paths:
        - AGENT -> GAIA (must go through PROJECT)
        - Any downward promotion
        - Cross-project promotion

        Args:
            from_scope: Source memory scope
            to_scope: Target memory scope

        Returns:
            True if valid promotion path
        """
        # Define hierarchy
        hierarchy = {
            MemoryAccessLevel.GAIA: 3,
            MemoryAccessLevel.PROJECT: 2,
            MemoryAccessLevel.AGENT: 1
        }

        # Must be upward promotion
        if hierarchy[to_scope.level] <= hierarchy[from_scope.level]:
            return False

        # AGENT -> PROJECT: must be same project
        if from_scope.level == MemoryAccessLevel.AGENT and \
           to_scope.level == MemoryAccessLevel.PROJECT:
            return from_scope.project_id == to_scope.project_id

        # PROJECT -> GAIA: allowed
        if from_scope.level == MemoryAccessLevel.PROJECT and \
           to_scope.level == MemoryAccessLevel.GAIA:
            return True

        # AGENT -> GAIA: not allowed (must go through PROJECT)
        if from_scope.level == MemoryAccessLevel.AGENT and \
           to_scope.level == MemoryAccessLevel.GAIA:
            return False

        return False

    def create_agent_scope(
        self,
        agent_id: str,
        project_id: str,
        auto_expire: bool = True,
        ttl_seconds: int = 3600
    ) -> MemoryScope:
        """
        Create memory scope for agent-level memory.

        Args:
            agent_id: Agent identifier
            project_id: Project identifier
            auto_expire: Whether memory auto-expires
            ttl_seconds: Time-to-live in seconds (default: 1 hour)

        Returns:
            Memory scope for agent memory
        """
        return MemoryScope(
            level=MemoryAccessLevel.AGENT,
            project_id=project_id,
            agent_id=agent_id,
            auto_expire=auto_expire,
            ttl_seconds=ttl_seconds
        )

    def create_project_scope(self, project_id: str) -> MemoryScope:
        """
        Create memory scope for project-level memory.

        Args:
            project_id: Project identifier

        Returns:
            Memory scope for project memory
        """
        return MemoryScope(
            level=MemoryAccessLevel.PROJECT,
            project_id=project_id
        )

    def create_gaia_scope(self) -> MemoryScope:
        """
        Create memory scope for GAIA-level memory.

        Returns:
            Memory scope for GAIA memory
        """
        return MemoryScope(level=MemoryAccessLevel.GAIA)
