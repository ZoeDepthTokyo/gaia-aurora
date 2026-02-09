# GECO Review Matrix — Claude Code Feature Audit

**Date:** 2026-02-09
**Scope:** All 16 registered GAIA ecosystem components
**Purpose:** Evaluate Claude Code integration maturity across all agents/products
**Type:** Evaluation only (no execution)

---

## Legend

| Symbol | Meaning |
|--------|---------|
| :white_check_mark: | Configured and active |
| :construction: | Partially configured / scaffolded |
| :x: | Not configured |
| N/A | Not applicable for this component type |

---

## 1. Summary Matrix

| # | Component | Type | CLAUDE.md | .claude/ folder | Hooks | Subagents | Skills (Slash Cmds) | Memory/Sessions | Plugins | MCP Connections | Permissions | Git |
|---|-----------|------|-----------|-----------------|-------|-----------|---------------------|-----------------|---------|-----------------|-------------|-----|
| 1 | **ARGUS** | Shared Service | :white_check_mark: | :x: | :x: | :x: | :x: | :x: | :x: | :x: | :x: | :white_check_mark: |
| 2 | **LOOM** | Shared Service | :white_check_mark: | :x: | :x: | :x: | :x: | :x: | :x: | :x: | :x: | :white_check_mark: |
| 3 | **MNEMIS** | Shared Service | :white_check_mark: | :x: | :x: | :x: | :x: | :x: | :x: | :x: | :x: | :white_check_mark: |
| 4 | **MYCEL** | Shared Service | :x: | :x: | :x: | :x: | :x: | :x: | :x: | :x: | :x: | :white_check_mark: |
| 5 | **VULCAN** | Shared Service | :x: | :x: | :x: | :x: | :x: | :x: | :x: | :x: | :x: | :white_check_mark: |
| 6 | **WARDEN** | Shared Service | :x: | :x: | :x: | :x: | :x: | :x: | :x: | :x: | :x: | :x: |
| 7 | **RAVEN** | Shared Service | :x: | :x: | :x: | :x: | :x: | :x: | :x: | :x: | :x: | :x: |
| 8 | **ABIS** | Shared Service | :x: | :x: | :x: | :x: | :x: | :x: | :x: | :x: | :x: | :x: |
| 9 | **HART OS** | Product | :x: | :white_check_mark: | :x: | :x: | :x: | :x: | :x: | :x: | :white_check_mark: | :white_check_mark: |
| 10 | **VIA** | Product | :x: | :x: | :x: | :x: | :x: | :x: | :x: | :x: | :x: | :white_check_mark: |
| 11 | **DATA FORGE** | Product | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :x: | :x: | :white_check_mark: | :white_check_mark: |
| 12 | **jSeeker** | Product | :white_check_mark: | :x: | :x: | :x: | :x: | :x: | :x: | :x: | :x: | :white_check_mark: |
| 13 | **GPT_ECHO** | Product | :x: | :x: | :x: | :x: | :x: | :x: | :x: | :x: | :x: | :x: |
| 14 | **DOS** | Product | :x: | :x: | :x: | :x: | :x: | :x: | :x: | :x: | :x: | :x: |
| 15 | **The Palace** | Product | :x: | :x: | :x: | :x: | :x: | :x: | :x: | :x: | :x: | :x: |
| 16 | **Mental Models** | Library | :x: | :x: | :x: | :x: | :x: | :x: | :x: | :x: | :x: | :white_check_mark: |

---

## 2. Detailed Per-Component Audit

### 2.1 SHARED SERVICES

---

#### ARGUS — The Watchman
| Feature | Status | Details |
|---------|--------|---------|
| **CLAUDE.md** | :white_check_mark: | `_ARGUS/CLAUDE.md` — Role, constraints, directory structure, coding patterns, integrations, DO NOTs |
| **.claude/ folder** | :x: | No `.claude/` directory exists |
| **Hooks** | :x: | No Claude Code hooks configured |
| **Subagents** | :x: | No custom agent definitions (`.claude/agents/`) |
| **Skills / Slash Commands** | :x: | No custom commands (`.claude/commands/`) |
| **Memory / Sessions** | :x: | No session persistence configured. Context tracked only via global memory system |
| **Plugins** | :x: | No project-level plugins |
| **MCP Connections** | :x: | No `.mcp.json` at project level |
| **Permissions** | :x: | No `settings.local.json` — relies on global permissions |
| **Git** | :white_check_mark: | Git initialized per registry |

