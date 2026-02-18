# GAIA MANIFEST v1.0.4 — Last Updated: 2026-02-18

<!-- last_reconciled: 2026-02-18 -->
<!-- manifest_version: 1.0.4 -->

## Identity

GAIA is a constitutional AI governance framework orchestrating 18 projects (9 shared services + 8 products + 1 library) with glass-box transparency, human-in-the-loop controls, and progressive trust. It solves project fragmentation by providing unified architecture, shared intelligence (MYCEL), cross-project memory (MNEMIS), and runtime observability (ARGUS). Current ecosystem version: **v0.5.2**.

## Architecture (Three Pillars)

```
VULCAN (Create)  →  LOOM (Modify)  →  ARGUS (Monitor)
   The Forge         The Workbench       The Watchman
```

## Constitutional Constraints

1. **Glass-box transparency**: All agent logic must be inspectable; no opaque black boxes
2. **Human-in-Loop (HITL)**: Destructive operations require explicit user confirmation
3. **Progressive trust**: System complexity scales with user confidence
4. **Sovereignty**: Users can override any autonomous decision
5. **Memory tier boundaries**: Promotion follows AGENT → PROJECT → GAIA; never skip tiers
6. **Governance at design time**: Rules defined before execution, not discovered at runtime
7. **Three pillars**: VULCAN creates, LOOM modifies, ARGUS monitors — no overlap
8. **GECO compliance**: All components must satisfy 27 GECO requirements before production
9. **Cost accountability**: All LLM calls tracked, logged, attributed to component via MYCEL
10. **Immutable past**: Never rewrite commit history on main; destructive git ops require explicit request

## Component State Table

| Component | Version | Status | Type | Role | Dependencies | Last Changed |
|-----------|---------|--------|------|------|--------------|--------------|
| ARGUS | 0.7.0 | stable | Service | Monitor + Mental Models | mycel | 2026-02-17 |
| AURORA | 0.2.0 | dev | Service | UX/UI Lead | mnemis | 2026-02-12 |
| LOOM | 0.1.0 | dev | Service | Workflow Engine | mycel, mnemis | 2026-02-04 |
| MNEMIS | 0.1.0 | dev | Service | Cross-Project Memory | mycel | 2026-02-04 |
| MYCEL | 0.2.0 | active | Service | Shared Intelligence (RAG) | — | 2026-02-08 |
| VULCAN | 0.4.0-dev | dev | Service | Project Creator | mycel | 2026-02-08 |
| WARDEN | 0.3.1 | active | Service | Governance & Compliance | mycel | 2026-02-18 |
| RAVEN | 0.3.0 | active | Service | Research Agent | mycel, mnemis, argus | 2026-02-17 |
| ABIS | 0.0.1 | planning | Service | Visual System Builder | mycel, loom, argus, mnemis | 2026-02-09 |
| Mental Models | 1.0.0 | active | Library | Decision Support (59 models) | — | 2026-02-04 |
| GAIA Runtime | 1.1.0 | active | Service | Background Tasks + Skill Oracle | warden, argus, mnemis | 2026-02-18 |
| HART OS | 6.2.8 | prod | Product | Therapy Scoring | — | — |
| VIA Intelligence | 6.4 | prod | Product | Investment RAG | mycel | — |
| DATA FORGE | 1.1 | prod | Product | Data Processing | — | — |
| jSeeker | 0.2.1 | active | Product | Job Seeking + Resume | mycel | 2026-02-09 |
| GPT_ECHO | 0.1.0 | stale | Product | ChatGPT Archaeology | mycel | — |
| DOS | 0.0.1 | planning | Product | Multi-Agent Decisions | mycel, mnemis, argus | — |
| THE PALACE | 1.0 | complete | Product | Case Study (static) | — | — |

**Status legend**: prod = production, active = operational, dev = development, defined = spec only, planning = PRD only, stale = inactive, complete = done

## Active Priorities

1. Skill usability system live (v1.0): 16 skills, 4 hook scripts, 22 tests — proactive surfacing active
2. ARGUS: wire telemetry to MYCEL/VULCAN (stable v0.7.0, dashboard UX complete)
3. MNEMIS: activate first real memory entries, test promotion protocol
4. WARDEN: integrate compliance scan into CI pipeline (v0.3.1 subprocess fix applied)
5. Submodule CLAUDE.md updates: /running-autonomous-loop refs added to 7 components (pending submodule commits)

## Cascade Rules

When a component changes, the following upstream documents MAY need updating. Each rule has a permission tier: `auto` (applied by /reconciling-gaia without asking), `ask` (requires HITL approval), `block` (requires dedicated session).

### Universal Cascades (apply to ALL component changes)

- `registry.json`: version field update → **auto**
- `GAIA_MANIFEST.md`: component table row → **auto**
- `GECO_REVIEW_MATRIX.md`: component row if capabilities changed → **auto**

### Conditional Cascades

- `GAIA_PRD.md`: section update if new capability added → **ask**
- `VERSION_LOG.md`: new entry if version bumped → **ask**
- `GAIA_BIBLE.md`: modification → **block**
- Component deletion or architectural change → **block**

### Component-Specific Cascades

Each component CLAUDE.md contains a `<!-- CASCADE_MAP -->` section with component-specific cascade rules. The `/reconciling-gaia` skill reads these maps.

## Document Authority Map

| Topic | Authoritative Source | Fallback |
|-------|---------------------|----------|
| Architecture & principles | GAIA_BIBLE.md | MANIFEST |
| Component status & versions | GAIA_MANIFEST.md (this file) | registry.json |
| Governance requirements | GECO_AUDIT.md | GAIA_BIBLE.md |
| Version history | VERSION_LOG.md | registry.json |
| Product requirements | GAIA_PRD.md | GAIA_BIBLE.md |
| Component details | Component CLAUDE.md | MANIFEST table |
| Claude Code integration | GECO_REVIEW_MATRIX.md | Component CLAUDE.md |

## Reconciliation

Run `/reconciling-gaia` at end of each session to propagate changes. Use `--dry-run` to preview.

- **Last reconciled**: 2026-02-17
- **Reconciliation log**: `.gaia_reconcile_log`
- **Session changes**: `.gaia_changes` (auto-tracked by hooks)

## Benevolent Autonomy Tiers

| Tier | Permission | Examples |
|------|------------|----------|
| GREEN (auto) | Applied without asking | Registry version bump, MANIFEST table update, GECO checkmark |
| YELLOW (ask) | Requires user approval | PRD section update, VERSION_LOG entry, new dependency |
| RED (block) | Requires dedicated session | BIBLE modification, architecture change, component deletion |

---

*This is the canonical state document for GAIA. Updated by `/reconciling-gaia`, not manually.*
*Line budget: 116/250 max. Keep compact.*
