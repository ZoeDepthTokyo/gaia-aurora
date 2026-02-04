"""
ARGUS telemetry hooks for LOOM workflow execution.

Provides structured logging for workflow execution and agent tracing.
"""

from typing import Dict, Any, Optional
from datetime import datetime
import json
from pathlib import Path

from loom.models.agent_models import AgentExecutionRecord
from loom.core.execution_context import ExecutionContext


class WorkflowTelemetryHooks:
    """
    Telemetry hooks for ARGUS integration.

    Logs all workflow and agent execution in JSONL format for ARGUS dashboard.
    """

    def __init__(self, log_dir: Optional[Path] = None):
        """
        Initialize telemetry hooks.

        Args:
            log_dir: Directory for telemetry logs
                    (defaults to X:/Projects/_gaia/logs/loom/)
        """
        if log_dir is None:
            log_dir = Path("X:/Projects/_gaia/logs/loom")

        self.log_dir = Path(log_dir)
        self.log_dir.mkdir(parents=True, exist_ok=True)

        self.workflow_log = self.log_dir / "workflow_executions.jsonl"
        self.agent_log = self.log_dir / "agent_executions.jsonl"
        self.errors_log = self.log_dir / "execution_errors.jsonl"

    def log_workflow_start(
        self,
        workflow_id: str,
        workflow_name: str,
        execution_id: str
    ) -> None:
        """
        Log workflow execution start.

        Args:
            workflow_id: Workflow identifier
            workflow_name: Workflow name
            execution_id: Execution identifier
        """
        self._write_log(
            self.workflow_log,
            {
                "event_type": "workflow_started",
                "workflow_id": workflow_id,
                "workflow_name": workflow_name,
                "execution_id": execution_id,
                "timestamp": datetime.utcnow().isoformat()
            }
        )

    def log_workflow_complete(
        self,
        context: ExecutionContext
    ) -> None:
        """
        Log workflow execution completion.

        Args:
            context: Execution context
        """
        summary = context.get_summary()

        self._write_log(
            self.workflow_log,
            {
                "event_type": "workflow_completed",
                "workflow_id": context.workflow_id,
                "workflow_name": context.workflow_name,
                "execution_id": context.execution_id,
                "summary": summary,
                "timestamp": datetime.utcnow().isoformat()
            }
        )

    def log_agent_execution(
        self,
        workflow_id: str,
        execution_id: str,
        record: AgentExecutionRecord
    ) -> None:
        """
        Log individual agent execution.

        Args:
            workflow_id: Workflow identifier
            execution_id: Execution identifier
            record: Agent execution record
        """
        self._write_log(
            self.agent_log,
            {
                "event_type": "agent_executed",
                "workflow_id": workflow_id,
                "execution_id": execution_id,
                "agent_id": record.agent_id,
                "state": record.state.value,
                "started_at": record.started_at.isoformat(),
                "completed_at": record.completed_at.isoformat() if record.completed_at else None,
                "has_error": record.error is not None,
                "governance_violations": record.governance_violations,
                "timestamp": datetime.utcnow().isoformat()
            }
        )

    def log_execution_error(
        self,
        workflow_id: str,
        execution_id: str,
        agent_id: str,
        error: str
    ) -> None:
        """
        Log execution error.

        Args:
            workflow_id: Workflow identifier
            execution_id: Execution identifier
            agent_id: Agent that errored
            error: Error message
        """
        self._write_log(
            self.errors_log,
            {
                "event_type": "execution_error",
                "workflow_id": workflow_id,
                "execution_id": execution_id,
                "agent_id": agent_id,
                "error": error,
                "timestamp": datetime.utcnow().isoformat()
            }
        )

    def log_governance_violation(
        self,
        workflow_id: str,
        execution_id: str,
        agent_id: str,
        violations: list
    ) -> None:
        """
        Log governance rule violation.

        Args:
            workflow_id: Workflow identifier
            execution_id: Execution identifier
            agent_id: Agent that violated rules
            violations: List of violations
        """
        self._write_log(
            self.errors_log,
            {
                "event_type": "governance_violation",
                "workflow_id": workflow_id,
                "execution_id": execution_id,
                "agent_id": agent_id,
                "violations": violations,
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
