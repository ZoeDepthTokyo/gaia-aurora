#!/usr/bin/env python3
"""
skill_guard.py -- PreToolUse guard: blocks component edits without active change spec.

Usage: python skill_guard.py --check spec-before-code --path <file_path>
Exit 0: allow. Exit 1: block (prints explanation).
Suppress: set SKIP_SPEC_GUARD=1 in environment.
"""
import argparse
import os
import re
import sys
from pathlib import Path


def has_active_change_spec(gaia_root: Path) -> tuple:
    """Check if any changes/*/tasks.md has unchecked items."""
    changes_dir = gaia_root / "changes"
    if not changes_dir.exists():
        return False, "no changes/ directory"
    for tasks_file in changes_dir.glob("*/tasks.md"):
        content = tasks_file.read_text(encoding="utf-8", errors="ignore")
        if re.search(r"- \[ \]", content):
            return True, tasks_file.parent.name
    return False, "no active change with unchecked tasks"


def is_component_path(path: str) -> bool:
    """Returns True if path is under a GAIA component (_[A-Z]+/)."""
    return bool(re.match(r"_[A-Z]+/", path.replace("\\", "/")))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", default="spec-before-code")
    parser.add_argument("--path", required=True)
    args = parser.parse_args()

    if os.environ.get("SKIP_SPEC_GUARD"):
        sys.exit(0)

    if not is_component_path(args.path):
        sys.exit(0)

    gaia_root = Path.cwd()
    has_spec, detail = has_active_change_spec(gaia_root)

    if has_spec:
        sys.exit(0)

    print(f"BLOCKED: No active change spec found for {args.path}", flush=True)
    print(f"Rule: {args.check} (GAIA constitutional principle #6)", flush=True)
    print(
        "Why: Spec artifacts create governance audit trail before implementation",
        flush=True,
    )
    print("Fix: Run /creating-change <name>, then retry this edit", flush=True)
    print(f"Detail: {detail}", flush=True)
    sys.exit(1)


if __name__ == "__main__":
    main()
