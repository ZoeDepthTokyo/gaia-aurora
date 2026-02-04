# LOOM - Visual Agent Editor Foundation

**Version:** 0.1.0
**Status:** Phase 3 Implementation (Data Structures)
**GAIA Role:** Agent Workflow Design

## Overview

LOOM (mythic weaver of fate) is the visual agent editor for the GAIA ecosystem. This Phase 3 implementation provides the foundational data structures, execution engine, and contracts for defining, connecting, and executing agents in a glass-box, inspectable manner.

**Note**: Visual UI will be implemented in later phases. This release focuses on core architecture.

## Constitutional Principles

1. **Glass-Box Transparency**: All agent logic is inspectable
2. **No Autonomous Action**: Execution requires explicit approval
3. **Explicit Contracts**: Input/output schemas are enforced
4. **Governance Rules**: Constraints defined at design-time

## Architecture

```
LOOM
├── models/                  # Data models and schemas
│   ├── agent_models.py      # Agent nodes, workflows, governance
│   └── wire_models.py       # Connections between agents
├── core/                    # Execution engine
│   ├── workflow_engine.py   # Workflow executor
│   ├── execution_context.py # Execution state tracking
│   └── state_manager.py     # Workflow persistence
├── integrations/            # External integrations
│   ├── mycel_bridge.py      # MYCEL LLM integration
│   ├── mnemis_bridge.py     # MNEMIS memory integration
│   └── argus_telemetry.py   # ARGUS telemetry
└── tests/                   # Test suite
```

## Quick Start

### Installation

```bash
cd X:/Projects/_gaia/loom
pip install -e .
```

### Basic Usage

```python
from loom import AgentNode, AgentWorkflow, WorkflowEngine
from loom.models.agent_models import (
    AgentType,
    AgentInputSchema,
    AgentOutputSchema,
    GovernanceRule
)

# Define agent
agent = AgentNode(
    id="analyzer_001",
    name="Data Analyzer",
    agent_type=AgentType.EXECUTOR,
    description="Analyzes input data",
    input_schema=[
        AgentInputSchema(
            name="data",
            type="dict",
            required=True,
            description="Data to analyze"
        )
    ],
    output_schema=[
        AgentOutputSchema(
            name="result",
            type="dict",
            description="Analysis result"
        )
    ],
    implementation="my_module.analyze_data"
)

# Add governance rule
agent.add_governance_rule(
    GovernanceRule(
        rule_id="cost_limit",
        rule_type="cost_limit",
        constraint={"max_cost": 1.0},
        action_on_violation="halt"
    )
)

# Create workflow
workflow = AgentWorkflow(
    id="analysis_workflow",
    name="Data Analysis Pipeline",
    description="Analyzes data through multiple stages",
    agents=[agent],
    connections=[],
    entry_points=["analyzer_001"]
)

# Execute workflow
engine = WorkflowEngine()

# Register implementation
def analyze_data(inputs):
    return {"result": f"Analyzed: {inputs['data']}"}

engine.register_agent_implementation("analyzer_001", analyze_data)

# Run workflow
context = engine.execute_workflow(
    workflow=workflow,
    initial_inputs={"data": {"value": 42}}
)

print(context.get_summary())
```

## Agent Types

LOOM supports four agent classifications:

### EXECUTOR
- **Purpose**: Performs actions (tools, API calls, LLM execution)
- **Characteristics**: Side effects, state changes
- **Example**: LLM agent, database writer, API caller

### OBSERVER
- **Purpose**: Read-only analysis, no actions
- **Characteristics**: No side effects, cannot modify state
- **Example**: Process observer, pattern detector

### COORDINATOR
- **Purpose**: Manages other agents, orchestrates workflows
- **Characteristics**: Translates between agents, manages multi-agent workflows
- **Example**: Technical PM agent, workflow manager

### TRANSFORMER
- **Purpose**: Pure data transformation
- **Characteristics**: Deterministic, no external calls
- **Example**: Data validator, format converter

## Agent Definition Schema

### Input Schema

```python
AgentInputSchema(
    name="query",
    type="str",
    required=True,
    default=None,
    description="User query to process",
    validation_rules={"min_length": 1}
)
```

### Output Schema

```python
AgentOutputSchema(
    name="response",
    type="str",
    description="LLM response",
    confidence_score=True  # Include confidence in output
)
```

## Workflow Definition

### Creating Connected Agents

```python
from loom import AgentConnection

# Define two agents
agent1 = AgentNode(...)  # Has output "result"
agent2 = AgentNode(...)  # Has input "data"

# Connect them
connection = AgentConnection(
    id="conn_001",
    source_agent_id=agent1.id,
    source_output="result",
    target_agent_id=agent2.id,
    target_input="data"
)

# Create workflow
workflow = AgentWorkflow(
    id="workflow_001",
    name="Pipeline",
    description="Multi-stage pipeline",
    agents=[agent1, agent2],
    connections=[connection],
    entry_points=[agent1.id]
)
```

### Workflow Execution

```python
# Dry run (validate without executing)
context = engine.execute_workflow(
    workflow=workflow,
    initial_inputs={},
    dry_run=True
)

# Real execution
context = engine.execute_workflow(
    workflow=workflow,
    initial_inputs={"query": "analyze this"}
)

# Check results
if context.has_errors():
    for error in context.errors:
        print(f"Error in {error['agent_id']}: {error['error']}")
else:
    print("Workflow completed successfully")
    print(f"Total cost: ${context.total_cost}")
    print(f"Executions: {context.execution_count}")
```

