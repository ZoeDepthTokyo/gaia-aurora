#!/usr/bin/env bash
# GAIA Loop Stop Hook
# Intercepts Claude Code session exit and re-feeds the prompt if loop is active.
# Only active when .gaia_loop_state exists and status is "running".

set -euo pipefail

STATE_FILE="X:/projects/_GAIA/.gaia_loop_state"
PLAN_FILE="X:/projects/_GAIA/.gaia_loop_plan.md"
LOG_FILE="X:/projects/_GAIA/.gaia_loop_log"

# If no state file, loop is not active — allow normal exit
if [ ! -f "$STATE_FILE" ]; then
    exit 0
fi

# Read loop state
STATUS=$(python -c "import json; print(json.load(open('$STATE_FILE'))['status'])" 2>/dev/null || echo "unknown")
CURRENT=$(python -c "import json; print(json.load(open('$STATE_FILE'))['current_iteration'])" 2>/dev/null || echo "0")
MAX=$(python -c "import json; print(json.load(open('$STATE_FILE'))['max_iterations'])" 2>/dev/null || echo "25")
PROMISE=$(python -c "import json; print(json.load(open('$STATE_FILE'))['completion_promise'])" 2>/dev/null || echo "GAIA_LOOP_COMPLETE")
TASK=$(python -c "import json; print(json.load(open('$STATE_FILE'))['task'])" 2>/dev/null || echo "Unknown task")

# Check if loop should continue
if [ "$STATUS" != "running" ]; then
    echo "[GAIA Loop] Status is '$STATUS' — exiting loop."
    exit 0
fi

# Check max iterations
if [ "$CURRENT" -ge "$MAX" ]; then
    python -c "
import json
state = json.load(open('$STATE_FILE'))
state['status'] = 'MAX_ITERATIONS'
json.dump(state, open('$STATE_FILE', 'w'), indent=2)
"
    echo "[GAIA Loop] Max iterations ($MAX) reached. Loop complete."
    exit 0
fi

# Run circuit breaker check
python "X:/projects/_GAIA/runtime/circuit_breaker.py" "$STATE_FILE" 2>/dev/null
BREAKER_STATUS=$(python -c "import json; print(json.load(open('$STATE_FILE'))['status'])" 2>/dev/null || echo "running")

if [ "$BREAKER_STATUS" != "running" ]; then
    echo "[GAIA Loop] Circuit breaker triggered. Loop halted."
    exit 0
fi

# Loop continues — re-feed prompt via exit code 1 (blocks exit)
# and provide context for next iteration
NEXT=$((CURRENT + 1))

echo "[GAIA Loop] Iteration $NEXT/$MAX starting..."
echo ""
echo "You are in a GAIA Loop (iteration $NEXT/$MAX)."
echo ""
echo "Task: $TASK"
echo "Completion Promise: $PROMISE"
echo ""
echo "INSTRUCTIONS:"
echo "1. Read .gaia_loop_plan.md for prior progress"
echo "2. Read .gaia_loop_state for loop status"
echo "3. Continue working on the task from where you left off"
echo "4. Update .gaia_loop_plan.md with progress"
echo "5. Run tests to verify progress"
echo "6. If ALL success criteria are met, output: $PROMISE"
echo "7. If blocked after 3 attempts on the same issue, document blockers in plan"

# Exit code 1 tells Claude Code Stop hook to block exit and re-feed
exit 1
