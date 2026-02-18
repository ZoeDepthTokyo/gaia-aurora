# Delta Spec Format Reference

## Overview

Delta specs describe only what changes — not the full system state. Use ADDED, MODIFIED, or REMOVED tags.

## Tags

### ADDED
For new requirements that didn't exist before.

```markdown
### ADDED: <Requirement Name>
The system MUST <new behavior>.

#### Scenario: <descriptive scenario name>
- GIVEN <precondition — system or user state before trigger>
- WHEN <trigger — the action or event>
- THEN <expected outcome — observable, verifiable result>
```

Multiple scenarios per requirement are allowed.

### MODIFIED
For requirements that existed but are changing.

```markdown
### MODIFIED: <Requirement Name>
Was: <old behavior — quote or paraphrase the old requirement>
Now: The system MUST <new behavior>.

#### Scenario: <descriptive scenario name>
- GIVEN <precondition>
- WHEN <trigger>
- THEN <expected outcome>
```

### REMOVED
For requirements being deleted.

```markdown
### REMOVED: <Requirement Name>
Reason: <justification — why this behavior is no longer needed>
```

No scenario needed for REMOVED — the behavior simply won't exist.

## Given-When-Then Rules

- **GIVEN** describes state, not action. Use present tense ("the user has", "the system is").
- **WHEN** is a single trigger event. If you need multiple WHENs, split into separate scenarios.
- **THEN** must be observable and verifiable. Avoid vague outcomes like "it works correctly".
- One scenario per specific case. Don't cram edge cases into one scenario.

## File Header

Each `specs/<component>.md` file must start with:

```markdown
# Delta Spec: <component-name>
Change: <change-name>
Version: draft | reviewed | approved
Last updated: YYYY-MM-DD

## Summary
<1-2 sentence description of what changes in this component>

## Requirements
```

## Examples

### Good ADDED scenario
```markdown
### ADDED: ATS Platform Score
The system MUST compute an ATS compatibility score per job platform.

#### Scenario: LinkedIn job detected
- GIVEN the user has pasted a job description
- WHEN the URL domain contains "linkedin.com"
- THEN the system returns an ATS score calibrated for LinkedIn's parser
```

### Good MODIFIED scenario
```markdown
### MODIFIED: Cost Display
Was: Cost shown only in sidebar after analysis completes.
Now: The system MUST display estimated cost BEFORE the user triggers analysis.

#### Scenario: User opens analysis tab
- GIVEN the user has loaded a job description
- WHEN the user navigates to the Analysis tab
- THEN the estimated API cost is shown prominently above the Run button
```

### Bad scenario (avoid)
```markdown
#### Scenario: It works
- GIVEN the system is running
- WHEN the user does something
- THEN it works correctly
```
Problems: vague GIVEN, vague WHEN, unverifiable THEN.

## Validation Checklist

Before marking specs as reviewed:
- [ ] Every ADDED requirement has at least one scenario
- [ ] Every MODIFIED requirement shows the old behavior explicitly
- [ ] Every THEN is machine-verifiable (can be tested)
- [ ] No scenarios overlap or contradict each other
- [ ] All affected components have a spec file
