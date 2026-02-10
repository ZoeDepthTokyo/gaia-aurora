---
name: geco-status
description: GECO audit status dashboard and next action recommendations
disable-model-invocation: true
---

# GECO Status Dashboard

Quick overview of GECO audit progress (27 requirements) and actionable next steps.

## Usage
```
/geco-status [--priority high|medium|low] [--component <name>] [--verbose]
```

## Process

1. **Parse GECO Audit**
   ```bash
   cat GECO_AUDIT.md | grep -E "Status:|Priority:|Component:"
   ```

2. **Extract Metrics**
   - Total requirements: 27
   - Resolved count
   - Partial count
   - Remaining count
   - Completion percentage

3. **Categorize by Priority**
   - HIGH: Critical blockers
   - MEDIUM: Important but not blocking
   - LOW: Nice-to-have improvements

4. **Component Breakdown**
   - Per-component status (_ARGUS, _MYCEL, _VULCAN, etc.)
   - Missing implementations
   - Partially complete items

5. **Identify Next Actions**
   - Highest priority unresolved items
   - Low-hanging fruit (easy wins)
   - Blocked dependencies

## Output Format

### Summary View (Default)
```
GECO Audit Status (v0.5.2)
==========================

Progress: 10/27 (37%)
├── ✅ Resolved: 10
├── 🟡 Partial: 4
└── ⏳ Remaining: 13

By Priority:
├── 🔴 HIGH: 3 remaining
├── 🟡 MEDIUM: 7 remaining
└── 🟢 LOW: 3 remaining

Top 3 Next Actions:
1. [HIGH] Add CI/CD workflows for LOOM & MNEMIS
2. [HIGH] Implement test coverage gates (60-80%)
3. [MEDIUM] Complete pre-commit hooks for all repos

Components Requiring Attention:
- _LOOM: 0/5 GECO requirements met
- _MNEMIS: 1/5 GECO requirements met
- _ABIS: Planning phase (defer)
```

### Verbose View (--verbose)
```
GECO Audit Detailed Report
===========================

[GECO-001] ✅ RESOLVED
Requirement: Pre-commit hooks framework installed
Status: All 9 repos have .pre-commit-config.yaml
Components: _ARGUS, _MYCEL, _VULCAN, _WARDEN, _LOOM, _MNEMIS, _AURORA, _RAVEN, _ABIS

[GECO-004] ⏳ REMAINING (HIGH)
Requirement: TDD enforcement with coverage gates
Status: ONLY MYCEL has CI/CD with 80% minimum
Gap: Need CI for LOOM, MNEMIS, AURORA
Action: Create .github/workflows/ci.yml for each
Est. Time: 30 min per component

[GECO-009] 🟡 PARTIAL (HIGH)
Requirement: Test coverage thresholds (60-80%)
Status: MYCEL 92%, VULCAN 60%, others unknown
Gap: Need coverage reporting for all components
Action: Add pytest-cov to all test commands

...
```

### Component-Specific View (--component)
```
GECO Status: _ARGUS
===================

Requirements Met: 4/6 (67%)

✅ Pre-commit hooks installed
✅ CI/CD workflow configured
✅ Tests present (>50 files)
✅ CLAUDE.md exists

⏳ Coverage reporting missing
⏳ Mutation testing not configured

Next Actions for ARGUS:
1. Add pytest --cov flag to CI workflow
2. Configure coverage.py with 80% threshold
3. (Optional) Add mutmut for mutation testing
```

## Options

- `--priority <level>`: Filter by HIGH, MEDIUM, or LOW priority
- `--component <name>`: Focus on single component
- `--verbose`: Show detailed requirement breakdown
- `--json`: Output as JSON for automation
- `--next-actions`: Only show actionable next steps (top 5)

## Integration

### With GECO Auditor Subagent
```
/geco-status --component _LOOM
# Then launch geco-auditor subagent for detailed audit
```

### With CI/CD
```bash
# In GitHub Actions
claude -p "/geco-status --json" > geco_report.json
```

### With Planning
Use before sprint planning to prioritize GECO work.

## Quick Wins Identification

Automatically suggests "low-hanging fruit":
- Components with 1-2 small gaps
- Items that can be copy-pasted from working components
- Quick documentation updates

```
🍇 Quick Wins (Est. <1 hour each):
1. Copy CI workflow from MYCEL → LOOM (15 min)
2. Add CLAUDE.md to _RAVEN (30 min, use template)
3. Enable coverage reporting in VULCAN CI (10 min)
```
