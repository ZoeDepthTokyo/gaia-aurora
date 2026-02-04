#!/usr/bin/env python
"""
Validate that all imports required by integration tests can be resolved.

Run this before executing tests to ensure all dependencies are available.
"""

import sys
from pathlib import Path

# Add GAIA root to path
gaia_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(gaia_root))

print("=" * 70)
print("Validating Integration Test Imports")
print("=" * 70)
print()

errors = []
warnings = []

# Test Mental Models imports
print("Checking Mental Models...")
try:
    from mental_models.selector import MentalModelSelector, SelectionResult
    from mental_models.models import (
        MentalModel,
        ModelCategory,
        ContextPattern,
        ModelInvocation
    )
    print("  ✓ Mental Models imports OK")
except ImportError as e:
    errors.append(f"Mental Models: {e}")
    print(f"  ✗ Mental Models import failed: {e}")

# Test ARGUS Subconscious imports
print("Checking ARGUS Subconscious...")
try:
    from argus.subconscious.memory import (
        ExternalMemory,
        MemoryEntry,
        MemoryType,
        MemoryScope
    )
    print("  ✓ ARGUS Memory imports OK")
except ImportError as e:
    errors.append(f"ARGUS Memory: {e}")
    print(f"  ✗ ARGUS Memory import failed: {e}")

try:
    from argus.subconscious.pattern_detector import (
        PatternDetector,
        DetectedPattern,
        PatternType
    )
    print("  ✓ ARGUS Pattern Detector imports OK")
except ImportError as e:
    errors.append(f"ARGUS Pattern Detector: {e}")
    print(f"  ✗ ARGUS Pattern Detector import failed: {e}")

try:
    from argus.subconscious.hypothesis_generator import (
        HypothesisGenerator,
        Hypothesis,
        HypothesisType
    )
    print("  ✓ ARGUS Hypothesis Generator imports OK")
except ImportError as e:
    errors.append(f"ARGUS Hypothesis Generator: {e}")
    print(f"  ✗ ARGUS Hypothesis Generator import failed: {e}")

# Test ARGUS Explainability imports
print("Checking ARGUS Explainability...")
try:
    from argus.explainability.explainer import (
        Explainer,
        Explanation,
        ExplanationLevel
    )
    print("  ✓ ARGUS Explainer imports OK")
except ImportError as e:
    errors.append(f"ARGUS Explainer: {e}")
    print(f"  ✗ ARGUS Explainer import failed: {e}")

# Test MNEMIS imports
print("Checking MNEMIS...")
try:
    from mnemis.core.memory_store import MnemisStore
    from mnemis.core.contracts import MemoryAccessController
    from mnemis.core.promotion import MemoryPromotionEngine
    from mnemis.models.memory_models import (
        MemoryEntry,
        MemoryContract,
        MemoryScope,
        MemoryAccessLevel,
        MemoryAccessViolation,
        MemoryPromotionProposal,
    )
    print("  ✓ MNEMIS imports OK")
except ImportError as e:
    errors.append(f"MNEMIS: {e}")
    print(f"  ✗ MNEMIS import failed: {e}")

# Test LOOM imports
print("Checking LOOM...")
try:
    from loom.core.workflow_engine import WorkflowEngine
    from loom.models.agent_models import (
        AgentWorkflow,
        AgentNode,
        AgentExecutionState,
        AgentConnection,
        GovernanceRule,
    )
    print("  ✓ LOOM imports OK")
except ImportError as e:
    errors.append(f"LOOM: {e}")
    print(f"  ✗ LOOM import failed: {e}")

# Test pytest
print("Checking pytest...")
try:
    import pytest
    print(f"  ✓ pytest {pytest.__version__} installed")
except ImportError:
    errors.append("pytest not installed")
    print("  ✗ pytest not installed (run: pip install pytest)")

# Check optional dependencies
print("Checking optional dependencies...")
try:
    import pytest_cov
    print(f"  ✓ pytest-cov installed")
except ImportError:
    warnings.append("pytest-cov not installed (coverage reports unavailable)")
    print("  ⚠ pytest-cov not installed (optional, for coverage)")

print()
print("=" * 70)

if errors:
    print("❌ VALIDATION FAILED")
    print()
    print("Errors:")
    for error in errors:
        print(f"  - {error}")
    print()
    print("Fix these errors before running integration tests.")
    sys.exit(1)
else:
    print("✅ VALIDATION PASSED")
    print()
    if warnings:
        print("Warnings:")
        for warning in warnings:
            print(f"  - {warning}")
        print()
    print("All required imports available. Ready to run integration tests!")
    print()
    print("Run tests with:")
    print("  python -m pytest tests/integration/ -v")
    sys.exit(0)
