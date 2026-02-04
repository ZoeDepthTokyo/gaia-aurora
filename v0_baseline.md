# GAIA Ecosystem - v0 Baseline
## Recorded: February 3, 2026
## Purpose: Pre-consolidation snapshot. Reference point for all future changes.

---

## Production Systems

### HART OS v6.2.8
- **Canonical Location:** X:\Projects\hart_os_v6
- **Other Locations:** C:\Claude\reference_app (divergent copy, archived), C:\hart_os_v6 (empty, deleted)
- **Python:** 3.9+
- **Git:** Yes (active, GitHub)
- **Tests:** 92 tests, 100% pass rate, 53% coverage (target 80%)
- **Streamlit Port:** Not currently assigned
- **LLM Provider:** OpenAI (GPT-4, GPT-4o-mini)
- **Key Dependencies:** streamlit>=1.28.0, openai>=1.0.0, PyMuPDF>=1.23.0, python-docx>=1.1.0, pandas>=1.5.0
- **Known P0 Bugs:**
  1. Logic Panel Display Incomplete
  2. API Key Persistence Broken
  3. Session Search/Load Broken
  4. Crear Participante Button not working
  5. Export DOCX/PDF Broken
- **Architecture:** 8-stage deterministic pipeline, 6-component scoring, modular services
- **Config Approach:** JSON files (api_keys.json) + dataclass config
- **Depends On:** None (standalone, will integrate MYCEL)

### VIA Intelligence v6.4
- **Location:** X:\Projects\VIA
- **Python:** 3.10+
- **Git:** NO (initialized during GAIA Phase 0)
- **Tests:** 4 integration tests
- **Streamlit Port:** 8503 (currently running)
- **LLM Providers:** Google Gemini (extraction), OpenAI + Anthropic (via rag-intelligence)
- **Key Dependencies:** streamlit>=1.52.2, google-generativeai, plotly, pymupdf, openai, anthropic, rag-intelligence
- **Known Issues:** None documented
- **Architecture:** 7 Streamlit pages, multi-stage pipeline (PDF > extract > chunk > insight > pitch)
- **Config Approach:** Hand-rolled .env parser + custom load_env_file()
- **Depends On:** rag-intelligence (via rag_adapter.py)
- **Data:** 46 PDFs, 5,403 semantic claim chunks, 80+ generated insights

### DATA FORGE v1.1
- **Location:** X:\Projects\Python tools\data-forge-v1.1
- **Python:** 3.10+
- **Git:** NO (initialized during GAIA Phase 0)
- **Tests:** Unknown count
- **Streamlit Port:** Not assigned
- **LLM Provider:** OpenAI (tiered model routing)
- **Key Dependencies:** streamlit>=1.28.0, pypdf2>=3.0.0, python-docx>=1.0.0, pydantic>=2.0.0, openai>=1.0.0, networkx>=3.0
- **Known Issues:** None documented
- **Architecture:** 8 Streamlit pages, Module 1 (compiler) + Module 2 (memory bank), hybrid BM25+vector search
- **Config Approach:** pydantic-settings BaseSettings (BEST pattern in ecosystem)
- **Depends On:** rag-intelligence (concept, not direct import)

### MYCEL (ex-rag-intelligence) v0.1.0
- **Location:** X:\Projects\Python tools\rag-intelligence
- **Python:** 3.10+
- **Git:** NO (initialized during GAIA Phase 0)
- **Tests:** 200+ tests, 92-100% coverage per module
- **LLM Providers:** OpenAI, Anthropic
- **Key Dependencies:** openai>=1.0.0, anthropic>=0.18.0, chromadb>=0.4.0, streamlit>=1.28.0, pydantic>=2.0.0, numpy>=1.24.0, pandas>=2.0.0, plotly>=5.0.0
- **Known Issues:** __init__.py has most exports commented out, OpenAIClient.__init__ is `pass` (skeleton)
- **Architecture:** 52 modules, ~15,000 LOC. Core (chunking, embedding, indexing, retrieval) + Intelligence (synthesis, contradiction, trends, gaps) + UI + Evaluation
- **Config Approach:** None standardized (to be created in Phase 0.5)
- **Used By:** VIA Intelligence, HART OS, DATA FORGE

