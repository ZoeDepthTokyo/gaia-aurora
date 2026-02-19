"""Tests for GAIA Background Task Runner.

Covers TaskRunner class (class-based API) as well as the legacy
module-level helpers (register_task, run_all_once, list_tasks) so that
both APIs remain tested simultaneously.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path
from unittest.mock import patch

import pytest

# Allow direct imports from the runtime package when run via pytest from root.
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from runtime.task_runner import (
    REGISTERED_TASKS,
    ScheduledTask,
    TaskRunner,
    list_tasks,
    register_task,
    run_all_once,
    task_health_check,
    task_stale_cache_cleanup,
)

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _make_runner() -> TaskRunner:
    """Return a fresh TaskRunner with NO default tasks pre-registered."""
    return TaskRunner(register_defaults=False)


# ---------------------------------------------------------------------------
# Class-based API — TaskRunner
# ---------------------------------------------------------------------------


class TestTaskRunnerInit:
    def test_initializes_with_empty_registry(self) -> None:
        """TaskRunner starts with no tasks when register_defaults=False."""
        runner = _make_runner()
        assert runner.list_tasks() == []

    def test_initializes_with_default_tasks(self) -> None:
        """TaskRunner with defaults registers the 5 built-in tasks."""
        runner = TaskRunner(register_defaults=True)
        names = {t.name for t in runner.list_tasks()}
        assert "warden_scan" in names
        assert "health_check" in names
        assert "stale_cache_cleanup" in names
        assert "guardrail_check" in names
        assert "baseline_update" in names
        assert len(names) == 5


class TestRegister:
    def test_register_adds_task(self) -> None:
        """register() stores the task in the internal registry."""
        runner = _make_runner()
        runner.register("ping", lambda: "pong", interval_seconds=60)
        tasks = runner.list_tasks()
        assert len(tasks) == 1
        assert tasks[0].name == "ping"

    def test_register_sets_interval(self) -> None:
        """register() correctly stores interval_seconds."""
        runner = _make_runner()
        runner.register("t", lambda: None, interval_seconds=300)
        assert runner.list_tasks()[0].interval_seconds == 300

    def test_register_task_enabled_by_default(self) -> None:
        """Newly registered tasks are enabled by default."""
        runner = _make_runner()
        runner.register("t", lambda: None, interval_seconds=60)
        assert runner.list_tasks()[0].enabled is True

    def test_register_overrides_existing(self) -> None:
        """Re-registering a name replaces the previous entry."""
        runner = _make_runner()
        runner.register("t", lambda: "v1", interval_seconds=60)
        runner.register("t", lambda: "v2", interval_seconds=120)
        tasks = runner.list_tasks()
        assert len(tasks) == 1
        assert tasks[0].interval_seconds == 120


class TestListTasks:
    def test_list_tasks_returns_all(self) -> None:
        """list_tasks returns one entry per registered task."""
        runner = _make_runner()
        runner.register("a", lambda: None, interval_seconds=60)
        runner.register("b", lambda: None, interval_seconds=120)
        assert len(runner.list_tasks()) == 2

    def test_list_tasks_returns_scheduled_task_objects(self) -> None:
        """list_tasks entries are ScheduledTask dataclass instances."""
        runner = _make_runner()
        runner.register("t", lambda: None, interval_seconds=60)
        entry = runner.list_tasks()[0]
        assert isinstance(entry, ScheduledTask)


class TestRunOnce:
    def test_run_once_executes_due_tasks(self) -> None:
        """run_once calls tasks whose interval has elapsed."""
        runner = _make_runner()
        executed: list[str] = []
        runner.register("t", lambda: executed.append("t"), interval_seconds=0)
        count = runner.run_once()
        assert count == 1
        assert "t" in executed

    def test_run_once_skips_tasks_not_yet_due(self) -> None:
        """run_once skips tasks last run within the interval window."""
        runner = _make_runner()
        executed: list[str] = []

        def fn() -> None:
            executed.append("ran")

        runner.register("t", fn, interval_seconds=9999)
        # Manually mark it as just-run
        runner._tasks["t"].last_run = time.time()

        count = runner.run_once()
        assert count == 0
        assert executed == []

    def test_run_once_returns_task_count(self) -> None:
        """run_once return value equals the number of tasks executed."""
        runner = _make_runner()
        runner.register("a", lambda: None, interval_seconds=0)
        runner.register("b", lambda: None, interval_seconds=0)
        count = runner.run_once()
        assert count == 2

    def test_run_once_zero_interval_always_runs(self) -> None:
        """A task with interval_seconds=0 executes every run_once call."""
        runner = _make_runner()
        calls: list[int] = []
        runner.register("t", lambda: calls.append(1), interval_seconds=0)
        runner.run_once()
        runner.run_once()
        assert len(calls) == 2

    def test_run_once_exception_does_not_crash_runner(self) -> None:
        """A task that raises must not propagate and must not prevent other tasks."""
        runner = _make_runner()
        executed: list[str] = []

        def bad() -> None:
            raise RuntimeError("boom")

        runner.register("bad", bad, interval_seconds=0)
        runner.register("good", lambda: executed.append("good"), interval_seconds=0)

        # Must not raise
        count = runner.run_once()
        assert "good" in executed
        # Both tasks were attempted, so count reflects attempted executions
        assert count >= 1

    def test_run_once_results_include_timestamp_and_status(self) -> None:
        """Results dict contains 'timestamp' and 'status' keys for each executed task."""
        runner = _make_runner()
        runner.register("t", lambda: {"val": 1}, interval_seconds=0)
        runner.run_once()
        results = runner.get_results()
        assert "t" in results
        assert "timestamp" in results["t"]
        assert "status" in results["t"]

    def test_run_once_error_status_in_results(self) -> None:
        """A failing task records status='error' and includes 'error' key in results."""
        runner = _make_runner()

        def bad() -> None:
            raise ValueError("oops")

        runner.register("bad", bad, interval_seconds=0)
        runner.run_once()
        result = runner.get_results()["bad"]
        assert result["status"] == "error"
        assert "oops" in result["error"]


class TestRunAll:
    def test_run_all_executes_regardless_of_interval(self) -> None:
        """run_all() forces execution even for tasks not yet due."""
        runner = _make_runner()
        executed: list[str] = []
        runner.register("t", lambda: executed.append("t"), interval_seconds=9999)
        runner._tasks["t"].last_run = time.time()  # mark as recently run
        runner.run_all()
        assert "t" in executed

    def test_run_all_executes_all_tasks(self) -> None:
        """run_all() runs every registered task exactly once."""
        runner = _make_runner()
        executed: list[str] = []
        runner.register("a", lambda: executed.append("a"), interval_seconds=9999)
        runner.register("b", lambda: executed.append("b"), interval_seconds=9999)
        runner._tasks["a"].last_run = time.time()
        runner._tasks["b"].last_run = time.time()
        runner.run_all()
        assert sorted(executed) == ["a", "b"]


class TestGetResults:
    def test_get_results_empty_before_any_run(self) -> None:
        """get_results returns empty dict before any run_once call."""
        runner = _make_runner()
        runner.register("t", lambda: None, interval_seconds=0)
        assert runner.get_results() == {}

    def test_get_results_populated_after_run(self) -> None:
        """get_results returns entries for all tasks that ran."""
        runner = _make_runner()
        runner.register("t", lambda: {"ok": True}, interval_seconds=0)
        runner.run_once()
        results = runner.get_results()
        assert "t" in results


# ---------------------------------------------------------------------------
# Default tasks (registered via register_defaults=True)
# ---------------------------------------------------------------------------


class TestDefaultTasks:
    def test_five_default_tasks_are_registered(self) -> None:
        """Exactly 5 tasks are pre-registered by default."""
        runner = TaskRunner(register_defaults=True)
        assert len(runner.list_tasks()) == 5

    def test_default_task_names(self) -> None:
        """All expected default task names are present."""
        runner = TaskRunner(register_defaults=True)
        names = {t.name for t in runner.list_tasks()}
        expected = {
            "warden_scan",
            "health_check",
            "stale_cache_cleanup",
            "guardrail_check",
            "baseline_update",
        }
        assert names == expected


# ---------------------------------------------------------------------------
# Legacy module-level API (backward compat — kept for existing consumers)
# ---------------------------------------------------------------------------


class TestLegacyModuleAPI:
    def setup_method(self) -> None:
        """Clear the global registry before each test."""
        REGISTERED_TASKS.clear()

    def test_register_task_adds_to_registry(self) -> None:
        register_task("leg", lambda: None, "hourly", "legacy task")
        assert "leg" in REGISTERED_TASKS

    def test_run_all_once_executes_and_returns_results(self) -> None:
        calls: list[str] = []
        register_task("t", lambda: calls.append("t") or {"done": True}, "hourly")
        results = run_all_once()
        assert "t" in results
        assert calls == ["t"]

    def test_run_all_once_handles_exception(self) -> None:
        def bad() -> None:
            raise RuntimeError("fail")

        register_task("bad", bad, "hourly")
        results = run_all_once()
        assert "error" in results["bad"]

    def test_list_tasks_prints_names(self, capsys: pytest.CaptureFixture) -> None:
        register_task("mytask", lambda: None, "daily", "desc")
        list_tasks()
        out = capsys.readouterr().out
        assert "mytask" in out

    def test_task_health_check_missing_registry(self) -> None:
        with patch("pathlib.Path.exists", return_value=False):
            result = task_health_check()
        assert result == {"error": "Registry not found"}

    def test_task_stale_cache_cleanup_no_registry(self) -> None:
        with patch("pathlib.Path.exists", return_value=False):
            result = task_stale_cache_cleanup()
        assert result is None
