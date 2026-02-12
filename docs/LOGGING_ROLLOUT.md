# GAIA Logging Standard - Rollout Plan

**Version:** 1.0.0
**Date:** February 9, 2026
**Priority:** HIGH (GECO Audit Item)

---

## Overview

This document provides a phased rollout plan for implementing the GAIA Logging Standard across all 17+ GAIA ecosystem components.

**Status:**
- Standard defined: COMPLETE
- Implementation ready: COMPLETE
- Rollout: PENDING

---

## Quick Links

- **Standard**: `X:\Projects\_GAIA\docs\LOGGING_STANDARD.md`
- **Implementation**: `X:\Projects\_GAIA\_MYCEL\rag_intelligence\logging_config.py`
- **Examples**: `X:\Projects\_GAIA\_MYCEL\examples\logging_example.py`

---

## Implementation Status

| Component | Type | Status | Priority | Notes |
|-----------|------|--------|----------|-------|
| MYCEL | Shared Service | READY | P0 | Contains logging_config.py |
| LOOM | Shared Service | NOT STARTED | P0 | Active development |
| ARGUS | Shared Service | NOT STARTED | P0 | Monitors logs |
| MNEMIS | Shared Service | NOT STARTED | P0 | Active development |
| VULCAN | Shared Service | NOT STARTED | P1 | Project creator |
| WARDEN | Shared Service | NOT STARTED | P2 | Not implemented |
| ABIS | Shared Service | NOT STARTED | P3 | Design phase |
| RAVEN | Shared Service | NOT STARTED | P3 | Planned |
| jSeeker | Product | NOT STARTED | P1 | Already has telemetry |
| VIA | Product | NOT STARTED | P1 | Production |
| HART OS | Product | NOT STARTED | P1 | Production |
| DATA FORGE | Product | NOT STARTED | P2 | Production |
| GPT_ECHO | Product | NOT STARTED | P2 | Stale |
| DOS | Product | NOT STARTED | P3 | Planning |
| The Palace | Product | N/A | P4 | Static HTML |
| Waymo Data | Product | N/A | P4 | Data only |

**Priority Definitions:**
- **P0**: Core infrastructure, blocks other work
- **P1**: Production components, high value
- **P2**: Lower priority production, stale projects
- **P3**: Planned/future components
- **P4**: No logging needed

---

## Phase 1: Core Infrastructure (P0)

**Goal**: Implement logging in shared services that other components depend on.

**Components**: MYCEL, LOOM, ARGUS, MNEMIS

**Timeline**: Week 1

### MYCEL

**Status**: READY (logging_config.py exists)

**Tasks**:
- [x] Create logging_config.py
- [x] Update __init__.py exports
- [x] Create examples/logging_example.py
- [ ] Add tests for logging_config.py
- [ ] Update MYCEL documentation
- [ ] Test with example script

**Testing**:
```bash
cd X:\Projects\_GAIA\_MYCEL
python examples/logging_example.py
cat X:\Projects\_GAIA\logs\mycel.log | python -m json.tool
```

### LOOM

**Status**: NOT STARTED

**Tasks**:
- [ ] Add `rag-intelligence>=0.2.1` to requirements.txt
- [ ] Replace logging setup in `loom/core/workflow_engine.py`
- [ ] Add correlation IDs to workflow execution
- [ ] Update MYCEL bridge to pass correlation IDs
- [ ] Add tests

**Example**:
```python
# loom/core/workflow_engine.py
from rag_intelligence import setup_gaia_logger
import uuid

logger = setup_gaia_logger("LOOM")

def execute_workflow(workflow: AgentWorkflow, inputs: dict):
    correlation_id = str(uuid.uuid4())
    logger.info(
        f"Executing workflow: {workflow.name}",
        extra={"correlation_id": correlation_id}
    )
    # ... rest of implementation
```

### ARGUS

**Status**: NOT STARTED

**Tasks**:
- [ ] Add `rag-intelligence>=0.2.1` to requirements.txt
- [ ] Replace logging in mental models
- [ ] Replace logging in explainability
- [ ] Update dashboard to read JSON logs
- [ ] Add tests

**Example**:
```python
# argus/explainability/explainer.py
from rag_intelligence import setup_gaia_logger

logger = setup_gaia_logger("ARGUS")

def explain(decision: dict, level: str):
    logger.info(
        f"Generating explanation: {level}",
        extra={"metadata": {"decision_id": decision["id"]}}
    )
    # ... rest of implementation
```

