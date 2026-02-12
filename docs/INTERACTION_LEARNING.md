# User Interaction Learning in GAIA

**Owner**: ARGUS + MNEMIS + WARDEN
**Updated**: 2026-02-09
**Status**: Proposed

---

## Overview

GAIA currently learns from user interactions **manually** through:
- `MEMORY.md` - Documented preferences and patterns
- `patterns.md` - Code patterns and anti-patterns
- `.claude/CLAUDE.md` - Project-specific instructions

**Goal**: Automate this learning loop so GAIA agents improve from user corrections without manual documentation.

---

## Current State (Manual Learning)

### Example 1: Resume Adaptation in jSeeker
**Scenario**: User corrects Claude's resume bullet from passive to active voice.

**Current Flow**:
1. User edits: "Responsible for leading..." → "Led 10-person team..."
2. Developer notices pattern
3. Developer updates `data/prompts/adaptation_prompt.txt` manually
4. Pattern is now enforced

**Problem**: Requires manual observation and intervention. No automatic pattern capture.

---

### Example 2: VIA Claim Extraction
**Scenario**: Claude extracts "Company has good product" as a claim. User marks it as too vague.

**Current Flow**:
1. User rejects claim via UI
2. No correction data is stored
3. Same mistake repeats next time

**Problem**: No feedback loop. Claude doesn't learn from rejections.

---

## Proposed Automated Pipeline

```
User Correction → ARGUS Logs → MNEMIS Stores → WARDEN Enforces
```

### 1. ARGUS: Correction Tracker
**Location**: `X:\Projects\_GAIA\_ARGUS\correction_tracker.py`

**Responsibilities**:
- Log user corrections in real-time
- Categorize correction types (style, accuracy, format, etc.)
- Store in JSONL for analysis

**API**:
```python
from argus.correction_tracker import log_correction

log_correction(
    type="resume_bullet_voice",
    original="Responsible for leading engineering team",
    corrected="Led 10-person engineering team",
    context={"project": "jSeeker", "operation": "resume_adaptation"}
)
```

---

### 2. MNEMIS: Pattern Storage
**Location**: `X:\Projects\_GAIA\_MNEMIS\pattern_learner.py` (future)

**Responsibilities**:
- Analyze correction logs from ARGUS
- Extract reusable patterns
- Promote patterns across projects

**Example Pattern**:
```yaml
pattern_id: resume_active_voice
source: jSeeker corrections (2024-02-09)
rule: "Replace passive constructions ('Responsible for X') with active verbs ('Led X')"
confidence: 0.85  # Based on 20 corrections
applicable_to: [jSeeker, VIA (role descriptions)]
```

---

### 3. WARDEN: Pattern Enforcement
**Location**: `X:\Projects\_GAIA\_WARDEN\pattern_validator.py` (future)

**Responsibilities**:
- Validate LLM outputs against learned patterns
- Reject outputs that violate high-confidence patterns
- Provide correction hints

**Example**:
```python
# In jSeeker adapter
output = llm.generate(prompt)
violations = warden.validate(output, patterns=["resume_active_voice"])

if violations:
    # Retry with pattern hints
    prompt += f"\n\nIMPORTANT: {violations[0].hint}"
    output = llm.generate(prompt)
```

---

## Correction Event Schema

**Stored in**: `X:\Projects\_GAIA\_ARGUS\data\corrections.jsonl`

```json
{
  "timestamp": "2026-02-09T14:30:22Z",
  "session_id": "jseeker_20240209_143000",
  "correction_type": "resume_bullet_voice",
  "original": "Responsible for leading 10-person engineering team",
  "corrected": "Led 10-person engineering team to deliver product launch",
  "context": {
    "project": "jSeeker",
    "operation": "resume_adaptation",
    "model": "claude-sonnet-4.5",
    "prompt_template": "adaptation_v2"
  },
  "user_id": "default",
  "correction_method": "manual_edit"
}
```

