"""Tests for runtime/track_change.py -- GAIA change tracker."""

import sys
from pathlib import Path

# Ensure the runtime package is importable via absolute path
RUNTIME_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RUNTIME_DIR.parent))

import runtime.track_change as track_change_module
from runtime.track_change import classify_change, extract_component

# ---------------------------------------------------------------------------
# extract_component
# ---------------------------------------------------------------------------


class TestExtractComponent:
    def test_argus_path(self):
        assert extract_component("_ARGUS/foo.py") == "_ARGUS"

    def test_loom_nested_path(self):
        assert extract_component("_LOOM/bar/baz.py") == "_LOOM"

    def test_registry_json_is_root_file(self):
        assert extract_component("registry.json") == "ROOT:registry.json"

    def test_gaia_manifest_is_root_file(self):
        assert extract_component("GAIA_MANIFEST.md") == "ROOT:GAIA_MANIFEST.md"

    def test_runtime_directory(self):
        assert extract_component("runtime/task_runner.py") == "RUNTIME"

    def test_unrecognised_file_returns_none(self):
        assert extract_component("random_file.txt") is None

    def test_aurora_path(self):
        assert extract_component("_AURORA/design_system/tokens.json") == "_AURORA"

    def test_mycel_path(self):
        assert extract_component("_MYCEL/src/llm.py") == "_MYCEL"

    def test_warden_deeply_nested(self):
        assert extract_component("_WARDEN/warden/cli.py") == "_WARDEN"

    def test_unrelated_deep_path_returns_none(self):
        assert extract_component("docs/architecture/overview.md") is None

    def test_vulcan_path(self):
        assert extract_component("_VULCAN/ui/main.py") == "_VULCAN"

    def test_raven_path(self):
        assert extract_component("_RAVEN/raven/cli.py") == "_RAVEN"

    def test_runtime_subdirectory(self):
        result = extract_component("runtime/tests/test_task_runner.py")
        assert result == "RUNTIME"

    def test_version_log_is_root_file(self):
        assert extract_component("VERSION_LOG.md") == "ROOT:VERSION_LOG.md"


# ---------------------------------------------------------------------------
# classify_change
# ---------------------------------------------------------------------------


class TestClassifyChange:
    def test_python_file_is_code(self):
        assert classify_change("foo.py") == "code"

    def test_markdown_file_is_docs(self):
        assert classify_change("foo.md") == "docs"

    def test_json_file_is_config(self):
        assert classify_change("foo.json") == "config"

    def test_yaml_file_is_config(self):
        assert classify_change("foo.yaml") == "config"

    def test_yml_file_is_config(self):
        assert classify_change("foo.yml") == "config"

    def test_toml_file_is_config(self):
        assert classify_change("pyproject.toml") == "config"

    def test_unknown_extension_is_other(self):
        assert classify_change("foo.sh") == "other"

    def test_text_file_is_other(self):
        assert classify_change("notes.txt") == "other"


# ---------------------------------------------------------------------------
# track -- writes to CHANGES_FILE, deduplicates
# ---------------------------------------------------------------------------


class TestTrack:
    def test_track_writes_entry_for_component_file(self, tmp_path, monkeypatch):
        changes_file = tmp_path / ".gaia_changes"
        monkeypatch.setattr(track_change_module, "CHANGES_FILE", changes_file)

        track_change_module.track("_ARGUS/dashboard/app.py")

        assert changes_file.exists(), ".gaia_changes was not created"
        content = changes_file.read_text(encoding="utf-8")
        assert "_ARGUS|code|app.py" in content

    def test_track_skips_unrecognised_path(self, tmp_path, monkeypatch):
        changes_file = tmp_path / ".gaia_changes"
        monkeypatch.setattr(track_change_module, "CHANGES_FILE", changes_file)

        track_change_module.track("completely/unknown/path.txt")

        assert not changes_file.exists(), ".gaia_changes should not be created"

    def test_track_deduplicates_entries(self, tmp_path, monkeypatch):
        changes_file = tmp_path / ".gaia_changes"
        monkeypatch.setattr(track_change_module, "CHANGES_FILE", changes_file)

        track_change_module.track("_ARGUS/dashboard/app.py")
        track_change_module.track("_ARGUS/dashboard/app.py")

        lines = [ln for ln in changes_file.read_text(encoding="utf-8").splitlines() if ln]
        assert lines.count("_ARGUS|code|app.py") == 1

    def test_track_appends_distinct_entries(self, tmp_path, monkeypatch):
        changes_file = tmp_path / ".gaia_changes"
        monkeypatch.setattr(track_change_module, "CHANGES_FILE", changes_file)

        track_change_module.track("_ARGUS/dashboard/app.py")
        track_change_module.track("_AURORA/design_system/tokens.json")

        content = changes_file.read_text(encoding="utf-8")
        assert "_ARGUS|code|app.py" in content
        assert "_AURORA|config|tokens.json" in content

    def test_track_root_file(self, tmp_path, monkeypatch):
        changes_file = tmp_path / ".gaia_changes"
        monkeypatch.setattr(track_change_module, "CHANGES_FILE", changes_file)

        track_change_module.track("registry.json")

        content = changes_file.read_text(encoding="utf-8")
        assert "ROOT:registry.json|config|registry.json" in content

    def test_track_runtime_file(self, tmp_path, monkeypatch):
        changes_file = tmp_path / ".gaia_changes"
        monkeypatch.setattr(track_change_module, "CHANGES_FILE", changes_file)

        track_change_module.track("runtime/task_runner.py")

        content = changes_file.read_text(encoding="utf-8")
        assert "RUNTIME|code|task_runner.py" in content

    def test_track_preserves_existing_entries(self, tmp_path, monkeypatch):
        changes_file = tmp_path / ".gaia_changes"
        changes_file.write_text("_MYCEL|code|llm.py\n", encoding="utf-8")
        monkeypatch.setattr(track_change_module, "CHANGES_FILE", changes_file)

        track_change_module.track("_ARGUS/app.py")

        content = changes_file.read_text(encoding="utf-8")
        assert "_MYCEL|code|llm.py" in content
        assert "_ARGUS|code|app.py" in content
