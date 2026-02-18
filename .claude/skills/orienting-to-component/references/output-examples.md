# Component Overview — Output Examples

## Single Component Example

```
/component-overview _MYCEL
```

**Output:**
```
MYCEL - RAG Intelligence Library
=================================

📊 Status
Version: 0.2.0
Status: Active (Production-ready shared service)
Role: Shared Service #1 (Critical Dependency)
Last Updated: Feb 9, 2026

📝 Description
Advanced RAG system with multi-LLM support, knowledge synthesis, contradiction
detection, and intelligent routing. All GAIA projects use MYCEL for LLM access.

🚀 Quick Start
1. cd /x/Projects/_GAIA/_MYCEL
2. pip install -e .
3. Set ANTHROPIC_API_KEY in .env
4. python -c "from rag_intelligence import create_llm_client; print('✓ Ready')"

🔧 Key Commands
Setup: pip install -e .
Tests: pytest tests/ --cov=rag_intelligence -v
Docs: cat README_LOGGING.md

📁 Key Files
- rag_intelligence/__init__.py (Public API)
- rag_intelligence/config.py (Configuration)
- rag_intelligence/logging_config.py (Structured logging)
- pyproject.toml (Package metadata)

🔗 Integration Points
Used by: ALL GAIA projects (jSeeker, VIA, HART, etc.)
Depends on: Anthropic SDK, OpenAI SDK (optional)
Provides to: LLM client creation, RAG pipelines, intelligence layers

⚠️  Gotchas
- MUST install as editable: pip install -e .
- Requires ANTHROPIC_API_KEY in .env
- Don't import anthropic directly (use create_llm_client)
- Coverage target: 80% minimum (enforced in CI)

🎯 Current Work
- ✅ Structured logging (v0.2.0)
- ⏳ Knowledge graph visualization
- ⏳ Multi-modal RAG (text + images)

📍 Location
Path: X:/Projects/_GAIA/_MYCEL
CLAUDE.md: X:/Projects/_GAIA/_MYCEL/CLAUDE.md
Tests: 92-100% coverage (gold standard)

🏛️ Constitutional Compliance
✅ Glass-box: All logic inspectable
✅ Cost tracking: All LLM calls logged
✅ No autonomous actions without approval
```

## All Components Summary Example

```
/component-overview --all
```

**Output:**
```
GAIA Ecosystem Overview
=======================

📊 Shared Services (9)

1. MYCEL (v0.2.0) - RAG Intelligence
   Status: ✅ Production | Coverage: 92-100%
   Role: LLM client creation, RAG operations

2. VULCAN (v0.4.0-dev) - The Forge
   Status: 🟡 Development | Coverage: 60%
   Role: Project scaffolding and creation

3. LOOM (v0.1.0) - Workflow Engine
   Status: 🟡 Development | Coverage: TBD
   Role: Visual agent workflow composition

4. MNEMIS (v0.1.0) - Cross-Project Memory
   Status: 🟡 Development | Coverage: TBD
   Role: 3-tier memory hierarchy (GAIA > PROJECT > AGENT)

5. ARGUS (v0.5.1) - The Watchman
   Status: 🟡 Development | Dashboard: ✅ Active
   Role: Monitoring, mental models, explainability

6. WARDEN (v0.3.0) - Governance & Compliance
   Status: ✅ Active | Tests: ✅ Added (v0.3.0)
   Role: Secret scanning, pre-commit validation

7. RAVEN (v0.1.0) - Research Agent
   Status: 📝 Specification | No implementation yet
   Role: Autonomous research investigations

8. AURORA (v0.1.0) - UX/UI Design Lead
   Status: 🟡 Development | Design system scaffolded
   Role: UX specifications, design systems, prototypes

9. ABIS (v0.0.1) - Visual System Builder
   Status: 📝 Planning | No implementation yet
   Role: No-code agent system editor

📦 Products (8)

1. HART OS (v6.2.8) - ✅ Production
2. VIA Intelligence (v6.4) - ✅ Production
3. DATA FORGE (v1.1) - ✅ Production
4. jSeeker (v0.2.1) - 🟡 Active Development
5. GPT_ECHO (v0.1.0) - 🟢 Active (external)
6. Semantic RM (v2.0.8) - ✅ Production
7. Data Cleansing RAG (v0.6) - 🟡 Active
8. THE PALACE (v1.0) - ✅ Complete

📊 Ecosystem Health
Total Components: 17
Production: 4 (24%)
Active/Development: 9 (53%)
Planning/Spec: 2 (12%)
Complete/External: 2 (12%)

🎯 GECO Progress: 10/27 resolved (37%)

🔗 Registry: X:/Projects/_GAIA/registry.json
📖 Bible: X:/Projects/_GAIA/GAIA_BIBLE.md
📋 Audit: X:/Projects/_GAIA/GECO_AUDIT.md
```

## Filtered View Example

```
/component-overview --all --status production
```

Shows only production-ready components.
