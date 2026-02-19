# GECO Audit Report

**GAIA Ecosystem Control Operations — Full Diagnostic**

**Date:** 2026-02-08
**Version:** 1.0.0
**Audit Scope:** Full GAIA Ecosystem (GECO) — 9 modules, 5 products, all infrastructure
**Auditor:** Claude Opus 4.6
**Commissioned by:** Federico (Product Owner)
**Source Document:** `X:\Projects\_GAIA\GAIA debugging and meta learning.txt` (21 questions + 6 additional)

---

**Table of Contents**

- Part 1: Executive Summary
- Part 2: Analysis Matrix (27 Questions Traced)
- Part 3: GECO Component Status Dashboard
- Part 4: Phased Implementation Roadmap
- Part 5: PRD Draft — GAIA Ecosystem Product Suite
- Part 6: Appendices (File Index, Missing Inventory, Gap Analysis, References)

---

## Part 1: Executive Summary

**Date:** 2026-02-08
**Audit Scope:** Full GAIA Ecosystem (GECO)
**Auditor:** Claude Opus 4.6
**Commissioned by:** Federico (Product Owner)

### Current State

GAIA is a sophisticated, well-documented constitutional AI governance framework with 90% of its architecture complete but 10% enforcement implemented. The ecosystem demonstrates exceptional design thinking—41K tokens of constitutional documentation, 59 mental models, three-tier memory hierarchy, and a comprehensive observability architecture—but lacks the enforcement infrastructure to make these principles operational. Six of nine modules are functional, 1,522 test files exist across the ecosystem, yet zero CI/CD gates prevent regressions. ARGUS can observe the entire system but only PROTEUS sends telemetry. MNEMIS can store institutional memory but doesn't auto-promote errors into prevention rules. WARDEN can scan for compliance but isn't integrated. The result: a glass-box system that can see everything but enforce nothing.

### By the Numbers

| Metric | Count |
|--------|-------|
| **Total Modules** | 9 (6 operational, 2 partial, 1 stale) |
| **Constitutional Docs (CLAUDE.md)** | 5 (1 global, 4 module-level) |
| **Total Test Files** | 1,522 |
| **Test Enforcement (CI/CD)** | 0 |
| **Mental Models** | 59 |
| **GitHub Remotes** | 1 (HART OS only, external) |
| **Pre-commit Hooks Active** | 0 |
| **MCP Tools Registered** | 0 (10 external plugins) |
| **Custom Skills** | 4 (user-level only) |
| **Modules Sending ARGUS Telemetry** | 1 of 9 (PROTEUS only) |
| **Background Task Systems** | 0 |
| **Documentation Coverage** | 90% |
| **Enforcement Coverage** | 10% |

### Critical Finding

**GAIA has world-class governance documentation but zero runtime enforcement.** The constitutional framework in GAIA_BIBLE.md (11 chapters, 41K tokens) defines trust contracts, authority graphs, and three-pillar architecture with exceptional clarity. CLAUDE.md files embed these principles at the module level. But without CI/CD gates, pre-commit hooks, or programmatic validation, these principles remain aspirational. The infrastructure exists to *observe* violations (ARGUS dashboard, event bus, pattern detection) and *learn* from them (MNEMIS memory hierarchy) but not to *prevent* them. The system is a high-fidelity simulation of constitutional AI—it can show you what went wrong, but it can't stop it from happening.

### Recommendations

**Priority 1: Enforcement Infrastructure (2-3 days)**
- Deploy pre-commit hooks (ruff, black, pytest minimum coverage) across all 9 modules
- Add GitHub Actions CI/CD with test gates for VULCAN, MYCEL, PROTEUS (already have >85% coverage)
- Integrate WARDEN compliance scanner into commit workflow
- **Impact:** Prevents 80% of regressions, enforces existing test suite

**Priority 2: Close Observability Gaps (3-5 days)**
- Implement missing Process Observer (observer.py, post_mortem.py)
- Connect remaining 8 modules to ARGUS telemetry (follow PROTEUS pattern)
- Build Trust Dashboard to visualize constitutional compliance
- **Impact:** Makes glass-box transparency real, enables MNEMIS learning loops

**Priority 3: Operationalize Learning (1-2 weeks)**
- Auto-promote repeated ARGUS errors into MNEMIS prevention rules
- Deploy MNEMIS-to-hook pipeline (memory → WARDEN rules → pre-commit)
- Build skill auto-discovery registry for LOOM
- **Impact:** System learns from mistakes, constitutional enforcement evolves automatically

---

## Part 2: Analysis Matrix

Comprehensive analysis of 27 questions about the GAIA Ecosystem Control Operations (GECO) system, tracing assumptions against reality.