**Gap Assessment:** ARGUS has a strong CLAUDE.md defining its read-only observer role, but lacks all Claude Code operational infrastructure (hooks, agents, commands, permissions). As a monitoring service, many features are less critical — but permissions should be locked down to enforce the "read-only" constitutional constraint.

---

#### LOOM — Visual Agent Editor
| Feature | Status | Details |
|---------|--------|---------|
| **CLAUDE.md** | :white_check_mark: | `_LOOM/CLAUDE.md` — Agent types (4), workflow engine, governance rules, glass-box transparency |
| **.claude/ folder** | :x: | No `.claude/` directory exists |
| **Hooks** | :x: | No hooks |
| **Subagents** | :x: | No custom agents |
| **Skills / Slash Commands** | :x: | No slash commands |
| **Memory / Sessions** | :x: | No session config |
| **Plugins** | :x: | No plugins |
| **MCP Connections** | :x: | No MCP |
| **Permissions** | :x: | No permissions file |
| **Git** | :white_check_mark: | Git initialized |

**Gap Assessment:** CLAUDE.md defines the workflow engine well. Missing operational tooling. LOOM's "no autonomous action" constraint should be enforced via permissions deny rules.

---

#### MNEMIS — Cross-Project Memory
| Feature | Status | Details |
|---------|--------|---------|
| **CLAUDE.md** | :white_check_mark: | `_MNEMIS/CLAUDE.md` — Three-tier hierarchy, promotion workflow, provenance tracking |
| **.claude/ folder** | :x: | No `.claude/` directory |
| **Hooks** | :x: | No hooks |
| **Subagents** | :x: | No custom agents |
| **Skills / Slash Commands** | :x: | No slash commands |
| **Memory / Sessions** | :x: | Ironic: the memory service itself has no Claude Code session persistence |
| **Plugins** | :x: | No plugins |
| **MCP Connections** | :x: | No MCP |
| **Permissions** | :x: | No permissions |
| **Git** | :white_check_mark: | Git initialized |

**Gap Assessment:** Well-documented CLAUDE.md. The memory hierarchy rules (GAIA > PROJECT > AGENT) should be enforced via hooks that validate write operations. Session persistence would be valuable given MNEMIS's cross-project nature.

---

#### MYCEL — Shared Intelligence Library
| Feature | Status | Details |
|---------|--------|---------|
| **CLAUDE.md** | :x: | **Missing** — No CLAUDE.md file |
| **.claude/ folder** | :x: | No `.claude/` directory |
| **Hooks** | :x: | No hooks |
| **Subagents** | :x: | No custom agents |
| **Skills / Slash Commands** | :x: | No slash commands |
| **Memory / Sessions** | :x: | No session config |
| **Plugins** | :x: | No plugins |
| **MCP Connections** | :x: | No MCP |
| **Permissions** | :x: | No permissions |
| **Git** | :white_check_mark: | Git initialized |

**Gap Assessment:** **Critical gap.** MYCEL is the shared intelligence library used by nearly every component (VIA, VULCAN, LOOM, MNEMIS, ARGUS, jSeeker, GPT_ECHO, WARDEN, RAVEN, ABIS, DOS). It needs a CLAUDE.md at minimum to define API contracts, model routing rules, and cost constraints.

---

#### VULCAN — The Forge
| Feature | Status | Details |
|---------|--------|---------|
| **CLAUDE.md** | :x: | **Missing** — Has `claude_md_generator.py` (ENG-010) but no own CLAUDE.md |
| **.claude/ folder** | :x: | No `.claude/` directory |
| **Hooks** | :x: | No hooks |
| **Subagents** | :x: | No custom agents |
| **Skills / Slash Commands** | :x: | No slash commands |
| **Memory / Sessions** | :x: | No session config |
| **Plugins** | :x: | No plugins |
| **MCP Connections** | :x: | No MCP |
| **Permissions** | :x: | No permissions |
| **Git** | :white_check_mark: | Git initialized |

**Gap Assessment:** Ironic: VULCAN has a CLAUDE.md *generator* (ENG-010) but lacks its own CLAUDE.md. Should be first to benefit from its own tooling.

