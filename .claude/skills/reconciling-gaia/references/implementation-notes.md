# Implementation Notes

## Registry.json Updates (GREEN)
When updating registry.json version:
1. Read current registry.json
2. Find the component entry by key
3. Update version field only
4. Write back with same formatting
5. The PreToolUse hook on registry.json will fire — this is expected. The reconcile skill has implicit WARDEN validation permission since it's a governance tool.

**IMPORTANT**: The existing PreToolUse hook blocks registry.json edits with a message to use `/registry-sync`. When running `/reconcile`, present the registry changes to the user and ask them to approve the registry.json edit specifically, OR use the registry-sync skill for that portion.

## MANIFEST Updates (GREEN)
When updating MANIFEST Component State Table:
1. Read GAIA_MANIFEST.md
2. Find the row for the changed component
3. Update version, status, and last_changed columns
4. Update `last_reconciled` comment in header
5. Verify line count < 250

## Cross-Validation
After applying changes, verify consistency:
- registry.json version matches MANIFEST table version
- MANIFEST `last_reconciled` matches today's date
- No circular cascade rules triggered

## Idempotency
Running `/reconcile` twice should produce the same result. Each step checks current state before applying:
- If registry version already matches, skip
- If MANIFEST row already current, skip
- If VERSION_LOG already has entry, skip

## Error Handling
- If a file can't be read: warn and skip that cascade, continue with others
- If a write fails: log the failure, continue with remaining items
- If registry.json hook blocks the edit: present changes to user as YELLOW instead of GREEN
- Never leave files in a partially-updated state

## Dry Run Mode (`--dry-run`)
When `--dry-run` is specified:
- Perform all detection and classification steps
- Output the full report with what WOULD be changed
- Do NOT modify any files
- Do NOT clear `.gaia_changes`
