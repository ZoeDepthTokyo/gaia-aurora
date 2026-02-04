# Integration Tests Quick Start

Fast track to running GAIA Phase 2 & 3 integration tests.

## 1. Validate Setup (30 seconds)

```bash
cd X:/Projects/_gaia/tests/integration
python validate_imports.py
```

**Expected**: ✅ VALIDATION PASSED

If you see errors, install missing dependencies:
```bash
pip install pytest pytest-cov
```

## 2. Run All Tests (2-3 minutes)

```bash
cd X:/Projects/_gaia
python -m pytest tests/integration/ -v
```

**Expected**: ~50+ tests passing

## 3. Run Individual Test Suites

### Mental Models (Phase 2)
```bash
python -m pytest tests/integration/test_mental_models_integration.py -v
```
Tests: Mental model selection, invocation rules, real-world scenarios

### ARGUS Subconscious (Phase 2)
```bash
python -m pytest tests/integration/test_argus_subconscious.py -v
```
Tests: Pattern detection, hypothesis generation, explainability

### MNEMIS + LOOM (Phase 3)
```bash
python -m pytest tests/integration/test_mnemis_loom_integration.py -v
```
Tests: Memory contracts, promotion workflow, workflow execution

## 4. Generate Coverage Report

```bash
cd X:/Projects/_gaia/tests/integration
python run_tests.py --coverage
```

Opens coverage report in `htmlcov/index.html`

## What Each Test Suite Covers

### test_mental_models_integration.py (521 lines)
- ✅ Context-aware model selection
- ✅ Pattern matching and invocation rules
- ✅ Confidence threshold filtering
- ✅ Graceful degradation
- ✅ Real scenarios (HART OS, cost optimization)

### test_argus_subconscious.py (643 lines)
- ✅ Pattern detection from memory
- ✅ Hypothesis generation (non-intervening)
- ✅ 4-level explanations (SIMPLE/DEFAULT/METAPHOR/ADVANCED)
- ✅ Growth ladder mapping
- ✅ End-to-end observation workflow

### test_mnemis_loom_integration.py (858 lines)
- ✅ Memory access contracts (read down, write exact)
- ✅ Cross-project isolation
- ✅ Memory promotion (AGENT → PROJECT → GAIA)
- ✅ Human approval requirements
- ✅ Workflow governance enforcement
- ✅ Ephemeral memory cleanup

## Constitutional Boundaries Verified

Every test validates:
1. **No Autonomous Actions** - All changes require approval
2. **Transparency** - All decisions have rationale
3. **Graceful Degradation** - Errors handled cleanly
4. **Auditability** - Full provenance tracking

## Common Issues

### "No module named 'mental_models'"
```bash
# Run from GAIA root:
cd X:/Projects/_gaia
python -m pytest tests/integration/ -v
```

### "No module named 'pytest'"
```bash
pip install pytest
```

### Tests fail with "database locked"
- Tests use temporary databases
- Should clean up automatically
- If issues persist, check disk space

## Quick Test Examples

### Test specific functionality:
```bash
# Mental model for performance issues
python -m pytest tests/integration/test_mental_models_integration.py::TestMentalModelSelection::test_performance_degradation_context -v

# Pattern detection
python -m pytest tests/integration/test_argus_subconscious.py::TestPatternDetectionWithMemory::test_recurring_error_detection -v

# Memory contracts
python -m pytest tests/integration/test_mnemis_loom_integration.py::TestMemoryContractsEnforcement::test_agent_cannot_read_up_hierarchy -v
```

## Success Indicators

✅ All tests pass
✅ No constitutional violations detected
✅ Coverage > 75% for all components
✅ Zero autonomous actions executed
✅ All hypotheses require human review
✅ All memory promotions require approval

## Next Steps After Tests Pass

1. Review coverage report for gaps
2. Add project-specific test scenarios
3. Integrate with CI/CD pipeline
4. Document any custom test requirements

## Files Overview

- `validate_imports.py` - Check dependencies
- `run_tests.py` - Test runner with coverage
- `test_mental_models_integration.py` - Phase 2 mental models
- `test_argus_subconscious.py` - Phase 2 ARGUS
- `test_mnemis_loom_integration.py` - Phase 3 MNEMIS/LOOM
- `README.md` - Detailed documentation
- `QUICKSTART.md` - This file

## Need Help?

See `README.md` for detailed documentation and troubleshooting.

**Time to First Test Results**: < 5 minutes
**Total Test Count**: 50+ integration tests
**Coverage**: Phase 2 + Phase 3 components
