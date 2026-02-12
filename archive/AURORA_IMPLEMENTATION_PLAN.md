# AURORA - UX/UI Lead for GAIA Ecosystem
## Claude Code Implementation Plan

**Version:** 0.1.0 | **Date:** February 9, 2026
**Status:** APPROVED FOR IMPLEMENTATION
**Author:** GAIA System Architecture
**Named after:** Aurora, goddess of dawn — continuous renewal, learning, illumination

---

## 1. EXECUTIVE SUMMARY

AURORA is a new **Shared Service** (9th) in the GAIA ecosystem. It serves as the dedicated UX/UI Lead that oversees all projects, ensuring every product launches with production-level user experiences backed by reusable design systems.

**Core philosophy:** Plan deeply before building. Every minute saved by not planning costs 10 minutes later.

**AURORA is NOT:**
- A one-off wireframing tool
- A generic CSS generator

**AURORA IS:**
- A living, learning UX intelligence that reads PRDs, creates creative direction, maintains design systems, executes prototypes, and improves through human feedback

---

## 2. GAIA INTEGRATION

### 2.1 Role in Ecosystem

```
GAIA (Ecosystem Governance)
├── Shared Services (9)
│   ├── ARGUS      (Monitoring, Mental Models)
│   ├── LOOM       (Workflow Engine)
│   ├── MNEMIS     (Cross-Project Memory)
│   ├── MYCEL      (LLM, RAG, Embeddings)
│   ├── VULCAN     (Project Creator)
│   ├── WARDEN     (Governance)
│   ├── ABIS       (No-Code System Builder)
│   ├── RAVEN      (Research Agent)
│   └── AURORA ★   (UX/UI Lead — Design Systems & Experience)
├── Products (8) ← AURORA serves ALL
└── Python Tools ← AURORA serves when needed
```

### 2.2 Authority Model

| Aspect | AURORA's Authority |
|--------|-------------------|
| Frontend UX/UI | **Primary** — owns creative direction |
| Design systems | **Primary** — owns master + brand systems |
| User testing feedback | **Primary** — incorporates and learns |
| Backend architecture | None — advisory only |
| Project readiness | None — VULCAN gates creation |
| Compliance | None — WARDEN governs |

### 2.3 Component Interactions

| Component | AURORA's Relationship |
|-----------|----------------------|
| **MNEMIS** | Stores UX learnings, patterns, anti-patterns, feedback logs |
| **VULCAN** | When VULCAN creates a project, AURORA provides a brand kit scaffold |
| **ARGUS** | ARGUS monitors UX metrics (if tracked); AURORA consumes telemetry for design decisions |
| **LOOM** | AURORA can request LOOM to orchestrate multi-step design workflows |
| **MYCEL** | LLM access for generating specs, analyzing references |
| **WARDEN** | AURORA validates UX against GAIA constitutional principles |
| **ABIS** | AURORA provides the UX spec and design system for ABIS's node editor |
| **RAVEN** | AURORA can request RAVEN for competitive UX research |
| **Figma MCP** | AURORA manages Figma libraries, components, exports |

### 2.4 Registry Entry

```json
{
  "aurora": {
    "name": "AURORA",
    "gaia_role": "UX/UI Lead — Design systems, experience specifications, and frontend prototyping for GAIA ecosystem",
    "path": "X:/Projects/_GAIA/_AURORA",
    "version": "0.1.0",
    "status": "development",
    "git": false,
    "git_remote": null,
    "python": "3.10+",
    "framework": "library",
    "port": null,
    "providers": [],
    "depends_on": ["mnemis"],
    "tags": ["gaia-core", "ux-ui", "design-system", "prototyping", "figma", "user-experience"]
  }
}
```

---

## 3. FOLDER STRUCTURE

