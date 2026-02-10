# Model Effort Optimization Guide

## Overview
Choose the right Claude model for each task to balance quality, speed, and cost. GAIA uses a three-tier approach optimized for Constitutional AI governance workflows.

## Model Selection Matrix

### 🏃 Haiku 4.5 — Fast & Cheap
**Use for: High-volume, low-complexity tasks**

**When to use:**
- Routine code formatting (Ruff hooks)
- Simple grep/file searches
- Registry validation checks
- Quick CLAUDE.md lookups
- Component status checks
- Log parsing and filtering
- Simple text transformations
- Template rendering

**Cost:** ~$0.001 per 1K tokens
**Speed:** ~50-100 tokens/sec
**Context:** 200K tokens

**Examples:**
```python
# In MYCEL llm.py:
llm = create_llm_client(model="haiku")  # For simple tasks
```

**Skills that should use Haiku:**
- `/component-overview` — Quick orientation
- `/registry-sync --validate-only` — Fast validation
- Simple `/explain-code` queries

---

### ⚖️ Sonnet 4.5 — Balanced (Default)
**Use for: Most development work**

**When to use:**
- Code generation and editing
- GECO audits (moderate complexity)
- UX analysis (7-pass framework)
- Design reviews
- Accessibility checks
- Documentation writing
- Test generation
- Submodule sync planning
- Multi-file refactoring

**Cost:** ~$0.003 per 1K tokens (3x Haiku)
**Speed:** ~30-60 tokens/sec
**Context:** 200K tokens

**Examples:**
```python
# Default in MYCEL:
llm = create_llm_client()  # Defaults to Sonnet
```

**Skills that should use Sonnet:**
- `/ux-audit` — 7-pass analysis
- `/design-review` — Design system compliance
- `/accessibility-check` — WCAG audits
- `/geco-status` — Full GECO reports
- `/explain-code --level detailed`

---

### 🧠 Opus 4.6 — Highest Quality
**Use for: Complex, critical decisions**

**When to use:**
- Architectural decisions
- Constitutional principle validation
- Complex multi-repo refactoring
- Critical security reviews
- ABIS node editor logic (complex UX)
- Cross-component integration design
- GAIA Bible updates
- Complex pattern learning

**Cost:** ~$0.015 per 1K tokens (15x Haiku, 5x Sonnet)
**Speed:** ~20-40 tokens/sec
**Context:** 200K tokens

**When to explicitly request:**
```
# In your prompt:
"Use Opus model for this architectural decision"

# Or in MYCEL:
llm = create_llm_client(model="opus")
```

**Skills that might need Opus:**
- `/explain-code --level expert` (complex systems)
- Constitutional audits (GAIA principles)
- AURORA design decisions (novel UX patterns)
- ABIS-specific work (most complex component)

---

## Cost Optimization Strategies

### 1. Progressive Escalation
Start with Haiku, escalate to Sonnet if needed:

```python
# Try fast first
result = haiku_llm.generate(prompt)
if not result.is_satisfactory:
    result = sonnet_llm.generate(prompt)
```

### 2. Batch Similar Tasks
Group similar operations to amortize prompt caching:

```bash
# Bad: 10 separate calls
/component-overview _ARGUS
/component-overview _AURORA
# ... (10x overhead)

# Good: One batch query
"Give me overviews of all GAIA components"
```

### 3. Use Prompt Caching
Claude caches prompts automatically. Reuse similar context:

```python
# First call: Full cost
llm.generate(f"{SYSTEM_PROMPT}\n{task1}")

# Second call: Cached system prompt (90% discount)
llm.generate(f"{SYSTEM_PROMPT}\n{task2}")
```

### 4. Lazy Evaluation
Only invoke LLMs when necessary:

```python
# Bad: Always generate
description = llm.generate(f"Describe {component}")

# Good: Use existing CLAUDE.md
description = read_claude_md(component)
```

---

## Task-Specific Recommendations

### GECO Audits
- **Status check**: Haiku (`/geco-status --component _ARGUS`)
- **Full audit**: Sonnet (`geco-auditor` subagent)
- **Constitutional review**: Opus (manual prompt)