---

#### WARDEN — Governance & Compliance
| Feature | Status | Details |
|---------|--------|---------|
| **CLAUDE.md** | :x: | **Missing** — Only has README.md placeholder |
| **.claude/ folder** | :x: | No `.claude/` directory |
| **Hooks** | :x: | No Claude Code hooks (has pre-commit framework via ENG-009, but not integrated into `.claude/`) |
| **Subagents** | :x: | No custom agents |
| **Skills / Slash Commands** | :x: | No slash commands |
| **Memory / Sessions** | :x: | No session config |
| **Plugins** | :x: | No plugins |
| **MCP Connections** | :x: | No MCP |
| **Permissions** | :x: | No permissions |
| **Git** | :x: | Not git initialized |

**Gap Assessment:** **Critical gap.** WARDEN is the governance layer — it should be the *most* configured with hooks (pre-commit validation), permissions (deny destructive ops), and Claude Code integration. The CLI exists (ENG-001) but isn't wired into Claude Code's hook system.

---

#### RAVEN — Autonomous Research Agent
| Feature | Status | Details |
|---------|--------|---------|
| **CLAUDE.md** | :x: | **Missing** — Has README.md with use cases and roadmap |
| **.claude/ folder** | :x: | No `.claude/` directory |
| **Hooks** | :x: | No hooks |
| **Subagents** | :x: | No custom agents (ironically, RAVEN IS designed to be an agent) |
| **Skills / Slash Commands** | :x: | No slash commands |
| **Memory / Sessions** | :x: | No session persistence (critical for research continuity) |
| **Plugins** | :x: | No plugins |
| **MCP Connections** | :x: | No MCP (would benefit from WebSearch, Notion integration) |
| **Permissions** | :x: | No permissions |
| **Git** | :x: | Not git initialized |

**Gap Assessment:** RAVEN is defined but has zero Claude Code infrastructure. As an autonomous research agent, it critically needs: session persistence (multi-exchange research), MCP connections (web search, Notion for report storage), and custom subagents.

---

#### ABIS — Visual System Builder
| Feature | Status | Details |
|---------|--------|---------|
| **CLAUDE.md** | :x: | **Missing** — Only scaffolded (planning status) |
| **.claude/ folder** | :x: | No `.claude/` directory |
| **Hooks** | :x: | No hooks |
| **Subagents** | :x: | No custom agents |
| **Skills / Slash Commands** | :x: | No slash commands |
| **Memory / Sessions** | :x: | No session config |
| **Plugins** | :x: | No plugins |
| **MCP Connections** | :x: | No MCP |
| **Permissions** | :x: | No permissions |
| **Git** | :x: | Not git initialized |

**Gap Assessment:** Still in planning phase. Infrastructure setup should happen when active development begins. Would benefit from Figma MCP integration for visual design work.

---

### 2.2 PRODUCTS

---

#### HART OS — Therapeutic Assessment System
| Feature | Status | Details |
|---------|--------|---------|
| **CLAUDE.md** | :x: | **Missing** — No CLAUDE.md file in project root |
| **.claude/ folder** | :white_check_mark: | `.claude/settings.local.json` exists |
| **Hooks** | :x: | No hooks in settings |
| **Subagents** | :x: | No custom agents |
| **Skills / Slash Commands** | :x: | No slash commands |
| **Memory / Sessions** | :x: | No session config |
| **Plugins** | :x: | No project-level plugins |
| **MCP Connections** | :x: | No MCP |
| **Permissions** | :white_check_mark: | `settings.local.json` with allow rules: python, git diff, pytest, ruff, mypy, py_compile, dir, pip install |
| **Git** | :white_check_mark: | Git initialized with remote (`github.com/ZoeDepthTokyo/hart-os.git`) |

**Gap Assessment:** Production-ready product with basic permissions but missing CLAUDE.md. The settings.local.json has accumulated ad-hoc permission entries (some very specific bash commands from past sessions). Needs cleanup and a proper CLAUDE.md for context.

---

