# GAIA Token Budget Management

**Version:** 1.0 | **Updated:** 2026-02-09

---

## Overview

Token budget management ensures cost-effective LLM usage across the GAIA ecosystem. Each module routes tasks to the cheapest model that meets quality requirements, tracks usage via ARGUS telemetry, and enforces monthly budget caps.

---

## 1. Current Token Tracking

### jSeeker (Reference Implementation)

jSeeker implements the most complete token tracking in the ecosystem:

**Cost Tracking (`jseeker/llm.py`)**
- Every API call records: model, task name, input/output/cache tokens, cost in USD
- Costs stored in `APICost` Pydantic model and persisted to SQLite
- Session costs accessible via `llm.get_session_costs()` and `llm.get_total_session_cost()`
- Monthly budget enforcement via `BudgetExceededError` (configurable cap)

**ARGUS Telemetry (`jseeker/integrations/argus_telemetry.py`)**
- Build events: agent, wave, module, status, duration
- Runtime events: task, model, cost_usd, input_tokens, output_tokens
- All events written as JSONL to `X:\Projects\_GAIA\logs\jseeker_runtime.jsonl`

**Prompt Caching**
- SHA256-based local cache (memory + disk) prevents redundant API calls
- Anthropic prompt caching (`cache_control: ephemeral`) for system prompts
- Cache read tokens priced at ~10% of input tokens (significant savings)

### Other Modules

| Module | Provider | Tracking Status |
|--------|----------|-----------------|
| HART OS | OpenAI | Basic logging, no ARGUS integration |
| VIA | Gemini/OpenAI/Anthropic | MYCEL-based, partial tracking |
| MYCEL | Multi-provider | Library-level tracking available |

---

## 2. Model Routing Per Task Type

### Anthropic (jSeeker, RAVEN)

| Task Type | Model | Cost (per 1M tokens) | Use When |
|-----------|-------|---------------------|----------|
| JD parsing, bullet extraction, classification | Haiku | $0.80 in / $4.00 out | Speed and cost matter more than nuance |
| Resume adaptation, ATS scoring, outreach drafts | Sonnet | $3.00 in / $15.00 out | Quality and accuracy are important |
| Architecture planning, system design | Opus | $15.00 in / $75.00 out | Multi-step reasoning, complex decisions |

### OpenAI (HART OS)

| Task Type | Model | Use When |
|-----------|-------|----------|
| Scoring, classification | GPT-4o-mini | Deterministic pipeline steps |
| Therapeutic language, complex analysis | GPT-4o | Sensitivity and nuance required |

### Gemini (VIA)

| Task Type | Model | Use When |
|-----------|-------|----------|
| RAG retrieval, claim extraction | Gemini 2.0 Flash | High-volume semantic search |
| Investment synthesis, complex analysis | Gemini 2.0 Pro | Accuracy-critical financial analysis |

---

## 3. Session Budget Guidelines

### Quick Fix Sessions
- **Budget:** ~50,000 tokens max
- **Models:** Haiku, Sonnet
- **Typical tasks:** Bug fixes, small feature tweaks, config changes
- **Strategy:** Haiku-first, Sonnet only if quality insufficient

### Feature Development Sessions
- **Budget:** ~200,000 tokens max
- **Models:** Sonnet, Opus (sparingly)
- **Typical tasks:** New features, multi-file changes, test writing
- **Strategy:** Sonnet for implementation, Opus only for design decisions

### Architecture Sessions
- **Budget:** ~500,000 tokens max
- **Models:** Opus primarily
- **Typical tasks:** System design, cross-project refactoring, GAIA planning
- **Strategy:** Opus for reasoning, Sonnet for implementation

---

## 4. CLAUDE.md Progressive Disclosure (Token Savings)

### The Problem
Loading the full CLAUDE.md into every session wastes context window tokens on rules that may not be relevant.

### The Solution: Two-Tier System
- **L1 (`CLAUDE.md`):** Always loaded. Under 30 lines. Contains environment, top 5 rules, GAIA awareness, subagent limitations.
- **L2 (`CLAUDE_L2.md`):** Loaded on demand. Full coding patterns, detailed GAIA principles, extended workflow preferences, project-specific notes.

### Estimated Token Savings
| Scenario | Old (flat file) | New (L1 only) | Savings |
|----------|-----------------|---------------|---------|
| Quick question | ~600 tokens | ~400 tokens | ~33% |
| Code task (no GAIA) | ~600 tokens | ~400 tokens | ~33% |
| GAIA architecture | ~600 tokens | ~600 tokens (L1+L2) | 0% (appropriate) |

The savings compound across hundreds of sessions. At ~200 tokens saved per session across 10+ sessions/day, this is ~2,000 tokens/day or ~60,000 tokens/month of unnecessary context eliminated.

---

## 5. Future: Per-Module Budget Alerts in ARGUS

### Planned Features (Phase 4+)

**ARGUS Trust Dashboard Integration**
- Real-time cost display per module on the ARGUS dashboard
- Daily/weekly/monthly cost trends with configurable alert thresholds
- Model usage breakdown (which tasks use which models)
- Budget burn rate projection ("at current rate, monthly budget exhausted by...")

**Alert Rules**
- Warning at 80% of monthly module budget
- Critical at 95% of monthly module budget
- Auto-downgrade to cheaper model at 100% (if configured)
- Cross-module cost anomaly detection (sudden spikes)

**Configuration**
- Per-module budgets defined in `X:\Projects\_GAIA\token_budget.json`
- Alert thresholds configurable per module
- Override capability for one-time expensive tasks

**Implementation Path**
1. Standardize ARGUS telemetry format across all modules (jSeeker pattern)
2. Add cost aggregation endpoint to ARGUS dashboard
3. Build alert rule engine with configurable thresholds
4. Add budget enforcement middleware (like jSeeker's `BudgetExceededError`)
5. Dashboard visualization: cost charts, budget gauges, model mix pie charts

---

## 6. Best Practices

1. **Always route to the cheapest viable model.** Start with Haiku; upgrade only when quality demands it.
2. **Use prompt caching aggressively.** System prompts that repeat across calls should use `cache_control`.
3. **Cache locally.** Same input + same model = same output. Don't pay twice.
4. **Log everything.** Every API call should write to ARGUS telemetry. You can't optimize what you don't measure.
5. **Set monthly caps.** Use `BudgetExceededError` pattern to prevent runaway costs.
6. **Review model routing quarterly.** As model pricing changes, routing rules should be updated.
7. **Keep CLAUDE.md lean.** Use progressive disclosure (L1/L2) to avoid wasting context tokens on irrelevant rules.
