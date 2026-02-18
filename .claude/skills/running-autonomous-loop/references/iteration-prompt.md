# Iteration Prompt Template

When the Stop hook re-feeds, Claude receives this context:

```
You are in a GAIA Loop (iteration {N}/{max}).

Task: {task_description}
Completion Promise: {completion_promise}

INSTRUCTIONS:
1. Read .gaia_loop_plan.md for prior progress
2. Read .gaia_loop_state for loop status
3. Continue working on the task from where you left off
4. Update .gaia_loop_plan.md with progress
5. Run tests to verify progress
6. If ALL success criteria are met, output: {completion_promise}
7. If blocked after 3 attempts on the same issue, document in plan and move on

AUTONOMOUS TASK RULES:
- Define clear completion criteria (testable, not subjective)
- Use phased decomposition (Phase 1, Phase 2, ...)
- Self-correct: if tests fail, read error, fix, re-run
- Escape hatch: if blocked after 3 attempts, document blockers in plan
- Never use subjective completion ("make it good") — use verifiable checks
```
