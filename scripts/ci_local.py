#!/usr/bin/env python
"""Thin wrapper: runs WARDEN CI simulation for a GAIA component.

Usage:
    python scripts/ci_local.py                    # auto-detect from CWD
    python scripts/ci_local.py --component mycel  # explicit
    python scripts/ci_local.py --all              # all components

This calls `python -m warden.cli ci` which WARDEN owns as CI governor.
Requires WARDEN installed: pip install -e X:/Projects/_GAIA/_WARDEN
"""

import sys
from pathlib import Path

WARDEN_PATH = Path(__file__).parent.parent / "_WARDEN"


def main() -> int:
    """Parse args and delegate to WARDEN ci_governor.

    Returns:
        Exit code: 0 when all checks pass, 1 otherwise.
    """
    sys.path.insert(0, str(WARDEN_PATH))
    try:
        from warden.ci_governor import run_ci_command
    except ImportError:
        print("[ERR] WARDEN not installed. Run: pip install -e X:/Projects/_GAIA/_WARDEN")
        return 1

    component = None
    run_all = False
    args = sys.argv[1:]
    i = 0
    while i < len(args):
        if args[i] in ("--component", "-c") and i + 1 < len(args):
            component = args[i + 1]
            i += 2
        elif args[i] in ("--all", "-a"):
            run_all = True
            i += 1
        else:
            i += 1

    return run_ci_command(component=component, run_all=run_all)


if __name__ == "__main__":
    sys.exit(main())