### Code Explanation
- **Simple function**: Haiku (`/explain-code utils.py:calculate`)
- **Complex module**: Sonnet (`/explain-code jseeker/adapter.py`)
- **System architecture**: Opus (`/explain-code --level expert`)

### UX/UI Work
- **Quick accessibility check**: Haiku (contrast validation)
- **Full WCAG audit**: Sonnet (`/accessibility-check`)
- **Novel interaction design**: Opus (AURORA agent)

### Registry Management
- **Validation**: Haiku (`/registry-sync --validate-only`)
- **Sync with fixes**: Sonnet (`/registry-sync --fix`)
- **Schema evolution**: Opus (manual design)

### Git Operations
- **Submodule status**: Haiku (`git submodule status`)
- **Merge planning**: Sonnet (`submodule-sync` agent)
- **Complex conflict resolution**: Opus (manual prompt)

---

## Usage Patterns by Component

### jSeeker (Resume Engine)
- **Resume adaptation**: Sonnet (quality matters for job apps)
- **JD parsing**: Haiku (structured extraction)
- **Template rendering**: Haiku (simple HTML generation)
- **Outreach generation**: Sonnet (persuasive writing)

### ARGUS (Monitoring)
- **Dashboard queries**: Haiku (read-only data viz)
- **Mental model selection**: Sonnet (analysis required)
- **Trace analysis**: Sonnet (pattern detection)

### AURORA (UX/UI)
- **Inspiration search**: Haiku (catalog lookup)
- **UX spec generation**: Sonnet (7-pass framework)
- **Novel pattern design**: Opus (creative thinking)

### VULCAN (Creation)
- **Project scaffolding**: Haiku (template expansion)
- **HITL questionnaire**: Sonnet (interactive wizard)
- **Architecture decisions**: Opus (critical choices)

### MYCEL (LLM Client)
- **Model routing**: Haiku (cheap dispatcher)
- **Prompt engineering**: Sonnet (default quality)
- **Benchmark optimization**: Opus (performance critical)

### LOOM (Modification)
- **Simple edits**: Haiku (search/replace)
- **Refactoring**: Sonnet (code understanding)
- **Contract enforcement**: Sonnet (validation logic)

### WARDEN (Security)
- **Secret scanning**: Haiku (regex patterns)
- **Vulnerability analysis**: Sonnet (code review)
- **Threat modeling**: Opus (security critical)

---

## Cost Tracking

### Per-Component Monthly Budget (Estimated)

| Component | Haiku | Sonnet | Opus | Total/Month |
|-----------|-------|--------|------|-------------|
| jSeeker   | $2    | $15    | $5   | $22         |
| ARGUS     | $1    | $8     | $2   | $11         |
| AURORA    | $1    | $10    | $8   | $19         |
| VULCAN    | $1    | $6     | $3   | $10         |
| MYCEL     | $0.50 | $3     | $1   | $4.50       |
| LOOM      | $1    | $5     | $2   | $8          |
| WARDEN    | $2    | $4     | $1   | $7          |
| **Total** | $8.50 | $51    | $22  | **$81.50**  |

*Assumes 10 hours/week active development across ecosystem*

### Cost Alerts
Set up MYCEL tracking:
```python
# In config.py:
COST_ALERT_THRESHOLD = 100  # USD per month
COST_ALERT_EMAIL = "your-email@example.com"
```

---

## Performance Tips

### 1. Streaming for Long Tasks
```python
# Better UX for long generation
for chunk in llm.stream(prompt):
    print(chunk, end="", flush=True)
```

### 2. Parallel Requests
Use Haiku for parallel cheap tasks:
```python
from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor() as executor:
    results = executor.map(haiku_llm.generate, tasks)
```

### 3. Early Termination
Stop generation when you have enough:
```python
result = llm.generate(prompt, max_tokens=500)  # Cap output
```

---

## Quick Decision Tree

```
Is this a critical decision affecting architecture?
├─ YES → Opus
└─ NO → Is this complex code generation/analysis?
    ├─ YES → Sonnet
    └─ NO → Is this a simple lookup/validation?
        ├─ YES → Haiku
        └─ NO → Default to Sonnet (safe choice)
```

