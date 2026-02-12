# AURORA v0.2.0 — Workflow Diagram

## Three Workflows: Full, Quick, and Style Extraction

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        AURORA v0.2.0 WORKFLOWS                          │
└─────────────────────────────────────────────────────────────────────────┘

╔═══════════════════════════════════════════════════════════════════════╗
║                        1. FULL PROJECT WORKFLOW                        ║
║                     (Complete UX for new projects)                     ║
╚═══════════════════════════════════════════════════════════════════════╝

   /aurora-intake <project>
          │
          ├─ Read PRD
          ├─ Extract UX requirements
          └─ Output: specs/{project}/ux_requirements.md
          │
          ▼
   /aurora-mood <project>  ◄── NEW v0.2.0
          │
          ├─ Generate creative brief (personality, audience, constraints)
          ├─ User Checkpoint 1: Approve brief ✓
          ├─ Propose 5-7 visual references
          ├─ User Checkpoint 2: Approve references ✓
          ├─ Generate mood board + style direction
          ├─ Extract design tokens from references
          ├─ User Checkpoint 3: Approve mood board ✓
          └─ Output: creative_direction/mood_boards/{project}/
          │
          ▼
   /aurora-spec <project>
          │
          ├─ 7-pass UX analysis (informed by mood board)
          │  1. Mental Model Alignment
          │  2. Information Architecture
          │  3. Affordance & Action
          │  4. Progressive Disclosure
          │  5. System Feedback
          │  6. Interaction Patterns
          │  7. Accessibility (WCAG 2.1 AA)
          └─ Output: specs/{project}/ux_spec.md
          │
          ▼
   /aurora-build <project>
          │
          ├─ Translate UX spec into build order
          ├─ Reference mood board tokens
          └─ Output: specs/{project}/build_order.md (Figma Make prompts)
          │
          ▼
   /aurora-refine <project>
          │
          ├─ UX Eng Loop: Build → Review → Iterate
          ├─ User feedback integration
          └─ Working prototype
          │
          ▼
   Deploy
          │
          ├─ Finalize prototype
          ├─ Figma sync (if available)
          ├─ Document learnings
          └─ Output: specs/{project}/learnings.md


╔═══════════════════════════════════════════════════════════════════════╗
║                         2. QUICK TASK WORKFLOW                         ║
║                  (Single component, < 5 min turnaround)                ║
╚═══════════════════════════════════════════════════════════════════════╝

   /aurora-quick "Design a loading spinner for ARGUS dashboard"
          │
          ├─ Check design system for existing patterns
          ├─ Check brand kit for tokens (ARGUS/brand_tokens.json)
          ├─ Design component following AURORA principles
          ├─ Generate code (HTML/CSS/Streamlit/React)
          ├─ Document rationale + accessibility notes
          └─ Output: Instant response (no files)

   ✅ Use for: Single components, quick fixes, small enhancements
   ❌ Avoid for: New features, system-wide changes, multiple components


╔═══════════════════════════════════════════════════════════════════════╗
║                      3. STYLE EXTRACTION WORKFLOW                      ║
║              (Analyze successful sites, build reference library)       ║
╚═══════════════════════════════════════════════════════════════════════╝

   /aurora-extract-style https://linear.app
          │
          ├─ Fetch URL via WebFetch
          ├─ Analyze visual design
          │  ├─ Colors (primary, secondary, accent, neutrals, semantic)
          │  ├─ Typography (font families, scale, weights, line heights)
          │  ├─ Spacing (base unit, scale, grid system)
          │  ├─ Borders (radius values, border widths)
          │  └─ Shadows (elevation tokens)
          ├─ Identify interaction patterns
          │  ├─ Navigation (sidebar, top nav, command palette)
          │  ├─ Buttons (primary, secondary, ghost, sizes)
          │  ├─ Forms (input style, validation, error display)
          │  ├─ Data display (tables, cards, lists)
          │  └─ Feedback states (loading, empty, error, success)
          ├─ Document creative observations
          │  ├─ What makes this successful?
          │  ├─ Patterns to borrow
          │  └─ Patterns to avoid
          └─ Output: creative_direction/extracted_styles/linear/
             ├─ analysis.md (full analysis)
             ├─ tokens.json (design tokens)
             └─ observations.md (creative insights)


╔═══════════════════════════════════════════════════════════════════════╗
║                          WORKFLOW INTEGRATION                          ║
╚═══════════════════════════════════════════════════════════════════════╝

   Extract Styles          Build Library         Use in Mood Board
   ─────────────►          ─────────────►        ─────────────►
   /aurora-extract-style   Multiple sites        /aurora-mood
   (5 min/site)            extracted             (uses extracted tokens)
                           └─ Library: creative_direction/extracted_styles/


   Generate Mood Board     Inform Spec           Build Components
   ─────────────►          ─────────────►        ─────────────►
   /aurora-mood            /aurora-spec          /aurora-build
   (creative direction)    (uses mood board)     (uses tokens)


   Quick Task              Design System         Future Reuse
   ─────────────►          ─────────────►        ─────────────►
   /aurora-quick           Pattern saved         Reusable component
   (< 5 min)               in patterns/          in design system


