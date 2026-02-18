---
name: reconciling-gaia
description: "[CLOSING] Propagates component changes to upstream GAIA documents (registry.json, MANIFEST, GECO matrix) using CASCADE_MAP rules. Use after any session that modifies component code, configuration, or documentation. Triggers on: end of session, reconcile, cascade, sync docs, propagate changes. Why: keeps ecosystem docs current via cascade propagation."
---

# /reconcile — GAIA Cascade Reconciliation

## Usage
```
/reconcile [--dry-run] [--auto] [--ask-all]
```

**Flags:**
- `--dry-run`: Preview changes without applying anything
- `--auto`: Skip HITL for GREEN tier items (default behavior)
- `--ask-all`: Force HITL approval on ALL items including GREEN

## When to Use
Run at end of each session after making changes to any GAIA component. Also suggested by hooks when component files are modified.

## Workflow

### Step 0.5: RUN SKILL HEALTH CHECK

Before processing cascades, verify skill ecosystem integrity:

```bash
python runtime/scripts/skill_health.py
```

Review the output for:
- Missing phase tags (skills without [OPENING], [CLOSING], or [CONTEXT])
- Oversized SKILL.md files (over 500 lines)
- Phantom skills (referenced but no directory)
- Unreferenced skills (directory exists but not in any CLAUDE.md)

Include the health check summary in the session reconciliation report.
If issues are found, note them as advisories but do not block reconciliation.

### Step 0: CHECK ACTIVE CHANGES

Before processing cascades, scan for completed ChangeSpec artifacts:

1. **Scan `changes/` directory** for active change folders
2. **For each change folder**, read `tasks.md` and check if ALL checkboxes are checked
3. **If completed changes found**, suggest:
   ```
   Completed changes ready for archive:
     - changes/<name>/ (all tasks done)

   Run /archiving-change <name> to archive and merge specs.
   ```
4. **If no completed changes**, proceed to Step 1

This step ensures completed changes are archived before new cascades are processed.

### Step 1: DETECT Changes

Identify what changed this session:

```bash
# Check git diff for staged + unstaged changes
git diff --name-only HEAD
git diff --name-only --cached
```

Also read `.gaia_changes` file if it exists (populated by PostToolUse hook):
```bash
cat .gaia_changes 2>/dev/null || echo "No tracked changes"
```

Classify each changed file:
- **Component directory**: `_ARGUS/`, `_AURORA/`, `_LOOM/`, `_MNEMIS/`, `_MYCEL/`, `_VULCAN/`, `_WARDEN/`, `_RAVEN/`, `_ABIS/`, `_ECHO/`, `_PROTEUS_ARCHIVED/`, `runtime/`
- **Change type**: `code` (.py), `config` (.json, .yaml, .toml), `docs` (.md), `tests` (tests/), `version` (VERSION_LOG, registry)

### Step 2: READ CASCADE MAPS

For each changed component, read its CLAUDE.md and extract the `<!-- CASCADE_MAP -->` section. Parse rules in format:
```
- target_file: description → permission_tier
```

Where `permission_tier` is one of: `auto`, `ask`, `block`

Also apply universal cascade rules from GAIA_MANIFEST.md:
- `registry.json` version field → auto
- `GAIA_MANIFEST.md` component table row → auto
- `GECO_REVIEW_MATRIX.md` component row → auto

### Step 3: CLASSIFY Each Cascade

Build a checklist with three tiers:

**GREEN (auto-apply)**:
- registry.json: version bump
- GAIA_MANIFEST.md: Component State Table row update (version, status, last_changed)
- GECO_REVIEW_MATRIX.md: capability checkmarks

**YELLOW (ask first)**:
- GAIA_PRD.md: section content update
- VERSION_LOG.md: new version entry
- New dependency added to registry.json `depends_on`
- API surface changes affecting dependents

**RED (block — do not apply)**:
- GAIA_BIBLE.md: any modification
- Constitutional constraint changes
- Component deletion from registry
- Architecture pattern changes

### Step 4: EXECUTE

#### For GREEN items (unless `--ask-all`):
1. Read the target file
2. Apply the specific update (version bump, table row, checkmark)
3. Validate the result (JSON parse for registry, line count for MANIFEST)
4. Log to `.gaia_reconcile_log`

#### For YELLOW items:
Present numbered checklist to user:
```
Awaiting approval:
  [1] VERSION_LOG.md: Add v0.5.3 entry for AURORA creative direction? (Y/N)
  [2] GAIA_PRD.md Section 4.8: Add creative direction capabilities? (Y/N)

Respond with numbers to approve (e.g., "1,2" or "all" or "none")
```

Apply approved items, skip rejected ones.

#### For RED items:
Flag and do NOT apply:
```
BLOCKED (requires dedicated session):
  - GAIA_BIBLE.md: constitutional constraint addition proposed
```

### Step 5: UPDATE MANIFEST

After all changes applied:
1. Refresh Component State Table with current registry.json data
2. Update `last_reconciled` timestamp in MANIFEST header
3. Update "Active Priorities" if priorities shifted during session
4. Verify MANIFEST stays under 250 lines — warn if approaching limit
5. Bump manifest_version patch number

### Step 6: REPORT

Output a structured report:

```
GAIA Reconciliation Report
==========================

Session Changes Detected:
  _AURORA/creative_direction/*.py  (3 files, code)
  _AURORA/CLAUDE.md                (1 file, docs)

Cascade Analysis:
  [AUTO] registry.json: AURORA version 0.1.0 → 0.2.0
  [AUTO] MANIFEST: AURORA row updated, last_changed = 2026-02-11
  [AUTO] GECO matrix: AURORA row updated
  [ASK]  GAIA_PRD.md Section 4.8: Add creative direction capabilities?
  [ASK]  VERSION_LOG.md: Add v0.5.3 entry for AURORA creative direction?

Auto-applied: 3 changes
Awaiting approval: 2 changes
Blocked: 0

Reconciliation log: .gaia_reconcile_log
```

### Step 7: CLEANUP

- Clear `.gaia_changes` file (reset for next session)
- Append session summary to `.gaia_reconcile_log`

## Implementation Notes

Covers: registry.json hook behavior, MANIFEST update steps, cross-validation, idempotency, error handling, and dry-run semantics.

For full implementation guidance, see references/implementation-notes.md.
