# MNEMIS - Cross-Project Memory System

**Version:** 0.1.0
**Status:** Phase 3 Implementation
**GAIA Role:** Memory Management

## Overview

MNEMIS (Mnemosyne, titan of memory) is the cross-project memory system for the GAIA ecosystem. It provides hierarchical memory management with enforced access contracts, promotion discipline, and full provenance tracking.

## Constitutional Principles

1. **Three-Tier Hierarchy**: GAIA (ecosystem) > PROJECT > AGENT (ephemeral)
2. **Explicit Promotion**: Memory moves up hierarchy via proposal only, never automatically
3. **Provenance Tracking**: All memory operations tracked with full audit trail
4. **No Silent Drift**: All access violations are explicit and logged

## Architecture

```
MNEMIS
├── models/               # Data models and schemas
│   └── memory_models.py  # Memory, contracts, scopes, proposals
├── core/                 # Core functionality
│   ├── memory_store.py   # Storage engine
│   ├── contracts.py      # Access control
│   ├── promotion.py      # Promotion workflow
│   └── search.py         # Memory search
├── integrations/         # External integrations
│   ├── mycel_bridge.py   # MYCEL integration
│   └── argus_telemetry.py # ARGUS logging
└── tests/                # Test suite
```

## Quick Start

### Installation

```bash
cd X:/Projects/_gaia/mnemis
pip install -e .
```

### Basic Usage

```python
from mnemis import MnemisStore, MemoryAccessController

# Initialize
store = MnemisStore()
controller = MemoryAccessController()

# Register agent
contract = controller.register_agent(
    agent_id="my_agent",
    access_level=MemoryAccessLevel.PROJECT,
    project_id="my_project"
)

# Write memory
scope = controller.create_project_scope("my_project")
memory_id = store.write(
    content={"pattern": "useful_pattern"},
    scope=scope,
    contract=contract,
    tags=["pattern", "optimization"]
)

# Read memory
memory = store.read(memory_id, contract)
print(memory.content)
```

## Memory Hierarchy

### GAIA Tier (Ecosystem-Wide)

- **Scope**: All projects in ecosystem
- **Persistence**: Eternal (stored in `X:/Projects/_gaia/mnemis/shared_memory/`)
- **Access**: GAIA-level agents can read/write
- **Use Cases**: Cross-project patterns, ecosystem learnings

### PROJECT Tier (Project-Scoped)

- **Scope**: Single project
- **Persistence**: Project lifecycle (stored in `X:/Projects/_gaia/mnemis/shared_memory/projects/`)
- **Access**: PROJECT-level agents can read/write
- **Use Cases**: Project-specific patterns, local optimizations

### AGENT Tier (Ephemeral)

- **Scope**: Single agent execution
- **Persistence**: Auto-expire after TTL (in-memory only)
- **Access**: AGENT-level only
- **Use Cases**: Execution context, temporary state

## Memory Contracts

### Read Permissions

Agents can read DOWN the hierarchy:

```
GAIA agents   → Read: GAIA, PROJECT, AGENT
PROJECT agents → Read: PROJECT, AGENT
AGENT          → Read: AGENT only
```

### Write Permissions

Agents can write ONLY at their exact level:

```
GAIA agents   → Write: GAIA only
PROJECT agents → Write: PROJECT only
AGENT          → Write: AGENT only
```

## Promotion Workflow

Memory promotion requires explicit approval:

```
AGENT memory → Propose to PROJECT
    ↓
PROJECT agent reviews → Approve/Reject
    ↓
If approved → Memory promoted to PROJECT tier
    ↓
PROJECT memory → Propose to GAIA
    ↓
GAIA/Human reviews → Approve/Reject
    ↓
If approved → Memory promoted to GAIA tier
```

### Example: Promote Memory

```python
from mnemis import MemoryPromotionEngine

promotion_engine = MemoryPromotionEngine(store, controller)

# Propose promotion
proposal_id = promotion_engine.propose_promotion(
    memory_id="mem_123",
    to_scope=controller.create_gaia_scope(),
    agent_id="project_agent",
    rationale="This pattern is useful for all projects"
)

# Approve promotion (by human or GAIA-level agent)
promoted_memory_id = promotion_engine.approve_promotion(
    proposal_id=proposal_id,
    reviewer="human",
    notes="Approved - useful cross-project pattern"
)
```

## Search Interface

### Search by Tags

```python
from mnemis import MemorySearchEngine

search_engine = MemorySearchEngine(store)

results = search_engine.search_by_tags(
    tags=["optimization", "performance"],
    contract=my_contract,
    match_all=False  # Match ANY tag
)
```

### Advanced Search

```python
from datetime import datetime, timedelta

results = search_engine.advanced_search(
    contract=my_contract,
    tags=["pattern"],
    content_query="optimization",
    start_date=datetime.now() - timedelta(days=30),
    levels=[MemoryAccessLevel.PROJECT, MemoryAccessLevel.GAIA]
)
```

## Integration with MYCEL

```python
from mnemis.integrations import MycelMemoryBridge

bridge = MycelMemoryBridge(store, controller)

# Create agent session
contract = bridge.create_agent_session(
    agent_id="mycel_agent",
    project_id="my_project",
    ttl_seconds=3600
)

# Store agent memory
memory_id = bridge.store_agent_memory(
    agent_id="mycel_agent",
    project_id="my_project",
    content={"result": "analysis_output"},
    tags=["analysis"]
)

# Cleanup expired sessions
cleaned = bridge.cleanup_expired_sessions()
```

## Integration with ARGUS

```python
from mnemis.integrations import MemoryTelemetryHooks

telemetry = MemoryTelemetryHooks()

# Log operations
telemetry.log_memory_write(
    memory_id="mem_123",
    agent_id="my_agent",
    access_level="project",
    memory_level="project",
    tags=["pattern"],
    success=True
)

# Log violations
telemetry.log_access_violation(
    agent_id="bad_agent",
    violation_type="unauthorized_read",
    details={"attempted_level": "gaia"}
)
```

## Testing

```bash
# Run tests
cd X:/Projects/_gaia/mnemis
pytest tests/ -v

# With coverage
pytest tests/ --cov=mnemis --cov-report=html
```

## API Reference

### Core Classes

- **MnemisStore**: Central memory storage
- **MemoryAccessController**: Access control enforcement
- **MemoryPromotionEngine**: Promotion workflow management
- **MemorySearchEngine**: Memory search and retrieval

### Models

- **MemoryEntry**: Single memory entry with provenance
- **MemoryContract**: Agent access contract
- **MemoryScope**: Memory visibility scope
- **MemoryPromotionProposal**: Promotion request

See [API_REFERENCE.md](./API_REFERENCE.md) for complete API documentation.

## Constitutional Compliance

MNEMIS adheres to GAIA constitutional principles:

- ✅ **Glass-Box Transparency**: All memory operations logged
- ✅ **No Silent Failures**: Access violations are explicit
- ✅ **Graceful Degradation**: Violations logged, not hidden
- ✅ **Explicit Learning**: Promotions require approval
- ✅ **Inspectable**: Full provenance tracking

## Next Steps (Phase 4+)

- Visual memory graph explorer
- Pattern detection across memories
- Automatic promotion recommendations (with approval)
- Memory compression for large ecosystems
- Cross-ecosystem memory federation

## Support

For issues or questions:
- See GAIA_BIBLE.md for ecosystem context
- Check SR_COUNCIL_ANALYSIS.md for governance details
- Review PREDICTIVE_GAIA_SPEC.md for predictive patterns
