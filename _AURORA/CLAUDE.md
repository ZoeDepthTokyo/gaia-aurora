# AURORA — UX/UI Lead for GAIA Ecosystem

> **Context**: Read `GAIA_MANIFEST.md` first for ecosystem state.
> This component is part of the GAIA ecosystem. See cascade rules below.

## Role
AURORA is the dedicated UX/UI Lead (Shared Service #9) in GAIA. It oversees design systems, creates UX specifications, manages inspiration libraries, builds prototypes, and learns from user feedback across ALL GAIA products.

Named after Aurora, goddess of dawn — continuous renewal, learning, illumination.

## Quick Start
1. Extract styles: `/aurora-extract-style <url>` — Learn from successful sites
2. Generate mood board: `/aurora-mood <project>` — Creative brief + visual direction
3. Quick design: `/aurora-quick "<description>"` — Single component in < 5 min
4. Full workflow: Use `aurora-ux-lead` agent for intake → mood → spec → build → refine
5. Access design system: `design_system/master/tokens.json`

**Version:** v0.2.0
**Status:** Development
**GAIA Role:** Shared Service #9 (UX/UI)

**New in v0.2.0**: Creative Direction System (style extraction, mood boards, quick tasks)

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
# Invoke agent directly (handles full 6-phase workflow)
claude --agent aurora-ux-lead

# Standalone skills (work from any context)
/aurora-extract-style <url>        # Extract design tokens from a site
/aurora-mood <project>              # Generate creative brief + mood board
/aurora-quick "<description>"       # Single component design (< 5 min)
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
Every project engagement follows this sequence (via `aurora-ux-lead` agent):
1. **PRD Intake** — Extract UX requirements from PRD
2. **Inspiration** — Curate references, align direction (`/aurora-mood` for creative brief)
3. **UX Specification** — 7-pass analysis
4. **Build Order** — Numbered implementation prompts
5. **Refine** — UX Eng Loop (build → review → iterate)
6. **Deploy** — Finalize + Figma sync + docs

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
- Agent: `aurora-ux-lead` (in `~/.claude/agents/`) — handles full 6-phase workflow
- Skills: `/aurora-extract-style`, `/aurora-mood`, `/aurora-quick` (standalone convenience skills)

## Gotchas
- **Workflow selection**: Use `/aurora-quick` for single components (< 5 min), `/aurora-mood` for creative direction, full 6-phase for complete projects
- **Style extraction first**: Build reference library with `/aurora-extract-style` on 5-10 sites before generating mood boards
- **Mood board checkpoints**: 3 user approvals required (brief, references, final) - don't skip them
- **Creative direction location**: All files in `creative_direction/` (extracted_styles, mood_boards, learnings)
- **Agent-only workflows**: AURORA work must use the aurora-ux-lead agent, not general agents
- **30/70 enforcement**: Master tokens (30%) cannot be overridden in brand kits
- **Sequential phases**: Cannot skip phases in the 6-phase workflow (integrity check)
- **MNEMIS dependency**: UX learnings require MNEMIS to be configured
- **Figma sync**: Manual sync to Figma required (no auto-sync yet)
- **Brand kit naming**: Must match project name in registry.json exactly

## Relevant Skills
- `/creating-change` — before implementing any new feature
- `/auditing-ux` — when reviewing design decisions or UX patterns
- `/reviewing-design` — before finalizing any component or spec
- `/checking-accessibility` — during Phase 7 (Accessibility) of UX analysis
- `/reconciling-gaia` — end of every session
- `/running-autonomous-loop` — for batch design token or template updates

## DO NOT
- Skip the 6-phase workflow for "quick" UI fixes
- Override master design tokens in brand kits (30% DNA is enforced)
- Deploy prototypes without user approval
- Delegate design decisions to sub-agents

## Testing Specifications

Coverage target: 70%

### Requirement: Style Extraction
The system MUST extract a complete set of design tokens (colors, typography, spacing) from a target URL.

#### Scenario: Successful style extraction
- GIVEN a valid URL pointing to a live website
- WHEN `/aurora-extract-style <url>` is invoked
- THEN a JSON file is written to `creative_direction/extracted_styles/` containing at minimum primary color, font families, and spacing scale

#### Scenario: Extraction preserves source provenance
- GIVEN a URL is extracted
- WHEN the tokens file is written
- THEN it includes the source URL, extraction timestamp, and token count metadata

---

### Requirement: Mood Board Generation
The system MUST generate a structured creative brief and visual direction through 3 user-approval checkpoints.

#### Scenario: Checkpoint gating enforced
- GIVEN a mood board is initiated via `/aurora-mood <project>`
- WHEN the user does not approve checkpoint 1 (brief)
- THEN the workflow pauses at that checkpoint and does not advance to checkpoint 2 (references)

#### Scenario: Mood board produces design token output
- GIVEN a project with an existing brand kit path
- WHEN all 3 checkpoints are approved
- THEN a `mood_board.json` file is written to `creative_direction/mood_boards/<project>/` with palette, typography, and mood keywords

---

### Requirement: Quick Component Design
The system MUST produce a single-component design spec in under 5 minutes without requiring the full 6-phase workflow.

#### Scenario: Quick task completes without mood board
- GIVEN a component description is provided to `/aurora-quick`
- WHEN no existing mood board exists for the project
- THEN the system uses master tokens as fallback and produces a spec without blocking

---

### Requirement: Master Token Enforcement
The system MUST prevent brand kits from overriding 30% master DNA tokens.

#### Scenario: Override attempt is blocked
- GIVEN a brand kit file attempts to set a spacing scale value that conflicts with `master/tokens.json`
- WHEN the brand kit is validated
- THEN an error is raised identifying the conflicting key and referencing the master token path

---

### Requirement: 6-Phase Workflow Integrity
The system MUST enforce sequential phase execution — phases cannot be skipped.

#### Scenario: Phase skip attempt is blocked
- GIVEN a workflow instance is in Phase 2 (Inspiration)
- WHEN a caller attempts to invoke Phase 4 (Build Order) directly
- THEN the workflow raises an integrity violation and returns the current phase state

---

### Requirement: MNEMIS Pattern Storage
The system MUST store approved UX patterns to MNEMIS at PROJECT tier after the refine phase.

#### Scenario: Pattern stored with provenance
- GIVEN Phase 5 (Refine) completes with user approval
- WHEN a reusable pattern is identified
- THEN `MnemisWorkflowBridge.store_agent_output_to_memory()` is called with scope=PROJECT and source attribution matching the AURORA session

## When I Change
<!-- CASCADE_MAP: machine-readable, do not edit manually -->
- registry.json: version field → auto
- GAIA_MANIFEST.md: component table row → auto
- GECO_REVIEW_MATRIX.md: component row → auto
- GAIA_PRD.md: Section 4.8 (UX/Design) → ask
- VERSION_LOG.md: new entry → ask
<!-- END_CASCADE_MAP -->
