# Onboarding a New Project to AURORA

Step-by-step guide for engaging AURORA on a new GAIA product.

---

## Prerequisites

1. Project is registered in `X:\Projects\_GAIA\registry.json`
2. Project has a PRD or feature spec
3. AURORA master design system is initialized

---

## Steps

### Step 1: Check Existing Assets
- Brand kit: `design_system/brands/{project}/brand_tokens.json`
- Previous specs: `specs/{project}/`
- Relevant patterns: `patterns/_index.md`

### Step 2: Create Brand Kit (if none exists)
Run `/aurora-brand` to define brand personality, colors, and component personality.

### Step 3: Phase 1 — PRD Intake
```
/aurora-intake {path_to_prd}
```
Extracts UX requirements. Resolve all flagged ambiguities before proceeding.

### Step 4: Phase 2 — Inspiration
```
/aurora-inspire
```
Curates design references. Select creative direction before proceeding.

### Step 5: Phase 3 — UX Specification
```
/aurora-spec
```
Produces comprehensive UX spec through 7 analysis passes. Review and approve.

### Step 6: Phase 4 — Build Order
```
/aurora-build
```
Translates spec into ordered implementation prompts. Review before execution.

### Step 7: Phase 5 — Refine
```
/aurora-refine
```
Iterative build loop. Review each stage, provide feedback, approve to proceed.

### Step 8: Ship
Finalize code, sync to Figma, integrate into product, update metrics.

---

## Tips

1. **Be specific with feedback** — "spacing between cards too tight" beats "looks off"
2. **Reference inspirations** — "more like ref-008 (Linear)" gives clear direction
3. **Trust the phases** — skipping leads to rework
4. **Invest in Phase 3** — the UX spec is the most important document
5. **Iterate freely in Phase 5** — multiple feedback rounds are expected
