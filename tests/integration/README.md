# GAIA Integration Tests

Integration tests for Phase 2 (ARGUS) and Phase 3 (MNEMIS/LOOM) implementations.

## Test Files

### 1. test_mental_models_integration.py

Tests for Mental Models Library (Phase 2):

- **TestMentalModelSelection**: Context-aware model selection
  - Performance degradation scenarios
  - Error handling contexts
  - Decision-making scenarios
  - Confidence threshold filtering
  - Max models limit enforcement

- **TestInvocationRules**: Pattern matching and combinations
  - Context pattern triggers
  - Combination pattern retrieval
  - Keyword extraction
  - Category filtering

- **TestModelRetrieval**: Individual model access
  - Get model by ID
  - Validate model metadata
  - List all available models

- **TestConstitutionalBoundaries**: Graceful degradation
  - Empty context handling
  - Unknown model IDs
  - Rationale transparency
  - Confidence scoring validity

- **TestRealWorldScenarios**: GAIA use cases
  - HART OS confidence decline
  - Cost optimization
  - Agent trust building

### 2. test_argus_subconscious.py

Tests for ARGUS Subconscious Layer (Phase 2):

- **TestPatternDetectionWithMemory**: Pattern detection integration
  - Recurring error detection
  - Performance degradation trends
  - Pattern evidence tracking
  - Non-intervening behavior

- **TestHypothesisGeneration**: Hypothesis workflow
  - Hypothesis from error patterns
  - Storage in external memory
  - No autonomous actions (constitutional boundary)

- **TestExplainabilityIntegration**: Multi-level explanations
  - SIMPLE level (new users)
  - DEFAULT level (intermediate)
  - METAPHOR level (analogies)
  - ADVANCED level (technical)
  - Growth rung mapping
  - Markdown formatting

- **TestSubconsciousWorkflow**: End-to-end workflow
  - Observation → Pattern → Hypothesis → Explanation
  - Graceful degradation
  - Transparency in uncertainty

### 3. test_mnemis_loom_integration.py

Tests for MNEMIS and LOOM (Phase 3):

- **TestMemoryContractsEnforcement**: Access control
  - Read own memory
  - Read down hierarchy
  - Cannot read up hierarchy
  - Write only exact level
  - Cross-project isolation
  - Provenance tracking

- **TestMemoryPromotionWorkflow**: Memory tier promotion
  - AGENT → PROJECT promotion
  - PROJECT → GAIA promotion
  - Rejection workflow
  - Invalid path blocking
  - Promotion queue visibility

- **TestLoomMemoryAccess**: Workflow + memory integration
  - Workflow agent reads memory
  - Governance enforcement
  - No autonomous promotion
  - Graceful error degradation

- **TestEphemeralMemoryCleanup**: Auto-expiration
  - Agent memory expires
  - Project memory persists

## Running Tests

### Run all integration tests:
```bash
cd X:/Projects/_gaia
python -m pytest tests/integration/ -v
```

### Run specific test file:
```bash
python -m pytest tests/integration/test_mental_models_integration.py -v
python -m pytest tests/integration/test_argus_subconscious.py -v
python -m pytest tests/integration/test_mnemis_loom_integration.py -v
```

### Run specific test class:
```bash
python -m pytest tests/integration/test_mental_models_integration.py::TestMentalModelSelection -v
```

### Run specific test method:
```bash
python -m pytest tests/integration/test_mental_models_integration.py::TestMentalModelSelection::test_performance_degradation_context -v
```

### Run with coverage:
```bash
python -m pytest tests/integration/ --cov=mental_models --cov=argus --cov=mnemis --cov=loom -v
```

### Run with detailed output:
```bash
python -m pytest tests/integration/ -v --tb=long
```

## Test Requirements

Tests use mocked external dependencies:
- SQLite (for ExternalMemory) - uses temporary files
- No actual ChromaDB required (not yet implemented)
- All file operations use temporary directories

### Required packages:
```
pytest>=7.0.0
pytest-cov>=4.0.0  # For coverage reports
```

## Constitutional Boundaries Tested

All tests verify constitutional principles:

1. **No Autonomous Actions**
   - Hypotheses require human review
   - Memory promotion requires approval
   - Governance rules enforced

2. **Transparency**
   - All decisions have rationale
   - Confidence scores explicit
   - Provenance tracked

3. **Graceful Degradation**
   - Empty/invalid inputs handled
   - Unknown IDs return None (not crash)
   - Low confidence clearly marked

4. **Auditability**
   - Memory provenance tracked
   - Pattern evidence preserved
   - Workflow execution recorded

## Expected Results

All tests should pass with:
- No constitutional violations
- No autonomous actions
- Transparent error messages
- Graceful failure modes

## Troubleshooting

### Import Errors

If you see import errors, ensure PYTHONPATH includes GAIA root:

```bash
export PYTHONPATH="X:/Projects/_gaia:$PYTHONPATH"
```

Or run from GAIA root:
```bash
cd X:/Projects/_gaia
python -m pytest tests/integration/ -v
```

### File Not Found Errors

Tests create temporary databases. If you see persistence issues:
- Check write permissions on temp directory
- Ensure sufficient disk space

### Missing Dependencies

If components are missing:
```bash
# Check mental_models
ls X:/Projects/_gaia/mental_models/

# Check argus
ls X:/Projects/_gaia/argus/

# Check mnemis
ls X:/Projects/_gaia/mnemis/

# Check loom
ls X:/Projects/_gaia/loom/
```

## Contributing

When adding new integration tests:

1. Follow existing test structure
2. Use descriptive docstrings
3. Test constitutional boundaries
4. Include both success and failure cases
5. Use temporary files/directories
6. Clean up resources in fixtures

## Coverage Goals

Target coverage for integration tests:
- Mental Models: 80%+ of selector.py
- ARGUS Subconscious: 75%+ of memory.py, pattern_detector.py, explainer.py
- MNEMIS: 80%+ of contracts.py, memory_store.py, promotion.py
- LOOM: 75%+ of workflow_engine.py

Unit tests provide additional coverage for edge cases.
