---
name: registry-sync
description: Validate and sync GAIA registry.json with governance checks
disable-model-invocation: true
---

# Registry Sync Workflow

Manages registry.json updates with WARDEN validation and git tracking.

## Usage
```
/registry-sync [--validate-only] [--component <name>]
```

## Process

1. **Read Current State**
   - Load registry.json
   - Parse all 17 component entries
   - Check current VERSION_LOG.md

2. **Schema Validation**
   ```bash
   python -c "import json; json.load(open('registry.json'))"
   ```

3. **WARDEN Governance Check**
   ```bash
   cd _WARDEN
   python -m warden.cli validate --project /x/Projects/_GAIA
   ```

4. **Integrity Checks**
   - Verify no duplicate component names
   - Check all paths exist on filesystem
   - Validate version format (semver)
   - Ensure status values: production/active/development/planning/stale/defined/complete

5. **Cross-Reference**
   - Check GAIA_BIBLE.md matches registry count
   - Verify GECO_AUDIT.md lists all components
   - Ensure all git_remote URLs populated (where applicable)

6. **Update VERSION_LOG.md**
   - Document registry changes
   - Add timestamp and change summary

7. **Git Operations**
   ```bash
   git add registry.json VERSION_LOG.md
   git status
   ```

8. **User Confirmation**
   - Display changes summary
   - Prompt: "Commit changes? (y/n)"
   - If yes: `git commit -m "chore: Update GAIA registry - [summary]"`

## Options

- `--validate-only`: Check integrity without making changes
- `--component <name>`: Focus validation on specific component
- `--fix`: Attempt auto-fix common issues (missing paths, version formats)

## Output Format

```
Registry Sync Report
====================

✅ Schema Valid
✅ WARDEN Passed
✅ 17/17 Paths Exist
✅ No Duplicates

Changes Detected:
- ARGUS: 0.5.1 → 0.5.2
- WARDEN: git_remote added

GAIA_BIBLE.md: ✅ Synced (17 components)
VERSION_LOG.md: ✅ Updated

Next: git commit -m "chore: Update GAIA registry - version bumps"
```

## Error Handling

**Common Issues:**
- Missing component path → Suggest correction or mark as stale
- Invalid semver → Prompt for correct format
- WARDEN failure → Display validation errors, block commit
- Duplicate names → Show conflicts, require manual resolution

## Integration

This skill replaces manual registry.json edits and ensures:
- Constitutional compliance (WARDEN validation)
- Git tracking (VERSION_LOG.md)
- Ecosystem integrity (cross-references)