#### VIA Intelligence — Investment Analysis
| Feature | Status | Details |
|---------|--------|---------|
| **CLAUDE.md** | :x: | **Missing** |
| **.claude/ folder** | :x: | No `.claude/` directory |
| **Hooks** | :x: | No hooks |
| **Subagents** | :x: | No custom agents |
| **Skills / Slash Commands** | :x: | No slash commands |
| **Memory / Sessions** | :x: | No session config |
| **Plugins** | :x: | No plugins |
| **MCP Connections** | :x: | No MCP (would benefit from financial data APIs) |
| **Permissions** | :x: | No permissions |
| **Git** | :white_check_mark: | Git initialized |

**Gap Assessment:** Production product with multi-provider LLM support (Gemini, OpenAI, Anthropic) but zero Claude Code infrastructure. Needs CLAUDE.md at minimum.

---

#### DATA FORGE — Intelligent Document Processing :star: GOLD STANDARD
| Feature | Status | Details |
|---------|--------|---------|
| **CLAUDE.md** | :white_check_mark: | **Comprehensive** (511 lines) — Full project context, coding patterns, workflows, gotchas, agent/command reference |
| **.claude/ folder** | :white_check_mark: | Full structure: `agents/`, `commands/`, `settings.json` |
| **Hooks** | :white_check_mark: | **4 hooks configured:** PreToolUse (security validation on Write/Edit), SessionStart (load context), SessionEnd (save state), PostToolUse (doc reminder on Write/Edit) |
| **Subagents** | :white_check_mark: | **8 custom agents:** product-owner, ux-design-lead, architect, planner, code-reviewer, tdd-guide, senior-python-ml-engineer, doc-updater |
| **Skills / Slash Commands** | :white_check_mark: | **7 commands:** `/prd`, `/plan`, `/review`, `/tdd`, `/ux`, `/architect`, `/docs` |
| **Memory / Sessions** | :white_check_mark: | SessionStart/SessionEnd hooks for context persistence across sessions. Session summaries at `.claude/session-summaries/` |
| **Plugins** | :x: | No project-level plugins (inherits global) |
| **MCP Connections** | :x: | No project-level MCP (inherits global: Notion, Pinecone, Figma, etc.) |
| **Permissions** | :white_check_mark: | **3-tier system:** Allow (read, glob, grep, python, pytest, ruff, mypy, git read-only, streamlit), Ask (write, edit, pip install, git commit/push), Deny (.env, secrets, credentials, rm -rf, force push, pip uninstall) |
| **Git** | :white_check_mark: | Git initialized |

**Gap Assessment:** **This is the gold standard for the ecosystem.** Every other component should aspire to this level of Claude Code integration. The Bootstrap System (ENG-010) should generate configurations modeled after Data Forge.

---

#### jSeeker — Job Seeking & Resume Adaptation (formerly PROTEUS)
| Feature | Status | Details |
|---------|--------|---------|
| **CLAUDE.md** | :white_check_mark: | At `jSeeker/CLAUDE.md` — Updated from PROTEUS naming. Role, constraints, structure, patterns |
| **.claude/ folder** | :x: | No `.claude/` directory |
| **Hooks** | :x: | No hooks |
| **Subagents** | :x: | No custom agents |
| **Skills / Slash Commands** | :x: | No slash commands |
| **Memory / Sessions** | :x: | No session config |
| **Plugins** | :x: | No plugins |
| **MCP Connections** | :x: | No MCP |
| **Permissions** | :x: | No permissions |
| **Git** | :white_check_mark: | Git initialized |

**Gap Assessment:** Has CLAUDE.md but nothing else. As an active product using Anthropic API directly, it would benefit from permissions (deny .env reads, budget constraints) and hooks (cost tracking validation).

**Note:** Old `_PROTEUS/CLAUDE.md` still exists with PROTEUS naming — should be removed to avoid confusion.

---

#### GPT_ECHO — ChatGPT Archaeology
| Feature | Status | Details |
|---------|--------|---------|
| **CLAUDE.md** | :x: | **Missing** |
| **.claude/ folder** | :x: | No `.claude/` directory |
| **Hooks** | :x: | No hooks |
| **Subagents** | :x: | No custom agents |
| **Skills / Slash Commands** | :x: | No slash commands |
| **Memory / Sessions** | :x: | No session config |
| **Plugins** | :x: | No plugins |
| **MCP Connections** | :x: | No MCP |
| **Permissions** | :x: | No permissions |
| **Git** | :x: | Not git initialized (status: stale) |