**Fields**:
- `timestamp`: ISO 8601 timestamp
- `session_id`: Unique session identifier
- `correction_type`: Category (see taxonomy below)
- `original`: Agent's original output
- `corrected`: User's corrected version
- `context`: Additional metadata
- `user_id`: User identifier (for multi-user systems)
- `correction_method`: How correction was made (manual_edit, rejection, feedback_form)

---

## Correction Type Taxonomy

### Content Corrections
- `factual_error` - Hallucinated or incorrect information
- `missing_detail` - Output too vague, needs specifics
- `excessive_detail` - Output too verbose, needs trimming

### Style Corrections
- `tone_mismatch` - Wrong formality/voice
- `passive_to_active` - Passive voice → active voice
- `jargon_overuse` - Too much technical jargon
- `formatting` - Markdown, spacing, structure

### Structural Corrections
- `missing_section` - Required section omitted
- `section_order` - Sections in wrong order
- `bullet_structure` - Bullet point format wrong

### Domain-Specific (jSeeker)
- `ats_keyword_missing` - Missing required ATS keyword
- `metric_vague` - Lacks concrete metrics
- `experience_inflated` - Output exaggerates experience

### Domain-Specific (VIA)
- `claim_too_vague` - Extracted claim lacks specificity
- `source_missing` - No source attribution
- `claim_unsupported` - Claim not backed by evidence

---

## Implementation Roadmap

### Phase 1: Correction Logging (ARGUS)
**Timeline**: Immediate (this deliverable)

- [x] Create `correction_tracker.py` in ARGUS
- [x] Define correction event schema
- [ ] Integrate into jSeeker UI (manual edits)
- [ ] Integrate into VIA UI (claim rejections)

**Deliverable**: JSONL logs of user corrections

---

### Phase 2: Pattern Analysis (MNEMIS)
**Timeline**: 2-4 weeks

- [ ] Create `pattern_learner.py` in MNEMIS
- [ ] Analyze correction logs (frequency, clustering)
- [ ] Extract top 10 patterns from jSeeker corrections
- [ ] Create pattern YAML format
- [ ] Dashboard to review/approve patterns

**Deliverable**: `X:\Projects\_GAIA\_MNEMIS\patterns\learned\` directory with YAML patterns

---

### Phase 3: Pattern Enforcement (WARDEN)
**Timeline**: 4-6 weeks

- [ ] Create `pattern_validator.py` in WARDEN
- [ ] Implement validation rules from MNEMIS patterns
- [ ] Add pre-generation validation hooks
- [ ] Add post-generation validation hooks
- [ ] Integrate with jSeeker adapter

**Deliverable**: Automatic pattern enforcement in LLM pipelines

---

### Phase 4: Closed-Loop Learning
**Timeline**: 6-8 weeks

- [ ] User reviews learned patterns (approve/reject)
- [ ] Patterns with 5+ approvals auto-promoted
- [ ] Patterns update prompt templates automatically
- [ ] ARGUS dashboard shows correction trends
- [ ] A/B testing: patterns ON vs OFF

**Deliverable**: Fully automated learning pipeline

---

## Example: End-to-End Flow

**Scenario**: jSeeker user corrects resume bullets 5 times (passive → active voice)

### Week 1: Logging
```python
# In jSeeker UI (Streamlit)
if st.button("Save Edits"):
    for i, (original, edited) in enumerate(diff):
        if original != edited:
            log_correction(
                type="resume_bullet_edit",
                original=original,
                corrected=edited,
                context={"section": "experience", "bullet_index": i}
            )
