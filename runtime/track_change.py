"""GAIA Change Tracker — logs component-level changes for /reconcile.

Called by PostToolUse hook on Edit/Write to component directories.
Usage: python track_change.py <file_path>
"""

import os
import re
import sys
from pathlib import Path

GAIA_ROOT = Path(__file__).resolve().parent.parent
CHANGES_FILE = GAIA_ROOT / ".gaia_changes"

# Patterns that identify GAIA component directories
COMPONENT_PATTERN = re.compile(
    r"[_/\\](ARGUS|AURORA|LOOM|MNEMIS|MYCEL|VULCAN|WARDEN|RAVEN|ABIS|ECHO|PROTEUS_ARCHIVED)[/\\]",
    re.IGNORECASE,
)
ROOT_FILES = {
    "registry.json",
    "GAIA_MANIFEST.md",
    "GAIA_PRD.md",
    "GAIA_BIBLE.md",
    "VERSION_LOG.md",
    "GECO_AUDIT.md",
    "GECO_REVIEW_MATRIX.md",
    "CALIBRATION.md",
}


def extract_component(path: str) -> str | None:
    """Extract component name from file path."""
    match = COMPONENT_PATTERN.search(path)
    if match:
        return f"_{match.group(1).upper()}"
    # Check if it's a root-level governance file
    basename = os.path.basename(path)
    if basename in ROOT_FILES:
        return f"ROOT:{basename}"
    # Check runtime directory
    if "runtime" in path.lower():
        return "RUNTIME"
    return None


def classify_change(path: str) -> str:
    """Classify the type of change."""
    if path.endswith(".py"):
        return "code"
    if path.endswith((".json", ".yaml", ".yml", ".toml")):
        return "config"
    if path.endswith(".md"):
        return "docs"
    if "test" in path.lower():
        return "tests"
    return "other"


def track(filepath: str) -> None:
    """Append component change to .gaia_changes (deduplicated)."""
    component = extract_component(filepath)
    if not component:
        return

    change_type = classify_change(filepath)
    entry = f"{component}|{change_type}|{os.path.basename(filepath)}"

    # Read existing entries for dedup
    existing = set()
    if CHANGES_FILE.exists():
        existing = set(CHANGES_FILE.read_text(encoding="utf-8").strip().splitlines())

    if entry not in existing:
        with open(CHANGES_FILE, "a", encoding="utf-8") as f:
            f.write(entry + "\n")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        track(sys.argv[1])