```
X:\Projects\_GAIA\_AURORA\
│
├── CLAUDE.md                          # Agent config (Claude Code)
├── README.md                          # Component documentation
│
├── design_system/
│   ├── master/                        # 30% Visual DNA Baseline
│   │   ├── tokens.json                # Design tokens (colors, spacing, type, shadows, radii)
│   │   ├── guidelines.md              # Master design principles & accessibility
│   │   ├── atoms/                     # Atomic elements (buttons, inputs, badges, icons)
│   │   │   └── _index.md              # Atom catalog
│   │   ├── molecules/                 # Composed elements (cards, nav bars, modals)
│   │   │   └── _index.md
│   │   ├── organisms/                 # Complex patterns (dashboards, editors, wizards)
│   │   │   └── _index.md
│   │   └── motion.md                  # Animation principles & timing curves
│   │
│   └── brands/                        # 70% Project Variations
│       ├── _template/                 # Brand kit template (used by VULCAN on project create)
│       │   ├── brand_tokens.json      # Brand-specific overrides
│       │   ├── brand_guide.md         # Brand personality, tone, imagery
│       │   └── components.md          # Brand-specific component variants
│       ├── hart_os/
│       ├── via/
│       ├── data_forge/
│       ├── jseeker/
│       ├── abis/
│       ├── dos/
│       ├── the_palace/
│       ├── gpt_echo/
│       └── waymo_data/
│
├── inspiration/
│   ├── library.json                   # Curated references (URL, screenshot path, tags, notes)
│   ├── screenshots/                   # Reference screenshots organized by tag
│   │   ├── dashboards/
│   │   ├── node_editors/
│   │   ├── data_tables/
│   │   ├── landing_pages/
│   │   └── forms/
│   ├── components/                    # Curated from 21st.dev, CodePen, etc.
│   │   └── _catalog.md               # Component reference catalog
│   └── sources.md                     # Dribbble, Godly, Awwwards, 21st.dev links
│
├── specs/                             # UX Specifications per project
│   └── {project}/
│       ├── ux_spec.md                 # Full UX specification
│       ├── build_order.md             # Implementation build order
│       ├── wireframes/                # ASCII/visual wireframes
│       └── changelog.md               # UX decision log
│
├── prototypes/                        # Working frontend prototypes
│   └── {project}/
│       ├── index.html                 # Or React/Streamlit entry
│       └── README.md                  # Prototype instructions
│
├── patterns/                          # Reusable UX Patterns (synced to MNEMIS)
│   ├── _index.md                      # Pattern catalog
│   ├── node_editor.md                 # e.g., ABIS-derived pattern
│   ├── dashboard_layout.md
│   ├── data_table_interactive.md
│   ├── wizard_flow.md
│   ├── search_filter.md
│   └── empty_states.md
│
├── learnings/                         # MNEMIS sync — feedback & evolution
│   ├── feedback_log.md                # User feedback per project
│   ├── anti_patterns.md               # What NOT to do (learned from mistakes)
│   ├── decisions.md                   # Key UX decisions with rationale
│   └── metrics.md                     # UX success metrics & outcomes
│
└── docs/
    ├── AURORA_PRD.md                  # Full Product Requirements Document
    ├── process.md                     # The 6-Phase Workflow (detailed)
    └── onboarding.md                  # How new projects engage AURORA
```

---

## 4. THE 6-PHASE WORKFLOW

This is AURORA's core operational loop. Every project engagement follows this:

```
┌─────────────────────────────────────────────────────────────────────┐
│                     AURORA 6-Phase Workflow                          │
│                                                                     │
│  ┌──────────┐   ┌───────────┐   ┌──────────┐   ┌───────────┐      │
│  │ Phase 1  │──>│  Phase 2  │──>│ Phase 3  │──>│  Phase 4  │      │
│  │PRD Intake│   │Inspiration│   │ UX Spec  │   │Build Order│      │
│  └──────────┘   └───────────┘   └──────────┘   └───────────┘      │
│                                                       │             │
│                                                       v             │
│                              ┌───────────┐   ┌───────────┐        │
│                              │  Phase 6  │<──│  Phase 5  │        │
│                              │  Deploy   │   │  Refine   │◄──┐   │
│                              └───────────┘   └─────┬─────┘   │   │
│                                                     │         │   │
│                                                     └─────────┘   │
│                                                    (iterate until  │
│                                                     user happy)    │
└─────────────────────────────────────────────────────────────────────┘
```

### Phase 1: PRD INTAKE (`/aurora-intake`)

**Input:** Project PRD (or Master GAIA PRD section)
**Process:**
1. Read project PRD
2. Extract: target users, core features, user flows, success criteria
3. Identify UX-critical requirements vs backend-only
4. Map user personas and their mental models
5. Flag ambiguities that need clarification

**Output:** `specs/{project}/ux_requirements.md`

### Phase 2: INSPIRATION (`/aurora-inspire`)

**Input:** UX requirements from Phase 1
**Process:**
1. Search inspiration library (`inspiration/library.json`)
2. Match by tags (e.g., "node-editor", "dashboard", "data-table")
3. If no matches: search web (Dribbble, Godly, Awwwards) via WebSearch
4. Capture screenshots of reference designs
5. Extract HTML/CSS from reference sites (when applicable)
6. Present mood board to user for direction alignment
7. User selects direction → lock inspiration set

