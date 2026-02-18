---
name: orienting-to-component
description: "[OPENING] Provides instant orientation on any GAIA component — what it does, how to run it, current status, key files, and relevant skills. Use when starting work on an unfamiliar component, onboarding to GAIA, or needing a quick status summary. Triggers on: overview, orient, what is X, how do I start with, show me status. Why: prevents wasted time exploring unfamiliar components."
disable-model-invocation: false
---

# Component Overview

Provides instant orientation on any GAIA component - what it does, how to run it, current status, and where to start.

## Usage
```
/component-overview <component_name>
/component-overview --all [--status <filter>]
```

## Session Placement

This is an **[OPENING]** skill -- run it at the very start of a session when working on any GAIA component. It provides the context needed to make informed decisions before writing code.

Recommended opening sequence:
1. `/orienting-to-component <target>` -- understand what you're working with
2. `/creating-change <name>` -- if implementing a new feature
3. Begin implementation with full context

## Process

1. **Component Identification**
   - Read registry.json for component metadata
   - Load CLAUDE.md for detailed info
   - Check git status for current state

2. **Status Assessment**
   - Version number
   - Development status (production/active/development/planning)
   - Recent commits
   - Test coverage (if available)
   - Open issues/TODOs

3. **Quick Reference**
   - Setup commands
   - Launch commands
   - Test commands
   - Key files to know
   - Gotchas/warnings

4. **Integration Map**
   - Dependencies (what it needs)
   - Dependents (what needs it)
   - GAIA ecosystem role

## Output Format

Outputs include: status, description, quick start, key commands, key files, integration points, gotchas, current work, and constitutional compliance.

For full annotated examples (single component + all-components summary), see references/output-examples.md.

## Use Cases

### 1. New Developer Onboarding
```
/component-overview --all
# Get ecosystem map in 30 seconds
```

### 2. Before Editing a Component
```
/component-overview _VULCAN
# Quick refresh on role, setup, gotchas
```

### 3. Dependency Analysis
```
/component-overview _MYCEL
# See "Used by" to understand impact of changes
```

### 4. Sprint Planning
```
/component-overview --all --status development
# Focus on components under active development
```

## Integration

### With Explain-Code
```
/component-overview _ARGUS
/explain-code _ARGUS/subconscious/pattern_detector.py
```

### With GECO Status
```
/component-overview --all
/geco-status --component _LOOM
```

### With Registry Sync
```
/component-overview _WARDEN
# Check version before registry update
/registry-sync --component _WARDEN
```
