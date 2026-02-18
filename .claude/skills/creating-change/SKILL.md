---
name: creating-change
description: "[OPENING] Generates a complete spec artifact trail (proposal, delta specs, design doc, task checklist) before implementing any non-trivial GAIA change. Use when starting new features, refactoring, bug fixes, or any change spanning multiple files. Triggers on: new feature, implement, add capability, refactor, redesign. Why: governance audit trail before code changes."
---

# /creating-change

Creates the full spec artifact trail for a GAIA change before any implementation begins.

## Usage

```
/creating-change <change-name>
```

`<change-name>` should be kebab-case and describe the change (e.g., `add-ats-scoring`, `refactor-sim-engine`).

## Session Placement

This is an **[OPENING]** skill -- run it at the start of a session before writing any implementation code. The spec artifacts it creates are prerequisites for the `skill_guard.py` PreToolUse hook, which blocks component edits without an active change spec.

Typical opening sequence:
1. `/orienting-to-component <target>` -- understand current state
2. `/creating-change <name>` -- create spec trail
3. Implement against the spec

## When to Use

Use this skill when:
- Starting any new feature or capability
- Refactoring code that spans multiple files or components
- Fixing a bug with non-trivial root cause or fix scope
- Making any change that touches more than one GAIA component
- The word "implement", "add", "refactor", "new feature", or "redesign" appears in the request

Skip for: single-file typo fixes, doc-only edits, config tweaks with no behavior change.

## Artifact Chain

```
changes/<name>/
├── proposal.md      Step 1: WHY
├── specs/           Step 2: WHAT (one file per component)
│   └── <comp>.md
├── design.md        Step 3: HOW
└── tasks.md         Step 4: WHEN
```

Full templates: see `references/artifact-templates.md`
Spec format details: see `references/spec-format.md`

## Workflow

### Step 1 — Proposal (WHY)

Ask the user (or infer from context):
1. **Intent**: What problem does this change solve?
2. **Scope**: Which GAIA components are affected?
3. **Out-of-scope**: What is explicitly excluded?
4. **Success criteria**: How do we know it's done? (machine-verifiable preferred)

Write `changes/<name>/proposal.md`. Do not proceed until the user confirms scope.

### Step 2 — Delta Specs (WHAT)

For each affected component:
1. Read that component's `CLAUDE.md` to understand current behavior
2. Identify ADDED / MODIFIED / REMOVED requirements
3. Write `changes/<name>/specs/<component>.md` using Given-When-Then format

See `references/spec-format.md` for format rules and examples.

**Gate**: Review specs with user before writing design.md. Specs define the contract.

### Step 3 — Design (HOW)

Document:
- Chosen technical approach with rationale
- Alternatives considered and why they were rejected
- Key files that will change
- API/interface changes (if any)
- Risk factors and mitigations

Write `changes/<name>/design.md`.

### Step 4 — Task Checklist (WHEN)

Break the implementation into numbered, atomic tasks with checkboxes:
```markdown
- [ ] 1. <specific action> (`path/to/file.py`)
- [ ] 2. <specific action> (tests)
- [ ] 3. Run /reconciling-gaia --dry-run
```

Rules:
- Each task must be completable in one focused session
- Tests must be an explicit task (not bundled with implementation)
- Last task is always: verify all tests pass
- Write `changes/<name>/tasks.md`

## Integration

| After this skill | Use this skill |
|---|---|
| Implementation complete, all tasks checked | `/archiving-change <name>` |
| Docs may be out of sync | `/reconciling-gaia` |

## Checkpoints

This skill has 3 user checkpoints (HITL compliance):
1. After proposal — confirm scope before writing specs
2. After specs — confirm contract before writing design
3. After tasks — confirm checklist before implementation begins

Never auto-proceed past a checkpoint without user confirmation.
