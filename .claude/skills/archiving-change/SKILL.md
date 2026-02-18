---
name: archiving-change
description: "[CLOSING] Archives completed GAIA changes by moving artifacts to changes/archive/, merging delta specs into component baselines, and triggering reconciliation. Use when all tasks in a change are complete, after implementation and testing. Triggers on: archive, close change, all tasks done. Why: closes audit trail and frees active changes directory."
---

# /archiving-change

Archives a completed change by moving its spec artifacts to `changes/archive/`, stamping the proposal with a completion timestamp, and suggesting reconciliation.

## Usage

```
/archiving-change <change-name>
```

## When to Use

Use this skill when:
- All checkboxes in `changes/<name>/tasks.md` are checked
- Implementation is complete and tests are passing
- You want to close out a change and free the active changes directory

Do NOT use if any tasks.md item is unchecked — the change is not done.

## Pre-flight Checks

Before archiving, verify:

1. **All tasks checked** — Read `changes/<name>/tasks.md`. Count unchecked `- [ ]` items. If any remain, stop and report which tasks are incomplete.
2. **Change directory exists** — Confirm `changes/<name>/` is present. If not, report an error.
3. **Archive target is clear** — Confirm `changes/archive/<name>/` does not already exist. If it does, warn the user and ask for confirmation before overwriting.

## Workflow

### Step 1 — Verify Completeness

Read `changes/<name>/tasks.md` and count unchecked items.

If unchecked tasks found:
```
BLOCKED: Cannot archive '<name>' — N tasks remain incomplete:
  - [ ] 3. <task text>
  - [ ] 7. <task text>

Complete these tasks before archiving.
```

### Step 2 — Stamp proposal.md

Add a completion block to the top of `changes/<name>/proposal.md`:

```markdown
> **ARCHIVED**: Completed YYYY-MM-DD
> All N tasks verified complete.
```

### Step 3 — Move to archive

Move the entire directory:
```
changes/<name>/  →  changes/archive/<name>/
```

On Windows, use Python's `shutil.move()` (via `scripts/merge_specs.py`) or instruct the user to run:
```bash
mv changes/<name> changes/archive/<name>
```

### Step 4 — Report

Output a summary:
```
Archived: changes/<name>/ → changes/archive/<name>/
Artifacts:
  proposal.md (stamped YYYY-MM-DD)
  specs/<component1>.md
  specs/<component2>.md
  design.md
  tasks.md (N/N tasks complete)
```

### Step 5 — Suggest reconciliation

After archiving, prompt:
```
Suggest running /reconciling-gaia --dry-run to check if any cascade updates
are needed based on the changes made during this change.
```

## Spec Merging (Optional)

Delta specs in `changes/archive/<name>/specs/` may need to be merged into component baseline specs if they exist. This is handled by `scripts/merge_specs.py`.

This step is optional — only needed if the component has a formal baseline spec at `changes/<component>-baseline.md` or similar.

## Integration

| Before this skill | Use this skill |
|---|---|
| /creating-change created the artifacts | Implementation + testing complete |

| After this skill | Use this skill |
|---|---|
| Docs may be out of date | `/reconciling-gaia` |

## Error Cases

| Error | Response |
|-------|----------|
| Unchecked tasks remain | Block, list incomplete tasks |
| Change directory not found | Report, suggest `ls changes/` |
| Archive target already exists | Warn, ask user to confirm |
| tasks.md missing | Warn, ask user to verify manually |