---

## Other Projects

### THE PALACE (Complete)
- **Location:** X:\Projects\The Palace
- **Status:** Complete - interview case study presentation
- **Content:** 33 agents, 29 strategy documents, 49 HTML visualizations, 54 SVG icons
- **Relevance to GAIA:** Kanban/agent orchestration patterns harvested for ARGUS

### ECHO (ex-chatgpt_personal_os) (Stale Prototype)
- **Location:** X:\Projects\Python tools\ChatGTP\chatgpt_personal_os
- **Status:** Functional but stale (last activity Jan 5, 2026)
- **Issues:** Empty requirements.txt, no tests, 19 manual version copies, hardcoded paths
- **LLM:** Google Gemini
- **Relevance to GAIA:** Taxonomy/classification patterns, conversation processing

### ai_knowledge_system (Experimental)
- **Location:** C:\ai_knowledge_system
- **Status:** Prototype, 6 documents, 85 chunks
- **Relevance to GAIA:** To be absorbed into MYCEL

### LOOM (ex-ABIS) (Design Only)
- **Location:** X:\Projects\ABIS\docs
- **Status:** 150+ page PRD (v2.0), zero code
- **Relevance to GAIA:** Vision for visual agent editor, Phase 3

### VULCAN (ex-Claude Bootstrap) (Production Meta-Framework)
- **Location:** C:\Claude
- **Status:** Production-ready (v1.0, 2026-01-26)
- **Content:** 5 agent templates, 4 slash commands, 3 lifecycle hooks, project discovery + validation
- **Relevance to GAIA:** Core of VULCAN project creator, Phase 1

---

## Duplications Map

| Capability | HART OS | VIA | DATA FORGE | MYCEL | ECHO |
|-----------|---------|-----|------------|-------|------|
| LLM Client | llm_gateway.py (OpenAI, PHI filter) | 2 clients (Gemini + OpenAI) | llm_client.py (OpenAI, tiered) | skeleton only | gemini_client.py |
| Embedding | None | Via MYCEL adapter | embedding_client.py | EmbeddingService | None |
| Chunking | Intake chunking | Semantic claims | Configurable overlap | Multi-resolution | Turn-based |
| Config/Env | api_keys.json + dataclass | Hand-rolled .env parser | pydantic-settings | None | .env + hardcoded |
| Progress Tracking | .progress_tracker.txt | Pipeline status | State machine | None | None |
| Streamlit Theme | Custom CSS | Custom CSS | Custom CSS (MD3) | UI components | Custom CSS (MD3) |
| Classification | Symptom matching | Theme classification | Taxonomy + LLM | None | Folder taxonomy + Gemini |

---

## Cross-Project Dependencies

```
VIA ──depends on──> MYCEL (rag-intelligence) via rag_adapter.py
HART OS ──will integrate──> MYCEL (planned)
DATA FORGE ──concept shares──> MYCEL (not direct import yet)
```

---

## Environment Summary

- **Machine:** Windows, single user (Fed)
- **IDE:** VSCode
- **UI Framework:** Streamlit (all projects)
- **Primary LLM:** Claude (Anthropic) + OpenAI + Google Gemini
- **Storage:** JSON files (all projects), ChromaDB (MYCEL only)
- **Drives:** C:\ (system, some projects), X:\ (main project drive)

---

## What This Baseline Enables

After recording this state, any future change can be measured against it:
- Did we reduce LLM client duplication? (from 5 to target: 1 in MYCEL)
- Did we add version control? (from 1/4 to target: 4/4)
- Did we resolve location conflicts? (from 3 HART locations to 1)
- Did we achieve cross-project observability? (from 0 to ARGUS dashboard)
- Did we standardize config? (from 3 approaches to 1 pydantic-settings pattern)