## Governance Rules

LOOM enforces governance at design-time and runtime:

### Cost Limits

```python
GovernanceRule(
    rule_id="max_cost",
    rule_type="cost_limit",
    constraint={"max_cost": 5.0},
    action_on_violation="halt"
)
```

### Rate Limits

```python
GovernanceRule(
    rule_id="max_executions",
    rule_type="rate_limit",
    constraint={"max_executions": 100},
    action_on_violation="warn"
)
```

### Approval Required

```python
GovernanceRule(
    rule_id="human_review",
    rule_type="approval_required",
    constraint={"requires_human": True},
    action_on_violation="escalate"
)
```

## State Management

### Save Workflow

```python
from loom import StateManager

state_manager = StateManager()

version_id = state_manager.save_workflow(
    workflow=my_workflow,
    version_comment="Added data validation stage"
)
```

### Load Workflow

```python
# Load current version
workflow = state_manager.load_workflow("workflow_001")

# Load specific version
workflow = state_manager.load_workflow(
    workflow_id="workflow_001",
    version_id="20260204_143022"
)

# List versions
versions = state_manager.list_workflow_versions("workflow_001")
for version in versions:
    print(f"{version['version_id']}: {version['comment']}")
```

### Execution Audit Trail

```python
# Save execution record
state_manager.save_execution_record(
    execution_id=context.execution_id,
    workflow_id=workflow.id,
    execution_data=context.model_dump()
)

# List recent executions
executions = state_manager.list_executions(
    workflow_id="workflow_001",
    limit=10
)
```

## Integration with MYCEL

```python
from loom.integrations import MycelAgentBridge

bridge = MycelAgentBridge()

# Create LLM agent implementation
llm_agent_impl = bridge.create_llm_agent_implementation(
    agent_id="llm_agent_001",
    model_provider="openai",
    model_name="gpt-4o",
    system_prompt="You are a helpful assistant"
)

# Register with workflow engine
engine.register_agent_implementation(
    "llm_agent_001",
    llm_agent_impl
)

# Create RAG agent
rag_agent_impl = bridge.create_rag_agent_implementation(
    agent_id="rag_agent_001",
    knowledge_base_path="/path/to/kb",
    model_provider="anthropic"
)
```

## Integration with MNEMIS

```python
from loom.integrations import MnemisWorkflowBridge

mnemis_bridge = MnemisWorkflowBridge()
mnemis_bridge.initialize(memory_store, access_controller)

# Store agent output to memory
memory_id = mnemis_bridge.store_agent_output_to_memory(
    agent_id="analyzer_001",
    project_id="my_project",
    output_data={"result": "analysis"},
    tags=["analysis", "output"]
)

# Retrieve workflow patterns
patterns = mnemis_bridge.retrieve_workflow_patterns(
    workflow_id="workflow_001",
    project_id="my_project",
    tags=["optimization"]
)
```

## Integration with ARGUS

```python
from loom.integrations import WorkflowTelemetryHooks

telemetry = WorkflowTelemetryHooks()

# Log workflow execution
telemetry.log_workflow_start(
    workflow_id=workflow.id,
    workflow_name=workflow.name,
    execution_id=context.execution_id
)

# Log completion
telemetry.log_workflow_complete(context)

# Log errors
telemetry.log_execution_error(
    workflow_id=workflow.id,
    execution_id=context.execution_id,
    agent_id="agent_001",
    error="Connection timeout"
)
```

## Testing

```bash
# Run tests
cd X:/Projects/_gaia/loom
pytest tests/ -v

# With coverage
pytest tests/ --cov=loom --cov-report=html
```

## Wire System

Wires connect agent outputs to inputs:

```python
from loom.models.wire_models import Wire, WireType

wire = Wire(
    id="wire_001",
    wire_type=WireType.DATA,
    source_node_id="agent_001",
    source_port="output1",
    target_node_id="agent_002",
    target_port="input1"
)

# Validate type compatibility
wire.validate_connection(
    source_type="str",
    target_type="str"  # Compatible
)
```

## API Reference

### Core Classes

- **AgentNode**: Agent definition with contracts
- **AgentWorkflow**: Complete workflow with agents and connections
- **WorkflowEngine**: Workflow execution engine
- **ExecutionContext**: Execution state and audit trail
- **StateManager**: Workflow persistence and versioning

### Models

- **AgentInputSchema**: Input contract definition
- **AgentOutputSchema**: Output contract definition
- **GovernanceRule**: Execution constraints
- **Wire**: Connection between agents

See [API_REFERENCE.md](./API_REFERENCE.md) for complete API documentation.

## Constitutional Compliance

LOOM adheres to GAIA constitutional principles:

- ✅ **Glass-Box Transparency**: All workflows inspectable
- ✅ **No Silent Failures**: Errors explicit and logged
- ✅ **Graceful Degradation**: Governance violations halt or warn
- ✅ **Explicit Execution**: No autonomous action
- ✅ **Full Auditability**: Complete execution trace

## Next Steps (Phase 4+)

- Visual node editor UI (Streamlit/React)
- Natural language workflow editing
- Drag-and-drop agent connections
- Real-time execution visualization
- Pattern library and agent templates
- Workflow debugging tools

## Support

For issues or questions:
- See GAIA_BIBLE.md for ecosystem context
- Check SR_COUNCIL_ANALYSIS.md for agent hierarchy
- Review PREDICTIVE_GAIA_SPEC.md for proactive suggestions
