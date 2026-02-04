"""
ARGUS telemetry hooks for MNEMIS memory operations.

Provides structured logging for memory access patterns and violations.
"""

from typing import Dict, Any, Optional
from datetime import datetime
import json
from pathlib import Path

from mnemis.models.memory_models import (
    MemoryEntry,
    MemoryPromotionProposal,
    MemoryAccessViolation,
)


class MemoryTelemetryHooks:
    """
    Telemetry hooks for ARGUS integration.

    Logs all memory operations in JSONL format for ARGUS dashboard.
    """

    def __init__(self, log_dir: Optional[Path] = None):
        """
        Initialize telemetry hooks.

        Args:
            log_dir: Directory for telemetry logs
                    (defaults to X:/Projects/_gaia/logs/mnemis/)
        """
        if log_dir is None:
            log_dir = Path("X:/Projects/_gaia/logs/mnemis")

        self.log_dir = Path(log_dir)
        self.log_dir.mkdir(parents=True, exist_ok=True)

        self.memory_ops_log = self.log_dir / "memory_operations.jsonl"
        self.access_violations_log = self.log_dir / "access_violations.jsonl"
        self.promotions_log = self.log_dir / "promotions.jsonl"

    def log_memory_read(
        self,
        memory_id: str,
        agent_id: str,
        access_level: str,
        memory_level: str,
        success: bool
    ) -> None:
        """
        Log memory read operation.

        Args:
            memory_id: Memory identifier
            agent_id: Agent performing read
            access_level: Agent's access level
            memory_level: Memory tier level
            success: Whether read succeeded
        """
        self._write_log(
            self.memory_ops_log,
            {
                "event_type": "memory_read",
                "memory_id": memory_id,
                "agent_id": agent_id,
                "access_level": access_level,
                "memory_level": memory_level,
                "success": success,
                "timestamp": datetime.utcnow().isoformat()
            }
        )

    def log_memory_write(
        self,
        memory_id: str,
        agent_id: str,
        access_level: str,
        memory_level: str,
        tags: list,
        success: bool
    ) -> None:
        """
        Log memory write operation.

        Args:
            memory_id: Memory identifier
            agent_id: Agent performing write
            access_level: Agent's access level
            memory_level: Memory tier level
            tags: Memory tags
            success: Whether write succeeded
        """
        self._write_log(
            self.memory_ops_log,
            {
                "event_type": "memory_write",
                "memory_id": memory_id,
                "agent_id": agent_id,
                "access_level": access_level,
                "memory_level": memory_level,
                "tags": tags,
                "success": success,
                "timestamp": datetime.utcnow().isoformat()
            }
        )

    def log_access_violation(
        self,
        agent_id: str,
        violation_type: str,
        details: Dict[str, Any]
    ) -> None:
        """
        Log memory access violation.

        Args:
            agent_id: Agent that violated access
            violation_type: Type of violation
            details: Violation details
        """
        self._write_log(
            self.access_violations_log,
            {
                "event_type": "access_violation",
                "agent_id": agent_id,
                "violation_type": violation_type,
                "details": details,
                "timestamp": datetime.utcnow().isoformat()
            }
        )

    def log_promotion_proposal(
        self,
        proposal: MemoryPromotionProposal
    ) -> None:
        """
        Log memory promotion proposal.

        Args:
            proposal: Promotion proposal
        """
        self._write_log(
            self.promotions_log,
            {
                "event_type": "promotion_proposed",
                "proposal_id": proposal.id,
                "memory_id": proposal.memory_id,
                "from_level": proposal.from_scope.level.value,
                "to_level": proposal.to_scope.level.value,
                "proposed_by": proposal.proposed_by,
                "rationale": proposal.rationale,
                "timestamp": datetime.utcnow().isoformat()
            }
        )

    def log_promotion_decision(
        self,
        proposal: MemoryPromotionProposal,
        approved: bool,
        reviewer: str,
        notes: Optional[str] = None
    ) -> None:
        """
        Log promotion approval/rejection.

        Args:
            proposal: Promotion proposal
            approved: Whether approved
            reviewer: Who made the decision
            notes: Decision notes
        """
        self._write_log(
            self.promotions_log,
            {
                "event_type": "promotion_approved" if approved else "promotion_rejected",
                "proposal_id": proposal.id,
                "memory_id": proposal.memory_id,
                "from_level": proposal.from_scope.level.value,
                "to_level": proposal.to_scope.level.value,
                "reviewed_by": reviewer,
                "notes": notes,
                "timestamp": datetime.utcnow().isoformat()
            }
        )

    def _write_log(self, log_file: Path, data: Dict[str, Any]) -> None:
        """
        Write log entry to JSONL file.

        Args:
            log_file: Log file path
            data: Log entry data
        """
        with open(log_file, 'a', encoding='utf-8') as f:
            f.write(json.dumps(data) + '\n')
