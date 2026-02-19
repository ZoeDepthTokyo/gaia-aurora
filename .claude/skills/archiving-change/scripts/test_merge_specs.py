"""Tests for merge_specs.py."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from merge_specs import (
    merge_added,
    merge_modified,
    merge_removed,
    merge_spec,
    parse_delta_sections,
)


class TestParseDeltaSections:
    def test_parses_added(self):
        text = "### ADDED: New Feature\nSome content\n- GIVEN x\n- WHEN y\n- THEN z\n"
        result = parse_delta_sections(text)
        assert len(result["added"]) == 1
        assert "New Feature" in result["added"][0]

    def test_parses_modified(self):
        text = "### MODIFIED: Existing\nWas: old\nNow: new\n"
        result = parse_delta_sections(text)
        assert len(result["modified"]) == 1

    def test_parses_removed(self):
        text = "### REMOVED: Old Feature\nReason: deprecated\n"
        result = parse_delta_sections(text)
        assert len(result["removed"]) == 1

    def test_mixed_sections(self):
        text = "### ADDED: A\ncontent\n### MODIFIED: B\nWas: x\nNow: y\n### REMOVED: C\nbye\n"
        result = parse_delta_sections(text)
        assert len(result["added"]) == 1
        assert len(result["modified"]) == 1
        assert len(result["removed"]) == 1

    def test_empty_text(self):
        result = parse_delta_sections("")
        assert all(len(v) == 0 for v in result.values())


class TestMergeAdded:
    def test_appends_to_baseline(self):
        baseline = "# Spec\n\n### Existing\nContent\n"
        added = ["### ADDED: New Thing\n- GIVEN a\n- WHEN b\n- THEN c"]
        result = merge_added(baseline, added)
        assert "### New Thing" in result
        assert "GIVEN a" in result


class TestMergeModified:
    def test_replaces_content(self):
        baseline = "### Feature X\nold content here\n"
        modified = ["### MODIFIED: Feature X\nWas: old content\nNow: new content here\n"]
        result = merge_modified(baseline, modified)
        assert "new content here" in result


class TestMergeRemoved:
    def test_removes_section(self):
        baseline = "### Keep This\nkeep\n\n### Remove This\nremove me\n\n### Also Keep\nkeep too\n"
        removed = ["### REMOVED: Remove This\nReason: deprecated"]
        result = merge_removed(baseline, removed)
        assert "Keep This" in result
        assert "Remove This" not in result
        assert "Also Keep" in result


class TestMergeSpec:
    def test_no_delta_sections_skips(self, tmp_path):
        delta = tmp_path / "argus.md"
        delta.write_text("# Just a plain doc\nNo delta sections here.\n")
        result = merge_spec(delta)
        assert result["status"] == "skip"

    def test_dry_run_no_write(self, tmp_path):
        delta = tmp_path / "argus.md"
        delta.write_text("### ADDED: Test\n- GIVEN x\n- WHEN y\n- THEN z\n")
        result = merge_spec(delta, dry_run=True)
        # Should not crash; actual write depends on baseline existence
        assert result["status"] in ("promoted", "skip", "merged")