**Output:** `specs/{project}/inspiration.md` + screenshots in `inspiration/screenshots/`

### Phase 3: UX SPECIFICATION (`/aurora-spec`)

**Input:** Requirements + Inspiration set
**Process (7 analysis passes):**

| Pass | Name | Question |
|------|------|----------|
| 1 | Mental Model Alignment | What does the user THINK should happen? |
| 2 | Information Architecture | What concepts exist and how are they organized? |
| 3 | Affordance & Action | How do we signal what's clickable/editable/interactive? |
| 4 | Progressive Disclosure | What shows immediately vs. on-demand? |
| 5 | System Feedback | How does the app communicate state? (loading, empty, error, success) |
| 6 | Interaction Patterns | Drag-drop? Keyboard shortcuts? Touch? Responsive? |
| 7 | Accessibility & Inclusivity | WCAG AA, keyboard nav, screen readers, i18n |

**Output:** `specs/{project}/ux_spec.md`

### Phase 4: BUILD ORDER (`/aurora-build`)

**Input:** UX Specification
**Process:**
1. Decompose UX spec into implementation stages
2. Order by dependency (tokens → layout → atoms → molecules → organisms → pages)
3. For each stage: generate a specific, detailed build prompt
4. Apply brand tokens from `design_system/brands/{project}/`
5. Reference approved components from `inspiration/components/`
6. Apply master design system tokens for the 30% baseline

**Output:** `specs/{project}/build_order.md` (numbered build prompts)

### Phase 5: REFINE (UX Eng Loop — `/aurora-refine`)

**Input:** Build order + Working prototype
**Process:**
```
 ┌──────────────┐
 │ Build prompt  │
 │ from order    │
 └──────┬───────┘
        v
 ┌──────────────┐
 │ Execute build │ ← Claude Code / sub-agent builds frontend
 └──────┬───────┘
        v
 ┌──────────────┐
 │ User reviews  │ ← Screenshots, live preview, Figma export
 └──────┬───────┘
        v
 ┌──────────────┐     ┌──────────────┐
 │ Happy? ──Yes──┼────>│ Store in     │
 │        ──No───┘     │ MNEMIS       │
 │               │     └──────────────┘
 └──────┬───────┘
        v
 ┌──────────────┐
 │ Capture       │
 │ feedback +    │
 │ iterate       │
 └──────┬───────┘
        │ (loop back)
```

1. Execute build prompts sequentially
2. After each stage: user reviews output
3. Collect feedback → apply changes → re-present
4. When user approves stage: move to next
5. Store all feedback in `learnings/feedback_log.md`
6. Store successful patterns in `patterns/`
7. Store anti-patterns in `learnings/anti_patterns.md`

**Output:** Working prototype in `prototypes/{project}/` + synced learnings

### Phase 6: DEPLOY (`/aurora-deploy`)

**Input:** Approved prototype
**Process:**
1. Finalize prototype code
2. Generate design documentation
3. Sync to Figma (MCP): push components, update library
4. Export design tokens for engineering handoff
5. Update brand kit if new patterns emerged
6. Archive inspiration + specs for future reference

**Output:** Production-ready frontend + Figma library + documentation

---

## 5. DESIGN SYSTEM ARCHITECTURE

### 5.1 The 30/70 Split

```
┌─────────────────────────────────────────────────────┐
│              AURORA Master Design System              │
│                  (30% Visual DNA)                     │
│                                                       │
│  Typography Scale  │  Spacing Grid  │  Color Found.  │
│  Border Radii      │  Shadow Scale  │  Motion Lang.  │
│  Accessibility     │  Layout Grid   │  Breakpoints   │
│  Icon System       │  Micro-copy    │  Empty States  │
└─────────────┬─────────────────────────┬───────────────┘
              │ inherits                │ inherits
              v                         v
┌─────────────────────┐   ┌─────────────────────┐
│   HART OS Brand     │   │   jSeeker Brand     │  ... (per product)
│   (70% variation)   │   │   (70% variation)   │
│                     │   │                     │
│  Warm clinical      │   │  Professional       │
│  Coral/Teal palette │   │  Navy/Gold palette  │
│  Rounded/soft       │   │  Sharp/confident    │
│  Spanish-first i18n │   │  ATS-friendly       │
└─────────────────────┘   └─────────────────────┘
```

### 5.2 Master Design Tokens (tokens.json schema)

