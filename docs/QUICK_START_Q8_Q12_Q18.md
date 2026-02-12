# Quick Start: Q8, Q12, Q18

Fast reference for using the new GECO implementations.

---

## Q8: VULCAN Phase Planner

### Basic Usage

```python
from vulcan_forge import PhasePlanner

planner = PhasePlanner()
plan = planner.create_plan(
    project_name="MyProject",
    features=[
        {
            "name": "user_auth",
            "description": "User authentication",
            "complexity": "low",
            "dependencies": []
        },
        {
            "name": "dashboard",
            "description": "Main dashboard",
            "complexity": "medium",
            "dependencies": ["user_auth"]
        }
    ],
    constraints={"timeline": "2 months", "team_size": "1"}
)

# Export as markdown
print(plan.to_markdown())

# Export as JSON
import json
print(json.dumps(plan.to_dict(), indent=2))
```

### Complexity Levels
- `"low"` → MVP phase
- `"medium"` → Enhancement phase
- `"high"` → Scale phase

### Validate Dependencies

```python
from vulcan_forge import Feature

features = [
    Feature("base", "Base feature", "low"),
    Feature("addon", "Add-on", "medium", dependencies=["base"])
]

errors = planner.validate_dependencies(features)
if errors:
    print("Dependency errors:", errors)
```

---

## Q12: Contract Testing

### Run Validator

```bash
cd X:\Projects\_GAIA
python runtime\contract_validator.py --verbose
```

### Check Specific Contract

```python
from runtime.contract_validator import ContractValidator, CONTRACTS

validator = ContractValidator(verbose=True)

# Validate MYCEL Document contract
spec = CONTRACTS["mycel.Document"]
result = validator.validate_contract("mycel.Document", spec)

if result.passed:
    print("✓ Contract valid")
else:
    print("✗ Contract broken:")
    for error in result.errors:
        print(f"  - {error}")
```

### Add New Contract

Edit `runtime/contract_validator.py`:

```python
CONTRACTS["myproject.MyModel"] = {
    "producer": "MyProject",
    "module_path": "myproject.models",
    "class_name": "MyModel",
    "consumers": ["ConsumerA", "ConsumerB"],
    "required_fields": ["id", "name"],
    "field_types": {
        "id": str,
        "name": str,
    }
}
```

---

## Q18: Interaction Learning

### Log a Correction

```python
from argus.correction_tracker import log_correction

log_correction(
    type="resume_bullet_voice",
    original="Responsible for leading team",
    corrected="Led 10-person engineering team",
    context={
        "project": "jSeeker",
        "operation": "resume_adaptation",
        "section": "experience"
    }
)
```

### Get Recent Corrections

```python
from argus.correction_tracker import get_corrections

# Get last 20 corrections
corrections = get_corrections(limit=20)

for corr in corrections:
    print(f"{corr.correction_type}: {corr.original[:50]}...")
```

### Filter Corrections

```python
# Get jSeeker corrections only
jseeker_corrections = get_corrections(
    limit=50,
    project="jSeeker",
    correction_type="resume_bullet_voice"
)

# Get corrections after specific date
recent = get_corrections(after="2026-02-09T00:00:00Z")
```

### Get Statistics

```python
from argus.correction_tracker import get_stats

stats = get_stats()
print(f"Total corrections: {stats['total']}")
print(f"By type: {stats['by_type']}")
print(f"By project: {stats['by_project']}")
```

### Export for Analysis

```python
from argus.correction_tracker import CorrectionTracker

tracker = CorrectionTracker()
count = tracker.export_to_csv("corrections_export.csv")
print(f"Exported {count} corrections")
```

---

## Integration Examples

### jSeeker Resume Editor

```python
import streamlit as st
from argus.correction_tracker import log_correction

# After user edits resume
if st.button("Save Edits"):
    for i, (original, edited) in enumerate(zip(original_bullets, edited_bullets)):
        if original != edited:
            log_correction(
                type="resume_bullet_edit",  # Or classify automatically
                original=original,
                corrected=edited,
                context={
                    "project": "jSeeker",
                    "jd_id": st.session_state.jd_id,
                    "section": "experience",
                    "bullet_index": i
                }
            )
```

### VIA Claim Review

