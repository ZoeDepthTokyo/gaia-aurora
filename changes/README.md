# GAIA ChangeSpec Convention

## Purpose
Every non-trivial change to GAIA must produce a spec artifact trail BEFORE implementation begins.

## Directory Structure
```
changes/
├── <change-name>/
│   ├── proposal.md     # Intent, scope, out-of-scope, success criteria
│   ├── specs/           # Delta specs per affected component
│   │   └── <component>.md
│   ├── design.md        # Technical approach, alternatives, chosen approach
│   └── tasks.md         # Numbered checklist with checkboxes
└── archive/             # Completed changes (moved here by /archiving-change)
    └── <change-name>/
```

## Artifact Chain
1. proposal.md — WHY (intent, scope, success criteria)
2. specs/<component>.md — WHAT (delta requirements with Given-When-Then)
3. design.md — HOW (technical approach, trade-offs)
4. tasks.md — WHEN (ordered checklist)

## Delta Spec Format
Use ADDED/MODIFIED/REMOVED tags:

### ADDED: <Requirement Name>
The system MUST <new behavior>.
#### Scenario: <descriptive name>
- GIVEN <precondition>
- WHEN <trigger>
- THEN <expected outcome>

### MODIFIED: <Requirement Name>
Was: <old behavior>
Now: The system MUST <new behavior>.

### REMOVED: <Requirement Name>
Reason: <justification>

## Archive Rules
- A change is complete when ALL tasks.md checkboxes are checked
- /archiving-change moves completed changes to archive/
- Archive is searchable institutional memory
- Never delete archived changes