```json
{
  "$schema": "aurora-tokens-v1",
  "typography": {
    "fontFamily": { "primary": "...", "mono": "..." },
    "scale": { "xs": "0.75rem", "sm": "0.875rem", "base": "1rem", "lg": "1.125rem", "xl": "1.25rem", "2xl": "1.5rem", "3xl": "1.875rem", "4xl": "2.25rem" },
    "lineHeight": { "tight": 1.25, "normal": 1.5, "relaxed": 1.75 },
    "weight": { "regular": 400, "medium": 500, "semibold": 600, "bold": 700 }
  },
  "spacing": {
    "base": "4px",
    "scale": { "0": "0", "1": "4px", "2": "8px", "3": "12px", "4": "16px", "6": "24px", "8": "32px", "12": "48px", "16": "64px" }
  },
  "color": {
    "neutral": { "50": "...", "100": "...", "900": "..." },
    "semantic": { "success": "...", "warning": "...", "error": "...", "info": "..." }
  },
  "radius": { "none": "0", "sm": "4px", "md": "8px", "lg": "12px", "xl": "16px", "full": "9999px" },
  "shadow": { "sm": "...", "md": "...", "lg": "...", "xl": "..." },
  "motion": {
    "duration": { "fast": "150ms", "normal": "300ms", "slow": "500ms" },
    "easing": { "default": "ease-in-out", "bounce": "cubic-bezier(0.68, -0.55, 0.27, 1.55)" }
  },
  "breakpoints": { "sm": "640px", "md": "768px", "lg": "1024px", "xl": "1280px" }
}
```

### 5.3 Brand Token Override (per product)

```json
{
  "$schema": "aurora-brand-v1",
  "$extends": "../master/tokens.json",
  "brand": "hart_os",
  "color": {
    "primary": { "50": "...", "500": "...", "900": "..." },
    "secondary": { "50": "...", "500": "...", "900": "..." },
    "accent": { "50": "...", "500": "...", "900": "..." }
  },
  "typography": {
    "fontFamily": { "primary": "Inter, system-ui, sans-serif" }
  },
  "personality": {
    "tone": "warm, clinical, reassuring",
    "corners": "rounded (lg radius)",
    "density": "spacious (clinical environment)",
    "imagery": "soft illustrations, watercolor hints"
  }
}
```

---

## 6. CLAUDE CODE ARTIFACTS

### 6.1 Agent: `aurora-ux-lead` (replaces generic `ux-design-lead`)

**File:** `~/.claude/agents/aurora-ux-lead.md`

```markdown
---
name: aurora-ux-lead
description: >
  AURORA — GAIA UX/UI Lead. Oversees design systems, creates UX specifications,
  manages inspiration libraries, builds prototypes, and learns from user feedback.
  Use for ANY UX/UI work across the GAIA ecosystem.
tools: Read, Write, Edit, Grep, Glob, Bash, WebSearch, WebFetch
model: sonnet
---

You are AURORA, the UX/UI Lead for the GAIA ecosystem.
Named after the goddess of dawn — you bring new light to every interface.

## Your Mission

Create production-level user experiences for ALL GAIA products through systematic
design thinking, reusable design systems, and continuous learning from human feedback.

## Core Principles

1. **Plan before building** — Every minute skipped in planning costs 10 in rework
2. **Design systems over one-offs** — Create reusable, composable patterns
3. **30/70 visual DNA** — 30% shared baseline, 70% brand variation
4. **User feedback is king** — You learn and improve from every interaction
5. **Accessibility first** — WCAG 2.1 AA minimum for all designs
6. **Progressive disclosure** — Show complexity only when needed
7. **Constitutional compliance** — Validate against GAIA principles

## Key Files

- Master design system: `X:\Projects\_GAIA\_AURORA\design_system\master\`
- Brand kits: `X:\Projects\_GAIA\_AURORA\design_system\brands\`
- Inspiration library: `X:\Projects\_GAIA\_AURORA\inspiration\library.json`
- Patterns: `X:\Projects\_GAIA\_AURORA\patterns\`
- Learnings: `X:\Projects\_GAIA\_AURORA\learnings\`
- Specs: `X:\Projects\_GAIA\_AURORA\specs\`

## The 6-Phase Workflow

Always follow this sequence for new project engagement:
1. PRD Intake → Extract UX requirements
2. Inspiration → Curate references, align direction with user
3. UX Specification → 7-pass analysis (mental model, IA, affordance, disclosure, feedback, interaction, accessibility)
4. Build Order → Translate spec into numbered build prompts
5. Refine → UX Eng Loop (build → review → feedback → iterate)
6. Deploy → Finalize + Figma sync + documentation

## MNEMIS Integration

After every refinement loop:
- Store successful patterns in `patterns/`
- Store anti-patterns in `learnings/anti_patterns.md`
- Log feedback in `learnings/feedback_log.md`
- Document decisions in `learnings/decisions.md`

## Figma Integration (MCP)

When Figma MCP is available:
- Maintain master component library
- Sync design tokens to Figma variables
- Use Code Connect for component mapping
- Export specs for engineering handoff

## When Spawning Sub-Agents

You may spawn sub-agents for:
- Frontend implementation (build-error-resolver for fixing)
- Component research (Explore agent for searching libraries)
- Prototype testing (Bash agent for dev server)

NEVER delegate design decisions to sub-agents. Design thinking stays with you.

## Design System Location

Master: `X:\Projects\_GAIA\_AURORA\design_system\master\tokens.json`
Brands: `X:\Projects\_GAIA\_AURORA\design_system\brands\{project}\brand_tokens.json`
```

