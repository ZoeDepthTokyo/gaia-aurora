---
name: running-autonomous-loop
description: "[CONTEXT] Runs autonomous iteration loops with GAIA governance guardrails including circuit breaker, HITL gates, and cost tracking. Use for well-defined, test-verifiable tasks like greenfield implementations, bug fixes with reproducible failures, or refactoring with existing test coverage. Triggers on: autonomous, loop, iterate, batch, auto-fix. Why: hands-free iteration with safety guardrails."
---

# /gaia-loop — Autonomous Iteration with GAIA Governance

## Usage
```
/gaia-loop "<task description>" [--max-iterations N] [--max-calls N] [--completion-promise TEXT]
```

**Flags:**
- `--max-iterations N`: Maximum loop iterations (default: 25)
- `--max-calls N`: API call budget for the session (default: 200)
- `--completion-promise TEXT`: Exit signal phrase (default: `GAIA_LOOP_COMPLETE`)

## When to Use
Use for well-defined, test-verifiable tasks that benefit from autonomous iteration:
- Greenfield implementations with clear test criteria
- Bug fixes with reproducible test failures
- Refactoring with existing test coverage
- Multi-step scaffolding tasks

Do NOT use for:
- Exploratory/research tasks (no clear "done" signal)
- Tasks requiring human judgment (design decisions, UX review)
- Tasks touching RED-tier files (GAIA_BIBLE.md, constitutional changes)

## How It Works

The loop uses a Claude Code Stop hook (`stop_hook.sh`) that intercepts session exit and re-feeds the prompt. Each iteration, Claude reads its own prior modifications and continues working.

### Safety Guardrails (GAIA Additions)
1. **Circuit breaker**: Halts on 3 iterations with zero file changes or 5 with same error
2. **HITL gate**: Loop pauses if any iteration touches RED-tier files (registry.json, GAIA_BIBLE.md)
3. **Cost tracking**: Each iteration logged with cumulative API call count
4. **Rate limit**: Hard stop at `--max-calls` budget
5. **Change tracking**: All edits logged via existing `.gaia_changes` PostToolUse hook
6. **Constitutional compliance**: All PreToolUse hooks remain active (registry block, BIBLE warn)

## Workflow

### Step 1: INITIALIZE

Parse arguments from the invocation:
```
Task: <task description>
Max Iterations: <N, default 25>
Max Calls: <N, default 200>
Completion Promise: <TEXT, default GAIA_LOOP_COMPLETE>
```

Create the loop state file `.gaia_loop_state` (gitignored):
```json
{
  "task": "<description>",
  "max_iterations": 25,
  "max_calls": 200,
  "completion_promise": "GAIA_LOOP_COMPLETE",
  "current_iteration": 0,
  "total_api_calls": 0,
  "status": "running",
  "started_at": "<ISO timestamp>",
  "circuit_breaker": {
    "consecutive_no_change": 0,
    "error_history": [],
    "triggered": false
  }
}
```

Create the loop plan file `.gaia_loop_plan.md`:
```markdown
# Loop Plan: <task description>

**Started**: <timestamp>
**Max Iterations**: <N>
**Completion Promise**: <promise>

## Iteration Log
<!-- Updated by Claude each iteration -->

## Current Blockers
<!-- Populated when issues arise -->

## Next Steps
<!-- Claude's plan for next iteration -->
```

Register the Stop hook by writing to `.claude/settings.local.json` (session-only):
```json
{
  "hooks": {
    "Stop": [{
      "hooks": [{
        "type": "command",
        "command": "bash X:/projects/_GAIA/.claude/skills/gaia-loop/scripts/stop_hook.sh"
      }]
    }]
  }
}
```

### Step 2: EXECUTE ITERATION

At the start of each iteration:

1. **Read `.gaia_loop_state`** — check status, iteration count, call budget
2. **Read `.gaia_loop_plan.md`** — understand prior progress, blockers, next steps
3. **Increment iteration counter** in state file
4. **Work on the task** — follow the plan, implement, test
5. **Run tests** if applicable: `python -m pytest <test_file> -v`
6. **Update `.gaia_loop_plan.md`** with:
   - What was done this iteration (checkbox item)
   - Any new blockers discovered
   - Next steps for subsequent iteration
7. **Check completion**: If all success criteria met, write the completion promise

### Step 3: CHECK EXIT CONDITIONS

After each iteration, evaluate (in order):

1. **Completion promise found?** → Exit cleanly with summary
2. **Max iterations reached?** → Exit with "MAX_ITERATIONS" status
3. **Circuit breaker triggered?** → Exit with "CIRCUIT_BREAKER" status
4. **Rate limit exceeded?** → Exit with "RATE_LIMITED" status
5. **HITL interrupt?** → Pause loop, present situation to user
6. **None of the above** → Continue to next iteration (Stop hook re-feeds prompt)

### Step 4: COMPLETION REPORT

When exiting for any reason, output:

```
GAIA Loop Report
================
Task: <description>
Status: <COMPLETE | MAX_ITERATIONS | CIRCUIT_BREAKER | RATE_LIMITED | HITL_PAUSED>
Iterations: <completed> / <max>
API Calls: <used> / <budget>
Files Modified: <count>
Tests: <pass_count> passing, <fail_count> failing

Iteration Summary:
  [x] Iteration 1: <what was done>
  [x] Iteration 2: <what was done>
  ...

Remaining Work (if incomplete):
  - <blocker or unfinished item>
```

Then clean up:
- Remove Stop hook from `.claude/settings.local.json`
- Keep `.gaia_loop_plan.md` for debugging (gitignored)
- Keep `.gaia_loop_state` for post-mortem (gitignored)

## Circuit Breaker Rules

Monitors 3 conditions: no file changes (3 iterations), same error repeated (5x), rate limit exceeded. Writes `CIRCUIT_BREAKER_OPEN` to state file to prevent re-feeding.

For full rules table and plan file format, see references/circuit-breaker-rules.md.

## Prompt Template for Each Iteration

The Stop hook re-feeds a structured prompt with task, completion promise, and autonomous task rules.

For the full iteration prompt template, see references/iteration-prompt.md.

## Cleanup

To cancel a running loop:
```
# Delete the state file — Stop hook will see missing file and not re-feed
rm .gaia_loop_state
# Or set status manually
# Edit .gaia_loop_state: "status": "cancelled"
```

Files created during loop (all gitignored):
- `.gaia_loop_state` — JSON state tracking
- `.gaia_loop_plan.md` — iteration log and plan
- `.gaia_loop_log` — circuit breaker event log
