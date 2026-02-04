"""
Agent definition models for LOOM.

Defines the schema for agents, their contracts, and governance rules.
"""

from typing import Any, Dict, List, Optional, Callable
from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field, field_validator


class AgentType(str, Enum):
    """Agent classification types."""
    EXECUTOR = "executor"  # Performs actions (tools, API calls)
    OBSERVER = "observer"  # Read-only, analyzes but doesn't act
    COORDINATOR = "coordinator"  # Manages other agents
    TRANSFORMER = "transformer"  # Pure data transformation


class AgentInputSchema(BaseModel):
    """
    Schema definition for agent input.

    Attributes:
        name: Input parameter name
        type: Data type (str, int, dict, list, etc.)
        required: Whether input is required
        default: Default value if not provided
        description: Human-readable description
        validation_rules: Optional validation constraints
    """
    name: str
    type: str
    required: bool = True
    default: Optional[Any] = None
    description: str = ""
    validation_rules: Dict[str, Any] = Field(default_factory=dict)

    @field_validator('type')
    @classmethod
    def validate_type(cls, v: str) -> str:
        """Validate type is recognized."""
        allowed_types = ["str", "int", "float", "bool", "dict", "list", "Any"]
        if v not in allowed_types:
            raise ValueError(f"type must be one of {allowed_types}")
        return v


class AgentOutputSchema(BaseModel):
    """
    Schema definition for agent output.

    Attributes:
        name: Output parameter name
        type: Data type
        description: Human-readable description
        confidence_score: Whether output includes confidence
    """
    name: str
    type: str
    description: str = ""
    confidence_score: bool = False


class AgentInput(BaseModel):
    """
    Runtime agent input data.

    Attributes:
        schema: Input schema definition
        value: Actual input value
        source: Where input came from (agent_id or 'user')
    """
    schema: AgentInputSchema
    value: Any
    source: str  # agent_id or 'user'


class AgentOutput(BaseModel):
    """
    Runtime agent output data.

    Attributes:
        schema: Output schema definition
        value: Actual output value
        confidence: Optional confidence score (0.0-1.0)
        metadata: Optional output metadata
    """
    schema: AgentOutputSchema
    value: Any
    confidence: Optional[float] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)

    @field_validator('confidence')
    @classmethod
    def validate_confidence(cls, v: Optional[float]) -> Optional[float]:
        """Validate confidence is in valid range."""
        if v is not None and (v < 0.0 or v > 1.0):
            raise ValueError("confidence must be between 0.0 and 1.0")
        return v


class GovernanceRule(BaseModel):
    """
    Governance constraints for agent execution.

    Constitutional principle: Explicit constraints prevent autonomous drift.

    Attributes:
        rule_id: Unique rule identifier
        rule_type: Type of governance rule
        constraint: Constraint definition
        action_on_violation: What to do if violated
        enabled: Whether rule is active
    """
    rule_id: str
    rule_type: str  # cost_limit, rate_limit, approval_required, etc.
    constraint: Dict[str, Any]
    action_on_violation: str = "halt"  # halt, warn, escalate
    enabled: bool = True

    @field_validator('action_on_violation')
    @classmethod
    def validate_action(cls, v: str) -> str:
        """Validate action is recognized."""
        allowed = ["halt", "warn", "escalate", "log"]
        if v not in allowed:
            raise ValueError(f"action_on_violation must be one of {allowed}")
        return v


class AgentNode(BaseModel):
    """
    Agent node definition for LOOM workflows.

    Represents a single agent in the workflow graph with full
    transparency on inputs, outputs, and governance.

    Attributes:
        id: Unique agent identifier
        name: Human-readable agent name
        agent_type: Agent classification
        description: What this agent does
        input_schema: Expected inputs
        output_schema: Produced outputs
        governance_rules: Execution constraints
        implementation: Agent implementation reference
        metadata: Additional metadata
        created_at: Creation timestamp
        updated_at: Last modification timestamp
    """
    id: str
    name: str
    agent_type: AgentType
    description: str
    input_schema: List[AgentInputSchema]
    output_schema: List[AgentOutputSchema]
    governance_rules: List[GovernanceRule] = Field(default_factory=list)
    implementation: str  # Module path or callable reference
    metadata: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    def validate_input(self, input_data: Dict[str, Any]) -> List[str]:
        """
        Validate input data against schema.

        Args:
            input_data: Input data to validate

        Returns:
            List of validation errors (empty if valid)
        """
        errors = []

        # Check required inputs
        for schema in self.input_schema:
            if schema.required and schema.name not in input_data:
                if schema.default is None:
                    errors.append(f"Required input '{schema.name}' missing")

        # Type validation would go here (simplified for now)
        return errors

    def add_governance_rule(self, rule: GovernanceRule) -> None:
        """
        Add governance rule to agent.

        Args:
            rule: Governance rule to add
        """
        self.governance_rules.append(rule)
        self.updated_at = datetime.utcnow()

    def to_serializable(self) -> Dict[str, Any]:
        """
        Convert to JSON-serializable format.

        Returns:
            Dictionary representation
        """
        return self.model_dump(mode='json')


