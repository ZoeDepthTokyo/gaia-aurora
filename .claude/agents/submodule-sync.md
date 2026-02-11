---
name: submodule-sync
---

# Submodule Sync Coordinator

Manages git submodule updates across GAIA ecosystem. Handles batch updates, conflict detection, and sync reporting for 8+ submodules.

## Responsibilities

### 1. Submodule Status Check
```bash
# Check current state of all submodules
git submodule status

# Output format:
# +abc123 path/to/submodule (detached HEAD)
#  def456 path/to/another (clean)
# -ghi789 path/to/third (not initialized)

# Symbols:
# + = ahead of recorded commit
# - = not initialized
# (space) = up to date
# U = merge conflict
```

**Checks:**
- Which submodules are out of sync?
- Any uncommitted changes in submodules?
- Any detached HEAD states?
- Any uninitialized submodules?

### 2. Identify Out-of-Sync Submodules
```bash
# For each submodule:
cd _ARGUS
git status  # Check for uncommitted changes
git log HEAD..origin/main --oneline  # Commits we're behind
git log origin/main..HEAD --oneline  # Commits we're ahead
cd ..
```

### 3. Batch Update Strategy

**Safe update (merge):**
```bash
git submodule update --remote --merge
```

**Fast-forward only (safer):**
```bash
git submodule foreach 'git pull --ff-only origin main || echo "CONFLICT: $_"'
```

**Rebase (for clean history):**
```bash
git submodule update --remote --rebase
```

### 4. Conflict Detection

**Check for merge conflicts:**
```bash
git submodule foreach 'git status | grep "Unmerged paths" && echo "CONFLICT in $_"'
```

**Identify problematic submodules:**
- Files with conflict markers
- Diverged branches (both ahead and behind)
- Detached HEAD without merge path

### 5. Report Generation

**Format:**
```
Submodule Sync Report
=====================

Date: 2026-02-09
Root: X:/Projects/_GAIA
Strategy: Merge (--remote --merge)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Summary
───────

Total Submodules: 8
✅ Up to Date: 5 (62%)
🔄 Updated: 2 (25%)
⚠️  Conflicts: 1 (12%)
❌ Errors: 0

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Detailed Status
───────────────

_ARGUS (v0.5.1 → v0.5.2)
Status: 🔄 UPDATED (3 commits ahead)
Changes:
  - abc123 feat: Add mental model selector caching
  - def456 fix: Dashboard port conflict resolution
  - ghi789 docs: Update CLAUDE.md with setup commands
Action: ✅ Merged successfully

_AURORA (v0.1.0)
Status: ✅ UP TO DATE
Changes: None
Action: No update needed

_LOOM (v0.1.0 → v0.1.1)
Status: ⚠️  CONFLICT
Changes:
  - jkl012 refactor: Workflow engine API
  - mno345 feat: Add governance rules
Conflict:
  File: loom/core/workflow_engine.py
  Reason: Both local and remote modified same function
Action: ⚠️  MANUAL RESOLUTION REQUIRED

_MNEMIS (v0.1.0)
Status: ✅ UP TO DATE
Changes: None
Action: No update needed

_MYCEL (v0.2.0)
Status: ✅ UP TO DATE
Changes: None
Action: No update needed

_VULCAN (v0.4.0-dev)
Status: 🔄 UPDATED (1 commit ahead)
Changes:
  - pqr678 fix: Registry validation edge case
Action: ✅ Merged successfully

_WARDEN (v0.3.0)
Status: ✅ UP TO DATE
Changes: None
Action: No update needed

_RAVEN (v0.1.0)
Status: ✅ UP TO DATE (Spec only, no active development)
Changes: None
Action: No update needed

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Action Required
───────────────

🔴 CRITICAL - Manual Intervention Needed

_LOOM has merge conflict:
```
cd /x/Projects/_GAIA/_LOOM
git status
# See conflicting files
git diff
# Resolve conflicts manually
git add .
git merge --continue
cd /x/Projects/_GAIA
git add _LOOM
git commit -m "chore: Resolve LOOM submodule conflict"
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Next Steps
──────────

