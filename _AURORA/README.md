# AURORA

**UX/UI Lead for the GAIA Ecosystem**

> Named after Aurora, goddess of dawn — bringing new light to every interface.

## Overview

AURORA is the 9th Shared Service in the GAIA ecosystem. It serves as the dedicated UX/UI Lead that oversees all products, ensuring every launch has production-level user experiences backed by reusable design systems.

**AURORA is NOT** a one-off wireframing tool or a generic CSS generator.

**AURORA IS** a living, learning UX intelligence that reads PRDs, creates creative direction, maintains design systems, executes prototypes, and improves through human feedback.

## Quick Start

```bash
# NEW v0.2.0: Quick workflows
/aurora-extract-style <url>         # Extract design tokens from successful sites
/aurora-mood <project>               # Generate creative brief + mood board
/aurora-quick "<description>"        # Single component design (< 5 min)

# Full workflow for a new project (via aurora-ux-lead agent)
# Agent handles: intake → mood → spec → build → refine → deploy

# Spawn AURORA agent for ad-hoc UX work
# Use Task tool → subagent_type: "aurora-ux-lead"
```

## The 6-Phase Workflow

Phases are executed by the `aurora-ux-lead` agent (not standalone skills):

| Phase | Agent Step | Input | Output |
|-------|-----------|-------|--------|
| 1. PRD Intake | Intake | Project PRD | `specs/{project}/ux_requirements.md` |
| 2. Inspiration | Mood/Inspire | UX requirements | `specs/{project}/inspiration.md` |
| 3. UX Spec | Spec | Requirements + Inspiration | `specs/{project}/ux_spec.md` |
| 4. Build Order | Build | UX Specification | `specs/{project}/build_order.md` |
| 5. Refine | Refine | Build order + prototype | Working prototype |
| 6. Deploy | manual | Approved prototype | Production frontend |

## Design System Architecture

### 30/70 Split

- **30% Master DNA** — Shared baseline across all GAIA products (typography scale, spacing grid, breakpoints, accessibility standards, motion timing, layout grid)
- **70% Brand Variation** — Per-product identity (colors, font families, border radii, shadows, component skins, imagery, micro-copy tone)

### Atomic Design Hierarchy

```
Tokens → Atoms → Molecules → Organisms → Pages
```

- **Tokens**: `design_system/master/tokens.json`
- **Atoms**: Buttons, inputs, badges, icons
- **Molecules**: Cards, nav bars, form groups, search bars
- **Organisms**: Dashboards, editors, wizards, data tables

## GAIA Integration

| Component | Relationship |
|-----------|-------------|
| MNEMIS | Stores UX learnings and patterns |
| VULCAN | AURORA provides brand kit scaffold on project creation |
| ARGUS | AURORA consumes telemetry for design decisions |
| LOOM | Orchestrates multi-step design workflows |
| MYCEL | LLM access for generating specs |
| WARDEN | AURORA validates UX against GAIA principles |
| ABIS | AURORA provides UX spec for node editor |
| RAVEN | Competitive UX research |
| Figma MCP | Component libraries, design tokens, Code Connect |

## Version

- **Current**: 0.2.0 (Creative Direction System)
- **Status**: Development (Phase A + Creative Intelligence complete)
- **Python**: 3.10+
- **Framework**: Library (design system + specifications)

## What's New in v0.2.0

**Creative Direction System** — AURORA now has systematic creative intelligence:
1. **Style Extraction** (`/aurora-extract-style`) — Analyze successful sites, extract design tokens
2. **Mood Boards** (`/aurora-mood`) — Generate creative briefs and visual direction
3. **Quick Tasks** (`/aurora-quick`) — Single component design in < 5 minutes

See `QUICK_START_v0.2.0.md` for usage guide.

## License

Part of the GAIA ecosystem. Internal use only.