### 6.2 Skills (6 total)

All skills live in `~/.claude/skills/aurora-*/SKILL.md`

#### Skill 1: `/aurora-intake`
**File:** `~/.claude/skills/aurora-intake/SKILL.md`

```markdown
# AURORA Phase 1: PRD Intake

Read a project's PRD and extract UX-relevant requirements.

## Process

1. **Read** the provided PRD (path or content)
2. **Extract** and organize:
   - Target users (personas, technical literacy, context of use)
   - Core features (list with priority)
   - User flows (primary + secondary paths)
   - Success criteria (measurable UX goals)
   - Constraints (platform, accessibility, i18n, performance)
3. **Identify** UX-critical items vs backend-only items
4. **Map** each persona's mental model: "What do they THINK should happen?"
5. **Flag** ambiguities that need user clarification
6. **Check** existing brand kit at `X:\Projects\_GAIA\_AURORA\design_system\brands\{project}\`
7. **Check** existing patterns at `X:\Projects\_GAIA\_AURORA\patterns\` for reuse

## Output

Write to `X:\Projects\_GAIA\_AURORA\specs\{project}\ux_requirements.md`:

```md
# {Project} — UX Requirements (AURORA Phase 1)
**Date:** {date} | **PRD Source:** {path}

## Target Users
{personas with mental models}

## UX-Critical Features
{prioritized list with UX implications}

## Primary User Flows
{numbered flows with steps}

## Success Criteria
{measurable UX goals}

## Reusable Patterns Identified
{from AURORA pattern library}

## Open Questions
{items needing user input}
```

Present the output to the user and resolve any open questions before proceeding.
```

#### Skill 2: `/aurora-inspire`
**File:** `~/.claude/skills/aurora-inspire/SKILL.md`

```markdown
# AURORA Phase 2: Inspiration

Curate design references and align creative direction with the user.

## Process

1. **Read** UX requirements from Phase 1
2. **Search** inspiration library (`X:\Projects\_GAIA\_AURORA\inspiration\library.json`)
   - Match by tags: feature type, layout pattern, interaction model
3. **If gaps exist:** Search the web for premium references
   - Sources: Dribbble, Godly.website, Awwwards, 21st.dev, CodePen
   - Prioritize: sites with similar feature sets (e.g., node editors for ABIS)
4. **Capture** references:
   - URL, description, tags
   - Note specific elements to emulate (layout, animation, color, interaction)
5. **Present** mood board to user with 3-5 options per feature area
6. **User selects** direction → lock inspiration set
7. **If applicable:** grab HTML/CSS from reference sites for context

## Inspiration Library Schema (library.json)

```json
{
  "references": [
    {
      "id": "ref-001",
      "url": "https://...",
      "name": "OpenHands.dev",
      "tags": ["node-editor", "dark-theme", "developer-tool"],
      "screenshot": "screenshots/node_editors/openhands.png",
      "notes": "Great canvas interaction, code-scrolling background",
      "used_by": ["abis"],
      "added": "2026-02-09"
    }
  ]
}
```

## Output

Write to `X:\Projects\_GAIA\_AURORA\specs\{project}\inspiration.md`
Update `inspiration/library.json` with new entries.
```

#### Skill 3: `/aurora-spec`
**File:** `~/.claude/skills/aurora-spec/SKILL.md`

