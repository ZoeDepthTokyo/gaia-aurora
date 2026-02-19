"""
Configure git remotes for all GAIA projects.

Usage:
    python setup_remotes.py --org gaia-ecosystem
    python setup_remotes.py --org gaia-ecosystem --project mycel
    python setup_remotes.py --org gaia-ecosystem --dry-run
"""

import argparse
import json
import subprocess
from pathlib import Path

GAIA_ROOT = Path(r"X:\Projects\_GAIA")
REGISTRY_PATH = GAIA_ROOT / "registry.json"

# Mapping from registry key to GitHub repo name
REPO_NAME_MAP = {
    # Shared services (prefixed with gaia-)
    "argus": "gaia-argus",
    "loom": "gaia-loom",
    "mnemis": "gaia-mnemis",
    "mycel": "gaia-mycel",
    "raven": "gaia-raven",
    "vulcan": "gaia-vulcan",
    "warden": "gaia-warden",
    "abis": "gaia-abis",
    # Products (no prefix)
    "hart_os": "hart-os",
    "via": "via-intel",
    "data_forge": "data-forge",
    "jseeker": "jseeker",
    "dos": "dos",
    "gpt_echo": "gpt-echo",
    "the_palace": "the-palace",
    "waymo_data": "waymo-data",
}


def load_registry():
    """Load the GAIA registry.json file."""
    with open(REGISTRY_PATH) as f:
        return json.load(f)


def run_git(args, cwd=None):
    """Run a git command and return (success, output)."""
    try:
        result = subprocess.run(
            ["git"] + args,
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=30,
        )
        return result.returncode == 0, result.stdout.strip()
    except (subprocess.TimeoutExpired, FileNotFoundError) as e:
        return False, str(e)


def setup_remote(project_key, project_path, org_name, dry_run=False):
    """Setup git remote for a project."""
    path = Path(project_path)
    repo_name = REPO_NAME_MAP.get(project_key, project_key)
    remote_url = f"https://github.com/{org_name}/{repo_name}.git"

    print(f"\n[{project_key}] {path}")

    if not path.is_dir():
        print("  SKIP: Directory does not exist")
        return False

    # Check if git is initialized
    git_dir = path / ".git"
    if not git_dir.is_dir():
        if dry_run:
            print("  [DRY RUN] Would initialize git repo")
            print(f"  [DRY RUN] Would add remote: {remote_url}")
            return True

        success, output = run_git(["init"], cwd=str(path))
        if success:
            print("  INIT: Git repository initialized")
        else:
            print(f"  ERROR: Failed to initialize git: {output}")
            return False

    # Check existing remotes
    success, output = run_git(["remote", "-v"], cwd=str(path))
    if success and "origin" in output:
        print("  EXISTS: Remote 'origin' already configured")
        # Show current remote
        for line in output.splitlines():
            if line.startswith("origin"):
                print(f"    {line}")
        return True

    if dry_run:
        print(f"  [DRY RUN] Would add remote: {remote_url}")
        return True

    success, output = run_git(["remote", "add", "origin", remote_url], cwd=str(path))
    if success:
        print(f"  ADDED: origin -> {remote_url}")
        return True
    else:
        print(f"  ERROR: {output}")
        return False


def main():
    parser = argparse.ArgumentParser(description="Setup git remotes for GAIA projects")
    parser.add_argument("--org", required=True, help="GitHub organization name")
    parser.add_argument("--project", type=str, help="Specific project key (from registry)")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be done")

    args = parser.parse_args()

    registry = load_registry()
    projects = registry.get("projects", {})

    success_count = 0
    total = 0

    for key, info in sorted(projects.items()):
        if args.project and key != args.project:
            continue

        project_path = info.get("path")
        if not project_path:
            print(f"\n[{key}] SKIP: No path in registry")
            continue

        total += 1
        if setup_remote(key, project_path, args.org, args.dry_run):
            success_count += 1

    # Also setup gaia-core for the GAIA root
    if not args.project or args.project == "gaia":
        total += 1
        print(f"\n[gaia-core] {GAIA_ROOT}")
        remote_url = f"https://github.com/{args.org}/gaia-core.git"
        if args.dry_run:
            print(f"  [DRY RUN] Would add remote: {remote_url}")
            success_count += 1
        else:
            git_dir = GAIA_ROOT / ".git"
            if not git_dir.is_dir():
                run_git(["init"], cwd=str(GAIA_ROOT))
            success, existing = run_git(["remote", "-v"], cwd=str(GAIA_ROOT))
            if "origin" not in existing:
                success, output = run_git(
                    ["remote", "add", "origin", remote_url], cwd=str(GAIA_ROOT)
                )
                if success:
                    print(f"  ADDED: origin -> {remote_url}")
                    success_count += 1
            else:
                print("  EXISTS: Remote already configured")
                success_count += 1

    print(f"\n{'=' * 40}")
    print(f"Done: {success_count}/{total} projects configured")


if __name__ == "__main__":
    main()
