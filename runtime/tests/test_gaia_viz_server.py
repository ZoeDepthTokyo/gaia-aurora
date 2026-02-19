#!/usr/bin/env python3
"""
Tests for GAIA Visualization Server

TDD approach - test server endpoints, state management, and component detection
"""
import json
import pytest
import tempfile
from pathlib import Path
from datetime import datetime
import sys

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

import gaia_viz_server as viz


def test_classify_component_argus():
    """Test ARGUS component detection"""
    assert viz.classify_component("_ARGUS/dashboard/app.py") == "ARGUS"
    assert viz.classify_component("X:/projects/_GAIA/_ARGUS/sim/test.py") == "ARGUS"


def test_classify_component_vulcan():
    """Test VULCAN component detection"""
    assert viz.classify_component("_VULCAN/ui/main.py") == "VULCAN"
    assert viz.classify_component("X:/projects/_GAIA/_VULCAN/test.py") == "VULCAN"


def test_classify_component_mycel():
    """Test MYCEL component detection"""
    assert viz.classify_component("_MYCEL/rag_intelligence/llm.py") == "MYCEL"


def test_classify_component_fallback():
    """Test fallback to GAIA for non-component files"""
    assert viz.classify_component("registry.json") == "GAIA"
    assert viz.classify_component("GAIA_MANIFEST.md") == "GAIA"
    assert viz.classify_component("random/path/file.py") == "GAIA"


def test_all_components_detected():
    """Test that all 9 GAIA components can be detected"""
    test_cases = {
        "_ARGUS/test.py": "ARGUS",
        "_WARDEN/test.py": "WARDEN",
        "_VULCAN/test.py": "VULCAN",
        "_AURORA/test.py": "AURORA",
        "_LOOM/test.py": "LOOM",
        "_MYCEL/test.py": "MYCEL",
        "_MNEMIS/test.py": "MNEMIS",
        "_RAVEN/test.py": "RAVEN",
        "_ABIS/test.py": "ABIS",
    }

    for file_path, expected_component in test_cases.items():
        assert viz.classify_component(file_path) == expected_component


def test_case_insensitive_detection():
    """Test component detection is case-insensitive"""
    assert viz.classify_component("_argus/test.py") == "ARGUS"
    assert viz.classify_component("_ARGUS/test.py") == "ARGUS"
    assert viz.classify_component("_ArGuS/test.py") == "ARGUS"


def test_component_state_structure():
    """Test initial component state has correct structure"""
    assert len(viz.component_state) == 10  # 9 components + GAIA
    assert "GAIA" in viz.component_state
    assert "ARGUS" in viz.component_state

    for component, state in viz.component_state.items():
        assert "status" in state
        assert state["status"] == "IDLE"
        assert "last_activity" in state


def test_process_change_updates_state():
    """Test that processing a change updates component state"""
    # Reset state
    viz.component_state["ARGUS"] = {"status": "IDLE", "last_activity": None}

    change = {
        "file": "_ARGUS/dashboard/app.py",
        "tool": "Edit",
        "timestamp": datetime.now().isoformat(),
    }

    viz.process_change(change)

    # Check ARGUS was activated
    assert viz.component_state["ARGUS"]["status"] == "ACTIVE"
    assert viz.component_state["ARGUS"]["last_tool"] == "Edit"
    assert viz.component_state["ARGUS"]["last_file"] == "_ARGUS/dashboard/app.py"


def test_event_log_appends():
    """Test that events are added to event log"""
    initial_len = len(viz.event_log)

    change = {
        "file": "_VULCAN/ui/main.py",
        "tool": "Write",
        "timestamp": datetime.now().isoformat(),
    }

    viz.process_change(change)

    assert len(viz.event_log) > initial_len
    assert viz.event_log[-1]["component"] == "VULCAN"
    assert viz.event_log[-1]["tool"] == "Write"


def test_event_log_max_size():
    """Test that event log doesn't exceed MAX_EVENTS"""
    # Fill event log beyond max
    viz.event_log.clear()

    for i in range(viz.MAX_EVENTS + 20):
        change = {
            "file": "_ARGUS/test.py",
            "tool": "Read",
            "timestamp": datetime.now().isoformat(),
        }
        viz.process_change(change)

    assert len(viz.event_log) == viz.MAX_EVENTS


def test_save_state_creates_file(tmp_path):
    """Test that save_state creates state file"""
    # Temporarily change STATE_FILE path
    original_path = viz.STATE_FILE
    viz.STATE_FILE = tmp_path / "test_state.json"

    viz.save_state()

    assert viz.STATE_FILE.exists()
    state_data = json.loads(viz.STATE_FILE.read_text())
    assert "GAIA" in state_data
    assert "ARGUS" in state_data

    # Restore original
    viz.STATE_FILE = original_path


def test_reset_component():
    """Test component reset to IDLE"""
    viz.component_state["MYCEL"] = {"status": "ACTIVE", "last_activity": "test"}

    viz.reset_component("MYCEL")

    assert viz.component_state["MYCEL"]["status"] == "IDLE"


def test_multiple_tools_detected():
    """Test different tool types are recorded"""
    tools = ["Edit", "Write", "Read", "Bash"]

    for tool in tools:
        change = {
            "file": "_ARGUS/test.py",
            "tool": tool,
            "timestamp": datetime.now().isoformat(),
        }
        viz.process_change(change)
        assert viz.component_state["ARGUS"]["last_tool"] == tool


def test_component_state_persistence(tmp_path):
    """Test state can be saved and loaded"""
    viz.STATE_FILE = tmp_path / "persistence_test.json"

    # Set some state
    viz.component_state["VULCAN"] = {
        "status": "ACTIVE",
        "last_activity": "2026-02-14T12:00:00",
        "last_tool": "Write",
    }

    viz.save_state()

    # Load it back
    loaded = json.loads(viz.STATE_FILE.read_text())
    assert loaded["VULCAN"]["status"] == "ACTIVE"
    assert loaded["VULCAN"]["last_tool"] == "Write"


def test_empty_file_path_handled():
    """Test empty file path doesn't crash"""
    change = {"file": "", "tool": "Read", "timestamp": datetime.now().isoformat()}

    # Should not raise exception
    viz.process_change(change)

    # Should classify as GAIA
    assert viz.component_state["GAIA"]["status"] == "ACTIVE"


def test_malformed_timestamp_handled():
    """Test malformed timestamp doesn't crash"""
    change = {"file": "_ARGUS/test.py", "tool": "Edit", "timestamp": "invalid"}

    # Should not raise exception
    viz.process_change(change)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
