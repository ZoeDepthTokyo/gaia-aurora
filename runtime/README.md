# GAIA Runtime - Background Task Infrastructure

Provides scheduled task execution for ecosystem maintenance with zero reactive monitoring overhead.

## Features

- **WARDEN compliance scans** (daily) - Scans all registered projects for compliance issues
- **ARGUS health checks** (hourly) - Verifies project existence, git status, test presence
- **Stale cache cleanup** (every 15 minutes) - Detects __pycache__ directories
- **Extensible task registry** - Easy to add custom tasks

## Quick Start

### List all registered tasks

```powershell
cd X:\Projects\_GAIA
python -m runtime.task_runner --list
```

### Run all tasks once (no scheduler)

```powershell
python -m runtime.task_runner --once
```

Output is JSON with results from each task.

### Run continuous scheduler (requires APScheduler)

```powershell
pip install apscheduler
python -m runtime.task_runner
```

Press Ctrl+C to stop.

## Adding Custom Tasks

Edit `runtime/task_runner.py` and register your task:

```python
def task_my_custom_check():
    """My custom maintenance task."""
    # Your logic here
    return {"status": "ok"}

register_task(
    name="my_check",
    func=task_my_custom_check,
    schedule="hourly",  # or "daily", "every_15m"
    description="My custom health check"
)
```

## Built-in Tasks

| Task Name | Schedule | Description |
|-----------|----------|-------------|
| `warden_scan` | daily | WARDEN compliance scan across all projects |
| `health_check` | hourly | Ecosystem health check (git, tests, CLAUDE.md) |
| `stale_cache` | every_15m | Detect stale __pycache__ directories |

## Architecture

- **Task Registry**: Global `REGISTERED_TASKS` dict tracks all tasks
- **Scheduler**: APScheduler for interval-based execution
- **Fallback Mode**: Works without APScheduler using `--once` mode
- **Graceful Shutdown**: SIGINT/SIGTERM handling for clean exit

## Testing

```powershell
cd X:\Projects\_GAIA\runtime
python -m pytest tests/test_task_runner.py -v
```

All tests passing:
- Task registration
- Execution flow
- Exception handling
- Health check structure
- CLI modes

## Dependencies

- **Required**: Python 3.10+
- **Optional**: `apscheduler` (for continuous scheduler mode)

Without APScheduler, the runner automatically falls back to `--once` mode.

## Integration with GAIA Components

The task runner reads from `X:/Projects/_GAIA/registry.json` to discover all projects. Each task iterates over registered projects and performs checks.

### WARDEN Integration

Imports `scanner.ComplianceScanner` from `X:/Projects/_GAIA/_WARDEN` and runs compliance checks on all projects.

### Future Integrations

- **MNEMIS**: Daily memory promotion evaluation
- **ARGUS**: Runtime telemetry health checks
- **RAVEN**: Autonomous investigation triggers

## Notes

- All tasks log to `gaia.runtime` logger
- Task results include execution status and timestamps
- Registry must exist at `X:/Projects/_GAIA/registry.json`
- Tasks gracefully handle missing projects or components
