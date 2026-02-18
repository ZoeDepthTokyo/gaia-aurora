# Artifact Templates

Full copy-paste templates for all 4 ChangeSpec artifacts.

---

## Template: proposal.md

```markdown
# Change Proposal: <change-name>

Date: YYYY-MM-DD
Author: <who initiated this>
Status: draft | approved | in-progress | complete

## Intent
<1-3 sentences: what problem does this change solve? why now?>

## Scope

### Affected Components
- <component-1>: <brief description of impact>
- <component-2>: <brief description of impact>

### Out of Scope
- <explicitly excluded thing 1>
- <explicitly excluded thing 2>

## Success Criteria
<!-- Must be machine-verifiable where possible -->
- [ ] <criterion 1 — e.g., "all existing tests pass">
- [ ] <criterion 2 — e.g., "new feature works end-to-end in manual test">
- [ ] <criterion 3 — e.g., "no regressions in ARGUS dashboard">

## Risks
- <risk 1>: <mitigation>
- <risk 2>: <mitigation>

## Dependencies
<!-- Other changes or external work this depends on -->
- <dependency 1>
```

---

## Template: specs/<component>.md

```markdown
# Delta Spec: <component-name>
Change: <change-name>
Version: draft
Last updated: YYYY-MM-DD

## Summary
<1-2 sentences: what changes in this component>

## Requirements

### ADDED: <Requirement Name>
The system MUST <new behavior>.

#### Scenario: <name>
- GIVEN <precondition>
- WHEN <trigger>
- THEN <expected outcome>

### MODIFIED: <Requirement Name>
Was: <old behavior>
Now: The system MUST <new behavior>.

#### Scenario: <name>
- GIVEN <precondition>
- WHEN <trigger>
- THEN <expected outcome>

### REMOVED: <Requirement Name>
Reason: <justification>
```

---

## Template: design.md

```markdown
# Design: <change-name>

Date: YYYY-MM-DD
Status: draft | reviewed | approved

## Chosen Approach
<Description of the technical approach selected>

### Rationale
<Why this approach over alternatives>

## Alternatives Considered

### Option A: <name>
<Description>
Rejected because: <reason>

### Option B: <name>
<Description>
Rejected because: <reason>

## Key Changes

### Files Modified
| File | Change Type | Notes |
|------|------------|-------|
| `path/to/file.py` | Modified | <brief description> |
| `path/to/new.py` | Added | <brief description> |

### API / Interface Changes
<!-- List any public API, CLI, or UI changes -->
- <change 1>
- <change 2>

## Data Flow
<!-- Optional: mermaid diagram or ASCII art for complex flows -->

## Testing Strategy
- Unit tests: <what to test>
- Integration tests: <what to test>
- Manual verification: <what to check>

## Rollback Plan
<How to undo this change if needed>
```

---

## Template: tasks.md

```markdown
# Tasks: <change-name>

Total: N tasks | Completed: 0

## Implementation Checklist

- [ ] 1. <atomic task — be specific about what file/function changes>
- [ ] 2. <atomic task>
- [ ] 3. Write tests for <specific behavior> (`tests/test_<module>.py`)
- [ ] 4. <atomic task>
- [ ] 5. Run existing test suite — all tests must pass
- [ ] 6. Manual smoke test: <specific steps>
- [ ] 7. Run `/reconciling-gaia --dry-run` — review cascade impacts
- [ ] 8. Update GAIA_MANIFEST.md if component versions changed

## Notes
<!-- Add implementation notes here as you work -->
```

---

## Naming Conventions

| Field | Convention | Example |
|-------|-----------|---------|
| `<change-name>` | kebab-case, verb-noun | `add-ats-scoring` |
| `<component>` | match registry.json name | `argus`, `mycel` |
| Spec version | `draft` → `reviewed` → `approved` | — |
| Task numbers | Sequential integers, never skip | 1, 2, 3... |
