"""
Install pre-commit hooks to all GAIA projects.

Usage:
    python install_precommit.py --all
    python install_precommit.py --project jSeeker
    python install_precommit.py --all --dry-run
"""

import argparse
import json
import shutil
import sys
from pathlib import Path

GAIA_ROOT = Path(r"X:\Projects\_GAIA")
REGISTRY_PATH = GAIA_ROOT / "registry.json"
TEMPLATE_PATH = GAIA_ROOT / ".pre-commit-config-template.yaml"


def load_registry():
    """Load GAIA registry."""
    with open(REGISTRY_PATH) as f:
        return json.load(f)


def get_project_paths(registry, project_name=None):
    """Get project paths from registry."""
    projects = registry.get("projects", {})
    paths = {}

    for name, info in projects.items():
        project_path = info.get("path")
        if project_path:
            if project_name and name != project_name.lower():
                continue
            paths[name] = Path(project_path)

    return paths


def install_precommit_config(project_path: Path, template_path: Path, dry_run: bool = False):
    """Copy pre-commit config template to project."""
    target = project_path / ".pre-commit-config.yaml"

    if not project_path.is_dir():
        print(f"  SKIP: {project_path} does not exist")
        return False

    if target.exists():
        print(f"  EXISTS: {target} (skipping)")
        return True

    if dry_run:
        print(f"  [DRY RUN] Would copy template to: {target}")
        return True

    shutil.copy2(template_path, target)
    print(f"  INSTALLED: {target}")
    return True


def main():
    parser = argparse.ArgumentParser(description="Install pre-commit config to GAIA projects")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--all", action="store_true", help="Install to all projects")
    group.add_argument("--project", type=str, help="Install to specific project")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be done")

    args = parser.parse_args()

    if not TEMPLATE_PATH.exists():
        print(f"Error: Template not found at {TEMPLATE_PATH}")
        sys.exit(1)

    registry = load_registry()
    project_paths = get_project_paths(registry, args.project)

    if not project_paths:
        print("No matching projects found in registry")
        sys.exit(1)

    print(f"Installing pre-commit config to {len(project_paths)} project(s):")
    print()

    success = 0
    for name, path in sorted(project_paths.items()):
        print(f"[{name}]")
        if install_precommit_config(path, TEMPLATE_PATH, args.dry_run):
            success += 1
        print()

    print(f"Done: {success}/{len(project_paths)} projects configured")


if __name__ == "__main__":
    main()
