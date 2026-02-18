---
name: researching
description: "[CONTEXT] Dispatches Master Raven epistemic research engine for structured investigation with web search, source tiering, triangulation, and executive synthesis. Use when any GAIA task requires external research, competitive analysis, technology scouting, or knowledge gap discovery. Triggers on: research, investigate, find out, scout, competitive analysis, compare. Why: structured research with provenance tracking."
---

# /researching -- Master Raven Research Dispatch

## Quick Usage

```
/researching "What is OpenClaw and how to set it up?"
/researching "Compare RAG frameworks 2026" --depth deep
/researching "Anthropic API changes" --depth quick
```

## Workflow

### 1. Parse & Classify
- Extract research question from user input
- Classify depth: quick_scan (fast, $0.50) / comprehensive (default, $2) / deep_audit (thorough, $5)
- Check MNEMIS cache for existing research

### 2. Scout Pass (Always First)
- Run quick WebSearch from main context
- Collect initial Finding[] with source URLs
- Classify sources: PRIMARY / SECONDARY / TERTIARY
- If sufficient signal at quick depth, synthesize immediately

### 3. Unkindness Deployment (comprehensive/deep only)
- Spawn agent team using `/orchestrating-agents` patterns:
  - **Scout Ravens** (Sonnet, bypassPermissions): WebSearch + WebFetch
  - **Analyst Raven** (Sonnet): Triangulation + hypothesis generation
  - **Red Team Raven** (Sonnet): Adversarial counter-thesis
- Raven Master (Opus or main context): Final synthesis

### 4. MCP Enrichment (Main Context Only)
- **GitHub MCP**: Search repos, read READMEs, check issues
- **Context7 MCP**: Query library documentation
- **Notion MCP**: Store research brief (optional)

### 5. Synthesis & Output
- Apply 4-step LLM chain via MYCEL: triangulate -> hypothesize -> red-team -> synthesize
- Enforce output token budgets (5.6K quick / 11K deep max)
- Generate 9-section Master Raven report
- Save to `_RAVEN/reports/{topic}.md`
- Cache in MNEMIS (PROJECT tier, 7-day TTL)
- Emit ARGUS telemetry events

## Output Format

9-section Master Raven report:
1. Question -- scope boundary
2. Hypotheses -- testable claims
3. Sources -- tiered list
4. Method -- strategy + cost
5. Findings -- ranked with confidence tags
6. Contradictions -- conflicting pairs
7. Confidence -- overall assessment
8. Implications -- recommendations
9. Monitoring Signals -- what to watch

## Autonomous Permissions

All RAVEN agents run with `mode: "bypassPermissions"`:
- Full tool access: Read, Write, Edit, Bash, Glob, Grep, WebSearch, WebFetch
- Git operations: push, pull
- Team coordination: TaskCreate, SendMessage

## Cost Governance

| Depth | Cost Cap | Agents |
|-------|----------|--------|
| quick_scan | $0.50 | 1 Scout + synthesis |
| comprehensive | $2.00 | 2 Scouts + Analyst + Red Team |
| deep_audit | $5.00 | 2 Scouts + Analyst + Red Team + subs |
