"""Rollback all GAIA submodules to a known-good tag.

Usage: python scripts/rollback.py v0.5.2
"""
import json
import os
import subprocess
import sys

GAIA_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_submodules() -> list:
    """Read submodule paths from registry.json.

    Returns:
        List of filesystem paths for GAIA submodule directories.

    Raises:
        FileNotFoundError: If registry.json does not exist.
        json.JSONDecodeError: If registry.json is malformed.
    """
    registry_path = os.path.join(GAIA_ROOT, "registry.json")
    with open(registry_path) as f:
        registry = json.load(f)

    submodule_dirs = []
    for key, project in registry["projects"].items():
        path = project.get("path", "")
        if "_GAIA/_" in path.replace("\\", "/"):
            submodule_dirs.append(path)
    return submodule_dirs


def rollback_to(version: str) -> None:
    """Checkout tagged version in root + all submodules.

    Args:
        version: Tag name to roll back to (e.g. "v0.5.2").

    Raises:
        SystemExit: If the tag is not found in the GAIA root repository.
        subprocess.CalledProcessError: If any git checkout command fails.
    """
    print(f"Rolling back to {version}...")

    # Verify tag exists in root before touching anything
    result = subprocess.run(
        ["git", "tag", "-l", version],
        capture_output=True,
        text=True,
        cwd=GAIA_ROOT,
    )
    if version not in result.stdout:
        print(f"ERROR: Tag {version} not found in GAIA root")
        sys.exit(1)

    # Checkout root
    subprocess.run(["git", "checkout", version], cwd=GAIA_ROOT, check=True)

    # Checkout each submodule that has a .git directory
    for path in get_submodules():
        git_dir = os.path.join(path, ".git")
        if os.path.isdir(git_dir):
            name = os.path.basename(path)
            print(f"Rolling back {name} to {version}...")
            subprocess.run(["git", "checkout", version], cwd=path, check=True)

    print(f"Rolled back to {version}.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scripts/rollback.py v0.5.2")
        sys.exit(1)
    rollback_to(sys.argv[1])