### MNEMIS

**Status**: NOT STARTED

**Tasks**:
- [ ] Add `rag-intelligence>=0.2.1` to requirements.txt
- [ ] Replace logging in memory_store.py
- [ ] Replace logging in promotion.py
- [ ] Add correlation IDs to memory operations
- [ ] Add tests

**Example**:
```python
# mnemis/core/memory_store.py
from rag_intelligence import setup_gaia_logger

logger = setup_gaia_logger("MNEMIS")

def store_memory(memory: Memory, scope: MemoryScope):
    logger.info(
        f"Storing memory: {memory.id}",
        extra={
            "metadata": {
                "scope": scope.level,
                "tier": scope.tier
            }
        }
    )
    # ... rest of implementation
```

---

## Phase 2: Production Products (P1)

**Goal**: Add logging to production components with active users.

**Components**: jSeeker, VIA, HART OS

**Timeline**: Week 2-3

### jSeeker (formerly PROTEUS)

**Status**: NOT STARTED (has ARGUS telemetry, needs standardization)

**Tasks**:
- [ ] Add `rag-intelligence>=0.2.1` to requirements.txt
- [ ] Replace logging in `jseeker/llm.py`
- [ ] Add correlation IDs to resume generation pipeline
- [ ] Integrate with existing ARGUS telemetry
- [ ] Update tests

**Example**:
```python
# jseeker/llm.py
from rag_intelligence import setup_gaia_logger, log_llm_call
import time

logger = setup_gaia_logger("jSeeker")

def call_llm(prompt: str, model: str, correlation_id: str):
    start = time.time()

    # ... API call ...

    duration_ms = int((time.time() - start) * 1000)
    log_llm_call(
        logger=logger,
        task="resume_adaptation",
        model=model,
        cost_usd=cost,
        input_tokens=usage.input_tokens,
        output_tokens=usage.output_tokens,
        duration_ms=duration_ms,
        correlation_id=correlation_id
    )
```

### VIA

**Status**: NOT STARTED

**Current logging**: Likely uses print() or basic logging

**Tasks**:
- [ ] Audit current logging approach
- [ ] Add `rag-intelligence>=0.2.1` to requirements.txt
- [ ] Replace logging in RAG pipeline
- [ ] Add correlation IDs to investment research workflows
- [ ] Add cost tracking for LLM calls
- [ ] Update tests

### HART OS

**Status**: NOT STARTED

**Current logging**: Likely uses print() or basic logging

**Tasks**:
- [ ] Audit current logging approach
- [ ] Add `rag-intelligence>=0.2.1` to requirements.txt
- [ ] Replace logging in therapy scoring pipeline
- [ ] Add correlation IDs to session processing
- [ ] Add cost tracking for OpenAI calls
- [ ] Update tests

---

## Phase 3: Secondary Products (P2)

**Goal**: Standardize logging in lower-priority production components.

**Components**: DATA FORGE, GPT_ECHO, VULCAN

**Timeline**: Week 4

### DATA FORGE

**Status**: NOT STARTED

**Tasks**:
- [ ] Audit current logging
- [ ] Add `rag-intelligence>=0.2.1` to requirements.txt
- [ ] Replace logging in data processing pipeline
- [ ] Add cost tracking
- [ ] Update tests

### GPT_ECHO

**Status**: NOT STARTED (stale, needs consolidation first)

**Tasks**:
- [ ] Wait for ENG-003 consolidation
- [ ] Then add logging during refactor

### VULCAN

**Status**: NOT STARTED

**Tasks**:
- [ ] Add `rag-intelligence>=0.2.1` to requirements.txt
- [ ] Replace logging in project_creator.py
- [ ] Replace logging in adapters
- [ ] Add tests

---

## Phase 4: Future Components (P3)

**Goal**: Ensure new components use logging standard from day one.

**Components**: DOS, RAVEN, ABIS

**Timeline**: When implemented

**Tasks**:
- [ ] Update VULCAN adapters to include logging setup
- [ ] Add logging examples to component templates
- [ ] Ensure all new components inherit from GaiaSettings

---

## Testing Checklist

For each component migration:

### Pre-Migration
- [ ] Document current logging approach
- [ ] Identify all logging statements
- [ ] Create test plan

### Migration
- [ ] Add rag-intelligence dependency
- [ ] Replace logging setup
- [ ] Add correlation IDs
- [ ] Add structured metadata
- [ ] Add cost tracking (for LLM calls)

