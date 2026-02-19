"""GAIA Loop Circuit Breaker — detects stuck loops and halts execution.

Monitors iteration progress and triggers a halt when:
- 3 consecutive iterations with zero file changes
- 5 iterations with the same error pattern
- API call budget exceeded (rate limiting)

Usage:
    python circuit_breaker.py <state_file_path>

Called by stop_hook.sh between iterations. Updates state file status
to "CIRCUIT_BREAKER_OPEN" or "RATE_LIMITED" when triggered.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

# Thresholds
MAX_NO_CHANGE_ITERATIONS = 3
MAX_SAME_ERROR_COUNT = 5
DEFAULT_MAX_CALLS = 200

_GAIA_ROOT = Path(os.getenv("GAIA_ROOT", Path(__file__).parent.parent))
LOG_FILE = _GAIA_ROOT / ".gaia_loop_log"


def _get_changed_files() -> list[str]:
    """Get list of files changed since last commit (unstaged + staged)."""
    try:
        result = subprocess.run(
            ["git", "diff", "--name-only"],
            capture_output=True,
            text=True,
            cwd=str(_GAIA_ROOT),
            timeout=10,
        )
        files = [f.strip() for f in result.stdout.strip().split("\n") if f.strip()]
        return files
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return []


def _get_test_errors() -> str | None:
    """Extract error signature from last test run if available.

    Returns a normalized error string for comparison, or None if no errors.
    """
    # Read the plan file for error mentions
    plan_file = _GAIA_ROOT / ".gaia_loop_plan.md"
    if not plan_file.exists():
        return None

    content = plan_file.read_text(encoding="utf-8")
    # Look for "Current Blockers" section
    if "## Current Blockers" not in content:
        return None

    blockers_start = content.index("## Current Blockers")
    blockers_end = content.find("##", blockers_start + 1)
    if blockers_end == -1:
        blockers_end = len(content)

    blockers = content[blockers_start:blockers_end].strip()
    # Normalize: remove timestamps, line numbers, whitespace variations
    normalized = " ".join(blockers.split())
    return normalized if len(normalized) > 30 else None


def _log_event(iteration: int, event: str, details: str = "") -> None:
    """Append event to .gaia_loop_log."""
    timestamp = datetime.now(timezone.utc).isoformat()
    entry = f"[{timestamp}] Iteration {iteration}: {event}"
    if details:
        entry += f" — {details}"
    entry += "\n"

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(entry)


def check(state_file_path: str) -> dict:
    """Run circuit breaker checks and update state file if triggered.

    Returns the updated state dict.
    """
    state_path = Path(state_file_path)
    if not state_path.exists():
        return {"status": "no_state_file"}

    state = json.loads(state_path.read_text(encoding="utf-8"))
    iteration = state.get("current_iteration", 0)
    max_calls = state.get("max_calls", DEFAULT_MAX_CALLS)
    total_calls = state.get("total_api_calls", 0)
    cb = state.setdefault(
        "circuit_breaker",
        {
            "consecutive_no_change": 0,
            "error_history": [],
            "triggered": False,
        },
    )

    # --- Check 1: Rate limit ---
    if total_calls >= max_calls:
        state["status"] = "RATE_LIMITED"
        cb["triggered"] = True
        _log_event(iteration, "RATE_LIMITED", f"{total_calls}/{max_calls} calls used")
        state_path.write_text(json.dumps(state, indent=2), encoding="utf-8")
        return state

    # --- Check 2: No file changes ---
    changed_files = _get_changed_files()
    if not changed_files:
        cb["consecutive_no_change"] = cb.get("consecutive_no_change", 0) + 1
        _log_event(
            iteration,
            "NO_CHANGES",
            f"{cb['consecutive_no_change']}/{MAX_NO_CHANGE_ITERATIONS} consecutive",
        )
    else:
        cb["consecutive_no_change"] = 0
        _log_event(iteration, "FILES_CHANGED", f"{len(changed_files)} files")

    if cb["consecutive_no_change"] >= MAX_NO_CHANGE_ITERATIONS:
        state["status"] = "CIRCUIT_BREAKER_OPEN"
        cb["triggered"] = True
        _log_event(
            iteration,
            "CIRCUIT_BREAKER",
            f"No file changes for {MAX_NO_CHANGE_ITERATIONS} consecutive iterations",
        )
        state_path.write_text(json.dumps(state, indent=2), encoding="utf-8")
        return state

    # --- Check 3: Repeated errors ---
    current_error = _get_test_errors()
    error_history: list[str] = cb.get("error_history", [])

    if current_error:
        error_history.append(current_error)
        # Keep only last 10 entries
        if len(error_history) > 10:
            error_history = error_history[-10:]
        cb["error_history"] = error_history

        # Count occurrences of the current error pattern
        same_error_count = sum(1 for e in error_history if e == current_error)
        if same_error_count >= MAX_SAME_ERROR_COUNT:
            state["status"] = "CIRCUIT_BREAKER_OPEN"
            cb["triggered"] = True
            _log_event(
                iteration,
                "CIRCUIT_BREAKER",
                f"Same error repeated {same_error_count} times",
            )
            state_path.write_text(json.dumps(state, indent=2), encoding="utf-8")
            return state

    # --- All checks passed ---
    state_path.write_text(json.dumps(state, indent=2), encoding="utf-8")
    return state


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python circuit_breaker.py <state_file_path>", file=sys.stderr)
        sys.exit(1)

    state = check(sys.argv[1])
    status = state.get("status", "unknown")

    if status in ("CIRCUIT_BREAKER_OPEN", "RATE_LIMITED"):
        print(f"[Circuit Breaker] Loop halted: {status}")
        sys.exit(0)


if __name__ == "__main__":
    main()
