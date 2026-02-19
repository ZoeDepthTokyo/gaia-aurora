"""Tests for validate_specs.py -- GAIA spec format validator."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from validate_specs import _validate_spec_file, validate_change  # noqa: E402

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

VALID_PROPOSAL = """\
## intent
Introduce new governance pipeline.

## scope
Affects runtime and registry components.

## out of scope
UI changes are deferred.

## success criteria
All 27 GECO checks pass with no regressions.
"""

VALID_SPEC = """\
change: governance-pipeline
version: 1.0
last updated: 2026-02-17

### ADDED: New cascade propagation rule

- GIVEN a component CLAUDE.md is modified
- WHEN the reconcile skill runs
- THEN the MANIFEST row is updated automatically within 5 seconds

#### Scenario: Basic cascade test
"""

VALID_DESIGN = """\
## Technical Approach
Use a PostToolUse hook to detect changes and write to .gaia_changes.
"""

VALID_TASKS = """\
- [ ] Write cascade parser
- [ ] Hook into reconcile skill
- [x] Draft proposal
"""


def _make_change_dir(tmp_path: Path, **overrides) -> Path:
    """Create a minimal valid change directory, allowing per-artifact overrides."""
    change = tmp_path / "my-change"
    change.mkdir()
    specs = change / "specs"
    specs.mkdir()

    files = {
        "proposal.md": VALID_PROPOSAL,
        "design.md": VALID_DESIGN,
        "tasks.md": VALID_TASKS,
        "specs/component.md": VALID_SPEC,
    }
    files.update(overrides)

    for rel_path, content in files.items():
        if content is None:
            continue  # skip creating this artifact
        dest = change / rel_path
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(content, encoding="utf-8")

    return change


# ---------------------------------------------------------------------------
# validate_change -- artifact completeness
# ---------------------------------------------------------------------------


class TestValidChangeDirectory:
    def test_valid_change_passes_with_no_errors(self, tmp_path):
        change = _make_change_dir(tmp_path)
        result = validate_change(change)
        assert result["errors"] == [], f"Unexpected errors: {result['errors']}"

    def test_valid_change_has_correct_name(self, tmp_path):
        change = _make_change_dir(tmp_path)
        result = validate_change(change)
        assert result["name"] == "my-change"

    def test_valid_change_populates_checks(self, tmp_path):
        change = _make_change_dir(tmp_path)
        result = validate_change(change)
        assert len(result["checks"]) > 0


class TestMissingArtifacts:
    def test_missing_proposal_raises_error(self, tmp_path):
        change = _make_change_dir(tmp_path, **{"proposal.md": None})
        result = validate_change(change)
        assert any("proposal.md" in e for e in result["errors"])

    def test_missing_specs_dir_raises_error(self, tmp_path):
        change = _make_change_dir(tmp_path)
        # Remove specs directory after creation
        import shutil

        shutil.rmtree(change / "specs")
        result = validate_change(change)
        assert any("specs/" in e for e in result["errors"])

    def test_empty_specs_dir_raises_error(self, tmp_path):
        change = _make_change_dir(tmp_path)
        # Remove the spec file, leaving an empty specs/ dir
        (change / "specs" / "component.md").unlink()
        result = validate_change(change)
        assert any("empty" in e for e in result["errors"])

    def test_missing_design_raises_error(self, tmp_path):
        change = _make_change_dir(tmp_path, **{"design.md": None})
        result = validate_change(change)
        assert any("design.md" in e for e in result["errors"])

    def test_missing_tasks_raises_error(self, tmp_path):
        change = _make_change_dir(tmp_path, **{"tasks.md": None})
        result = validate_change(change)
        assert any("tasks.md" in e for e in result["errors"])


class TestProposalSections:
    def test_missing_proposal_section_produces_warning(self, tmp_path):
        # Remove the "intent" section so the validator warns about it.
        # (Removing "scope" doesn't work because "out of scope" still contains "scope".)
        proposal_no_intent = VALID_PROPOSAL.replace(
            "## intent\nIntroduce new governance pipeline.\n\n", ""
        )
        change = _make_change_dir(tmp_path, **{"proposal.md": proposal_no_intent})
        result = validate_change(change)
        assert any("intent" in w for w in result["warnings"])

    def test_complete_proposal_no_section_warnings(self, tmp_path):
        change = _make_change_dir(tmp_path)
        result = validate_change(change)
        section_warnings = [w for w in result["warnings"] if "missing sections" in w]
        assert section_warnings == []


class TestTasksFile:
    def test_tasks_without_checkboxes_produces_warning(self, tmp_path):
        tasks_no_boxes = "Task 1\nTask 2\nTask 3\n"
        change = _make_change_dir(tmp_path, **{"tasks.md": tasks_no_boxes})
        result = validate_change(change)
        assert any("checkbox" in w for w in result["warnings"])


# ---------------------------------------------------------------------------
# _validate_spec_file -- delta format compliance
# ---------------------------------------------------------------------------


class TestAddedRequirements:
    def test_added_with_gwt_passes(self, tmp_path):
        """ADDED block that has full GWT should produce no GWT errors."""
        spec = tmp_path / "spec.md"
        spec.write_text(VALID_SPEC, encoding="utf-8")
        results = {"errors": [], "warnings": [], "checks": []}
        _validate_spec_file(spec, results)
        gwt_errors = [e for e in results["errors"] if "Given-When-Then" in e]
        assert gwt_errors == []

    def test_added_without_gwt_produces_error(self, tmp_path):
        spec_content = """\