class AgentConnection(BaseModel):
    """
    Connection between two agents in workflow.

    Represents data flow from source agent's output to target agent's input.

    Attributes:
        id: Unique connection identifier
        source_agent_id: Source agent
        source_output: Output parameter name
        target_agent_id: Target agent
        target_input: Input parameter name
        transformation: Optional data transformation
        condition: Optional execution condition
    """
    id: str
    source_agent_id: str
    source_output: str
    target_agent_id: str
    target_input: str
    transformation: Optional[str] = None  # Transformation function reference
    condition: Optional[str] = None  # Conditional execution


class AgentExecutionState(str, Enum):
    """Agent execution states."""
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    SKIPPED = "skipped"


class AgentExecutionRecord(BaseModel):
    """
    Record of agent execution for auditability.

    Attributes:
        agent_id: Agent that executed
        state: Execution state
        inputs: Input data received
        outputs: Output data produced
        started_at: Execution start time
        completed_at: Execution completion time
        error: Error message if failed
        governance_violations: Any governance violations
    """
    agent_id: str
    state: AgentExecutionState
    inputs: Dict[str, Any]
    outputs: Optional[Dict[str, Any]] = None
    started_at: datetime = Field(default_factory=datetime.utcnow)
    completed_at: Optional[datetime] = None
    error: Optional[str] = None
    governance_violations: List[str] = Field(default_factory=list)


class AgentWorkflow(BaseModel):
    """
    Complete workflow definition with agents and connections.

    Constitutional principle: Workflows are glass-box and inspectable.

    Attributes:
        id: Unique workflow identifier
        name: Workflow name
        description: What this workflow does
        agents: Agent nodes in workflow
        connections: Connections between agents
        entry_points: Initial agents to execute
        metadata: Additional metadata
        created_at: Creation timestamp
        updated_at: Last modification timestamp
    """
    id: str
    name: str
    description: str
    agents: List[AgentNode]
    connections: List[AgentConnection]
    entry_points: List[str]  # Agent IDs
    metadata: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    def get_agent(self, agent_id: str) -> Optional[AgentNode]:
        """
        Get agent by ID.

        Args:
            agent_id: Agent identifier

        Returns:
            Agent node or None if not found
        """
        for agent in self.agents:
            if agent.id == agent_id:
                return agent
        return None

    def get_downstream_agents(self, agent_id: str) -> List[str]:
        """
        Get all agents that receive output from this agent.

        Args:
            agent_id: Source agent ID

        Returns:
            List of downstream agent IDs
        """
        return [
            conn.target_agent_id
            for conn in self.connections
            if conn.source_agent_id == agent_id
        ]

    def get_upstream_agents(self, agent_id: str) -> List[str]:
        """
        Get all agents that provide input to this agent.

        Args:
            agent_id: Target agent ID

        Returns:
            List of upstream agent IDs
        """
        return [
            conn.source_agent_id
            for conn in self.connections
            if conn.target_agent_id == agent_id
        ]

    def validate_workflow(self) -> List[str]:
        """
        Validate workflow structure.

        Returns:
            List of validation errors (empty if valid)
        """
        errors = []

        # Check entry points exist
        agent_ids = {agent.id for agent in self.agents}
        for entry_id in self.entry_points:
            if entry_id not in agent_ids:
                errors.append(f"Entry point {entry_id} not found in agents")

        # Check connections reference valid agents
        for conn in self.connections:
            if conn.source_agent_id not in agent_ids:
                errors.append(
                    f"Connection source {conn.source_agent_id} not found"
                )
            if conn.target_agent_id not in agent_ids:
                errors.append(
                    f"Connection target {conn.target_agent_id} not found"
                )

        # Check for cycles (simplified - would use proper graph algorithm)
        # TODO: Implement cycle detection

        return errors

    def to_serializable(self) -> Dict[str, Any]:
        """
        Convert workflow to JSON-serializable format.

        Returns:
            Dictionary representation
        """
        return self.model_dump(mode='json')
