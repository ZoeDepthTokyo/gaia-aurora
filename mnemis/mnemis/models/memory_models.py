"""
Memory data models and access contracts for MNEMIS.

Implements constitutional memory hierarchy with enforced boundaries.
"""

from typing import Any, Optional, Dict, List
from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field, field_validator


class MemoryAccessLevel(str, Enum):
    """
    Three-tier memory hierarchy levels.

    GAIA: Ecosystem-wide, eternal, cross-project patterns
    PROJECT: Project-scoped, persistent within project lifecycle
    AGENT: Execution-scoped, ephemeral, auto-expire after session
    """
    GAIA = "gaia"
    PROJECT = "project"
    AGENT = "agent"


class MemoryScope(BaseModel):
    """
    Defines the visibility and persistence scope for a memory entry.

    Attributes:
        level: Access level (GAIA/PROJECT/AGENT)
        project_id: Project identifier (if PROJECT or AGENT level)
        agent_id: Agent identifier (if AGENT level)
        auto_expire: Whether memory auto-expires (AGENT level only)
        ttl_seconds: Time-to-live in seconds for ephemeral memory
    """
    level: MemoryAccessLevel
    project_id: Optional[str] = None
    agent_id: Optional[str] = None
    auto_expire: bool = False
    ttl_seconds: Optional[int] = None

    @field_validator('project_id')
    @classmethod
    def validate_project_id(cls, v: Optional[str], info) -> Optional[str]:
        """Validate project_id is set for PROJECT and AGENT levels."""
        level = info.data.get('level')
        if level in [MemoryAccessLevel.PROJECT, MemoryAccessLevel.AGENT] and not v:
            raise ValueError(f"project_id required for {level} level memory")
        return v

    @field_validator('agent_id')
    @classmethod
    def validate_agent_id(cls, v: Optional[str], info) -> Optional[str]:
        """Validate agent_id is set for AGENT level."""
        level = info.data.get('level')
        if level == MemoryAccessLevel.AGENT and not v:
            raise ValueError("agent_id required for AGENT level memory")
        return v

    @field_validator('auto_expire')
    @classmethod
    def validate_auto_expire(cls, v: bool, info) -> bool:
        """AGENT level memory always auto-expires."""
        level = info.data.get('level')
        if level == MemoryAccessLevel.AGENT:
            return True
        return v


class MemoryEntry(BaseModel):
    """
    Single memory entry with full provenance tracking.

    Attributes:
        id: Unique memory identifier
        content: Memory content (arbitrary JSON structure)
        scope: Memory visibility scope
        created_by: Agent/system that created this memory
        created_at: Creation timestamp
        updated_at: Last update timestamp
        promoted_from: Source memory ID if promoted from lower tier
        tags: Searchable tags
        metadata: Additional metadata
        provenance: Full audit trail
    """
    id: str
    content: Dict[str, Any]
    scope: MemoryScope
    created_by: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    promoted_from: Optional[str] = None
    tags: List[str] = Field(default_factory=list)
    metadata: Dict[str, Any] = Field(default_factory=dict)
    provenance: List[Dict[str, Any]] = Field(default_factory=list)

    def add_provenance_event(self, event_type: str, actor: str, details: Dict[str, Any]) -> None:
        """
        Add provenance tracking event.

        Args:
            event_type: Type of event (created, promoted, updated, accessed)
            actor: Agent/system performing the action
            details: Event-specific details
        """
        self.provenance.append({
            "event_type": event_type,
            "actor": actor,
            "timestamp": datetime.utcnow().isoformat(),
            "details": details
        })
        self.updated_at = datetime.utcnow()

    def is_expired(self) -> bool:
        """Check if ephemeral memory has expired."""
        if not self.scope.auto_expire or not self.scope.ttl_seconds:
            return False

        age_seconds = (datetime.utcnow() - self.created_at).total_seconds()
        return age_seconds > self.scope.ttl_seconds