```

**Result**: `corrections.jsonl` has 5 entries with passive → active pattern.

---

### Week 3: Pattern Detection (MNEMIS)
```python
# MNEMIS pattern learner
patterns = analyze_corrections("corrections.jsonl")
# Detects: 5 corrections with "Responsible for" → action verb
# Creates pattern: resume_active_voice
```

**Result**: `patterns/learned/resume_active_voice.yaml` created.

---

### Week 5: Pattern Enforcement (WARDEN)
```python
# In jSeeker adapter
adapted_bullets = llm.adapt_bullets(...)
violations = warden.validate(adapted_bullets, patterns=["resume_active_voice"])

if violations:
    # Add hint to prompt
    prompt += "\n\nRULE: Use active voice. Replace 'Responsible for X' with action verbs."
    adapted_bullets = llm.adapt_bullets(prompt)
```

**Result**: Future resumes automatically use active voice.

---

## Metrics to Track

### Correction Volume
- Corrections per session
- Corrections per project
- Corrections per LLM model

### Pattern Effectiveness
- % of corrections that form patterns (>3 instances)
- % of patterns that reduce future corrections
- Pattern confidence scores

### User Satisfaction
- Time to correct (before vs after pattern enforcement)
- User rating of LLM outputs (1-5 scale)
- Rejection rate (corrected outputs / total outputs)

---

## Integration Points

### jSeeker
**Location**: `ui/pages/2_new_resume.py`

```python
from argus.correction_tracker import log_correction

# After user edits generated resume
if original_resume != edited_resume:
    diff = compute_diff(original_resume, edited_resume)
    for change in diff:
        log_correction(
            type=classify_change(change),  # Auto-classify or user selects
            original=change.before,
            corrected=change.after,
            context={"jd_id": jd_id, "template": template_type}
        )
```

---

### VIA
**Location**: `ui/pages/claim_review.py` (hypothetical)

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

---

## Privacy & Data Governance

### PII Protection
- **No PHI in correction logs** (jSeeker resumes)
- Anonymize user names: "John Smith" → "[NAME_1]"
- Anonymize companies: "Google" → "[COMPANY_1]"
- Store mapping separately with encryption

### Data Retention
- Correction logs retained for 90 days (analysis window)
- Learned patterns retained indefinitely
- User can request correction data deletion

### User Consent
- Opt-in during first use: "Help improve GAIA by sharing corrections?"
- Toggle in settings: "Learning Mode: ON/OFF"
- If OFF, corrections not logged

---

## Future Enhancements

### 1. Multi-User Pattern Aggregation
Aggregate corrections from multiple users to find consensus patterns.

```python
# Pattern with consensus score
pattern = {
    "rule": "Use active voice in resume bullets",
    "users_confirmed": 5,
    "users_rejected": 1,
    "consensus_score": 0.83
}
```

---

### 2. Real-Time Correction Suggestions
As user types, suggest corrections based on patterns.

```python
# In Streamlit editor
if detect_pattern_violation(user_input):
    st.info("Tip: Consider using active voice here")
```

---

### 3. Pattern Promotion Across Projects
Promote jSeeker patterns to VIA if applicable.

```python
# Example: Active voice pattern applies to VIA's role descriptions
if pattern.applicable_to(["VIA"]):
    mnemis.promote_pattern(pattern, target="VIA")
```

---

## References

- ARGUS Correction Tracker: `X:\Projects\_GAIA\_ARGUS\correction_tracker.py`
- MNEMIS Pattern Storage: `X:\Projects\_GAIA\_MNEMIS\pattern_learner.py` (future)
- WARDEN Pattern Validator: `X:\Projects\_GAIA\_WARDEN\pattern_validator.py` (future)
- jSeeker Integration: `X:\Projects\jSeeker\ui\pages\2_new_resume.py`
- VIA Integration: `X:\Projects\VIA\ui\pages\claim_review.py` (future)

---

## Next Steps

1. **Implement ARGUS correction tracker** (this deliverable)
2. **Add correction logging to jSeeker UI** (Week 2)
3. **Collect 100 corrections** (baseline dataset)
4. **Analyze patterns manually** (proof of concept)
5. **Build MNEMIS pattern learner** (Phase 2)
