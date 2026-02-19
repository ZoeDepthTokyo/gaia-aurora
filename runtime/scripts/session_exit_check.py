#!/usr/bin/env python3
"""
session_exit_check.py -- Stop hook: session recap + advisories on exit.
Always exits 0 (never blocks). Prints what was automated + what to do next.
"""

import re
import sys
from pathlib import Path


def main():
    gaia_root = Path.cwd()
    # Try to find GAIA root by looking for registry.json
    for candidate in [Path.cwd(), Path(__file__).parent.parent.parent]:
        if (candidate / "registry.json").exists():
            gaia_root = candidate
            break

    # -- Gather state ---------------------------------------------------------
    changes_entries = []
    gaia_changes = gaia_root / ".gaia_changes"
    if gaia_changes.exists():
        content = gaia_changes.read_text(encoding="utf-8", errors="ignore").strip()
        if content:
            changes_entries = [line for line in content.splitlines() if line.strip()]

    unchecked_tasks = {}  # change_name -> count
    changes_dir = gaia_root / "changes"
    if changes_dir.exists():
        for tasks_file in changes_dir.glob("*/tasks.md"):
            content = tasks_file.read_text(encoding="utf-8", errors="ignore")
            count = len(re.findall(r"- \[ \]", content))
            if count > 0:
                unchecked_tasks[tasks_file.parent.name] = count

    # -- SESSION RECAP --------------------------------------------------------
    print("", flush=True)
    print("=" * 60, flush=True)
    print("SESSION RECAP", flush=True)
    print("=" * 60, flush=True)
    print(f"  Files tracked in .gaia_changes: {len(changes_entries)}", flush=True)
    if changes_entries:
        for entry in changes_entries[:5]:
            print(f"    - {entry}", flush=True)
        if len(changes_entries) > 5:
            print(f"    ... and {len(changes_entries) - 5} more", flush=True)
    print(f"  Active changes with unchecked tasks: {len(unchecked_tasks)}", flush=True)
    if unchecked_tasks:
        for name, count in unchecked_tasks.items():
            print(f"    - {name}: {count} unchecked item(s)", flush=True)

    # -- ADVISORIES -----------------------------------------------------------
    advisories = []

    if changes_entries:
        advisories.append(
            (
                f".gaia_changes has {len(changes_entries)} entr(ies)"
                " -> run /reconciling-gaia before next session",
                "Why: cascade propagation keeps MANIFEST and GECO matrix"
                " current with component changes",
            )
        )

    for name, count in unchecked_tasks.items():
        advisories.append(
            (
                f"changes/{name}/tasks.md has {count} unchecked item(s)",
                "Why: incomplete tasks block /archiving-change" " and leave the audit trail open",
            )
        )

    if advisories:
        print("", flush=True)
        print("ADVISORIES", flush=True)
        print("-" * 60, flush=True)
        for msg, why in advisories:
            print(f"[!] {msg}", flush=True)
            print(f"    {why}", flush=True)
    else:
        print("", flush=True)
        print("[OK] No advisories -- session state is clean.", flush=True)

    print("=" * 60, flush=True)
    sys.exit(0)


if __name__ == "__main__":
    main()
