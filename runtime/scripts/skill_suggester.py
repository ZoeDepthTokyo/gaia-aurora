#!/usr/bin/env python3
"""
skill_suggester.py -- PostToolUse hook: suggests relevant skill for edited file.

Usage: python skill_suggester.py --path <file_path>
Outputs 3-line Announce->Explain->Escape block when a pattern matches.
Suppress: set SKIP_SKILL_TIPS=1 in environment.
"""
import argparse
import fnmatch
import os
import sys

# Pattern -> (skill_name, reason, manual_example)
SKILL_MAP = [
    (
        "_AURORA/**",
        "auditing-ux",
        "AURORA edits frequently need design review",
        "/auditing-ux _AURORA",
    ),
    (
        "_ARGUS/dashboard/**",
        "auditing-ux",
        "dashboard changes affect UX patterns",
        "/auditing-ux _ARGUS",
    ),
    (
        "changes/*/tasks.md",
        "archiving-change",
        "all tasks done? archive the change",
        "/archiving-change <name>",
    ),
    (
        "_*/CLAUDE.md",
        "reconciling-gaia",
        "CLAUDE.md changes need cascade propagation to MANIFEST",
        "/reconciling-gaia",
    ),
    (
        "tests/test_spec_*.py",
        "validating-specs",
        "check GWT format if scenarios changed",
        "/validating-specs changes/<name>",
    ),
]


def match_pattern(path: str, pattern: str) -> bool:
    path = path.replace("\\", "/")
    if fnmatch.fnmatch(path, pattern):
        return True
    # Also try with ** collapsed to single *
    collapsed = pattern.replace("**", "*")
    if fnmatch.fnmatch(path, collapsed):
        return True
    return False


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", required=True)
    args = parser.parse_args()

    if os.environ.get("SKIP_SKILL_TIPS"):
        sys.exit(0)

    path = args.path.replace("\\", "/")

    for pattern, skill, reason, manual in SKILL_MAP:
        if match_pattern(path, pattern):
            print(f"[HOOK: skill_suggester] {path} edited", flush=True)
            print(f"-> TIP: /{skill} -- {reason}", flush=True)
            print(f"-> Manual: {manual}", flush=True)
            sys.exit(0)

    sys.exit(0)


if __name__ == "__main__":
    main()