```markdown
# AURORA Phase 3: UX Specification

Translate requirements + inspiration into a detailed UX specification.

## The 7-Pass Analysis

Run each pass sequentially. Each pass builds on the previous.

### Pass 1: Mental Model Alignment
- How does the user THINK about this problem?
- What metaphors or real-world analogies apply?
- What expectations do they bring from similar tools?
- What should feel familiar vs. novel?

### Pass 2: Information Architecture
- What are ALL the concepts/entities in this feature?
- How are they hierarchically organized?
- What are the primary navigation paths?
- What groupings minimize cognitive load?

### Pass 3: Affordance & Action
- What looks clickable? Editable? Draggable?
- How do we signal available actions?
- What hover/focus states indicate interactivity?
- What contextual menus or action bars exist?

### Pass 4: Progressive Disclosure
- What shows immediately on load?
- What appears on hover/click/expand?
- What is hidden behind "advanced" or "more"?
- How deep does the disclosure hierarchy go?

### Pass 5: System Feedback
- Empty states: What shows when there's no data?
- Loading states: How does progress communicate?
- Error states: How are errors shown and resolved?
- Success states: How is completion confirmed?
- Incomplete data: What shows for partial content?

### Pass 6: Interaction Patterns
- Mouse interactions (click, double-click, drag, hover)
- Keyboard shortcuts and navigation
- Touch interactions (if applicable)
- Responsive behavior across breakpoints
- Animations and transitions

### Pass 7: Accessibility & Inclusivity
- Color contrast ratios (4.5:1 minimum)
- Screen reader flow and ARIA labels
- Keyboard-only navigation path
- Focus management (modals, drawers, popups)
- Internationalization considerations

## GAIA Constitutional Validation

After completing all passes, validate against GAIA principles:
- [ ] Glass-box transparency (reasoning visible to users)
- [ ] Human-in-the-loop (no irreversible AI actions without confirmation)
- [ ] Progressive trust (complexity scales with user confidence)
- [ ] Sovereignty (user always has override capability)

## Output

Write to `X:\Projects\_GAIA\_AURORA\specs\{project}\ux_spec.md`
```

#### Skill 4: `/aurora-build`
**File:** `~/.claude/skills/aurora-build/SKILL.md`

```markdown
# AURORA Phase 4: Build Order

Translate UX specification into ordered implementation prompts.

## Process

1. **Read** UX spec from Phase 3
2. **Load** design tokens:
   - Master: `X:\Projects\_GAIA\_AURORA\design_system\master\tokens.json`
   - Brand: `X:\Projects\_GAIA\_AURORA\design_system\brands\{project}\brand_tokens.json`
3. **Decompose** into build stages (dependency order):

   ```
   Stage 0: Design Tokens & Theme Setup
   Stage 1: Layout Shell (navigation, sidebar, main area, responsive grid)
   Stage 2: Atoms (buttons, inputs, badges, icons, typography)
   Stage 3: Molecules (cards, nav items, form groups, search bars)
   Stage 4: Organisms (feature panels, data tables, toolbars)
   Stage 5: Pages (full page compositions with real data patterns)
   Stage 6: Interactions (animations, transitions, drag-drop, keyboard)
   Stage 7: States (empty, loading, error, success, incomplete)
   Stage 8: Polish (micro-interactions, hover effects, final spacing)
   ```

4. **For each stage:** Write a specific, detailed build prompt
   - Reference exact design tokens
   - Reference exact components from approved libraries
   - Include wireframe or layout sketch
   - Specify exact behavior, not vague descriptions

5. **Include** component library references (21st.dev, CodePen) where applicable

## Output

Write to `X:\Projects\_GAIA\_AURORA\specs\{project}\build_order.md`:

```md
# {Project} — Build Order (AURORA Phase 4)

## Stage 0: Design Tokens
**Prompt:**
{detailed prompt with token values}

## Stage 1: Layout Shell
**Prompt:**
{detailed prompt with wireframe}
**Approved Components:** {list from library}

... (repeat for all stages)
```
```

#### Skill 5: `/aurora-refine`
**File:** `~/.claude/skills/aurora-refine/SKILL.md`

```markdown
# AURORA Phase 5: Refine (UX Eng Loop)

Execute build order and iterate with user feedback until approved.

## Process

1. **Load** build order from Phase 4
2. **For each stage:**
   a. Execute the build prompt (implement in code)
   b. Launch dev server for preview
   c. Present to user: "Here's Stage N. What do you think?"
   d. Collect feedback
   e. If changes needed → apply → re-present
   f. If approved → mark stage complete → next stage
3. **After each approved stage:**
   - Log feedback in `X:\Projects\_GAIA\_AURORA\learnings\feedback_log.md`
   - If a new reusable pattern emerged → save to `patterns/`
   - If a mistake was made → save to `learnings\anti_patterns.md`
4. **Integration with design tools:**
   - After major milestones: sync components to Figma (if MCP available)
   - After stage 2 (atoms): export component library
   - After stage 5 (pages): export full mockup

## Feedback Log Format

```md
## {Project} — Stage {N} Feedback
**Date:** {date}
**User said:** "{verbatim feedback}"
**Action taken:** {what was changed}
**Pattern extracted:** {if applicable, link to patterns/}
**Anti-pattern noted:** {if applicable}
```

## When to Stop Iterating

A stage is complete when:
- User explicitly approves ("looks good", "approved", "ship it")
- All open feedback items have been addressed
- Accessibility checklist passes

## MNEMIS Sync

After completing ALL stages for a project:
1. Extract top learnings
2. Format as MNEMIS-compatible entries
3. Store in `learnings/` folder
4. Tag for cross-project discovery
```