change: test
version: 1.0
last updated: 2026-02-17

### ADDED: My new requirement

Some description with no scenario.
"""
        spec = tmp_path / "spec.md"
        spec.write_text(spec_content, encoding="utf-8")
        results = {"errors": [], "warnings": [], "checks": []}
        _validate_spec_file(spec, results)
        assert any("Given-When-Then" in e for e in results["errors"])

    def test_added_missing_given_only_produces_error(self, tmp_path):
        spec_content = """\
change: test
version: 1.0
last updated: 2026-02-17

### ADDED: Partial scenario

- WHEN something happens
- THEN something is returned
"""
        spec = tmp_path / "spec.md"
        spec.write_text(spec_content, encoding="utf-8")
        results = {"errors": [], "warnings": [], "checks": []}
        _validate_spec_file(spec, results)
        assert any("Given-When-Then" in e for e in results["errors"])


class TestVagueWords:
    def test_then_with_vague_word_produces_warning(self, tmp_path):
        spec_content = """\
change: test
version: 1.0
last updated: 2026-02-17

### ADDED: Requirement with vague then

- GIVEN a valid input
- WHEN processing runs
- THEN the system works correctly
"""
        spec = tmp_path / "spec.md"
        spec.write_text(spec_content, encoding="utf-8")
        results = {"errors": [], "warnings": [], "checks": []}
        _validate_spec_file(spec, results)
        vague_warnings = [w for w in results["warnings"] if "vague word" in w]
        assert len(vague_warnings) >= 1

    def test_then_without_vague_words_no_warning(self, tmp_path):
        spec = tmp_path / "spec.md"
        spec.write_text(VALID_SPEC, encoding="utf-8")
        results = {"errors": [], "warnings": [], "checks": []}
        _validate_spec_file(spec, results)
        vague_warnings = [w for w in results["warnings"] if "vague word" in w]
        assert vague_warnings == []


class TestWindowsPaths:
    def test_windows_path_produces_warning(self, tmp_path):
        spec_content = VALID_SPEC + "\nSee C:\\Users\\Fede\\file.py for reference.\n"
        spec = tmp_path / "spec.md"
        spec.write_text(spec_content, encoding="utf-8")
        results = {"errors": [], "warnings": [], "checks": []}
        _validate_spec_file(spec, results)
        assert any("Windows" in w for w in results["warnings"])

    def test_forward_slash_paths_no_warning(self, tmp_path):
        spec = tmp_path / "spec.md"
        spec.write_text(VALID_SPEC, encoding="utf-8")
        results = {"errors": [], "warnings": [], "checks": []}
        _validate_spec_file(spec, results)
        windows_warnings = [w for w in results["warnings"] if "Windows" in w]
        assert windows_warnings == []


class TestDuplicateRequirements:
    def test_duplicate_requirement_name_produces_error(self, tmp_path):
        spec_content = """\
