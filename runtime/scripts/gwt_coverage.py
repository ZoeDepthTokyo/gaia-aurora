"""GWT Coverage Tracker -- cross-references spec scenarios with test files.

Usage:
    python gwt_coverage.py [--json]

Scans:
- _*/specs/core-behaviors.md for GWT scenarios (### Scenario: lines)
- _*/CLAUDE.md for #### Scenario: lines in Testing sections
- _*/tests/test_spec_*.py for test functions

Reports coverage as: tested_scenarios / total_scenarios
"""

import json
import re
import sys
from pathlib import Path

GAIA_ROOT = Path(__file__).resolve().parents[2]
COMPONENTS = [
    "ARGUS",
    "AURORA",
    "LOOM",
    "MNEMIS",
    "MYCEL",
    "VULCAN",
    "WARDEN",
    "RAVEN",
    "ABIS",
]


def count_spec_scenarios(component: str) -> list[str]:
    """Count GWT scenarios in spec files and CLAUDE.md.

    Args:
        component: Component name (e.g. "ARGUS")

    Returns:
        List of scenario names found in spec files and CLAUDE.md
    """
    scenarios = []
    comp_dir = GAIA_ROOT / f"_{component}"

    # Check specs/core-behaviors.md
    spec_file = comp_dir / "specs" / "core-behaviors.md"
    if spec_file.exists():
        text = spec_file.read_text(encoding="utf-8")
        for match in re.finditer(r"###?\s+Scenario:\s+(.+)", text):
            scenarios.append(match.group(1).strip())

    # Check CLAUDE.md testing section
    claude_md = comp_dir / "CLAUDE.md"
    if claude_md.exists():
        text = claude_md.read_text(encoding="utf-8")
        # Only count scenarios after "## Testing Specifications"
        testing_section = text.split("## Testing Specifications")
        if len(testing_section) > 1:
            for match in re.finditer(r"####?\s+Scenario:\s+(.+)", testing_section[1]):
                scenarios.append(match.group(1).strip())

    return scenarios


def count_test_functions(component: str) -> list[str]:
    """Count test functions in spec test files.

    Args:
        component: Component name (e.g. "ARGUS")

    Returns:
        List of test function names found in spec test files
    """
    tests = []
    comp_dir = GAIA_ROOT / f"_{component}"

    for test_file in comp_dir.glob("tests/test_spec_*.py"):
        text = test_file.read_text(encoding="utf-8")
        for match in re.finditer(r"def (test_\w+)", text):
            tests.append(match.group(1))

    # Also check test_creative_direction.py for AURORA
    for test_file in comp_dir.glob("tests/test_creative_direction.py"):
        text = test_file.read_text(encoding="utf-8")
        for match in re.finditer(r"def (test_\w+)", text):
            tests.append(match.group(1))

    return tests


def generate_report(as_json: bool = False) -> dict:
    """Generate GWT coverage report.

    Args:
        as_json: If True, format output as JSON (unused in this function,
                 kept for API compatibility)

    Returns:
        Report dict with per-component stats and overall coverage percentage
    """
    report: dict = {"components": {}, "total_scenarios": 0, "total_tests": 0}

    for comp in COMPONENTS:
        scenarios = count_spec_scenarios(comp)
        tests = count_test_functions(comp)
        coverage = min(len(tests), len(scenarios)) / max(len(scenarios), 1) * 100

        report["components"][comp] = {
            "scenarios": len(scenarios),
            "tests": len(tests),
            "coverage_pct": round(coverage, 1),
            "scenario_names": scenarios,
            "test_names": tests,
        }
        report["total_scenarios"] += len(scenarios)
        report["total_tests"] += len(tests)

    report["overall_coverage_pct"] = round(
        min(report["total_tests"], report["total_scenarios"])
        / max(report["total_scenarios"], 1)
        * 100,
        1,
    )
    return report


def main() -> None:
    """Entry point for CLI usage."""
    as_json = "--json" in sys.argv
    report = generate_report(as_json)

    if as_json:
        print(json.dumps(report, indent=2))
        return

    print("\nGWT Scenario Coverage Report")
    print("=" * 60)

    for comp, data in report["components"].items():
        if data["scenarios"] > 0 or data["tests"] > 0:
            bar = "#" * int(data["coverage_pct"] / 5) + "-" * (20 - int(data["coverage_pct"] / 5))
            print(
                f"  {comp:10s} [{bar}] {data['coverage_pct']:5.1f}%"
                f"  ({data['tests']}/{data['scenarios']} scenarios)"
            )

    print(
        f"\n  TOTAL: {report['overall_coverage_pct']}%"
        f" ({report['total_tests']}/{report['total_scenarios']} scenarios)"
    )
    print()


if __name__ == "__main__":
    main()
