# GECO Implementation: Q8, Q12, Q18

**Date**: 2026-02-09
**Priority**: MEDIUM
**Status**: Complete

---

## Overview

This document describes the implementation of three GECO items:
- **Q8**: VULCAN Phase Planner
- **Q12**: Contract Testing Utilities
- **Q18**: User Interaction Learning

All three are foundational infrastructure for GAIA ecosystem quality and evolution.

---

## Q8: VULCAN Phase Planner

**Objective**: Add phased planning capability to VULCAN for MVP scoping and development roadmaps.

### Implementation

**Files Created**:
- `X:\Projects\_GAIA\_VULCAN\vulcan_forge\phase_planner.py`
- `X:\Projects\_GAIA\_VULCAN\tests\test_phase_planner.py`

**Updated**:
- `X:\Projects\_GAIA\_VULCAN\vulcan_forge\__init__.py` (exports added)

### Features

1. **Phase Classification**: Automatically sorts features into MVP, Enhancement, and Scale phases based on complexity and dependencies
2. **Dependency Validation**: Detects missing and circular dependencies
3. **Success Criteria**: Auto-generates phase-specific success criteria
4. **Markdown Export**: Outputs human-readable phase plans
5. **JSON Export**: Machine-readable format for tooling

### Usage Example

```python
from vulcan_forge import PhasePlanner

planner = PhasePlanner()
plan = planner.create_plan(
    project_name="ABIS",
    features=[
        {
            "name": "node_editor",
            "description": "Visual workflow editor",
            "complexity": "high",
            "dependencies": ["base_ui"]
        },
        {
            "name": "base_ui",
            "description": "Basic UI framework",
            "complexity": "low",
            "dependencies": []
        }
    ],
    constraints={"timeline": "3 months", "team_size": 1}
)

print(plan.to_markdown())
```

### Output

```markdown
# ABIS — Phase Plan

## Constraints
- **Timeline:** 3 months
- **Team Size:** 1

## Phase 1: Foundation & MVP (mvp)
**Effort:** 1-2 weeks

### Features
- [LOW] base_ui: Basic UI framework

### Success Criteria
- [ ] Core functionality works end-to-end
- [ ] Basic test coverage (>60%)
- [ ] CLAUDE.md created
- [ ] Pre-commit hooks active

## Phase 2: Feature Completion (enhancement)
**Effort:** 2-4 weeks

### Features
- [HIGH] node_editor: Visual workflow editor (depends: base_ui)

### Success Criteria
- [ ] All planned features implemented
- [ ] Test coverage >80%
- [ ] CI/CD pipeline active
- [ ] Integration tests passing
```

### Tests

14 tests implemented covering:
- Basic plan creation
- Markdown export
- Feature sorting by complexity
- Empty/invalid feature handling
- Dependency validation
- Large feature sets

**All tests passing** ✓

---

## Q12: Contract Testing Utilities

**Objective**: Document and validate Pydantic models that serve as contracts between GAIA modules.

### Implementation

**Files Created**:
- `X:\Projects\_GAIA\docs\CONTRACT_TESTING.md` (comprehensive documentation)
- `X:\Projects\_GAIA\runtime\contract_validator.py` (validation script)
- `X:\Projects\_GAIA\runtime\tests\test_contract_validator.py` (test suite)

### Key Concepts

**Contract**: A Pydantic model that defines an interface between producer and consumer modules.

**Example**: MYCEL's `Document` model is consumed by VIA and jSeeker. Changes to `Document` must not break consumers.

### Contracts Documented

1. **mycel.Document**
   - Producer: MYCEL
   - Consumers: VIA, jSeeker, DATA FORGE
   - Required fields: `id`, `content`, `created_at`

2. **mycel.Chunk**
   - Producer: MYCEL
   - Consumers: VIA, jSeeker
   - Required fields: `id`, `document_id`, `content`, `start_idx`, `end_idx`
   - Required properties: `chunk_id` (backward compatibility)

3. **mycel.RetrievalResult**
   - Producer: MYCEL
   - Consumers: VIA, jSeeker
   - Required fields: `chunk_id`, `content`, `similarity_score`

### Contract Validator

**Run validation**:
```bash
cd X:\Projects\_GAIA
python runtime\contract_validator.py --verbose
```

**Output**:
```
=== GAIA Contract Validator ===

[OK] mycel.Document: All required fields present
  Consumers: VIA, jSeeker, DATA_FORGE
  ✓ Field 'id' present
  ✓ Field 'content' present
  ✓ Field 'created_at' present

[OK] mycel.Chunk: All required fields present
  Consumers: VIA, jSeeker
  ✓ Property 'chunk_id' present

[OK] mycel.RetrievalResult: All required fields present
  Consumers: VIA, jSeeker

==================================================
Summary: 3 passed, 0 failed, 0 warnings
==================================================
```