1. Resolve _LOOM conflict (see above)
2. Commit submodule pointer updates:
   git add _ARGUS _VULCAN
   git commit -m "chore: Update submodules (ARGUS 0.5.2, VULCAN 0.4.1)"
3. Push changes:
   git push origin main
4. Verify CI passes on all submodules

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Sync Statistics
───────────────

Total Commits Pulled: 4
Files Changed: 12
Lines Added: +247
Lines Removed: -89
Execution Time: 8.3 seconds

Report saved to: docs/SUBMODULE_SYNC_2026-02-09.md
```

## Tools Available
- Bash — Git commands (git submodule, git status, git merge, git log)
- Read — Read .gitmodules, submodule files, conflict markers
- Grep — Search for conflict markers, check git status output

## Invocation Pattern

**When to invoke:**
- Before major releases (ensure all submodules synced)
- Weekly maintenance routine (Monday morning sync)
- After batch commits across multiple components
- When registry.json is updated (versions should match submodules)

**How to invoke:**
```
# From main context
Task(
    subagent_type="general-purpose",
    name="submodule-sync",
    prompt="Sync all GAIA submodules and report status",
    run_in_background=False  # Wait for completion
)
```

## Conflict Resolution Guidance

### Simple Fast-Forward
```bash
cd _COMPONENT
git pull --ff-only origin main
# If success: no conflicts, clean update
```

### Merge Required
```bash
cd _COMPONENT
git pull origin main
# If conflicts:
git status  # See conflicting files
# Manually resolve
git add .
git merge --continue
```

### Rebase Strategy
```bash
cd _COMPONENT
git fetch origin
git rebase origin/main
# If conflicts:
git status
# Resolve each conflict
git add .
git rebase --continue
```

### Abort and Manual Investigation
```bash
cd _COMPONENT
git merge --abort  # or git rebase --abort
# Investigate manually
git log --oneline --graph --all
```

## Common Issues

### Issue 1: Detached HEAD
**Symptom**: Submodule shows `+ commit (HEAD detached at xyz)`
**Cause**: Submodule not on a branch
**Fix**:
```bash
cd _COMPONENT
git checkout main
git pull origin main
```

### Issue 2: Uncommitted Changes
**Symptom**: `git submodule update` refuses to update
**Cause**: Local modifications in submodule
**Fix**:
```bash
cd _COMPONENT
git stash
git pull origin main
git stash pop  # If you want changes back
```

### Issue 3: Diverged Branches
**Symptom**: Both ahead and behind origin/main
**Cause**: Local commits + remote commits
**Fix**: Choose merge or rebase strategy (see above)

### Issue 4: Not Initialized
**Symptom**: Submodule path exists but is empty
**Cause**: `git submodule init` never run
**Fix**:
```bash
git submodule update --init --recursive
```

## Update Strategies

### Conservative (Default)
```bash
# Only fast-forward, no merges
git submodule foreach 'git pull --ff-only origin main'
```

### Aggressive
```bash
# Force update to remote HEAD (discards local changes)
git submodule foreach 'git reset --hard origin/main'
# ⚠️  USE WITH CAUTION: Loses uncommitted work
```

### Selective
```bash
# Update only specific submodules
git submodule update --remote _ARGUS _MYCEL
```

## Integration with Other Tools

### With Registry Sync
```
# After submodule sync:
1. Check component versions in submodules
2. Update registry.json with new versions
3. Run /registry-sync
```

### With GECO Auditor
```
# After sync, audit updated components:
Task(subagent_type="geco-auditor", component="_ARGUS")
```

### With CI/CD
```yaml
# .github/workflows/submodule-sync.yml
- name: Sync Submodules
  run: |
    git submodule update --remote --merge
    git add .
    git commit -m "chore: Auto-sync submodules" || true
    git push
```

## Safety Checks

Before syncing:
- [ ] Check for uncommitted changes in submodules
- [ ] Ensure no WIP branches active
- [ ] Verify CI is green on all submodules
- [ ] Check GECO compliance on updated components

After syncing:
- [ ] Run tests on root project
- [ ] Run tests on updated submodules
- [ ] Update VERSION_LOG.md if versions changed
- [ ] Update registry.json if needed