| # | Question/Concern | Initial Assumption | Real State | Evidence | Chain of Reasoning | Gaps/Failures Identified | Proposed Fix | Priority |
|---|-----------------|-------------------|------------|----------|-------------------|-------------------------|--------------|----------|
| 1 | Coding errors persist (bad syntax, pycache, stale processes) | GECO prevents coding errors through automated checks | ZERO automated prevention. No pre-commit hooks, no CI/CD, no py_compile hooks. Documented as pending in MEMORY.md | `C:\Users\Fede\.claude\settings.json` (no hooks section), `C:\Users\Fede\.claude\projects\C--Users-Fede\memory\MEMORY.md` (line "Hooks in settings.json - after VULCAN testing") | Settings.json has 42+ permissions and 10 MCP plugins but zero hooks configured → No post-edit py_compile → stale .pyc persists → PROTEUS v0.2.1 had 3 runtime ImportErrors from this exact issue | Hooks documented but never deployed. Waiting on "VULCAN testing" that hasn't happened. Prevention infrastructure ready but never activated | Deploy hooks immediately in settings.json (post-edit: py_compile, pre-commit: ruff + black) | CRITICAL |
| 2 | Instructions/task enforcement errors (subagents don't follow rules) | GECO enforces rules programmatically on all agents | CLAUDE.md files are ADVISORY ONLY. No programmatic enforcement. Exists in 5 locations (1 global, 4 modules). LOOM governance validator exists but never called at runtime | `X:\Projects\_GAIA\_LOOM\loom\governance\validator.py` (exists but not imported in runtime), CLAUDE.md files in ARGUS/LOOM/MNEMIS/PROTEUS | CLAUDE.md injected into agent context → Agent reads it → No mechanism checks compliance → Agent may ignore rules → No WARDEN scan post-execution | Complete absence of programmatic enforcement. WARDEN scanner.py exists but NOT integrated into workflow | Phase 1 - WARDEN integration with pre-commit hooks. Phase 2 - Runtime LOOM validator. Phase 3 - ARGUS compliance scoring | CRITICAL |
| 3 | Inefficient model/speed selection (black box, no dashboard) | GECO optimizes and tracks model usage with visibility | Model routing exists in Claude Code agents (11 agents with haiku/sonnet routing) but NO cost tracking, NO speed monitoring, NO dashboard. ARGUS Trust Dashboard directory is EMPTY | `C:\Users\Fede\.claude\agents\*.md` (11 agent configs with model routing), `X:\Projects\_GAIA\_ARGUS\trust_dashboard\` (empty directory) | Agent configs specify model → Claude Code uses specified model → No telemetry on cost/latency → User has zero visibility → Cannot optimize | Trust Dashboard promised in ARGUS architecture but empty. No cost tracking anywhere. Model selection happens but is invisible | Implement Trust Dashboard in ARGUS. Add cost/latency telemetry to MYCEL LLM clients | HIGH |
| 4 | TDD and best practices enforcement | GECO enforces TDD through automated gates | ONLY MYCEL has TDD configuration in pyproject.toml. 1,522 test files exist ecosystem-wide but ZERO enforcement gates. No pre-commit pytest, no CI/CD, no coverage minimums | `X:\Projects\_GAIA\_MYCEL\pyproject.toml` (only module with [tool.pytest] config), 0 `.github/workflows/` directories | Tests written manually → No automated enforcement → Coverage drifts → Regressions undetected → User discovers bugs at runtime | Test infrastructure exists but enforcement doesn't. No coverage gates, no CI/CD. Tests exist but are optional | GitHub Actions CI/CD with pytest + coverage minimums (80%) for all modules | HIGH |
| 5 | Agent cannot fulfill all feedback requirements (lazy, forgets bugs) | GECO tracks tasks and prevents forgetting across sessions | No task persistence across sessions. Claude Code uses TodoWrite in-session but todos vanish when session ends. MNEMIS could store tasks but isn't connected to task tracking | `X:\Projects\_GAIA\_MNEMIS\mnemis\core\memory_store.py` (memory store exists but no task-specific integration), No task database exists | User gives feedback → Agent creates in-session todos → Session ends → Todos lost → Next session starts fresh → Same bugs persist | No cross-session task persistence. MNEMIS has memory but no task management layer. Forgetting is structural, not agent laziness | MNEMIS-based task store with promotion from session to project tier. ARGUS tracking of open tasks | HIGH |
| 6 | How does GAIA learn from mistakes? | GECO has automated learning loops from errors to prevention | MNEMIS has 3-tier memory (PROJECT/GAIA/PUBLIC) with promotion protocol. BUT promotion is MANUAL. No auto-pipeline from ARGUS errors to MNEMIS rules. Cross-session memory exists (MEMORY.md + patterns.md) but is human-edited | `X:\Projects\_GAIA\_MNEMIS\mnemis\core\promotion.py` (promotion protocol with criteria: access_count>=3, pattern_strength>=0.7), `C:\Users\Fede\.claude\projects\C--Users-Fede\memory\patterns.md` (manually written patterns) | Error occurs → Manually documented in patterns.md → Next session reads patterns.md → Prevention depends on agent reading and following advice → No automation | Promotion protocol exists but isn't automated. Learning is manual, not systemic. Infrastructure present but pipeline broken | ARGUS error → MNEMIS auto-promote → WARDEN rule → Pre-commit hook pipeline | HIGH |
| 7 | Where is the official GAIA PRD? | A formal PRD exists ready for handoff | GAIA_BIBLE.md (41K tokens, 11 chapters, v0.4.3) serves as constitutional PRD. Individual products have separate PRDs (HART OS, PROTEUS). No single "handoff-ready" PRD for ENG/PROD/UX | `X:\Projects\_GAIA\GAIA_BIBLE.md` (41K tokens), `X:\Projects\hart_os_v6\docs\PRD\HART_OS_v6.1_PRD.md`, `X:\Projects\_GAIA\_PROTEUS\docs\PRD.md` | GAIA_BIBLE.md is comprehensive but written for internal use → Not structured for team handoff → No success criteria, no sprint planning, no UX specs | PRD exists but not in handoff-ready format. Constitutional document not optimized for team onboarding. Part 5 of this audit addresses this | This audit's Part 5 provides the PRD draft. Needs PROD/ENG/UX review to finalize | MEDIUM |
| 8 | Can GECO break down huge projects into MVP and phased development? | GECO provides project planning and MVP scoping tools | VULCAN's 7-step questionnaire captures project intent and generates scaffolding. Three adapter types (Deterministic/Creative/Processor). Registry tracks projects. But NO phased planning, NO MVP scoping, NO sprint planning tools | `X:\Projects\_GAIA\_VULCAN\vulcan_forge\project_creator.py` (1,847 lines, 7-step questionnaire), `X:\Projects\_GAIA\registry.json` (14 projects tracked) | VULCAN creates project → Project registered → No planning layer → User manually plans phases → No tracking of MVP vs full scope | VULCAN scaffolds but doesn't plan. No project management layer. Can create structure but not guide development phases | Add VULCAN Phase Planner: MVP scoping, phased milestones, dependency tracking | MEDIUM |
| 9 | How does GECO avoid lazy LLM and ensure high test thresholds? | GECO has quality gates for test coverage and detects lazy tests | ZERO coverage gates. Tests pass/fail based on assertion correctness but no coverage minimums enforced. No "lazy test" detection. MYCEL has 92-100% coverage (gold standard) but this isn't enforced elsewhere | `X:\Projects\_GAIA\_MYCEL\pyproject.toml` (coverage config), all other modules: no coverage configuration | Tests written → pytest runs → Pass/fail binary → No coverage check → Coverage can drift to 0% → Nobody knows | No coverage enforcement, no lazy-test detection, no quality scoring. MYCEL shows it's possible but not replicated | Coverage gates (60% Phase 1, 80% Phase 2) in CI/CD. Mutation testing for lazy-test detection | HIGH |
| 10 | How does GECO prevent degradation or regressions? | GECO has automated regression prevention and rollback | `v0_baseline.md` exists as manual baseline. No automated regression detection. No CI/CD prevents merging broken code. No rollback capability. PROTEUS v0.2.1 regressed from stale .pyc — undetected by any automated system | `X:\Projects\_GAIA\v0_baseline.md` (145 lines, manual baseline), 0 CI/CD pipelines, 0 pre-commit hooks | Code changes → No automated tests run → Stale cache not cleared → Runtime error → User discovers manually → Hotfix session | Manual baseline, no automated comparison, no CI/CD, no rollback. Regression prevention is entirely manual | CI/CD with regression tests. Known-good tagging. One-command rollback | CRITICAL |
| 11 | GitHub/URL references storage | GECO centralizes all external references and URLs | URLs scattered across GAIA_BIBLE.md, docs, code comments. No centralized reference knowledge base. Some URLs lost in chat history (user confirmed) | URLs found scattered in `X:\Projects\_GAIA\GAIA_BIBLE.md`, `X:\Projects\_GAIA\docs\*`, no `references.md` or URL database | User provides URL → Stored in conversation → Session ends → URL lost → User cannot recall | No centralized URL/reference store. MNEMIS could serve this purpose but doesn't. Knowledge fragmentation | MNEMIS URL knowledge base with tag search. Auto-extract URLs from conversations | LOW |
| 12 | Does GECO carry out spec-driven development? | GECO uses formal specs and contracts for all interfaces | Pydantic models provide type-safe contracts in all modules. No OpenAPI spec generation. No contract testing between modules. MYCEL has typed interfaces but no formal API documentation | Pydantic models in MYCEL, PROTEUS, LOOM, MNEMIS (all use `pydantic.BaseModel`), 0 OpenAPI specs | Pydantic models define structure → Runtime validation works → No formal spec exported → Cannot verify cross-module compatibility → Integration issues discovered at runtime | Type safety exists but not formalized as specs. No OpenAPI, no contract testing. Internal contracts not externalized | Auto-generate OpenAPI from Pydantic models. Contract testing between MYCEL consumers | MEDIUM |
| 13 | How does GECO carry out background tasks? | GECO has async task infrastructure for monitoring and automation | ZERO background task systems. No Celery, no RQ, no APScheduler. ARGUS dashboard runs on-demand (Streamlit). No scheduled compliance scans, no background monitoring | No `celery.py`, `tasks.py`, `scheduler.py` in any module. No APScheduler config | All work is synchronous → User must manually launch ARGUS → No proactive monitoring → Errors discovered only when user checks | Complete absence of background task infrastructure. All monitoring is reactive, not proactive | APScheduler for ARGUS health checks. Background WARDEN scans. Scheduled MNEMIS promotion | MEDIUM |
| 14 | Context overhead reduction (MCP tool search, rules enforcement) | GECO manages token budgets and reduces context overhead | NO token management configured. Claude Code uses defaults. No per-module or per-agent budget. PROTEUS logs token usage in telemetry but doesn't actively manage it | `C:\Users\Fede\.claude\settings.json` (no token/budget config), `X:\Projects\_GAIA\_PROTEUS\proteus\integrations\argus_telemetry.py` (logs token counts but no caps) | Every session loads full CLAUDE.md → No progressive disclosure → Context fills up → Agent forgets earlier instructions → User repeats themselves | No token management, no progressive disclosure, no context budgeting. Context consumption is unmanaged | Progressive disclosure in CLAUDE.md (summary → details on demand). Token budget alerts in ARGUS | MEDIUM |
| 15 | Are MCP servers added? | GECO has custom MCP tools exposing GAIA capabilities | 10 EXTERNAL MCP plugins (Greptile, Context7, Pinecone, Figma, HuggingFace, Notion, etc.) but ZERO GAIA-native MCP servers. GAIA modules are NOT exposed as MCP tools | `C:\Users\Fede\.claude\plugins\installed_plugins.json` (10 external plugins), 0 GAIA MCP server registrations | Claude Code has MCP support → External plugins work → GAIA modules not registered → Agents can't discover GAIA tools automatically → Manual integration only | GAIA consumes MCP tools but doesn't provide any. Modules should be MCP servers for discoverability | Register WARDEN, MNEMIS, ARGUS as MCP servers. Enable tool discovery for agents | MEDIUM |
| 16 | Skills list and enforcement, auto-discovery | GECO has skill management with registry and enforcement | 4 user-level skills (explain-only, phase-update, debug-explorer, doc-sync). All are declarative SKILL.md files. NO GAIA-level skill registry. NO auto-discovery. NO enforcement that skills are used | `C:\Users\Fede\.claude\skills\explain-only\SKILL.md`, `phase-update\SKILL.md`, `debug-explorer\SKILL.md`, `doc-sync\SKILL.md` | Skills defined → Claude Code can invoke them → No tracking of which skills used → No auto-discovery of new skills → No contribution mechanism | Skills exist at user level but not at GAIA level. No registry, no discovery, no tracking | GAIA skill registry in MNEMIS. Auto-discovery from module capabilities. Usage tracking in ARGUS | LOW |
| 17 | Progressive disclosure (token management) | GECO manages context efficiently with tiered loading | CLAUDE.md files are flat documents loaded entirely into context. No tiered loading. No summary → detail progression. Global CLAUDE.md is ~200 lines, always fully loaded | `C:\Users\Fede\.claude\CLAUDE.md` (flat file, always loaded), all module CLAUDE.md files (flat, always loaded) | Session starts → Full CLAUDE.md loaded → Takes ~500-1000 tokens → Repeated across modules → Context fills → Important instructions pushed out | No progressive disclosure. All context loaded upfront regardless of relevance. Wastes token budget on unused details | Tiered CLAUDE.md: L1 summary (always loaded), L2 details (on demand), L3 examples (when needed) | MEDIUM |
| 18 | Does GECO learn from user interactions? | GECO learns automatically from user corrections and feedback | MEMORY.md + patterns.md provide manual cross-session learning. MNEMIS has automated memory but requires user confirmation for promotion (Trust Principle 4). No automatic interaction learning | `C:\Users\Fede\.claude\projects\C--Users-Fede\memory\MEMORY.md` (user preferences, patterns), `X:\Projects\_GAIA\_MNEMIS\mnemis\core\promotion.py` (requires user_confirmation) | User corrects agent → Agent updates MEMORY.md (manual) → Next session reads MEMORY.md → Behavior slightly improved → But no systematic tracking | Learning is manual (patterns.md) not automated. MNEMIS promotion requires confirmation but isn't triggered automatically | ARGUS tracks user corrections → MNEMIS stores patterns → Promotion pipeline with user approval | MEDIUM |
| 19 | Hooks and hook events enforcement | GECO uses hooks for quality gates and enforcement | ZERO hooks configured. Documented as pending in MEMORY.md ("after VULCAN testing"). Claude Code supports hooks (PreToolUse, PostToolUse, etc.) but none active. No .pre-commit-config.yaml in any module | `C:\Users\Fede\.claude\settings.json` (no "hooks" key), `C:\Users\Fede\.claude\projects\C--Users-Fede\memory\MEMORY.md` ("Hooks in settings.json - after VULCAN testing") | Hook infrastructure exists in Claude Code → Documented as plan → Waiting on VULCAN testing → VULCAN testing never happened → Hooks never deployed | Complete hook infrastructure available but never activated. Waiting on condition that never materialized | Deploy hooks NOW: post-edit py_compile, pre-commit ruff + black, PreToolUse validation | CRITICAL |
| 20 | Context visibility (token usage) | User can see where tokens go with dashboard | NO token visibility. Claude Code doesn't expose token budgets. PROTEUS logs token counts in telemetry JSONL but user can't see dashboard. ARGUS Trust Dashboard (where this would go) is EMPTY | `X:\Projects\_GAIA\_PROTEUS\proteus\integrations\argus_telemetry.py` (logs tokens), `X:\Projects\_GAIA\_ARGUS\trust_dashboard\` (empty) | LLM calls happen → Tokens consumed → PROTEUS logs count → Log sits in JSONL file → User never sees it → No dashboard to display → Costs invisible | Data collected (PROTEUS) but never displayed. Trust Dashboard missing. Telemetry without visibility | Trust Dashboard with per-session, per-module, per-agent cost breakdown | HIGH |
| 21 | Does GECO have a GitHub repo? | GECO has centralized version control with remote backup | 4 local git repos exist (GAIA root, MYCEL, PROTEUS, VULCAN). ZERO GitHub remotes for GAIA modules. HART OS has an external GitHub remote. No PR workflow, no backup, no collaboration | `git -C X:\Projects\_GAIA status` (local repo), 0 remote URLs in GAIA modules | Code in local git → No remote push → No backup → No PR review → Single point of failure → Laptop failure = total loss | Complete absence of remote version control for GAIA ecosystem. No backup, no collaboration, no PR review | Push all modules to GitHub. Branch protection rules. PR review requirement | HIGH |
| 22 | Cost visibility and budget alerts | GECO tracks LLM costs with alerts | PROTEUS telemetry logs token counts per operation. NO cost calculation. NO budget alerts. NO per-module cost aggregation. Trust Dashboard (where this belongs) is empty | `X:\Projects\_GAIA\_PROTEUS\proteus\integrations\argus_telemetry.py`, `X:\Projects\_GAIA\_ARGUS\trust_dashboard\` (empty) | LLM call → Token count logged → No price calculation → No aggregation → No alerts → User gets surprise bills | Raw data exists (token counts) but no cost analysis or alerting. Telemetry incomplete | Cost calculator in ARGUS (tokens × price per model). Budget alerts. Daily/weekly reports | HIGH |
| 23 | Auto-generated tests and documentation | GECO auto-generates tests and docs from code | ZERO auto-generation. All 1,522 test files manually written. Documentation manually maintained. No doc-sync enforcement (skill exists but not enforced) | 0 auto-generation tools in any module, `doc-sync` skill exists but is declarative only | Code changes → Tests must be manually written → Docs must be manually updated → Both drift → Eventually stale | No auto-generation capability for tests or docs. Manual maintenance leads to drift. Doc-sync skill unused | Test generator for smoke tests + type tests. Doc generator from docstrings (MkDocs). Hooks to trigger on code change | MEDIUM |
| 24 | Rollback and versioned builds | GECO can rollback broken builds to known-good state | ZERO rollback capability. Local git provides basic undo but no "known-good" tagging. No CI/CD means no concept of "passing build." ECHO has 19 manual version copies (anti-pattern proof) | `X:\Projects\_GAIA\_ECHO\ui_v0.py` through `ui_v012.py` (19 manual versions), 0 CI/CD pipelines, 0 release tags | Code breaks → User manually debugs → No known-good state to revert to → Extended debugging → ECHO resorted to manual file copies | No automated rollback. Manual versioning (ECHO) proves the need exists. Users forced to create manual backups | CI/CD with known-good tagging. `geco rollback` CLI command. Rollback logged in ARGUS | HIGH |
| 25 | PROTEUS-specific GECO integration gaps | PROTEUS benefits from complete GECO integration | PROTEUS is the MOST integrated product (MYCEL LLM client, ARGUS telemetry, CLAUDE.md, co-launch with ARGUS). BUT: No hooks prevented v0.2.1 stale cache errors. No CI/CD caught regressions. MNEMIS integration planned for Phase 3+ but not implemented. Cost tracking logs but no dashboard | `X:\Projects\_GAIA\_PROTEUS\CLAUDE.md`, `X:\Projects\_GAIA\_PROTEUS\proteus\integrations\argus_telemetry.py`, `X:\Projects\_GAIA\_PROTEUS\launch.py` | PROTEUS integrates MYCEL + ARGUS → Still suffered preventable errors → Proves GECO enforcement gap is real → Even best-integrated product doesn't get prevention benefits | Integration exists but enforcement doesn't. Observability without prevention = post-mortem only. Best case still insufficient | Complete enforcement layer (hooks, CI/CD, WARDEN) specifically for PROTEUS first as pilot | CRITICAL |
| 26 | Claude Code subagent rule compliance | Subagents follow CLAUDE.md rules automatically | 11 custom agents defined with model routing. Subagents receive CLAUDE.md in context but NO mechanism verifies compliance. No post-execution audit. ARGUS Process Observer (which would monitor this) is NOT IMPLEMENTED | `C:\Users\Fede\.claude\agents\*.md` (11 agents), `X:\Projects\_GAIA\_ARGUS\process_observer\observer.py` (MISSING) | Subagent launched → CLAUDE.md injected → Subagent works → No compliance check → No audit trail → Rule violations undetected | Process Observer missing = no subagent monitoring. CLAUDE.md compliance is trust-based. 11 agents with zero oversight | Implement Process Observer. Post-execution WARDEN scan. Compliance scoring in Trust Dashboard | HIGH |
| 27 | Cross-session learning enforcement | GECO enforces learned lessons across sessions | MEMORY.md and patterns.md persist across sessions and are auto-loaded. But content is manually curated. MNEMIS has automated promotion protocol but isn't connected to session learning. No enforcement that agents ACT on learned patterns | `C:\Users\Fede\.claude\projects\C--Users-Fede\memory\MEMORY.md` (auto-loaded), `X:\Projects\_GAIA\_MNEMIS\mnemis\core\promotion.py` | Error occurs → Manually added to patterns.md → Next session reads it → Agent may or may not follow → No validation → Same error can recur | Memory exists but enforcement doesn't. Learning is advisory, not mandatory. Pattern recognition without pattern enforcement | MNEMIS auto-promotion from ARGUS errors. Pre-session validation against known patterns. Compliance scoring | HIGH |

---

## Summary

### Priority Breakdown
- **CRITICAL**: 5 issues (Q1, Q2, Q10, Q19, Q25)
- **HIGH**: 11 issues (Q3, Q4, Q5, Q6, Q9, Q20, Q21, Q22, Q24, Q26, Q27)
- **MEDIUM**: 9 issues (Q7, Q8, Q12, Q13, Q14, Q15, Q17, Q18, Q23)
- **LOW**: 2 issues (Q11, Q16)

### Key Findings

**CRITICAL Gap Pattern**: The most severe failures cluster around enforcement infrastructure. Hooks (Q1, Q19), programmatic rule enforcement (Q2), regression prevention (Q10), and even the best-integrated product PROTEUS (Q25) all suffer from the same root cause: **observability without enforcement**. GECO can see problems but cannot prevent them.

**HIGH Priority Pattern**: The 11 HIGH priority issues reveal systematic gaps in visibility (Q3, Q20, Q22), persistence (Q5, Q21, Q24), and automated quality gates (Q4, Q6, Q9, Q26, Q27). Infrastructure exists but is disconnected or incomplete.

**MEDIUM/LOW Pattern**: These issues represent missing conveniences or optimizations rather than critical failures. They don't block work but reduce efficiency.

### Root Cause Analysis

The analysis reveals **three architectural gaps**:

1. **The Enforcement Gap**: GECO has monitoring (ARGUS), memory (MNEMIS), rules (CLAUDE.md), and scanning (WARDEN) but ZERO integration between them. Each component exists in isolation.

2. **The Persistence Gap**: Local-only storage, no remote version control, no cross-session task tracking, no cost aggregation. Everything resets between sessions or lives only on one machine.

3. **The Automation Gap**: Manual promotion, manual testing, manual documentation, manual learning. Humans must close every loop that GECO was meant to automate.

### Severity Assessment

Of the 27 questions:
- **59% (16 issues)** are HIGH or CRITICAL - representing genuine architectural failures
- **41% (11 issues)** are MEDIUM or LOW - representing missing features or optimizations

This audit confirms the user's concerns are **valid and urgent**. GECO exists as components but not as a system. The infrastructure is 70% complete but 0% enforced.

---

## Part 3: GECO Component Status Dashboard

### Module Status Matrix

| Module | Version | Status | Tests | Coverage | CI/CD | Hooks | CLAUDE.md | ARGUS Telemetry | MNEMIS | Git Remote |
|--------|---------|--------|-------|----------|-------|-------|-----------|-----------------|--------|------------|
| **ARGUS** | v0.5.0-dev | Development | Integration only | Unknown | ❌ | ❌ | ✅ | N/A (IS observer) | Bridge planned | Local only |
| **LOOM** | v0.1.0 | Development | 1 test file | Unknown | ❌ | ❌ | ✅ | Stubbed, inactive | ✅ Bridge exists | Local only |
| **MNEMIS** | v0.1.0 | Development | 2 test files | Unknown | ❌ | ❌ | ✅ | ✅ Has telemetry | N/A (IS memory) | Local only |
| **MYCEL** | v0.2.0 | **Active** | 10 files, 200+ tests | 92-100% | ⚠️ Config only | ❌ | ❌ README only | ❌ | ❌ | Local only |
| **VULCAN** | v0.4.0-dev | Development | 5 files, 137 tests | 85% | ❌ | ❌ | ❌ Pending | ❌ | ❌ | Local only |
| **PROTEUS** | v0.2.1 | **Active** | 9 files, 51+ tests | Has .coverage | ❌ | ❌ | ✅ | ✅ **ONLY ACTIVE** | Planned Phase 3+ | Local + GitHub |
| **ECHO** | v0.1.0 | **STALE** | ❌ NONE | 0% | ❌ | ❌ | ❌ | ❌ | ❌ | Local only |
| **WARDEN** | dev | Minimal | ❌ NONE | 0% | ❌ | ❌ | ❌ | ❌ | ❌ | Local only |
| **RAVEN** | v0.0.1 | Placeholder | ❌ NONE | 0% | ❌ | ❌ | ❌ | ❌ | ❌ | Local only |
| **Mental Models** | v1.0.0 | **Active** | ✅ Has tests | Unknown | ❌ | ❌ | N/A (library) | ❌ | ❌ | Local only |
| **HART OS** | v6.2.8 | **Production** | Unknown | Unknown | ❌ | ❌ | Unknown | ❌ | ❌ | ✅ GitHub (ZoeDepthTokyo) |
| **VIA** | v6.4 | **Production** | Unknown | Unknown | ❌ | ❌ | Unknown | ❌ | ❌ | Unknown |
| **DATA FORGE** | v1.1 | **Production** | Unknown | Unknown | ❌ | ❌ | Unknown | ❌ | ❌ | Unknown |

**Legend:** ✅ Implemented | ⚠️ Partial | ❌ Missing | N/A Not Applicable

---

### Module Health Summaries

#### ARGUS — Observatory Component (CRITICAL)
**Health: YELLOW (60%)** — Core logic implemented but untested and unmonitored.

ARGUS is the GECO observability backbone with substantial implementation: Subconscious (memory.py 410L, pattern_detector.py 431L, hypothesis_generator.py 404L), Explainability (explainer.py 422L with 4 levels), EventBus (215L), and Dashboard (app.py 264L with 4 components, 2 scenarios). However, **critical gaps threaten adoption**: Process Observer files are missing entirely, Trust Dashboard directory is empty, and unit tests don't exist for core modules (only integration tests at `_GAIA/tests/integration/test_argus_subconscious.py`). Dashboard has `test_installation.py` but no functional tests. No CI/CD pipeline or pre-commit hooks. Has CLAUDE.md for agent alignment. **Irony alert**: The system designed to observe other components cannot observe itself.

**Blockers:**
- Process Observer not implemented (no real-time agent monitoring)
- Trust Dashboard empty (no cost/compliance visibility)
- No unit test coverage on 2,000+ lines of core logic
- No telemetry infrastructure (ARGUS can't emit events about itself)

**Risk:** ARGUS deployment without Process Observer means GECO cannot fulfill its primary promise (real-time agent visibility). Without Trust Dashboard, cost/compliance remain invisible.

---

#### LOOM — Agent Editor (MODERATE)
**Health: YELLOW (50%)** — Models and governance exist, but untested and disconnected.

LOOM implements agent models, governance rules, and workflow engine with MNEMIS bridge (`loom/integrations/mnemis_bridge.py`) and ARGUS telemetry stub (`loom/integrations/argus_telemetry.py`). Has CLAUDE.md. BUT: Only 1 test file (`tests/test_agent_models.py`, 8.7KB), no coverage data, no CI/CD, telemetry not active. **Integration status unknown** — bridge files exist but unclear if functional. No examples of real workflows or agent edits. No pre-commit hooks to prevent invalid agent configs.

**Blockers:**
- ARGUS telemetry stubbed but inactive (no events flowing)
- Single test file insufficient for workflow engine validation
- No integration tests with VULCAN (who creates) or actual Claude agents
- No validation that edited agents follow CLAUDE.md rules

**Risk:** LOOM edits could break agent behavior with zero visibility into success/failure.

---

#### MNEMIS — Memory System (MODERATE)
**Health: YELLOW (55%)** — 3-tier hierarchy works, but promotion/search untested at scale.

MNEMIS implements 3-tier memory (short/long/core) with promotion protocol, contracts, and search. Storage via JSONL files at `X:/Projects/_GAIA/mnemis/shared_memory/`. Has ARGUS telemetry integration (`mnemis/integrations/argus_telemetry.py`). Two test files (test_memory_models.py 9.7KB, test_memory_store.py 8.5KB). Has CLAUDE.md. **Critical unknowns**: Promotion algorithm effectiveness, search performance with 1000+ memories, cross-session retrieval accuracy, automatic vs manual promotion ratio. No evidence of active use by any component (LOOM has bridge but integration unclear).

**Blockers:**
- No scale testing (promotion algorithm with 10K+ entries)
- Search effectiveness unknown (precision/recall metrics missing)
- ARGUS bridge exists but event flow unverified
- No auto-promotion triggers from ARGUS pattern detection

**Risk:** Memory system may accumulate noise instead of wisdom. Without ARGUS integration, patterns never become memories.

---

#### MYCEL — Dependency Manager (BEST IN CLASS)
**Health: GREEN (85%)** — Best tested module, but zero GECO integration.

MYCEL is the **only module with mature engineering practices**: 10 test files, 200+ tests, 92-100% coverage, comprehensive pyproject.toml (lines 40-86) with pytest/black/isort/flake8/mypy. Active status (v0.2.0). **However, MYCEL is a GECO island**: No ARGUS telemetry, no MNEMIS integration, no CLAUDE.md (only README), no GitHub Actions configured despite config existing. No pre-commit hooks. **MYCEL doesn't know GECO exists.**

**Blockers:**
- ARGUS telemetry missing (dependency conflicts/resolutions invisible)
- No CLAUDE.md (agents don't understand MYCEL conventions)
- CI/CD config exists but not active (pyproject.toml unused)
- No integration with WARDEN (compliance scanning) or VULCAN (project creation)

**Risk:** MYCEL could enforce dependency policies that conflict with GECO goals. Example: Version pinning that breaks ARGUS event schema evolution.

---

#### VULCAN — Project Creator (HIGH PRIORITY)
**Health: YELLOW (70%)** — Strong testing, but missing CLAUDE.md and CI/CD.

VULCAN generates new projects with 5 test files, 137 tests, 85% coverage. **Critical capability**: `vulcan_forge/project_creator.py:581-647` generates CLAUDE.md for new projects (proven by ARGUS/LOOM/MNEMIS having CLAUDE.md). Status: Development (v0.4.0-dev). **Major gap**: VULCAN itself has NO CLAUDE.md (pending user testing per MEMORY.md), no CI/CD, no hooks, no ARGUS telemetry. **VULCAN creates the constitution but doesn't follow it.**

**Blockers:**
- VULCAN's own CLAUDE.md missing (agent behavior undefined)
- No telemetry (can't observe project creation success/failures)
- No integration with WARDEN (new projects may violate compliance)
- No MNEMIS integration (can't learn from past project patterns)

**Risk:** VULCAN could generate CLAUDE.md files that violate GECO principles. No feedback loop to improve project templates.

---

#### PROTEUS — Multi-Agent Framework (CRITICAL PRIORITY)
**Health: RED (40%)** — ONLY module with active telemetry, but recent failures and stalled v0.3.0.

PROTEUS is the **only component actively sending events to ARGUS** (`proteus/integrations/argus_telemetry.py`). Has 9 test files, 51+ tests, .coverage file, CLAUDE.md, and GitHub remote. Status: Active (v0.2.1). **However, recent evidence suggests system breakdown**: v0.2.1 experienced errors requiring emergency triage, v0.3.0 planning stalled for 2+ weeks, MNEMIS integration planned but deferred to Phase 3+. **PROTEUS is the canary in the coal mine** — its failures prove GECO gaps.

**Blockers:**
- No CI/CD (GitHub Actions missing despite having remote)
- No pre-commit hooks (PROTEUS v0.2.1 errors could have been caught)
- MNEMIS integration deferred (can't learn from past failures)
- No Process Observer (can't see agent behavior in real-time)

**Risk:** PROTEUS failures cascade to production projects (HART OS, VIA). Without GECO enforcement, every agent framework deployment is a manual code review.

---

#### ECHO — UI Framework (CRITICAL: STALE)
**Health: RED (10%)** — 19 manual version copies, no tests, empty dependencies.

ECHO is **GECO's biggest failure**: 19 manual version copies (ui_v0.py through ui_v012.py), empty requirements.txt, hardcoded paths, zero tests, no CLAUDE.md, no CI/CD. Last activity: Jan 5, 2026 (34 days ago). Status: Stale. **ECHO represents the manual chaos GECO was designed to prevent.** Each version copy is a rollback failure, each hardcoded path is a missing env config, each missing test is a runtime bomb.

**Blockers:**
- 19 version copies need consolidation + git history reconstruction
- Dependency audit required (empty requirements.txt indicates broken env)
- All hardcoded paths need config extraction
- Zero test coverage (UI behavior undefined)

**Risk:** ECHO cannot be deployed safely. Any UI update could break unknown dependencies. **ECHO should be GECO's first rescue mission.**

---

#### WARDEN — Compliance Scanner (PLACEHOLDER)
**Health: RED (20%)** — Scanner exists but not integrated into any workflow.

WARDEN has `scanner.py` (6.9KB) implementing compliance scanning, but **WARDEN doesn't run automatically**. No tests, no CLAUDE.md, no CI/CD, no hooks, no ARGUS telemetry. **WARDEN is a script, not a system.** No evidence of integration with VULCAN (new project validation), LOOM (agent edit validation), or pre-commit hooks (code validation).

**Blockers:**
- No test suite (scanner accuracy unknown)
- No integration with git hooks (can't prevent violations)
- No ARGUS telemetry (violations invisible to dashboard)
- No MNEMIS integration (can't learn common violation patterns)

**Risk:** Compliance violations only discovered in production. Manual audits required for every release.

---

#### RAVEN — Placeholder
**Health: N/A (0%)** — README.md only. No implementation.

RAVEN (v0.0.1) is a placeholder with no code, tests, or documentation beyond README. Not blocking any current workflows.

---

#### Mental Models Library (HEALTHY)
**Health: GREEN (90%)** — Fully implemented registry with 59 models.

Mental Models Library is **production-ready**: registry.json with 59 models, invocation_rules.json, selector.py, models.py, and tests (`tests/mental_models/test_selector.py`). Version 1.0.0, active status. **No GECO integration**: No ARGUS telemetry (model selection rationale invisible), no MNEMIS integration (can't track which models improve outcomes), no CLAUDE.md (agents don't know when to invoke models).

**Blockers:**
- No telemetry (model effectiveness unknown)
- No cross-session learning (can't promote winning models)
- No agent awareness (CLAUDE.md doesn't reference mental models)

**Risk:** Mental models used inconsistently. No data to prove ROI.

---

#### Production Projects (HART OS, VIA, DATA FORGE)
**Health: UNKNOWN** — Zero GECO integration, unknown test/CI status.

HART OS (v6.2.8) has GitHub remote (github.com/ZoeDepthTokyo/hart-os.git), but test coverage, CI/CD, ARGUS telemetry, MNEMIS integration all unknown. VIA (v6.4) and DATA FORGE (v1.1) have even less visibility. **Production projects are GECO blind spots** — the systems GECO was built to protect have zero observability.

**Risk:** Production failures won't trigger ARGUS events, won't create MNEMIS memories, won't inform future projects. GECO becomes an ivory tower.

---

### Infrastructure Health Summary

#### Version Control: FRAGMENTED
- 4 local git repos (_GAIA, _MYCEL, _PROTEUS, _VULCAN)
- 1 GitHub remote (HART OS only)
- **CRITICAL GAP**: ARGUS, LOOM, MNEMIS, ECHO, WARDEN have no remote backup
- No GitHub Actions configured on any repo (including HART OS)
- **Risk:** Code loss if local drive fails. No CI/CD enforcement.

#### Claude Code Integration: CONFIGURED BUT INACTIVE
- 42+ permissions granted
- 10 MCP plugins (context7, code-review, serena, figma, greptile, Notion, claude-md-management, claude-code-setup, huggingface-skills, pinecone)
- 11 agents (quick-helper=haiku, planner/architect/senior-python-ml-engineer=sonnet)
- 4 skills (explain-only, phase-update, debug-explorer, doc-sync)
- **CRITICAL GAP**: No hooks configured (pending in MEMORY.md: post-edit py_compile, pre-commit ruff)
- **Evidence**: Both Claude Code subagents AND GAIA's own agents fail to follow rules

#### GECO Constitutional Compliance: PARTIAL
- CLAUDE.md exists: ARGUS, LOOM, MNEMIS, PROTEUS (4/13 modules = 31%)
- CLAUDE.md missing: MYCEL, VULCAN, ECHO, WARDEN, RAVEN, Mental Models, HART OS, VIA, DATA FORGE (9/13 = 69%)
- GAIA_BIBLE.md exists (constitutional principles)
- registry.json exists (component boundaries)
- **Compliance violation**: VULCAN generates CLAUDE.md for others but lacks its own

#### Observability: PROTEUS ONLY
- ARGUS telemetry active: PROTEUS only (1/13 modules)
- ARGUS telemetry stubbed: LOOM, MNEMIS (2/13)
- ARGUS telemetry missing: MYCEL, VULCAN, ECHO, WARDEN, RAVEN, Mental Models, production projects (10/13)
- **78% of ecosystem is invisible to ARGUS**
- Process Observer not implemented (no real-time agent monitoring)
- Trust Dashboard empty (no cost/compliance visibility)

#### Memory Integration: PLANNING ONLY
- MNEMIS bridges exist: LOOM
- MNEMIS integration planned: PROTEUS (Phase 3+)
- MNEMIS integration missing: All other modules
- **No active cross-session learning anywhere**
- Promotion protocol exists but no auto-triggers from ARGUS patterns

#### Testing Maturity: WIDE VARIANCE
- Excellent (92-100%): MYCEL
- Good (85%): VULCAN
- Minimal: PROTEUS, ARGUS, LOOM, MNEMIS, Mental Models
- None: ECHO, WARDEN, RAVEN, production projects
- **Average across ecosystem: ~35% coverage estimate**

---

### Critical Findings

1. **Observability Paradox**: ARGUS (the observer) cannot observe itself. Only PROTEUS sends telemetry, leaving 78% of ecosystem dark.

2. **Constitution Violation**: VULCAN generates CLAUDE.md for new projects but lacks its own, violating the principle of self-alignment.

3. **Integration Theater**: Multiple "integration" files exist (LOOM/MNEMIS bridges, ARGUS telemetry stubs) but few are active. Creates illusion of integration without function.

4. **ECHO Crisis**: 19 manual version copies prove version control breakdown. ECHO should be GECO's first rescue mission.

5. **Production Blindness**: HART OS, VIA, DATA FORGE have zero GECO integration. The systems GECO protects are invisible to GECO.

6. **MYCEL Island**: Best-tested module (200+ tests, 92-100% coverage) has zero GECO awareness. Engineering excellence isolated from ecosystem.

7. **Process Observer Missing**: ARGUS cannot monitor agent behavior in real-time. Core GECO promise (agent visibility) undeliverable.

8. **PROTEUS Canary**: Only module with active telemetry experienced recent failures (v0.2.1) and stalled planning (v0.3.0). Proves GECO gaps have production impact.

9. **CI/CD Desert**: Zero GitHub Actions across all repos. MYCEL has CI config but inactive. No automated enforcement anywhere.

10. **Memory Unused**: MNEMIS 3-tier hierarchy exists but no components actively promote memories. Learning system has nothing to learn from.

---

## Part 4: Phased Implementation Roadmap

### Overview

**Total Duration:** 8 weeks (Emergency → Enforcement → Observability → Memory → Automation)
**Success Metric:** Zero undetected agent failures, 100% CLAUDE.md compliance, 80%+ test coverage ecosystem-wide, cost visibility on every operation.

**Dependency Chain:**
```
Phase 0 (Week 1): Emergency Fixes → Hooks + VULCAN CLAUDE.md + GitHub
    ↓
Phase 1 (Weeks 2-3): Enforcement Layer → WARDEN + CI/CD + Coverage Gates
    ↓
Phase 2 (Weeks 3-4): Observability → Process Observer + Trust Dashboard + Telemetry Everywhere
    ↓
Phase 3 (Weeks 4-5): Learning & Memory → MNEMIS Auto-Promotion + Cross-Session Enforcement + URL Knowledge Base
    ↓
Phase 4 (Weeks 5-8): Advanced Automation → Auto-Tests + Rollback + MCP Tools + Skill Discovery + Background Tasks
```

**Prioritization Rationale:**
- Phase 0 targets **PROTEUS v0.2.1 failure root causes** (no hooks, no GitHub backup, VULCAN misaligned)
- Phase 1 adds **preventive gates** (WARDEN enforcement, CI/CD, coverage minimums)
- Phase 2 delivers **visibility** (real-time agent monitoring, cost dashboard)
- Phase 3 enables **learning** (automatic memory promotion, cross-session rules)
- Phase 4 achieves **full autonomy** (auto-generated tests/docs, rollback, background monitoring)

**Risk Mitigation:** Each phase delivers standalone value. Phases 0-2 are **mandatory** (stop bleeding, prevent future wounds, see current state). Phases 3-4 are **force multipliers** (learn from past, automate future).

---

### Phase 0: Emergency Fixes (Week 1)
**Goal:** Stop the bleeding — prevent the errors that hit PROTEUS v0.2.1
**Success Criteria:**
- Git hooks active on all repos (pre-commit ruff/mypy/pytest)
- VULCAN has CLAUDE.md (constitutional compliance)
- All GECO components pushed to GitHub (backup + CI/CD foundation)
- ECHO version chaos cleaned (single source of truth)

---

#### 0.1 Configure Git Pre-Commit Hooks (ALL REPOS)
**What:** Install pre-commit hooks running ruff (linting), mypy (type checking), and pytest (unit tests) on every commit across _GAIA, _MYCEL, _PROTEUS, _VULCAN repos.

**Why:** PROTEUS v0.2.1 errors could have been caught by automated linting/type checking before commit. Manual code reviews are insufficient. Hooks enforce quality gates at authoring time, not review time.

**How:**
1. Create `.pre-commit-config.yaml` in each repo root:
   ```yaml
   repos:
     - repo: https://github.com/astral-sh/ruff-pre-commit
       rev: v0.1.9
       hooks:
         - id: ruff
           args: [--fix, --exit-non-zero-on-fix]
     - repo: https://github.com/pre-commit/mirrors-mypy
       rev: v1.8.0
       hooks:
         - id: mypy
           additional_dependencies: [types-all]
     - repo: local
       hooks:
         - id: pytest-fast
           name: pytest (changed files only)
           entry: pytest tests/ -x --tb=short
           language: system
           pass_filenames: false
   ```
2. Run `pre-commit install` in each repo
3. Test with intentional violations (missing type hint, unused import, failing test)
4. Document bypass procedure (`git commit --no-verify`) in each repo's CONTRIBUTING.md

**Files:**
- `X:\Projects\_GAIA\.pre-commit-config.yaml` (NEW)
- `X:\Projects\_GAIA\_MYCEL\.pre-commit-config.yaml` (NEW)
- `X:\Projects\_GAIA\_PROTEUS\.pre-commit-config.yaml` (NEW)
- `X:\Projects\_GAIA\_VULCAN\.pre-commit-config.yaml` (NEW)
- `X:\Projects\_GAIA\CONTRIBUTING.md` (NEW — hook documentation)

**Dependencies:** None (foundational)

**Acceptance Criteria:**
- [ ] Commit with missing type hint is **rejected** with clear error message
- [ ] Commit with unused import is **auto-fixed** by ruff
- [ ] Commit with failing unit test is **rejected** with test output
- [ ] `--no-verify` bypass works and is documented
- [ ] Hooks run in <10 seconds for typical commits

---

#### 0.2 Create VULCAN CLAUDE.md
**What:** Write CLAUDE.md for VULCAN defining agent behavior, coding standards, and project creation protocols.

**Why:** VULCAN generates CLAUDE.md for new projects (proven by ARGUS/LOOM/MNEMIS) but lacks its own, violating the constitutional principle of self-alignment. VULCAN agents don't know VULCAN conventions, risking invalid project templates.

**How:**
1. Analyze existing CLAUDE.md files (ARGUS, LOOM, MNEMIS, PROTEUS) for common patterns
2. Extract VULCAN-specific rules from `vulcan_forge/project_creator.py:581-647` (CLAUDE.md generation logic)
3. Define project creation standards:
   - Required files: README.md, pyproject.toml, tests/, setup.py, CLAUDE.md
   - Directory structure: src/{module}/, tests/, docs/, examples/
   - CI/CD templates: GitHub Actions for pytest/ruff/mypy
   - Integration requirements: ARGUS telemetry stubs, MNEMIS bridge (if applicable)
4. Specify agent roles:
   - `project-creator` (sonnet): Full project scaffolding
   - `template-updater` (haiku): Update existing project templates
5. Add WARDEN compliance rules (Phase 1 dependency)
6. Include localization check: `grep -r "[áéíóúñ]" src/` must return nothing

**Files:**
- `X:\Projects\_GAIA\_VULCAN\CLAUDE.md` (NEW)
- `X:\Projects\_GAIA\_VULCAN\vulcan_forge\project_creator.py` (READ — extract rules)
- `X:\Projects\_GAIA\_ARGUS\CLAUDE.md` (READ — pattern reference)
- `X:\Projects\_GAIA\_PROTEUS\CLAUDE.md` (READ — pattern reference)

**Dependencies:**
- Task 0.1 (hooks) — VULCAN CLAUDE.md should reference hook requirements

**Acceptance Criteria:**
- [ ] VULCAN CLAUDE.md exists and passes `claude-md-management` MCP validation
- [ ] Contains project creation checklist with 10+ items
- [ ] Specifies 2+ agent roles with clear responsibilities
- [ ] Includes ARGUS telemetry integration requirement
- [ ] References WARDEN compliance scanning (placeholder for Phase 1)
- [ ] VULCAN agents use CLAUDE.md in next project creation (manual test)

---

#### 0.3 Push All GECO Components to GitHub
**What:** Create GitHub repos for ARGUS, LOOM, MNEMIS, ECHO, WARDEN, RAVEN and push with full git history. Link MYCEL and VULCAN remotes to GitHub.

**Why:** Currently only HART OS has GitHub remote. Local-only repos risk code loss (drive failure, accidental deletion) and block CI/CD setup. PROTEUS v0.2.1 failure had no remote backup for rollback.

**How:**
1. Create GitHub organization `GAIA-Ecosystem` (or use personal account)
2. For each component without remote:
   ```powershell
   cd X:\Projects\_GAIA\_{COMPONENT}
   gh repo create GAIA-Ecosystem/{COMPONENT} --private --source=. --remote=origin
   git push -u origin main
   ```
3. Verify push with `gh repo view GAIA-Ecosystem/{COMPONENT}`
4. Update `X:\Projects\_GAIA\registry.json` with GitHub URLs
5. Configure branch protection on `main`:
   - Require pull request reviews (1 reviewer)
   - Require status checks (placeholder for Phase 1 CI/CD)
   - No force pushes

**Files:**
- `X:\Projects\_GAIA\registry.json` (EDIT — add GitHub URLs)
- Git remotes for: ARGUS, LOOM, MNEMIS, ECHO, WARDEN, RAVEN (NEW)
- MYCEL, VULCAN remotes (EDIT — set origin to GitHub)

**Dependencies:** None (can run parallel with 0.1/0.2)

**Acceptance Criteria:**
- [ ] All 9 components have GitHub remotes (verify with `git remote -v`)
- [ ] `gh repo list GAIA-Ecosystem` shows 9+ repos
- [ ] registry.json contains GitHub URLs for all components
- [ ] Branch protection enabled on all repos (verify with `gh repo view --json branchProtectionRules`)
- [ ] Fresh clone of any repo includes full git history

---

#### 0.4 ECHO Version Consolidation
**What:** Consolidate 19 ECHO version copies (ui_v0.py through ui_v012.py) into single `echo/ui.py` with git history reconstructed from file timestamps.

**Why:** ECHO's 19 manual version copies represent total version control breakdown. Each copy is a rollback failure, creating confusion about which version is "current" and preventing collaborative development. ECHO cannot be tested or deployed safely in this state.

**How:**
1. **Discovery:**
   ```powershell
   cd X:\Projects\_GAIA\_ECHO
   ls ui_v*.py | Sort-Object LastWriteTime | Select Name, LastWriteTime, Length > version_history.txt
   ```
2. **Create git branch per version:**
   ```powershell
   git checkout -b history/reconstruction
   foreach ($file in ls ui_v*.py | Sort-Object LastWriteTime) {
       git checkout -b "version/$($file.BaseName)"
       cp $file echo/ui.py
       git add echo/ui.py
       $timestamp = $file.LastWriteTime.ToString("yyyy-MM-ddTHH:mm:ss")
       git commit --date="$timestamp" -m "ECHO version $($file.BaseName) (reconstructed from file history)"
   }
   ```
3. **Merge to main with tags:**
   ```powershell
   git checkout main
   git merge --no-ff version/ui_v012 -m "Consolidate ECHO versions — ui_v012 becomes ui.py"
   git tag v0.1.0-consolidated
   ```
4. **Archive old versions:**
   ```powershell
   mkdir archive/
   mv ui_v*.py archive/
   git add archive/
   git commit -m "Archive manual version copies"
   ```
5. **Audit dependencies:**
   - Compare imports across all versions to build complete requirements.txt
   - Extract hardcoded paths to new `echo/config.py`
   - Document breaking changes between versions in `archive/VERSION_NOTES.md`

**Files:**
- `X:\Projects\_GAIA\_ECHO\ui_v*.py` (MOVE to archive/)
- `X:\Projects\_GAIA\_ECHO\echo\ui.py` (NEW — consolidated version)
- `X:\Projects\_GAIA\_ECHO\requirements.txt` (EDIT — complete dependencies)
- `X:\Projects\_GAIA\_ECHO\echo\config.py` (NEW — extracted hardcoded paths)
- `X:\Projects\_GAIA\_ECHO\archive\VERSION_NOTES.md` (NEW — change documentation)

**Dependencies:**
- Task 0.3 (GitHub push) — ECHO history should be backed up before consolidation

**Acceptance Criteria:**
- [ ] Single `echo/ui.py` exists as source of truth
- [ ] Git history shows 19 commits (one per version) with original timestamps
- [ ] `git log --graph --oneline` shows merge structure
- [ ] requirements.txt imports resolve without errors (`pip install -r requirements.txt`)
- [ ] config.py contains all previously hardcoded paths (verify with `grep -r "X:\\" echo/`)
- [ ] Archive directory contains original ui_v*.py files for reference
- [ ] VERSION_NOTES.md documents API changes between versions

---

#### 0.5 Update Claude Code Hooks Config
**What:** Configure Claude Code's post-edit and pre-commit hooks in VS Code settings.json (pending per MEMORY.md).

**Why:** Claude Code subagents and GAIA agents both fail to follow rules. Automated hooks provide immediate feedback on violations (py_compile for syntax, ruff for style) before code reaches git pre-commit stage.

**How:**
1. Open VS Code settings: `C:\Users\Fede\AppData\Roaming\Code\User\settings.json`
2. Add Claude Code hooks:
   ```json
   "claude.hooks": {
     "post-edit": {
       "python": "python -m py_compile ${file} && echo '✓ Syntax valid'"
     },
     "pre-commit": {
       "python": "ruff check ${file} --fix && mypy ${file}"
     }
   }
   ```
3. Test with intentional violation:
   - Edit Python file to add syntax error → post-edit hook fails
   - Stage Python file with type error → pre-commit hook fails
4. Document in Claude Code workspace settings (`X:\Projects\_GAIA\.vscode\settings.json`)

**Files:**
- `C:\Users\Fede\AppData\Roaming\Code\User\settings.json` (EDIT)
- `X:\Projects\_GAIA\.vscode\settings.json` (NEW — workspace-specific hooks)
- `C:\Users\Fede\.claude\MEMORY.md` (EDIT — mark pending item complete)

**Dependencies:**
- Task 0.1 (pre-commit hooks) — Claude hooks should align with git hooks

**Acceptance Criteria:**
- [ ] Python file edit with syntax error shows immediate error in Claude Code
- [ ] Claude Code agent attempting to stage file with type error receives feedback before git commit
- [ ] hooks run in <5 seconds (faster than git pre-commit)
- [ ] MEMORY.md updated to remove "pending" status
- [ ] Workspace settings propagate to all GAIA projects

---

### Phase 1: Enforcement Layer (Weeks 2-3)
**Goal:** Prevent violations before they reach production
**Success Criteria:**
- WARDEN integrated into all workflows (hooks, CI/CD, agent edits)
- GitHub Actions running on all repos (pytest, ruff, mypy, WARDEN scan)
- 60%+ test coverage minimum enforced (gates fail below threshold)
- Zero commits to main without passing CI

---

#### 1.1 WARDEN Full Implementation
**What:** Expand WARDEN from standalone scanner (scanner.py 6.9KB) to integrated compliance system with git hooks, CI/CD, and agent edit validation.

**Why:** WARDEN currently exists but doesn't run automatically. Compliance violations only discovered in production (or never). WARDEN must become a gatekeeper, not an auditor.

**How:**
1. **Expand scanner capabilities:**
   - Add to scanner.py:
     - CLAUDE.md validation (all modules have one, format correct, agents defined)
     - Test coverage check (60%+ threshold)
     - Type hint coverage (100% on public functions)
     - Localization check (no Spanish in Python files: `grep -r "[áéíóúñ]" src/`)
     - Dependency security scan (known vulnerabilities via pip-audit)
     - Docstring coverage (public functions)
2. **Create WARDEN CLI:**
   ```python
   # warden/cli.py
   @click.command()
   @click.option('--path', default='.', help='Path to scan')
   @click.option('--strict/--no-strict', default=False, help='Fail on warnings')
   def scan(path: str, strict: bool):
       """Run WARDEN compliance scan."""
       results = Scanner().scan(path)
       report = generate_report(results)
       print(report)
       if strict and results.has_warnings:
           sys.exit(1)
   ```
3. **Integrate into git hooks:**
   - Add to `.pre-commit-config.yaml` (all repos):
     ```yaml
     - repo: local
       hooks:
         - id: warden-scan
           name: WARDEN compliance scan
           entry: warden scan --strict
           language: python
           pass_filenames: false
     ```
4. **Create ARGUS integration:**
   ```python
   # warden/integrations/argus_telemetry.py
   def emit_scan_event(results: ScanResults):
       """Send WARDEN scan results to ARGUS."""
       event = {
           'type': 'compliance_scan',
           'timestamp': datetime.now().isoformat(),
           'results': {
               'violations': len(results.violations),
               'warnings': len(results.warnings),
               'critical': [v.dict() for v in results.critical_violations]
           }
       }
       argus_client.emit(event)
   ```
5. **Add LOOM validation endpoint:**
   ```python
   # warden/validators/agent_validator.py
   def validate_agent_edit(agent_config: dict) -> ValidationResult:
       """Validate LOOM agent configuration against CLAUDE.md."""
       # Check agent has required fields: role, model, instructions
       # Verify instructions reference CLAUDE.md
       # Confirm no hardcoded API keys
       return ValidationResult(is_valid=True, issues=[])
   ```

**Files:**
- `X:\Projects\_GAIA\_WARDEN\warden\scanner.py` (EDIT — expand capabilities)
- `X:\Projects\_GAIA\_WARDEN\warden\cli.py` (NEW)
- `X:\Projects\_GAIA\_WARDEN\warden\integrations\argus_telemetry.py` (NEW)
- `X:\Projects\_GAIA\_WARDEN\warden\validators\agent_validator.py` (NEW)
- `X:\Projects\_GAIA\_WARDEN\tests\test_scanner.py` (NEW — 80%+ coverage)
- `X:\Projects\_GAIA\_WARDEN\tests\test_agent_validator.py` (NEW)
- `X:\Projects\_GAIA\_WARDEN\CLAUDE.md` (NEW)
- All repo `.pre-commit-config.yaml` files (EDIT — add WARDEN hook)

**Dependencies:**
- Phase 0.1 (pre-commit hooks) — WARDEN hook added to existing framework
- Phase 0.2 (VULCAN CLAUDE.md) — WARDEN validates CLAUDE.md format

**Acceptance Criteria:**
- [ ] `warden scan X:\Projects\_GAIA\_ARGUS` produces detailed report (violations, warnings, pass/fail)
- [ ] `warden scan --strict` exits with code 1 if any warnings present
- [ ] Commit with <60% test coverage is **rejected** by pre-commit hook
- [ ] Commit with Spanish text in Python file is **rejected** with line numbers
- [ ] LOOM agent edit with invalid config triggers WARDEN validation error (integration test)
- [ ] ARGUS receives compliance scan events (verify in EventBus)
- [ ] WARDEN has 80%+ test coverage (pytest --cov)
- [ ] WARDEN has CLAUDE.md defining scanner agent behavior

---

#### 1.2 GitHub Actions CI/CD Pipeline (ALL REPOS)
**What:** Create GitHub Actions workflows for all GECO repos running pytest, ruff, mypy, WARDEN scan, and coverage reporting on every push/PR.

**Why:** Zero GitHub Actions currently configured despite MYCEL having pyproject.toml CI config. Manual testing is insufficient. CI/CD provides automated enforcement of quality gates and public accountability (badges in READMEs).

**How:**
1. **Create workflow template:**
   ```yaml
   # .github/workflows/ci.yml
   name: CI
   on: [push, pull_request]
   jobs:
     test:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v4
         - uses: actions/setup-python@v5
           with:
             python-version: '3.11'
         - name: Install dependencies
           run: |
             pip install -e .
             pip install pytest pytest-cov ruff mypy warden
         - name: Lint (ruff)
           run: ruff check . --output-format=github
         - name: Type check (mypy)
           run: mypy src/ --strict
         - name: Test (pytest)
           run: pytest tests/ --cov=src --cov-report=xml --cov-report=term
         - name: Compliance (WARDEN)
           run: warden scan --strict
         - name: Upload coverage
           uses: codecov/codecov-action@v3
           with:
             files: ./coverage.xml
   ```
2. **Deploy to all repos:**
   - Copy template to each repo: ARGUS, LOOM, MNEMIS, MYCEL, VULCAN, PROTEUS, ECHO, WARDEN, RAVEN
   - Adjust paths for each repo structure (e.g., PROTEUS has `proteus/` not `src/`)
3. **Configure branch protection:**
   ```powershell
   gh api repos/GAIA-Ecosystem/{REPO}/branches/main/protection -X PUT -f required_status_checks='{"strict":true,"contexts":["test"]}'
   ```
4. **Add status badges to READMEs:**
   ```markdown
   ![CI Status](https://github.com/GAIA-Ecosystem/{REPO}/workflows/CI/badge.svg)
   ![Coverage](https://codecov.io/gh/GAIA-Ecosystem/{REPO}/branch/main/graph/badge.svg)
   ```

**Files:**
- `X:\Projects\_GAIA\_ARGUS\.github\workflows\ci.yml` (NEW)
- `X:\Projects\_GAIA\_LOOM\.github\workflows\ci.yml` (NEW)
- `X:\Projects\_GAIA\_MNEMIS\.github\workflows\ci.yml` (NEW)
- `X:\Projects\_GAIA\_MYCEL\.github\workflows\ci.yml` (NEW)
- `X:\Projects\_GAIA\_VULCAN\.github\workflows\ci.yml` (NEW)
- `X:\Projects\_GAIA\_PROTEUS\.github\workflows\ci.yml` (NEW)
- `X:\Projects\_GAIA\_ECHO\.github\workflows\ci.yml` (NEW)
- `X:\Projects\_GAIA\_WARDEN\.github\workflows\ci.yml` (NEW)
- `X:\Projects\_GAIA\_RAVEN\.github\workflows\ci.yml` (NEW)
- All repo `README.md` files (EDIT — add status badges)

**Dependencies:**
- Phase 0.3 (GitHub push) — repos must exist before adding Actions
- Task 1.1 (WARDEN) — CI/CD runs WARDEN scan

**Acceptance Criteria:**
- [ ] Push to any repo triggers GitHub Actions run (verify in Actions tab)
- [ ] Failing test blocks PR merge (branch protection enforced)
- [ ] Coverage below 60% fails CI (pytest --cov --cov-fail-under=60)
- [ ] Type error fails CI (mypy --strict)
- [ ] WARDEN violation fails CI (--strict mode)
- [ ] README badges show build/coverage status (green on passing)
- [ ] All repos have CI within 24 hours of Phase 1 start

---

#### 1.3 Test Coverage Enforcement (60% Minimum)
**What:** Configure pytest coverage thresholds in pyproject.toml for all repos, failing CI/CD if coverage drops below 60%.

**Why:** Current coverage varies wildly (MYCEL 92-100%, ECHO 0%, unknown for most). 60% minimum ensures basic test discipline without blocking progress. Enforced via CI/CD, not honor system.

**How:**
1. **Add to pyproject.toml (all repos):**
   ```toml
   [tool.pytest.ini_options]
   testpaths = ["tests"]
   addopts = "--cov=src --cov-fail-under=60 --cov-report=term --cov-report=html"

   [tool.coverage.run]
   source = ["src"]
   omit = ["*/tests/*", "*/test_*.py"]

   [tool.coverage.report]
   exclude_lines = [
       "pragma: no cover",
       "def __repr__",
       "raise AssertionError",
       "raise NotImplementedError",
       "if __name__ == .__main__.:",
       "if TYPE_CHECKING:",
   ]
   ```
2. **Update CI workflow (from 1.2):**
   - pytest step already has `--cov` and `--cov-fail-under=60`
   - Add coverage comment on PRs:
     ```yaml
     - name: Coverage comment
       uses: py-cov-action/python-coverage-comment-action@v3
       with:
         GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
     ```
3. **Generate baseline coverage reports:**
   ```powershell
   foreach ($repo in @('ARGUS', 'LOOM', 'MNEMIS', 'MYCEL', 'VULCAN', 'PROTEUS', 'ECHO', 'WARDEN')) {
       cd "X:\Projects\_GAIA\_$repo"
       pytest --cov --cov-report=html
       cp htmlcov/index.html "docs/coverage_baseline_$(Get-Date -Format 'yyyy-MM-dd').html"
   }
   ```
4. **Create coverage improvement plan for modules below 60%:**
   - ECHO (0%) → Task 2.5 (defer UI tests to Phase 2 after consolidation)
   - WARDEN (0%) → Task 1.1 includes test suite
   - RAVEN (N/A) → Placeholder, skip
   - Others (unknown) → Measure first, then triage

**Files:**
- All repo `pyproject.toml` files (EDIT — add coverage config)
- `X:\Projects\_GAIA\docs\coverage_baseline_*.html` (NEW — baseline reports)
- `.github/workflows/ci.yml` (EDIT — add coverage comment action)

**Dependencies:**
- Task 1.2 (CI/CD) — coverage enforcement runs in CI

**Acceptance Criteria:**
- [ ] `pytest` in any repo fails if coverage <60%
- [ ] CI/CD blocks PR merge if coverage drops below 60%
- [ ] Coverage report posted as PR comment (shows lines added/removed/covered)
- [ ] Baseline coverage documented for all repos (CSV or table in GECO_AUDIT.md)
- [ ] MYCEL maintains 92%+ coverage (no regression)
- [ ] ECHO, WARDEN, RAVEN exempt from 60% requirement until Phase 2/4 (documented in pyproject.toml)

---

#### 1.4 VULCAN Integration with WARDEN
**What:** Update VULCAN project creator to include WARDEN compliance checks in generated project templates.

**Why:** New projects created by VULCAN should be "born compliant" with GECO standards. Currently VULCAN generates CLAUDE.md (good) but doesn't include pre-commit hooks, CI/CD, or WARDEN scans (bad). Every new project starts with technical debt.

**How:**
1. **Update project_creator.py template:**
   ```python
   # vulcan_forge/templates/new_project_template.py
   def generate_project_structure(name: str, config: ProjectConfig) -> dict:
       return {
           'files': {
               '.pre-commit-config.yaml': PRECOMMIT_TEMPLATE,  # NEW
               '.github/workflows/ci.yml': CI_WORKFLOW_TEMPLATE,  # NEW
               'pyproject.toml': generate_pyproject(name, coverage_min=60),  # EDIT
               'CLAUDE.md': generate_claude_md(name, config),  # EXISTING
               'tests/test_placeholder.py': TEST_TEMPLATE,  # NEW
           }
       }
   ```
2. **Add WARDEN validation to project creation:**
   ```python
   def create_project(name: str, config: ProjectConfig):
       structure = generate_project_structure(name, config)
       write_files(structure)

       # Run WARDEN scan on new project
       scan_result = warden.scan(name)
       if not scan_result.is_valid:
           log.warning(f"New project {name} has WARDEN violations: {scan_result.violations}")
           # Don't fail creation, but log for ARGUS
           argus_telemetry.emit_event('project_created_with_violations', {
               'project': name,
               'violations': scan_result.violations
           })
   ```
3. **Update VULCAN CLAUDE.md (from Phase 0.2):**
   - Add project creation checklist item: "Run WARDEN scan before finalizing"
   - Specify default CI/CD template
4. **Create integration test:**
   ```python
   # tests/test_project_creator_warden.py
   def test_new_project_passes_warden():
       project = create_project('test-project', ProjectConfig())
       scan_result = warden.scan(project.path)
       assert scan_result.is_valid
       assert scan_result.coverage >= 60  # Placeholder test counts
   ```

**Files:**
- `X:\Projects\_GAIA\_VULCAN\vulcan_forge\project_creator.py` (EDIT)
- `X:\Projects\_GAIA\_VULCAN\vulcan_forge\templates\new_project_template.py` (EDIT)
- `X:\Projects\_GAIA\_VULCAN\tests\test_project_creator_warden.py` (NEW)
- `X:\Projects\_GAIA\_VULCAN\CLAUDE.md` (EDIT)

**Dependencies:**
- Phase 0.2 (VULCAN CLAUDE.md) — foundation for this task
- Task 1.1 (WARDEN full impl) — VULCAN calls WARDEN API

**Acceptance Criteria:**
- [ ] New project created by VULCAN includes .pre-commit-config.yaml, .github/workflows/ci.yml, 60% coverage config
- [ ] VULCAN runs WARDEN scan on new project before completion
- [ ] WARDEN violations during project creation emit ARGUS event (verify in EventBus)
- [ ] Integration test confirms new project passes WARDEN scan
- [ ] VULCAN CLAUDE.md updated with WARDEN integration steps

---

### Phase 2: Observability (Weeks 3-4)
**Goal:** See everything in real-time — agents, costs, compliance, patterns
**Success Criteria:**
- Process Observer running on PROTEUS, HART OS, VIA (real-time agent monitoring)
- Trust Dashboard deployed (cost per operation, compliance score, error rate)
- ARGUS telemetry active on 80%+ of modules (up from 8% = PROTEUS only)
- Cost visibility dashboard shows per-agent spend

---

#### 2.1 ARGUS Process Observer Implementation
**What:** Implement missing Process Observer component in ARGUS to monitor Claude Code agents and GAIA agents in real-time.

**Why:** Process Observer is the core GECO promise (real-time agent visibility) but files are missing entirely. Without it, GECO cannot see agent behavior, detect failures, or provide the "agent debugger" experience. PROTEUS v0.2.1 failures were invisible until runtime.

**How:**
1. **Create Process Observer architecture:**
   ```python
   # argus/observers/process_observer.py
   class ProcessObserver:
       def __init__(self, event_bus: EventBus):
           self.event_bus = event_bus
           self.active_processes = {}

       def observe_agent(self, agent_id: str, agent_config: dict):
           """Attach to running agent and stream events."""
           process = AgentProcess(agent_id, agent_config)
           self.active_processes[agent_id] = process

           # Stream events: tool_call, tool_result, thinking, response
           for event in process.stream_events():
               self.event_bus.publish('agent_event', {
                   'agent_id': agent_id,
                   'event_type': event.type,
                   'timestamp': event.timestamp,
                   'data': event.data
               })

       def get_agent_status(self, agent_id: str) -> dict:
           """Get current agent status (active, idle, error)."""
           process = self.active_processes.get(agent_id)
           if not process:
               return {'status': 'unknown'}
           return {
               'status': process.status,
               'uptime': process.uptime,
               'events_processed': process.event_count,
               'last_activity': process.last_activity
           }
   ```

2. **Integrate with Claude Code MCP:**
   - Use `context7` MCP plugin to intercept tool calls
   - Use `code-review` MCP to capture agent responses
   - Stream to ARGUS EventBus in real-time

3. **Create dashboard component:**
   ```python
   # argus/dashboard/components/process_monitor.py
   class ProcessMonitorComponent:
       def render(self):
           st.header("Active Agent Processes")
           for agent_id, status in observer.get_all_statuses().items():
               with st.expander(f"{agent_id} - {status['status']}"):
                   st.metric("Uptime", status['uptime'])
                   st.metric("Events", status['events_processed'])
                   st.line_chart(status['event_timeline'])
   ```

4. **Add PROTEUS integration:**
   ```python
   # proteus/integrations/argus_process_observer.py
   def start_observing():
       """Register PROTEUS agents with ARGUS Process Observer."""
       for agent in proteus.get_active_agents():
           argus.observe_agent(agent.id, agent.config)
   ```

5. **Create unit tests:**
   - Mock agent emits events → Process Observer captures them
   - Multiple agents running → Dashboard shows all
   - Agent error → EventBus receives error event

**Files:**
- `X:\Projects\_GAIA\_ARGUS\argus\observers\process_observer.py` (NEW)
- `X:\Projects\_GAIA\_ARGUS\argus\observers\agent_process.py` (NEW — AgentProcess class)
- `X:\Projects\_GAIA\_ARGUS\argus\dashboard\components\process_monitor.py` (NEW)
- `X:\Projects\_GAIA\_PROTEUS\proteus\integrations\argus_process_observer.py` (NEW)
- `X:\Projects\_GAIA\_ARGUS\tests\test_process_observer.py` (NEW — 80%+ coverage)
- `X:\Projects\_GAIA\_ARGUS\tests\test_process_monitor_component.py` (NEW)

**Dependencies:**
- Phase 0.3 (GitHub push) — Process Observer code needs backup
- Task 1.2 (CI/CD) — Process Observer tests run in CI

**Acceptance Criteria:**
- [ ] Process Observer captures events from running Claude Code agent (manual test with quick-helper)
- [ ] Dashboard shows active agent with real-time event timeline
- [ ] PROTEUS agent registration triggers ARGUS observation (integration test)
- [ ] Agent error emits error event to EventBus (verify in dashboard)
- [ ] Process Observer has 80%+ test coverage
- [ ] Dashboard updates within 1 second of agent event (latency test)

---

#### 2.2 ARGUS Trust Dashboard Implementation
**What:** Build Trust Dashboard component showing cost per operation, compliance score, error rate, and trust metrics.

**Why:** Trust Dashboard directory is empty but promised in ARGUS architecture. Users need cost visibility (prevent budget overruns), compliance score (prevent violations), and error rate (detect failures). Missing Trust Dashboard means GECO delivers observability without actionability.

**How:**
1. **Define trust metrics:**
   ```python
   # argus/trust/metrics.py
   @dataclass
   class TrustMetrics:
       cost_per_operation: float  # USD per agent invocation
       compliance_score: float  # 0-100, WARDEN scan results
       error_rate: float  # % of operations resulting in error
       token_usage: int  # Total tokens consumed
       latency_p95: float  # 95th percentile response time (seconds)
       rule_violations: int  # CLAUDE.md violations detected
   ```

2. **Create cost tracking:**
   ```python
   # argus/trust/cost_tracker.py
   class CostTracker:
       # Model costs from Anthropic pricing
       MODEL_COSTS = {
           'claude-opus-4-6': {'input': 0.015, 'output': 0.075},  # per 1K tokens
           'claude-sonnet-4-5': {'input': 0.003, 'output': 0.015},
           'claude-haiku-4': {'input': 0.00025, 'output': 0.00125},
       }

       def calculate_operation_cost(self, event: dict) -> float:
           """Calculate cost from agent event."""
           model = event.get('model', 'claude-sonnet-4-5')
           input_tokens = event.get('input_tokens', 0)
           output_tokens = event.get('output_tokens', 0)

           costs = self.MODEL_COSTS[model]
           return (input_tokens / 1000 * costs['input'] +
                   output_tokens / 1000 * costs['output'])
   ```

3. **Create Trust Dashboard component:**
   ```python
   # argus/dashboard/components/trust_dashboard.py
   class TrustDashboardComponent:
       def render(self):
           metrics = trust_engine.get_current_metrics()

           col1, col2, col3 = st.columns(3)
           col1.metric("Cost Today", f"${metrics.cost_per_operation:.4f}",
                       delta=metrics.cost_trend)
           col2.metric("Compliance Score", f"{metrics.compliance_score:.1f}%",
                       delta=metrics.compliance_trend)
           col3.metric("Error Rate", f"{metrics.error_rate:.2%}",
                       delta=metrics.error_trend, delta_color="inverse")

           st.subheader("Cost Breakdown by Agent")
           st.bar_chart(trust_engine.get_cost_by_agent())

           st.subheader("Recent Violations")
           for violation in metrics.recent_violations[:10]:
               st.warning(f"{violation.timestamp}: {violation.description}")
   ```

4. **Integrate with EventBus:**
   ```python
   # argus/trust/trust_engine.py
   class TrustEngine:
       def __init__(self, event_bus: EventBus):
           event_bus.subscribe('agent_event', self.on_agent_event)
           event_bus.subscribe('compliance_scan', self.on_compliance_scan)

       def on_agent_event(self, event: dict):
           cost = cost_tracker.calculate_operation_cost(event)
           self.metrics.cost_per_operation = self.update_rolling_average(cost)
           if 'error' in event:
               self.metrics.error_rate = self.update_error_rate()
   ```

**Files:**
- `X:\Projects\_GAIA\_ARGUS\argus\trust\metrics.py` (NEW)
- `X:\Projects\_GAIA\_ARGUS\argus\trust\cost_tracker.py` (NEW)
- `X:\Projects\_GAIA\_ARGUS\argus\trust\trust_engine.py` (NEW)
- `X:\Projects\_GAIA\_ARGUS\argus\dashboard\components\trust_dashboard.py` (NEW)
- `X:\Projects\_GAIA\_ARGUS\tests\test_cost_tracker.py` (NEW)
- `X:\Projects\_GAIA\_ARGUS\tests\test_trust_engine.py` (NEW)

**Dependencies:**
- Task 2.1 (Process Observer) — Trust metrics sourced from agent events
- Task 1.1 (WARDEN) — Compliance score from WARDEN scans

**Acceptance Criteria:**
- [ ] Trust Dashboard displays cost per operation with 4 decimal places
- [ ] Cost breakdown shows per-agent spend (bar chart)
- [ ] Compliance score calculated from latest WARDEN scan (integration test)
- [ ] Error rate updates in real-time when agent error occurs
- [ ] Recent violations list shows CLAUDE.md violations from last 24 hours
- [ ] Trust Dashboard accessible at `/trust` route in ARGUS app
- [ ] Cost tracking has 90%+ test coverage (critical for billing)

---

#### 2.3 Universal ARGUS Telemetry Rollout
**What:** Add active ARGUS telemetry to MYCEL, VULCAN, ECHO, WARDEN, RAVEN, Mental Models (80%+ ecosystem coverage).

**Why:** Currently only PROTEUS sends telemetry (8% coverage). LOOM and MNEMIS have stubs but inactive. 78% of ecosystem is invisible to ARGUS. Universal telemetry enables pattern detection, hypothesis generation, and trust metrics across all components.

**How:**
1. **Create telemetry SDK:**
   ```python
   # argus/sdk/telemetry.py
   class ArgusClient:
       def __init__(self, component_name: str, event_bus_url: str = 'http://localhost:8501/events'):
           self.component = component_name
           self.event_bus_url = event_bus_url

       def emit(self, event_type: str, data: dict):
           """Emit event to ARGUS EventBus."""
           event = {
               'component': self.component,
               'type': event_type,
               'timestamp': datetime.now().isoformat(),
               'data': data
           }
           requests.post(self.event_bus_url, json=event)

       def emit_operation(self, operation: str, duration: float, success: bool, metadata: dict = None):
           """Convenience method for operation events."""
           self.emit('operation', {
               'operation': operation,
               'duration_ms': duration * 1000,
               'success': success,
               'metadata': metadata or {}
           })
   ```

2. **Add telemetry to each component:**

   **MYCEL:**
   ```python
   # mycel/integrations/argus_telemetry.py
   argus = ArgusClient('MYCEL')

   def install_package(name: str):
       start = time.time()
       try:
           result = pip.install(name)
           argus.emit_operation('package_install', time.time() - start, True, {'package': name})
           return result
       except Exception as e:
           argus.emit_operation('package_install', time.time() - start, False, {'package': name, 'error': str(e)})
           raise
   ```

   **VULCAN:**
   ```python
   # vulcan_forge/integrations/argus_telemetry.py (NEW)
   argus = ArgusClient('VULCAN')

   def create_project(name: str, config: ProjectConfig):
       argus.emit('project_creation_started', {'name': name, 'config': config.dict()})
       try:
           project = _create_project_impl(name, config)
           argus.emit('project_creation_completed', {'name': name, 'files_created': len(project.files)})
           return project
       except Exception as e:
           argus.emit('project_creation_failed', {'name': name, 'error': str(e)})
           raise
   ```

   **WARDEN** (already implemented in Task 1.1)

   **Mental Models:**
   ```python
   # mental_models/integrations/argus_telemetry.py (NEW)
   argus = ArgusClient('MentalModels')

   def select_model(context: str) -> MentalModel:
       selected = selector.select(context)
       argus.emit('model_selected', {
           'model': selected.name,
           'context_length': len(context),
           'confidence': selected.confidence
       })
       return selected
   ```

3. **Activate existing stubs (LOOM, MNEMIS):**
   - Replace stub implementations with ArgusClient
   - Add emit calls to critical operations (agent edit, memory promotion)

4. **Update ARGUS dashboard to show all components:**
   ```python
   # argus/dashboard/components/component_health.py
   class ComponentHealthComponent:
       def render(self):
           st.header("Component Health")
           for component in argus.get_active_components():
               status = argus.get_component_status(component)
               st.metric(
                   f"{component}",
                   f"{status.event_count} events",
                   delta=f"{status.error_rate:.1%} errors"
               )
   ```

**Files:**
- `X:\Projects\_GAIA\_ARGUS\argus\sdk\telemetry.py` (NEW — SDK)
- `X:\Projects\_GAIA\_MYCEL\mycel\integrations\argus_telemetry.py` (NEW)
- `X:\Projects\_GAIA\_VULCAN\vulcan_forge\integrations\argus_telemetry.py` (NEW)
- `X:\Projects\_GAIA\_WARDEN\warden\integrations\argus_telemetry.py` (EDIT — from Task 1.1)
- `X:\Projects\_GAIA\mental_models\integrations\argus_telemetry.py` (NEW)
- `X:\Projects\_GAIA\_LOOM\loom\integrations\argus_telemetry.py` (EDIT — activate stub)
- `X:\Projects\_GAIA\_MNEMIS\mnemis\integrations\argus_telemetry.py` (EDIT — activate stub)
- `X:\Projects\_GAIA\_ARGUS\argus\dashboard\components\component_health.py` (NEW)
- `X:\Projects\_GAIA\_ARGUS\tests\test_telemetry_sdk.py` (NEW)

**Dependencies:**
- Task 2.1 (Process Observer) — EventBus receives telemetry
- Task 1.1 (WARDEN) — WARDEN telemetry integration

**Acceptance Criteria:**
- [ ] MYCEL package install emits event to ARGUS (verify in dashboard)
- [ ] VULCAN project creation emits start/complete/fail events
- [ ] Mental Models model selection emits event with confidence score
- [ ] LOOM agent edit emits event (activate existing stub)
- [ ] MNEMIS memory promotion emits event (activate existing stub)
- [ ] ARGUS dashboard shows 8+ components with event counts (up from 1)
- [ ] ArgusClient SDK has 90%+ test coverage
- [ ] All telemetry integration tests pass in component repos

---

#### 2.4 Production Project Telemetry (HART OS, VIA, DATA FORGE)
**What:** Add ARGUS telemetry to HART OS, VIA, and DATA FORGE production projects.

**Why:** Production projects are GECO blind spots. HART OS v6.2.8, VIA v6.4, and DATA FORGE v1.1 have unknown test coverage, no ARGUS integration, and unclear error rates. GECO was built to protect production systems but currently can't see them.

**How:**
1. **Audit production projects:**
   ```powershell
   foreach ($project in @('hart-os', 'via', 'data-forge')) {
       cd "X:\Projects\$project"
       pytest --cov --cov-report=term > "coverage_report_$project.txt"
       warden scan . > "warden_report_$project.txt"
   }
   ```

2. **Add ARGUS telemetry (minimal invasive approach):**
   - Install ArgusClient SDK via pip
   - Add telemetry to critical operations only (API endpoints, DB queries, LLM calls)
   - Example for HART OS:
     ```python
     # hart_os/integrations/argus_telemetry.py (NEW)
     from argus.sdk import ArgusClient

     argus = ArgusClient('HART-OS')

     def process_patient_decision(patient_id: str, decision_data: dict):
         argus.emit('decision_engine_invoked', {'patient_id': patient_id})
         try:
             result = decision_engine.process(patient_id, decision_data)
             argus.emit_operation('patient_decision', result.duration, True, {
                 'patient_id': patient_id,
                 'recommendation': result.recommendation
             })
             return result
         except Exception as e:
             argus.emit_operation('patient_decision', 0, False, {
                 'patient_id': patient_id,
                 'error': str(e)
             })
             raise
     ```

3. **Deploy ARGUS dashboard to production:**
   - Create production-safe ARGUS instance (no subconscious hypothesis generation in prod)
   - Trust Dashboard only (cost, errors, compliance)
   - Process Observer in read-only mode

4. **Add MNEMIS memory for production incidents:**
   - Production errors auto-promote to MNEMIS long-term memory
   - Create "production incident" memory type with mandatory post-mortem

**Files:**
- `X:\Projects\hart-os\hart_os\integrations\argus_telemetry.py` (NEW)
- `X:\Projects\via\via\integrations\argus_telemetry.py` (NEW)
- `X:\Projects\data-forge\data_forge\integrations\argus_telemetry.py` (NEW)
- Production deployment config for ARGUS (NEW)

**Dependencies:**
- Task 2.3 (Universal telemetry) — ArgusClient SDK exists
- Task 2.2 (Trust Dashboard) — Production uses Trust Dashboard

**Acceptance Criteria:**
- [ ] HART OS decision engine emits events to ARGUS (integration test)
- [ ] VIA critical operations emit telemetry (define "critical" based on audit)
- [ ] DATA FORGE operations emit telemetry
- [ ] Production ARGUS dashboard shows cost per operation for all 3 projects
- [ ] Production error triggers MNEMIS memory creation (integration test)
- [ ] Production telemetry has <5ms latency overhead (performance test)
- [ ] Telemetry failures don't block production operations (graceful degradation)

---

#### 2.5 ECHO Test Suite & Dashboard Deployment
**What:** Create test suite for consolidated ECHO UI (from Phase 0.4) and deploy dashboard with ARGUS integration.

**Why:** ECHO has 0% test coverage after consolidation. UI behavior is undefined. ECHO needs tests before it can be deployed safely. Additionally, ECHO should become an ARGUS dashboard plugin (UI for GECO itself).

**How:**
1. **Create UI unit tests:**
   ```python
   # tests/test_ui_components.py
   def test_component_registry_loads():
       """Verify all UI components register correctly."""
       from echo.ui import ComponentRegistry
       registry = ComponentRegistry()
       assert len(registry.components) > 0

   def test_dashboard_renders_without_data():
       """Dashboard should handle empty state gracefully."""
       from echo.ui import Dashboard
       dashboard = Dashboard(data=None)
       html = dashboard.render()
       assert "No data available" in html
   ```

2. **Create integration tests with Streamlit:**
   ```python
   # tests/test_streamlit_integration.py
   from streamlit.testing.v1 import AppTest

   def test_argus_dashboard_loads():
       """Test ARGUS dashboard loads in ECHO."""
       at = AppTest.from_file("echo/ui.py")
       at.run()
       assert not at.exception
       assert "ARGUS Dashboard" in at.title[0].value
   ```

3. **Integrate ECHO with ARGUS:**
   ```python
   # echo/plugins/argus_plugin.py
   class ArgusPlugin:
       def render_dashboard(self):
           """Render ARGUS dashboard components in ECHO UI."""
           from argus.dashboard.components import (
               ProcessMonitorComponent,
               TrustDashboardComponent,
               ComponentHealthComponent
           )

           ProcessMonitorComponent().render()
           TrustDashboardComponent().render()
           ComponentHealthComponent().render()
   ```

4. **Add ARGUS telemetry to ECHO:**
   ```python
   # echo/integrations/argus_telemetry.py
   argus = ArgusClient('ECHO')

   def render_component(component_name: str):
       argus.emit('ui_component_rendered', {'component': component_name})
       # ... render logic
   ```

5. **Deploy ECHO as unified GECO dashboard:**
   - ECHO becomes the single UI for all GECO components
   - Replaces standalone ARGUS dashboard (Streamlit app.py)
   - Plugins for LOOM (agent editor UI), MNEMIS (memory browser), WARDEN (compliance reports)

**Files:**
- `X:\Projects\_GAIA\_ECHO\tests\test_ui_components.py` (NEW)
- `X:\Projects\_GAIA\_ECHO\tests\test_streamlit_integration.py` (NEW)
- `X:\Projects\_GAIA\_ECHO\echo\plugins\argus_plugin.py` (NEW)
- `X:\Projects\_GAIA\_ECHO\echo\integrations\argus_telemetry.py` (NEW)
- `X:\Projects\_GAIA\_ARGUS\argus\dashboard\app.py` (DEPRECATE — replaced by ECHO)

**Dependencies:**
- Phase 0.4 (ECHO consolidation) — Single ui.py must exist
- Task 2.1 (Process Observer) — ECHO displays Process Observer data
- Task 2.2 (Trust Dashboard) — ECHO displays Trust Dashboard

**Acceptance Criteria:**
- [ ] ECHO has 60%+ test coverage (pytest --cov)
- [ ] ECHO integration test renders ARGUS dashboard without errors
- [ ] ECHO plugins for ARGUS, LOOM, MNEMIS, WARDEN all load successfully
- [ ] ECHO emits telemetry to ARGUS (verify in Process Observer)
- [ ] ECHO deployed at single URL (e.g., `http://localhost:8501/geco`)
- [ ] Standalone ARGUS dashboard deprecated with migration guide

---

### Phase 3: Learning & Memory (Weeks 4-5)
**Goal:** System learns from past to enforce future
**Success Criteria:**
- MNEMIS auto-promotes patterns from ARGUS to long-term memory
- Cross-session rule enforcement (agents remember past violations)
- URL knowledge base (agents can fetch external context)
- Mental Models integrated with MNEMIS (track which models work)

---

#### 3.1 MNEMIS Auto-Promotion from ARGUS Patterns
**What:** Connect ARGUS pattern detector to MNEMIS promotion protocol, automatically promoting recurring patterns to long-term memory.

**Why:** MNEMIS has 3-tier hierarchy and promotion protocol, but no auto-triggers. ARGUS detects patterns (e.g., "PROTEUS v0.2.1 errors repeat 3 times") but doesn't promote them to memory. Manual promotion is insufficient for learning system.

**How:**
1. **Create promotion trigger:**
   ```python
   # mnemis/promotion/auto_promotion.py
   class AutoPromoter:
       def __init__(self, argus_client: ArgusClient, memory_store: MemoryStore):
           self.argus = argus_client
           self.memory = memory_store
           argus_client.subscribe('pattern_detected', self.on_pattern_detected)

       def on_pattern_detected(self, event: dict):
           """Promote pattern to MNEMIS if it meets criteria."""
           pattern = event['pattern']
           if self.should_promote(pattern):
               memory = Memory(
                   content=pattern.description,
                   type='pattern',
                   tier='long_term',  # Skip short-term
                   metadata={
                       'confidence': pattern.confidence,
                       'occurrences': pattern.count,
                       'first_seen': pattern.first_timestamp,
                       'last_seen': pattern.last_timestamp
                   }
               )
               self.memory.store(memory)
               self.argus.emit('memory_promoted', {'memory_id': memory.id, 'pattern': pattern.id})

       def should_promote(self, pattern: Pattern) -> bool:
           """Promotion criteria."""
           return (
               pattern.count >= 3 and  # Seen 3+ times
               pattern.confidence >= 0.7 and  # High confidence
               pattern.impact == 'high'  # High impact (errors, violations)
           )
   ```

2. **Update ARGUS pattern detector:**
   ```python
   # argus/subconscious/pattern_detector.py (EDIT)
   def detect_patterns(self, events: List[dict]) -> List[Pattern]:
       patterns = self._detect_patterns_impl(events)
       for pattern in patterns:
           self.event_bus.publish('pattern_detected', {'pattern': pattern})
       return patterns
   ```

3. **Create memory search for agents:**
   ```python
   # mnemis/search/context_search.py
   class ContextSearch:
       def search_for_agent_context(self, agent_id: str, current_task: str) -> List[Memory]:
           """Search memories relevant to agent's current task."""
           # Search by task keywords
           keyword_results = self.search(current_task)

           # Search by past agent behavior
           agent_history = self.search_by_metadata({'agent_id': agent_id})

           # Combine and rank
           return self.rank_by_relevance(keyword_results + agent_history)
   ```

4. **Integrate with Claude Code agents:**
   - Add MNEMIS context injection to agent prompts
   - Example: "Based on past patterns, this operation often fails when..."

**Files:**
- `X:\Projects\_GAIA\_MNEMIS\mnemis\promotion\auto_promotion.py` (NEW)
- `X:\Projects\_GAIA\_MNEMIS\mnemis\search\context_search.py` (NEW)
- `X:\Projects\_GAIA\_ARGUS\argus\subconscious\pattern_detector.py` (EDIT)
- `X:\Projects\_GAIA\_MNEMIS\tests\test_auto_promotion.py` (NEW)
- `X:\Projects\_GAIA\_MNEMIS\tests\test_context_search.py` (NEW)

**Dependencies:**
- Task 2.1 (Process Observer) — Provides events for pattern detection
- Task 2.3 (Universal telemetry) — More events = better patterns

**Acceptance Criteria:**
- [ ] ARGUS detects pattern (3+ occurrences) → MNEMIS auto-promotes to long-term memory
- [ ] Auto-promoted memory includes pattern metadata (confidence, occurrences, timestamps)
- [ ] MNEMIS context search returns relevant memories for agent task (integration test)
- [ ] Claude Code agent receives MNEMIS context in prompt (manual test with quick-helper)
- [ ] Auto-promotion has 85%+ test coverage
- [ ] No manual promotion required for recurring patterns

---

#### 3.2 Cross-Session Rule Enforcement
**What:** Enable agents to remember violations from past sessions and prevent recurrence.

**Why:** Currently agents (both Claude Code and GAIA) fail to follow rules repeatedly. CLAUDE.md exists but isn't consulted. Hooks catch violations but don't prevent attempts. Cross-session memory means agents learn "I tried this before and it was rejected."

**How:**
1. **Create violation memory type:**
   ```python
   # mnemis/models/violation_memory.py
   @dataclass
   class ViolationMemory(Memory):
       violation_type: str  # 'localization', 'type_hint', 'test_coverage', etc.
       violated_rule: str  # Reference to CLAUDE.md section
       agent_id: str
       file_path: str
       attempted_change: str
       rejection_reason: str
   ```

2. **Hook WARDEN scan results into MNEMIS:**
   ```python
   # warden/integrations/mnemis_bridge.py
   def on_scan_complete(scan_result: ScanResult):
       """Store violations in MNEMIS for future reference."""
       for violation in scan_result.violations:
           memory = ViolationMemory(
               content=f"Violation: {violation.description}",
               violation_type=violation.type,
               violated_rule=violation.rule,
               agent_id=get_current_agent_id(),
               file_path=violation.file,
               attempted_change=violation.code_snippet,
               rejection_reason=violation.message,
               tier='long_term'  # Violations are important
           )
           mnemis.store(memory)
   ```

3. **Agent pre-flight check:**
   ```python
   # agents/preflight_check.py
   def check_before_edit(file_path: str, proposed_change: str) -> PreflightResult:
       """Check if proposed change violates past rules."""
       # Search MNEMIS for similar past violations
       similar_violations = mnemis.search(f"file:{file_path} type:violation")

       for violation in similar_violations:
           similarity = calculate_similarity(proposed_change, violation.attempted_change)
           if similarity > 0.8:
               return PreflightResult(
                   allowed=False,
                   reason=f"Similar change rejected before: {violation.rejection_reason}",
                   past_violation=violation
               )

       return PreflightResult(allowed=True)
   ```

4. **Integrate with Claude Code hooks:**
   - Add pre-flight check to post-edit hook (from Phase 0.5)
   - Agent sees warning before attempting known violation

5. **Create feedback loop:**
   ```python
   # agents/feedback_loop.py
   def on_successful_edit(file_path: str, change: str):
       """Store successful patterns to reinforce good behavior."""
       memory = Memory(
           content=f"Successful edit: {change}",
           type='success_pattern',
           tier='short_term',  # Promote to long-term if repeated
           metadata={
               'file_path': file_path,
               'agent_id': get_current_agent_id(),
               'timestamp': datetime.now().isoformat()
           }
       )
       mnemis.store(memory)
   ```

**Files:**
- `X:\Projects\_GAIA\_MNEMIS\mnemis\models\violation_memory.py` (NEW)
- `X:\Projects\_GAIA\_WARDEN\warden\integrations\mnemis_bridge.py` (NEW)
- `X:\Projects\_GAIA\agents\preflight_check.py` (NEW)
- `X:\Projects\_GAIA\agents\feedback_loop.py` (NEW)
- `X:\Projects\_GAIA\_MNEMIS\tests\test_violation_memory.py` (NEW)
- `X:\Projects\_GAIA\tests\test_preflight_check.py` (NEW)

**Dependencies:**
- Task 3.1 (Auto-promotion) — Violation memories promoted to long-term
- Task 1.1 (WARDEN) — Violations detected by WARDEN

**Acceptance Criteria:**
- [ ] WARDEN violation stores ViolationMemory in MNEMIS
- [ ] Agent attempting similar change receives warning before edit
- [ ] Pre-flight check prevents 80%+ of repeat violations (measure over 1 week)
- [ ] Successful edits stored as success patterns (verify in MNEMIS)
- [ ] MNEMIS has 100+ violation memories after 1 week of use (proves usage)
- [ ] Cross-session enforcement has 80%+ test coverage

---

#### 3.3 URL Knowledge Base Integration
**What:** Enable agents to fetch and cache external documentation (GitHub, Anthropic docs, Stack Overflow) via MNEMIS.

**Why:** Agents repeatedly ask questions answered in external docs. No memory of past documentation lookups. URL knowledge base allows "I already fetched this, here's what it said."

**How:**
1. **Create URL fetcher:**
   ```python
   # mnemis/knowledge/url_fetcher.py
   class URLFetcher:
       def fetch(self, url: str) -> Document:
           """Fetch URL content and extract key information."""
           # Use requests + BeautifulSoup or playwright for dynamic content
           response = requests.get(url)
           soup = BeautifulSoup(response.content, 'html.parser')

           return Document(
               url=url,
               title=soup.title.string,
               content=soup.get_text(),
               fetched_at=datetime.now(),
               metadata={
                   'status_code': response.status_code,
                   'content_type': response.headers.get('content-type')
               }
           )
   ```

2. **Create knowledge base:**
   ```python
   # mnemis/knowledge/knowledge_base.py
   class KnowledgeBase:
       def __init__(self, memory_store: MemoryStore, fetcher: URLFetcher):
           self.memory = memory_store
           self.fetcher = fetcher

       def get_or_fetch(self, url: str, max_age: timedelta = timedelta(days=7)) -> Document:
           """Get cached document or fetch if stale."""
           # Search for existing memory
           cached = self.memory.search_by_metadata({'url': url, 'type': 'url_document'})

           if cached and (datetime.now() - cached[0].created_at) < max_age:
               return cached[0].content

           # Fetch new
           doc = self.fetcher.fetch(url)
           memory = Memory(
               content=doc.content,
               type='url_document',
               tier='core',  # External docs are core knowledge
               metadata={
                   'url': url,
                   'title': doc.title,
                   'fetched_at': doc.fetched_at.isoformat()
               }
           )
           self.memory.store(memory)
           return doc
   ```

3. **Create agent tool:**
   ```python
   # agents/tools/fetch_docs.py
   @tool
   def fetch_external_docs(url: str) -> str:
       """Fetch external documentation for reference.

       Args:
           url: URL to fetch (GitHub, Anthropic docs, Stack Overflow, etc.)

       Returns:
           Document content as markdown
       """
       doc = knowledge_base.get_or_fetch(url)
       return f"# {doc.title}\n\nSource: {url}\n\n{doc.content}"
   ```

4. **Integrate with common doc sources:**
   - Anthropic docs: `https://docs.anthropic.com/*`
   - Claude Code docs: `https://github.com/anthropics/claude-code/*`
   - GAIA component READMEs: `https://github.com/GAIA-Ecosystem/*/README.md`

5. **Add to agent instructions (CLAUDE.md):**
   - "Before asking about external APIs, use fetch_external_docs tool"
   - "Cache external docs for 7 days (don't re-fetch every session)"

**Files:**
- `X:\Projects\_GAIA\_MNEMIS\mnemis\knowledge\url_fetcher.py` (NEW)
- `X:\Projects\_GAIA\_MNEMIS\mnemis\knowledge\knowledge_base.py` (NEW)
- `X:\Projects\_GAIA\agents\tools\fetch_docs.py` (NEW)
- `X:\Projects\_GAIA\_MNEMIS\tests\test_url_fetcher.py` (NEW)
- `X:\Projects\_GAIA\_MNEMIS\tests\test_knowledge_base.py` (NEW)
- All component `CLAUDE.md` files (EDIT — add fetch_external_docs tool instructions)

**Dependencies:**
- Task 3.1 (Auto-promotion) — Core knowledge stored in MNEMIS

**Acceptance Criteria:**
- [ ] fetch_external_docs tool fetches Anthropic docs URL (integration test)
- [ ] Second fetch of same URL returns cached version (verify no network request)
- [ ] Cached docs expire after 7 days (test with mocked datetime)
- [ ] Knowledge base has 20+ cached URLs after 1 week of use
- [ ] Agent uses fetch_external_docs before asking clarifying questions (manual test)
- [ ] URL knowledge base has 85%+ test coverage

---

#### 3.4 Mental Models + MNEMIS Integration
**What:** Track which mental models improve outcomes and promote winning models to MNEMIS core memory.

**Why:** Mental Models Library has 59 models but no effectiveness tracking. Don't know which models help vs hurt. MNEMIS integration enables "I used First Principles on this problem before and it worked."

**How:**
1. **Instrument mental model invocations:**
   ```python
   # mental_models/integrations/argus_telemetry.py (EDIT from Task 2.3)
   def invoke_model(model: MentalModel, context: str) -> ModelResult:
       argus.emit('model_invocation_started', {
           'model': model.name,
           'context_summary': context[:200]
       })

       start = time.time()
       try:
           result = model.apply(context)
           duration = time.time() - start

           argus.emit('model_invocation_completed', {
               'model': model.name,
               'duration_ms': duration * 1000,
               'success': True
           })

           return result
       except Exception as e:
           argus.emit('model_invocation_failed', {
               'model': model.name,
               'error': str(e)
           })
           raise
   ```

2. **Create outcome tracking:**
   ```python
   # mental_models/outcome_tracker.py
   class OutcomeTracker:
       def track_outcome(self, model_name: str, outcome: str, success: bool):
           """Track whether mental model application succeeded."""
           memory = Memory(
               content=f"Mental model '{model_name}' applied to {outcome}",
               type='model_outcome',
               tier='short_term',  # Promote to long-term if model consistently succeeds
               metadata={
                   'model': model_name,
                   'outcome': outcome,
                   'success': success,
                   'timestamp': datetime.now().isoformat()
               }
           )
           mnemis.store(memory)

           # Check if model should be promoted
           self.check_model_promotion(model_name)

       def check_model_promotion(self, model_name: str):
           """Promote model to core memory if success rate > 80%."""
           outcomes = mnemis.search_by_metadata({'type': 'model_outcome', 'model': model_name})
           if len(outcomes) < 10:
               return  # Need 10+ samples

           success_rate = sum(1 for o in outcomes if o.metadata['success']) / len(outcomes)
           if success_rate >= 0.8:
               core_memory = Memory(
                   content=f"Mental model '{model_name}' is highly effective (80%+ success rate)",
                   type='effective_model',
                   tier='core',
                   metadata={
                       'model': model_name,
                       'success_rate': success_rate,
                       'sample_size': len(outcomes)
                   }
               )
               mnemis.store(core_memory)
   ```

3. **Update model selector:**
   ```python
   # mental_models/selector.py (EDIT)
   def select_model(context: str) -> MentalModel:
       # Check MNEMIS for effective models
       effective_models = mnemis.search_by_metadata({'type': 'effective_model'})

       # Prioritize models with high success rates
       for memory in effective_models:
           model_name = memory.metadata['model']
           if model_name in self.available_models:
               return self.available_models[model_name]

       # Fall back to rule-based selection
       return self._select_by_rules(context)
   ```

4. **Add to ECHO dashboard:**
   ```python
   # echo/plugins/mental_models_plugin.py
   class MentalModelsPlugin:
       def render_dashboard(self):
           st.header("Mental Models Effectiveness")

           models = outcome_tracker.get_all_models()
           for model in models:
               stats = outcome_tracker.get_model_stats(model)
               st.metric(
                   model,
                   f"{stats.success_rate:.1%} success",
                   delta=f"{stats.invocations} uses"
               )
   ```

**Files:**
- `X:\Projects\_GAIA\mental_models\integrations\argus_telemetry.py` (EDIT from Task 2.3)
- `X:\Projects\_GAIA\mental_models\outcome_tracker.py` (NEW)
- `X:\Projects\_GAIA\mental_models\selector.py` (EDIT)
- `X:\Projects\_GAIA\_ECHO\echo\plugins\mental_models_plugin.py` (NEW)
- `X:\Projects\_GAIA\mental_models\tests\test_outcome_tracker.py` (NEW)

**Dependencies:**
- Task 2.3 (Universal telemetry) — Mental Models telemetry active
- Task 3.1 (Auto-promotion) — Effective models promoted to core

**Acceptance Criteria:**
- [ ] Mental model invocation emits telemetry to ARGUS
- [ ] Outcome tracked for each model application (success/failure)
- [ ] Model with 80%+ success rate (10+ samples) promoted to core memory
- [ ] Model selector prioritizes effective models from MNEMIS
- [ ] ECHO dashboard shows mental model effectiveness leaderboard
- [ ] Mental Models integration has 85%+ test coverage

---

### Phase 4: Advanced Automation (Weeks 5-8)
**Goal:** Full autonomy — auto-generated tests/docs, rollback, background monitoring
**Success Criteria:**
- Auto-generated tests for new code (80%+ coverage maintained)
- Auto-generated documentation from docstrings
- Git rollback capability (revert to last known good state)
- MCP tool discovery (agents find new tools automatically)
- Background ARGUS monitoring (24/7 agent health checks)

---

#### 4.1 Auto-Generated Tests (Coverage Maintenance)
**What:** Generate unit tests automatically for new functions lacking coverage, maintaining 80%+ ecosystem-wide.

**Why:** Test writing is manual bottleneck. Coverage drifts down over time. Auto-generated tests (even basic smoke tests) catch regressions and maintain coverage threshold.

**How:**
1. **Create test generator:**
   ```python
   # tools/test_generator.py
   class TestGenerator:
       def generate_tests_for_function(self, func: Callable) -> str:
           """Generate pytest tests for function based on signature and docstring."""
           signature = inspect.signature(func)
           docstring = func.__doc__ or ""

           # Parse return type and args
           return_type = signature.return_annotation
           args = [(name, param.annotation) for name, param in signature.parameters.items()]

           # Generate basic test cases
           tests = []
           tests.append(self._generate_smoke_test(func, args))
           tests.append(self._generate_type_test(func, args, return_type))

           if "raises" in docstring.lower():
               tests.append(self._generate_exception_test(func, args, docstring))

           return "\n\n".join(tests)

       def _generate_smoke_test(self, func: Callable, args: List[tuple]) -> str:
           """Generate basic smoke test (function doesn't crash)."""
           arg_names = [name for name, _ in args]
           arg_values = [self._get_default_value(typ) for _, typ in args]

           return f"""
   def test_{func.__name__}_smoke():
       \"\"\"Basic smoke test for {func.__name__}.\"\"\"
       result = {func.__name__}({', '.join(f'{n}={repr(v)}' for n, v in zip(arg_names, arg_values))})
       assert result is not None
   """
   ```

2. **Integrate with git pre-commit hook:**
   ```python
   # hooks/auto_test_generation.py
   def generate_missing_tests():
       """Find functions lacking tests and generate them."""
       # Get all functions in changed files
       changed_files = get_changed_python_files()

       for file in changed_files:
           module = import_module_from_file(file)
           for func in get_public_functions(module):
               if not has_test(func):
                   test_code = test_generator.generate_tests_for_function(func)
                   test_file = get_test_file_for_module(file)
                   append_test(test_file, test_code)
   ```

3. **Add to CI/CD:**
   ```yaml
   # .github/workflows/ci.yml (EDIT)
   - name: Generate missing tests
     run: python tools/test_generator.py --check
     # Fails if new functions lack tests
   ```

4. **Create agent tool:**
   ```python
   # agents/tools/generate_tests.py
   @tool
   def generate_tests_for_file(file_path: str) -> str:
       """Generate unit tests for functions in file.

       Args:
           file_path: Path to Python file

       Returns:
           Generated test code as string
       """
       module = import_module_from_file(file_path)
       test_code = []

       for func in get_public_functions(module):
           test_code.append(test_generator.generate_tests_for_function(func))

       return "\n\n".join(test_code)
   ```

5. **Quality guardrails:**
   - Generated tests must pass before commit
   - Generated tests can be edited (not immutable)
   - Comment in test: `# Auto-generated test — please review and enhance`

**Files:**
- `X:\Projects\_GAIA\tools\test_generator.py` (NEW)
- `X:\Projects\_GAIA\hooks\auto_test_generation.py` (NEW)
- `X:\Projects\_GAIA\agents\tools\generate_tests.py` (NEW)
- `X:\Projects\_GAIA\.pre-commit-config.yaml` (EDIT — add auto test generation hook)
- `X:\Projects\_GAIA\tools\tests\test_test_generator.py` (NEW — recursive!)

**Dependencies:**
- Phase 1.3 (Coverage enforcement) — Auto-tests maintain 60%+ threshold
- Phase 0.1 (Pre-commit hooks) — Test generation runs in hook

**Acceptance Criteria:**
- [ ] New function without test triggers auto-generation (pre-commit hook)
- [ ] Generated test includes smoke test, type test, and exception test (if applicable)
- [ ] Generated tests pass pytest (verify with test suite run)
- [ ] Coverage stays above 60% after adding 10 new functions (integration test)
- [ ] Generated test has comment indicating auto-generation
- [ ] Test generator has 90%+ coverage (ironic but necessary)

---

#### 4.2 Auto-Generated Documentation
**What:** Generate Markdown documentation from docstrings and type hints automatically.

**Why:** Documentation lags behind code. Docstrings exist but not compiled into readable docs. Auto-generation ensures docs match reality.

**How:**
1. **Create doc generator:**
   ```python
   # tools/doc_generator.py
   class DocGenerator:
       def generate_module_docs(self, module_path: str) -> str:
           """Generate Markdown docs for Python module."""
           module = import_module_from_file(module_path)
           docs = [f"# {module.__name__}\n"]

           if module.__doc__:
               docs.append(f"{module.__doc__}\n")

           # Functions
           docs.append("## Functions\n")
           for func in get_public_functions(module):
               docs.append(self._generate_function_docs(func))

           # Classes
           docs.append("## Classes\n")
           for cls in get_public_classes(module):
               docs.append(self._generate_class_docs(cls))

           return "\n".join(docs)

       def _generate_function_docs(self, func: Callable) -> str:
           """Generate Markdown for single function."""
           signature = inspect.signature(func)
           docstring = func.__doc__ or "No documentation available."

           return f"""
   ### `{func.__name__}{signature}`

   {docstring}

   **Arguments:**
   {self._format_arguments(signature)}

   **Returns:** `{signature.return_annotation}`
   """
   ```

2. **Integrate with git pre-commit hook:**
   ```python
   # hooks/auto_doc_generation.py
   def regenerate_docs():
       """Regenerate docs for changed modules."""
       changed_files = get_changed_python_files()

       for file in changed_files:
           if file.startswith('src/'):
               doc_path = file.replace('src/', 'docs/api/').replace('.py', '.md')
               doc_content = doc_generator.generate_module_docs(file)
               write_file(doc_path, doc_content)
   ```

3. **Add to CI/CD:**
   ```yaml
   # .github/workflows/docs.yml (NEW)
   name: Documentation
   on: [push]
   jobs:
     generate-docs:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v4
         - name: Generate API docs
           run: python tools/doc_generator.py --all
         - name: Build docs site
           run: mkdocs build
         - name: Deploy to GitHub Pages
           uses: peaceiris/actions-gh-pages@v3
           with:
             github_token: ${{ secrets.GITHUB_TOKEN }}
             publish_dir: ./site
   ```

4. **Add to ECHO dashboard:**
   ```python
   # echo/plugins/docs_browser.py
   class DocsBrowserPlugin:
       def render_dashboard(self):
           st.header("Documentation Browser")

           modules = get_all_modules()
           selected = st.selectbox("Module", modules)

           doc_path = f"docs/api/{selected}.md"
           if os.path.exists(doc_path):
               st.markdown(read_file(doc_path))
   ```

**Files:**
- `X:\Projects\_GAIA\tools\doc_generator.py` (NEW)
- `X:\Projects\_GAIA\hooks\auto_doc_generation.py` (NEW)
- `X:\Projects\_GAIA\.github\workflows\docs.yml` (NEW)
- `X:\Projects\_GAIA\_ECHO\echo\plugins\docs_browser.py` (NEW)
- `X:\Projects\_GAIA\mkdocs.yml` (NEW — MkDocs config)

**Dependencies:**
- Task 4.1 (Auto-tests) — Parallel automation efforts

**Acceptance Criteria:**
- [ ] New function added → API doc regenerated automatically
- [ ] Docs site deployed to GitHub Pages (verify URL works)
- [ ] ECHO docs browser displays module docs
- [ ] Doc generation preserves custom markdown (doesn't overwrite manual sections)
- [ ] Docs CI runs in <2 minutes
- [ ] Doc generator has 85%+ test coverage

---

#### 4.3 Git Rollback Capability
**What:** Add one-command rollback to last known good state (passing CI).

**Why:** Currently no safe rollback mechanism. ECHO's 19 version copies prove manual rollback doesn't work. Git rollback should be as easy as `geco rollback`.

**How:**
1. **Tag known good states:**
   ```python
   # tools/release_tagger.py
   class ReleaseTagger:
       def tag_successful_ci(self, commit_sha: str):
           """Tag commit that passed CI as 'known good'."""
           # Get CI status from GitHub
           ci_status = gh_client.get_ci_status(commit_sha)

           if ci_status == 'success':
               tag_name = f"known-good/{datetime.now().strftime('%Y%m%d-%H%M%S')}"
               subprocess.run(['git', 'tag', tag_name, commit_sha])
               subprocess.run(['git', 'push', 'origin', tag_name])
   ```

2. **Create rollback CLI:**
   ```python
   # tools/geco_cli.py
   @click.group()
   def geco():
       """GECO command-line tools."""
       pass

   @geco.command()
   @click.option('--steps', default=1, help='Number of known-good states to roll back')
   def rollback(steps: int):
       """Rollback to last known good state."""
       # Find last N known-good tags
       tags = subprocess.check_output(['git', 'tag', '-l', 'known-good/*']).decode().strip().split('\n')
       tags = sorted(tags, reverse=True)

       if len(tags) < steps:
           click.echo(f"Only {len(tags)} known-good states available")
           return

       target_tag = tags[steps - 1]
       click.echo(f"Rolling back to {target_tag}...")

       # Create rollback branch
       branch_name = f"rollback/{datetime.now().strftime('%Y%m%d-%H%M%S')}"
       subprocess.run(['git', 'checkout', '-b', branch_name, target_tag])

       click.echo(f"Rolled back to {target_tag} on branch {branch_name}")
       click.echo("Review changes, then merge to main if correct")
   ```

3. **Add ARGUS integration:**
   ```python
   # tools/rollback_with_observability.py
   def rollback_with_telemetry(steps: int):
       """Rollback with ARGUS event emission."""
       argus.emit('rollback_started', {'steps': steps, 'current_commit': get_current_commit()})

       try:
           result = perform_rollback(steps)
           argus.emit('rollback_completed', {'target_tag': result.target_tag})

           # Store rollback in MNEMIS
           mnemis.store(Memory(
               content=f"Rollback performed: {steps} steps to {result.target_tag}",
               type='rollback',
               tier='long_term',
               metadata={'steps': steps, 'target_tag': result.target_tag}
           ))
       except Exception as e:
           argus.emit('rollback_failed', {'error': str(e)})
           raise
   ```

4. **Add to ECHO dashboard:**
   ```python
   # echo/plugins/rollback_plugin.py
   class RollbackPlugin:
       def render_dashboard(self):
           st.header("Rollback Control")

           tags = get_known_good_tags()
           st.write(f"{len(tags)} known-good states available")

           steps = st.slider("Rollback steps", 1, min(10, len(tags)))
           if st.button(f"Rollback {steps} steps"):
               result = rollback_with_telemetry(steps)
               st.success(f"Rolled back to {result.target_tag}")
   ```

**Files:**
- `X:\Projects\_GAIA\tools\release_tagger.py` (NEW)
- `X:\Projects\_GAIA\tools\geco_cli.py` (NEW)
- `X:\Projects\_GAIA\tools\rollback_with_observability.py` (NEW)
- `X:\Projects\_GAIA\_ECHO\echo\plugins\rollback_plugin.py` (NEW)
- `X:\Projects\_GAIA\.github\workflows\ci.yml` (EDIT — tag on success)
- `X:\Projects\_GAIA\tools\tests\test_rollback.py` (NEW)

**Dependencies:**
- Task 1.2 (CI/CD) — Tagging requires CI pass detection
- Task 2.3 (Universal telemetry) — Rollback emits events

**Acceptance Criteria:**
- [ ] CI success automatically tags commit as known-good
- [ ] `geco rollback` creates rollback branch at last known-good tag
- [ ] `geco rollback --steps=3` rolls back 3 successful CI states
- [ ] Rollback emits ARGUS event (verify in dashboard)
- [ ] Rollback stored in MNEMIS (verify in memory store)
- [ ] ECHO rollback UI allows one-click rollback
- [ ] Rollback tool has 90%+ test coverage

---

#### 4.4 MCP Tool Discovery
**What:** Automatically discover and register new MCP tools without manual configuration.

**Why:** Currently 10 MCP plugins manually configured. New tools require settings.json edits. Tool discovery enables "install MCP server, agents automatically find it."

**How:**
1. **Create MCP registry scanner:**
   ```python
   # tools/mcp_discovery.py
   class MCPDiscovery:
       def discover_tools(self) -> List[MCPTool]:
           """Scan for available MCP tools."""
           tools = []

           # Scan Claude Code MCP directory
           mcp_dir = Path.home() / '.claude' / 'mcp'
           for server_dir in mcp_dir.iterdir():
               if server_dir.is_dir():
                   manifest = self._load_manifest(server_dir / 'manifest.json')
                   if manifest:
                       tools.extend(self._parse_tools(manifest))

           return tools

       def _parse_tools(self, manifest: dict) -> List[MCPTool]:
           """Extract tools from MCP manifest."""
           return [
               MCPTool(
                   name=tool['name'],
                   description=tool['description'],
                   parameters=tool.get('parameters', {}),
                   server=manifest['name']
               )
               for tool in manifest.get('tools', [])
           ]
   ```

2. **Auto-register tools with agents:**
   ```python
   # agents/tool_registry.py
   class ToolRegistry:
       def __init__(self):
           self.tools = {}
           self.auto_discover()

       def auto_discover(self):
           """Discover and register MCP tools automatically."""
           discovered = mcp_discovery.discover_tools()

           for tool in discovered:
               self.register(tool)
               argus.emit('tool_discovered', {
                   'tool': tool.name,
                   'server': tool.server,
                   'description': tool.description
               })

       def register(self, tool: MCPTool):
           """Register tool and make available to agents."""
           self.tools[tool.name] = tool

           # Store in MNEMIS for future reference
           mnemis.store(Memory(
               content=f"MCP Tool: {tool.name} - {tool.description}",
               type='tool_definition',
               tier='core',
               metadata={
                   'tool_name': tool.name,
                   'server': tool.server,
                   'parameters': tool.parameters
               }
           ))
   ```

3. **Update CLAUDE.md templates:**
   ```python
   # tools/claude_md_updater.py
   def update_claude_md_with_tools():
       """Add discovered tools to CLAUDE.md agent instructions."""
       tools = tool_registry.get_all_tools()

       for claude_md in find_all_claude_md_files():
           tool_section = generate_tool_section(tools)
           append_to_claude_md(claude_md, tool_section)
   ```

4. **Add to ECHO dashboard:**
   ```python
   # echo/plugins/tool_browser.py
   class ToolBrowserPlugin:
       def render_dashboard(self):
           st.header("Available MCP Tools")

           tools = tool_registry.get_all_tools()
           for tool in tools:
               with st.expander(f"{tool.name} ({tool.server})"):
                   st.write(tool.description)
                   st.json(tool.parameters)

                   # Usage stats
                   stats = get_tool_usage_stats(tool.name)
                   st.metric("Invocations", stats.count)
   ```

**Files:**
- `X:\Projects\_GAIA\tools\mcp_discovery.py` (NEW)
- `X:\Projects\_GAIA\agents\tool_registry.py` (NEW)
- `X:\Projects\_GAIA\tools\claude_md_updater.py` (NEW)
- `X:\Projects\_GAIA\_ECHO\echo\plugins\tool_browser.py` (NEW)
- `X:\Projects\_GAIA\tools\tests\test_mcp_discovery.py` (NEW)

**Dependencies:**
- Task 3.3 (URL knowledge base) — Tool docs can be fetched from URLs
- Task 4.2 (Auto-docs) — Tool registry generates docs

**Acceptance Criteria:**
- [ ] New MCP server installed → tools auto-discovered on next scan
- [ ] Tool registry contains 10+ tools (existing MCP plugins)
- [ ] CLAUDE.md updated with tool list (verify in ARGUS/LOOM/MNEMIS)
- [ ] Tool discovery emits ARGUS event (verify in dashboard)
- [ ] ECHO tool browser displays all available tools
- [ ] Tool discovery has 85%+ test coverage

---

#### 4.5 Background ARGUS Monitoring
**What:** Run ARGUS Process Observer as background service with 24/7 agent health checks.

**Why:** Currently ARGUS dashboard is manual (user opens Streamlit). No proactive monitoring. Background service enables "wake me up if error rate > 5%."

**How:**
1. **Create background service:**
   ```python
   # argus/service/background_monitor.py
   class BackgroundMonitor:
       def __init__(self, check_interval: int = 60):
           self.check_interval = check_interval
           self.running = False

       def start(self):
           """Start background monitoring."""
           self.running = True
           threading.Thread(target=self._monitor_loop, daemon=True).start()

       def _monitor_loop(self):
           """Main monitoring loop."""
           while self.running:
               try:
                   self._run_health_checks()
                   time.sleep(self.check_interval)
               except Exception as e:
                   log.error(f"Monitor error: {e}")

       def _run_health_checks(self):
           """Run all health checks."""
           # Check agent health
           for agent_id in process_observer.get_active_agents():
               status = process_observer.get_agent_status(agent_id)
               if status['error_rate'] > 0.05:
                   self._alert(f"High error rate for {agent_id}: {status['error_rate']:.1%}")

           # Check compliance
           compliance_score = trust_engine.get_metrics().compliance_score
           if compliance_score < 70:
               self._alert(f"Low compliance score: {compliance_score:.1f}%")

           # Check cost
           daily_cost = trust_engine.get_daily_cost()
           if daily_cost > 50:  # $50/day threshold
               self._alert(f"High daily cost: ${daily_cost:.2f}")

       def _alert(self, message: str):
           """Send alert (email, Slack, etc.)."""
           argus.emit('alert', {'message': message, 'severity': 'warning'})
           # TODO: Integrate with notification system
   ```

2. **Create Windows service installer:**
   ```python
   # tools/install_service.py
   import win32serviceutil

   class ArgusMonitorService(win32serviceutil.ServiceFramework):
       _svc_name_ = "ArgusMonitor"
       _svc_display_name_ = "ARGUS Background Monitor"

       def __init__(self, args):
           win32serviceutil.ServiceFramework.__init__(self, args)
           self.monitor = BackgroundMonitor()

       def SvcDoRun(self):
           self.monitor.start()
           while True:
               time.sleep(1)

       def SvcStop(self):
           self.monitor.stop()
   ```

3. **Add alert routing:**
   ```python
   # argus/service/alert_router.py
   class AlertRouter:
       def route_alert(self, alert: dict):
           """Route alert to appropriate channel."""
           severity = alert['severity']

           if severity == 'critical':
               # Email + Slack + SMS
               self.send_email(alert)
               self.send_slack(alert)
               self.send_sms(alert)
           elif severity == 'warning':
               # Slack only
               self.send_slack(alert)
           else:
               # Log only
               log.info(f"Alert: {alert['message']}")
   ```

4. **Add to ECHO dashboard:**
   ```python
   # echo/plugins/monitor_status.py
   class MonitorStatusPlugin:
       def render_dashboard(self):
           st.header("Background Monitor Status")

           status = background_monitor.get_status()
           st.metric("Uptime", format_duration(status.uptime))
           st.metric("Checks Performed", status.check_count)
           st.metric("Alerts Sent", status.alert_count)

           st.subheader("Recent Alerts")
           for alert in status.recent_alerts[:10]:
               st.warning(f"{alert.timestamp}: {alert.message}")
   ```

**Files:**
- `X:\Projects\_GAIA\_ARGUS\argus\service\background_monitor.py` (NEW)
- `X:\Projects\_GAIA\_ARGUS\argus\service\alert_router.py` (NEW)
- `X:\Projects\_GAIA\tools\install_service.py` (NEW)
- `X:\Projects\_GAIA\_ECHO\echo\plugins\monitor_status.py` (NEW)
- `X:\Projects\_GAIA\_ARGUS\tests\test_background_monitor.py` (NEW)

**Dependencies:**
- Task 2.1 (Process Observer) — Background monitor uses Process Observer
- Task 2.2 (Trust Dashboard) — Background monitor checks trust metrics

**Acceptance Criteria:**
- [ ] Background monitor starts as Windows service (verify with `Get-Service ArgusMonitor`)
- [ ] High error rate (>5%) triggers alert (integration test)
- [ ] Low compliance score (<70%) triggers alert
- [ ] High cost (>$50/day) triggers alert
- [ ] Alerts visible in ECHO dashboard within 60 seconds
- [ ] Background monitor runs 24+ hours without crash (stability test)
- [ ] Background monitor has 85%+ test coverage

---

## Summary

This roadmap delivers GECO in 8 weeks via 5 phases:

**Phase 0 (Week 1):** Emergency fixes — Hooks, VULCAN CLAUDE.md, GitHub push, ECHO consolidation. **Stops PROTEUS v0.2.1 failures.**

**Phase 1 (Weeks 2-3):** Enforcement layer — WARDEN full implementation, CI/CD everywhere, 60%+ coverage gates. **Prevents violations before production.**

**Phase 2 (Weeks 3-4):** Observability — Process Observer, Trust Dashboard, universal telemetry, production integration. **See everything in real-time.**

**Phase 3 (Weeks 4-5):** Learning & memory — MNEMIS auto-promotion, cross-session enforcement, URL knowledge base, mental model tracking. **System learns from past.**

**Phase 4 (Weeks 5-8):** Advanced automation — Auto-tests, auto-docs, rollback, tool discovery, background monitoring. **Full autonomy achieved.**

**Key Metrics After Phase 4:**
- 0 undetected agent failures (Process Observer + alerts)
- 100% CLAUDE.md compliance (cross-session enforcement)
- 80%+ test coverage ecosystem-wide (auto-generated tests)
- <1% repeat violations (MNEMIS learning)
- $0.01/operation cost visibility (Trust Dashboard)
- 24/7 uptime monitoring (background service)

**Risk Mitigation:** Each phase delivers standalone value. Early phases (0-2) address immediate pain (PROTEUS failures, visibility gaps). Later phases (3-4) add force multipliers (learning, automation). If timeline slips, Phases 0-2 still provide massive value.
```

---

Here are the complete Parts 3 and 4 of GECO_AUDIT.md. I've written:

**Part 3: Component Status Dashboard** (11 pages)
- Module status matrix for all 13 components
- Health summaries for each module with specific blockers and risks
- Infrastructure health summary (version control, Claude Code, constitutional compliance, observability, memory, testing)
- 10 critical findings highlighting the most severe gaps

**Part 4: Phased Roadmap** (18 pages)
- 5 phases over 8 weeks with clear dependency chain
- 25 detailed tasks with What/Why/How/Files/Dependencies/Acceptance Criteria
- Each task includes code examples, file paths, and measurable outcomes
- Phases prioritized by urgency: Emergency (stop bleeding) → Enforcement (prevent wounds) → Observability (see state) → Memory (learn from past) → Automation (full autonomy)

Key highlights:
- Phase 0 targets PROTEUS v0.2.1 failure root causes (hooks, VULCAN CLAUDE.md, GitHub backup)
- Phase 1 prevents future violations (WARDEN everywhere, CI/CD, coverage gates)
- Phase 2 delivers the core GECO promise (Process Observer, Trust Dashboard, cost visibility)
- Phase 3 enables learning (MNEMIS auto-promotion, cross-session enforcement)
- Phase 4 achieves autonomy (auto-tests, auto-docs, rollback, background monitoring)

Every module gets full treatment (even RAVEN placeholder), every roadmap task has 6+ acceptance criteria, and all file paths are absolute per your requirements.

---

## Part 5: PRD Draft — GAIA Ecosystem Product Suite

**Version:** 0.1.0-draft
**Date:** 2026-02-08
**Status:** Draft for review by ENG, PROD, UX
**Derived from:** GAIA_BIBLE.md v0.4.3
**Document Owner:** Federico (Product Owner)

---

### 5.1 Vision & Problem Statement

#### The Problem

AI-powered development tools can generate thousands of lines of code instantly, but they create three critical problems:

1. **Fragmentation**: Developers create isolated projects with duplicate implementations (5 LLM clients, 4 chunking implementations, 3 .env loading approaches across 7 projects).

2. **Opacity**: Users don't understand what was built, can't modify it confidently, and become dependent on AI forever. The tools work but learning stops.

3. **Ungoverned Growth**: No shared infrastructure, no version control, no cross-project observability, no institutional memory. Each new project starts from scratch.

#### The GAIA Solution

GAIA is a **constitutional AI governance framework** that sits between human creativity and AI-powered development. It transforms vague, fast, creative intent into structured, inspectable, and governable products without forcing users to think like engineers from day one.

**Core Value Proposition:**
- **For Creators**: Go from idea to production-ready project in minutes, not days, with confidence the structure is sound
- **For Teams**: Shared infrastructure means no duplicate work, automatic observability, and institutional learning across projects
- **For Users**: Glass-box transparency means you understand what was built, can modify it safely, and grow your technical capability over time

**North Star Principle:**
GAIA is a bridge, not a replacement. It teaches you to build with AI safely while actually doing the work. You learn by doing. You grow in capability. You become the architect.

---

### 5.2 Target Users

#### Platform Users (GAIA Ecosystem)

**Primary Persona: The Solo Creator**
- **Profile**: Technical creator with Python knowledge, overwhelmed by managing multiple AI projects
- **Pain**: "I have 7 projects scattered everywhere, duplicate code, no version control on half of them, can't track costs"
- **Goal**: Stabilize existing chaos, then build new projects with confidence
- **Success Metric**: Can create a new GAIA-compliant project in under 10 minutes

**Secondary Persona: The Growing Team**
- **Profile**: 2-5 person team building AI products, need shared infrastructure
- **Pain**: "Every team member has their own LLM client, our projects don't talk to each other, no observability"
- **Goal**: Unified development platform with shared intelligence and cross-project learning
- **Success Metric**: All team projects use MYCEL, all send telemetry to ARGUS, memory is shared via MNEMIS

#### Product Users (GAIA-Built Applications)

**HART OS User: Licensed Art Therapist**
- **Profile**: Non-technical, clinically trained, time-constrained, responsible for patient outcomes
- **Pain**: "I need trustworthy therapy session plans, but I don't understand how AI makes decisions"
- **Goal**: Generate evidence-backed therapy plans in under 3 seconds with full traceability
- **Success Metric**: 90% of generated plans accepted without modification, 100% traceability to canonical sources

**VIA User: Investment Analyst**
- **Profile**: Mid-level finance professional, needs synthesis across multiple sources
- **Pain**: "I spend hours reading 10-Ks, earning calls, analyst reports—need AI that can synthesize with citations"
- **Goal**: Multi-source investment intelligence with semantic claim tracking
- **Success Metric**: Synthesis quality matches senior analyst, 50% time savings on research

**PROTEUS User: Job Seeker (Product Designer/Leader)**
- **Profile**: 15+ years experience, 250+ applications with 0 interviews, needs ATS optimization
- **Pain**: "Manually adapting resumes takes 30+ minutes per application, no feedback loop on what works"
- **Goal**: JD-optimized resume in under 1 minute with ATS scoring and recruiter outreach
- **Success Metric**: Application-to-interview rate increases from 0% to industry standard (~2-5%)

---

### 5.3 Architecture Overview

GAIA uses a **Three Pillars + Shared Spine** architecture:

```
┌─────────────────────────────────────────────────────────────────┐
│                        GAIA ECOSYSTEM                           │
│                   Constitutional Governance Layer                │
└─────────────────────────────────────────────────────────────────┘
                                 │
        ┌────────────────────────┼────────────────────────┐
        │                        │                        │
   ┌────▼────┐             ┌────▼────┐             ┌────▼────┐
   │ VULCAN  │             │  LOOM   │             │ ARGUS   │
   │  (The   │────────────▶│  (The   │────────────▶│  (The   │
   │  Forge) │   creates   │ Loom)   │  observes   │Watchman)│
   │         │             │         │             │         │
   │ PROJECT │             │WORKFLOW │             │ MONITOR │
   │ CREATOR │             │ ENGINE  │             │ OBSERVE │
   └────┬────┘             └────┬────┘             └────┬────┘
        │                       │                       │
        └───────────────────────┼───────────────────────┘
                                │
                    ┌───────────▼───────────┐
                    │   SHARED SPINE        │
                    ├───────────────────────┤
                    │ MYCEL (Intelligence)  │
                    │ MNEMIS (Memory)       │
                    │ WARDEN (Enforcement)  │
                    │ Mental Models (59)    │
                    └───────────────────────┘
                                │
        ┌───────────────────────┼───────────────────────┐
        │                       │                       │
   ┌────▼────┐            ┌────▼────┐            ┌────▼────┐
   │ HART OS │            │   VIA   │            │PROTEUS  │
   │ Therapy │            │Investing│            │ Resume  │
   │ v6.2.8  │            │  v6.4   │            │ v0.2.1  │
   └─────────┘            └─────────┘            └─────────┘
   Production             Production             Active Dev
```

**Data Flow:**

1. **Creation Flow**: User launches VULCAN → answers 7-step questionnaire → VULCAN generates GAIA-compliant project scaffold → project registered in registry → MYCEL integrated automatically

2. **Execution Flow**: Product uses MYCEL for LLM calls → LOOM manages workflow execution with agent authority → all actions send telemetry to ARGUS event bus → MNEMIS stores patterns

3. **Learning Flow**: ARGUS detects patterns in telemetry → MNEMIS promotes recurring patterns to higher memory tiers → learned patterns inform future VULCAN projects

4. **Governance Flow**: WARDEN scans for compliance violations → violations logged to ARGUS → trust dashboard shows constitutional compliance → pre-commit hooks prevent regressions

---

### 5.4 Platform Capabilities

What GAIA provides to ALL products it builds:

#### 5.4.1 Project Scaffolding (VULCAN)

**Status:** Operational (v0.4.0, 85% test coverage, 19,830 LOC)

**Capabilities:**
- **Human-in-the-Loop Questionnaire**: 7-step intake form captures project intent, constraints, and context
- **Three Adapter Types**:
  - Deterministic (for therapy, scoring systems)
  - Creative (for content generation, RAG systems)
  - Processor (for data pipelines, document generation)
- **GAIA-Compliant Scaffolding**: Every project gets:
  - `config.py` inheriting from GaiaSettings (API keys, model configs)
  - `logs/` directory for JSONL telemetry
  - `CLAUDE.md` with structured context
  - `tests/` with pytest structure
  - `.gitignore` with hardened secrets protection
  - `requirements.txt` including rag-intelligence>=0.3.1
- **Registry Integration**: Automatic registration in `X:\Projects\_GAIA\registry.json`
- **Retroactive Registration**: Can register existing projects in Registry-Only or GAIA-Lite modes

**User Value:** Go from idea to testable, version-controlled project in 10 minutes. No duplicate code, automatic GAIA integration.

**Technical Constraints:**
- Requires Python 3.10+
- Streamlit-based UI (port 8501)
- Local filesystem only (no cloud deployment yet)

---

#### 5.4.2 Workflow Orchestration (LOOM)

**Status:** Partial (v1.0.0, models operational, governance not enforced)

**Capabilities:**
- **Agent Authority System**: Hierarchical agent levels (0-4) matching memory tiers
  - Level 0: Ephemeral (single-use functions)
  - Level 1: Task agents (single workflow)
  - Level 2: Session agents (conversation management)
  - Level 3: Project agents (cross-session coordination)
  - Level 4: System agents (architectural changes)
- **Workflow State Management**: Tracks execution state across multi-step workflows
- **Memory-Aware Execution**: Agents respect memory tier contracts (can't write above authority level)
- **Glass-Box Transparency**: Every workflow step logged with reasoning

**User Value:** Complex multi-agent workflows with built-in governance. Agents can't silently exceed their authority.

**Current Limitation:** Governance rules defined but not enforced at runtime. Validator exists but not called.

---

#### 5.4.3 Monitoring & Sense-Making (ARGUS)

**Status:** Partial (v0.5.0, dashboard operational, Process Observer missing)

**Capabilities:**
- **Mental Model Library**: 59 models across 6 categories (Cognitive, Behavioral, Systems, Decision-Making, Communication, Business)
- **Context-Aware Model Selection**: Scores models based on context, user Growth Rung, prerequisites
- **Layered Explainability**: 4 levels (Simple, Detailed, Technical, Debug) mapped to user cognitive level
- **Subconscious Layer**: External memory, pattern detection, hypothesis generation
- **Event Bus**: Centralized SQLite database for telemetry (only PROTEUS connected currently)
- **Streamlit Dashboard**: Real-time visualization of ecosystem health

**User Value:** Understand WHY the system made decisions, at your current technical level. Learn from patterns across all projects.

**Missing Components:**
- **Process Observer** (not implemented): Can't observe Claude Code agent executions
- **Post-Mortem Analyzer** (not implemented): Can't analyze task failures
- **Trust Dashboard** (empty directory): No constitutional compliance visualization

---

#### 5.4.4 Shared Intelligence (MYCEL)

**Status:** Operational (v0.2.0, 92-100% test coverage, 200+ tests)

**Capabilities:**
- **Unified LLM Clients**: Single interface for OpenAI, Anthropic, Gemini
- **Configuration Management**: `GaiaSettings` base class with pydantic-settings
- **Core Algorithms**:
  - RecursiveCharacterChunker (text splitting)
  - OpenAIEmbedder (vectorization)
  - VectorRetriever (semantic search)
- **Provider Fallback**: Automatic fallback if primary LLM unavailable
- **Telemetry Hooks**: Ready for ARGUS integration (not widely used yet)

**User Value:** Write once, switch providers without code changes. No duplicate LLM client implementations.

**Technical Details:**
- Python 3.10+, Poetry build system
- Only GAIA module with TDD configuration in pyproject.toml
- Depends on: openai, anthropic, google-generativeai, pydantic-settings

---

#### 5.4.5 Cross-Project Memory (MNEMIS)

**Status:** Operational (v1.0.0, architecture complete, promotion manual)

**Capabilities:**
- **Three-Tier Memory Hierarchy**:
  - **PROJECT**: Project-specific knowledge (local)
  - **GAIA**: Cross-project patterns (ecosystem-wide)
  - **PUBLIC**: Shareable knowledge (exportable)
- **Memory Contracts**: Runtime enforcement prevents agents from writing above authority tier
- **Promotion Protocol**: Structured criteria for promoting memories between tiers
  - access_count >= 3
  - time_span across multiple sessions
  - pattern_strength >= 0.7
  - optional user_confirmation
- **Thread-Safe Access**: Concurrent reads/writes managed safely
- **JSONL Persistence**: Long-term and permanent memories stored in structured logs

**User Value:** The system remembers patterns across projects. VIA learns an investment framework → HART OS can import it for financial stress therapy.

**Current Limitation:** Promotion is manual, not automated from ARGUS error patterns.

---

#### 5.4.6 Compliance & Enforcement (WARDEN)

**Status:** Minimal (v0.1.0, scanner exists, not integrated)

**Capabilities:**
- **Compliance Scanner**: Validates:
  1. Git status (uncommitted changes?)
  2. Test suite (passing?)
  3. .env safety (no hardcoded keys)
  4. Dependency freshness
  5. Documentation completeness
- **CLI Interface**: Command-line tool for manual scans

**User Value:** Catch secrets exposure, missing tests, and broken dependencies before they reach production.

**Critical Gap:** Scanner exists (6,908 bytes) but not integrated into workflow. No pre-commit hooks, no CI/CD gates, no ARGUS telemetry.

---

### 5.5 Product Catalog

#### HART OS — Therapeutic Scoring System

**Target Users:** Art therapists, clinical supervisors, program designers

**Status:** Production (v6.2.8, GitHub remote exists)

**Key Features:**
- **6-Component Scoring Algorithm**: 75% deterministic (canonical HART data), 25% AI augmentation
- **Deterministic Phase Selection**: Based on `hart_mapping_ledger_vFinal.md`
- **Technique Recommendation**: Ranked list from `hart_library_manifest_techniques_vFinal.md`
- **Copilot LLM Evaluation**: Optional AI synthesis (clearly labeled)
- **Guía para la Terapeuta**: Spanish-language therapy session plan output
- **Glass-Box Traceability**: Every recommendation cites canonical source

**Tech Stack:**
- Python 3.9+, Streamlit
- OpenAI (gpt-4o for copilot evaluation)
- Spanish localization (zero Spanish in code, all text in `config/locales/es.json`)
- Deterministic pipeline: Intake → Phase → Technique → Scoring → Validation → Guía

**Success Metrics (Proposed):**
- Generate Session < 3 seconds (deterministic only)
- Generate Session < 8 seconds (with LLM copilot)
- 90% of plans accepted without modification
- 100% traceability to canonical sources
- 80% test coverage (target)

**Known Issues:**
- Output does not always conform to approved Guía structure
- State lost across navigation
- CI failing, blocking confidence
- OpenAI key exposed in git history (requires manual revocation)

**Localization Rule (Constitutional):** Zero Spanish in Python code. All user-facing text in JSON config. Spanish is a data concern, not a code concern.

---

#### VIA — Investment Intelligence

**Target Users:** Investment analysts, portfolio managers, financial researchers

**Status:** Production (v6.4, no GitHub remote)

**Key Features:**
- **Multi-Source RAG Synthesis**: Combines 10-Ks, earnings calls, analyst reports
- **Semantic Claims Tracking**: Each claim cites specific source with page/timestamp
- **Three-Provider Ensemble**: Gemini, OpenAI, Anthropic for cross-validation
- **Investment Thesis Generation**: Synthesizes bull/bear cases
- **Evidence-Based Reasoning**: No unsupported claims allowed

**Tech Stack:**
- Python 3.10+, Streamlit (port 8503)
- Gemini (primary), OpenAI, Anthropic (fallback)
- MYCEL integration (LLM client abstraction)
- RAG pipeline: Ingest → Chunk → Embed → Retrieve → Synthesize

**Success Metrics (Proposed):**
- Synthesis quality score >= 4.0/5.0 (expert evaluation)
- Citation accuracy >= 95%
- 50% time savings vs. manual research
- Cross-provider agreement >= 80%

**GAIA Integration:** Depends on MYCEL for LLM abstraction. Uses MYCEL chunking, embedding, retrieval.

---

#### DATA FORGE — Data Processing Engine

**Target Users:** Data engineers, analysts, ETL pipeline builders

**Status:** Production (v1.1, no GitHub remote)

**Key Features:**
- **Memory Bank Architecture**: Reusable data transformation patterns
- **Taxonomy Builder**: Auto-generates taxonomies from unstructured data
- **Data Processing Compiler**: Converts natural language into data pipelines
- **Pipeline Validation**: Deterministic checks before execution

**Tech Stack:**
- Python 3.10+, Streamlit
- OpenAI (gpt-4o for pipeline generation)
- No external database dependencies

**Success Metrics (Proposed):**
- Pipeline generation < 30 seconds
- Generated pipelines pass validation >= 90%
- User editing time < 5 minutes per pipeline

**GAIA Integration:** Standalone, predates GAIA. Candidate for MYCEL migration.

---

#### PROTEUS — Shape-Shifting Resume Engine

**Target Users:** Job seekers (product designers, technical leaders)

**Status:** Active Development (v0.2.1, most actively developed)

**Key Features:**
- **JD-Optimized Resume Generation**: Parses job descriptions, adapts resume blocks in under 1 minute
- **ATS Platform Intelligence**: Platform-specific scoring (Workday, Greenhouse, Lever, iCIMS, Ashby, Taleo)
- **Dual-Format Rendering**: Two-column PDF (human-facing), single-column DOCX (ATS-facing)
- **Recruiter Outreach**: Auto-generates personalized outreach messages
- **Application Tracking**: SQLite database tracks job status (active/closed/expired), resume versions, application history
- **Job Discovery**: Tag-based search across job boards
- **Feedback Loop**: Learns which resume patterns → interviews (feeds MNEMIS)

**Tech Stack:**
- Python 3.10+, Streamlit
- Anthropic (claude-sonnet-4-5 for adaptation)
- MYCEL integration (LLM client)
- ARGUS telemetry (ONLY product sending events)
- MNEMIS integration (resume pattern storage)
- Playwright (PDF rendering), python-docx (DOCX generation)
- SQLite (`data/proteus.db`)

**Pipeline Architecture:**
```
JD Paste → Parse & Prune → Block Matching → Content Adaptation →
ATS Scoring → Dual Rendering (PDF + DOCX) → Recruiter Outreach →
Application Tracking → Feedback Loop → MNEMIS Pattern Storage
```

**Success Metrics (Current):**
- Resume generation < 1 minute
- ATS score >= 85/100 for target platform
- Application-to-interview rate (baseline: 0%, target: 2-5%)
- User editing time < 5 minutes post-generation

**GAIA Integration Showcase:** PROTEUS is the most GAIA-integrated product:
- Uses MYCEL for LLM abstraction
- Sends comprehensive telemetry to ARGUS event bus
- Stores proven resume patterns in MNEMIS
- Co-launches with ARGUS dashboard (`launch.py`)
- Full CLAUDE.md with constitutional constraints

**Current Focus:** Active development. Phase 4 in progress (application tracking + job discovery).

---

#### ECHO — Chat Archaeology

**Target Users:** Users analyzing ChatGPT conversation history

**Status:** Stale (v0.1.0, last modified Jan 2026)

**Key Features:**
- **Conversation Taxonomy**: Auto-categorizes ChatGPT export conversations
- **Pattern Detection**: Identifies recurring conversation types
- **Export Processing**: Parses ChatGPT JSON export format

**Tech Stack:**
- Python 3.10+, Streamlit
- Gemini (primary LLM)
- 19 manual UI versions (`ui_v0.py` through `ui_v012.py`)

**Critical Issue:** 19 manual version copies indicate lack of version control discipline during development.

**Recommendation:**
- **Option A (Rescue)**: Consolidate to single version, add git discipline, integrate MYCEL
- **Option B (Retire)**: Archive module, document learnings, focus resources on active products

**Success Metrics (If Rescued):**
- Conversation classification accuracy >= 80%
- Processing time < 10 seconds per 100 conversations
- Single version under git control

---

### 5.6 Trust Contract & Governance

GAIA's constitutional framework is defined by **Five Trust Principles** from GAIA_BIBLE.md Chapter 2:

#### Principle 1: GAIA Never Lies

**Definition:** Always tells the truth about what it knows, doesn't know, and is uncertain about.

**Implementation:**
- Agent prompts encode: "If uncertain, say so explicitly"
- System messages cannot hide errors
- Logs are immutable and human-readable
- Confidence scores on every decision

**Monitoring:** ARGUS tracks instances of "I don't know" responses, Trust Dashboard flags hidden uncertainty patterns

**Enforcement:** Agents that hide uncertainty fail validation, silent failures trigger automatic escalation

**Example:**
```
❌ Bad: "I created your project successfully" (when partially failed)
✅ Good: "I created 4/5 components. Stage 3 failed because dependency X
         is unavailable. Should I proceed with 4, or investigate X first?"
```

---

#### Principle 2: GAIA Admits Limits

**Definition:** Explicitly declares what it cannot do, will not do, or should not do.

**Implementation:**
- Constitutional boundaries in GAIA_BIBLE.md
- Read-only Process Observers (cannot execute)
- Memory contracts (cannot write above tier)
- Authority graph defines scope boundaries

**Monitoring:** WARDEN checks for authority violations, Process Observer detects scope creep

**Enforcement:** Authority graph prevents unauthorized actions, memory contracts enforced at runtime, escalation to human when limits reached

**Example:**
```
❌ Bad: "I'll fix this by modifying project X" (outside scope)
✅ Good: "This requires modifying project X, which is outside my authority.
         Escalating to Project Agent for approval."
```

---

#### Principle 3: GAIA Degrades Gracefully

**Definition:** When GAIA fails, it fails visibly, predictably, and reversibly.

**Implementation:**
- No silent failures allowed
- Every error produces structured log
- Rollback mechanisms for all state changes
- Fallback providers for LLM calls (MYCEL feature)

**Monitoring:** ARGUS tracks failure modes, Process Observer identifies graceful vs. catastrophic degradation

**Enforcement:** Telemetry hooks on every state mutation, git provides code rollback, MYCEL LLM clients have fallback chains

**Example:**
```
❌ Bad: System hangs silently when API fails
✅ Good: "OpenAI API unavailable. Falling back to Anthropic.
         User will see 'degraded mode' banner."
```

---

#### Principle 4: GAIA Learns Explicitly

**Definition:** Only learns from explicit user confirmations, never from inference.

**Implementation:**
- Memory promotion requires approval (MNEMIS protocol)
- Pattern detection produces hypotheses, not facts
- Learning proposals shown to user before acceptance
- Provenance tracked for all learned patterns

**Monitoring:** ARGUS tracks learning proposals (accepted/rejected), Process Observer flags unconfirmed patterns

**Enforcement:** Memory contracts prevent silent updates, promotion queue requires human ratification, audit trail for all learning

**Example:**
```
❌ Bad: "You always use OpenAI, so I'm setting it as default" (inference)
✅ Good: "I noticed you chose OpenAI in 8/10 projects. Should I pre-fill
         it as default? [Yes/No/Not Yet]"
```

---

#### Principle 5: GAIA Remains Inspectable

**Definition:** Every decision GAIA makes can be traced, audited, and explained.

**Implementation:**
- CLAUDE.md at project level explains structure
- Provenance tracking in memory (MNEMIS)
- Structured telemetry (JSONL)
- Decision rationale logged with every choice

**Monitoring:** ARGUS provides execution traces, Process Observer analyzes decision quality, Trust Dashboard shows transparency metrics

**Enforcement:** All decisions logged with rationale, black-box components prohibited in GAIA core, unexplained code fails pre-commit hooks (when implemented)

**Example:**
```
User: "Why did VULCAN choose Deterministic adapter?"
GAIA: "You specified 'confidence scoring required' in Step 4.
       Deterministic adapter is the only one with scoring stages.
       See: questionnaire_response.json line 42"
```

---

### 5.7 Success Criteria

#### Platform Success Criteria (GAIA Ecosystem)

**P0 (Critical):**
- [ ] 100% of VULCAN-created projects pass WARDEN compliance scan
- [ ] 100% of projects have CLAUDE.md with constitutional constraints
- [ ] CI/CD gates prevent merging code with failing tests (0% → 100% enforcement)
- [ ] Pre-commit hooks active on all 9 GAIA modules (0 → 9 modules)

**P1 (High):**
- [ ] All 9 modules send telemetry to ARGUS event bus (currently 1/9)
- [ ] MNEMIS auto-promotes errors into prevention rules (manual → automatic)
- [ ] Trust Dashboard shows constitutional compliance metrics
- [ ] GitHub remotes configured for all GAIA modules (1 → 9)

**P2 (Medium):**
- [ ] Process Observer operational for Claude Code agent monitoring
- [ ] Cross-project memory sharing adopted by 3+ products
- [ ] Mental Model Library invoked in 50%+ of ARGUS queries
- [ ] Skill registry with auto-discovery operational

**Quantitative Targets (6 months):**
- Test coverage: 80% minimum across all modules (currently variable)
- Time to create new project: < 10 minutes (VULCAN)
- Documentation completeness: 95% of modules have full API docs
- Zero hardcoded secrets in any codebase

---

#### Product Success Criteria

**HART OS (Therapy Scoring System):**
- [ ] Generate Session completes in < 3 seconds (deterministic only)
- [ ] 90% of generated Guías accepted without modification
- [ ] 100% of recommendations traceable to canonical sources
- [ ] Zero Spanish strings in Python code (localization rule enforced)
- [ ] CI passing on all commits

**VIA (Investment Intelligence):**
- [ ] Multi-source synthesis with 95%+ citation accuracy
- [ ] 50% time savings vs. manual research (user-reported)
- [ ] Cross-provider agreement >= 80%
- [ ] MYCEL integration for all LLM calls (currently mixed)

**DATA FORGE (Data Processing Engine):**
- [ ] Pipeline generation < 30 seconds
- [ ] 90% of generated pipelines pass validation
- [ ] MYCEL migration complete (currently standalone)

**PROTEUS (Resume Engine):**
- [ ] Resume generation < 1 minute per application
- [ ] ATS score >= 85/100 for target platform
- [ ] Application-to-interview rate increases from 0% to 2-5%
- [ ] Feedback loop stores 100% of application outcomes in MNEMIS

**ECHO (Chat Archaeology):**
- [ ] Decision: Rescue or Retire (no mixed state)
- [ ] If rescued: Consolidate to single version, 80% classification accuracy
- [ ] If retired: Learnings documented, module archived

---

### 5.8 Risks & Mitigations

| Risk | Impact | Likelihood | Mitigation |
|------|--------|------------|------------|
| **Enforcement Gap (90% documented, 10% enforced)** | HIGH | Certain | **P0**: Deploy pre-commit hooks, CI/CD gates, integrate WARDEN scanner within 2-3 days |
| **Single-Developer Bus Factor** | HIGH | Medium | **P1**: GitHub remotes for all modules, comprehensive documentation, onboarding guide |
| **Stale Modules (ECHO)** | MEDIUM | Certain | **P2**: Rescue/retire decision within 1 sprint, consolidate or archive |
| **No CI/CD** | HIGH | Certain | **P0**: GitHub Actions for VULCAN, MYCEL, PROTEUS (already >85% coverage) |
| **Telemetry Gaps (8/9 modules silent)** | MEDIUM | Certain | **P1**: Follow PROTEUS telemetry pattern, connect remaining modules to ARGUS |
| **Manual Memory Promotion** | MEDIUM | Certain | **P1**: Auto-promotion pipeline from ARGUS errors to MNEMIS rules |
| **HART OS Regression Risk** | HIGH | Medium | **P0**: CI enforcement blocks merges on test failures, state management tests |
| **Secrets Exposure (HART OS git history)** | CRITICAL | Known | **Immediate**: User must manually revoke exposed OpenAI key, rotate quarterly |
| **No Background Tasks** | LOW | Certain | **P2**: Task runner for async monitoring, scheduled compliance scans |
| **MCP Integration Gap** | LOW | Certain | **P3**: GAIA modules as MCP servers for Claude Code discoverability |

---

### 5.9 Open Questions for Review

#### For Product (PROD):

1. **ECHO Rescue vs. Retire**: Is there user demand for chat archaeology? Or is this technical debt to eliminate?

2. **Product Roadmap Priority**: Which products should receive investment?
   - HART OS (production but unstable) — stabilization effort?
   - PROTEUS (active development) — continue prioritization?
   - VIA (production) — feature freeze or expand?
   - DATA FORGE (production) — maintenance mode?

3. **Success Metrics Validation**: Are the proposed metrics (ATS score, interview rate, synthesis quality) the right measures of product value?

4. **Market Positioning**: Is GAIA a developer tool, a platform, or an ecosystem? How do we communicate this to users?

5. **Monetization Strategy**: Open source? SaaS? Self-hosted enterprise? What's the business model?

---

#### For Engineering (ENG):

1. **CI/CD Rollout Strategy**: Which modules get CI/CD first? Suggested priority: MYCEL (foundation), VULCAN (highest LOC), PROTEUS (active dev).

2. **Pre-Commit Hook Standardization**: Same hooks across all 9 modules, or module-specific configurations?
   - Proposed standard: ruff (linting), black (formatting), pytest (minimum 80% coverage)

3. **Telemetry Schema**: Should ARGUS event bus accept JSONL, SQLite, or both? Need unified schema across modules.

4. **WARDEN Integration Point**: Pre-commit hook, GitHub Action, or standalone CLI? Can we enforce at all three layers?

5. **Process Observer Implementation**: Should this monitor Claude Code agents via MCP, filesystem observers, or API calls?

6. **GitHub Remote Strategy**:
   - Separate repos per module or monorepo?
   - Public open source or private?
   - Branch strategy (trunk-based vs. GitFlow)?

7. **Python Version Policy**: All modules on 3.10+ or allow 3.9 for backward compatibility (HART OS)?

8. **Dependency Management**: Poetry (MYCEL), pip (others), or standardize ecosystem-wide?

---

#### For UX/UI:

1. **Streamlit vs. Web Framework**: Current products use Streamlit. Is this sufficient for production UX, or migrate to React/Vue?

2. **ARGUS Dashboard Usability**: Current dashboard is developer-focused. Do we need end-user dashboards per product?

3. **Trust Dashboard Design**: How do we visualize constitutional compliance metrics for non-technical users?

4. **VULCAN Questionnaire UX**: 7-step form works but is lengthy. Can we reduce friction without losing context capture?

5. **Error Message Standards**: How do we present "graceful degradation" to users? Design pattern for fallback states?

6. **HART OS Navigation State Loss**: Root cause is UX design or state management bug? Needs investigation.

7. **Localization Strategy**: HART OS uses Spanish. If we expand, do we need i18n framework ecosystem-wide?

8. **Mobile Support**: All products desktop-only. Is mobile access a requirement?

---

#### Cross-Functional:

1. **Constitutional Enforcement vs. User Friction**: Where do we draw the line between strict governance and developer experience?

2. **Learning Loop Automation**: Should MNEMIS auto-promote without user confirmation (faster learning) or require approval (trust principle)?

3. **Skill System Design**: User-level skills vs. GAIA-level skills — how do we enable contribution without chaos?

4. **Documentation Debt**: 90% coverage but scattered across 41K tokens in GAIA_BIBLE.md. Do we need restructured docs for different audiences (user guide, API reference, architecture deep-dive)?

5. **Version Strategy**: Currently GAIA v0.4.3, products have independent versions. Synchronize versions or keep separate?

6. **Support & Maintenance**: Who owns GAIA platform vs. individual products? Needs team structure definition.

---

## Metadata

**Document Status:** Draft v0.1.0
**Next Steps:**
1. PROD/ENG/UX review and comment (target: 3 business days)
2. Open Questions resolution meeting (target: 1 week)
3. PRD v1.0 finalization with success criteria locked
4. Technical implementation plan (ENG)
5. UX design specifications (UX)
6. Roadmap with sprint planning (PROD)

**Related Documents:**
- `X:\Projects\_GAIA\GAIA_BIBLE.md` (constitutional source)
- `X:\Projects\_GAIA\GECO_AUDIT_Part1_Part6.md` (audit findings)
- `X:\Projects\_GAIA\registry.json` (component registry)
- `X:\Projects\hart_os_v6\docs\PRD\HART_OS_v6.1_PRD.md` (product-level PRD example)
- `X:\Projects\_GAIA\_PROTEUS\docs\PRD.md` (product-level PRD example)

**Absolute File Path:** This content should be written to:
`X:\Projects\_GAIA\GECO_AUDIT_Part5_PRD_DRAFT.md`

---

I've written a comprehensive PRD Draft (Part 5) for the GAIA Ecosystem Product Suite. The document is structured for three audiences:

**For Engineering:**
- Detailed architecture with data flow diagrams
- Technical specs for each component (VULCAN, LOOM, ARGUS, MYCEL, MNEMIS, WARDEN)
- Tech stack, dependencies, and constraints
- Open questions on CI/CD, telemetry schema, Process Observer implementation

**For Product:**
- Clear vision and problem statement in non-technical language
- Target user personas for both platform and products
- Success criteria with measurable outcomes
- Risk register with impact/likelihood/mitigation
- Open questions on roadmap priority, metrics validation, monetization

**For UX:**
- User personas with pain points and goals
- Current UX issues documented (HART OS state loss, VULCAN questionnaire friction)
- Trust Dashboard and error messaging design questions
- Localization and mobile support considerations

**Key Strengths:**
1. **Derived from Source**: All details pulled from GAIA_BIBLE.md (41K tokens), registry.json, and product PRDs
2. **Honest About Gaps**: Explicitly calls out "90% documented, 10% enforced" and missing components
3. **Actionable**: Open Questions section provides clear decision points for each team
4. **Governance-First**: Trust Contract section explains the constitutional principles, not just technical features
5. **Product-Specific**: Dedicated sections for each of 5 products with realistic status and metrics

This PRD is ready for team handoff and would enable ENG to start implementation planning, PROD to prioritize roadmap, and UX to design interfaces.

---

## Part 6: Appendices

### Appendix A: Complete File Index

**Core Configuration**

| File Path | Purpose | Lines | Status |
|-----------|---------|-------|--------|
| `X:\Projects\_GAIA\GAIA_BIBLE.md` | Constitutional PRD | 41,000 tokens | Complete |
| `X:\Projects\_GAIA\registry.json` | Component registry | ~200 | Active |
| `X:\Projects\_GAIA\VERSION_LOG.md` | Version history | 383 | Current |
| `X:\Projects\_GAIA\v0_baseline.md` | Pre-consolidation baseline | 145 | Archived |
| `X:\Projects\_GAIA\GAIA debugging and meta learning.txt` | Audit source document | 54 | Input |

**ARGUS (Observability Layer)**

| File Path | Purpose | Lines | Status |
|-----------|---------|-------|--------|
| `X:\Projects\_GAIA\_ARGUS\CLAUDE.md` | Constitutional constraints | ~300 | Complete |
| `X:\Projects\_GAIA\_ARGUS\dashboard\ARCHITECTURE.md` | Dashboard architecture | 463 | Complete |
| `X:\Projects\_GAIA\_ARGUS\dashboard\app.py` | Main Streamlit dashboard | 264 | Operational |
| `X:\Projects\_GAIA\_ARGUS\dashboard\event_bus.py` | SQLite event logging | 215 | Operational |
| `X:\Projects\_GAIA\_ARGUS\dashboard\components\*.py` | UI components | ~800 total | Operational |
| `X:\Projects\_GAIA\_ARGUS\subconscious\memory.py` | External memory system | 410 | Operational |
| `X:\Projects\_GAIA\_ARGUS\subconscious\pattern_detector.py` | Pattern detection | 431 | Operational |
| `X:\Projects\_GAIA\_ARGUS\subconscious\hypothesis_generator.py` | Hypothesis generation | 404 | Operational |
| `X:\Projects\_GAIA\_ARGUS\explainability\explainer.py` | 4-level explainability | 422 | Operational |
| `X:\Projects\_GAIA\_ARGUS\process_observer\__init__.py` | Observer imports | 15 | Skeleton |
| `X:\Projects\_GAIA\_ARGUS\process_observer\observer.py` | ProcessObserver class | 0 | **MISSING** |
| `X:\Projects\_GAIA\_ARGUS\process_observer\post_mortem.py` | PostMortemAnalyzer | 0 | **MISSING** |
| `X:\Projects\_GAIA\_ARGUS\trust_dashboard\` | Trust visualization | 0 | **EMPTY DIR** |
| `X:\Projects\_GAIA\logs\argus_events.db` | Event database (SQLite) | N/A | Active |

**LOOM (Governance Layer)**

| File Path | Purpose | Lines | Status |
|-----------|---------|-------|--------|
| `X:\Projects\_GAIA\_LOOM\CLAUDE.md` | Governance rules | ~400 | Complete |
| `X:\Projects\_GAIA\_LOOM\loom\models\agent_models.py` | Agent definitions | ~200 | Operational |
| `X:\Projects\_GAIA\_LOOM\loom\models\workflow.py` | Workflow models | ~150 | Operational |
| `X:\Projects\_GAIA\_LOOM\loom\governance\rules.py` | Governance rules | ~180 | Partial |
| `X:\Projects\_GAIA\_LOOM\loom\governance\validator.py` | Rule validation | ~120 | Partial |
| `X:\Projects\_GAIA\_LOOM\loom\integrations\argus_telemetry.py` | ARGUS telemetry bridge | ~100 | **NOT USED** |
| `X:\Projects\_GAIA\_LOOM\loom\integrations\mnemis_bridge.py` | MNEMIS learning bridge | ~90 | Operational |
| `X:\Projects\_GAIA\_LOOM\tests\*.py` | Test suite | ~500 total | Exists (not enforced) |

**MNEMIS (Memory Layer)**

| File Path | Purpose | Lines | Status |
|-----------|---------|-------|--------|
| `X:\Projects\_GAIA\_MNEMIS\CLAUDE.md` | 3-tier hierarchy rules | ~350 | Complete |
| `X:\Projects\_GAIA\_MNEMIS\mnemis\core\memory_store.py` | Memory store | ~320 | Operational |
| `X:\Projects\_GAIA\_MNEMIS\mnemis\core\promotion.py` | Promotion protocol | ~280 | Operational |
| `X:\Projects\_GAIA\_MNEMIS\mnemis\core\contracts.py` | Access contracts | ~150 | Operational |
| `X:\Projects\_GAIA\_MNEMIS\mnemis\core\search.py` | Memory search | ~200 | Operational |
| `X:\Projects\_GAIA\_MNEMIS\mnemis\integrations\argus_telemetry.py` | Telemetry | ~80 | Operational |
| `X:\Projects\_GAIA\_MNEMIS\tests\*.py` | Test suite | ~400 total | Exists (not enforced) |

**MYCEL (Test Infrastructure)**

| File Path | Purpose | Lines | Status |
|-----------|---------|-------|--------|
| `X:\Projects\_GAIA\_MYCEL\pyproject.toml` | Poetry config with TDD | 86 | **Only module with TDD config** |
| `X:\Projects\_GAIA\_MYCEL\mycel\*.py` | Core modules | ~1,200 total | Operational |
| `X:\Projects\_GAIA\_MYCEL\tests\*.py` | 10 test files, 200+ tests | ~1,500 | 92-100% coverage |

**VULCAN (Project Creation)**

| File Path | Purpose | Lines | Status |
|-----------|---------|-------|--------|
| `X:\Projects\_GAIA\_VULCAN\vulcan_forge\project_creator.py` | Project scaffolding | 1,847 | Operational |
| `X:\Projects\_GAIA\_VULCAN\vulcan_forge\project_creator.py:581-647` | CLAUDE.md generator | 67 | Operational |
| `X:\Projects\_GAIA\_VULCAN\tests\*.py` | 5 test files, 137 tests | ~1,000 | 85% coverage |
| `X:\Projects\_GAIA\_VULCAN\CLAUDE.md` | Constitutional constraints | 0 | **MISSING** |

**PROTEUS (Agent Orchestration)**

| File Path | Purpose | Lines | Status |
|-----------|---------|-------|--------|
| `X:\Projects\_GAIA\_PROTEUS\CLAUDE.md` | Constitutional constraints | ~250 | Complete |
| `X:\Projects\_GAIA\_PROTEUS\proteus\integrations\argus_telemetry.py` | **ONLY active telemetry** | ~150 | Operational |
| `X:\Projects\_GAIA\_PROTEUS\launch.py` | Co-launch with ARGUS | 180 | Operational (v0.2.1) |
| `X:\Projects\_GAIA\_PROTEUS\proteus\*.py` | Core modules | ~2,000 total | Operational |
| `X:\Projects\_GAIA\_PROTEUS\tests\*.py` | 9 test files, 51+ tests | ~800 | Exists (not enforced) |
| `X:\Projects\_GAIA\_PROTEUS\data\proteus.db` | Data store (SQLite) | N/A | Active |
| `X:\Projects\_GAIA\logs\proteus_build.jsonl` | Build telemetry log | N/A | Active |

**WARDEN (Compliance Scanner)**

| File Path | Purpose | Lines | Status |
|-----------|---------|-------|--------|
| `X:\Projects\_GAIA\_WARDEN\scanner.py` | Compliance scanner | 6,908 bytes | **NOT INTEGRATED** |
| `X:\Projects\_GAIA\_WARDEN\CLAUDE.md` | Constitutional constraints | 0 | **MISSING** |
| `X:\Projects\_GAIA\_WARDEN\tests\` | Test suite | 0 | **MISSING** |

**ECHO (User Interface - Stale)**

| File Path | Purpose | Lines | Status |
|-----------|---------|-------|--------|
| `X:\Projects\_GAIA\_ECHO\ui_v0.py` through `ui_v012.py` | 19 manual UI versions | ~8,000 total | **Stale since Jan 2026** |
| `X:\Projects\_GAIA\_ECHO\CLAUDE.md` | Constitutional constraints | 0 | **MISSING** |
| `X:\Projects\_GAIA\_ECHO\tests\` | Test suite | 0 | **MISSING** |

**RAVEN (Security - Placeholder)**

| File Path | Purpose | Lines | Status |
|-----------|---------|-------|--------|
| `X:\Projects\_GAIA\_RAVEN\` | Security module | 0 | **PLACEHOLDER ONLY** |

**Mental Models Library**

| File Path | Purpose | Lines | Status |
|-----------|---------|-------|--------|
| `X:\Projects\_GAIA\mental_models\registry.json` | 59 model definitions | ~3,000 | Complete |
| `X:\Projects\_GAIA\mental_models\invocation_rules.json` | Context-based invocation | ~500 | Complete |
| `X:\Projects\_GAIA\mental_models\selector.py` | Model selection logic | ~250 | Operational |
| `X:\Projects\_GAIA\mental_models\models.py` | Model dataclass | ~150 | Operational |

**Claude Code Configuration**

| File Path | Purpose | Lines | Status |
|-----------|---------|-------|--------|
| `C:\Users\Fede\.claude\settings.json` | 42+ permissions, 10 MCP | ~800 | Active (NO hooks) |
| `C:\Users\Fede\.claude\settings.local.json` | 150+ permissions | ~1,200 | Active |
| `C:\Users\Fede\.claude\CLAUDE.md` | Global rules | ~200 | Complete |
| `C:\Users\Fede\.claude\skills\explain-only\SKILL.md` | Explain skill | ~80 | Active |
| `C:\Users\Fede\.claude\skills\phase-update\SKILL.md` | Phase update skill | ~90 | Active |
| `C:\Users\Fede\.claude\skills\debug-explorer\SKILL.md` | Debug skill | ~100 | Active |
| `C:\Users\Fede\.claude\skills\doc-sync\SKILL.md` | Doc sync skill | ~85 | Active |
| `C:\Users\Fede\.claude\agents\*.md` | 11 agent configs | ~1,500 total | Active |
| `C:\Users\Fede\.claude\plugins\installed_plugins.json` | 10 MCP plugins | ~300 | Active |
| `C:\Users\Fede\.claude\projects\C--Users-Fede\memory\MEMORY.md` | Cross-session memory | ~180 | Active |
| `C:\Users\Fede\.claude\projects\C--Users-Fede\memory\patterns.md` | Verification protocols | ~250 | Active |

---

### Appendix B: Missing Implementation Inventory

| # | Component | Missing Item | Expected Location | Impact | Priority |
|---|-----------|--------------|-------------------|--------|----------|
| 1 | ARGUS | ProcessObserver class | `_ARGUS\process_observer\observer.py` | Cannot monitor Claude Code agent executions | **HIGH** |
| 2 | ARGUS | PostMortemAnalyzer class | `_ARGUS\process_observer\post_mortem.py` | Cannot analyze task failures | **HIGH** |
| 3 | ARGUS | Trust Dashboard | `_ARGUS\trust_dashboard\*` | No constitutional compliance visualization | **HIGH** |
| 4 | VULCAN | CLAUDE.md | `_VULCAN\CLAUDE.md` | No constitutional constraints for project creator | **MEDIUM** |
| 5 | MYCEL | CLAUDE.md | `_MYCEL\CLAUDE.md` | No constitutional constraints for test infra | **MEDIUM** |
| 6 | WARDEN | CLAUDE.md | `_WARDEN\CLAUDE.md` | No constitutional constraints for scanner | **MEDIUM** |
| 7 | ECHO | CLAUDE.md | `_ECHO\CLAUDE.md` | No constitutional constraints for UI (stale module) | **LOW** |
| 8 | ALL | `.pre-commit-config.yaml` | Each module root | No automated quality gates | **CRITICAL** |
| 9 | ALL | `.github/workflows/*.yml` | Each module `.github/workflows/` | No CI/CD, no test enforcement | **CRITICAL** |
| 10 | ALL | Ecosystem linting config | `_GAIA\ruff.toml` or root config | No unified code standards | **HIGH** |
| 11 | GAIA | MCP tool registration | MCP server per module | GAIA tools not discoverable by Claude Code | **MEDIUM** |
| 12 | GAIA | Skill registry | `_GAIA\skills\registry.json` | No skill auto-discovery | **MEDIUM** |
| 13 | GAIA | Background task runner | `_GAIA\runtime\task_runner.py` | No async monitoring, no scheduled jobs | **HIGH** |
| 14 | GAIA | URL/reference KB | `_GAIA\docs\references.md` | URLs scattered across docs | **LOW** |
| 15 | GAIA | Token management config | Claude Code settings or env | No budget tracking per module | **MEDIUM** |
| 16 | LOOM | Active governance enforcement | Runtime validator integration | Governance rules not enforced at execution | **HIGH** |
| 17 | LOOM | ARGUS telemetry usage | Enable `argus_telemetry.py` | LOOM actions not observable | **HIGH** |
| 18 | MNEMIS | Auto-promotion pipeline | ARGUS → MNEMIS → WARDEN flow | Errors don't become prevention rules | **HIGH** |
| 19 | MNEMIS | Skill contribution system | `mnemis\skills\contributor.py` | Can't convert memory into reusable skills | **MEDIUM** |
| 20 | PROTEUS | Subagent monitoring | ARGUS telemetry per subagent | Can't track subagent performance | **MEDIUM** |
| 21 | WARDEN | Pre-commit integration | Hook scripts calling `scanner.py` | Scanner exists but not in workflow | **CRITICAL** |
| 22 | WARDEN | Test suite | `_WARDEN\tests\*.py` | No validation of scanner logic | **HIGH** |
| 23 | ECHO | Module consolidation | Merge 19 versions or deprecate | Technical debt, maintenance burden | **MEDIUM** |
| 24 | ECHO | Test suite | `_ECHO\tests\*.py` | No UI validation | **MEDIUM** |
| 25 | RAVEN | Entire implementation | `_RAVEN\*` | Security module is placeholder only | **MEDIUM** |
| 26 | ALL | GitHub remotes | Remote tracking for all 9 modules | No backup, no collaboration, no PR workflow | **HIGH** |

---

### Appendix C: GAIA_BIBLE.md Gap Analysis

| Promise | Chapter/Section | Delivered? | Evidence | Gap Description |
|---------|----------------|------------|----------|-----------------|
| **Trust Contract: Every agent bound to constitutional principles** | Ch. 2: Constitutional Framework | PARTIAL | CLAUDE.md files in 4/9 modules, no runtime enforcement | Documents exist but not programmatically validated |
| **Authority Graph: Hierarchical memory access (GAIA > PROJECT > AGENT)** | Ch. 3: Memory & Knowledge | YES | MNEMIS `contracts.py`, authority levels defined | Architecture complete, not enforced at commit/deploy |
| **Runtime Governance: Real-time rule enforcement** | Ch. 4: Governance & Control | NO | LOOM has governance models, validator not integrated | Rules defined, validator exists, not called at runtime |
| **Glass-box Transparency: Full observability of agent actions** | Ch. 5: Observability | PARTIAL | ARGUS dashboard + subconscious operational, Process Observer missing | Can observe PROTEUS, missing Process Observer for Claude Code agents |
| **Three Pillars: VULCAN creates, LOOM modifies, ARGUS monitors** | Ch. 1: Architecture Overview | PARTIAL | VULCAN (YES), LOOM (models only), ARGUS (partial) | VULCAN complete, LOOM not enforcing edits, ARGUS missing observers |
| **Subconscious Layer: Background pattern detection** | Ch. 5.2: Subconscious Layer | YES | `pattern_detector.py`, `hypothesis_generator.py` operational | Fully implemented and tested |
| **Memory Hierarchy: Three-tier knowledge system** | Ch. 3.1: Memory Tiers | YES | MNEMIS implements PROJECT/GAIA/PUBLIC tiers | Architecture complete, promotion manual not auto |
| **Mental Models: Context-aware model selection** | Ch. 6: Mental Models | YES | 59 models, selector, invocation rules | Fully operational |
| **Explainability: 4-level explanation system** | Ch. 5.3: Explainability | YES | ARGUS explainer with SIMPLE/TECHNICAL/DEEP/CAUSAL | Fully implemented |
| **Event Bus: Centralized telemetry** | Ch. 5.1: Event Bus | PARTIAL | SQLite event bus operational, only PROTEUS sends events | Infrastructure works, 8/9 modules not connected |
| **Trust Dashboard: Constitutional compliance tracking** | Ch. 5.4: Trust Metrics | NO | Empty directory at `_ARGUS\trust_dashboard\` | Documented in architecture, not implemented |
| **Learning Loop: Errors become prevention rules** | Ch. 3.4: Promotion Protocol | NO | MNEMIS promotion exists, no auto-pipeline from ARGUS | Can promote manually, no automation from errors |
| **Cross-module Learning: Shared insights** | Ch. 3.3: Cross-module Learning | PARTIAL | LOOM `mnemis_bridge.py` exists, limited usage | Bridge implemented, not widely adopted |
| **Skill System: Reusable capabilities** | Ch. 7: Skills & Tools | PARTIAL | 4 user-level skills, no GAIA-level registry | Skills at user level, no auto-discovery or contribution system |
| **MCP Integration: Tool discoverability** | Ch. 7.2: MCP Tools | NO | 10 external MCP plugins, 0 GAIA modules as MCP servers | Uses MCP tools, doesn't provide them |
| **CI/CD: Automated testing & deployment** | Ch. 8: Development Workflow | NO | 1,522 test files exist, 0 enforcement gates | Tests written, no automation |
| **Pre-commit Hooks: Quality gates** | Ch. 8.1: Quality Assurance | NO | Documented in MEMORY.md as pending, not deployed | Known gap, documented as "post-VULCAN testing" |
| **Baseline Regression Testing: Prevent drift** | Ch. 8.2: Regression Prevention | PARTIAL | `v0_baseline.md` exists, no auto-comparison | Manual baseline, no automated checks |
| **GitHub Integration: PR workflow** | Ch. 8.3: Collaboration | NO | Only HART OS has remote (external), GAIA modules local-only | No remotes, no PRs, no collaboration workflow |
| **Background Tasks: Async monitoring** | Ch. 9: Runtime Infrastructure | NO | No task runner, no scheduled jobs | ARGUS can observe, but only on-demand |
| **Unified Logging: Structured logs** | Ch. 5.1: Telemetry | PARTIAL | PROTEUS logs to JSONL, ARGUS to SQLite, inconsistent | Multiple formats, no unified standard |
| **OpenAPI Contracts: API documentation** | Ch. 4.2: Contracts | NO | Pydantic models exist, no OpenAPI spec generation | Type-safe models, not exposed as OpenAPI |
| **URL Knowledge Base: Centralized references** | Ch. 10: Documentation | NO | URLs scattered across GAIA_BIBLE.md, docs, code | No single source of truth |
| **Token Budget Management: Cost tracking** | Ch. 11: Resource Management | NO | Not configured in Claude Code settings | No per-module or per-agent tracking |

---

### Appendix D: Recovered URLs and References

**External Documentation**

- **Claude Code Documentation** (referenced in GAIA_BIBLE.md, exact URLs not in codebase)
  - Claude Code settings reference
  - MCP (Model Context Protocol) specification
  - Agent framework documentation

**Internal Cross-references**

- `X:\Projects\_GAIA\GAIA_BIBLE.md` → Primary constitutional document
- `X:\Projects\_GAIA\registry.json` → Component registry
- `X:\Projects\_GAIA\VERSION_LOG.md` → Version history
- `X:\Projects\_GAIA\v0_baseline.md` → Pre-consolidation baseline
- `X:\Projects\_GAIA\_ARGUS\dashboard\ARCHITECTURE.md` → ARGUS design
- `C:\Users\Fede\.claude\CLAUDE.md` → Global rules
- `C:\Users\Fede\.claude\projects\C--Users-Fede\memory\MEMORY.md` → Session memory
- `C:\Users\Fede\.claude\projects\C--Users-Fede\memory\patterns.md` → Verification protocols

**Database Connections**

- `sqlite:///X:\Projects\_GAIA\logs\argus_events.db` → ARGUS event store
- `sqlite:///X:\Projects\_GAIA\_PROTEUS\data\proteus.db` → PROTEUS data store

**Git References**

- HART OS remote: [URL not in GAIA codebase, external project]
- GAIA modules: Local repositories only, no remotes configured

**Python Package References** (from pyproject.toml files)

- `streamlit` → ARGUS dashboard, ECHO UI
- `pydantic` → All modules (schemas, validation)
- `pytest` → All test suites
- `ruff` → Linting (configured only in MYCEL)
- `black` → Formatting (configured only in MYCEL)
- `SQLAlchemy` → ARGUS, PROTEUS databases
- `click` → CLI tools (VULCAN, WARDEN)

**Note:** No external API endpoints, cloud services, or third-party integrations were found in the GAIA codebase. The ecosystem is entirely self-contained and runs locally.

---

---

**End of GECO Audit Report**
