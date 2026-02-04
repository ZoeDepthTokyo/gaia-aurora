"""
Execution context for workflow runs.

Tracks state, results, and audit trail for a single workflow execution.
"""

from typing import Dict, Any, List, Optional, Set
from datetime import datetime
from pydantic import BaseModel, Field

from loom.models.agent_models import AgentExecutionRecord, AgentExecutionState


class ExecutionContext(BaseModel):
    """
    Context for a single workflow execution.

    Provides auditability and observability for all workflow runs.

    Attributes:
        execution_id: Unique execution identifier
        workflow_id: Workflow being executed
        workflow_name: Workflow name
        started_at: Execution start time
        completed_at: Execution completion time
        execution_records: Agent execution records
        errors: Execution errors
        total_cost: Cumulative cost
        execution_count: Number of agent executions
        dry_run: Whether this is a dry run
        approvals: Agent IDs with human approval
    """
    execution_id: str = Field(default_factory=lambda: __import__('uuid').uuid4().hex)
    workflow_id: str
    workflow_name: str
    started_at: datetime = Field(default_factory=datetime.utcnow)
    completed_at: Optional[datetime] = None
    execution_records: List[AgentExecutionRecord] = Field(default_factory=list)
    errors: List[Dict[str, Any]] = Field(default_factory=list)
    total_cost: float = 0.0
    execution_count: int = 0
    dry_run: bool = False
    approvals: Set[str] = Field(default_factory=set)

    class Config:
        """Pydantic config."""
        arbitrary_types_allowed = True

    def add_execution_record(self, record: AgentExecutionRecord) -> None:
        """
        Add agent execution record.

        Args:
            record: Execution record to add
        """
        self.execution_records.append(record)
        self.execution_count += 1

        # Update cost if metadata available
        if record.outputs and "cost" in record.outputs:
            self.total_cost += record.outputs["cost"]

    def record_error(self, agent_id: str, error: Optional[str]) -> None:
        """
        Record execution error.

        Args:
            agent_id: Agent that errored
            error: Error message
        """
        self.errors.append({
            "agent_id": agent_id,
            "error": error,
            "timestamp": datetime.utcnow().isoformat()
        })

    def complete(self) -> None:
        """Mark execution as completed."""
        self.completed_at = datetime.utcnow()

    def has_approval(self, agent_id: str) -> bool:
        """
        Check if agent has human approval.

        Args:
            agent_id: Agent identifier

        Returns:
            True if approved
        """
        return agent_id in self.approvals

    def grant_approval(self, agent_id: str) -> None:
        """
        Grant human approval for agent execution.

        Args:
            agent_id: Agent identifier
        """
        self.approvals.add(agent_id)

    def get_agent_record(self, agent_id: str) -> Optional[AgentExecutionRecord]:
        """
        Get execution record for agent.

        Args:
            agent_id: Agent identifier

        Returns:
            Execution record or None
        """
        for record in self.execution_records:
            if record.agent_id == agent_id:
                return record
        return None

    def get_successful_executions(self) -> List[AgentExecutionRecord]:
        """
        Get all successful agent executions.

        Returns:
            List of successful execution records
        """
        return [
            record for record in self.execution_records
            if record.state == AgentExecutionState.COMPLETED
        ]

    def get_failed_executions(self) -> List[AgentExecutionRecord]:
        """
        Get all failed agent executions.

        Returns:
            List of failed execution records
        """
        return [
            record for record in self.execution_records
            if record.state == AgentExecutionState.FAILED
        ]

    def has_errors(self) -> bool:
        """
        Check if execution has any errors.

        Returns:
            True if errors occurred
        """
        return len(self.errors) > 0 or len(self.get_failed_executions()) > 0

    def get_summary(self) -> Dict[str, Any]:
        """
        Get execution summary.

        Returns:
            Summary dictionary
        """
        duration = None
        if self.completed_at:
            duration = (self.completed_at - self.started_at).total_seconds()

        return {
            "execution_id": self.execution_id,
            "workflow_id": self.workflow_id,
            "workflow_name": self.workflow_name,
            "started_at": self.started_at.isoformat(),
            "completed_at": self.completed_at.isoformat() if self.completed_at else None,
            "duration_seconds": duration,
            "total_executions": self.execution_count,
            "successful_executions": len(self.get_successful_executions()),
            "failed_executions": len(self.get_failed_executions()),
            "total_cost": self.total_cost,
            "has_errors": self.has_errors(),
            "dry_run": self.dry_run
        }