### Post-Migration
- [ ] Run test suite (all tests pass)
- [ ] Verify console logs appear
- [ ] Verify JSON logs written to `X:\Projects\_GAIA\logs\{component}.log`
- [ ] Verify ARGUS telemetry (if LLM calls present)
- [ ] Check log rotation works
- [ ] Update component documentation

### Validation
```bash
# Check logs exist
ls X:\Projects\_GAIA\logs\

# Validate JSON format
cat X:\Projects\_GAIA\logs\{component}.log | head -n 10 | python -m json.tool

# Check ARGUS telemetry
cat X:\Projects\_GAIA\logs\{component}_runtime.jsonl | python -m json.tool

# Check log rotation
# (manually create large log file and verify rotation)
```

---

## Common Migration Patterns

### Pattern 1: Replace Basic Logging

**Before**:
```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
```

**After**:
```python
from rag_intelligence import setup_gaia_logger

logger = setup_gaia_logger("MYCEL")
```

### Pattern 2: Add Correlation IDs

**Before**:
```python
def process_request(data):
    logger.info("Processing request")
    # ... processing ...
    logger.info("Request completed")
```

**After**:
```python
import uuid

def process_request(data):
    correlation_id = str(uuid.uuid4())
    logger.info(
        "Processing request",
        extra={"correlation_id": correlation_id}
    )
    # ... processing ...
    logger.info(
        "Request completed",
        extra={"correlation_id": correlation_id}
    )
```

### Pattern 3: Add Cost Tracking

**Before**:
```python
response = llm.call(prompt)
logger.info("LLM call completed")
```

**After**:
```python
from rag_intelligence import log_llm_call
import time

start = time.time()
response = llm.call(prompt)
duration_ms = int((time.time() - start) * 1000)

log_llm_call(
    logger=logger,
    task="embedding_generation",
    model="text-embedding-3-small",
    cost_usd=0.0001,
    input_tokens=150,
    output_tokens=0,
    duration_ms=duration_ms,
    correlation_id=correlation_id
)
```

### Pattern 4: Exception Logging

**Before**:
```python
try:
    risky_operation()
except Exception as e:
    logger.error(f"Error: {e}")
```

**After**:
```python
try:
    risky_operation()
except Exception as e:
    logger.error(
        "Operation failed",
        exc_info=True,  # Includes full stack trace
        extra={"correlation_id": correlation_id}
    )
```

---

## Metrics

Track rollout progress:

| Metric | Target | Current |
|--------|--------|---------|
| Components with standard logging | 17 | 0 |
| Shared services migrated | 8 | 0 |
| Products migrated | 9 | 0 |
| Test coverage | 80% | N/A |
| Documentation updated | 100% | 100% |

---

## Success Criteria

The rollout is complete when:

1. All P0 and P1 components use the standard
2. All components log to `X:\Projects\_GAIA\logs\`
3. All LLM calls emit ARGUS telemetry
4. All multi-step operations use correlation IDs
5. ARGUS dashboard can display ecosystem-wide logs
6. All components have 80%+ test coverage
7. All component documentation updated

---

## Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Breaking existing logging | HIGH | Thorough testing, gradual rollout |
| Performance overhead | MEDIUM | Logging is async, minimal impact |
| Disk space exhaustion | MEDIUM | Log rotation (10 MB × 5 backups per component) |
| Resistance to change | LOW | Clear documentation, examples, support |

---

## Support

**Questions?** Contact:
- GAIA Architect: Fed
- Documentation: `X:\Projects\_GAIA\docs\LOGGING_STANDARD.md`
- Examples: `X:\Projects\_GAIA\_MYCEL\examples\logging_example.py`

**Issues?** Report to:
- GitHub: (to be created)
- Discord: (to be created)

---

## Next Steps

1. **Immediate**: Review this plan with GAIA architect
2. **Week 1**: Implement Phase 1 (MYCEL, LOOM, ARGUS, MNEMIS)
3. **Week 2-3**: Implement Phase 2 (jSeeker, VIA, HART OS)
4. **Week 4**: Implement Phase 3 (DATA FORGE, VULCAN)
5. **Ongoing**: Ensure new components use standard from day one

---

**Document Maintenance:**
- Update component status as migrations complete
- Track metrics weekly
- Update risks as discovered
- Last Updated: 2026-02-09

**Contributors:**
- Author: Claude Code (Sonnet 4.5)
- Reviewer: Fed (GAIA Architect)
