"""GAIA Spec Validator -- checks change artifacts for format compliance.

Usage:
    python validate_specs.py changes/<change-name>
    python validate_specs.py changes/<change-name> --strict --json
    python validate_specs.py --all

Exit codes:
    0 = pass (or warnings only)
    1 = warnings found (non-strict mode)
    2 = errors found
"""

import json
import re
import sys
from pathlib import Path

VAGUE_WORDS = {"correctly", "properly", "works", "appropriate", "good", "fine", "right"}
REQUIRED_PROPOSAL_SECTIONS = {"intent", "scope", "out of scope", "success criteria"}
REQUIRED_SPEC_HEADER_FIELDS = {"change", "version", "last updated"}


def validate_change(change_dir: Path) -> dict:
    """Validate a single change directory. Returns {errors, warnings, checks}."""
    results = {"errors": [], "warnings": [], "checks": [], "name": change_dir.name}

    # --- Artifact completeness ---
    proposal = change_dir / "proposal.md"
    specs_dir = change_dir / "specs"
    design = change_dir / "design.md"
    tasks = change_dir / "tasks.md"

    if proposal.exists():
        text = proposal.read_text(encoding="utf-8").lower()
        found = {s for s in REQUIRED_PROPOSAL_SECTIONS if s in text}
        missing = REQUIRED_PROPOSAL_SECTIONS - found
        if missing:
            results["warnings"].append(
                f"proposal.md missing sections: {', '.join(sorted(missing))}"
            )
        results["checks"].append(
            f"proposal.md ({len(found)}/{len(REQUIRED_PROPOSAL_SECTIONS)} sections)"
        )
    else:
        results["errors"].append("proposal.md not found")

    if specs_dir.exists() and specs_dir.is_dir():
        spec_files = list(specs_dir.glob("*.md"))
        if not spec_files:
            results["errors"].append(
                "specs/ directory is empty -- need at least one component spec"
            )
        else:
            results["checks"].append(f"specs/ has {len(spec_files)} component spec(s)")
            for sf in spec_files:
                _validate_spec_file(sf, results)
    else:
        results["errors"].append("specs/ directory not found")

    if design.exists():
        text = design.read_text(encoding="utf-8").lower()
        if "technical approach" in text or "approach" in text:
            results["checks"].append("design.md has Technical Approach")
        else:
            results["warnings"].append("design.md missing 'Technical Approach' section")
    else:
        results["errors"].append("design.md not found")

    if tasks.exists():
        text = tasks.read_text(encoding="utf-8")
        checkboxes = re.findall(r"- \[([ x])\]", text)
        if checkboxes:
            checked = sum(1 for c in checkboxes if c == "x")
            results["checks"].append(f"tasks.md ({len(checkboxes)} items, {checked} checked)")
        else:
            results["warnings"].append("tasks.md has no checkbox items (expected '- [ ] ...')")
    else:
        results["errors"].append("tasks.md not found")

    return results