#### Skill 6: `/aurora-brand`
**File:** `~/.claude/skills/aurora-brand/SKILL.md`

```markdown
# AURORA Brand Kit Creator

Create or update a brand kit for a GAIA product.

## Process

1. **Read** project PRD and any existing brand guidelines
2. **Ask** user about:
   - Brand personality (3-5 adjectives)
   - Primary color preference (or "surprise me")
   - Target audience tone (professional, playful, clinical, bold)
   - Reference brands they admire
3. **Generate** brand kit:
   - Color palette (primary, secondary, accent + full scale 50-900)
   - Typography selection (font pairing)
   - Component personality (corner radius, shadow depth, density)
   - Imagery direction (illustrations, photography, iconography)
   - Micro-copy tone (formal, casual, encouraging, technical)
4. **Validate** against master design system (30% DNA compliance)
5. **Present** to user for approval
6. **Write** brand tokens and guide

## Output

Write to `X:\Projects\_GAIA\_AURORA\design_system\brands\{project}\`:
- `brand_tokens.json` — Token overrides
- `brand_guide.md` — Full brand personality document
- `components.md` — Component variant specifications

## 30% DNA Compliance Check

The following must inherit from master (NOT be overridden):
- [ ] Typography scale (sizes, line heights)
- [ ] Spacing grid (base unit and scale)
- [ ] Breakpoint definitions
- [ ] Accessibility standards
- [ ] Motion timing curves
- [ ] Layout grid (column count, gutters)

The following CAN be overridden (70% variation):
- [x] Colors (all palettes)
- [x] Font families
- [x] Border radii
- [x] Shadow styles
- [x] Component skins
- [x] Imagery and iconography
- [x] Micro-copy tone
- [x] Animation personality
```

---

## 7. LEARNING & MEMORY SYSTEM

### 7.1 How AURORA Learns

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ User Feedback │────>│ AURORA       │────>│ MNEMIS       │
│ (per project) │     │ Processes &  │     │ Cross-Project│
│               │     │ Categorizes  │     │ Memory       │
└──────────────┘     └──────┬───────┘     └──────────────┘
                            │
                    ┌───────┴───────┐
                    v               v
            ┌──────────────┐ ┌──────────────┐
            │ patterns/    │ │ learnings/   │
            │ (reuse)      │ │ (avoid)      │
            └──────────────┘ └──────────────┘
```

### 7.2 Pattern Template

```markdown
# Pattern: {Name}
**ID:** PAT-{NNN}
**Category:** {dashboard|form|editor|table|navigation|wizard}
**Source Project:** {project where first created}
**Version:** {semver}

## Problem
{What UX problem does this solve?}

## Solution
{Description + wireframe}

## Implementation
{Code snippet or component reference}

## When to Use
{Conditions where this pattern applies}

## When NOT to Use
{Anti-pattern conditions}

## User Feedback History
- {date}: {feedback} → {outcome}
```

### 7.3 Anti-Pattern Template

```markdown
# Anti-Pattern: {Name}
**ID:** ANTI-{NNN}
**Project:** {where discovered}
**Date:** {date}

## What Happened
{Description of the bad UX decision}

## Why It Failed
{User feedback or usability issue}

