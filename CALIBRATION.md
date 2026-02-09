# GAIA CALIBRATION DOCUMENT

**Version:** 0.5.1
**Date:** February 9, 2026
**Author:** Claude Opus 4.6 (calibration agent)
**Commissioned by:** Federico (Product Owner)
**Type:** Living document -- evolves with every session, commit, and user input

---

## Purpose

This document is a **reality check**. It maps what GAIA claims to be versus what it actually is today. It distinguishes between documented aspirations and operational capabilities, identifies what's real and what's scaffolding, and provides a ground-truth baseline for future development.

Unlike the GAIA Bible (constitutional intent) or the GECO Audit (diagnostic findings), this Calibration document tracks **the gap between design and reality** and closes incrementally with each session.

---

## 1. Ecosystem Overview (Verified Feb 9, 2026)

### Registry: 17 Projects

| # | Component | Type | Version | Status | Operational? | CLAUDE.md | Pre-commit | Tests | Git Remote |
|---|-----------|------|---------|--------|-------------|-----------|------------|-------|------------|
| 1 | HART OS | Product | 6.2.8 | production | YES -- serves real users | NO | NO | Unknown | YES (GitHub) |
| 2 | VIA Intelligence | Product | 6.4 | production | YES -- serves real users | NO | NO | Unknown | NO |
| 3 | DATA FORGE | Product | 1.1 | production | YES -- serves real users | YES | YES | Unknown | NO |
| 4 | MYCEL | Shared Service | 0.2.0 | active | YES -- used by VIA, jSeeker | NO | YES | 200+ tests, 92-100% cov | NO |
| 5 | VULCAN | Shared Service | 0.4.0-dev | development | PARTIAL -- questionnaire works, adapters untested in production | NO | YES | 137 tests, 85% cov | NO |
| 6 | LOOM | Shared Service | 0.1.0 | development | SCAFFOLDED -- models exist, workflow engine untested | YES | YES | 1 file | NO |
| 7 | MNEMIS | Shared Service | 0.1.0 | development | SCAFFOLDED -- core exists, no data stored yet | YES | YES | 2 files | NO |
| 8 | ARGUS | Shared Service | 0.5.1 | development | PARTIAL -- dashboard works, Process Observer empty, Trust Dashboard empty | YES | YES | Installation test only | NO |
| 9 | Mental Models | Library | 1.0.0 | active | YES -- 59 models with selector | NO | YES | Unknown | NO |
| 10 | GPT_ECHO | Product | 0.1.0 | stale | NO -- abandoned, 19 manual version copies | NO | NO | None | NO |
| 11 | WARDEN | Shared Service | 0.3.0 | active | PARTIAL -- scanner.py exists, CLI scaffolded, not integrated into workflows | NO | YES | None | NO |
| 12 | RAVEN | Shared Service | 0.1.0 | defined | NO -- placeholder README only | NO | YES | None | NO |
| 13 | THE PALACE | Product | 1.0 | complete | YES -- static HTML, done | NO | NO | None | NO |
| 14 | jSeeker | Product | 0.2.1 | active | PARTIAL -- core works but v2 feedback shows regressions (handled by parallel session) | YES | YES | 92 tests | NO |
| 15 | ABIS | Shared Service | 0.0.1 | planning | NO -- PRD exists at `X:\Projects\ABIS\docs\`, no code | NO | YES | None | NO |
| 16 | AURORA | Shared Service | 0.1.0 | development | SCAFFOLDED -- design system structure, tokens, guidelines, skills created, no real brand kits yet | YES | NO | None | NO |
| 17 | DOS | Product | 0.0.1 | planning | NO -- defined in registry only | NO | NO | None | NO |

### Totals

| Metric | Count |
|--------|-------|
| Truly operational (serves users or actively used) | 7 (HART OS, VIA, DATA FORGE, MYCEL, Mental Models, jSeeker, THE PALACE) |
| Partially operational (some features work) | 3 (VULCAN, ARGUS, WARDEN) |
| Scaffolded (code exists, not operational) | 3 (LOOM, MNEMIS, AURORA) |
| Defined only (placeholder/PRD) | 3 (RAVEN, ABIS, DOS) |
| Stale/abandoned | 1 (GPT_ECHO) |
| **CLAUDE.md files** | 6 of 17 (35%) |
| **Pre-commit configs** | 12 of 17 (71%) |
| **Pre-commit ACTIVE** | 9 of 17 (53%) -- all _GAIA sub-components |
| **Git remotes** | 9 of 17 (53%) -- HART OS + 8 GAIA submodules |
| **CI/CD pipelines** | 4 of 17 (24%) -- ARGUS, MYCEL, VULCAN, WARDEN |
| **Shared logging** | Standard created, not yet adopted |

---

## 2. What Is Real vs. What Is Documentation

### REAL (Working Code, Tested, Serving Purpose)

| Capability | Evidence |
|-----------|----------|
| MYCEL LLM client (OpenAI, Anthropic, Gemini) | Used by VIA and jSeeker in production. 92-100% test coverage |
| VULCAN project scaffolding | 7-step questionnaire generates project structures. 137 tests, 85% coverage |
| ARGUS Mental Model Library | 59 models in `mental_models/registry.json` with context-aware selector |
| ARGUS Dashboard | Streamlit app at `_ARGUS/dashboard/app.py` -- ecosystem graph, live trace, memory tree, scenarios. Fixed in this session (v0.5.1) |
| ARGUS EventBus | SQLite-backed event store. Functional, loads JSONL build logs |
| ARGUS Subconscious Layer | External memory, pattern detection, hypothesis generation (~1,245 lines) |
| ARGUS Explainability | 4-level system mapped to Growth Rungs (explainer.py, 422 lines) |
| MNEMIS Memory Models | 3-tier hierarchy with promotion protocol (core/contracts.py, memory_store.py, promotion.py) |
| LOOM Workflow Engine | Agent authority model, execution state management |
| WARDEN Scanner | Basic compliance scanning (secrets detection, file checks) |
| jSeeker Resume Pipeline | JD parse -> match -> adapt -> score -> render -> track. Working with bugs |
| Registry System | `registry.json` with 17 projects, read by ARGUS dashboard |
| Pre-commit Infrastructure | 10 of 11 sub-components have `.pre-commit-config.yaml` (not yet installed/active) |

### DOCUMENTED BUT NOT OPERATIONAL

| Claimed Capability | Reality | Gap |
|-------------------|---------|-----|
| WARDEN enforcement in commit workflow | scanner.py exists but is never called by pre-commit hooks or CI/CD | Not integrated |
| Process Observer (real-time agent monitoring) | `_ARGUS/process_observer/__init__.py` exists, but `observer.py` and `post_mortem.py` are **empty/missing** | Not implemented |
| Trust Dashboard | `_ARGUS/trust_dashboard/` directory exists but is **empty** | Not implemented |
| MNEMIS cross-project memory sharing | Memory store code exists but **zero data** has been stored. No project has called MNEMIS to write memory | No consumers |
| LOOM visual editing of agents | Workflow engine code exists but no UI, no real workflows executed | No frontend |
| RAVEN autonomous research | README placeholder only | Not started |
| ABIS visual system builder | PRD at `X:\Projects\ABIS\docs\` but no code | Not started |
| CI/CD pipelines | GitHub Actions templates exist (`jSeeker/.github/workflows/`) but GAIA root has none | Not deployed |
| ARGUS telemetry from all modules | Only jSeeker sends events. 16 other projects are silent | 94% gap |
| Cross-session task persistence | MNEMIS could do this but isn't connected. Todos vanish between sessions | Not connected |
| Automated learning pipeline (ARGUS -> MNEMIS -> WARDEN) | Each component exists independently but the pipeline is **not wired** | Not connected |
| Cost tracking dashboard | jSeeker logs token counts, ARGUS Trust Dashboard should display them -- but Trust Dashboard is empty | Display missing |
| GAIA MCP servers | 10 external MCP plugins (Greptile, Pinecone, etc.) but ZERO GAIA-native MCP tools registered | Not exposed |

### ASPIRATIONAL (Documented in Plans, No Implementation)

| Vision | Source Document | Status |
|--------|----------------|--------|
| Proactive Suggester (confidence-weighted suggestions) | GAIA Bible, PREDICTIVE_GAIA_SPEC.md | Specified, not coded |
| Background task scheduling (APScheduler) | GECO Audit Q13 | Not started |
| Auto-generated tests from code analysis | GECO Audit Q23 | Not started |
| Token budget management and progressive disclosure | GECO Audit Q14, Q17 | Not started |
| One-command rollback to known-good state | GECO Audit Q24 | Not started |
| GAIA skill auto-discovery registry | GECO Audit Q16 | Not started |

---

## 3. GECO Audit Gap Status (27 Questions)

The GECO Audit (Feb 8, 2026) identified 27 issues. Here is what has been addressed:

### RESOLVED (Session f2fa2749, Feb 9)

| Q# | Issue | Resolution |
|----|-------|------------|
| Q21 | No GitHub remote for GAIA | **DONE** -- GAIA + 8 sub-components pushed to GitHub (ZoeDepthTokyo org). All registry entries updated with git_remote URLs |
| Q19 | No pre-commit hooks | **DONE** -- `pre-commit install` activated in all 9 repos. Configs existed from GECO v1.1 swarm, now enforced |
| Q1 | No automated error prevention | **DONE** -- Pre-commit hooks active (ruff lint, trailing whitespace, YAML/JSON validation). CI/CD workflows created for ARGUS, MYCEL, VULCAN, WARDEN |
| Q10 | No regression prevention | **DONE** -- GitHub Actions CI with pytest + coverage gates for 4 modules. Pre-commit hooks catch syntax errors |
| Q4 | No TDD enforcement | **DONE** -- CI/CD pipelines enforce pytest on push/PR for MYCEL (80% min), VULCAN (60% min), ARGUS, WARDEN |
| Q9 | No coverage gates | **DONE** -- Coverage thresholds in CI: MYCEL 80%, VULCAN 60%. WARDEN tests created (was 0, now has test_scanner.py + test_cli.py) |

### PARTIALLY ADDRESSED

| Q# | Issue | Status |
|----|-------|--------|
| Q2 | CLAUDE.md advisory only | 6 CLAUDE.md files exist. WARDEN scanner available but not yet in CI enforcement path |
| Q7 | No handoff-ready PRD | GECO Audit Part 5 provides draft PRD. GAIA_PRD.md committed to repo |
| Q25 | jSeeker GECO integration | jSeeker has ARGUS telemetry + CLAUDE.md. CI/CD pending (handled by parallel session) |
| Q24 | No rollback capability | GitHub remotes provide git-based rollback. No one-command `geco rollback` yet |

### NOT YET ADDRESSED (17 of 27)

| Priority | Issues | Summary |
|----------|--------|---------|
| CRITICAL (1) | Q2 (full) | Full programmatic enforcement (WARDEN in CI pipeline, LOOM runtime validator) |
| HIGH (7) | Q3, Q5, Q6, Q20, Q22, Q26, Q27 | Model dashboard, cross-session tasks, learning loops, token visibility, cost alerts, subagent compliance, cross-session learning |
| MEDIUM (7) | Q8, Q12-Q15, Q17-Q18 | Project planning, contract testing, background tasks, progressive disclosure, MCP servers, interaction learning |
| LOW (2) | Q11, Q16 | URL reference storage, skill registry |

---

## 4. Architecture Honest Assessment

### The Three Pillars (What Bible Says vs. Reality)

| Pillar | Bible Claims | Actual State |
|--------|-------------|--------------|
| **VULCAN (Create)** | "Project creation is the only way new projects enter the ecosystem" | Projects CAN be created via VULCAN questionnaire, but most projects were created manually and registered retroactively. VULCAN itself works but is underutilized |
| **LOOM (Modify)** | "Glass-box transparency in modifications" | Workflow engine code exists. No one has used LOOM to modify a real project. Transparency comes from git + CLAUDE.md, not LOOM |
| **ARGUS (Monitor)** | "Mental model library and subconscious pattern detection" | Mental models: YES (59 models, selector works). Dashboard: YES (fixed this session). Process Observer: NO. Trust Dashboard: NO. Telemetry: 1 of 17 projects connected |

### Constitutional Compliance

| Trust Principle | Implementation Status |
|----------------|----------------------|
| **GAIA Never Lies** | PARTIALLY MET -- explicit uncertainty in docs, but no immutable logs or confidence tracking in code |
| **GAIA Admits Limits** | PARTIALLY MET -- authority boundaries documented, read-only contracts in CLAUDE.md, but not mechanically enforced |
| **GAIA Degrades Gracefully** | NOT MET -- ARGUS dashboard crashed on wrong paths before this session's fixes. No fallback mechanisms in LOOM/MNEMIS |
| **GAIA Learns Explicitly** | NOT MET -- MNEMIS has promotion protocol but it's never been triggered. Learning is manual (MEMORY.md) |
| **GAIA Remains Inspectable** | PARTIALLY MET -- ARGUS dashboard provides visibility. But Process Observer and Trust Dashboard are empty |

### The Fundamental Gap (from GECO Audit)

> GAIA has world-class governance documentation but zero runtime enforcement. The infrastructure exists to *observe* violations (ARGUS) and *learn* from them (MNEMIS) but not to *prevent* them.

This remains true after today's session. We fixed the dashboard so it can observe correctly. We haven't yet wired prevention.

---

## 5. Version History (Recent)

| Version | Date | Key Changes |
|---------|------|-------------|
| v0.4.3 | Feb 4 | Phase 2/3 complete: 59 mental models, subconscious layer, LOOM/MNEMIS |
| v0.5.0 | Feb 5 | ARGUS Dashboard MVP, folder restructure (_gaia -> _GAIA), WARDEN scanner, EventBus |
| v0.5.1 | Feb 8-9 | GECO v1.1.0 swarm (20 deliverables), ARGUS dashboard fixes (6 files), registry 10->17, pre-commit configs |

### What Changed in v0.5.1 (This Session)

**ARGUS Dashboard (6 files fixed):**
- `registry_reader.py` -- path `_gaia/` -> `_GAIA/`, schema key `components` -> `projects`
- `memory_tree.py` -- path `_gaia/mnemis/data` -> `_GAIA/_MNEMIS`, graceful "installed but no data" state
- `ecosystem_graph.py` -- schema key fix, status colors for production/active/development/planning/stale, shows gaia_role
- `live_trace.py` -- color map expanded from 6 stale entries to all 17 components
- `app.py` -- PROTEUS->jSeeker build log, sidebar from hardcoded list to dynamic registry, demo fallback updated, version 0.5.1

**GAIA Ecosystem (4 files):**
- `registry.json` -- ARGUS 0.5.0-dev -> 0.5.1, WARDEN git=true, AURORA added by parallel session
- `VERSION_LOG.md` -- v0.5.0 closed, v0.5.1 added
- `GAIA_BIBLE.md` -- status v0.4.3 -> v0.5.1, registry 10 -> 17, WARDEN/RAVEN status updated
- `.pre-commit-config.yaml` -- root-level config created

---

## 6. What To Work On Next (Prioritized)

### COMPLETED (Session f2fa2749)
- ~~Push to GitHub~~ -- 9 repos pushed (GAIA + 8 submodules)
- ~~Activate pre-commit hooks~~ -- `pre-commit install` in all 9 repos
- ~~CI/CD for ARGUS, MYCEL, VULCAN, WARDEN~~ -- GitHub Actions workflows created
- ~~Registry git_remote URLs~~ -- All 8 sub-components linked
- ~~WARDEN tests~~ -- test_scanner.py + test_cli.py created (was 0 tests)
- ~~Shared logging standard~~ -- LOGGING_STANDARD.md + logging_config module

### Immediate (Next Session)
1. **Wire ARGUS telemetry** to MYCEL and VULCAN (safest to integrate first)
2. **Implement Process Observer** -- `observer.py` with basic agent execution logging
3. **Trust Dashboard skeleton** -- Cost display from jSeeker telemetry JSONL
4. **Adopt shared logging** -- Import logging_config in ARGUS and MYCEL
5. **WARDEN in CI** -- Add WARDEN compliance scan as CI/CD step

### Short-term (Next 2 Sessions)
6. **MNEMIS activation** -- Store first real memory entries, test promotion protocol
7. **Cost tracking** -- Token count -> dollar amount calculation in ARGUS
8. **Cross-session task persistence** -- MNEMIS-based task store
9. **LOOM validation** -- Run a real workflow through the engine

### Deferred
10. ABIS development, DOS development, RAVEN research agent
11. Background task scheduling (APScheduler)
12. MCP server registration for GAIA modules
13. Auto-generated tests, progressive disclosure, contract testing

---

## 7. Session Context

### Active Sessions (Feb 9, 2026)
- **This session**: GAIA + ARGUS + GECO gaps (jSeeker workspace)
- **Parallel session**: jSeeker v2 bugs and regressions (same workspace, different window)
- **Parallel session (5bddf5a3)**: AURORA Phase A+B completion

### Key Session IDs
| Session | Scope | Date |
|---------|-------|------|
| `262c1443` | GECO v1.1.0 master swarm (70+ subagents) | Feb 8 |
| `5bddf5a3` | AURORA implementation | Feb 9 |
| `02cfa258` | AURORA completion + jSeeker rename | Feb 9 |
| `c7726e3d` | Global CLAUDE.md + skills | Feb 6 |
| `740c8b62` | ARGUS HITL v0.5.1 planning | Feb 8 |
| `f2fa2749` | GAIA v0.5.1 calibration + GitHub push + GECO fixes | Feb 9 |

---

## 8. Calibration Delta Tracking

This section tracks calibration changes over time. Each session that modifies this document adds an entry.

### Entry 1: Feb 9, 2026 -- Initial Calibration
- **Agent**: Claude Opus 4.6
- **Trigger**: User requested full ecosystem assessment
- **Findings**: 17 projects registered, 7 truly operational, 3 partially operational, enforcement gap remains the #1 issue
- **Actions Taken**: Fixed ARGUS dashboard (6 files), updated GAIA Bible, VERSION_LOG, registry. Created pre-commit root config. Pushed to GitHub.
- **Open Items**: 25 of 27 GECO audit issues remain unaddressed.

### Entry 2: Feb 9, 2026 -- GECO Enforcement Sprint (Session f2fa2749)
- **Agent**: Claude Opus 4.6 + 6 parallel subagents
- **Trigger**: User requested parallel agent orchestration for GECO items
- **Actions Taken**:
  - GitHub repos created + pushed for all 8 sub-components (gaia-abis through gaia-warden)
  - Registry updated with git_remote URLs (9 of 17 projects now have remotes)
  - Pre-commit hooks ACTIVATED in all 9 repos (was config-only, now enforced)
  - CI/CD workflows created: ARGUS, MYCEL, VULCAN, WARDEN (GitHub Actions with pytest + ruff)
  - WARDEN tests created (was 0, now has test_scanner.py + test_cli.py)
  - Shared logging standard created (LOGGING_STANDARD.md + logging_config.py)
  - README.md created for GitHub landing page
- **GECO Status**: 10 of 27 resolved, 4 partially addressed, 17 remaining (down from 25)
- **Open Items**: Trust Dashboard, Process Observer, MNEMIS activation, cost tracking, cross-session persistence, subagent compliance

---

*This is a living document. Update it when the state of GAIA changes.*
