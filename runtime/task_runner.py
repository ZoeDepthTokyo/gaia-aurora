"""GAIA background task runner.

Lightweight scheduler with task registry. No external deps.
Supports: run_once (execute all due tasks), run_all (force all), list tasks.

Usage (class-based):
    from runtime.task_runner import TaskRunner
    runner = TaskRunner()
    runner.register("my_task", my_fn, interval_seconds=3600)
    runner.run_once()   # execute tasks whose interval has elapsed
    runner.run_all()    # force-execute every task
    runner.list_tasks() # returns list[ScheduledTask]
    runner.get_results() # returns last execution results

Usage (CLI):
    python -m runtime.task_runner --once    # run due tasks and exit
    python -m runtime.task_runner --all     # force all tasks and exit
    python -m runtime.task_runner --list    # list tasks
    python -m runtime.task_runner --daemon  # loop forever (Ctrl-C to stop)
"""

from __future__ import annotations

import argparse
import logging
import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Callable, Dict, List, Optional

logger = logging.getLogger("gaia.runtime.task_runner")


# ---------------------------------------------------------------------------
# ScheduledTask dataclass
# ---------------------------------------------------------------------------


@dataclass
class ScheduledTask:
    """A single registered background task.

    Attributes:
        name: Unique task identifier.
        interval_seconds: How often the task should run. 0 means every call.
        fn: Callable invoked when the task executes.
        last_run: Unix timestamp of the most recent execution, or None.
        enabled: When False the task is skipped by run_once/run_all.
    """

    name: str
    interval_seconds: float
    fn: Callable[[], Any]
    last_run: Optional[float] = field(default=None)
    enabled: bool = field(default=True)

    def is_due(self) -> bool:
        """Return True when the task should execute now.

        Returns:
            True if interval_seconds == 0, if the task has never run, or if
            at least interval_seconds seconds have elapsed since last_run.
        """
        if self.interval_seconds == 0:
            return True
        if self.last_run is None:
            return True
        return (time.time() - self.last_run) >= self.interval_seconds


# ---------------------------------------------------------------------------
# TaskRunner
# ---------------------------------------------------------------------------


class TaskRunner:
    """Manages a registry of ScheduledTask objects and drives execution.

    No external dependencies — uses stdlib time for interval tracking.

    Args:
        register_defaults: When True (default) the 5 built-in GAIA
            maintenance tasks are pre-registered on construction.
    """

    def __init__(self, register_defaults: bool = True) -> None:
        """Initialise the runner, optionally loading default tasks.

        Args:
            register_defaults: Pre-register the 5 built-in tasks when True.
        """
        self._tasks: Dict[str, ScheduledTask] = {}
        self._results: Dict[str, Dict[str, Any]] = {}

        if register_defaults:
            self._register_default_tasks()

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def register(
        self,
        name: str,
        fn: Callable[[], Any],
        interval_seconds: float,
    ) -> None:
        """Add or replace a task in the registry.

        Args:
            name: Unique task identifier. Re-registering an existing name
                replaces the previous entry.
            fn: Zero-argument callable executed when the task is due.
            interval_seconds: Minimum seconds between executions.
                Pass 0 to execute on every run_once call.
        """
        self._tasks[name] = ScheduledTask(
            name=name,
            interval_seconds=interval_seconds,
            fn=fn,
        )

    def run_once(self) -> int:
        """Execute all enabled tasks that are currently due.

        Exceptions raised by individual tasks are caught, logged, and stored
        in results; they do not propagate to the caller.

        Returns:
            Number of tasks that were executed (attempted, whether or not
            they succeeded).
        """
        executed = 0
        for task in self._tasks.values():
            if not task.enabled:
                continue
            if not task.is_due():
                continue
            self._execute(task)
            executed += 1
        return executed

    def run_all(self) -> int:
        """Force-execute every enabled task regardless of interval.

        Ignores last_run — useful for ad-hoc maintenance runs.

        Returns:
            Number of tasks executed.
        """
        executed = 0
        for task in self._tasks.values():
            if not task.enabled:
                continue
            self._execute(task)
            executed += 1
        return executed

    def list_tasks(self) -> List[ScheduledTask]:
        """Return all registered tasks.

        Returns:
            List of ScheduledTask instances in registration order.
        """
        return list(self._tasks.values())

    def get_results(self) -> Dict[str, Dict[str, Any]]:
        """Return the results from the most recent execution of each task.

        Returns:
            Dict mapping task name to a result dict containing at minimum
            ``status`` (``"success"`` | ``"error"``) and ``timestamp`` (ISO
            8601 string). Error results also include an ``"error"`` key with
            the exception message. Successful results may include an
            ``"output"`` key with whatever the task callable returned.
        """
        return dict(self._results)

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _execute(self, task: ScheduledTask) -> None:
        """Run a single task, capture its result, and update last_run.

        Args:
            task: The ScheduledTask to execute.
        """
        timestamp = datetime.now(timezone.utc).isoformat()
        try:
            output = task.fn()
            task.last_run = time.time()
            self._results[task.name] = {
                "task": task.name,
                "status": "success",
                "timestamp": timestamp,
                "output": output,
            }
            logger.debug("Task %s completed successfully.", task.name)
        except Exception as exc:  # noqa: BLE001
            task.last_run = time.time()
            self._results[task.name] = {
                "task": task.name,
                "status": "error",
                "timestamp": timestamp,
                "error": str(exc),
            }
            logger.error("Task %s raised an exception: %s", task.name, exc)

    def _register_default_tasks(self) -> None:
        """Register the 5 built-in GAIA maintenance tasks."""
        self.register("warden_scan", _task_warden_scan, interval_seconds=86400)
        self.register("health_check", _task_health_check, interval_seconds=3600)
        self.register("stale_cache_cleanup", _task_stale_cache_cleanup, interval_seconds=900)
        self.register("guardrail_check", _task_guardrail_check, interval_seconds=21600)
        self.register("baseline_update", _task_baseline_update, interval_seconds=86400)