### Change Protocol

**Safe Changes** (non-breaking):
- Add optional fields with defaults
- Add new methods/properties
- Expand enum values

**Breaking Changes** (require coordination):
- Remove required fields
- Rename fields
- Change field types

**Migration Path Example**:
```python
# WRONG: Immediate breaking change
class Chunk(BaseModel):
    score: float  # Renamed from similarity_score - BREAKS CONSUMERS

# CORRECT: Deprecation path
class Chunk(BaseModel):
    score: float  # New preferred name

    @property
    def similarity_score(self) -> float:
        """Deprecated: Use 'score' instead."""
        warnings.warn("similarity_score is deprecated", DeprecationWarning)
        return self.score
```

### Tests

17 tests implemented covering:
- Validation result status
- Contract registry structure
- Field validation
- Type checking
- Missing field detection
- Malformed data handling

---

## Q18: User Interaction Learning

**Objective**: Create automated pipeline for learning from user corrections to agent outputs.

### Implementation

**Files Created**:
- `X:\Projects\_GAIA\docs\INTERACTION_LEARNING.md` (comprehensive roadmap)
- `X:\Projects\_GAIA\_ARGUS\correction_tracker.py` (logging module)
- `X:\Projects\_GAIA\_ARGUS\tests\test_correction_tracker.py` (test suite)
- `X:\Projects\_GAIA\_ARGUS\data\corrections\README.md` (data documentation)
- `X:\Projects\_GAIA\_ARGUS\examples\jseeker_integration_example.py` (integration guide)

### Architecture

```
User Correction → ARGUS Logs → MNEMIS Stores → WARDEN Enforces
```

**Phase 1** (This Implementation): ARGUS Correction Logging
**Phase 2** (Future): MNEMIS Pattern Learning
**Phase 3** (Future): WARDEN Pattern Enforcement

### Correction Event Schema

```json
{
  "timestamp": "2026-02-09T14:30:22Z",
  "session_id": "jseeker_20240209_143000",
  "correction_type": "resume_bullet_voice",
  "original": "Responsible for leading team",
  "corrected": "Led 10-person engineering team",
  "context": {
    "project": "jSeeker",
    "operation": "resume_adaptation",
    "model": "claude-sonnet-4.5"
  },
  "user_id": "default",
  "correction_method": "manual_edit"
}
```

### Usage Example

```python
from argus.correction_tracker import log_correction, get_corrections, get_stats

# Log a correction
log_correction(
    type="resume_bullet_voice",
    original="Responsible for leading engineering team",
    corrected="Led 10-person engineering team to deliver 5 product releases",
    context={
        "project": "jSeeker",
        "operation": "resume_adaptation",
        "section": "experience",
        "jd_id": "google_swe_123"
    }
)

# Retrieve corrections
corrections = get_corrections(limit=50, project="jSeeker")

# Get statistics
stats = get_stats()
print(f"Total corrections: {stats['total']}")
print(f"By type: {stats['by_type']}")
```

### Correction Type Taxonomy

**Content Corrections**:
- `factual_error` - Hallucinated information
- `missing_detail` - Output too vague
- `excessive_detail` - Output too verbose

**Style Corrections**:
- `tone_mismatch` - Wrong formality/voice
- `passive_to_active` - Passive → active voice
- `jargon_overuse` - Too much technical jargon
- `formatting` - Structure issues

**Domain-Specific (jSeeker)**:
- `ats_keyword_missing` - Missing required keyword
- `metric_vague` - Lacks concrete metrics
- `experience_inflated` - Exaggerated claims

**Domain-Specific (VIA)**:
- `claim_too_vague` - Claim lacks specificity
- `source_missing` - No attribution
- `claim_unsupported` - Not backed by evidence

### Integration Points

**jSeeker** (`ui/pages/2_new_resume.py`):
```python
# When user edits generated resume
if st.button("Save Edits"):
    for i, (original, edited) in enumerate(diff):
        if original != edited:
            log_correction(
                type=classify_change(original, edited),
                original=original,
                corrected=edited,
                context={"jd_id": jd_id, "section": "experience"}
            )
```

**VIA** (future integration):
```python
# When user rejects extracted claim
if st.button("Reject Claim"):
    log_correction(
        type="claim_rejection",
        original=claim.text,
        corrected=st.text_input("Better version?") or "",
        context={"document_id": doc.id, "confidence": claim.score}
    )
```

### Tests

20 tests implemented covering:
- Event creation and serialization
- Basic logging
- Session ID generation
- Field validation
- Filtering (by type, project, time)
- Statistics generation
- CSV export
- Malformed data handling
- Convenience functions

**All tests passing** ✓

### Example Output

Run the example integration:
```bash
cd X:\Projects\_GAIA\_ARGUS
python examples\jseeker_integration_example.py
```

