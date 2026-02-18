# Circuit Breaker Rules

The circuit breaker (implemented in `runtime/circuit_breaker.py`) monitors:

| Condition | Threshold | Action |
|---|---|---|
| No file changes | 3 consecutive iterations | Halt loop |
| Same error repeated | 5 occurrences of identical error | Halt loop |
| Rate limit | `--max-calls` exceeded | Halt loop |

When triggered, the circuit breaker writes `"status": "CIRCUIT_BREAKER_OPEN"` to `.gaia_loop_state`, which the Stop hook reads to prevent re-feeding.

## Iteration-Aware Plan File

The `.gaia_loop_plan.md` file serves as cross-iteration memory. Claude reads it at the start of each iteration instead of re-reading all files blindly.

Format:
```markdown
# Loop Plan: {task_description}

**Started**: 2026-02-13T14:30:00
**Max Iterations**: 15
**Completion Promise**: ALL_TESTS_PASS

## Iteration Log
- [x] Iteration 1: Scaffolded project structure (3 files created)
- [x] Iteration 2: Wrote failing tests (4 tests, 4 failing)
- [x] Iteration 3: Implemented parse_csv(), 2/4 tests pass
- [ ] Iteration 4: Fix remaining test failures

## Current Blockers
- test_parse_csv fails: FileNotFoundError on sample.csv

## Next Steps
- Create tests/fixtures/sample.csv with test data
- Fix parse_csv() to handle relative paths
```