# ---------------------------------------------------------------------------
# Built-in task implementations
# ---------------------------------------------------------------------------

_GAIA_ROOT = "X:/Projects/_GAIA"


def _task_warden_scan() -> Dict[str, Any]:
    """Run WARDEN SecretScanner on the GAIA root directory.

    Attempts to import ``warden.scanner.SecretScanner``; falls back to a
    warning result when WARDEN is not installed.

    Returns:
        Result dict with keys ``task``, ``status``, ``message``, and
        ``timestamp``.
    """
    from pathlib import Path

    timestamp = datetime.now(timezone.utc).isoformat()
    registry_path = Path(_GAIA_ROOT) / "registry.json"

    if not registry_path.exists():
        return {
            "task": "warden_scan",
            "status": "skipped",
            "message": "registry.json not found",
            "timestamp": timestamp,
        }

    try:
        import sys

        sys.path.insert(0, str(Path(_GAIA_ROOT) / "_WARDEN"))
        from warden.scanner import SecretScanner  # type: ignore[import]

        scanner = SecretScanner()
        issues = scanner.scan(Path(_GAIA_ROOT))
        return {
            "task": "warden_scan",
            "status": "success",
            "message": f"{len(issues)} issues found",
            "timestamp": timestamp,
            "issues": len(issues),
        }
    except ImportError:
        return {
            "task": "warden_scan",
            "status": "skipped",
            "message": "WARDEN not installed — skipping scan",
            "timestamp": timestamp,
        }


def _task_health_check() -> Dict[str, Any]:
    """Check git status of all submodule paths listed in registry.json.

    Returns:
        Result dict with per-component health booleans plus top-level
        ``task``, ``status``, ``message``, and ``timestamp`` keys.
    """
    import json
    from pathlib import Path

    timestamp = datetime.now(timezone.utc).isoformat()
    registry_path = Path(_GAIA_ROOT) / "registry.json"

    if not registry_path.exists():
        return {
            "task": "health_check",
            "status": "error",
            "message": "registry.json not found",
            "timestamp": timestamp,
        }

    registry = json.loads(registry_path.read_text(encoding="utf-8"))
    components: Dict[str, Any] = {}

    for key, project in registry.get("projects", {}).items():
        path = Path(project.get("path", ""))
        components[key] = {
            "exists": path.exists(),
            "has_git": (path / ".git").exists() if path.exists() else False,
            "has_tests": bool(list(path.glob("tests/test_*.py"))) if path.exists() else False,
            "has_claude_md": (path / "CLAUDE.md").exists() if path.exists() else False,
        }

    return {
        "task": "health_check",
        "status": "success",
        "message": f"{len(components)} components checked",
        "timestamp": timestamp,
        "components": components,
    }