```python
import streamlit as st
from argus.correction_tracker import log_correction

# When user rejects claim
if st.button("Reject Claim"):
    corrected = st.text_input("Provide better version (optional)")
    log_correction(
        type="claim_rejection",
        original=claim.text,
        corrected=corrected or "[REJECTED]",
        context={
            "project": "VIA",
            "document_id": doc.id,
            "confidence": claim.confidence_score
        }
    )
```

---

## Correction Type Reference

### Content
- `factual_error` - Hallucinated info
- `missing_detail` - Too vague
- `excessive_detail` - Too verbose

### Style
- `tone_mismatch` - Wrong formality
- `passive_to_active` - Voice correction
- `jargon_overuse` - Too technical
- `formatting` - Structure issues

### jSeeker-Specific
- `ats_keyword_missing` - Missing keyword
- `metric_vague` - No concrete numbers
- `experience_inflated` - Exaggerated claims

### VIA-Specific
- `claim_too_vague` - Lacks specificity
- `source_missing` - No attribution
- `claim_unsupported` - Not backed by evidence

---

## File Locations

### Phase Planner
- Code: `X:\Projects\_GAIA\_VULCAN\vulcan_forge\phase_planner.py`
- Tests: `X:\Projects\_GAIA\_VULCAN\tests\test_phase_planner.py`

### Contract Testing
- Docs: `X:\Projects\_GAIA\docs\CONTRACT_TESTING.md`
- Validator: `X:\Projects\_GAIA\runtime\contract_validator.py`
- Tests: `X:\Projects\_GAIA\runtime\tests\test_contract_validator.py`

### Correction Tracker
- Code: `X:\Projects\_GAIA\_ARGUS\correction_tracker.py`
- Tests: `X:\Projects\_GAIA\_ARGUS\tests\test_correction_tracker.py`
- Example: `X:\Projects\_GAIA\_ARGUS\examples\jseeker_integration_example.py`
- Data: `X:\Projects\_GAIA\_ARGUS\data\corrections\corrections.jsonl`

---

## Testing

```bash
# Test phase planner
cd X:\Projects\_GAIA\_VULCAN
python -m pytest tests/test_phase_planner.py -v

# Test contract validator
cd X:\Projects\_GAIA
python -m pytest runtime/tests/test_contract_validator.py -v

# Test correction tracker
cd X:\Projects\_GAIA\_ARGUS
python -m pytest tests/test_correction_tracker.py -v
```

---

## Troubleshooting

### Phase Planner

**Problem**: "Features list cannot be empty"
**Solution**: Ensure `features` parameter has at least one feature dict

**Problem**: "Feature must have a 'name' field"
**Solution**: All feature dicts must have `"name"` key

### Contract Validator

**Problem**: "Failed to import mycel.rag_intelligence.core.models"
**Solution**: Ensure MYCEL is in Python path or run from GAIA root

**Problem**: Contract shows as FAIL
**Solution**: Check if producer model was updated without updating consumers

### Correction Tracker

**Problem**: "correction_type is required"
**Solution**: Always provide `type` parameter when logging

**Problem**: "No corrections found"
**Solution**: Check if corrections.jsonl exists in `X:\Projects\_GAIA\_ARGUS\data\corrections\`

---

## Best Practices

### Phase Planner
1. Start with low-complexity features in MVP
2. Use descriptive feature names
3. Document dependencies explicitly
4. Review generated success criteria

### Contract Testing
1. Run validator before pushing breaking changes
2. Use deprecation paths for field renames
3. Update contract registry when adding contracts
4. Document breaking changes in CHANGELOG

### Correction Tracker
1. Log corrections immediately after user edit
2. Provide rich context (project, operation, model)
3. Use consistent correction types (see taxonomy)
4. Review statistics weekly to identify patterns
5. Export to CSV for deeper analysis

---

## Next Steps

1. **Integrate correction tracking** into jSeeker and VIA UIs
2. **Add contract validator** to WARDEN pre-commit hooks
3. **Use phase planner** for new project roadmaps
4. **Analyze corrections** to identify top 5 patterns
5. **Build MNEMIS pattern learner** (Phase 2)

---

**See also**:
- Full Documentation: `GECO_Q8_Q12_Q18_IMPLEMENTATION.md`
- Verification: `GECO_Q8_Q12_Q18_VERIFICATION.md`
- Contract Details: `CONTRACT_TESTING.md`
- Learning Roadmap: `INTERACTION_LEARNING.md`
