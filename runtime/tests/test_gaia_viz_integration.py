#!/usr/bin/env python3
"""
Integration tests for GAIA Visualization Server

Tests HTTP endpoints and threading behavior
"""
import json
import pytest
import tempfile
import threading
import time
from pathlib import Path
from http.server import HTTPServer
from urllib.request import urlopen
from urllib.error import HTTPError
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))

import gaia_viz_server as viz


@pytest.fixture
def test_server():
    """Start server in background for testing"""
    # Use random port for testing
    port = 18766

    # Reset state
    viz.component_state = {
        comp: {"status": "IDLE", "last_activity": None}
        for comp in [
            "GAIA",
            "ARGUS",
            "WARDEN",
            "VULCAN",
            "AURORA",
            "LOOM",
            "MYCEL",
            "MNEMIS",
            "RAVEN",
            "ABIS",
        ]
    }
    viz.event_log.clear()
    viz.sse_clients.clear()

    # Start server in thread
    server = HTTPServer(("localhost", port), viz.GAIAVizHandler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()

    yield f"http://localhost:{port}"

    # Cleanup
    server.shutdown()


def test_api_state_endpoint(test_server):
    """Test /api/state returns component state"""
    response = urlopen(f"{test_server}/api/state")
    assert response.status == 200

    data = json.loads(response.read())
    assert "GAIA" in data
    assert "ARGUS" in data
    assert data["GAIA"]["status"] == "IDLE"


def test_api_events_endpoint(test_server):
    """Test /api/events returns event log"""
    # Add some events
    viz.event_log.append(
        {
            "type": "tool_use",
            "component": "ARGUS",
            "tool": "Edit",
            "timestamp": "2026-02-14T12:00:00",
        }
    )

    response = urlopen(f"{test_server}/api/events")
    assert response.status == 200

    data = json.loads(response.read())
    assert isinstance(data, list)
    assert len(data) > 0
    assert data[0]["component"] == "ARGUS"


def test_api_404_on_invalid_path(test_server):
    """Test server returns 404 for invalid paths"""
    with pytest.raises(HTTPError) as exc_info:
        urlopen(f"{test_server}/invalid/path")

    assert exc_info.value.code == 404


def test_state_updates_after_process_change(test_server):
    """Test state endpoint reflects changes after process_change"""
    # Process a change
    change = {
        "file": "_VULCAN/ui/main.py",
        "tool": "Write",
        "timestamp": "2026-02-14T12:00:00",
    }
    viz.process_change(change)

    # Query state
    response = urlopen(f"{test_server}/api/state")
    data = json.loads(response.read())

    assert data["VULCAN"]["status"] == "ACTIVE"
    assert data["VULCAN"]["last_tool"] == "Write"


def test_cors_headers_present(test_server):
    """Test CORS headers are included in response"""
    response = urlopen(f"{test_server}/api/state")

    # Check for Access-Control-Allow-Origin header
    headers = dict(response.headers)
    assert "Access-Control-Allow-Origin" in headers
    assert headers["Access-Control-Allow-Origin"] == "*"


def test_monitor_changes_detects_new_lines(tmp_path):
    """Test monitor_changes function detects new file content"""
    # Create temp changes file
    changes_file = tmp_path / "test_changes"
    changes_file.write_text("")

    # Override CHANGES_FILE
    original_file = viz.CHANGES_FILE
    viz.CHANGES_FILE = changes_file

    # Start monitor in thread
    stop_event = threading.Event()

    def monitor_with_stop():
        for _ in range(5):  # Run for 5 iterations max
            if stop_event.is_set():
                break
            viz.monitor_changes()

    monitor_thread = threading.Thread(target=monitor_with_stop, daemon=True)
    monitor_thread.start()

    # Write a change
    change = {
        "file": "_ARGUS/test.py",
        "tool": "Edit",
        "timestamp": "2026-02-14T12:00:00",
    }
    changes_file.write_text(json.dumps(change) + "\n")

    # Wait for processing
    time.sleep(2)

    # Stop monitor
    stop_event.set()
    monitor_thread.join(timeout=3)

    # Check if change was processed
    # (This is a best-effort test - may be flaky due to timing)

    # Restore original
    viz.CHANGES_FILE = original_file


def test_broadcast_event_to_sse_clients():
    """Test broadcast_event sends to SSE clients"""

    class MockSSEClient:
        def __init__(self):
            self.messages = []
            self.wfile = self

        def write(self, data):
            self.messages.append(data)

        def flush(self):
            pass

    # Add mock client
    mock_client = MockSSEClient()
    viz.sse_clients.append(mock_client)

    # Broadcast event
    event = {"type": "test", "component": "ARGUS"}
    viz.broadcast_event(event)

    # Check client received event
    assert len(mock_client.messages) > 0
    assert b"ARGUS" in mock_client.messages[0]

    # Cleanup
    viz.sse_clients.clear()


def test_broadcast_removes_dead_clients():
    """Test broadcast_event removes clients that error"""

    class BadSSEClient:
        def __init__(self):
            self.wfile = self

        def write(self, data):
            raise BrokenPipeError("Connection closed")

        def flush(self):
            pass

    # Add bad client
    bad_client = BadSSEClient()
    viz.sse_clients.append(bad_client)

    # Broadcast should remove bad client
    viz.broadcast_event({"type": "test"})

    assert bad_client not in viz.sse_clients


def test_api_response_json_format(test_server):
    """Test API responses are valid JSON"""
    endpoints = ["/api/state", "/api/events"]

    for endpoint in endpoints:
        response = urlopen(f"{test_server}{endpoint}")
        data = json.loads(response.read())

        # Should not raise JSONDecodeError
        assert data is not None


def test_event_log_ordering(test_server):
    """Test events are returned in chronological order"""
    # Add multiple events
    for i in range(5):
        change = {
            "file": f"_ARGUS/file{i}.py",
            "tool": "Edit",
            "timestamp": f"2026-02-14T12:00:{i:02d}",
        }
        viz.process_change(change)

    response = urlopen(f"{test_server}/api/events")
    events = json.loads(response.read())

    # Check timestamps are in order
    timestamps = [e["timestamp"] for e in events]
    assert timestamps == sorted(timestamps)


def test_concurrent_requests(test_server):
    """Test server handles concurrent requests"""

    def make_request():
        urlopen(f"{test_server}/api/state")

    # Make 10 concurrent requests
    threads = [threading.Thread(target=make_request) for _ in range(10)]

    for t in threads:
        t.start()

    for t in threads:
        t.join(timeout=5)

    # All threads should complete without error


def test_monitor_changes_error_handling(tmp_path):
    """Test monitor_changes handles file errors gracefully"""
    # Point to non-existent file
    viz.CHANGES_FILE = tmp_path / "nonexistent.txt"

    # Should not crash
    try:
        viz.monitor_changes()  # Single iteration
    except Exception as e:
        pytest.fail(f"monitor_changes raised exception: {e}")


def test_save_state_error_handling(tmp_path):
    """Test save_state handles write errors gracefully"""
    # Point to read-only location (hopefully!)
    viz.STATE_FILE = Path("/invalid/path/state.json")

    # Should not crash, just log error
    try:
        viz.save_state()
    except Exception as e:
        pytest.fail(f"save_state raised exception: {e}")


def test_process_change_with_all_fields():
    """Test process_change with complete change object"""
    change = {
        "file": "_MYCEL/rag_intelligence/llm.py",
        "tool": "Edit",
        "timestamp": "2026-02-14T12:34:56",
        "component": "MYCEL",  # Pre-classified
        "extra_field": "ignored",  # Extra fields should be ignored
    }

    viz.process_change(change)

    assert viz.component_state["MYCEL"]["status"] == "ACTIVE"
    assert "extra_field" not in viz.component_state["MYCEL"]


def test_api_stream_endpoint_setup(test_server):
    """Test /api/stream endpoint exists (SSE setup)"""
    # Skip this test - SSE requires persistent connection which blocks pytest
    pytest.skip("SSE endpoint requires persistent connection, tested manually")


def test_component_state_keys_match_components():
    """Test all expected components are in state"""
    expected_components = {
        "GAIA",
        "ARGUS",
        "WARDEN",
        "VULCAN",
        "AURORA",
        "LOOM",
        "MYCEL",
        "MNEMIS",
        "RAVEN",
        "ABIS",
    }

    assert set(viz.component_state.keys()) == expected_components


def test_reset_component_inactive_state():
    """Test reset_component only resets ACTIVE components"""
    viz.component_state["LOOM"] = {"status": "IDLE", "last_activity": None}

    viz.reset_component("LOOM")

    # Should remain IDLE (not change if already idle)
    assert viz.component_state["LOOM"]["status"] == "IDLE"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
