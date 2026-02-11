# AURORA — UX/UI Lead for GAIA Ecosystem

## Role
AURORA is the dedicated UX/UI Lead (Shared Service #9) in GAIA. It oversees design systems, creates UX specifications, manages inspiration libraries, builds prototypes, and learns from user feedback across ALL GAIA products.

Named after Aurora, goddess of dawn — continuous renewal, learning, illumination.

## Quick Start
1. Invoke agent: `claude --agent aurora-ux-lead`
2. Run intake: `/aurora-intake <project_name>`
3. Follow 6-phase workflow: intake → inspire → spec → build → refine → deploy
4. Access design system: `design_system/master/tokens.json`

## Setup & Launch

### Setup
```bash
# From GAIA root
cd /x/Projects/_GAIA/_AURORA

# Agent is in ~/.claude/agents/aurora-ux-lead.md (already available)
# Skills are in ~/.claude/skills/aurora-* (already available)

# Verify agent availability
claude agents list | grep aurora
```

### Usage
```bash
# Invoke agent directly
claude --agent aurora-ux-lead

# Or use skills from any context
/aurora-intake project-name
/aurora-inspire project-name
/aurora-spec project-name
/aurora-build project-name
/aurora-refine project-name
/aurora-deploy project-name
```

### Design System Access
```bash
# View master design tokens
cat design_system/master/tokens.json

# Create new brand kit (from template)
cp -r design_system/brands/_template design_system/brands/new-product

# View inspiration library
cat inspiration/library.json
```

## Directory Structure
```
_AURORA/
├── CLAUDE.md                     # This file
├── README.md                     # Component documentation
├── design_system/
│   ├── master/                   # 30% Visual DNA Baseline
│   │   ├── tokens.json           # Design tokens (colors, spacing, type, shadows, radii)
│   │   ├── guidelines.md         # Master design principles & accessibility
│   │   ├── atoms/_index.md       # Atomic elements catalog
│   │   ├── molecules/_index.md   # Composed elements catalog
│   │   ├── organisms/_index.md   # Complex patterns catalog
│   │   └── motion.md             # Animation principles
│   └── brands/                   # 70% Project Variations
│       ├── _template/            # Brand kit template (VULCAN uses on project create)
│       └── {product}/            # Per-product brand overrides
├── inspiration/                  # Curated design references
│   ├── library.json              # Reference catalog
│   ├── sources.md                # Dribbble, Godly, Awwwards links
│   ├── screenshots/              # Organized by tag
│   └── components/               # Curated component references
├── specs/{project}/              # UX specifications per project
├── prototypes/{project}/         # Working frontend prototypes
├── patterns/                     # Reusable UX patterns (synced to MNEMIS)
└── learnings/                    # Feedback, anti-patterns, decisions, metrics
```

## The 6-Phase Workflow
Every project engagement follows this sequence:
1. **PRD Intake** (`/aurora-intake`) — Extract UX requirements from PRD
2. **Inspiration** (`/aurora-inspire`) — Curate references, align direction
3. **UX Specification** (`/aurora-spec`) — 7-pass analysis
4. **Build Order** (`/aurora-build`) — Numbered implementation prompts
5. **Refine** (`/aurora-refine`) — UX Eng Loop (build → review → iterate)
6. **Deploy** (`/aurora-deploy`) — Finalize + Figma sync + docs

## 7-Pass UX Analysis (Phase 3)
1. Mental Model Alignment — What does the user THINK should happen?
2. Information Architecture — How are concepts organized?
3. Affordance & Action — How do we signal interactivity?
4. Progressive Disclosure — What shows immediately vs on-demand?
5. System Feedback — Empty, loading, error, success states
6. Interaction Patterns — Mouse, keyboard, touch, responsive
7. Accessibility — WCAG 2.1 AA, keyboard nav, screen readers

## Design System: 30/70 Split
- **30% Master DNA** (enforced): Typography scale, spacing grid, breakpoints, accessibility, motion timing, layout grid
- **70% Brand Variation** (per product): Colors, font families, border radii, shadows, component skins, imagery, tone

## Key Principles
1. Plan before building — every minute skipped costs 10 in rework
2. Design systems over one-offs — reusable, composable patterns
3. User feedback is king — learn and improve from every interaction
4. Accessibility first — WCAG 2.1 AA minimum
5. Progressive disclosure — show complexity only when needed
6. Constitutional compliance — validate against GAIA principles

## GAIA Constitutional Validation
All designs must satisfy:
- Glass-box transparency (reasoning visible to users)
- Human-in-the-loop (no irreversible AI actions without confirmation)
- Progressive trust (complexity scales with confidence)
- Sovereignty (user always has override capability)

## Integration Points
- **MNEMIS**: Stores UX learnings, patterns, anti-patterns, feedback logs
- **VULCAN**: Provides brand kit scaffold on project creation
- **ARGUS**: Consumes UX metrics/telemetry for design decisions
- **LOOM**: Orchestrates multi-step design workflows
- **MYCEL**: LLM access for spec generation and analysis
- **WARDEN**: UX validated against GAIA constitutional principles
- **RAVEN**: Competitive UX research on demand
- **Figma MCP**: Component library, design tokens, Code Connect

## Agent & Skills
- Agent: `aurora-ux-lead` (in `~/.claude/agents/`)
- Skills: `/aurora-intake`, `/aurora-inspire`, `/aurora-spec`, `/aurora-build`, `/aurora-refine`, `/aurora-brand`

## Gotchas
- **Agent-only workflows**: AURORA work must use the aurora-ux-lead agent, not general agents
- **30/70 enforcement**: Master tokens (30%) cannot be overridden in brand kits
- **Sequential phases**: Cannot skip phases in the 6-phase workflow (integrity check)
- **MNEMIS dependency**: UX learnings require MNEMIS to be configured
- **Figma sync**: Manual sync to Figma required (no auto-sync yet)
- **Brand kit naming**: Must match project name in registry.json exactly

## DO NOT
- Skip the 6-phase workflow for "quick" UI fixes
- Override master design tokens in brand kits (30% DNA is enforced)
- Deploy prototypes without user approval
- Delegate design decisions to sub-agents
