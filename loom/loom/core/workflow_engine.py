"""
Workflow execution engine for LOOM.

Executes agent workflows with governance enforcement and full auditability.
"""

from typing import Dict, Any, List, Optional, Callable
from datetime import datetime
import uuid

from loom.models.agent_models import (
    AgentWorkflow,
    AgentNode,
    AgentExecutionRecord,
    AgentExecutionState,
    GovernanceRule,
)
from loom.core.execution_context import ExecutionContext
from loom.core.state_manager import StateManager


class WorkflowEngine:
    """
    Executes agent workflows with governance and observability.

    Constitutional principles:
    - No autonomous execution without approval
    - All state changes tracked
    - Governance rules enforced at runtime
    - Graceful degradation on failure
    """

    def __init__(self):
        """Initialize workflow engine."""
        self.state_manager = StateManager()
        self._agent_implementations: Dict[str, Callable] = {}

    def register_agent_implementation(
        self,
        agent_id: str,
        implementation: Callable
    ) -> None:
        """
        Register agent implementation function.

        Args:
            agent_id: Agent identifier
            implementation: Callable that implements agent logic
        """
        self._agent_implementations[agent_id] = implementation

    def execute_workflow(
        self,
        workflow: AgentWorkflow,
        initial_inputs: Dict[str, Any],
        dry_run: bool = False
    ) -> ExecutionContext:
        """
        Execute workflow from entry points.

        Args:
            workflow: Workflow to execute
            initial_inputs: Initial input data
            dry_run: If True, validate but don't execute

        Returns:
            Execution context with results and audit trail
        """
        # Validate workflow
        validation_errors = workflow.validate_workflow()
        if validation_errors:
            raise ValueError(f"Workflow validation failed: {validation_errors}")

        # Create execution context
        context = ExecutionContext(
            workflow_id=workflow.id,
            workflow_name=workflow.name
        )

        if dry_run:
            context.dry_run = True
            return context

        # Execute entry point agents
        for entry_agent_id in workflow.entry_points:
            agent = workflow.get_agent(entry_agent_id)
            if agent:
                self._execute_agent_cascade(
                    workflow=workflow,
                    agent=agent,
                    inputs=initial_inputs,
                    context=context
                )

        context.complete()
        return context

    def _execute_agent_cascade(
        self,
        workflow: AgentWorkflow,
        agent: AgentNode,
        inputs: Dict[str, Any],
        context: ExecutionContext
    ) -> None:
        """
        Execute agent and cascade to downstream agents.

        Args:
            workflow: Workflow being executed
            agent: Agent to execute
            inputs: Input data for agent
            context: Execution context
        """
        # Execute this agent
        execution_record = self._execute_agent(agent, inputs, context)
        context.add_execution_record(execution_record)

        # If execution failed, halt cascade
        if execution_record.state == AgentExecutionState.FAILED:
            context.record_error(
                agent_id=agent.id,
                error=execution_record.error
            )
            return

        # Get downstream agents
        downstream_ids = workflow.get_downstream_agents(agent.id)

        # Execute downstream agents
        for downstream_id in downstream_ids:
            downstream_agent = workflow.get_agent(downstream_id)
            if not downstream_agent:
                continue

            # Prepare inputs for downstream agent
            downstream_inputs = self._prepare_downstream_inputs(
                workflow=workflow,
                source_agent_id=agent.id,
                target_agent_id=downstream_id,
                source_outputs=execution_record.outputs or {}
            )

            # Recursive cascade
            self._execute_agent_cascade(
                workflow=workflow,
                agent=downstream_agent,
                inputs=downstream_inputs,
                context=context
            )

    def _execute_agent(
        self,
        agent: AgentNode,
        inputs: Dict[str, Any],
        context: ExecutionContext
    ) -> AgentExecutionRecord:
        """
        Execute single agent with governance enforcement.

        Args:
            agent: Agent to execute
            inputs: Input data
            context: Execution context

        Returns:
            Execution record
        """
        record = AgentExecutionRecord(
            agent_id=agent.id,
            state=AgentExecutionState.PENDING,
            inputs=inputs
        )

        try:
            # Validate inputs
            input_errors = agent.validate_input(inputs)
            if input_errors:
                record.state = AgentExecutionState.FAILED
                record.error = f"Input validation failed: {input_errors}"
                record.completed_at = datetime.utcnow()
                return record

            # Check governance rules
            governance_violations = self._check_governance_rules(
                agent=agent,
                inputs=inputs,
                context=context
            )

            if governance_violations:
                record.state = AgentExecutionState.FAILED
                record.governance_violations = governance_violations
                record.error = f"Governance violations: {governance_violations}"
                record.completed_at = datetime.utcnow()
                return record

            # Execute agent
            record.state = AgentExecutionState.RUNNING

            if agent.id in self._agent_implementations:
                implementation = self._agent_implementations[agent.id]
                outputs = implementation(inputs)
                record.outputs = outputs
                record.state = AgentExecutionState.COMPLETED
            else:
                record.state = AgentExecutionState.FAILED
                record.error = f"No implementation registered for agent {agent.id}"

        except Exception as e:
            record.state = AgentExecutionState.FAILED
            record.error = str(e)

        finally:
            record.completed_at = datetime.utcnow()

        return record

    def _check_governance_rules(
        self,
        agent: AgentNode,
        inputs: Dict[str, Any],
        context: ExecutionContext
    ) -> List[str]:
        """
        Check governance rules for agent execution.

        Args:
            agent: Agent to check
            inputs: Input data
            context: Execution context

        Returns:
            List of violations (empty if compliant)
        """
        violations = []

        for rule in agent.governance_rules:
            if not rule.enabled:
                continue

            # Check rule type
            if rule.rule_type == "cost_limit":
                # Check cumulative cost
                max_cost = rule.constraint.get("max_cost", float('inf'))
                if context.total_cost > max_cost:
                    violations.append(
                        f"Cost limit exceeded: {context.total_cost} > {max_cost}"
                    )

            elif rule.rule_type == "rate_limit":
                # Check execution rate
                max_executions = rule.constraint.get("max_executions", float('inf'))
                if context.execution_count >= max_executions:
                    violations.append(
                        f"Rate limit exceeded: {context.execution_count} >= {max_executions}"
                    )

            elif rule.rule_type == "approval_required":
                # Check for human approval
                if not context.has_approval(agent.id):
                    violations.append("Human approval required but not provided")

        return violations

    def _prepare_downstream_inputs(
        self,
        workflow: AgentWorkflow,
        source_agent_id: str,
        target_agent_id: str,
        source_outputs: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Prepare input data for downstream agent from upstream outputs.

        Args:
            workflow: Workflow being executed
            source_agent_id: Source agent ID
            target_agent_id: Target agent ID
            source_outputs: Outputs from source agent

        Returns:
            Input data for target agent
        """
        downstream_inputs = {}

        # Find connections from source to target
        connections = [
            conn for conn in workflow.connections
            if conn.source_agent_id == source_agent_id and
               conn.target_agent_id == target_agent_id
        ]

        # Map outputs to inputs via connections
        for conn in connections:
            if conn.source_output in source_outputs:
                value = source_outputs[conn.source_output]

                # Apply transformation if specified
                if conn.transformation:
                    # TODO: Apply transformation function
                    pass

                downstream_inputs[conn.target_input] = value

        return downstream_inputs
