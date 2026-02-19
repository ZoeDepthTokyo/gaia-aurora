"""Tests for GAIA Loop circuit breaker."""

from __future__ import annotations

import json
from pathlib import Path
from unittest.mock import patch

import pytest

from runtime.circuit_breaker import check


@pytest.fixture
def state_file(tmp_path: Path) -> Path:
    """Create a minimal loop state file."""
    state = {
        "task": "Test task",
        "max_iterations": 25,
        "max_calls": 200,
        "completion_promise": "GAIA_LOOP_COMPLETE",
        "current_iteration": 3,
        "total_api_calls": 10,
        "status": "running",
        "started_at": "2026-02-13T14:00:00Z",
        "circuit_breaker": {
            "consecutive_no_change": 0,
            "error_history": [],
            "triggered": False,
        },
    }
    fp = tmp_path / ".gaia_loop_state"
    fp.write_text(json.dumps(state, indent=2), encoding="utf-8")
    return fp


@pytest.fixture
def _mock_git_changes():
    """Mock git diff to return changed files."""
    with patch(
        "runtime.circuit_breaker._get_changed_files",
        return_value=["src/main.py", "tests/test_main.py"],
    ):
        yield


@pytest.fixture
def _mock_no_changes():
    """Mock git diff to return no changed files."""
    with patch("runtime.circuit_breaker._get_changed_files", return_value=[]):
        yield


@pytest.fixture
def _mock_no_errors():
    """Mock no test errors."""
    with patch("runtime.circuit_breaker._get_test_errors", return_value=None):
        yield


class TestCircuitBreakerHappy:
    """Tests where loop should continue."""

    @pytest.mark.usefixtures("_mock_git_changes", "_mock_no_errors")
    def test_continues_when_files_changed(self, state_file: Path) -> None:
        result = check(str(state_file))
        assert result["status"] == "running"
        assert result["circuit_breaker"]["triggered"] is False

    @pytest.mark.usefixtures("_mock_git_changes", "_mock_no_errors")
    def test_resets_no_change_counter_on_change(self, state_file: Path) -> None:
        # Set counter to 2 (almost triggered)
        state = json.loads(state_file.read_text())
        state["circuit_breaker"]["consecutive_no_change"] = 2
        state_file.write_text(json.dumps(state, indent=2))

        result = check(str(state_file))
        assert result["circuit_breaker"]["consecutive_no_change"] == 0
        assert result["status"] == "running"


class TestCircuitBreakerNoChange:
    """Tests for no-file-change detection."""

    @pytest.mark.usefixtures("_mock_no_changes", "_mock_no_errors")
    def test_increments_no_change_counter(self, state_file: Path) -> None:
        result = check(str(state_file))
        assert result["circuit_breaker"]["consecutive_no_change"] == 1
        assert result["status"] == "running"

    @pytest.mark.usefixtures("_mock_no_changes", "_mock_no_errors")
    def test_triggers_after_three_no_changes(self, state_file: Path) -> None:
        state = json.loads(state_file.read_text())
        state["circuit_breaker"]["consecutive_no_change"] = 2
        state_file.write_text(json.dumps(state, indent=2))

        result = check(str(state_file))
        assert result["status"] == "CIRCUIT_BREAKER_OPEN"
        assert result["circuit_breaker"]["triggered"] is True


class TestCircuitBreakerRepeatedErrors:
    """Tests for repeated error detection."""

    @pytest.mark.usefixtures("_mock_git_changes")
    def test_triggers_after_five_same_errors(self, state_file: Path) -> None:
        error_sig = "## Current Blockers FileNotFoundError sample.csv not found"
        state = json.loads(state_file.read_text())
        state["circuit_breaker"]["error_history"] = [error_sig] * 4
        state_file.write_text(json.dumps(state, indent=2))

        with patch("runtime.circuit_breaker._get_test_errors", return_value=error_sig):
            result = check(str(state_file))

        assert result["status"] == "CIRCUIT_BREAKER_OPEN"
        assert result["circuit_breaker"]["triggered"] is True

    @pytest.mark.usefixtures("_mock_git_changes")
    def test_does_not_trigger_on_different_errors(self, state_file: Path) -> None:
        state = json.loads(state_file.read_text())
        state["circuit_breaker"]["error_history"] = [
            "error_a",
            "error_b",
            "error_c",
            "error_d",
        ]
        state_file.write_text(json.dumps(state, indent=2))

        with patch("runtime.circuit_breaker._get_test_errors", return_value="error_e"):
            result = check(str(state_file))

        assert result["status"] == "running"


class TestRateLimiting:
    """Tests for API call budget enforcement."""

    @pytest.mark.usefixtures("_mock_git_changes", "_mock_no_errors")
    def test_triggers_when_budget_exceeded(self, state_file: Path) -> None:
        state = json.loads(state_file.read_text())
        state["total_api_calls"] = 200
        state["max_calls"] = 200
        state_file.write_text(json.dumps(state, indent=2))

        result = check(str(state_file))
        assert result["status"] == "RATE_LIMITED"
        assert result["circuit_breaker"]["triggered"] is True

    @pytest.mark.usefixtures("_mock_git_changes", "_mock_no_errors")
    def test_continues_under_budget(self, state_file: Path) -> None:
        state = json.loads(state_file.read_text())
        state["total_api_calls"] = 199
        state["max_calls"] = 200
        state_file.write_text(json.dumps(state, indent=2))

        result = check(str(state_file))
        assert result["status"] == "running"


class TestEdgeCases:
    """Edge case tests."""

    def test_missing_state_file(self, tmp_path: Path) -> None:
        result = check(str(tmp_path / "nonexistent.json"))
        assert result["status"] == "no_state_file"

    @pytest.mark.usefixtures("_mock_git_changes", "_mock_no_errors")
    def test_missing_circuit_breaker_key(self, state_file: Path) -> None:
        state = json.loads(state_file.read_text())
        del state["circuit_breaker"]
        state_file.write_text(json.dumps(state, indent=2))

        result = check(str(state_file))
        assert result["status"] == "running"
        assert "circuit_breaker" in result

    @pytest.mark.usefixtures("_mock_git_changes")
    def test_error_history_capped_at_ten(self, state_file: Path) -> None:
        state = json.loads(state_file.read_text())
        state["circuit_breaker"]["error_history"] = [f"error_{i}" for i in range(10)]
        state_file.write_text(json.dumps(state, indent=2))

        with patch("runtime.circuit_breaker._get_test_errors", return_value="new_error"):
            result = check(str(state_file))

        assert len(result["circuit_breaker"]["error_history"]) == 10
