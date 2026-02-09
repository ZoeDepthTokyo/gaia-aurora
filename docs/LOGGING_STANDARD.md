# GAIA Ecosystem Logging Standard

**Version:** 1.0.0
**Date:** February 9, 2026
**Status:** Active
**Audience:** All GAIA component developers

---

## Table of Contents

1. [Overview](#overview)
2. [Log Levels](#log-levels)
3. [Log Format](#log-format)
4. [Structured Logging](#structured-logging)
5. [File Rotation](#file-rotation)
6. [ARGUS Telemetry Integration](#argus-telemetry-integration)
7. [Implementation](#implementation)
8. [Examples](#examples)
9. [Migration Guide](#migration-guide)

---

## Overview

The GAIA Ecosystem Logging Standard provides a unified approach to logging across all 17+ GAIA components. This standard ensures:

- **Consistency**: All components log in the same format
- **Traceability**: Correlation IDs enable cross-component tracing
- **Machine-readability**: Structured JSON logs for ARGUS analysis
- **Human-readability**: Console logs with color and context
- **Cost tracking**: Integration with ARGUS telemetry

### Constitutional Principle

> All GAIA components MUST log to a shared standard format to enable ecosystem-wide observability, pattern detection, and cost optimization.

---

## Log Levels

GAIA uses the standard Python logging levels:

| Level | Numeric | Use Cases | Examples |
|-------|---------|-----------|----------|
| **DEBUG** | 10 | Development tracing, verbose diagnostics | Function entry/exit, variable states |
| **INFO** | 20 | Normal operation milestones, key events | Pipeline started, retrieval completed |
| **WARNING** | 30 | Recoverable issues, degraded performance | Cache miss, fallback to default |
| **ERROR** | 40 | Operation failures that need attention | API call failed, validation error |
| **CRITICAL** | 50 | System-level failures, data corruption | Database unreachable, memory corruption |

### Level Selection Guidelines

- **DEBUG**: Use liberally during development, disable in production
- **INFO**: Should tell the story of a successful operation
- **WARNING**: Something worked, but not as expected
- **ERROR**: An operation failed, but the system continues
- **CRITICAL**: The system cannot continue safely

---

## Log Format

### Console Format (Human-Readable)

```
2026-02-09T14:32:15.123Z [INFO] MYCEL.embedding - Generated embeddings for 5 chunks (correlation_id=abc123, duration_ms=250)
```

**Format Specification:**
```
{iso_timestamp} [{level}] {component}.{module} - {message} ({context_fields})
```

**Fields:**
- `iso_timestamp`: ISO 8601 with milliseconds and UTC timezone (YYYY-MM-DDTHH:MM:SS.sssZ)
- `level`: Log level (DEBUG/INFO/WARNING/ERROR/CRITICAL)
- `component`: GAIA component name (MYCEL, LOOM, ARGUS, etc.)
- `module`: Python module name (embedding, chunking, workflow_engine)
- `message`: Human-readable log message
- `context_fields`: Key-value pairs for additional context (optional)

### File Format (Machine-Readable JSON)

```json
{
  "timestamp": "2026-02-09T14:32:15.123Z",
  "level": "INFO",
  "component": "MYCEL",
  "module": "embedding",
  "message": "Generated embeddings for 5 chunks",
  "correlation_id": "abc123",
  "duration_ms": 250,
  "metadata": {
    "model": "text-embedding-3-small",
    "dimension": 1536
  }
}
```

**Required Fields:**
- `timestamp`: ISO 8601 UTC timestamp
- `level`: Log level string
- `component`: GAIA component name
- `module`: Python module name
- `message`: Log message

**Optional Fields:**
- `correlation_id`: Trace ID for cross-component tracking
- `duration_ms`: Operation duration in milliseconds
- `cost_usd`: Cost in USD for LLM operations
- `metadata`: Additional structured data (dict)
- `error`: Error details (for ERROR/CRITICAL levels)
- `stack_trace`: Full stack trace (for ERROR/CRITICAL levels)

---

## Structured Logging

### Correlation IDs

Correlation IDs enable tracing requests across multiple GAIA components:

```python
import uuid
from rag_intelligence.logging_config import setup_gaia_logger

logger = setup_gaia_logger("MYCEL")
correlation_id = str(uuid.uuid4())

logger.info("Starting workflow", extra={"correlation_id": correlation_id})
# Pass correlation_id to downstream components
```

### Metadata

Use the `extra` parameter for structured metadata:

```python
logger.info(
    "Embedding generated",
    extra={
        "correlation_id": correlation_id,
        "duration_ms": 250,
        "metadata": {
            "model": "text-embedding-3-small",
            "tokens": 150,
            "dimension": 1536
        }
    }
)
```

### Cost Tracking

For LLM operations, always include cost information:

```python
logger.info(
    "LLM call completed",
    extra={
        "correlation_id": correlation_id,
        "cost_usd": 0.0025,
        "metadata": {
            "model": "claude-sonnet-4-5-20250929",
            "input_tokens": 1500,
            "output_tokens": 800
        }
    }
)
```

---

## File Rotation

### Log File Locations

All GAIA components log to the shared logs directory:

```
X:\Projects\_GAIA\logs\
├── mycel.log              # MYCEL component logs
├── loom.log               # LOOM component logs
├── argus.log              # ARGUS component logs
├── mnemis.log             # MNEMIS component logs
├── jseeker.log            # jSeeker (product) logs
└── ...
```

### Rotation Policy

**Default Configuration:**
- **Max file size**: 10 MB
- **Backup count**: 5 files
- **Total retention**: 50 MB per component

**Rotation Example:**
```
mycel.log         (current, up to 10 MB)
mycel.log.1       (previous, 10 MB)
mycel.log.2       (older, 10 MB)
mycel.log.3       (older, 10 MB)
mycel.log.4       (older, 10 MB)
mycel.log.5       (oldest, 10 MB)
```

When `mycel.log` reaches 10 MB:
1. `mycel.log.5` is deleted
2. `mycel.log.4` → `mycel.log.5`
3. `mycel.log.3` → `mycel.log.4`
4. `mycel.log.2` → `mycel.log.3`
5. `mycel.log.1` → `mycel.log.2`
6. `mycel.log` → `mycel.log.1`
7. New `mycel.log` created

### Custom Rotation

Components with heavy logging can override defaults:

```python
logger = setup_gaia_logger(
    component_name="MYCEL",
    level="INFO",
    max_bytes=20 * 1024 * 1024,  # 20 MB
    backup_count=10               # 10 backups
)
```

---

## ARGUS Telemetry Integration

### Runtime Events

The logging system automatically emits runtime events to ARGUS-compatible JSONL files:

```
X:\Projects\_GAIA\logs\
├── mycel_runtime.jsonl       # ARGUS telemetry for MYCEL
├── loom_runtime.jsonl        # ARGUS telemetry for LOOM
└── ...
```

### Event Format

Runtime events use a simplified format for ARGUS:

```json
{
  "ts": "2026-02-09T14:32:15.123Z",
  "component": "MYCEL",
  "task": "embedding_generation",
  "model": "text-embedding-3-small",
  "cost_usd": 0.0001,
  "input_tokens": 150,
  "output_tokens": 0,
  "duration_ms": 250,
  "status": "success",
  "correlation_id": "abc123"
}
```

### Automatic Emission

When logging with cost information, the logger automatically emits to ARGUS:

```python
# This log entry goes to BOTH console/file AND ARGUS telemetry
logger.info(
    "LLM call completed",
    extra={
        "correlation_id": correlation_id,
        "cost_usd": 0.0025,  # Triggers ARGUS emission
        "duration_ms": 1200,
        "metadata": {
            "task": "resume_adaptation",
            "model": "claude-sonnet-4-5-20250929",
            "input_tokens": 1500,
            "output_tokens": 800
        }
    }
)
```

---

## Implementation

### Quick Start

```python
from rag_intelligence.logging_config import setup_gaia_logger

# Setup logger for your component
logger = setup_gaia_logger("MYCEL")

# Use standard logging
logger.info("Operation started")
logger.warning("Cache miss, using default")
logger.error("API call failed", exc_info=True)
```

### Advanced Configuration

```python
from rag_intelligence.logging_config import setup_gaia_logger

logger = setup_gaia_logger(
    component_name="MYCEL",
    level="DEBUG",              # Set to DEBUG for development
    max_bytes=20 * 1024 * 1024, # 20 MB log files
    backup_count=10,            # Keep 10 backups
    console_enabled=True,       # Enable console logging
    file_enabled=True           # Enable file logging
)
```

### Correlation ID Pattern

```python
import uuid
from rag_intelligence.logging_config import setup_gaia_logger, get_correlation_id, set_correlation_id

logger = setup_gaia_logger("MYCEL")

# Generate correlation ID at entry point
correlation_id = str(uuid.uuid4())
set_correlation_id(correlation_id)

# Logger automatically includes correlation_id
logger.info("Operation started")  # correlation_id=abc123 added automatically

# Pass to downstream components
downstream_function(correlation_id)
```

### Exception Logging

```python
try:
    risky_operation()
except Exception as e:
    logger.error(
        "Operation failed",
        exc_info=True,  # Includes full stack trace
        extra={
            "correlation_id": correlation_id,
            "metadata": {"operation": "risky_operation"}
        }
    )
```

---

## Examples

### Example 1: MYCEL Embedding Service

```python
from rag_intelligence.logging_config import setup_gaia_logger
import time

logger = setup_gaia_logger("MYCEL")

def generate_embeddings(texts: list[str], correlation_id: str) -> list:
    start = time.time()
    logger.info(
        f"Generating embeddings for {len(texts)} texts",
        extra={"correlation_id": correlation_id}
    )

    try:
        embeddings = _call_embedding_api(texts)
        duration_ms = int((time.time() - start) * 1000)

        logger.info(
            "Embeddings generated successfully",
            extra={
                "correlation_id": correlation_id,
                "duration_ms": duration_ms,
                "cost_usd": 0.0001,
                "metadata": {
                    "model": "text-embedding-3-small",
                    "num_texts": len(texts),
                    "total_tokens": sum(len(t.split()) for t in texts)
                }
            }
        )
        return embeddings

    except Exception as e:
        logger.error(
            "Embedding generation failed",
            exc_info=True,
            extra={
                "correlation_id": correlation_id,
                "metadata": {"num_texts": len(texts)}
            }
        )
        raise
```

### Example 2: LOOM Workflow Engine

```python
from rag_intelligence.logging_config import setup_gaia_logger
import uuid

logger = setup_gaia_logger("LOOM")

def execute_workflow(workflow_id: str, inputs: dict) -> dict:
    correlation_id = str(uuid.uuid4())

    logger.info(
        f"Executing workflow: {workflow_id}",
        extra={
            "correlation_id": correlation_id,
            "metadata": {"workflow_id": workflow_id, "num_inputs": len(inputs)}
        }
    )

    for agent_id in workflow.agents:
        logger.debug(
            f"Executing agent: {agent_id}",
            extra={"correlation_id": correlation_id}
        )
        result = execute_agent(agent_id, inputs, correlation_id)

    logger.info(
        "Workflow completed",
        extra={
            "correlation_id": correlation_id,
            "metadata": {"workflow_id": workflow_id, "success": True}
        }
    )

    return result
```

### Example 3: jSeeker Resume Adaptation

```python
from rag_intelligence.logging_config import setup_gaia_logger
import time

logger = setup_gaia_logger("jSeeker")

def adapt_resume(jd: str, resume_blocks: list, correlation_id: str) -> str:
    start = time.time()
    logger.info(
        "Starting resume adaptation",
        extra={
            "correlation_id": correlation_id,
            "metadata": {"num_blocks": len(resume_blocks)}
        }
    )

    # Call LLM
    adapted_resume = llm.call_sonnet(prompt)
    duration_ms = int((time.time() - start) * 1000)
    cost = llm.get_call_cost()

    logger.info(
        "Resume adaptation completed",
        extra={
            "correlation_id": correlation_id,
            "cost_usd": cost,
            "duration_ms": duration_ms,
            "metadata": {
                "task": "resume_adaptation",
                "model": "claude-sonnet-4-5-20250929",
                "input_tokens": 2500,
                "output_tokens": 1200
            }
        }
    )

    return adapted_resume
```

---

## Migration Guide

### Step 1: Add Dependency

Update `requirements.txt`:

```txt
rag-intelligence>=0.2.1  # Includes logging_config
```

### Step 2: Replace Existing Loggers

**Before:**
```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info("Operation started")
```

**After:**
```python
from rag_intelligence.logging_config import setup_gaia_logger

logger = setup_gaia_logger("MYCEL")
logger.info("Operation started")
```

### Step 3: Add Correlation IDs

**Before:**
```python
logger.info("Processing request")
```

**After:**
```python
import uuid

correlation_id = str(uuid.uuid4())
logger.info(
    "Processing request",
    extra={"correlation_id": correlation_id}
)
```

### Step 4: Add Cost Tracking

**Before:**
```python
response = llm.call(prompt)
logger.info("LLM call completed")
```

**After:**
```python
response = llm.call(prompt)
cost = llm.get_call_cost()
logger.info(
    "LLM call completed",
    extra={
        "cost_usd": cost,
        "metadata": {
            "model": "claude-sonnet-4-5-20250929",
            "input_tokens": 1500,
            "output_tokens": 800
        }
    }
)
```

### Step 5: Test

```bash
# Check logs are written
ls X:\Projects\_GAIA\logs\

# Verify JSON format
cat X:\Projects\_GAIA\logs\mycel.log | head -n 1 | python -m json.tool

# Verify ARGUS telemetry
cat X:\Projects\_GAIA\logs\mycel_runtime.jsonl | head -n 1 | python -m json.tool
```

---

## Best Practices

### DO

- Use correlation IDs for all multi-step operations
- Include cost information for all LLM operations
- Use structured metadata for machine-readable context
- Log at entry and exit of major operations
- Use `exc_info=True` for exception logging

### DON'T

- Log sensitive data (API keys, PHI, PII)
- Log at DEBUG level in production (use INFO)
- Include large payloads in log messages (log sizes instead)
- Use print() statements (use logger.debug() instead)
- Hard-code component names (use parameter)

### Security

- **Never log API keys**: Use `logger.debug("Using API key: ***")` if needed
- **No PHI in logs**: Use anonymized IDs instead of patient names
- **No PII in logs**: Hash or mask user identifiers
- **Sanitize inputs**: Don't log raw user input that might contain secrets

---

## Troubleshooting

### Logs not appearing

**Check log directory exists:**
```python
from pathlib import Path
log_dir = Path("X:/Projects/_GAIA/logs")
log_dir.mkdir(parents=True, exist_ok=True)
```

**Check logger level:**
```python
logger = setup_gaia_logger("MYCEL", level="DEBUG")
```

### JSON parsing errors

**Validate JSON format:**
```bash
cat X:\Projects\_GAIA\logs\mycel.log | python -m json.tool
```

**Check for multi-line messages:**
```python
# Don't do this - breaks JSON parsing
logger.info("Line 1\nLine 2")

# Do this instead
logger.info("Line 1. Line 2")
```

### Log rotation not working

**Check file permissions:**
```bash
# Windows
icacls X:\Projects\_GAIA\logs\mycel.log

# Should have write permissions
```

**Check disk space:**
```bash
# Windows
Get-PSDrive X | Select-Object Used,Free
```

---

## References

- **GAIA Constitution**: `X:\Projects\_GAIA\GAIA_BIBLE.md`
- **GAIA Registry**: `X:\Projects\_GAIA\registry.json`
- **GECO Architecture**: `X:\Projects\_GAIA\docs\GECO_ARCHITECTURE.md`
- **ARGUS Telemetry**: `X:\Projects\_GAIA\_ARGUS\docs\TELEMETRY.md`
- **Python Logging Docs**: https://docs.python.org/3/library/logging.html

---

**Document Maintenance:**
- This document is the authoritative logging standard for GAIA
- All GAIA components MUST comply with this standard
- For changes, propose via GAIA governance process
- Last Updated: 2026-02-09

**Contributors:**
- Author: Claude Code (Sonnet 4.5)
- Reviewer: Fed (GAIA Architect)
- Priority: HIGH (GECO Audit Item)
