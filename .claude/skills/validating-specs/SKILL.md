---
name: validating-specs
description: "[CLOSING] Validates spec files for correct Given-When-Then format, required sections, and proper markdown structure. Use after writing or editing spec files, before archiving changes, or during spec review. Triggers on: validate specs, check spec format, spec review, are my specs valid, GWT. Why: enforces spec quality before archiving."
---

# /validating-specs — Spec Format Validator

## Usage
```
/validating-specs [path]
```

**Arguments:**
- `path` — File or directory to validate (default: `changes/`)
- Omit path to validate all active changes
- Pass a specific file: `/validating-specs _ARGUS/specs/core-behaviors.md`
- Pass a directory: `/validating-specs _ARGUS/specs/`

## When to Use
- After writing new spec files in `changes/<name>/specs/` or `<component>/specs/`
- Before running `/archiving-change` (specs must be valid to archive)
- During PR review when spec files are modified
- After editing existing specs to verify format integrity

## What It Validates

### 1. Given-When-Then Presence
Every spec file must contain at least one complete scenario with:
- A `GIVEN` clause (setup state)
- A `WHEN` clause (triggering action)
- A `THEN` clause (expected outcome)

Files with narrative text only (no scenarios) fail this check.

### 2. Required Section Headers
Each spec file should contain:
- At least one `## Requirement:` header
- At least one `### Scenario:` header under each requirement

### 3. Delta Tags (for change spec files)
Files in `changes/<name>/specs/` should include delta tags:
- `ADDED` — new behavior not previously specified
- `MODIFIED` — change to an existing behavior
- `REMOVED` — behavior being deleted

Baseline specs in `<component>/specs/` do not require delta tags.

### 4. Path Format
Spec files must not contain Windows-style backslash paths in examples.
- Bad: `X:\Projects\_GAIA\registry.json`
- Good: `X:/Projects/_GAIA/registry.json`

## Process

### Step 1: Determine Scope
If path argument given, validate that path.
Otherwise, scan `changes/` directory for active change folders.

### Step 2: Run Validator Script
```bash
python X:/projects/_GAIA/.claude/skills/validating-specs/scripts/validate_specs.py [path]
```

### Step 3: Report Results
If validation passes:
```
All specs valid. (12 files checked)
```

If issues found:
```
Found 3 issue(s):
  - changes/my-feature/specs/delta.md: Missing Given-When-Then scenarios
  - _LOOM/specs/error-states.md: Missing WHEN clause
  - _ARGUS/specs/core-behaviors.md: Contains Windows-style paths (use forward slashes)
```

### Step 4: Fix or Proceed
- If all valid: proceed with `/archiving-change` or continue implementation
- If issues found: fix each issue, then re-run `/validating-specs`

## Quick Fix Guide

| Issue | Fix |
|-------|-----|
| Missing GIVEN/WHEN/THEN | Add scenario block with all three clauses |
| Missing `## Requirement:` | Add a requirement header before each scenario group |
| Windows paths | Replace `\` with `/` in all path examples |
| No delta tags | Add `ADDED:`, `MODIFIED:`, or `REMOVED:` to change specs |

## Script Location
`X:/projects/_GAIA/.claude/skills/validating-specs/scripts/validate_specs.py`

Run directly:
```bash
python X:/projects/_GAIA/.claude/skills/validating-specs/scripts/validate_specs.py changes/
python X:/projects/_GAIA/.claude/skills/validating-specs/scripts/validate_specs.py _ARGUS/specs/
```

Exit codes:
- `0` — All specs valid
- `1` — One or more issues found