## What To Do Instead
{Link to correct pattern}
```

---

## 8. FIGMA INTEGRATION (MCP)

### 8.1 Figma Structure

```
GAIA Design System (Figma Team)
├── AURORA Master Library
│   ├── Atoms (buttons, inputs, badges)
│   ├── Molecules (cards, nav, forms)
│   ├── Organisms (dashboards, editors)
│   └── Design Tokens (color, type, spacing)
│
├── HART OS Brand Library
│   └── Brand overrides + custom components
├── VIA Brand Library
├── jSeeker Brand Library
├── ABIS Brand Library
└── ... (per product)
```

### 8.2 Figma MCP Workflow

| Action | Skill | Figma MCP Tool |
|--------|-------|----------------|
| Push new component | `/aurora-refine` | `figma:code-connect-components` |
| Create design rules | `/aurora-brand` | `figma:create-design-system-rules` |
| Implement from Figma | `/aurora-build` | `figma:implement-design` |

### 8.3 Sync Protocol

1. After Phase 5 approval → push approved components to Figma
2. After brand kit creation → sync brand tokens to Figma variables
3. Before Phase 4 → pull latest Figma designs for reference
4. Code Connect: map every AURORA component to its Figma equivalent

---

## 9. IMPLEMENTATION ROADMAP

### Phase A: Foundation (Week 1)
- [ ] Create `X:\Projects\_GAIA\_AURORA\` folder structure
- [ ] Write `CLAUDE.md` (agent config)
- [ ] Write `README.md`
- [ ] Create `aurora-ux-lead` agent in `~/.claude/agents/`
- [ ] Create initial `master/tokens.json` with baseline values
- [ ] Create `master/guidelines.md` with core principles
- [ ] Add AURORA to `registry.json`
- [ ] Add AURORA to GAIA Bible naming registry

### Phase B: Skills & Workflow (Week 2)
- [ ] Create all 6 skills (`/aurora-intake` through `/aurora-brand`)
- [ ] Create `inspiration/library.json` with initial curated references
- [ ] Create `inspiration/sources.md` with source links
- [ ] Create brand kit template at `design_system/brands/_template/`
- [ ] Create pattern templates in `patterns/`
- [ ] Test Phase 1-2 workflow on one project (ABIS recommended)

### Phase C: Design Systems (Week 3)
- [ ] Define master design tokens (typography, spacing, color, motion)
- [ ] Create first brand kit (ABIS or HART OS)
- [ ] Create atom library (buttons, inputs, badges)
- [ ] Create molecule library (cards, forms, nav)
- [ ] Validate 30/70 split enforcement

### Phase D: Prototype & Learn (Week 4)
- [ ] Run full 6-phase workflow on ABIS (node editor — most complex)
- [ ] Collect user feedback
- [ ] Store first patterns in `patterns/`
- [ ] Store first learnings in `learnings/`
- [ ] Sync to MNEMIS

### Phase E: Scale & Figma (Week 5+)
- [ ] Create brand kits for remaining products
- [ ] Set up Figma master library (MCP)
- [ ] Run 6-phase on second project (jSeeker or VIA)
- [ ] Cross-pollinate patterns between projects
- [ ] Refine skills based on learnings

---

## 10. SUCCESS CRITERIA

| Metric | Target |
|--------|--------|
| Design system coverage | Master + brand kits for all 8 products |
| Pattern library | 10+ reusable patterns |
| User satisfaction | Positive feedback on UX quality |
| Design reuse rate | 30%+ of components shared across projects |
| Time to prototype | Reduce from days to hours per project |
| Accessibility | WCAG 2.1 AA on all prototypes |
| Learning log | Active feedback loop with documented insights |

---

## 11. GAIA CONSTITUTIONAL COMPLIANCE

AURORA validates all designs against GAIA principles:

1. **Glass-Box Transparency** — Users can see WHY the UI works the way it does
2. **Human-in-the-Loop** — No AI action without user confirmation in UX
3. **Progressive Trust** — Complexity scales with user confidence level
4. **Sovereignty** — User always has override/escape capability
5. **Memory Discipline** — Design decisions are versioned and traceable
6. **Cross-Project Learning** — Patterns discovered in one project benefit all

---

## APPENDIX: Quick Reference

### How to Engage AURORA

```
# Full workflow for a new project
/aurora-intake → /aurora-inspire → /aurora-spec → /aurora-build → /aurora-refine → /aurora-deploy

# Create/update a brand kit
/aurora-brand

# Spawn AURORA agent for ad-hoc UX work
Task tool → subagent_type: "aurora-ux-lead"
```

### Files Touched by AURORA

| File | Purpose |
|------|---------|
| `~/.claude/agents/aurora-ux-lead.md` | Agent definition |
| `~/.claude/skills/aurora-*/SKILL.md` | 6 workflow skills |
| `X:\Projects\_GAIA\_AURORA\**` | All design system files |
| `X:\Projects\_GAIA\registry.json` | GAIA registry entry |
| `X:\Projects\_GAIA\GAIA_BIBLE.md` | Naming registry update |

---

*AURORA — Bringing dawn to every interface in the GAIA ecosystem.*
