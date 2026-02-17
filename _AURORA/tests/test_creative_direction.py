"""AURORA Creative Direction -- basic structural tests."""

from pathlib import Path
import json

AURORA_ROOT = Path(__file__).resolve().parent.parent


def test_creative_direction_templates_exist():
    templates = AURORA_ROOT / "creative_direction" / "templates"
    assert templates.exists(), "creative_direction/templates/ missing"


def test_creative_direction_learnings_exist():
    learnings = AURORA_ROOT / "creative_direction" / "learnings"
    assert learnings.exists(), "creative_direction/learnings/ missing"


def test_design_system_master_exists():
    master = AURORA_ROOT / "design_system" / "master"
    assert master.exists(), "design_system/master/ missing"


def test_specs_directory_exists():
    specs = AURORA_ROOT / "specs"
    assert specs.exists(), "specs/ directory missing"


def test_claude_md_has_role_section():
    claude_md = AURORA_ROOT / "CLAUDE.md"
    assert claude_md.exists(), "CLAUDE.md missing"
    text = claude_md.read_text(encoding="utf-8")
    assert "## Role" in text, "CLAUDE.md missing ## Role section"
