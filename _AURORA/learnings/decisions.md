# AURORA Design Decisions

Key UX decisions with rationale, context, and outcome tracking. Decisions are numbered sequentially and never deleted — only superseded.

---

## Template

```markdown
## DEC-{NNN}: {Decision Title}
**Date:** {date}
**Project:** {project}
**Context:** {what prompted the decision}
**Decision:** {what was decided}
**Rationale:** {why}
**Alternatives Considered:** {what else was considered}
**Outcome:** {result — updated after implementation}
```

---

## DEC-001: 30/70 Design System Split

**Date:** 2026-02-09
**Project:** AURORA (ecosystem-wide)
**Context:** Need to balance cross-project consistency with per-product brand identity. 8 products with different audiences, tones, and purposes must feel like a family without looking identical.
**Decision:** 30% shared visual DNA (enforced by master tokens), 70% brand variation (per product brand kits).
**Rationale:** Full uniformity kills brand personality — HART OS (warm, clinical) cannot look like DATA FORGE (technical, dense). Full freedom kills ecosystem coherence — no shared patterns, no reusability. 30/70 provides recognizable family resemblance while allowing distinct identities.
**Alternatives Considered:**
- 50/50 split — too restrictive, brands feel constrained
- No split — chaos, every product diverges completely
- Theme-only (colors only) — insufficient variation for different densities, corners, imagery
**Outcome:** Pending validation with first brand kit implementation.

## DEC-002: Atomic Design Hierarchy

**Date:** 2026-02-09
**Project:** AURORA (ecosystem-wide)
**Context:** Need a systematic approach to component organization that scales across 8+ products.
**Decision:** Adopt Atomic Design methodology (tokens, atoms, molecules, organisms, pages).
**Rationale:** Industry-proven hierarchy that maps cleanly to design systems. Clear boundaries between composition levels. Easy to identify what's reusable vs. product-specific.
**Alternatives Considered:**
- Flat component library — no hierarchy, harder to find/reuse
- Feature-based organization — groups by feature, not composability
- BEM-style — CSS naming convention, not a design system architecture
**Outcome:** Pending validation.
