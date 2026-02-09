# AURORA

**UX/UI Lead for the GAIA Ecosystem**

> Named after Aurora, goddess of dawn — bringing new light to every interface.

## Overview

AURORA is the 9th Shared Service in the GAIA ecosystem. It serves as the dedicated UX/UI Lead that oversees all products, ensuring every launch has production-level user experiences backed by reusable design systems.

**AURORA is NOT** a one-off wireframing tool or a generic CSS generator.

**AURORA IS** a living, learning UX intelligence that reads PRDs, creates creative direction, maintains design systems, executes prototypes, and improves through human feedback.

## Quick Start

```bash
# Full workflow for a new project
/aurora-intake → /aurora-inspire → /aurora-spec → /aurora-build → /aurora-refine

# Create/update a brand kit
/aurora-brand

# Spawn AURORA agent for ad-hoc UX work
# Use Task tool → subagent_type: "aurora-ux-lead"
```

## The 6-Phase Workflow

| Phase | Skill | Input | Output |
|-------|-------|-------|--------|
| 1. PRD Intake | `/aurora-intake` | Project PRD | `specs/{project}/ux_requirements.md` |
| 2. Inspiration | `/aurora-inspire` | UX requirements | `specs/{project}/inspiration.md` |
| 3. UX Spec | `/aurora-spec` | Requirements + Inspiration | `specs/{project}/ux_spec.md` |
| 4. Build Order | `/aurora-build` | UX Specification | `specs/{project}/build_order.md` |
| 5. Refine | `/aurora-refine` | Build order + prototype | Working prototype |
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

- **Current**: 0.1.0
- **Status**: Development (Phase A complete)
- **Python**: 3.10+
- **Framework**: Library (design system + specifications)

## License

Part of the GAIA ecosystem. Internal use only.
