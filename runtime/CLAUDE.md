# GAIA Runtime — Background Task Runner

> **Context**: Read `GAIA_MANIFEST.md` first for ecosystem state.
> This service is part of the GAIA ecosystem.

## Role
Scheduled background task infrastructure for ecosystem maintenance. Runs periodic health checks (WARDEN scans, ARGUS monitoring, cache cleanup) with zero reactive overhead. Also provides the change tracking hook used by `/reconcile`.

**Current Version:** 1.0.0

## Quick Start
```bash
cd X:/Projects/_GAIA/runtime

# Run all tasks once
python task_runner.py --once

# List configured tasks
python task_runner.py --list

# Start scheduler (requires apscheduler)
python task_runner.py
```

## Directory Structure
```
runtime/
├── task_runner.py          # Main scheduler (3 built-in tasks)
├── track_change.py         # PostToolUse hook for /reconcile
├── contract_validator.py   # Contract validation logic
├── verify_runtime.py       # Runtime health verification
├── tests/                  # Test suite
├── __init__.py             # Package init
└── README.md               # Documentation
```

## Built-in Tasks
| Task | Schedule | Description |
|------|----------|-------------|
| `warden_scan` | daily | Run WARDEN governance scan |
| `health_check` | hourly | Check component health |
| `stale_cache` | every 15m | Clean expired cache files |

## Integration Points
- **WARDEN**: Governance scanning via CLI
- **ARGUS**: Health telemetry
- **MNEMIS**: Pattern storage
- **Hooks**: `track_change.py` is wired as PostToolUse hook in `.claude/settings.json`

## Key Files
- `task_runner.py` — Scheduler with APScheduler (optional graceful fallback)
- `track_change.py` — Logs component edits to `.gaia_changes` for `/reconcile`
- `contract_validator.py` — Validates component contracts

## Testing
```bash
cd X:/Projects/_GAIA/runtime
pytest tests/
```

## When I Change
<!-- CASCADE_MAP: machine-readable, do not edit manually -->
- registry.json: version field → auto
- GAIA_MANIFEST.md: component table row → auto
- GECO_REVIEW_MATRIX.md: component row → auto
- VERSION_LOG.md: new entry if tasks changed → ask
<!-- END_CASCADE_MAP -->

## DO NOT
- Remove `track_change.py` — it's wired into Claude Code hooks
- Run scheduler without checking port/process conflicts first