def _validate_spec_file(path: Path, results: dict):
    """Validate a single spec file for delta format compliance."""
    text = path.read_text(encoding="utf-8")
    fname = path.name

    # Check header fields
    header_lines = text[:500].lower()
    for field in REQUIRED_SPEC_HEADER_FIELDS:
        if f"{field}:" not in header_lines:
            results["warnings"].append(f"{fname}: missing header field '{field}'")

    # Check ADDED requirements have scenarios
    added_blocks = re.findall(r"###\s+ADDED:\s+(.+)", text)
    for req_name in added_blocks:
        pattern = (
            rf"###\s+ADDED:\s+{re.escape(req_name.strip())}"
            r"(.*?)(?=###\s+(?:ADDED|MODIFIED|REMOVED)|\Z)"
        )
        match = re.search(pattern, text, re.DOTALL)
        if match:
            section = match.group(1)
            if "- GIVEN" not in section or "- WHEN" not in section or "- THEN" not in section:
                results["errors"].append(
                    f"{fname}: ADDED '{req_name.strip()}' has no Given-When-Then scenario"
                )

    # Check MODIFIED requirements have Was:/Now:
    modified_blocks = re.findall(r"###\s+MODIFIED:\s+(.+)", text)
    for req_name in modified_blocks:
        pattern = (
            rf"###\s+MODIFIED:\s+{re.escape(req_name.strip())}"
            r"(.*?)(?=###\s+(?:ADDED|MODIFIED|REMOVED)|\Z)"
        )
        match = re.search(pattern, text, re.DOTALL)
        if match:
            section = match.group(1)
            if "Was:" not in section:
                results["errors"].append(
                    f"{fname}: MODIFIED '{req_name.strip()}' missing 'Was:' line"
                )
            if "Now:" not in section:
                results["errors"].append(
                    f"{fname}: MODIFIED '{req_name.strip()}' missing 'Now:' line"
                )

    # Check THEN clauses for vague words
    then_lines = re.findall(r"- THEN\s+(.+)", text)
    for line in then_lines:
        for word in VAGUE_WORDS:
            if word in line.lower().split():
                results["warnings"].append(
                    f"{fname}: THEN uses vague word '{word}': '{line.strip()[:60]}...'"
                )
                break

    # Check for duplicate requirement names
    all_reqs = re.findall(r"###\s+(?:ADDED|MODIFIED|REMOVED):\s+(.+)", text)
    seen = set()
    for r in all_reqs:
        r_clean = r.strip().lower()
        if r_clean in seen:
            results["errors"].append(f"{fname}: duplicate requirement '{r.strip()}'")
        seen.add(r_clean)

    # Check for Windows paths
    if re.search(r"[A-Z]:\\", text):
        results["warnings"].append(f"{fname}: Contains Windows-style paths (use forward slashes)")

    req_count = len(all_reqs)
    scenario_count = len(re.findall(r"####\s+Scenario:", text))
    results["checks"].append(f"{fname}: {req_count} requirements, {scenario_count} scenarios")


def print_report(results: dict, as_json: bool = False):
    """Print validation report."""
    if as_json:
        print(json.dumps(results, indent=2))
        return

    name = results["name"]
    print(f"\nSpec Validation: {name}")
    print("=" * (18 + len(name)))

    if results["checks"]:
        print("\nChecks:")
        for c in results["checks"]:
            print(f"  [OK] {c}")

    if results["warnings"]:
        print("\nWarnings:")
        for w in results["warnings"]:
            print(f"  [WARN] {w}")

    if results["errors"]:
        print("\nErrors:")
        for e in results["errors"]:
            print(f"  [ERR] {e}")

    # Summary
    e = len(results["errors"])
    w = len(results["warnings"])
    if e > 0:
        print(f"\nResult: FAIL ({e} error(s), {w} warning(s))")
    elif w > 0:
        print(f"\nResult: PASS ({w} warning(s))")
    else:
        print("\nResult: PASS")


def main():
    args = sys.argv[1:]
    strict = "--strict" in args
    as_json = "--json" in args
    check_only = "--check-only" in args
    validate_all = "--all" in args

    # Filter flags from args
    paths = [a for a in args if not a.startswith("--")]

    if validate_all:
        changes_dir = Path("changes")
        if not changes_dir.exists():
            print("No changes/ directory found.")
            sys.exit(0)
        paths = [str(d) for d in changes_dir.iterdir() if d.is_dir() and d.name != "archive"]

    if not paths:
        print(
            "Usage: python validate_specs.py changes/<change-name> " "[--strict] [--json] [--all]"
        )
        sys.exit(2)

    all_results = []
    max_severity = 0  # 0=pass, 1=warnings, 2=errors

    for p in paths:
        change_dir = Path(p)
        if not change_dir.exists():
            print(f"Directory not found: {p}")
            max_severity = 2
            continue
        results = validate_change(change_dir)
        all_results.append(results)
        print_report(results, as_json)

        if results["errors"]:
            max_severity = max(max_severity, 2)
        elif results["warnings"]:
            max_severity = max(max_severity, 1)

    if check_only:
        sys.exit(0)

    if strict and max_severity >= 1:
        sys.exit(2)

    sys.exit(min(max_severity, 2))


if __name__ == "__main__":
    main()