change: test
version: 1.0
last updated: 2026-02-17

### ADDED: My requirement

- GIVEN a state
- WHEN action occurs
- THEN result follows

### ADDED: My requirement

- GIVEN another state
- WHEN another action occurs
- THEN another result follows
"""
        spec = tmp_path / "spec.md"
        spec.write_text(spec_content, encoding="utf-8")
        results = {"errors": [], "warnings": [], "checks": []}
        _validate_spec_file(spec, results)
        assert any("duplicate" in e for e in results["errors"])

    def test_unique_requirement_names_no_error(self, tmp_path):
        spec = tmp_path / "spec.md"
        spec.write_text(VALID_SPEC, encoding="utf-8")
        results = {"errors": [], "warnings": [], "checks": []}
        _validate_spec_file(spec, results)
        dup_errors = [e for e in results["errors"] if "duplicate" in e]
        assert dup_errors == []


class TestModifiedRequirements:
    def test_modified_without_was_produces_error(self, tmp_path):
        spec_content = """\
change: test
version: 1.0
last updated: 2026-02-17

### MODIFIED: Existing requirement

Now: The new behavior after change.
"""
        spec = tmp_path / "spec.md"
        spec.write_text(spec_content, encoding="utf-8")
        results = {"errors": [], "warnings": [], "checks": []}
        _validate_spec_file(spec, results)
        assert any("Was:" in e for e in results["errors"])

    def test_modified_without_now_produces_error(self, tmp_path):
        spec_content = """\
change: test
version: 1.0
last updated: 2026-02-17

### MODIFIED: Existing requirement

Was: The old behavior before change.
"""
        spec = tmp_path / "spec.md"
        spec.write_text(spec_content, encoding="utf-8")
        results = {"errors": [], "warnings": [], "checks": []}
        _validate_spec_file(spec, results)
        assert any("Now:" in e for e in results["errors"])

    def test_modified_with_both_was_and_now_passes(self, tmp_path):
        spec_content = """\
change: test
version: 1.0
last updated: 2026-02-17

### MODIFIED: Existing requirement

Was: The old behavior before change.
Now: The new behavior after change.
"""
        spec = tmp_path / "spec.md"
        spec.write_text(spec_content, encoding="utf-8")
        results = {"errors": [], "warnings": [], "checks": []}
        _validate_spec_file(spec, results)
        mod_errors = [e for e in results["errors"] if "MODIFIED" in e or "Was:" in e or "Now:" in e]
        assert mod_errors == []


class TestSpecHeaderFields:
    def test_missing_header_field_produces_warning(self, tmp_path):
        spec_content = """\
change: test
version: 1.0

### ADDED: A requirement

- GIVEN state
- WHEN action
- THEN result
"""
        spec = tmp_path / "spec.md"
        spec.write_text(spec_content, encoding="utf-8")
        results = {"errors": [], "warnings": [], "checks": []}
        _validate_spec_file(spec, results)
        # "last updated" is missing
        assert any("last updated" in w for w in results["warnings"])

    def test_all_header_fields_present_no_warning(self, tmp_path):
        spec = tmp_path / "spec.md"
        spec.write_text(VALID_SPEC, encoding="utf-8")
        results = {"errors": [], "warnings": [], "checks": []}
        _validate_spec_file(spec, results)
        header_warnings = [
            w
            for w in results["warnings"]
            if any(f in w for f in ("change:", "version:", "last updated:"))
        ]
        assert header_warnings == []