**Gap Assessment:** Stale project with zero infrastructure. Low priority unless reactivated.

---

#### DOS — Multi-Agent Decision System
| Feature | Status | Details |
|---------|--------|---------|
| **CLAUDE.md** | :x: | **Missing** — Only README.md scaffold |
| **.claude/ folder** | :x: | No `.claude/` directory |
| **Hooks** | :x: | No hooks |
| **Subagents** | :x: | No custom agents (ironic for a multi-agent system) |
| **Skills / Slash Commands** | :x: | No slash commands |
| **Memory / Sessions** | :x: | No session config |
| **Plugins** | :x: | No plugins |
| **MCP Connections** | :x: | No MCP |
| **Permissions** | :x: | No permissions |
| **Git** | :x: | Not git initialized |

**Gap Assessment:** Planning phase. As a multi-agent decision system, DOS would be a prime candidate for full Claude Code integration (subagents, session persistence, MCP connections).

---

#### The Palace — Case Study (Static HTML)
| Feature | Status | Details |
|---------|--------|---------|
| **CLAUDE.md** | :x: | Missing |
| **.claude/ folder** | :x: | No `.claude/` |
| All other features | N/A | Static HTML product — Claude Code features not applicable |
| **Git** | :x: | Not git initialized |

**Gap Assessment:** Complete static product. Claude Code integration not needed.

---

#### Mental Models Library
| Feature | Status | Details |
|---------|--------|---------|
| **CLAUDE.md** | :x: | Missing |
| **.claude/ folder** | :x: | No `.claude/` |
| All other features | :x: | None configured |
| **Git** | :white_check_mark: | Git initialized |

**Gap Assessment:** Library component bundled with ARGUS. Could inherit ARGUS's eventual Claude Code config.

---

## 3. Global-Level Configuration (Inherited by All)

These are configured at `~/.claude/` and apply ecosystem-wide:

| Feature | Status | Details |
|---------|--------|---------|
| **Global CLAUDE.md** | :white_check_mark: | `~/.claude/CLAUDE.md` — Response style, environment, tech stack, workflow preferences, GAIA rules |
| **Global settings.json** | :white_check_mark: | Permissions (allow/ask), additional directories, plugins, experimental agent teams |
| **Plugins (10 enabled)** | :white_check_mark: | context7, code-review, serena, figma, greptile, Notion, claude-md-management, claude-code-setup, huggingface-skills, pinecone |
| **MCP Connections** | :white_check_mark: | Via plugins: Notion, Pinecone, Figma, Context7, Greptile, Serena |
| **Memory System** | :white_check_mark: | `~/.claude/projects/C--Users-Fede/memory/` with MEMORY.md + session files |
| **Experimental Flags** | :white_check_mark: | `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` |

**Note:** All projects inherit these global configs. However, MCP tools are NOT available to subagents (Task tool), only from the main context window.

---

## 4. Maturity Scorecard

Scoring: each feature = 1 point (max 10 per component)

| Component | Score | Grade | Priority for Remediation |
|-----------|-------|-------|--------------------------|
| **DATA FORGE** | **9/10** | A+ | Reference implementation |
| **HART OS** | 2/10 | D | P1 — Production product, needs CLAUDE.md + cleanup |
| **ARGUS** | 2/10 | D | P1 — Core service, well-documented but not wired |
| **LOOM** | 2/10 | D | P2 — Good docs, needs ops config |
| **MNEMIS** | 2/10 | D | P2 — Good docs, needs ops config |
| **jSeeker** | 2/10 | D | P1 — Active product, needs permissions + hooks |
| **MYCEL** | 1/10 | F | **P0** — Critical shared dependency, no docs at all |
| **VULCAN** | 1/10 | F | P1 — Should use its own generator |
| **WARDEN** | 0/10 | F | **P0** — Governance layer with zero governance on itself |
| **VIA** | 1/10 | F | P1 — Production product with nothing |
| **RAVEN** | 0/10 | F | P2 — Defined but not built |
| **ABIS** | 0/10 | F | P3 — Still planning |
| **DOS** | 0/10 | F | P3 — Still planning |
| **GPT_ECHO** | 0/10 | F | P3 — Stale |
| **The Palace** | 0/10 | N/A | Static — no action needed |
| **Mental Models** | 1/10 | F | P3 — Library, low priority |