Output:
```
ARGUS Correction Tracker - jSeeker Integration Example
============================================================
Logging corrections...
  Logged: passive_to_active
  Logged: vague_to_specific
  Logged: added_metrics

✓ Logged 3 corrections for session jseeker_resume_123

=== Correction Statistics ===
Total corrections: 3

By type:
  passive_to_active: 1
  vague_to_specific: 1
  added_metrics: 1

By project:
  jSeeker: 3

=== Recent Corrections (last 3) ===
1. passive_to_active
   Original:  Responsible for leading engineering team of 10 people
   Corrected: Led 10-person engineering team to deliver 5 major pro...

✓ Exported 3 corrections to /tmp/corrections_abc123.csv
  This CSV can be analyzed in Excel, Pandas, or by MNEMIS pattern learner
```

---

## Implementation Roadmap

### Immediate (Complete)
- [x] VULCAN Phase Planner
- [x] Contract Testing Documentation
- [x] Contract Validator Script
- [x] ARGUS Correction Tracker

### Short-Term (2-4 weeks)
- [ ] Integrate correction logging into jSeeker UI
- [ ] Integrate correction logging into VIA UI
- [ ] Collect baseline dataset (100+ corrections)
- [ ] Add contract validator to WARDEN pre-commit hooks

### Medium-Term (4-8 weeks)
- [ ] MNEMIS Pattern Learner (analyze corrections)
- [ ] WARDEN Pattern Validator (enforce patterns)
- [ ] Closed-loop learning (patterns → prompts)
- [ ] ARGUS dashboard for correction trends

### Long-Term (8-12 weeks)
- [ ] Multi-user pattern aggregation
- [ ] Real-time correction suggestions
- [ ] Pattern promotion across projects
- [ ] A/B testing framework

---

## File Locations

### VULCAN Phase Planner
- `X:\Projects\_GAIA\_VULCAN\vulcan_forge\phase_planner.py`
- `X:\Projects\_GAIA\_VULCAN\tests\test_phase_planner.py`

### Contract Testing
- `X:\Projects\_GAIA\docs\CONTRACT_TESTING.md`
- `X:\Projects\_GAIA\runtime\contract_validator.py`
- `X:\Projects\_GAIA\runtime\tests\test_contract_validator.py`

### Interaction Learning
- `X:\Projects\_GAIA\docs\INTERACTION_LEARNING.md`
- `X:\Projects\_GAIA\_ARGUS\correction_tracker.py`
- `X:\Projects\_GAIA\_ARGUS\tests\test_correction_tracker.py`
- `X:\Projects\_GAIA\_ARGUS\data\corrections\README.md`
- `X:\Projects\_GAIA\_ARGUS\examples\jseeker_integration_example.py`

---

## Verification

### Run All Tests

```bash
# VULCAN Phase Planner
cd X:\Projects\_GAIA\_VULCAN
python -m pytest tests/test_phase_planner.py -v

# Contract Validator
cd X:\Projects\_GAIA
python -m pytest runtime/tests/test_contract_validator.py -v

# Correction Tracker
cd X:\Projects\_GAIA\_ARGUS
python -m pytest tests/test_correction_tracker.py -v
```

### Run Validators

```bash
# Contract validation
cd X:\Projects\_GAIA
python runtime/contract_validator.py --verbose

# Example correction tracking
cd X:\Projects\_GAIA\_ARGUS
python examples/jseeker_integration_example.py
```

---

## Impact Assessment

### VULCAN Phase Planner
**Impact**: MEDIUM
- Improves project planning quality
- Reduces manual effort in scoping MVPs
- Provides structured roadmaps for new projects

### Contract Testing
**Impact**: HIGH
- Prevents breaking changes across modules
- Documents critical interfaces
- Enables safe refactoring

### Interaction Learning
**Impact**: HIGH (long-term)
- Automates improvement of LLM outputs
- Reduces manual prompt engineering
- Creates feedback loop for quality improvement

---

## Next Steps

1. **Integrate correction logging into jSeeker** (Week 1-2)
   - Add logging to resume editor
   - Collect 100+ corrections
   - Analyze patterns manually

2. **Add contract validator to CI/CD** (Week 2)
   - Run validator in WARDEN pre-commit hook
   - Alert on contract violations

3. **Build MNEMIS pattern learner** (Week 3-6)
   - Analyze correction frequency
   - Extract top patterns
   - Create pattern YAML format

4. **Close the learning loop** (Week 7-12)
   - WARDEN validates against patterns
   - Patterns update prompts automatically
   - A/B test pattern effectiveness

---

## References

- GECO Architecture: `X:\Projects\_GAIA\docs\GECO_ARCHITECTURE.md`
- GAIA Bible: `X:\Projects\_GAIA\GAIA_BIBLE.md`
- Logging Standard: `X:\Projects\_GAIA\docs\LOGGING_STANDARD.md`
