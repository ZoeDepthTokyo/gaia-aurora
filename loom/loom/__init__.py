"""
LOOM - Visual Agent Editor for GAIA Ecosystem.

Provides data structures and contracts for defining, connecting, and
executing agents in a glass-box, inspectable manner.

Constitutional Principles:
- All agent logic is inspectable
- No autonomous action without human approval
- Explicit input/output contracts
- Governance rules at design-time
"""

__version__ = "0.1.0"
__author__ = "GAIA Ecosystem"

from loom.models.agent_models import (
    AgentNode,
    AgentInput,
    AgentOutput,
    AgentConnection,
    AgentWorkflow,
    AgentExecutionState,
    GovernanceRule,
)

from loom.models.wire_models import (
    Wire,
    WireType,
    WireValidationError,
)

from loom.core.workflow_engine import WorkflowEngine
from loom.core.execution_context import ExecutionContext
from loom.core.state_manager import StateManager

__all__ = [
    # Agent Models
    "AgentNode",
    "AgentInput",
    "AgentOutput",
    "AgentConnection",
    "AgentWorkflow",
    "AgentExecutionState",
    "GovernanceRule",
    # Wire Models
    "Wire",
    "WireType",
    "WireValidationError",
    # Core
    "WorkflowEngine",
    "ExecutionContext",
    "StateManager",
]
