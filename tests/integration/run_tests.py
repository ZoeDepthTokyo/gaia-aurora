#!/usr/bin/env python
"""
Test runner for GAIA integration tests.

Runs all integration tests and provides summary report.
"""

import subprocess
import sys
from pathlib import Path


def run_integration_tests():
    """Run all integration tests with pytest."""

    # Ensure we're in the right directory
    test_dir = Path(__file__).parent
    gaia_root = test_dir.parent.parent

    print("=" * 70)
    print("GAIA Integration Tests - Phase 2 & 3")
    print("=" * 70)
    print()

    # Run pytest
    cmd = [
        sys.executable,
        "-m",
        "pytest",
        str(test_dir),
        "-v",
        "--tb=short",
        "-ra",  # Show summary of all test results
    ]

    print(f"Running: {' '.join(cmd)}")
    print()

    result = subprocess.run(cmd, cwd=str(gaia_root))

    return result.returncode


def run_with_coverage():
    """Run tests with coverage report."""

    test_dir = Path(__file__).parent
    gaia_root = test_dir.parent.parent

    print("=" * 70)
    print("GAIA Integration Tests - With Coverage")
    print("=" * 70)
    print()

    cmd = [
        sys.executable,
        "-m",
        "pytest",
        str(test_dir),
        "-v",
        "--cov=mental_models",
        "--cov=argus",
        "--cov=mnemis",
        "--cov=loom",
        "--cov-report=term-missing",
        "--cov-report=html",
    ]

    print(f"Running: {' '.join(cmd)}")
    print()

    result = subprocess.run(cmd, cwd=str(gaia_root))

    if result.returncode == 0:
        print()
        print("Coverage report generated in htmlcov/index.html")

    return result.returncode


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--coverage":
        exit_code = run_with_coverage()
    else:
        exit_code = run_integration_tests()

    sys.exit(exit_code)