def _task_stale_cache_cleanup() -> Dict[str, Any]:
    """Remove __pycache__ directories older than 24 hours across GAIA root.

    Returns:
        Result dict with ``removed`` count plus ``task``, ``status``,
        ``message``, and ``timestamp`` keys.
    """
    from pathlib import Path

    timestamp = datetime.now(timezone.utc).isoformat()
    gaia_root = Path(_GAIA_ROOT)
    cutoff = time.time() - 86400  # 24 hours
    removed = 0
    scanned = 0

    for cache_dir in gaia_root.rglob("__pycache__"):
        scanned += 1
        try:
            stat = cache_dir.stat()
            if stat.st_mtime < cutoff:
                # Remove .pyc files inside; leave directory skeleton
                for pyc in cache_dir.glob("*.pyc"):
                    pyc.unlink(missing_ok=True)
                    removed += 1
        except OSError:
            pass

    return {
        "task": "stale_cache_cleanup",
        "status": "success",
        "message": f"Scanned {scanned} __pycache__ dirs, removed {removed} stale .pyc files",
        "timestamp": timestamp,
        "scanned": scanned,
        "removed": removed,
    }


def _task_guardrail_check() -> Dict[str, Any]:
    """Run GuardrailEngine on all registered GAIA components.

    Attempts to import ``warden.guardrails.GuardrailEngine``; falls back to
    a skipped result when WARDEN is not installed.

    Returns:
        Result dict with ``task``, ``status``, ``message``, and ``timestamp``.
    """
    timestamp = datetime.now(timezone.utc).isoformat()
    from pathlib import Path

    try:
        import sys

        sys.path.insert(0, str(Path(_GAIA_ROOT) / "_WARDEN"))
        from warden.guardrails import GuardrailEngine  # type: ignore[import]

        engine = GuardrailEngine()
        results = engine.check_all(Path(_GAIA_ROOT))
        violations = sum(1 for r in results if not r.passed)
        return {
            "task": "guardrail_check",
            "status": "success",
            "message": f"{violations} guardrail violations across {len(results)} checks",
            "timestamp": timestamp,
            "violations": violations,
            "total_checks": len(results),
        }
    except ImportError:
        return {
            "task": "guardrail_check",
            "status": "skipped",
            "message": "GuardrailEngine not available — WARDEN not installed",
            "timestamp": timestamp,
        }


def _task_baseline_update() -> Dict[str, Any]:
    """Placeholder — persist anomaly detection baseline to disk.

    This task is a stub for future ARGUS anomaly baseline persistence.
    When ARGUS exposes a baseline API this function will call it.

    Returns:
        Result dict with ``task``, ``status``, ``message``, and ``timestamp``.
    """
    timestamp = datetime.now(timezone.utc).isoformat()
    return {
        "task": "baseline_update",
        "status": "skipped",
        "message": "Baseline persistence not yet implemented — placeholder task",
        "timestamp": timestamp,
    }


# ---------------------------------------------------------------------------
# Legacy module-level API (backward compatibility)
# ---------------------------------------------------------------------------
# These module-level names mirror the old task_runner interface.  Existing
# callers that do ``from task_runner import register_task, run_all_once``
# continue to work without modification.

REGISTERED_TASKS: Dict[str, dict] = {}


def register_task(
    name: str,
    func: Callable[[], Any],
    schedule: str,
    description: str = "",
) -> None:
    """Register a background task in the module-level registry (legacy API).

    Args:
        name: Unique task identifier.
        func: Callable to execute.
        schedule: Human-readable schedule string (e.g. ``"hourly"``, ``"daily"``).
        description: Human-readable description.
    """
    REGISTERED_TASKS[name] = {
        "func": func,
        "schedule": schedule,
        "description": description,
        "last_run": None,
        "last_status": None,
    }


def run_all_once() -> Dict[str, Any]:
    """Execute every task in the module-level registry exactly once.

    Returns:
        Dict mapping task name to its return value (or error dict).
    """
    results: Dict[str, Any] = {}
    for name, task in REGISTERED_TASKS.items():
        logger.info("Running task: %s", name)
        try:
            result = task["func"]()
            task["last_run"] = datetime.now().isoformat()
            task["last_status"] = "success"
            results[name] = result
        except Exception as exc:  # noqa: BLE001
            task["last_status"] = f"error: {exc}"
            logger.error("Task %s failed: %s", name, exc)
            results[name] = {"error": str(exc)}
    return results


