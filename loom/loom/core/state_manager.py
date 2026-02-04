"""
State management for LOOM workflows.

Provides persistence and versioning for workflow state.
"""

from typing import Dict, Any, Optional, List
from pathlib import Path
import json
from datetime import datetime

from loom.models.agent_models import AgentWorkflow


class StateManager:
    """
    Manages workflow state persistence and versioning.

    Constitutional principle: All state changes are tracked and reversible.
    """

    def __init__(self, state_dir: Optional[Path] = None):
        """
        Initialize state manager.

        Args:
            state_dir: Directory for state persistence
                      (defaults to X:/Projects/_gaia/loom/state/)
        """
        if state_dir is None:
            state_dir = Path("X:/Projects/_gaia/loom/state")

        self.state_dir = Path(state_dir)
        self.state_dir.mkdir(parents=True, exist_ok=True)

        self.workflows_dir = self.state_dir / "workflows"
        self.workflows_dir.mkdir(parents=True, exist_ok=True)

        self.executions_dir = self.state_dir / "executions"
        self.executions_dir.mkdir(parents=True, exist_ok=True)

    def save_workflow(
        self,
        workflow: AgentWorkflow,
        version_comment: Optional[str] = None
    ) -> str:
        """
        Save workflow state with versioning.

        Args:
            workflow: Workflow to save
            version_comment: Optional version comment

        Returns:
            Version identifier
        """
        workflow_dir = self.workflows_dir / workflow.id
        workflow_dir.mkdir(parents=True, exist_ok=True)

        # Create version
        version_id = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
        version_file = workflow_dir / f"{version_id}.json"

        # Save workflow
        workflow_data = workflow.to_serializable()
        workflow_data["_version_id"] = version_id
        workflow_data["_version_comment"] = version_comment

        with open(version_file, 'w', encoding='utf-8') as f:
            json.dump(workflow_data, f, indent=2)

        # Update current version pointer
        current_file = workflow_dir / "current.json"
        with open(current_file, 'w', encoding='utf-8') as f:
            json.dump(workflow_data, f, indent=2)

        return version_id

    def load_workflow(
        self,
        workflow_id: str,
        version_id: Optional[str] = None
    ) -> AgentWorkflow:
        """
        Load workflow state.

        Args:
            workflow_id: Workflow identifier
            version_id: Optional specific version (defaults to current)

        Returns:
            Workflow instance

        Raises:
            FileNotFoundError: If workflow not found
        """
        workflow_dir = self.workflows_dir / workflow_id

        if version_id:
            version_file = workflow_dir / f"{version_id}.json"
        else:
            version_file = workflow_dir / "current.json"

        if not version_file.exists():
            raise FileNotFoundError(
                f"Workflow {workflow_id} version {version_id or 'current'} not found"
            )

        with open(version_file, 'r', encoding='utf-8') as f:
            workflow_data = json.load(f)

        # Remove version metadata before creating workflow
        workflow_data.pop("_version_id", None)
        workflow_data.pop("_version_comment", None)

        return AgentWorkflow(**workflow_data)

    def list_workflow_versions(self, workflow_id: str) -> List[Dict[str, Any]]:
        """
        List all versions of a workflow.

        Args:
            workflow_id: Workflow identifier

        Returns:
            List of version metadata
        """
        workflow_dir = self.workflows_dir / workflow_id
        if not workflow_dir.exists():
            return []

        versions = []
        for version_file in sorted(workflow_dir.glob("*.json")):
            if version_file.name == "current.json":
                continue

            with open(version_file, 'r', encoding='utf-8') as f:
                data = json.load(f)

            versions.append({
                "version_id": data.get("_version_id"),
                "comment": data.get("_version_comment"),
                "updated_at": data.get("updated_at"),
                "name": data.get("name")
            })

        return versions

    def save_execution_record(
        self,
        execution_id: str,
        workflow_id: str,
        execution_data: Dict[str, Any]
    ) -> None:
        """
        Save execution record for audit trail.

        Args:
            execution_id: Execution identifier
            workflow_id: Workflow that was executed
            execution_data: Execution context data
        """
        execution_dir = self.executions_dir / workflow_id
        execution_dir.mkdir(parents=True, exist_ok=True)

        execution_file = execution_dir / f"{execution_id}.json"

        with open(execution_file, 'w', encoding='utf-8') as f:
            json.dump(execution_data, f, indent=2)

    def load_execution_record(
        self,
        execution_id: str,
        workflow_id: str
    ) -> Dict[str, Any]:
        """
        Load execution record.

        Args:
            execution_id: Execution identifier
            workflow_id: Workflow identifier

        Returns:
            Execution data

        Raises:
            FileNotFoundError: If record not found
        """
        execution_file = self.executions_dir / workflow_id / f"{execution_id}.json"

        if not execution_file.exists():
            raise FileNotFoundError(
                f"Execution {execution_id} for workflow {workflow_id} not found"
            )

        with open(execution_file, 'r', encoding='utf-8') as f:
            return json.load(f)

    def list_executions(
        self,
        workflow_id: str,
        limit: int = 100
    ) -> List[Dict[str, Any]]:
        """
        List recent executions for a workflow.

        Args:
            workflow_id: Workflow identifier
            limit: Maximum number of executions to return

        Returns:
            List of execution summaries
        """
        execution_dir = self.executions_dir / workflow_id
        if not execution_dir.exists():
            return []

        executions = []
        for execution_file in sorted(
            execution_dir.glob("*.json"),
            reverse=True
        )[:limit]:
            with open(execution_file, 'r', encoding='utf-8') as f:
                data = json.load(f)

            executions.append({
                "execution_id": execution_file.stem,
                "started_at": data.get("started_at"),
                "completed_at": data.get("completed_at"),
                "has_errors": data.get("has_errors", False),
                "execution_count": data.get("execution_count", 0)
            })

        return executions
