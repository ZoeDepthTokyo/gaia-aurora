"""Tests for GWT coverage tracker."""
import sys
from pathlib import Path

# Add parent to path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from gwt_coverage import count_spec_scenarios, count_test_functions, generate_report


def test_count_spec_scenarios_known_component():
    """ARGUS should have spec scenarios."""
    scenarios = count_spec_scenarios("ARGUS")
    assert len(scenarios) > 0, "ARGUS should have GWT scenarios"


def test_count_spec_scenarios_unknown_component():
    """Unknown component returns empty list."""
    scenarios = count_spec_scenarios("NONEXISTENT")
    assert scenarios == []


def test_count_test_functions():
    """Should find test functions in test files."""
    # This will find tests we just created
    tests = count_test_functions("ARGUS")
    assert isinstance(tests, list)


def test_generate_report_structure():
    """Report has required fields."""
    report = generate_report()
    assert "components" in report
    assert "total_scenarios" in report
    assert "total_tests" in report
    assert "overall_coverage_pct" in report
    assert len(report["components"]) == 9


def test_report_component_fields():
    """Each component entry has required fields."""
    report = generate_report()
    for comp, data in report["components"].items():
        assert "scenarios" in data
        assert "tests" in data
        assert "coverage_pct" in data
