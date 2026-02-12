# Mental Model Library

> **Context**: Read `GAIA_MANIFEST.md` first for ecosystem state.
> This library is part of the GAIA ecosystem under ARGUS.

## Role
Structured analytical framework library providing 59 mental models across 7 categories for consistent, auditable reasoning. Used by ARGUS Process Observer for context-aware model suggestion and pattern detection.

**Current Version:** 1.0.0

## Quick Start
```python
from mental_models.selector import MentalModelSelector
selector = MentalModelSelector()
models = selector.select_for_context({"domain": "strategy", "complexity": "high"})
```

## Directory Structure
```
mental_models/
├── __init__.py             # Package init
├── models.py               # 59 model definitions + ModelCategory enum
├── selector.py             # MentalModelSelector class
├── registry.json           # JSON schema (59 models, 12 context patterns)
├── invocation_rules.json   # Context matching rules
└── README.md               # Full documentation
```

## Tech Stack
- Pure Python (stdlib only, zero external dependencies)
- JSON-based model registry
- Enum-based categorization (ModelCategory)

## Integration Points
- **ARGUS**: Process Observer uses selector for context-aware suggestions
- **Registry**: Listed in `X:/Projects/_GAIA/registry.json`

## Key Files
- `models.py` — 59 model definitions with categories
- `selector.py` — `MentalModelSelector.select_for_context()` API
- `registry.json` — Machine-readable model definitions
- `invocation_rules.json` — 12 context matching patterns

## Testing
```bash
cd X:/Projects/_GAIA/_ARGUS
pytest tests/test_mental_models.py
```

## When I Change
<!-- CASCADE_MAP: machine-readable, do not edit manually -->
- registry.json: version field → auto
- GAIA_MANIFEST.md: component table row → auto
- GECO_REVIEW_MATRIX.md: component row → auto
- _ARGUS/CLAUDE.md: update if model API changed → ask
<!-- END_CASCADE_MAP -->

## DO NOT
- Add models without updating both `models.py` and `registry.json`
- Remove models that ARGUS Process Observer references
