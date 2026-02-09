# AURORA 6-Phase Process Reference

Detailed reference for each phase of the AURORA UX workflow. Every project engagement follows this sequence.

---

## Phase 1: PRD Intake

**Skill:** `/aurora-intake`
**Input:** Project PRD (path or content)
**Output:** `specs/{project}/ux_requirements.md`

### Process
1. Read the provided PRD
2. Extract: target users, core features, user flows, success criteria, constraints
3. Identify UX-critical items vs backend-only items
4. Map each persona's mental model: "What do they THINK should happen?"
5. Flag ambiguities that need user clarification
6. Check existing brand kit at `design_system/brands/{project}/`
7. Check existing patterns at `patterns/` for reuse opportunities

---

## Phase 2: Inspiration

**Skill:** `/aurora-inspire`
**Input:** UX requirements from Phase 1
**Output:** `specs/{project}/inspiration.md` + library updates

### Process
1. Search inspiration library (`inspiration/library.json`)
2. Match by tags (feature type, layout pattern, interaction model)
3. If gaps exist: search web (Dribbble, Godly, Awwwards, 21st.dev)
4. Capture references (URL, description, tags, specific elements to emulate)
5. Present mood board to user with 3-5 options per feature area
6. User selects direction — lock inspiration set
7. Grab HTML/CSS from reference sites when applicable

---

## Phase 3: UX Specification

**Skill:** `/aurora-spec`
**Input:** Requirements + locked inspiration set
**Output:** `specs/{project}/ux_spec.md`

### The 7-Pass Analysis

| Pass | Name | Core Question |
|------|------|--------------|
| 1 | Mental Model Alignment | What does the user THINK should happen? |
| 2 | Information Architecture | What concepts exist and how are they organized? |
| 3 | Affordance and Action | How do we signal what is clickable/editable/interactive? |
| 4 | Progressive Disclosure | What shows immediately vs on-demand? |
| 5 | System Feedback | How does the app communicate state? |
| 6 | Interaction Patterns | Mouse, keyboard, touch, responsive behavior? |
| 7 | Accessibility and Inclusivity | WCAG AA, keyboard nav, screen readers, i18n? |

---

## Phase 4: Build Order

**Skill:** `/aurora-build`
**Input:** UX Specification
**Output:** `specs/{project}/build_order.md`

### The 9-Stage Build Sequence

| Stage | Name | Description |
|-------|------|-------------|
| 0 | Design Tokens and Theme | Load master + brand tokens, set up theme |
| 1 | Layout Shell | Navigation, sidebar, main area, responsive grid |
| 2 | Atoms | Buttons, inputs, badges, icons, typography |
| 3 | Molecules | Cards, nav items, form groups, search bars |
| 4 | Organisms | Feature panels, data tables, toolbars |
| 5 | Pages | Full page compositions with real data patterns |
| 6 | Interactions | Animations, transitions, drag-drop, keyboard |
| 7 | States | Empty, loading, error, success, incomplete |
| 8 | Polish | Micro-interactions, hover effects, final spacing |

---

## Phase 5: Refine (UX Eng Loop)

**Skill:** `/aurora-refine`
**Input:** Build order + working prototype
**Output:** Working prototype + feedback logs + patterns

### Process
1. Execute each build stage prompt
2. Present to user for review
3. Collect feedback, apply changes, re-present
4. On approval: log feedback, extract patterns, note anti-patterns
5. Repeat until all stages approved

### Stage Completion Criteria
- User explicitly approves
- All open feedback items addressed
- Accessibility checklist passes

---

## Phase 6: Deploy

**Input:** Approved prototype
**Output:** Production frontend + Figma library + documentation

### Process
1. Finalize prototype code
2. Sync to Figma (MCP): push components, update library
3. Export design tokens for engineering handoff
4. Update brand kit if new patterns emerged

---

## GAIA Constitutional Validation

After completing all phases, validate:

- [ ] Glass-box transparency — Users can see WHY the UI works the way it does
- [ ] Human-in-the-loop — No AI action without user confirmation
- [ ] Progressive trust — Complexity scales with user confidence level
- [ ] Sovereignty — User always has override/escape capability
- [ ] Memory discipline — Design decisions are versioned and traceable
- [ ] Cross-project learning — Patterns discovered benefit all products
