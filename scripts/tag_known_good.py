"""Tag all GAIA submodules + root as 'known good' at a version.

Usage: python scripts/tag_known_good.py v0.5.3
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


def tag_version(version: str) -> None:
    """Tag root + all submodules with an annotated version tag.

    Args:
        version: Tag name to apply (e.g. "v0.5.3").

    Raises:
        subprocess.CalledProcessError: If any git tag command fails.
    """
    # Tag root
    print(f"Tagging GAIA root as {version}...")
    subprocess.run(
        ["git", "tag", "-a", version, "-m", f"Known good: {version}"],
        cwd=GAIA_ROOT,
        check=True,
    )

    # Tag each submodule that has a .git directory
    for path in get_submodules():
        git_dir = os.path.join(path, ".git")
        if os.path.isdir(git_dir):
            name = os.path.basename(path)
            print(f"Tagging {name} as {version}...")
            subprocess.run(
                ["git", "tag", "-a", version, "-m", f"Known good: {version}"],
                cwd=path,
                check=True,
            )

    print(f"Tagged {version} across all submodules.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scripts/tag_known_good.py v0.5.3")
        sys.exit(1)
    tag_version(sys.argv[1])
