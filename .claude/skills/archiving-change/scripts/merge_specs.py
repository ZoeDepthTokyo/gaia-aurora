"""merge_specs.py -- Merge delta specs from completed change into component baselines.

Usage:
    python merge_specs.py <change-name> [--dry-run]

Exit codes:
    0   Success
    1   Change not found
    2   Merge conflict
"""

import re
import sys
from pathlib import Path

GAIA_ROOT = Path(__file__).resolve().parents[4]  # .claude/skills/archiving-change/scripts/ -> root
ARCHIVE_DIR = GAIA_ROOT / "changes" / "archive"

# Map spec filename to component baseline directory
COMPONENT_MAP = {
    "argus": GAIA_ROOT / "_ARGUS" / "specs",
    "aurora": GAIA_ROOT / "_AURORA" / "specs",
    "loom": GAIA_ROOT / "_LOOM" / "specs",
    "mnemis": GAIA_ROOT / "_MNEMIS" / "specs",
    "mycel": GAIA_ROOT / "_MYCEL" / "specs",
    "vulcan": GAIA_ROOT / "_VULCAN" / "specs",
    "warden": GAIA_ROOT / "_WARDEN" / "specs",
    "raven": GAIA_ROOT / "_RAVEN" / "specs",
    "abis": GAIA_ROOT / "_ABIS" / "specs",
    "runtime": GAIA_ROOT / "runtime" / "specs",
}


def parse_delta_sections(text: str) -> dict:
    """Parse ADDED/MODIFIED/REMOVED sections from delta spec."""
    sections = {"added": [], "modified": [], "removed": []}
    pattern = r"###\s+(ADDED|MODIFIED|REMOVED):\s+(.+?)(?=\n###\s+(?:ADDED|MODIFIED|REMOVED):|\Z)"
    for match in re.finditer(pattern, text, re.DOTALL):
        action = match.group(1).lower()
        content = f"### {match.group(1)}: {match.group(2)}"
        sections[action].append(content.strip())
    return sections


def find_baseline(spec_name: str) -> Path | None:
    """Find baseline spec file for a component."""
    component = spec_name.replace(".md", "").lower()
    if component in COMPONENT_MAP:
        baseline_dir = COMPONENT_MAP[component]
        baseline = baseline_dir / "core-behaviors.md"
        if baseline.exists():
            return baseline
        # Try matching filename directly
        direct = baseline_dir / spec_name
        if direct.exists():
            return direct
    return None


def merge_added(baseline_text: str, added_sections: list[str]) -> str:
    """Append ADDED sections to end of baseline."""
    result = baseline_text.rstrip()
    for section in added_sections:
        # Convert ADDED to regular requirement heading
        heading = section.split("\n")[0]
        req_name = re.sub(r"###\s+ADDED:\s+", "### ", heading)
        body = "\n".join(section.split("\n")[1:])
        result += f"\n\n{req_name}\n{body}"
    return result + "\n"


def merge_modified(baseline_text: str, modified_sections: list[str]) -> str:
    """Apply MODIFIED sections: find matching heading, replace content."""
    result = baseline_text
    for section in modified_sections:
        heading = section.split("\n")[0]
        req_name = re.sub(r"###\s+MODIFIED:\s+", "", heading).strip()
        # Find "Now:" content
        now_match = re.search(r"Now:\s*(.+?)(?=\n(?:Was:|###)|\Z)", section, re.DOTALL)
        if now_match:
            new_content = now_match.group(1).strip()
            # Find and replace in baseline
            pattern = rf"(###\s+{re.escape(req_name)})\n.*?(?=\n###|\Z)"
            replacement = rf"\1\n{new_content}"
            result = re.sub(pattern, replacement, result, flags=re.DOTALL)
    return result


def merge_removed(baseline_text: str, removed_sections: list[str]) -> str:
    """Remove sections matching REMOVED headings."""
    result = baseline_text
    for section in removed_sections:
        heading = section.split("\n")[0]
        req_name = re.sub(r"###\s+REMOVED:\s+", "", heading).strip()
        pattern = rf"###\s+{re.escape(req_name)}\n.*?(?=\n###|\Z)"
        result = re.sub(pattern, "", result, flags=re.DOTALL)
    # Clean up double blank lines
    result = re.sub(r"\n{3,}", "\n\n", result)
    return result


def merge_spec(delta_path: Path, dry_run: bool = False) -> dict:
    """Merge one delta spec into its baseline. Returns status dict."""
    delta_text = delta_path.read_text(encoding="utf-8")
    spec_name = delta_path.name
    component = spec_name.replace(".md", "").lower()

    sections = parse_delta_sections(delta_text)
    total_changes = sum(len(v) for v in sections.values())

    if total_changes == 0:
        return {"file": spec_name, "status": "skip", "reason": "no delta sections found"}

    baseline_path = find_baseline(spec_name)

    if baseline_path is None:
        # No baseline exists -- promote delta as-is
        if component in COMPONENT_MAP:
            target_dir = COMPONENT_MAP[component]
            target_dir.mkdir(parents=True, exist_ok=True)
            target = target_dir / spec_name
            if not dry_run:
                target.write_text(delta_text, encoding="utf-8")
            return {
                "file": spec_name,
                "status": "promoted",
                "target": str(target),
                "changes": total_changes,
            }
        return {"file": spec_name, "status": "skip", "reason": f"unknown component: {component}"}

    baseline_text = baseline_path.read_text(encoding="utf-8")
    result = baseline_text

    if sections["added"]:
        result = merge_added(result, sections["added"])
    if sections["modified"]:
        result = merge_modified(result, sections["modified"])
    if sections["removed"]:
        result = merge_removed(result, sections["removed"])

    if not dry_run:
        baseline_path.write_text(result, encoding="utf-8")

    return {
        "file": spec_name,
        "status": "merged",
        "target": str(baseline_path),
        "added": len(sections["added"]),
        "modified": len(sections["modified"]),
        "removed": len(sections["removed"]),
    }


def main():
    args = sys.argv[1:]
    dry_run = "--dry-run" in args
    paths = [a for a in args if not a.startswith("--")]

    if not paths:
        print("Usage: python merge_specs.py <change-name> [--dry-run]")
        sys.exit(1)

    change_name = paths[0]
    archive_dir = ARCHIVE_DIR / change_name / "specs"

    if not archive_dir.exists():
        # Also check non-archived changes
        alt_dir = GAIA_ROOT / "changes" / change_name / "specs"
        if alt_dir.exists():
            archive_dir = alt_dir
        else:
            print(f"Change not found: {change_name}")
            print(f"  Checked: {archive_dir}")
            print(f"  Checked: {alt_dir}")
            sys.exit(1)

    spec_files = list(archive_dir.glob("*.md"))
    if not spec_files:
        print(f"No spec files found in {archive_dir}")
        sys.exit(0)

    mode = "[DRY RUN] " if dry_run else ""
    print(f"\n{mode}Merging specs from: {change_name}")
    print("=" * 50)

    for spec_file in spec_files:
        result = merge_spec(spec_file, dry_run=dry_run)
        status = result["status"]
        if status == "merged":
            print(f"  [MERGED] {result['file']} -> {result['target']}")
            print(f"           +{result['added']} added, ~{result['modified']} modified, -{result['removed']} removed")
        elif status == "promoted":
            print(f"  [NEW]    {result['file']} -> {result['target']}")
        elif status == "skip":
            print(f"  [SKIP]   {result['file']}: {result['reason']}")

    print("\nDone.")


if __name__ == "__main__":
    main()
