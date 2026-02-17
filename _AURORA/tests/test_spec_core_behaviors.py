"""AURORA core-behaviors spec tests.

Covers all 9 GWT scenarios from _AURORA/specs/core-behaviors.md:
  - Style Token Extraction (2 scenarios)
  - Mood Board Generation (2 scenarios)
  - Quick Component Design (2 scenarios)
  - Design Token Validation (2 scenarios)
  - 6-Phase Workflow Integrity (1 scenario)

AURORA has no Python source code, so these are structural/schema tests.
Helper stubs are defined within this file to model the expected contracts.
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

import pytest

AURORA_ROOT = Path(__file__).resolve().parent.parent
MASTER_TOKENS_PATH = AURORA_ROOT / "design_system" / "master" / "tokens.json"

# ---------------------------------------------------------------------------
# Helper stubs — model the contracts AURORA must satisfy
# These implement the minimum interface specified in the GWT scenarios.
# ---------------------------------------------------------------------------


@dataclass
class ExtractedTokenFile:
    """Schema for a file written by /aurora-extract-style."""

    source_url: str
    extracted_at: str  # ISO-8601 timestamp
    token_count: int
    primary_color: str
    font_families: List[str]
    spacing_scale: Dict[str, str]
    raw: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "source_url": self.source_url,
            "extracted_at": self.extracted_at,
            "token_count": self.token_count,
            "primary_color": self.primary_color,
            "font_families": self.font_families,
            "spacing_scale": self.spacing_scale,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ExtractedTokenFile":
        return cls(
            source_url=data["source_url"],
            extracted_at=data["extracted_at"],
            token_count=data["token_count"],
            primary_color=data["primary_color"],
            font_families=data["font_families"],
            spacing_scale=data["spacing_scale"],
            raw=data,
        )


@dataclass
class MoodBoardOutput:
    """Schema for mood_board.json produced by /aurora-mood."""

    project: str
    palette: List[str]
    typography: Dict[str, Any]
    mood_keywords: List[str]

    def to_dict(self) -> Dict[str, Any]:
        return {
            "project": self.project,
            "palette": self.palette,
            "typography": self.typography,
            "mood_keywords": self.mood_keywords,
        }

    @classmethod
    def validate_schema(cls, data: Dict[str, Any]) -> None:
        """Raise AssertionError if required fields are missing."""
        required = ("palette", "typography", "mood_keywords")
        for key in required:
            assert key in data, f"mood_board.json missing required key: '{key}'"
        assert isinstance(data["palette"], list), "palette must be a list"
        assert isinstance(data["mood_keywords"], list), "mood_keywords must be a list"
        assert isinstance(data["typography"], dict), "typography must be a dict"


class CheckpointWorkflow:
    """Stub: sequential 3-checkpoint mood-board workflow."""

    PHASES = ["brief", "references", "final"]

    def __init__(self) -> None:
        self._approved: List[str] = []

    @property
    def current_checkpoint(self) -> str:
        completed = len(self._approved)
        if completed >= len(self.PHASES):
            return "complete"
        return self.PHASES[completed]

    def approve(self, checkpoint: str) -> None:
        if checkpoint != self.current_checkpoint:
            raise ValueError(
                f"Cannot approve '{checkpoint}': expected '{self.current_checkpoint}'"
            )
        self._approved.append(checkpoint)

    def is_complete(self) -> bool:
        return len(self._approved) == len(self.PHASES)


class PhaseWorkflow:
    """Stub: 6-phase sequential AURORA workflow enforcing phase order."""

    VALID_PHASES = [1, 2, 3, 4, 5, 6]

    def __init__(self) -> None:
        self._current_phase: int = 1

    @property
    def current_phase(self) -> int:
        return self._current_phase

    def advance_to(self, phase: int) -> None:
        """Advance to the next phase.

        Raises:
            ValueError: If attempting to skip phases.
        """
        if phase != self._current_phase + 1:
            raise ValueError(
                f"Integrity violation: cannot jump from phase {self._current_phase} "
                f"to phase {phase}. Phases must execute sequentially."
            )
        self._current_phase = phase


def _load_master_tokens() -> Dict[str, Any]:
    """Load master tokens.json; skip test if file is absent."""
    if not MASTER_TOKENS_PATH.exists():
        pytest.skip(f"master tokens.json not found at {MASTER_TOKENS_PATH}")
    with open(MASTER_TOKENS_PATH, encoding="utf-8") as f:
        return json.load(f)


def _collect_flat_keys(d: Dict[str, Any], prefix: str = "") -> List[str]:
    """Recursively flatten dict keys with dot notation."""
    keys: List[str] = []
    for k, v in d.items():
        full = f"{prefix}.{k}" if prefix else k
        if isinstance(v, dict):
            keys.extend(_collect_flat_keys(v, full))
        else:
            keys.append(full)
    return keys


def validate_brand_kit(brand_kit: Dict[str, Any], master_tokens: Dict[str, Any]) -> None:
    """Check brand_kit for master DNA key conflicts.

    Raises:
        ValueError: If a brand key shadows a master token key.
    """
    master_keys = set(_collect_flat_keys(master_tokens))
    brand_keys = set(_collect_flat_keys(brand_kit))
    conflicts = master_keys & brand_keys
    if conflicts:
        sample = sorted(conflicts)[0]
        raise ValueError(
            f"Brand kit conflicts with master token key '{sample}'. "
            f"Master token path: {MASTER_TOKENS_PATH}"
        )


# ---------------------------------------------------------------------------
# Requirement: Style Token Extraction
# ---------------------------------------------------------------------------


class TestStyleTokenExtraction:
    """Scenarios for /aurora-extract-style output schema."""

    def test_extract_tokens_schema_valid(self, tmp_path: Path):
        """Scenario: Extract tokens from valid URL — output schema is correct.

        GIVEN a URL is extracted
        WHEN a JSON token file is written to extracted_styles/
        THEN it contains primary_color, font_families, and spacing_scale
        """
        token_file = ExtractedTokenFile(
            source_url="https://example.com",
            extracted_at=datetime.now(timezone.utc).isoformat(),
            token_count=42,
            primary_color="#0070f3",
            font_families=["Inter", "system-ui"],
            spacing_scale={"4": "16px", "8": "32px"},
        )

        output_path = tmp_path / "example_com.json"
        output_path.write_text(json.dumps(token_file.to_dict()), encoding="utf-8")

        data = json.loads(output_path.read_text(encoding="utf-8"))
        assert "primary_color" in data, "Missing primary_color in token file"
        assert "font_families" in data, "Missing font_families in token file"
        assert "spacing_scale" in data, "Missing spacing_scale in token file"
        assert data["font_families"], "font_families must be non-empty"
        assert data["spacing_scale"], "spacing_scale must be non-empty"

    def test_extraction_preserves_provenance(self, tmp_path: Path):
        """Scenario: Extraction preserves source provenance.

        GIVEN a URL is extracted
        WHEN the tokens file is written
        THEN it includes source_url, extracted_at timestamp, and token_count
        """
        url = "https://example.com"
        token_file = ExtractedTokenFile(
            source_url=url,
            extracted_at="2026-02-17T12:00:00+00:00",
            token_count=15,
            primary_color="#111827",
            font_families=["Roboto"],
            spacing_scale={"2": "8px"},
        )

        data = token_file.to_dict()

        assert data.get("source_url") == url, "source_url must match the extracted URL"
        assert data.get("extracted_at"), "extracted_at timestamp must be present and non-empty"
        assert isinstance(data.get("token_count"), int), "token_count must be an integer"
        assert data["token_count"] > 0, "token_count must be positive"


# ---------------------------------------------------------------------------
# Requirement: Mood Board Generation
# ---------------------------------------------------------------------------


class TestMoodBoardGeneration:
    """Scenarios for /aurora-mood checkpoint gating and output schema."""

    def test_checkpoint_gating_enforced(self):
        """Scenario: Checkpoint gating is enforced.

        GIVEN a mood board workflow is initiated
        WHEN the user does not approve checkpoint 1 (brief)
        THEN the workflow does not advance to checkpoint 2 (references)
        """
        workflow = CheckpointWorkflow()
        # Initial state is at checkpoint 1 (brief)
        assert workflow.current_checkpoint == "brief"

        # Attempting to approve a later checkpoint must fail
        with pytest.raises(ValueError, match="Cannot approve"):
            workflow.approve("references")

        # Checkpoint must still be at "brief"
        assert workflow.current_checkpoint == "brief"

    def test_mood_board_produces_token_output(self, tmp_path: Path):
        """Scenario: Mood board produces token output after all 3 checkpoints.

        GIVEN a project with all 3 checkpoints approved
        WHEN mood_board.json is written
        THEN it contains palette, typography, and mood_keywords
        """
        workflow = CheckpointWorkflow()
        workflow.approve("brief")
        workflow.approve("references")
        workflow.approve("final")
        assert workflow.is_complete()

        output = MoodBoardOutput(
            project="test_project",
            palette=["#0070f3", "#7c3aed", "#10b981"],
            typography={"primary": "Inter", "mono": "JetBrains Mono"},
            mood_keywords=["modern", "minimalist", "accessible"],
        )

        output_dir = tmp_path / "mood_boards" / "test_project"
        output_dir.mkdir(parents=True)
        output_path = output_dir / "mood_board.json"
        output_path.write_text(json.dumps(output.to_dict()), encoding="utf-8")

        data = json.loads(output_path.read_text(encoding="utf-8"))
        MoodBoardOutput.validate_schema(data)

        assert data["palette"], "palette must be non-empty"
        assert data["mood_keywords"], "mood_keywords must be non-empty"


# ---------------------------------------------------------------------------
# Requirement: Quick Component Design
# ---------------------------------------------------------------------------


class TestQuickComponentDesign:
    """Scenarios for /aurora-quick fallback to master tokens."""

    def test_quick_task_completes_without_mood_board(self):
        """Scenario: Quick task completes without mood board.

        GIVEN no mood board exists for the project
        WHEN /aurora-quick is invoked
        THEN it falls back to master tokens and does not block
        """
        assert MASTER_TOKENS_PATH.exists(), (
            f"Master tokens.json must exist at {MASTER_TOKENS_PATH} for fallback"
        )
        tokens = _load_master_tokens()
        assert tokens, "Master tokens file must not be empty"

        # Simulate: no mood board dir for project
        project_mood_board = AURORA_ROOT / "creative_direction" / "mood_boards" / "nonexistent_proj"
        has_mood_board = project_mood_board.exists()

        # Regardless of mood board presence, master tokens are available
        assert "spacing" in tokens or "typography" in tokens or "color" in tokens, (
            "Master tokens must contain at least one of: spacing, typography, color"
        )

    def test_quick_task_references_master_tokens(self):
        """Scenario: Quick task references master token constraints.

        GIVEN a quick task description mentions colors or spacing
        WHEN the spec is generated
        THEN all token references are drawn from design_system/master/tokens.json
        """
        tokens = _load_master_tokens()

        # Verify master token file has the top-level categories expected
        required_categories = {"typography", "spacing", "color"}
        present = {k for k in tokens if k in required_categories}
        assert present == required_categories, (
            f"Master tokens.json missing categories: {required_categories - present}"
        )

        # Verify spacing scale is populated
        spacing_scale = tokens.get("spacing", {}).get("scale", {})
        assert spacing_scale, "Master tokens.json must have a non-empty spacing.scale"

        # Verify at least one font family defined
        font_primary = tokens.get("typography", {}).get("fontFamily", {}).get("primary")
        assert font_primary, "Master tokens.json must define typography.fontFamily.primary"


# ---------------------------------------------------------------------------
# Requirement: Design Token Validation
# ---------------------------------------------------------------------------


class TestDesignTokenValidation:
    """Scenarios for 30/70 master DNA enforcement."""

    def test_override_attempt_is_blocked(self):
        """Scenario: Override attempt is blocked.

        GIVEN a brand kit sets a key that exists in master/tokens.json
        WHEN the brand kit is validated
        THEN ValueError is raised identifying the conflicting key
        """
        master_tokens = _load_master_tokens()

        # Extract a known master key to conflict with
        spacing_scale = master_tokens.get("spacing", {}).get("scale", {})
        assert spacing_scale, "Master tokens must have spacing.scale for this test"
        conflict_value = next(iter(spacing_scale.values()))

        # Build a brand kit that tries to override spacing.scale
        brand_kit = {
            "spacing": {
                "scale": {
                    next(iter(spacing_scale)): conflict_value  # same key
                }
            }
        }

        with pytest.raises(ValueError, match="conflicts with master token"):
            validate_brand_kit(brand_kit, master_tokens)

    def test_non_dna_override_is_allowed(self):
        """Scenario: Non-DNA token override is allowed.

        GIVEN a brand kit sets a color not present in master/tokens.json
        WHEN the brand kit is validated
        THEN no error is raised and the custom color is accepted
        """
        master_tokens = _load_master_tokens()

        # Use a brand-specific key that does NOT exist in master
        brand_kit = {
            "brand": {
                "accent": "#ff6b6b",
                "hero": "#4ecdc4",
            }
        }

        # Must not raise
        try:
            validate_brand_kit(brand_kit, master_tokens)
        except ValueError as exc:
            pytest.fail(
                f"validate_brand_kit raised ValueError for non-conflicting brand key: {exc}"
            )


# ---------------------------------------------------------------------------
# Requirement: 6-Phase Workflow Integrity
# ---------------------------------------------------------------------------


class TestWorkflowIntegrity:
    """Scenario: Phase skip attempt is blocked."""

    def test_phase_skip_is_blocked(self):
        """Scenario: Phase skip attempt is blocked.

        GIVEN a workflow instance is in Phase 2 (Inspiration)
        WHEN a caller attempts to invoke Phase 4 (Build Order) directly
        THEN ValueError is raised and current phase remains at 2
        """
        workflow = PhaseWorkflow()
        workflow.advance_to(2)  # Move from 1 to 2
        assert workflow.current_phase == 2

        # Attempt to jump to phase 4 (skipping 3)
        with pytest.raises(ValueError, match="Integrity violation"):
            workflow.advance_to(4)

        # Phase must remain at 2
        assert workflow.current_phase == 2, (
            "Workflow phase must remain at 2 after rejected skip attempt"
        )

    def test_sequential_advance_is_accepted(self):
        """Phases can advance one step at a time through all 6 phases."""
        workflow = PhaseWorkflow()
        for expected_phase in range(2, 7):
            workflow.advance_to(expected_phase)
            assert workflow.current_phase == expected_phase

    def test_reverse_phase_is_blocked(self):
        """Attempting to go backwards is also an integrity violation."""
        workflow = PhaseWorkflow()
        workflow.advance_to(2)
        workflow.advance_to(3)

        with pytest.raises(ValueError, match="Integrity violation"):
            workflow.advance_to(2)
