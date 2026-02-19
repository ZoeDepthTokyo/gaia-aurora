"""Tests for GAIA scripts: tag_known_good and rollback.

Covers registry parsing, submodule discovery, and GENESISCollector roundtrip.
No git commands are executed -- subprocess calls are mocked.
"""
import json
import os
import sys

import pytest

# Make scripts importable without installing as package
GAIA_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS_DIR = os.path.join(GAIA_ROOT, "scripts")
sys.path.insert(0, SCRIPTS_DIR)

# GENESIS protocol lives in _ARGUS
ARGUS_DIR = os.path.join(GAIA_ROOT, "_ARGUS")
sys.path.insert(0, ARGUS_DIR)


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

MINIMAL_REGISTRY = {
    "$schema": "gaia-registry-v1",
    "projects": {
        "mycel": {
            "name": "MYCEL",
            "path": "X:/Projects/_GAIA/_MYCEL",
            "version": "0.2.0",
            "status": "active",
        },
        "argus": {
            "name": "ARGUS",
            "path": "X:/Projects/_GAIA/_ARGUS",
            "version": "0.7.0",
            "status": "stable",
        },
        "hart_os": {
            "name": "HART OS",
            "path": "X:/Projects/hart_os_v6",  # NOT a _GAIA/_ path
            "version": "6.2.8",
            "status": "production",
        },
    },
}


@pytest.fixture()
def registry_file(tmp_path):
    """Write a minimal registry.json and return its path."""
    reg_path = tmp_path / "registry.json"
    reg_path.write_text(json.dumps(MINIMAL_REGISTRY))
    return str(tmp_path)


# ---------------------------------------------------------------------------
# tag_known_good: get_submodules
# ---------------------------------------------------------------------------


class TestTagKnownGoodGetSubmodules:
    def test_returns_only_gaia_submodule_paths(self, registry_file, monkeypatch):
        import tag_known_good

        monkeypatch.setattr(tag_known_good, "GAIA_ROOT", registry_file)
        paths = tag_known_good.get_submodules()
        # hart_os is NOT under _GAIA/_ so it must be excluded
        assert any("_MYCEL" in p for p in paths)
        assert any("_ARGUS" in p for p in paths)
        assert all("hart_os" not in p for p in paths)

    def test_returns_list_type(self, registry_file, monkeypatch):
        import tag_known_good

        monkeypatch.setattr(tag_known_good, "GAIA_ROOT", registry_file)
        result = tag_known_good.get_submodules()
        assert isinstance(result, list)


# ---------------------------------------------------------------------------
# rollback: get_submodules
# ---------------------------------------------------------------------------


class TestRollbackGetSubmodules:
    def test_returns_only_gaia_submodule_paths(self, registry_file, monkeypatch):
        import rollback

        monkeypatch.setattr(rollback, "GAIA_ROOT", registry_file)
        paths = rollback.get_submodules()
        assert any("_MYCEL" in p for p in paths)
        assert any("_ARGUS" in p for p in paths)
        assert all("hart_os" not in p for p in paths)

    def test_returns_list_type(self, registry_file, monkeypatch):
        import rollback

        monkeypatch.setattr(rollback, "GAIA_ROOT", registry_file)
        result = rollback.get_submodules()
        assert isinstance(result, list)


# ---------------------------------------------------------------------------
# GENESISCollector roundtrip (cross-validation with scripts context)
# ---------------------------------------------------------------------------


class TestGENESISCollectorRoundtrip:
    def test_record_flush_roundtrip(self):
        import json

        from genesis.protocol import GENESISCollector, GENESISEvent

        collector = GENESISCollector("inst-rt", "test")
        ev = collector.record_event("pattern_detected", {"key": "value"})

        # Serialize
        raw = ev.to_json()
        restored = GENESISEvent.from_dict(json.loads(raw))

        assert restored.event_id == ev.event_id
        assert restored.source_instance == "inst-rt"
        assert restored.payload["key"] == "value"

        count = collector.flush()
        assert count == 1
        assert collector.get_pending_events() == []

    def test_protocol_version_consistent(self):
        from genesis.protocol import PROTOCOL_VERSION, GENESISCollector

        collector = GENESISCollector("inst-v")
        ev = collector.record_event("compliance_report", {})
        hb = collector.generate_heartbeat(
            gaia_version="0.5.2",
            components=["ARGUS"],
            health_score=1.0,
            compliance_score=1.0,
            active_products=[],
            uptime_hours=0.0,
        )

        assert ev.schema_version == PROTOCOL_VERSION
        assert hb.protocol_version == PROTOCOL_VERSION
