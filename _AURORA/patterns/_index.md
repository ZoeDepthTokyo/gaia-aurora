# AURORA UX Pattern Library

**Version:** 0.1.0 | **Last Updated:** February 9, 2026

Reusable UX patterns discovered across GAIA product engagements. Synced to MNEMIS for cross-project discovery.

---

## Catalog

| ID | Pattern Name | Category | Source Project | Status |
|----|-------------|----------|---------------|--------|
| PAT-001 | Dashboard Layout | layout | — | Planned |
| PAT-002 | Data Table Interactive | data-display | — | Planned |
| PAT-003 | Wizard/Stepper Flow | navigation | — | Planned |
| PAT-004 | Node Editor Canvas | editor | — | Planned |
| PAT-005 | Search and Filter Bar | navigation | — | Planned |
| PAT-006 | Empty State | feedback | — | Planned |
| PAT-007 | Settings Panel | form | — | Planned |
| PAT-008 | Command Palette | navigation | — | Planned |
| PAT-009 | Toast Notifications | feedback | — | Planned |
| PAT-010 | Card Grid | layout | — | Planned |

---

## Pattern Document Template

Each pattern, when implemented, gets its own file in this directory:

```markdown
# Pattern: {Name}
**ID:** PAT-{NNN}
**Category:** {layout | data-display | navigation | editor | form | feedback}
**Source Project:** {project where first created}
**Version:** {semver}

## Problem
{What UX problem does this solve?}

## Solution
{Description + wireframe or screenshot}

## Implementation
{Code snippet or component reference}

## When to Use
{Conditions where this pattern applies}

## When NOT to Use
{Anti-pattern conditions — link to learnings/anti_patterns.md}

## User Feedback History
- {date}: {feedback} -> {outcome}
```

---

## Categories

- **layout** — Page structure, grid, sidebar, content arrangement
- **data-display** — Tables, lists, charts, metrics
- **navigation** — Menus, breadcrumbs, search, filters, steppers
- **editor** — Canvas, node editors, form builders, rich text
- **form** — Input patterns, validation, settings, configuration
- **feedback** — Empty states, loading, errors, success, notifications