---

## 5. Key Findings

### 5.1 Critical Gaps

1. **Only 1 of 16 components has full Claude Code integration** (DATA FORGE)
2. **MYCEL has no CLAUDE.md** despite being depended on by 10+ components
3. **WARDEN (the governance service) has zero governance infrastructure** on itself
4. **No component has project-level MCP connections** — all rely on global inheritance
5. **No component has project-level plugins** — all rely on global inheritance
6. **Session persistence exists only in DATA FORGE** via hooks
7. **Permission security is inconsistent** — HART OS has ad-hoc accumulated permissions; most have none

### 5.2 Ecosystem-Level Observations

- **Global config is strong** (10 plugins, memory system, CLAUDE.md, experimental features)
- **Project-level config is almost universally absent** — the ecosystem runs on global defaults
- **The VULCAN CLAUDE.md generator (ENG-010) exists but has never been used** on any GAIA component
- **Pre-commit framework (ENG-009) exists but isn't wired into any `.claude/settings.json` hooks**
- **Stale PROTEUS CLAUDE.md** at `_GAIA/_PROTEUS/CLAUDE.md` should be cleaned up (jSeeker has its own)

### 5.3 Data Forge as Template

DATA FORGE demonstrates the target state for all components:
- **CLAUDE.md**: Role, constraints, structure, patterns, gotchas, commands reference
- **.claude/agents/**: 8 specialized subagents with model routing
- **.claude/commands/**: 7 slash commands covering full dev lifecycle
- **.claude/settings.json**: 3-tier permissions (allow/ask/deny) + 4 hooks
- **Session persistence**: Start/end hooks for context continuity

---

## 6. Recommended Remediation Priority

### P0 — Immediate (Structural Integrity)
| Task | Component | Effort |
|------|-----------|--------|
| Create CLAUDE.md | MYCEL | Medium — define API contracts, model routing, cost rules |
| Create CLAUDE.md | WARDEN | Medium — define governance rules, CLI usage, hook integration |
| Wire WARDEN CLI into Claude Code hooks | WARDEN + Global | Low — add PreToolUse hook calling `warden validate` |

### P1 — Near-Term (Active Projects)
| Task | Component | Effort |
|------|-----------|--------|
| Run VULCAN generator on itself | VULCAN | Low — eat your own dogfood |
| Create CLAUDE.md | HART OS, VIA | Medium |
| Add .claude/settings.json with permissions | jSeeker, HART OS (cleanup) | Low |
| Remove stale `_PROTEUS/CLAUDE.md` | _GAIA/_PROTEUS | Trivial |
| Add session hooks (start/end) | jSeeker, HART OS | Low — copy Data Forge pattern |

### P2 — Medium-Term (Ecosystem Consistency)
| Task | Component | Effort |
|------|-----------|--------|
| Create CLAUDE.md | RAVEN, ABIS | Medium |
| Add .claude/ folder with agents + commands | ARGUS, LOOM, MNEMIS | Medium — define service-specific agents |
| Add permissions deny rules | All components with CLAUDE.md constraints | Low |
| Wire pre-commit hooks into `.claude/settings.json` | Ecosystem-wide | Medium |
| Add session persistence hooks | All active components | Low — templated from Data Forge |

### P3 — Future (When Activated)
| Task | Component | Effort |
|------|-----------|--------|
| Full Claude Code setup | DOS, GPT_ECHO | High — when development begins |
| Project-level MCP connections | RAVEN (web search), VIA (financial APIs) | Medium |
| Project-level plugins | As needed per component | Low |

---

## 7. Relationship to ENG Tasks

This review connects to the following open engineering tasks from `FEEDBACK_EVALUATION.md`:

- **ENG-010 (VULCAN Generator)**: Complete — should now be *used* on all components
- **ENG-009 (Pre-commit)**: Complete — should be wired into Claude Code hooks
- **ENG-001 (WARDEN CLI)**: Complete — should be integrated as PreToolUse hook
- **Missing ENG task**: "Bootstrap Claude Code config across all GAIA components" — use VULCAN generator + Data Forge template

---

*Generated by GAIA ecosystem review. Evaluation only — no changes executed.*
