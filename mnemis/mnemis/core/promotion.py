"""
Memory promotion engine for MNEMIS.

Manages the proposal and approval workflow for promoting memory
from lower to higher tiers in the hierarchy.
"""

from typing import Dict, List, Optional
from datetime import datetime
import uuid

from mnemis.models.memory_models import (
    MemoryEntry,
    MemoryPromotionProposal,
    MemoryScope,
    MemoryAccessLevel,
    MemoryAccessViolation,
)
from mnemis.core.memory_store import MnemisStore
from mnemis.core.contracts import MemoryAccessController


class MemoryPromotionEngine:
    """
    Manages memory promotion from lower to higher tiers.

    Constitutional principles:
    - Memory moves UP hierarchy via proposal only
    - All promotions require explicit approval
    - Provenance tracked at every step
    - Rejected proposals are logged (not discarded)
    """

    def __init__(
        self,
        memory_store: MnemisStore,
        access_controller: MemoryAccessController
    ):
        """
        Initialize promotion engine.

        Args:
            memory_store: Memory store instance
            access_controller: Access controller instance
        """
        self.memory_store = memory_store
        self.access_controller = access_controller
        self._proposals: Dict[str, MemoryPromotionProposal] = {}

    def propose_promotion(
        self,
        memory_id: str,
        to_scope: MemoryScope,
        agent_id: str,
        rationale: str
    ) -> str:
        """
        Propose promoting memory to higher tier.

        Args:
            memory_id: Memory to promote
            to_scope: Target memory scope
            agent_id: Agent making the proposal
            rationale: Human-readable explanation

        Returns:
            Proposal ID

        Raises:
            MemoryAccessViolation: If agent cannot propose promotion
            KeyError: If memory not found
        """
        # Locate memory
        memory = self.memory_store._locate_memory(memory_id)

        # Validate promotion authority
        self.access_controller.validate_promotion_proposal(
            agent_id=agent_id,
            from_scope=memory.scope,
            to_scope=to_scope
        )

        # Create proposal
        proposal_id = str(uuid.uuid4())
        proposal = MemoryPromotionProposal(
            id=proposal_id,
            memory_id=memory_id,
            from_scope=memory.scope,
            to_scope=to_scope,
            rationale=rationale,
            proposed_by=agent_id
        )

        self._proposals[proposal_id] = proposal

        # Add provenance to memory
        memory.add_provenance_event(
            event_type="promotion_proposed",
            actor=agent_id,
            details={
                "proposal_id": proposal_id,
                "from_level": memory.scope.level.value,
                "to_level": to_scope.level.value,
                "rationale": rationale
            }
        )

        return proposal_id

    def approve_promotion(
        self,
        proposal_id: str,
        reviewer: str,
        notes: Optional[str] = None
    ) -> str:
        """
        Approve memory promotion proposal.

        Args:
            proposal_id: Proposal identifier
            reviewer: Who approved the proposal
            notes: Optional review notes

        Returns:
            Promoted memory ID

        Raises:
            KeyError: If proposal not found
        """
        if proposal_id not in self._proposals:
            raise KeyError(f"Proposal {proposal_id} not found")

        proposal = self._proposals[proposal_id]

        # Approve proposal
        proposal.approve(reviewer=reviewer, notes=notes)

        # Execute promotion
        promoted_memory_id = self._execute_promotion(proposal, reviewer)

        return promoted_memory_id

    def reject_promotion(
        self,
        proposal_id: str,
        reviewer: str,
        notes: str
    ) -> None:
        """
        Reject memory promotion proposal.

        Args:
            proposal_id: Proposal identifier
            reviewer: Who rejected the proposal
            notes: Reason for rejection (required)

        Raises:
            KeyError: If proposal not found
        """
        if proposal_id not in self._proposals:
            raise KeyError(f"Proposal {proposal_id} not found")

        proposal = self._proposals[proposal_id]

        # Reject proposal
        proposal.reject(reviewer=reviewer, notes=notes)

        # Add rejection to memory provenance
        try:
            memory = self.memory_store._locate_memory(proposal.memory_id)
            memory.add_provenance_event(
                event_type="promotion_rejected",
                actor=reviewer,
                details={
                    "proposal_id": proposal_id,
                    "reason": notes
                }
            )
        except KeyError:
            # Memory might have been deleted
            pass

    def _execute_promotion(
        self,
        proposal: MemoryPromotionProposal,
        reviewer: str
    ) -> str:
        """
        Execute approved memory promotion.

        Args:
            proposal: Approved promotion proposal
            reviewer: Who approved the promotion

        Returns:
            Promoted memory ID
        """
        # Get source memory
        source_memory = self.memory_store._locate_memory(proposal.memory_id)

        # Create promoted memory entry
        promoted_memory_id = str(uuid.uuid4())
        promoted_memory = MemoryEntry(
            id=promoted_memory_id,
            content=source_memory.content.copy(),
            scope=proposal.to_scope,
            created_by=source_memory.created_by,
            created_at=datetime.utcnow(),
            promoted_from=proposal.memory_id,
            tags=source_memory.tags.copy(),
            metadata=source_memory.metadata.copy(),
            provenance=source_memory.provenance.copy()
        )

        # Add promotion event
        promoted_memory.add_provenance_event(
            event_type="promoted",
            actor=reviewer,
            details={
                "proposal_id": proposal.id,
                "from_level": proposal.from_scope.level.value,
                "to_level": proposal.to_scope.level.value,
                "original_memory_id": proposal.memory_id,
                "rationale": proposal.rationale
            }
        )

        # Store promoted memory
        self.memory_store._store_memory(promoted_memory)

        # Update source memory provenance
        source_memory.add_provenance_event(
            event_type="promoted_to_higher_tier",
            actor=reviewer,
            details={
                "promoted_memory_id": promoted_memory_id,
                "new_level": proposal.to_scope.level.value
            }
        )

        return promoted_memory_id

    def get_proposal(self, proposal_id: str) -> MemoryPromotionProposal:
        """
        Get promotion proposal by ID.

        Args:
            proposal_id: Proposal identifier

        Returns:
            Promotion proposal

        Raises:
            KeyError: If proposal not found
        """
        if proposal_id not in self._proposals:
            raise KeyError(f"Proposal {proposal_id} not found")
        return self._proposals[proposal_id]

    def get_pending_proposals(
        self,
        to_level: Optional[MemoryAccessLevel] = None
    ) -> List[MemoryPromotionProposal]:
        """
        Get all pending promotion proposals.

        Args:
            to_level: Optional filter by target level

        Returns:
            List of pending proposals
        """
        proposals = [
            p for p in self._proposals.values()
            if p.status == "pending"
        ]

        if to_level:
            proposals = [
                p for p in proposals
                if p.to_scope.level == to_level
            ]

        return proposals

    def get_gaia_promotion_queue(self) -> List[MemoryPromotionProposal]:
        """
        Get pending proposals for GAIA tier promotion.

        These require human/GAIA-level approval.

        Returns:
            List of pending GAIA promotions
        """
        return self.get_pending_proposals(to_level=MemoryAccessLevel.GAIA)

    def get_project_promotion_queue(
        self,
        project_id: str
    ) -> List[MemoryPromotionProposal]:
        """
        Get pending proposals for PROJECT tier promotion within a project.

        Args:
            project_id: Project identifier

        Returns:
            List of pending PROJECT promotions for this project
        """
        proposals = self.get_pending_proposals(to_level=MemoryAccessLevel.PROJECT)
        return [
            p for p in proposals
            if p.to_scope.project_id == project_id
        ]