class MemoryContract(BaseModel):
    """
    Enforces memory boundary constraints for agents.

    Constitutional principle: Agents can read down the hierarchy,
    but can only write at their exact level.

    Attributes:
        agent_id: Agent identifier
        access_level: Agent's access tier
        project_id: Project context (if applicable)
        read_permissions: Explicit read permissions
        write_permissions: Explicit write permissions
    """
    agent_id: str
    access_level: MemoryAccessLevel
    project_id: Optional[str] = None
    read_permissions: List[MemoryAccessLevel] = Field(default_factory=list)
    write_permissions: List[MemoryAccessLevel] = Field(default_factory=list)

    def __init__(self, **data):
        """Initialize contract with default permissions based on access level."""
        super().__init__(**data)
        if not self.read_permissions:
            self.read_permissions = self._default_read_permissions()
        if not self.write_permissions:
            self.write_permissions = self._default_write_permissions()

    def _default_read_permissions(self) -> List[MemoryAccessLevel]:
        """
        Default read permissions: can read at level and below.

        GAIA agents can read: GAIA, PROJECT, AGENT
        PROJECT agents can read: PROJECT, AGENT
        AGENT can read: AGENT only
        """
        hierarchy = {
            MemoryAccessLevel.GAIA: [
                MemoryAccessLevel.GAIA,
                MemoryAccessLevel.PROJECT,
                MemoryAccessLevel.AGENT
            ],
            MemoryAccessLevel.PROJECT: [
                MemoryAccessLevel.PROJECT,
                MemoryAccessLevel.AGENT
            ],
            MemoryAccessLevel.AGENT: [
                MemoryAccessLevel.AGENT
            ]
        }
        return hierarchy[self.access_level]

    def _default_write_permissions(self) -> List[MemoryAccessLevel]:
        """
        Default write permissions: can only write at exact level.

        Prevents accidental cross-tier contamination.
        """
        return [self.access_level]

    def can_read(self, memory_scope: MemoryScope) -> bool:
        """
        Check if agent can read memory at given scope.

        Args:
            memory_scope: Memory scope to check

        Returns:
            True if read is allowed
        """
        return memory_scope.level in self.read_permissions

    def can_write(self, memory_scope: MemoryScope) -> bool:
        """
        Check if agent can write to memory at given scope.

        Args:
            memory_scope: Memory scope to check

        Returns:
            True if write is allowed
        """
        # Must have write permission for this level
        if memory_scope.level not in self.write_permissions:
            return False

        # PROJECT and AGENT level writes must match project context
        if memory_scope.level in [MemoryAccessLevel.PROJECT, MemoryAccessLevel.AGENT]:
            if memory_scope.project_id != self.project_id:
                return False

        # AGENT level writes must match agent context
        if memory_scope.level == MemoryAccessLevel.AGENT:
            if memory_scope.agent_id != self.agent_id:
                return False

        return True

    def can_propose_promotion(self, from_scope: MemoryScope) -> bool:
        """
        Check if agent can propose memory promotion.

        Only PROJECT-level agents can propose to GAIA tier.
        AGENT-level agents can propose to PROJECT tier.

        Args:
            from_scope: Source memory scope

        Returns:
            True if promotion proposal is allowed
        """
        if self.access_level == MemoryAccessLevel.PROJECT:
            return from_scope.level == MemoryAccessLevel.PROJECT

        if self.access_level == MemoryAccessLevel.AGENT:
            return from_scope.level == MemoryAccessLevel.AGENT

        return False


class MemoryPromotionProposal(BaseModel):
    """
    Proposal to promote memory from lower to higher tier.

    Requires explicit approval - no automatic promotions.

    Attributes:
        id: Unique proposal identifier
        memory_id: Memory being proposed for promotion
        from_scope: Current memory scope
        to_scope: Target memory scope
        rationale: Human-readable explanation
        proposed_by: Agent making the proposal
        proposed_at: Proposal timestamp
        status: pending, approved, rejected
        reviewed_by: Who approved/rejected (optional)
        reviewed_at: Review timestamp (optional)
        review_notes: Reviewer comments (optional)
    """
    id: str
    memory_id: str
    from_scope: MemoryScope
    to_scope: MemoryScope
    rationale: str
    proposed_by: str
    proposed_at: datetime = Field(default_factory=datetime.utcnow)
    status: str = "pending"  # pending, approved, rejected
    reviewed_by: Optional[str] = None
    reviewed_at: Optional[datetime] = None
    review_notes: Optional[str] = None

    @field_validator('status')
    @classmethod
    def validate_status(cls, v: str) -> str:
        """Validate status is one of allowed values."""
        allowed = ["pending", "approved", "rejected"]
        if v not in allowed:
            raise ValueError(f"status must be one of {allowed}")
        return v

    def approve(self, reviewer: str, notes: Optional[str] = None) -> None:
        """
        Approve promotion proposal.

        Args:
            reviewer: Who approved the proposal
            notes: Optional review notes
        """
        self.status = "approved"
        self.reviewed_by = reviewer
        self.reviewed_at = datetime.utcnow()
        self.review_notes = notes

    def reject(self, reviewer: str, notes: str) -> None:
        """
        Reject promotion proposal.

        Args:
            reviewer: Who rejected the proposal
            notes: Reason for rejection (required)
        """
        self.status = "rejected"
        self.reviewed_by = reviewer
        self.reviewed_at = datetime.utcnow()
        self.review_notes = notes


class MemoryAccessViolation(Exception):
    """
    Raised when agent attempts unauthorized memory access.

    Constitutional principle: All violations must be explicit and logged.
    """
    pass
