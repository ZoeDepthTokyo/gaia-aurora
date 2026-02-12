"""Tests for GAIA Background Task Runner."""
import json
from pathlib import Path
from unittest.mock import patch, MagicMock
import pytest


# Add parent directory to path for imports
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

from task_runner import (
    register_task,
    run_all_once,
    list_tasks,
    task_health_check,
    task_stale_cache_cleanup,
    REGISTERED_TASKS,
)


def test_register_task_adds_to_registry():
    """Test that register_task adds task to REGISTERED_TASKS."""
    # Clear registry before test
    REGISTERED_TASKS.clear()

    def dummy_task():
        return "done"

    register_task(
        name="test_task",
        func=dummy_task,
        schedule="hourly",
        description="Test task for unit test"
    )

    assert "test_task" in REGISTERED_TASKS
    assert REGISTERED_TASKS["test_task"]["func"] == dummy_task
    assert REGISTERED_TASKS["test_task"]["schedule"] == "hourly"
    assert REGISTERED_TASKS["test_task"]["description"] == "Test task for unit test"
    assert REGISTERED_TASKS["test_task"]["last_run"] is None
    assert REGISTERED_TASKS["test_task"]["last_status"] is None


def test_run_all_once_executes_tasks():
    """Test that run_all_once executes all registered tasks."""
    # Clear registry and add test tasks
    REGISTERED_TASKS.clear()

    call_count = {"task1": 0, "task2": 0}

    def task1():
        call_count["task1"] += 1
        return {"result": "task1_success"}

    def task2():
        call_count["task2"] += 1
        return {"result": "task2_success"}

    register_task("task1", task1, "hourly", "Test task 1")
    register_task("task2", task2, "daily", "Test task 2")

    results = run_all_once()

    # Verify all tasks were called
    assert call_count["task1"] == 1
    assert call_count["task2"] == 1

    # Verify results
    assert "task1" in results
    assert "task2" in results
    assert results["task1"]["result"] == "task1_success"
    assert results["task2"]["result"] == "task2_success"

    # Verify last_run and last_status were updated
    assert REGISTERED_TASKS["task1"]["last_run"] is not None
    assert REGISTERED_TASKS["task1"]["last_status"] == "success"
    assert REGISTERED_TASKS["task2"]["last_run"] is not None
    assert REGISTERED_TASKS["task2"]["last_status"] == "success"


def test_run_all_once_handles_exceptions():
    """Test that run_all_once handles task exceptions gracefully."""
    REGISTERED_TASKS.clear()

    def failing_task():
        raise ValueError("Task failed!")

    def working_task():
        return {"status": "ok"}

    register_task("failing", failing_task, "hourly", "Task that fails")
    register_task("working", working_task, "hourly", "Task that works")

    results = run_all_once()

    # Verify failing task recorded error
    assert "failing" in results
    assert "error" in results["failing"]
    assert "Task failed!" in results["failing"]["error"]
    assert "error:" in REGISTERED_TASKS["failing"]["last_status"]

    # Verify working task succeeded
    assert "working" in results
    assert results["working"]["status"] == "ok"
    assert REGISTERED_TASKS["working"]["last_status"] == "success"


def test_list_tasks_doesnt_crash(capsys):
    """Test that list_tasks prints without crashing."""
    REGISTERED_TASKS.clear()

    def dummy_task():
        pass

    register_task("test_task", dummy_task, "daily", "A test task")

    # Should not raise
    list_tasks()

    captured = capsys.readouterr()
    assert "test_task" in captured.out
    assert "daily" in captured.out
    assert "A test task" in captured.out


def test_task_health_check_structure():
    """Test that task_health_check returns expected structure."""
    # Create a mock registry
    mock_registry = {
        "projects": {
            "test_project": {
                "path": "X:/Projects/_GAIA/_WARDEN"  # Use a real path for testing
            }
        }
    }

    with patch("pathlib.Path.exists") as mock_exists, \
         patch("pathlib.Path.read_text") as mock_read:

        # Mock registry file exists and contains our mock data
        mock_exists.return_value = True
        mock_read.return_value = json.dumps(mock_registry)

        result = task_health_check()

        # Verify structure
        assert isinstance(result, dict)
        assert "test_project" in result

        project_health = result["test_project"]
        assert "exists" in project_health
        assert "has_git" in project_health
        assert "has_tests" in project_health
        assert "has_claude_md" in project_health

        # All values should be booleans
        assert isinstance(project_health["exists"], bool)
        assert isinstance(project_health["has_git"], bool)
        assert isinstance(project_health["has_tests"], bool)
        assert isinstance(project_health["has_claude_md"], bool)


def test_task_health_check_missing_registry():
    """Test that task_health_check handles missing registry gracefully."""
    with patch("pathlib.Path.exists") as mock_exists:
        mock_exists.return_value = False

        result = task_health_check()

        assert result == {"error": "Registry not found"}


def test_task_stale_cache_cleanup_structure():
    """Test that task_stale_cache_cleanup returns expected structure."""
    mock_registry = {
        "projects": {
            "test_project": {
                "path": "X:/Projects/_GAIA/_WARDEN"
            }
        }
    }

    with patch("pathlib.Path.exists") as mock_exists, \
         patch("pathlib.Path.read_text") as mock_read, \
         patch("pathlib.Path.rglob") as mock_rglob:

        mock_exists.return_value = True
        mock_read.return_value = json.dumps(mock_registry)

        # Mock finding some __pycache__ directories
        mock_cache_dirs = [
            Path("X:/Projects/_GAIA/_WARDEN/__pycache__"),
            Path("X:/Projects/_GAIA/_WARDEN/tests/__pycache__"),
        ]
        mock_rglob.return_value = mock_cache_dirs

        result = task_stale_cache_cleanup()

        # Verify structure
        assert isinstance(result, dict)
        assert "cache_dirs" in result
        assert "paths" in result
        assert isinstance(result["cache_dirs"], int)
        assert isinstance(result["paths"], list)


def test_task_stale_cache_cleanup_no_registry():
    """Test that task_stale_cache_cleanup handles missing registry gracefully."""
    with patch("pathlib.Path.exists") as mock_exists:
        mock_exists.return_value = False

        result = task_stale_cache_cleanup()

        # Should return None without crashing
        assert result is None


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