---

## Model Override in Skills

Skills can specify model preference in frontmatter:

```yaml
---
name: my-skill
preferred-model: sonnet  # haiku | sonnet | opus
fallback-model: haiku    # If preferred unavailable
---
```

---

## Monitoring Usage

### View Current Month Costs
```python
from jseeker.llm import JseekerLLM
llm = JseekerLLM()
print(llm.get_monthly_costs())
```

### ARGUS Dashboard Integration
ARGUS tracks LLM usage across all components:
- Model distribution (Haiku/Sonnet/Opus %)
- Cost per component
- Token usage trends
- Latency metrics

Access at: `http://localhost:8501` → "LLM Analytics" tab

---

## Best Practices

1. **Default to Sonnet**: If unsure, Sonnet is safe
2. **Haiku for volume**: Batch operations, validations
3. **Opus for stakes**: Architecture, security, critical UX
4. **Cache aggressively**: Reuse system prompts
5. **Monitor costs**: Check ARGUS dashboard weekly
6. **Progressive escalation**: Try cheap first, escalate if needed
7. **Batch similar tasks**: Reduce API overhead

---

## Integration with GAIA Principles

### Glass-box Transparency
Log which model was used and why:
```python
logger.info(f"Using {model} for {task}: {reason}")
```

### Human-in-Loop
Use Opus for decisions requiring user approval:
```python
if requires_approval:
    result = opus_llm.generate(prompt)  # Highest quality
```

### Progressive Trust
Escalate model as trust increases:
```python
model = "haiku" if confidence > 0.9 else "sonnet"
```

### Sovereignty
User can override model choice in UI:
```python
model = st.selectbox("Model", ["haiku", "sonnet", "opus"])
```

---

## Examples from Real GAIA Work

### GECO v1.1 Audit (Feb 8, 2026)
- **Status checks**: Haiku (10 components × $0.001 = $0.01)
- **Audit reports**: Sonnet (10 components × $0.05 = $0.50)
- **Priority ranking**: Sonnet ($0.10)
- **Total**: $0.61 for full ecosystem audit

### jSeeker v0.2.1 Rename (Feb 9, 2026)
- **File renames**: Haiku (bulk operations, $0.05)
- **Test fixes**: Sonnet (logic understanding, $0.30)
- **Architecture review**: Sonnet ($0.15)
- **Total**: $0.50 for 68-file refactor

### AURORA Phase A+B (Feb 9, 2026)
- **Template expansion**: Haiku ($0.02)
- **Content generation**: Sonnet (22 files, $1.20)
- **Design decisions**: Opus (2 critical choices, $0.40)
- **Total**: $1.62 for complete UX system foundation

---

## Future Optimization (Phase 3+)

### MNEMIS Pattern Learning
Cache common operations in MNEMIS:
```python
# First time: Full LLM call
result = llm.generate(prompt)
mnemis.store(prompt, result, tier="PROJECT")

# Next time: Instant retrieval
result = mnemis.recall(prompt)  # $0.00 cost
```

### ARGUS Cost Prediction
Train model to predict costs before execution:
```python
estimated_cost = argus.predict_cost(task)
if estimated_cost > budget:
    downgrade_to_haiku()
```

### Auto-routing in MYCEL
MYCEL learns optimal model for each task:
```python
# MYCEL analyzes historical performance
optimal_model = mycel.route(task_type, complexity, budget)
```

---

## Quick Reference Card

| Task Type | Model | Typical Cost | When to Use |
|-----------|-------|--------------|-------------|
| Simple validation | Haiku | $0.001 | Always safe |
| Code generation | Sonnet | $0.05 | Default choice |
| Architecture | Opus | $0.30 | Critical only |
| Bulk operations | Haiku | $0.01/10 | High volume |
| UX analysis | Sonnet | $0.10 | 7-pass framework |
| Novel patterns | Opus | $0.50 | Creative work |
| Security audits | Sonnet | $0.08 | Standard review |
| Threat modeling | Opus | $0.40 | High stakes |

---

**Last Updated**: Feb 9, 2026
**Version**: 1.0
**Maintained by**: GAIA Core Team