╔═══════════════════════════════════════════════════════════════════════╗
║                          DECISION TREE                                 ║
╚═══════════════════════════════════════════════════════════════════════╝

   START: What do you need?
          │
          ├─ Single component or quick fix?
          │  └─ YES → /aurora-quick "<description>"
          │
          ├─ Learn from a successful site?
          │  └─ YES → /aurora-extract-style <url>
          │
          ├─ New project UX?
          │  └─ YES → Full workflow
          │           1. /aurora-intake
          │           2. /aurora-mood
          │           3. /aurora-spec
          │           4. /aurora-build
          │           5. /aurora-refine
          │
          └─ Just need creative direction?
             └─ YES → /aurora-mood <project>
                      (can skip intake if PRD is clear)


╔═══════════════════════════════════════════════════════════════════════╗
║                          FILE OUTPUTS                                  ║
╚═══════════════════════════════════════════════════════════════════════╝

creative_direction/
├── extracted_styles/{site}/     ← /aurora-extract-style
│   ├── analysis.md
│   ├── tokens.json
│   └── observations.md
│
├── mood_boards/{project}/       ← /aurora-mood
│   ├── creative_brief.md
│   ├── mood_board.md
│   └── references.json
│
└── learnings/
    ├── trends.md                ← Design trends (2026)
    ├── patterns.md              ← Successful patterns
    └── anti_patterns.md         ← What to avoid

specs/{project}/
├── ux_requirements.md           ← /aurora-intake
├── creative_direction.md        ← /aurora-mood (copy)
├── ux_spec.md                   ← /aurora-spec
├── build_order.md               ← /aurora-build
└── learnings.md                 ← Deploy phase

design_system/
├── master/                      ← 30% DNA (enforced)
│   └── tokens.json
└── brands/{project}/            ← 70% variation (from mood board)
    └── brand_tokens.json


╔═══════════════════════════════════════════════════════════════════════╗
║                          USER CHECKPOINTS                              ║
╚═══════════════════════════════════════════════════════════════════════╝

Full Workflow Checkpoints:
   1. Creative Brief Approval (personality, audience, constraints)
   2. Reference Selection Approval (5-7 sites with rationale)
   3. Mood Board Approval (complete style direction + tokens)
   4. UX Spec Approval (7-pass analysis)
   5. Build Order Approval (Figma prompts)
   6. Prototype Approval (working UI)

Quick Workflow Checkpoints:
   None (instant output, user reviews after)

Style Extraction Checkpoints:
   None (analysis output, user reviews after)


╔═══════════════════════════════════════════════════════════════════════╗
║                          KEY PRINCIPLES                                ║
╚═══════════════════════════════════════════════════════════════════════╝

1. Plan before building    — Skipping planning costs 10x in rework
2. Design systems first    — Reusable patterns over one-offs
3. 30/70 visual DNA        — 30% shared baseline, 70% brand variation
4. Creative direction      — Establish visual language BEFORE components
5. Accessibility first     — WCAG 2.1 AA minimum
6. Progressive disclosure  — Show complexity only when needed
7. User feedback           — Learn and improve from every interaction
8. Constitutional          — Validate against GAIA principles

```

---

## When to Use Each Workflow

| Workflow | When to Use | Time | Output |
|----------|-------------|------|--------|
| **Full Project** | New product UX, major feature | 2-4 hours | Complete UX spec + build order |
| **Quick Task** | Single component, quick fix | < 5 min | Component code + rationale |
| **Style Extraction** | Learn from successful site | 5-10 min | Design tokens + patterns |

---

## Example Session Timeline

```
Day 1: Build Reference Library (1 hour)
├─ /aurora-extract-style https://linear.app       (10 min)
├─ /aurora-extract-style https://notion.so        (10 min)
├─ /aurora-extract-style https://stripe.com/docs  (10 min)
├─ /aurora-extract-style https://vercel.com       (10 min)
└─ /aurora-extract-style https://ui.shadcn.com    (10 min)

Day 2: Generate Creative Direction (2 hours)
├─ /aurora-intake jseeker                         (20 min)
├─ /aurora-mood jseeker                           (60 min, 3 checkpoints)
└─ Review mood board with stakeholders            (40 min)

Day 3: UX Specification (3 hours)
├─ /aurora-spec jseeker                           (90 min, 7-pass analysis)
└─ Review spec with team                          (90 min)

Day 4: Build Order (2 hours)
├─ /aurora-build jseeker                          (60 min, Figma prompts)
└─ Review build order                             (60 min)

Day 5-7: Refine & Deploy
├─ /aurora-refine jseeker                         (iterative)
├─ Quick tasks during dev:
│  ├─ /aurora-quick "loading spinner"             (5 min)
│  ├─ /aurora-quick "empty state"                 (5 min)
│  └─ /aurora-quick "error toast"                 (5 min)
└─ Deploy prototype

Total: ~10 hours for complete UX from zero to prototype
```

---

**Version**: 0.2.0
**Last Updated**: 2026-02-11