def list_tasks() -> None:
    """Print all module-level registered tasks to stdout."""
    print(f"{'Name':<20} {'Schedule':<12} {'Last Run':<25} {'Description'}")
    print("-" * 80)
    for name, task in REGISTERED_TASKS.items():
        print(
            f"{name:<20} {task['schedule']:<12} "
            f"{task['last_run'] or 'never':<25} {task['description']}"
        )


# Module-level wrappers that delegate to standalone task functions so that
# tests importing them by name (``from task_runner import task_health_check``)
# continue to work.


def task_health_check() -> Any:
    """Legacy module-level health check — preserves original return contract.

    Returns a flat dict keyed by project name (not wrapped in a
    ``"components"`` envelope) so existing callers are unaffected.

    Returns:
        Dict mapping project key to health booleans, or ``{"error": ...}``
        when registry.json is missing.
    """
    import json
    from pathlib import Path

    registry_path = Path(_GAIA_ROOT) / "registry.json"
    if not registry_path.exists():
        return {"error": "Registry not found"}

    registry = json.loads(registry_path.read_text(encoding="utf-8"))
    health: Dict[str, Any] = {}

    for key, project in registry.get("projects", {}).items():
        path = Path(project.get("path", ""))
        health[key] = {
            "exists": path.exists(),
            "has_git": (path / ".git").exists() if path.exists() else False,
            "has_tests": bool(list(path.glob("tests/test_*.py"))) if path.exists() else False,
            "has_claude_md": (path / "CLAUDE.md").exists() if path.exists() else False,
        }

    return health


def task_stale_cache_cleanup() -> Any:
    """Legacy module-level stale-cache task — preserves original contract.

    Returns:
        Dict with ``cache_dirs`` (int) and ``paths`` (list), or ``None``
        when registry.json is missing.
    """
    import json
    from pathlib import Path

    registry_path = Path(_GAIA_ROOT) / "registry.json"
    if not registry_path.exists():
        return None

    registry = json.loads(registry_path.read_text(encoding="utf-8"))
    stale: list = []

    for _key, project in registry.get("projects", {}).items():
        path = Path(project.get("path", ""))
        if path.exists():
            for cache_dir in path.rglob("__pycache__"):
                stale.append(str(cache_dir))

    return {"cache_dirs": len(stale), "paths": stale[:10]}


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------


def _build_arg_parser() -> argparse.ArgumentParser:
    """Construct the CLI argument parser.

    Returns:
        Configured ArgumentParser instance.
    """
    parser = argparse.ArgumentParser(description="GAIA Background Task Runner")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--once", action="store_true", help="Execute due tasks and exit")
    group.add_argument(
        "--all", dest="run_all", action="store_true", help="Force all tasks and exit"
    )
    group.add_argument("--list", action="store_true", help="List registered tasks")
    group.add_argument(
        "--daemon",
        action="store_true",
        help="Loop forever, running due tasks every minute (Ctrl-C to stop)",
    )
    return parser


def main() -> None:
    """CLI entry point for the task runner."""
    import json

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(name)s] %(levelname)s: %(message)s",
    )

    args = _build_arg_parser().parse_args()
    runner = TaskRunner(register_defaults=True)

    if args.list:
        print(f"{'Name':<25} {'Interval(s)':<14} {'Last Run':<30} {'Enabled'}")
        print("-" * 80)
        for task in runner.list_tasks():
            last = str(task.last_run) if task.last_run else "never"
            print(f"{task.name:<25} {task.interval_seconds:<14} {last:<30} {task.enabled}")
        return

    if args.run_all:
        count = runner.run_all()
        print(json.dumps(runner.get_results(), indent=2, default=str))
        logger.info("Ran %d tasks (forced).", count)
        return

    if args.daemon:
        logger.info("GAIA Task Runner started (daemon mode). Press Ctrl-C to stop.")
        try:
            while True:
                count = runner.run_once()
                if count:
                    logger.info("Daemon cycle: executed %d due tasks.", count)
                time.sleep(60)
        except KeyboardInterrupt:
            logger.info("Daemon stopped.")
        return

    # Default: --once
    count = runner.run_once()
    print(json.dumps(runner.get_results(), indent=2, default=str))
    logger.info("Ran %d due tasks.", count)


if __name__ == "__main__":
    main()
