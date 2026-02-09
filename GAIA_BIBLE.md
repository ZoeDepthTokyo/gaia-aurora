# THE GAIA BIBLE
## Constitutional Document for the GAIA Ecosystem

**Status:** Phase 2 & 3 Complete ✅ | GAIA v0.5.1 | Last Updated: February 9, 2026

---

## Table of Contents

### TIER 1: FOUNDATION
- **[Chapter 0](#chapter-0-gaia-status--coordination)** - GAIA Status & Coordination
- **[Chapter 1](#chapter-1-the-gaia-vision--problem--solution)** - The GAIA Vision - Problem & Solution
- **[Chapter 2](#chapter-2-gaia-architecture--design-principles)** - GAIA Architecture & Design Principles

### TIER 2: OPERATIONAL
- Chapter 3 - Using VULCAN - Project Creation Guide
- Chapter 4 - VULCAN Adapter Architecture & Development
- Chapter 5 - VULCAN API Reference & Interfaces
- Chapter 6 - VULCAN Integration Patterns & Workflows

### TIER 3: REFERENCE
- Appendix A - GAIA Registry Schema & Format
- Appendix B - GAIA History & Evolution
- Appendix C - Phase Completion Reports
- Appendix D - Coordination & Cross-Project Records

---

---

# CHAPTER 0: GAIA Status & Coordination

## Executive Summary

**GAIA is the master layer** that sits above all AI projects in a local ecosystem. It solves fragmentation, lack of governance, and the complexity of managing multiple AI tools with different APIs and architectures.

**Current Status:** v0.5.1 (Phases 1, 2 & 3 Complete + GECO v1.1.0)
- All production projects under git version control
- VULCAN (The Forge) operational and tested
- ARGUS (Mental Model Library + Subconscious Layer + Dashboard) implemented
- LOOM (Workflow Engine) + MNEMIS (Memory Hierarchy) operational
- WARDEN (Governance & Compliance) active with scanner and pre-commit hooks
- AURORA (UX/UI Design Lead) design system scaffolded
- 59 mental models with context-aware selection
- Layered explainability (4 levels mapped to Growth Rungs)
- Memory contracts and promotion protocol enforced
- Registry operational with 17 registered projects

**Phase Progress:**
- ✅ v0.0.0 - Pre-GAIA fragmented state
- ✅ v0.1.0 - GAIA Genesis (naming, structure, PRD)
- ✅ v0.2.0 - Stabilization (git, version control)
- ✅ v0.3.0 - MYCEL spine (config, LLM clients)
- ✅ v0.3.1 - MYCEL Chunk.source critical fix
- ✅ v0.4.0 - VULCAN creator operational
- ✅ v0.4.3 - ARGUS (Mental Models + Subconscious) + LOOM/MNEMIS complete
- ✅ v0.5.0 - Phase 2 complete (59 models, layered explainability)
- ✅ v0.5.1 - GECO v1.1.0 (ARGUS dashboard fixes, 17-project registry, WARDEN/RAVEN/ABIS/DOS/AURORA defined)
- ✅ v1.0.0 - Phase 3 complete (memory hierarchy, workflow engine)

---

## GAIA Naming Registry (Locked)

| Name | Role | Status | Origin |
|------|------|--------|--------|
| **GAIA** | Ecosystem master layer | v0.4.0 | Greek primordial earth deity |
| **VULCAN** | Project Creator | v0.4.0 ✅ | Roman god of the forge |
| **LOOM** | Visual Agent Editor | v1.0.0 ✅ | Mythic weaver of fate |
| **ARGUS** | Monitoring & Telemetry | v0.5.0 ✅ | Greek 100-eyed watchman |
| **MYCEL** | Shared Intelligence Library | v0.3.1 ✅ | Mycelium -- nature's neural network |
| **MNEMIS** | Cross-Project Memory | v1.0.0 ✅ | Mnemosyne, titan of memory |
| **WARDEN** | Governance & Enforcement | v0.3.0 ✅ | Forest guardian |
| **RAVEN** | Research Agent | v0.1.0 (defined) | Odin's knowledge-gathering ravens |
| **GPT_ECHO** | ChatGPT Archaeology (Product) | v0.1.0 (stale) | Echoes past conversations |
| **ABIS** | No-Code Agent System Builder | v0.0.1 (planning) | Agentic Builder & Integration System |
| **AURORA** | UX/UI Lead | v0.1.0 (development) | Aurora, goddess of dawn |

**Existing Projects (Keep Names):** HART OS, VIA, DATA FORGE, THE PALACE, Waymo Data, DOS, jSeeker, GPT_ECHO

---

## The Three Pillars Framework

### Core User Flow

```
VULCAN                 LOOM                    ARGUS
(The Forge)            (The Workbench)         (The Watchman)

"What do you           "Rewire agent 3's       "Show me everything
want to build?"        memory schema"          everywhere"
     |                      |                        |
     v                      v                        v
Questionnaire ──> Project ──> Visual Node ──> Dashboards
User intent        scaffold    Editor           Kanbans
Context gather     aligned     NL editing       Agent traces
Constraints        to GAIA     Glass-box        Cost tracking
Decision gates     structure   Self-healing     Cross-project
     |                             |                 |
     v                             v                 v
  CREATES               MODIFIES            MONITORS
  projects              projects            projects
```

### The Three Pillars Explained

**VULCAN - The Forge (Operational)**
- **Purpose:** Project creation is the only way new projects enter the ecosystem
- **Enforces:** GAIA meta-structure at birth (not retrofit)
- **Method:** 7-step HITL questionnaire + intelligent adapters
- **Output:** GAIA-compliant project scaffold with tests, docs, and LLM integration
- **Status:** v0.4.0 operational (19,830 lines, 137 tests, 85% coverage)

**LOOM - The Workbench (Operational)**
- **Purpose:** Projects get modified and evolved after creation
- **Enforces:** Glass-box transparency in modifications
- **Method:** Workflow engine with agent authority and execution tracking
- **Output:** Modified agents, memory schemas, integration contracts
- **Status:** v1.0.0 operational (workflow engine, agent authority, execution state management)

**ARGUS - The Watchman (Operational)**
- **Purpose:** Mental model library and subconscious pattern detection
- **Enforces:** Context-aware reasoning, layered explainability
- **Method:** 59 mental models, 4-level explanation hierarchy, external memory
- **Output:** Growth rung-aligned explanations, pattern detection, model selection
- **Status:** v0.5.0 operational (mental models, subconscious layer, explainability system)

**Shared Layer (8 Services: MYCEL, MNEMIS, WARDEN, RAVEN, ARGUS, LOOM, VULCAN, ABIS)**
- **MYCEL:** Unified LLM clients (OpenAI, Anthropic, Gemini), configuration, chunking, retrieval
- **MNEMIS:** Cross-project memory with promotion discipline (v1.0.0 - 5-tier hierarchy, contracts enforced)
- **WARDEN:** Governance, compliance enforcement, git/test/secrets validation
- **RAVEN:** Research agent for ad-hoc investigations (deferred)
- **ARGUS:** Monitoring, mental models (59), subconscious layer, pattern detection
- **LOOM:** Workflow engine, agent authority, execution state management
- **VULCAN:** Project creator, The Forge, scaffolding with GAIA compliance
- **ABIS:** Visual system builder, no-code agent editor (planned)

### WARDEN — Governance & Enforcement (Planned)
- **Purpose:** Constitutional compliance enforcement
- **Enforcement Model:** Hard blocks (secrets in code, missing .gitignore) + Soft warnings (missing tests, stale docs)
- **Integration Points:** Pre-commit hooks, VULCAN scaffold validation, LOOM edit gates, CI/CD checks
- **Hard Blocks:** API keys in code, missing .gitignore, broken imports
- **Soft Warnings:** Low test coverage, outdated dependencies, missing documentation
- **Status:** v0.0.0 — scanner.py exists but not integrated into any workflow

### ABIS — Visual System Builder (Planning)
- **Purpose:** No-code agent system builder with visual node editor
- **Distinction from LOOM:** LOOM edits individual agents/workflows; ABIS builds entire multi-agent systems visually
- **Tech Stack (planned):** React + React Flow (visual canvas) + Python FastAPI (graph compilation)
- **Key Feature:** System Graph Spec v1 — canonical schema for user-designed agent systems
- **Status:** v0.0.1 — PRD exists at `X:\Projects\ABIS\docs\ABIS-PRD_v2.0.md`

---

## GECO Hierarchy (Authoritative)

```
GAIA (Ecosystem Governance)
├── Shared Services (8)
│   ├── ARGUS      (Monitoring, Mental Models, Subconscious)
│   ├── LOOM       (Workflow Engine, Agent Editor)
│   ├── MNEMIS     (Memory Hierarchy, Cross-Project Learning)
│   ├── MYCEL      (LLM Clients, Config, RAG Intelligence)
│   ├── RAVEN      (Research Agent — planned)
│   ├── VULCAN     (Project Creator, The Forge)
│   ├── WARDEN     (Governance, Compliance)
│   └── ABIS       (Visual System Builder, No-Code Agent Editor)
│
├── Products (8)
│   ├── HART OS    (Therapy Assistant, v6.2.8)
│   ├── VIA        (Investment Research, v6.4)
│   ├── DATA FORGE (Data Processing, v1.1)
│   ├── The Palace (Case Study, v1.0)
│   ├── Waymo Data (Reference Dataset)
│   ├── DOS        (Multi-Agent Decision System)
│   ├── jSeeker    (Job Seeking & Resume Adaptation, formerly PROTEUS)
│   └── GPT_ECHO   (ChatGPT Archaeology & Search, v0.1.0 stale)
│
└── Python Tools (Standalone utilities)
```

**Key distinction:** Shared services live under `X:\Projects\_GAIA\_*`. Products live at `X:\Projects\*` (root level). jSeeker will be moved from `_GAIA/_PROTEUS/` to `X:\Projects\jSeeker/` during cleanup.

---

## Operational Metrics (Current State)

| Metric | Current | Target | Gap |
|--------|---------|--------|-----|
| CLAUDE.md Coverage | 4/13 modules (31%) | 100% | 69% |
| Git Remotes | 1/15 projects | 100% | 93% |
| WARDEN Enforcement | 0% | Hard blocks active | 100% |
| LLM Cost Visibility | jSeeker only | All products | 85% |
| ARGUS Telemetry | 1/9 services | All services | 89% |
| CI/CD Pipelines | 0 | Core services | 100% |
| Pre-commit Hooks | 0 | All modules | 100% |

---

## Version Roadmap

### Completed Versions

**v0.0.0 - Pre-GAIA State (Feb 3, 2026)**
- 7+ Python AI projects running in isolation
- No shared infrastructure, no version control on 3/4 production systems
- 5 duplicate LLM client implementations
- No observability, enforcement, or cross-project memory

**v0.1.0 - GAIA Genesis (Feb 3-4, 2026)**
- Ecosystem naming locked (8 GAIA components + 4 existing projects)
- Architecture principle: thin spine, then products
- Three-pillar user flow: VULCAN creates > LOOM edits > ARGUS monitors
- PRD created incorporating GAIA architecture

**v0.2.0 - Stabilization (Feb 4, 2026)**
- All production projects under git version control
- HART OS location resolved (single canonical instance)
- v0 baseline recorded for all existing projects
- Secrets safety verified across ecosystem

**v0.3.0 - MYCEL Spine (Feb 4, 2026)**
- Configuration standardized using pydantic-settings
- Unified LLM client supporting OpenAI, Anthropic, Gemini
- MYCEL public API stabilized and documented
- GAIA registry operational for project discovery

**v0.3.1 - MYCEL Chunk.source Fix (Feb 4, 2026)**
- Critical fix to MYCEL Chunk model
- Added `source` and `timestamp` properties
- Unblocked VIA project from proceeding with integrations

**v0.4.0 - VULCAN Operational (Feb 4, 2026)**
- VULCAN - The Forge fully operational
- 7-step HITL questionnaire implemented
- Three project type adapters (Deterministic, Creative, Processor)
- Streamlit UI with main page + 3 functional pages
- Retroactive project registration (Registry-Only, GAIA-Lite modes)
- 19,830 lines of production code
- 137 tests, 85% coverage
- 31,000+ lines of documentation
- Git initialized and ecosystem registered

**v0.4.3 - ARGUS Mental Models + LOOM/MNEMIS Foundation (Feb 4, 2026)**
- 66 files committed across ARGUS and LOOM/MNEMIS
- ~6,770 lines of implementation code
- ~9,170 lines of documentation
- Phase 2 and Phase 3 architectures complete
- Foundation for v0.5.0 and v1.0.0 releases

**v0.5.0 - ARGUS Operational (Phase 2 Complete - Feb 4, 2026)**
- Mental Model Library with 59 models across 6 categories
- Context-aware model selection with scoring algorithm
- GAIA Subconscious Layer (external memory, pattern detection)
- Layered Explainability System (4 levels: Simple, Detailed, Technical, Debug)
- Growth Rung mapping (Rungs 1-4 to explanation complexity)
- Model categories: Cognitive, Behavioral, Systems, Decision-Making, Communication, Business
- Pattern detection and persistence across sessions
- Integration hooks for HART OS therapeutic framework

**v1.0.0 - Full Ecosystem (Phase 3 Complete - Feb 4, 2026)**
- LOOM workflow engine operational
- MNEMIS memory hierarchy with 5 tiers (Ephemeral → Working → Session → Long-term → Permanent)
- Memory contracts enforced at runtime (cannot write above tier)
- Memory promotion protocol with criteria validation
- Agent authority system with hierarchical execution
- Workflow state management and execution tracking
- Cross-project memory sharing with promotion discipline
- Glass-box explainability integrated into workflow execution
- End-to-end workflow: create in VULCAN > edit in LOOM > monitor in ARGUS

### Planned Versions

**v1.1.0 - GECO Consolidation (February 2026)**
- Add ABIS to shared services (visual system builder)
- Add DOS to products (multi-agent decision system)
- Rename PROTEUS → jSeeker, reclassify as product
- Master cleanup: consolidate folder structure
- Deploy pre-commit hooks ecosystem-wide
- Push core services to GitHub
- WARDEN Phase 1: pre-commit enforcement

---

## Current Ecosystem State

### Registered Projects (10 Total)

| Project | Version | Status | Git | Location | Providers | Tags |
|---------|---------|--------|-----|----------|-----------|------|
| HART OS | 6.2.8 | Production | ✅ | X:\Projects\hart_os | OpenAI | therapy, deterministic, medical |
| VIA | 6.4 | Production | ✅ | X:\Projects\via | Gemini, OpenAI, Anthropic | investment, rag, synthesis |
| DATA FORGE | 1.1 | Production | ✅ | X:\Projects\data_forge | OpenAI | data-processing, compiler, ETL |
| MYCEL | 0.3.1 | Active | ✅ | X:\Projects\Python tools\rag-intelligence | OpenAI, Anthropic, Gemini | intelligence, shared-lib, rag |
| **VULCAN** | **0.4.0** | **Development** | **✅** | **X:\Projects\vulcan** | - | **gaia-core, project-creator** |
| **LOOM** | **1.0.0** | **Operational** | **✅** | **X:\Projects\ABIS** | - | **workflow-engine, agent-authority** |
| **ARGUS** | **0.5.0** | **Operational** | **✅** | **X:\Projects\ABIS** | - | **mental-models, subconscious, explainability** |
| ECHO | 0.1.0 | Stale | ❌ | X:\Projects\Python tools\ChatGTP | Gemini | chat-archaeology |
| THE PALACE | 1.0 | Complete | ❌ | X:\Projects\The Palace | - | case-study, visualization |
| ai_knowledge_system | N/A | Experimental | ❌ | C:\ai_knowledge_system | - | archive-candidate |

---

## Ecosystem Directory Structure

```
X:\Projects\
├── _gaia/                        # GAIA ecosystem meta-layer
│   ├── GAIA_BIBLE.md            # This document
│   ├── VERSION_LOG.md           # Version history
│   ├── PHASE_1_HANDOFF.md       # Phase 1 completion report
│   ├── PHASE_1_COMPLETE.md      # Phase 1 detailed summary
│   ├── PHASE_2_COMPLETE.md      # Phase 2 completion (ARGUS)
│   ├── PHASE_3_COMPLETE.md      # Phase 3 completion (LOOM/MNEMIS)
│   ├── v0_baseline.md           # Pre-consolidation snapshot
│   ├── registry.json            # All projects with metadata
│   ├── warden/                  # Governance scripts
│   │   └── enforce.py          # (TBD)
│   └── logs/                    # Structured telemetry (JSONL)
│       ├── hart_os/
│       ├── via/
│       └── data_forge/
│
├── vulcan/                      # PHASE 1: Project creator
│   ├── vulcan_forge/            # Core package
│   │   ├── project_creator.py   # Main orchestrator
│   │   ├── questionnaire.py     # HITL intake forms
│   │   ├── registry_manager.py  # Registry CRUD
│   │   ├── project_validator.py # Compliance checker
│   │   ├── adapters/            # Three project types
│   │   │   ├── base_adapter.py
│   │   │   ├── deterministic_adapter.py
│   │   │   ├── creative_adapter.py
│   │   │   └── processor_adapter.py
│   │   └── templates/           # GAIA project scaffolds
│   ├── ui/                      # Streamlit interface
│   │   ├── main.py             # Landing page
│   │   └── pages/              # 3 functional pages
│   ├── tests/                   # 137 tests, 85% coverage
│   └── docs/                    # 31,000+ lines of documentation
│
├── ABIS/                        # PHASE 2 & 3: ARGUS + LOOM + MNEMIS + Visual Builder
│   ├── argus/                   # Mental Model Library & Subconscious
│   │   ├── mental_models/       # 59 models across 6 categories
│   │   ├── subconscious/        # External memory & pattern detection
│   │   └── explainability/      # 4-level explanation system
│   ├── loom/                    # Workflow Engine
│   │   ├── workflow/            # Agent authority & execution
│   │   └── state/               # State management
│   ├── mnemis/                  # Memory Hierarchy
│   │   ├── memory_manager.py    # 5-tier promotion protocol
│   │   └── contracts/           # Runtime enforcement
│   └── docs/                    # ABIS PRD (visual system builder planning)
│
├── hart_os/                     # Production therapy assistant
├── via/                         # Production investment research
├── data_forge/                  # Production data processing
├── jSeeker/                     # Product: Job seeking & resume adaptation (formerly PROTEUS)
├── dos/                         # Product: Multi-agent decision system
├── waymo_data/                  # Product: Reference dataset
├── echo/                        # Stale chat archaeology
└── the_palace/                  # Complete case study
```

---

## Key Contracts & Guarantees

### VULCAN Guarantees

Every project created by VULCAN has:
- ✅ `logs/` directory for JSONL telemetry (Phase 2 ready)
- ✅ `CLAUDE.md` with structured context
- ✅ Standard GAIA structure (config.py, main package, tests/, docs/)
- ✅ Registry entry in `X:\Projects\_gaia\registry.json`
- ✅ MYCEL integration (GaiaSettings, create_llm_client)
- ✅ `.gitignore` with hardened secrets protection
- ✅ `requirements.txt` including rag-intelligence>=0.3.1
- ✅ Three adapters available (Deterministic, Creative, Processor)

### ARGUS Guarantees (Phase 2 Complete)

ARGUS Mental Model Library provides:
- ✅ 59 mental models across 6 categories (Cognitive, Behavioral, Systems, Decision-Making, Communication, Business)
- ✅ Context-aware model selection with scoring algorithm
- ✅ Layered explainability (4 levels: Simple, Detailed, Technical, Debug)
- ✅ Growth Rung mapping (Rungs 1-4 to explanation complexity)
- ✅ GAIA Subconscious with external memory and pattern detection
- ✅ Model metadata (category, complexity, prerequisites, use_cases)
- ✅ Integration hooks for HART OS therapeutic framework

ARGUS can rely on:
- `X:\Projects\_gaia\registry.json` - All registered projects
- `X:\Projects\{project}\logs\*.jsonl` - Telemetry data
- `X:\Projects\{project}\CLAUDE.md` - Project context
- `X:\Projects\{project}\config.py` - Configuration (GaiaSettings subclass)

### LOOM/MNEMIS Guarantees (Phase 3 Complete)

LOOM Workflow Engine provides:
- ✅ Agent authority system with hierarchical execution
- ✅ Workflow state management and execution tracking
- ✅ Integration with ARGUS mental models for reasoning
- ✅ Integration with MNEMIS memory hierarchy

MNEMIS Memory System provides:
- ✅ 5-tier memory hierarchy (Ephemeral → Working → Session → Long-term → Permanent)
- ✅ Memory contracts enforced at runtime (cannot write above tier)
- ✅ Memory promotion protocol with criteria validation
- ✅ Cross-project memory sharing with promotion discipline
- ✅ Thread-safe access and expiration handling
- ✅ JSONL persistence for long-term and permanent memories

### WARDEN Enforcement (Planned)

WARDEN validates:
1. Git status (uncommitted changes?)
2. Test suite (passing?)
3. .env safety (no hardcoded keys)
4. Dependency freshness
5. Documentation completeness

---

## Critical Ongoing Issues

### HART OS OpenAI Key Exposure

**Status:** ⚠️ REQUIRES USER ACTION

- **Location:** Git history of X:\Projects\hart_os
- **Key:** `sk-proj-kNkhu_LsFv...` (partial)
- **Action:** User MUST manually revoke this key at OpenAI dashboard
- **Timeline:** Before using HART OS for sensitive data
- **Mitigation:** All subsequent commits have .gitignore properly configured

**This is a known limitation of git history retention. Regular rotation recommended quarterly.**

---

## Phase 2: ARGUS Mental Models & Subconscious (v0.5.0)

### Overview

ARGUS transforms from a planned monitoring system into an operational **Mental Model Library** and **Subconscious Layer** that provides context-aware reasoning and layered explainability.

**Implementation Stats:**
- 59 mental models across 6 categories
- 4-level layered explainability system
- Growth Rung mapping (Rungs 1-4)
- External memory and pattern detection
- ~3,200 lines of implementation
- ~4,500 lines of documentation

### Mental Model Library

**Categories and Models:**

1. **Cognitive Models (12 models)**
   - Mental Accounting, Anchoring Bias, Availability Heuristic
   - Confirmation Bias, Dunning-Kruger Effect, Sunk Cost Fallacy
   - Loss Aversion, Recency Bias, Hindsight Bias
   - Framing Effect, Cognitive Load Theory, Working Memory Model

2. **Behavioral Models (10 models)**
   - Operant Conditioning, Classical Conditioning, Social Learning Theory
   - Habit Loop, Implementation Intentions, Temporal Discounting
   - Goal Setting Theory, Self-Efficacy Theory, Reactance Theory
   - Nudge Theory

3. **Systems Thinking Models (11 models)**
   - Feedback Loops, Stock and Flow, System Archetypes
   - Leverage Points, Causal Loop Diagrams, Tragedy of the Commons
   - Limits to Growth, Network Effects, Emergent Properties
   - Homeostasis, System Boundaries

4. **Decision-Making Models (10 models)**
   - Expected Utility Theory, Prospect Theory, Decision Trees
   - Cost-Benefit Analysis, Multi-Criteria Decision Analysis, Six Thinking Hats
   - Eisenhower Matrix, SWOT Analysis, Decision Matrix
   - Pareto Principle

5. **Communication Models (8 models)**
   - Shannon-Weaver Model, Transactional Model, Nonviolent Communication
   - Active Listening, Johari Window, DISC Model
   - Crucial Conversations, Feedback Models

6. **Business/Strategy Models (8 models)**
   - Porter's Five Forces, Value Chain Analysis, Business Model Canvas
   - PESTEL Analysis, Core Competencies, Blue Ocean Strategy
   - Ansoff Matrix, BCG Growth-Share Matrix

**Model Structure:**
```python
@dataclass
class MentalModel:
    name: str
    category: str
    description: str
    application: str
    complexity: int  # 1-4 (maps to Growth Rungs)
    prerequisites: List[str]
    related_models: List[str]
    use_cases: List[str]
    explanation_template: str
```

### Context-Aware Model Selection

**Selection Algorithm:**
```python
def select_models(
    context: Dict[str, Any],
    max_models: int = 5
) -> List[Tuple[MentalModel, float]]:
    """
    Score models based on:
    - Context relevance (keywords match)
    - User Growth Rung compatibility
    - Model prerequisites met
    - Complexity appropriateness
    """
```

**Scoring Factors:**
- Keyword matching in context
- Growth Rung alignment (user cognitive level)
- Prerequisite model knowledge
- Complexity appropriateness for task
- Domain relevance

### Layered Explainability System

**Four Explanation Levels:**

1. **Simple (Rung 1-2):**
   - Plain language, analogies
   - No technical jargon
   - Concrete examples
   - "Explain like I'm 5"

2. **Detailed (Rung 2-3):**
   - Conceptual understanding
   - Some terminology introduced
   - Step-by-step reasoning
   - Real-world applications

3. **Technical (Rung 3-4):**
   - Full technical detail
   - Implementation specifics
   - Cross-model connections
   - Edge cases and limitations

4. **Debug (Rung 4):**
   - Complete decision trace
   - Model scoring details
   - Context analysis breakdown
   - Selection algorithm internals

**Growth Rung Mapping:**
```python
EXPLANATION_LEVEL_MAP = {
    1: "simple",      # Basic comprehension
    2: "detailed",    # Conceptual understanding
    3: "technical",   # Expert knowledge
    4: "debug"        # System-level understanding
}
```

### GAIA Subconscious Layer

**Purpose:** External memory and pattern detection across sessions

**Components:**

1. **External Memory:**
   - Persistent storage of patterns
   - Cross-session learning
   - User preference tracking
   - Model effectiveness history

2. **Pattern Detection:**
   - Recurring context patterns
   - User decision tendencies
   - Model selection patterns
   - Success/failure tracking

3. **Learning Protocol:**
   - Track model usage frequency
   - Record user feedback
   - Adjust scoring weights
   - Refine selection algorithm

**Storage Format (JSONL):**
```json
{
  "timestamp": "2026-02-04T12:00:00Z",
  "pattern_type": "model_selection",
  "context_hash": "abc123...",
  "models_selected": ["anchoring_bias", "confirmation_bias"],
  "user_growth_rung": 3,
  "effectiveness_score": 0.85
}
```

### HART OS Integration

**Therapeutic Framework Alignment:**

- Mental models inform therapeutic interventions
- Growth Rungs determine explanation complexity
- Subconscious tracks patient progress patterns
- Layered explanations adapt to patient comprehension level

**Integration Points:**
- `hart_os.therapy.intervention_selector` → ARGUS model selection
- `hart_os.growth_tracker` → ARGUS Growth Rung mapping
- `hart_os.explanation_engine` → ARGUS layered explainability

---

## Phase 3: LOOM Workflow Engine + MNEMIS Memory (v1.0.0)

### Overview

LOOM and MNEMIS implement the workflow execution and memory management layers, completing the GAIA ecosystem's core architecture.

**Implementation Stats:**
- 5-tier memory hierarchy with promotion protocol
- Agent authority and workflow execution system
- Memory contracts enforced at runtime
- ~3,570 lines of implementation
- ~4,670 lines of documentation

### MNEMIS Memory Hierarchy

**Five Memory Tiers:**

1. **Ephemeral Memory (Tier 0)**
   - Lifespan: Single function call
   - Use: Temporary calculations, intermediate results
   - Promotion: Never (discarded after use)
   - Example: Loop variables, temp formatting

2. **Working Memory (Tier 1)**
   - Lifespan: Single task execution
   - Use: Active context, current reasoning
   - Promotion: To Session if task-relevant pattern emerges
   - Example: Current user query, active document chunk

3. **Session Memory (Tier 2)**
   - Lifespan: Single conversation/workflow run
   - Use: Multi-turn context, accumulated decisions
   - Promotion: To Long-term if pattern repeated across sessions
   - Example: User preferences in current session, accumulated context

4. **Long-term Memory (Tier 3)**
   - Lifespan: Persistent across sessions (30-90 days)
   - Use: Learned patterns, user preferences, project knowledge
   - Promotion: To Permanent if foundational or repeatedly accessed
   - Example: User communication style, project constraints

5. **Permanent Memory (Tier 4)**
   - Lifespan: Indefinite (project lifetime)
   - Use: Core facts, architectural decisions, constitutional rules
   - Promotion: Never (highest tier)
   - Example: System architecture, core principles, critical constraints

### Memory Contracts

**Runtime Enforcement:**

```python
class MemoryContract:
    """
    Enforces memory tier access rules:
    - Agents can READ from any tier <= their authority
    - Agents can WRITE only to tiers <= their authority
    - Agents can PROMOTE memory up one tier (with validation)
    """

    def validate_write(
        agent_authority: int,
        target_tier: int,
        memory_content: Dict[str, Any]
    ) -> bool:
        """Raise exception if agent tries to write above authority"""
        if target_tier > agent_authority:
            raise MemoryContractViolation(
                f"Agent authority {agent_authority} cannot write to tier {target_tier}"
            )
```

**Contract Rules:**
- Agents cannot write above their authority tier
- Memory promotion requires criteria validation
- Cross-tier reads allowed (read down hierarchy)
- Automatic expiration for time-bound tiers

### Memory Promotion Protocol

**Promotion Criteria:**

```python
@dataclass
class PromotionCriteria:
    access_count: int = 3        # Times accessed
    time_span: timedelta = None   # Across how long?
    pattern_strength: float = 0.7 # How consistent?
    user_confirmation: bool = False # Explicit user validation
    importance_score: float = 0.6  # Calculated importance
```

**Promotion Process:**

1. **Detection:** System detects promotion candidate
2. **Validation:** Check promotion criteria met
3. **Review:** Optional user confirmation (high-tier promotions)
4. **Execute:** Copy to higher tier with metadata
5. **Audit:** Log promotion for transparency

**Example:**
```python
# Working → Session promotion
if memory_access_count >= 3 and task_relevance > 0.7:
    promote_memory(
        content=working_memory["user_preference"],
        from_tier=1,
        to_tier=2,
        reason="Repeated pattern across multiple tasks"
    )
```

### LOOM Workflow Engine

**Agent Authority System:**

Agents have authority levels (0-4) that match memory tiers:

```python
@dataclass
class Agent:
    name: str
    authority_level: int  # 0-4
    capabilities: List[str]
    memory_access: MemoryAccess
```

**Authority Levels:**
- **Level 0:** Ephemeral agents (single-use functions)
- **Level 1:** Task agents (single workflow task)
- **Level 2:** Session agents (manage conversation)
- **Level 3:** Project agents (cross-session coordination)
- **Level 4:** System agents (architectural changes)

**Workflow Execution:**

```python
class WorkflowEngine:
    def execute_workflow(
        workflow: Workflow,
        context: Dict[str, Any]
    ) -> WorkflowResult:
        """
        Execute workflow with:
        - Agent authority validation
        - Memory contract enforcement
        - State tracking
        - Explainability integration
        """
```

**Execution Features:**
- Hierarchical agent coordination
- State management across steps
- Integration with ARGUS mental models
- Memory tier-aware execution
- Automatic state persistence

### Cross-Project Memory Sharing

**Sharing Protocol:**

1. **Package for Export:**
   - Sanitize project-specific details
   - Tag with domain/category
   - Assign sharing permission level

2. **Validation:**
   - Check recipient project compatibility
   - Verify memory tier appropriateness
   - Validate promotion criteria

3. **Import:**
   - Map to recipient project memory tiers
   - Adjust authority requirements
   - Log cross-project transfer

**Example Use Case:**
- VIA learns investment analysis pattern (Long-term memory)
- Pattern promoted to Permanent as "fundamental analysis framework"
- HART OS imports pattern for "financial stress analysis" in therapy
- Both projects benefit from shared knowledge

### Glass-Box Explainability Integration

**Workflow Transparency:**

Every workflow execution produces:
- Step-by-step agent decisions
- Memory access/write log
- Mental model selection reasoning
- Tier-appropriate explanations

**Explanation Levels in Workflows:**
- **Simple:** "The system remembered your preference"
- **Detailed:** "Session memory promoted to long-term based on 3+ uses"
- **Technical:** "Memory promotion: Working → Session (criteria: access_count=5, relevance=0.82)"
- **Debug:** Full promotion algorithm trace with scoring breakdown

---

## Implementation Summary

### Code Statistics

**Phase 2 (ARGUS):**
- Implementation: ~3,200 lines
- Documentation: ~4,500 lines
- Total: ~7,700 lines

**Phase 3 (LOOM/MNEMIS):**
- Implementation: ~3,570 lines
- Documentation: ~4,670 lines
- Total: ~8,240 lines

**Combined:**
- 66 files committed
- ~6,770 lines implementation
- ~9,170 lines documentation
- ~15,940 total lines

### Constitutional Compliance

All implementations maintain GAIA constitutional principles:

✅ **Thin Spine, Then Products** - ARGUS/LOOM build on MYCEL foundation
✅ **Glass-Box Transparency** - Layered explainability at all levels
✅ **Memory Contracts** - Runtime enforcement prevents silent violations
✅ **Growth Rung Alignment** - Explanations adapt to user comprehension
✅ **Cross-Project Learning** - MNEMIS enables ecosystem-wide knowledge sharing
✅ **Hierarchical Governance** - Agent authority prevents unauthorized memory writes

### Next Steps

With Phases 2 and 3 complete, the GAIA ecosystem now has:

1. **Create** - VULCAN project creator (Phase 1)
2. **Monitor** - ARGUS mental models + subconscious (Phase 2)
3. **Execute** - LOOM workflow engine (Phase 3)
4. **Remember** - MNEMIS memory hierarchy (Phase 3)

**Future Enhancements:**
- WARDEN governance automation
- Telemetry dashboard (original ARGUS vision)
- RAVEN research agent
- Visual workflow editor UI

---

---

# CHAPTER 1: The GAIA Vision - Problem & Solution

## The Core Problem

### Before GAIA (State: Feb 3, 2026)

**Fragmentation across 7+ isolated projects:**
- 7 Python AI projects running in complete isolation
- No shared infrastructure or governance
- 5 duplicate LLM client implementations across projects
- 3 different .env loading approaches
- 4 different chunking implementations
- 3 conflicting HART OS installations

**Technical Debt:**
- 3 of 7 projects had no version control
- Zero cross-project telemetry or observability
- No unified configuration system
- Dependencies managed inconsistently
- No standardized project creation process

**User Pain:**
- Creating a new project = Copy-paste from existing projects
- Modifying projects = Hope nothing breaks
- Running projects = Can't see costs or errors ecosystem-wide
- Understanding workflows = Opaque to user, hidden inside AI
- Growing capability = Stuck learning from copy-paste

**Why This Happened:**
AI tools are powerful but opaque. They can generate thousands of lines of code instantly, but:
- You don't understand what was built
- You can't modify it confidently
- You don't learn from the process
- You become dependent on the AI forever

---

## The GAIA Solution

### Core Vision Statement

**GAIA is a system that sits between a creative human and AI-powered coding tools.**

Its core purpose is to turn **vague, fast, creative intent** into a **structured, inspectable, and governable product development process**, without forcing the user to think like an engineer on day one.

### Four Core Principles

#### 1. Glass-Box Transparency

GAIA never hides mistakes. If something is unknown, it says so.

- **Never:** Hide errors, make silent assumptions, produce black boxes
- **Always:** Admit uncertainty, show reasoning, explain trade-offs
- **Degrade gracefully:** If something breaks, system explains why and adapts

*Example:* When VULCAN creates a project, every choice is visible:
- "I chose Deterministic adapter because you need confidence scoring"
- "I used OpenAI as primary because Gemini didn't fit your constraints"
- "I'm unsure about this design choice - let's explore alternatives together"

#### 2. Pedagogical AI

Over time, GAIA learns how the user prefers to work. Not by guessing. By observing explicit choices and confirmations.

- **Never:** Infer intent, automate without consent, hide learning process
- **Always:** Ask for confirmation, show what was learned, let user correct
- **Progressive:** Reveal information at user's current capability level

*Example:* After 10 projects, GAIA might say:
- "I noticed you always choose Deterministic for therapy projects. Should I suggest that next time?"
- User confirms → GAIA remembers and pre-fills
- Or user says "No, that was coincidental" → GAIA doesn't assume

#### 3. Progressive Capability

The user gradually becomes more technical, more structured, and more confident, without ever needing to adopt black box AI behavior.

- **Day 1:** Simple questionnaire, click button, get project
- **Day 30:** User understands project types, recognizes patterns
- **Day 90:** User customizes adapters, modifies configurations
- **Day 180:** User documents workflows, teaches others
- **Day 365:** User designs new GAIA components, contributes back

*The ladder never disappears - it's always there when you need to go higher.*

#### 4. Bridge, Not Replacement

GAIA is the bridge between human creativity and structured engineering product execution.

- **GAIA is NOT:** A product that "builds software for you"
- **GAIA IS:** A system that teaches you how to build software with AI safely while actually doing the work

*You learn by doing. You grow in capability. You become the architect.*

---

## The Human Journey: Fed's Persona Progression

### Day 1: Creative Chaos

**State of Mind:** "I have 7 AI projects scattered everywhere, they're a mess, I need help"

**Capability:**
- Knows Python, has ideas, overwhelmed by complexity
- Can't manage multiple projects, can't see costs, can't enforce consistency

**GAIA Role:** Stabilize what exists first
- Git initialize all projects
- Create single source of truth (registry)
- Document baseline state

**Outcome:** Breathing room. "Now I know what exists and where"

**Key Moment:** First time running `git status` on all projects and seeing they're all tracked

---

### Day 30: Structured Exploration

**State of Mind:** "I want to create a new project. These questions VULCAN asks actually make sense"

**Capability:**
- Recognizes project types (Deterministic vs Creative vs Processor)
- Understands why questionnaire matters
- Can evaluate trade-offs between adapters

**GAIA Role:** Show options, let user choose
- VULCAN presents 7-step questionnaire
- For each decision: explain alternatives
- Confirm choice before proceeding

**Outcome:** New projects follow patterns, no duplication

**Key Moment:** "Oh, I see. A deterministic project needs pipelines and scoring. That's why HART looks different from VIA."

---

### Day 90: Confident Iteration

**State of Mind:** "I need to modify this adapter to add a custom stage. I understand the interface now"

**Capability:**
- Reads adapter code
- Understands BaseAdapter interface
- Can extend existing patterns

**GAIA Role:** Show pattern, guide extension
- "Here's how adapters work"
- "Here's where custom stages attach"
- "Here's the test template for your stage"

**Outcome:** Custom adapters, user-defined structures, no dependency on AI

**Key Moment:** User successfully extends DeterministicAdapter without asking for help

---

### Day 180: Teaching Others

**State of Mind:** "I want to document my workflow so my team can follow it"

**Capability:**
- Writes PRDs
- Creates guides
- Explains GAIA architecture to others
- Helps team members create projects

**GAIA Role:** Enable knowledge transfer
- "Export your patterns as templates"
- "Here's how to teach others the questionnaire"
- "Document your adapter extensions"

**Outcome:** Team adopts GAIA, user becomes architect

**Key Moment:** First team member creates a project using VULCAN without asking questions

---

### Day 365: Confident Architect

**State of Mind:** "I'm designing Phase 3 (LOOM) and know exactly how it integrates with everything"

**Capability:**
- Designs new GAIA components
- Understands thin-spine architecture
- Contributes back to ecosystem
- Mentors others on system design

**GAIA Role:** Partnership
- "You've outgrown this. You're the architect now."
- "Let's design Phase 4 together"
- "Your learnings should become our next component"

**Outcome:** Fed builds GAIA extensions, contributes back to ecosystem

**Key Moment:** Proposing and implementing a new component that benefits entire ecosystem

---

## Before/After Transformation: Same Task

### Task: "Create a customer sentiment analyzer"

#### Before GAIA (Day 0)

**Approach:** Copy-paste from ChatGPT, hope it works

```python
# Single fragile script
import openai

def analyze_sentiment(text):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": f"Sentiment: {text}"}]
    )
    return response['choices'][0]['message']['content']

if __name__ == "__main__":
    result = analyze_sentiment("I love this product!")
    print(result)
```

**Structure:** Single file, no tests, hardcoded keys in script

**Understanding:** "It works but I don't know why"

**Outcome:**
- ❌ Fragile (breaks if OpenAI API changes)
- ❌ Hard to modify (where's the logic?)
- ❌ Impossible to hand off (no documentation)
- ❌ Opaque (why does this work?)
- ❌ Unmaintainable (technical debt from day 1)

---

#### After GAIA (Day 365)

**Approach:** "This is a Deterministic project with 5 stages and confidence scoring"

**Structure:** GAIA-compliant project created by VULCAN

```
sentiment_analyzer/
├── config.py                    # GaiaSettings subclass
├── launch_sentiment_analyzer.py # Streamlit launcher
├── sentiment_analyzer/
│   ├── core/
│   │   ├── stages/
│   │   │   ├── 1_extract_phrases.py
│   │   │   ├── 2_classify_sentiment.py
│   │   │   ├── 3_calculate_confidence.py
│   │   │   ├── 4_apply_threshold.py
│   │   │   └── 5_format_output.py
│   │   └── scoring/
│   │       ├── confidence_engine.py
│   │       └── threshold_rules.py
│   ├── llm/
│   │   └── client.py            # Uses MYCEL
│   └── utils/
├── tests/
│   ├── test_stages.py           # Unit tests
│   └── test_integration.py      # End-to-end tests
├── docs/
│   ├── ARCHITECTURE.md
│   └── STAGE_GUIDE.md
├── logs/                        # ARGUS telemetry
├── .env.example                 # API key template
├── .gitignore                   # Secrets protection
└── requirements.txt             # rag-intelligence>=0.3.1
```

**Code Quality:** Tested (Stage 3 isolated, can test confidence scoring separately)

```python
# Stage 2: Classify sentiment
from mycel.integrations import create_llm_client
from .stage_base import StageBase

class ClassifySentimentStage(StageBase):
    def execute(self, input_data):
        client = create_llm_client(provider="openai")

        prompt = f"""Classify the sentiment:
        {input_data['phrases']}

        Return JSON with sentiment and reasoning."""

        result = client.complete_json(
            system="You are a sentiment classifier",
            user=prompt
        )
        return {"sentiment": result['sentiment'], "reasoning": result['reasoning']}
```

**Understanding:** "Stage 2 classifies sentiment using OpenAI, threshold is 0.75, confidence > 0.75 passes to Stage 4"

**Outcome:**
- ✅ Robust (testable stages, clear interfaces)
- ✅ Modifiable (add stage 6? Change threshold? Easy)
- ✅ Team-ready (documented, structured, hand-off ready)
- ✅ Inspectable (see exactly what each stage does)
- ✅ Learnable (understand why this structure exists)

---

## The Transformation Cycle

```
VAGUE INTENT                      STRUCTURED THINKING              CONFIDENT EXECUTION
  (Day 1)                         (Day 30-180)                       (Day 365)

User: "I want an app that        GAIA: "Let's explore what that    User: "This is a Deterministic
 does sentiment analysis"         means - show me 3 approaches"      project with 5 stages and
                                                                      confidence scoring"

                                  User learns: "Approach 2 works     GAIA: "Great - I'll create
                                  best because I can see the         that structure. You'll be able
                                  stages"                             to modify it later"

AI DEPENDENCY                     AI PARTNERSHIP                    AI AUGMENTATION
  (Black Box)                     (Glass Box)                       (White Box + Extension)

"Do this"                    →   "Show me options"            →    "I'll extend this"
Trust the AI                      Understand the process             Build new capabilities
Can't modify                      Can modify with help               Can design from scratch
Dependent forever                 Growing independence               Independent architect
```

---

## Why This Matters

### The Core Problem GAIA Solves

AI coding tools are powerful but opaque. They can generate thousands of lines of code instantly, but you don't understand what was built, can't modify it confidently, don't learn from the process, and become dependent on the AI forever.

**GAIA flips this:**

1. **Every line is generated with explanation**
   - Why this architecture? Why this pattern? Why this choice?
   - User understands the "why" behind the "what"

2. **Every structure is inspectable**
   - Open the code. Read it. Understand it.
   - Nothing is hidden. Nothing is magic.

3. **Every decision is yours to make**
   - GAIA suggests, user confirms
   - User grows in confidence and capability
   - Not "follow the AI blindly" but "collaborate with the AI"

4. **You become more capable over time**
   - Day 30: You understand project types
   - Day 90: You modify adapters
   - Day 180: You teach others
   - Day 365: You design new components

### The Promise

**GAIA is not a shortcut.**
**GAIA is a ladder.**

You climb it one rung at a time, and eventually, you don't need the ladder anymore.

But the ladder never disappears. It's always there when you need to go higher.

---

## GAIA's Self-Learning Mechanism

### What GAIA Observes (Not Guesses)

GAIA learns through explicit observation:
- User always chooses Deterministic for therapy projects
- User prefers confidence thresholds of 0.75
- User creates projects in X:\Projects\ (not C:\)
- User runs tests before committing
- User archives failed experiments

### What GAIA Learns

From these observations:
- Pre-fill Deterministic for therapy domain next time
- Default threshold to 0.75 for this user
- Suggest X:\Projects\ as default path
- Add pre-commit test hooks automatically
- Add archive workflow to templates

### What GAIA Does NOT Do

- Guess user intent
- Hide decisions
- Auto-apply changes without confirmation
- Assume understanding without validation

### The Learning Contract

**GAIA:** "I noticed you always use Deterministic for therapy projects. Should I suggest that next time?"

**User:** "Yes" → GAIA remembers and pre-fills next time
**OR**
**User:** "No, that was coincidental" → GAIA doesn't assume pattern

**Explicit consent. Observable learning. User control.**

---

## The GAIA Ladder: Growing Complexity

### Rung 1: Creator (Passive)
- Use VULCAN questionnaire
- Click button to create project
- Project works, tests pass
- "It works!"

### Rung 2: Explorer (Curious)
- Read CLAUDE.md to understand structure
- Read adapter code to see patterns
- Modify config.py to change defaults
- "I understand why this is structured this way"

### Rung 3: Adapter (Capable)
- Extend BaseAdapter for custom project type
- Add custom stages to DeterministicAdapter
- Modify templates for your domain
- "I can build my own specialized version"

### Rung 4: Architect (Confident)
- Design new GAIA components (Phase 2, 3)
- Define new adapter types
- Contribute to ecosystem standards
- "I'm designing systems, not just using them"

### Rung 5: Mentor (Teaching)
- Help others climb the ladder
- Document patterns and workflows
- Create new templates and examples
- "I'm teaching others to be architects"

**Each rung builds on previous. Each rung adds capability. No rung disappears.**

---

## The Trust Contract: Five Constitutional Principles

**Central Question:** How do we create, monitor, and enforce trust between user and GAIA?

### Principle 1: GAIA Never Lies

**Definition:** GAIA always tells the truth about what it knows, doesn't know, and is uncertain about.

**How Created:**
- Encoded in every agent prompt: "If uncertain, say so explicitly"
- System messages cannot hide errors
- Logs are immutable and human-readable

**How Monitored:**
- ARGUS tracks instances of "I don't know" responses
- Process Observer flags patterns of hidden uncertainty
- Telemetry includes confidence scores on every decision

**How Enforced:**
- Agents that hide uncertainty fail validation
- Systems that collapse silently trigger automatic escalation
- User can always audit decision trail

**Example:**
```
❌ Bad: "I created your project successfully" (when partially failed)
✅ Good: "I created 4/5 components. Stage 3 failed because dependency X
         is unavailable. Should I proceed with 4, or investigate X first?"
```

---

### Principle 2: GAIA Admits Limits

**Definition:** GAIA explicitly declares what it cannot do, will not do, or should not do.

**How Created:**
- Constitutional boundaries in GAIA Bible
- Read-only Process Observers (cannot execute)
- Memory contracts (cannot write above tier)
- Authority graph defines scope boundaries

**How Monitored:**
- WARDEN checks for authority violations
- Process Observer detects scope creep
- Registry tracks which projects GAIA created vs. registered-only

**How Enforced:**
- Authority graph prevents unauthorized actions
- Memory contracts enforced at runtime (Phase 3)
- Escalation to human when limits reached

**Example:**
```
❌ Bad: "I'll fix this by modifying project X" (outside scope)
✅ Good: "This requires modifying project X, which is outside my authority.
         Escalating to Project Agent for approval."
```

---

### Principle 3: GAIA Degrades Gracefully

**Definition:** When GAIA fails, it fails visibly, predictably, and reversibly.

**How Created:**
- No silent failures allowed
- Every error produces structured log
- Rollback mechanisms for all state changes
- Fallback providers for LLM calls

**How Monitored:**
- ARGUS tracks failure modes
- Process Observer identifies graceful vs. catastrophic degradation
- Post-mortems produced automatically

**How Enforced:**
- Telemetry hooks on every state mutation
- Git provides rollback for code changes
- Registry provides rollback for ecosystem changes
- MYCEL LLM clients have fallback chains

**Example:**
```
❌ Bad: System hangs silently when API fails
✅ Good: "OpenAI API unavailable. Falling back to Anthropic.
         User will see 'degraded mode' banner."
```

---

### Principle 4: GAIA Learns Explicitly

**Definition:** GAIA only learns from explicit user confirmations, never from inference.

**How Created:**
- Memory promotion requires approval (Phase 3)
- Pattern detection produces hypotheses, not facts
- Learning proposals shown to user before acceptance
- Provenance tracked for all learned patterns

**How Monitored:**
- ARGUS tracks learning proposals (accepted/rejected)
- Process Observer flags patterns user never confirmed
- Memory provenance shows what was learned when
- Rejected proposals logged (not discarded)

**How Enforced:**
- Memory contracts prevent silent updates (Phase 3)
- Promotion queue requires human ratification
- No automatic behavioral changes
- Audit trail for all learning

**Example:**
```
❌ Bad: "You always use OpenAI, so I'm setting it as default" (inference)
✅ Good: "I noticed you chose OpenAI in 8/10 projects. Should I pre-fill
         it as default? [Yes/No/Not Yet]"
```

---

### Principle 5: GAIA Remains Inspectable

**Definition:** Every decision GAIA makes can be traced, audited, and explained.

**How Created:**
- CLAUDE.md at project level explains structure
- Provenance tracking in memory (Phase 3)
- Structured telemetry (JSONL)
- Decision rationale logged with every choice

**How Monitored:**
- ARGUS provides execution traces
- Process Observer analyzes decision quality
- User can query "Why did you choose X?"
- Trust Dashboard shows transparency metrics

**How Enforced:**
- All decisions logged with rationale
- Black-box components prohibited in GAIA core
- Third-party integrations must expose reasoning
- Unexplained code fails pre-commit hooks

**Example:**
```
User: "Why did VULCAN choose Deterministic adapter?"
GAIA: "You specified 'confidence scoring required' in Step 4.
       Deterministic adapter is the only one with scoring stages.
       See: questionnaire_response.json line 42"
```

---

## Trust Monitoring in ARGUS (Phase 2)

**Trust Dashboard Metrics:**
- **Transparency Score:** Percentage of decisions with explicit reasoning
- **Graceful Degradation Score:** Ratio of graceful failures vs. crashes
- **Learning Explicitness Score:** Confirmed learning vs. inferred patterns
- **Inspectability Score:** Execution traces with complete provenance

**ARGUS UI Extension:**
```
┌─────────────────────────────────────────────┐
│  TRUST DASHBOARD - HART OS                  │
├─────────────────────────────────────────────┤
│                                              │
│  Overall Trust Score: 87%                   │
│                                              │
│  ✅ Transparency:        92%                │
│  ✅ Graceful Degradation: 95%               │
│  ⚠️  Learning Explicitness: 78%             │
│  ✅ Inspectability:      91%                │
│                                              │
│  [View Unconfirmed Patterns]                │
│  [Audit Decision Trail]                     │
│  [Export Trust Report]                      │
│                                              │
└─────────────────────────────────────────────┘
```

---

---

# CHAPTER 2: GAIA Architecture & Design Principles

## Architectural Principle: Thin Spine, Then Products

### The Core Concept

Infrastructure leads by **one step**, not one phase. Each product pulls in what it needs, thickening the spine.

```
Phase 0: STABILIZE (safety net)
    |
Phase 0.5: SPINE (minimum shared layer)
    |        ├─> MYCEL (config, LLM clients)
    |        ├─> Registry (project discovery)
    |        └─> Git (version control)
    |
Phase 1: VULCAN (project creator)
    |        ├─> Pulls: config, LLM client, templates
    |        └─> Adds: questionnaire, adapters, scaffolding
    |
Phase 2: ARGUS (monitoring)
    |        ├─> Pulls: telemetry hooks, registry
    |        └─> Adds: dashboards, cost tracking, error feeds
    |
Phase 3: LOOM (visual editor)
             ├─> Pulls: everything
             └─> Adds: visual UI, glass-box, MNEMIS
```

**Key Principle:** The spine never gets ahead of products. Products need the infrastructure, not the other way around.

If ARGUS needs something from MYCEL, we add it to MYCEL. We don't build ARGUS and hope MYCEL has what we need.

---

## Layer 1: The Spine (MYCEL)

### What Lives Here

**MYCEL** - The Shared Intelligence Library

**Purpose:** One place to manage:
- API keys (OpenAI, Anthropic, Gemini)
- Configuration (models, defaults, user preferences)
- LLM clients (unified interface across providers)
- Core algorithms (chunking, embedding, retrieval)
- Telemetry hooks (ready for ARGUS)

### MYCEL Core Components

#### Configuration (pydantic-settings)

```python
# mycel/config.py
from pydantic_settings import BaseSettings
from typing import Optional

class GaiaSettings(BaseSettings):
    # LLM API Keys
    openai_api_key: Optional[str] = None
    anthropic_api_key: Optional[str] = None
    gemini_api_key: Optional[str] = None

    # Default Models
    openai_model: str = "gpt-4o"
    anthropic_model: str = "claude-opus-4-5-20251101"
    gemini_model: str = "gemini-2.0-flash"

    # User Preferences
    default_provider: str = "openai"
    default_temperature: float = 0.7

    class Config:
        env_file = ".env"
        case_sensitive = False
```

**Every GAIA project inherits from GaiaSettings:**

```python
# my_project/config.py
from mycel.config import GaiaSettings

class MyProjectSettings(GaiaSettings):
    # Inherits all LLM config
    # Add project-specific settings
    custom_threshold: float = 0.75
```

#### LLM Clients (Unified Interface)

```python
# mycel/integrations/llm_factory.py
from mycel.integrations import create_llm_client

# Works the same regardless of provider
client = create_llm_client(provider="openai")
response = client.complete(
    system="You are a helpful assistant",
    user="What is sentiment analysis?"
)

# Switch providers - same interface
client = create_llm_client(provider="anthropic")
response = client.complete(
    system="You are a helpful assistant",
    user="What is sentiment analysis?"
)
```

**Implementations:**
- `openai_client.py` - OpenAI API wrapper
- `anthropic_client.py` - Anthropic API wrapper
- `gemini_client.py` - Google Gemini wrapper
- All implement `BaseClient` interface

#### Core Algorithms

**Chunking:** Break documents into retrieval-sized pieces
```python
from mycel.core.chunking import RecursiveCharacterChunker

chunker = RecursiveCharacterChunker(chunk_size=1000, overlap=100)
chunks = chunker.chunk(document)
```

**Embedding:** Convert text to vectors
```python
from mycel.core.embedding import OpenAIEmbedder

embedder = OpenAIEmbedder(model="text-embedding-3-small")
vector = embedder.embed("customer sentiment analysis")
```

**Retrieval:** Find relevant chunks
```python
from mycel.core.retrieval import VectorRetriever

retriever = VectorRetriever(embeddings, index)
relevant = retriever.retrieve(query, k=5)
```

#### Telemetry Hooks (Phase 2)

```python
# mycel/telemetry/logger.py (created in Phase 2)
from mycel.telemetry import log_llm_call

log_llm_call(
    provider="openai",
    model="gpt-4o",
    tokens_in=100,
    tokens_out=200,
    latency=1.2,
    cached=False
)
```

**Output:** JSONL to `X:\Projects\_gaia\logs\{project}\{date}.jsonl`

---

## Layer 2: Registry & Project Discovery

### The GAIA Registry

**Location:** `X:\Projects\_gaia\registry.json`

**Purpose:** Single source of truth for all ecosystem projects

**Format:**
```json
{
  "metadata": {
    "version": "1.0",
    "last_updated": "2026-02-04T20:00:00Z",
    "ecosystem": "GAIA v0.4.0"
  },
  "projects": {
    "hart_os": {
      "path": "X:/Projects/hart_os",
      "version": "6.2.8",
      "status": "production",
      "git": true,
      "providers": ["openai"],
      "tags": ["therapy", "deterministic", "medical"],
      "created": "2024-01-15",
      "last_updated": "2026-02-04",
      "type": "deterministic"
    },
    "via": {
      "path": "X:/Projects/via",
      "version": "6.4",
      "status": "production",
      "git": true,
      "providers": ["gemini", "openai", "anthropic"],
      "tags": ["investment", "rag", "synthesis"],
      "created": "2024-06-20",
      "last_updated": "2026-02-04",
      "type": "creative"
    },
    "vulcan": {
      "path": "X:/Projects/vulcan",
      "version": "0.4.0",
      "status": "development",
      "git": true,
      "providers": [],
      "tags": ["gaia-core", "project-creator"],
      "created": "2026-02-04",
      "last_updated": "2026-02-04",
      "type": "utility"
    }
  }
}
```

**Registry Manager** provides CRUD operations:

```python
# vulcan_forge/registry_manager.py
from pathlib import Path
import json

class RegistryManager:
    def __init__(self, registry_path):
        self.registry_path = Path(registry_path)

    def register_project(self, project_name, project_data):
        """Add or update project in registry"""
        registry = self.load()
        registry['projects'][project_name] = project_data
        self.save(registry)

    def get_project(self, project_name):
        """Get project metadata"""
        registry = self.load()
        return registry['projects'].get(project_name)

    def list_projects(self):
        """List all projects"""
        registry = self.load()
        return list(registry['projects'].keys())

    def load(self):
        """Load registry from disk"""
        with open(self.registry_path) as f:
            return json.load(f)

    def save(self, registry):
        """Save registry to disk"""
        with open(self.registry_path, 'w') as f:
            json.dump(registry, f, indent=2)
```

---

## Layer 3: Project Structure (GAIA Template)

### The Standard GAIA Project

Every project created by VULCAN follows this structure:

```
{project_name}/
├── config.py                    # GaiaSettings subclass
├── launch_{project_name}.py    # Streamlit entry point
├── .env.example                # API key template
├── .gitignore                  # Secrets protection
│
├── {project_name}/             # Main package
│   ├── __init__.py
│   ├── core/                   # Business logic (adapter-specific)
│   │   ├── __init__.py
│   │   └── [adapter adds specific subdirs]
│   ├── ui/                     # Streamlit pages
│   │   ├── __init__.py
│   │   └── components.py       # Shared UI components
│   ├── llm/                    # MYCEL integration
│   │   ├── __init__.py
│   │   └── client.py           # Uses create_llm_client(provider="openai")
│   └── utils/                  # Shared utilities
│       ├── __init__.py
│       ├── logging.py          # Structured logging (ARGUS-ready)
│       └── helpers.py
│
├── pages/                      # Streamlit pages (adapter-specific)
│   ├── 1_adapter_page.py
│   └── 2_adapter_page.py
│
├── data/                       # Project data (local)
├── logs/                       # ARGUS telemetry (JSONL)
├── tests/                      # Test suite (pytest)
│   ├── test_core.py
│   └── test_integration.py
├── docs/                       # Documentation
│   ├── ARCHITECTURE.md
│   ├── README.md
│   └── [adapter-specific docs]
│
├── CLAUDE.md                   # Claude Code context anchor
├── .clproj/                    # Claude Code template
├── pyproject.toml              # Python project config
├── requirements.txt            # Dependencies
└── README.md                   # Quick start guide
```

### Critical Files

#### 1. config.py (MYCEL Integration)

```python
from mycel.config import GaiaSettings

class SentimentAnalyzerSettings(GaiaSettings):
    """Configuration for sentiment analyzer project"""

    # Inherit all LLM API keys and defaults from GaiaSettings

    # Project-specific settings
    confidence_threshold: float = 0.75
    batch_size: int = 100
    output_format: str = "json"
```

#### 2. launch_{project}.py (Streamlit Entrypoint)

```python
import streamlit as st
from config import SentimentAnalyzerSettings

st.set_page_config(page_title="Sentiment Analyzer", layout="wide")

settings = SentimentAnalyzerSettings()

st.title("Customer Sentiment Analyzer")
st.write("Analyze customer feedback with confidence scoring")

# App code here
```

#### 3. {project}/llm/client.py (MYCEL Integration)

```python
from mycel.integrations import create_llm_client
from config import SentimentAnalyzerSettings

class LLMClient:
    def __init__(self):
        settings = SentimentAnalyzerSettings()
        self.client = create_llm_client(
            provider=settings.default_provider,
            api_key=settings.openai_api_key
        )

    def analyze_sentiment(self, text):
        response = self.client.complete_json(
            system="You are a sentiment analysis expert",
            user=f"Analyze: {text}"
        )
        return response
```

#### 4. CLAUDE.md (Context Anchor)

```markdown
# Sentiment Analyzer - Claude Code Context

## Project Identity
- **Type:** Deterministic (high confidence, strict rules)
- **Created:** 2026-02-04
- **Purpose:** Analyze customer sentiment with confidence scoring

## Architecture
- **Pipeline:** 5-stage deterministic pipeline
- **Stage 1:** Extract phrases
- **Stage 2:** Classify sentiment
- **Stage 3:** Calculate confidence
- **Stage 4:** Apply threshold
- **Stage 5:** Format output

## LLM Integration
- **Provider:** OpenAI (primary)
- **Model:** gpt-4o
- **Temperature:** 0.3 (low for consistency)

## Key Files
- `{project}/core/stages/` - Pipeline stages
- `{project}/llm/client.py` - LLM integration
- `tests/test_stages.py` - Unit tests
```

---

## Layer 4: Project Type Adapters

### The Three Adapters

VULCAN supports three project types via adapters:

#### 1. DeterministicAdapter (HART-like)

**Use Case:** Therapy assistants, medical AI, risk assessment - projects requiring high confidence and strict rules

**Adds to project structure:**
- `core/stages/` - Pipeline stage base classes
- `core/scoring/` - Confidence scoring engine
- `core/validation/` - Validation framework
- Pages: Pipeline, Scoring, Validation monitoring

**Example:** HART OS (therapy assistant with 5-stage pipeline)

#### 2. CreativeAdapter (VIA-like)

**Use Case:** Investment research, knowledge synthesis - projects requiring RAG and exploration

**Adds to project structure:**
- `rag/` - RAG pipeline (chunk, index, retrieve, synthesize)
- `insight_engines/` - Hypothesis generation, contradiction detection
- `corpus/` - Document management
- Pages: Corpus management, Insights explorer

**Example:** VIA (investment research with synthesis)

#### 3. ProcessorAdapter (DATA FORGE-like)

**Use Case:** Data processing, ETL, transformation - projects requiring multi-stage compilation

**Adds to project structure:**
- `compiler/` - Multi-stage compilation pipeline
- `taxonomy/` - Hierarchical classification
- `memory/` - SQLite-backed key-value store
- Pages: Processor config, Taxonomy explorer, Memory monitor, Data explorer

**Example:** DATA FORGE (data processing with compilation)

### Adapter Pattern: BaseAdapter

```python
# vulcan_forge/adapters/base_adapter.py
from abc import ABC, abstractmethod
from pathlib import Path

class BaseAdapter(ABC):
    """Abstract base for project type adapters"""

    def __init__(self, project_path: Path, settings: dict):
        self.project_path = project_path
        self.settings = settings

    @abstractmethod
    def add_core_structure(self) -> None:
        """Add adapter-specific core/ subdirectories"""
        pass

    @abstractmethod
    def add_pages(self) -> None:
        """Add adapter-specific Streamlit pages"""
        pass

    @abstractmethod
    def add_tests(self) -> None:
        """Add adapter-specific test templates"""
        pass

    @abstractmethod
    def add_documentation(self) -> None:
        """Add adapter-specific documentation"""
        pass

    def execute(self) -> None:
        """Execute all adapter setup"""
        self.add_core_structure()
        self.add_pages()
        self.add_tests()
        self.add_documentation()
```

---

## Layer 5: User Interface (VULCAN)

### The Three-Page Flow

#### Page 1: New Project Wizard (7-Step Questionnaire)

**7-Step HITL Questionnaire:**

1. **Project Identity** - Name, type, description
2. **LLM Configuration** - Primary/secondary providers, models
3. **Streamlit Configuration** - Port, theme, multi-page settings
4. **GAIA Integration** - Claude Code, ARGUS monitoring, git init
5. **Development Options** - Tests, sample data, documentation
6. **Project Type Specifics** - Adapter-dependent options
7. **Confirmation** - Review + create

**Questionnaire Data Model:**

```python
# vulcan_forge/questionnaire.py
from pydantic import BaseModel
from typing import Optional, List

class ProjectIdentity(BaseModel):
    name: str
    type: str  # "deterministic", "creative", "processor"
    description: str

class LLMConfiguration(BaseModel):
    primary_provider: str  # "openai", "anthropic", "gemini"
    secondary_provider: Optional[str] = None
    primary_model: str
    secondary_model: Optional[str] = None

class StreamlitConfiguration(BaseModel):
    port: int = 8501
    theme: str = "light"  # or "dark"
    multi_page: bool = True

class GaiaIntegration(BaseModel):
    use_claude_code: bool = True
    enable_argus_monitoring: bool = True
    init_git: bool = True

class DevelopmentOptions(BaseModel):
    include_tests: bool = True
    sample_data: bool = True
    documentation_level: str  # "minimal", "standard", "comprehensive"

class VulcanQuestionnaire(BaseModel):
    """Complete questionnaire response"""
    identity: ProjectIdentity
    llm: LLMConfiguration
    streamlit: StreamlitConfiguration
    gaia: GaiaIntegration
    dev: DevelopmentOptions
```

#### Page 2: Register Existing Project

**Three Retroactive Registration Modes:**

1. **Registry-Only**
   - Add to registry.json
   - No changes to project structure
   - Safest option

2. **GAIA-Lite**
   - Add .env.example (if missing)
   - Add config.py with GaiaSettings (if missing)
   - Add ARGUS hooks (if missing)
   - Minimal touch

3. **Full GAIA** (not recommended)
   - Complete restructure to GAIA template
   - High risk of breaking existing projects
   - Only for projects in development

#### Page 3: Project Explorer

**Features:**
- List all registered projects
- Filter by status, type, provider
- Validate project structure
- Bulk operations (update registry, add ARGUS hooks)
- One-click project launcher (via Streamlit)

---

## Layer 6: Core Orchestration (ProjectCreator)

### The ProjectCreator Engine

**Location:** `vulcan_forge/project_creator.py`

**Responsibilities:**
1. Orchestrate questionnaire flow
2. Select appropriate adapter
3. Generate project scaffolding
4. Update registry
5. Validate final structure

```python
# vulcan_forge/project_creator.py
from pathlib import Path
from vulcan_forge.questionnaire import VulcanQuestionnaire
from vulcan_forge.adapters import (
    DeterministicAdapter, CreativeAdapter, ProcessorAdapter
)
from vulcan_forge.registry_manager import RegistryManager

class ProjectCreator:
    def __init__(self, base_path: Path):
        self.base_path = base_path
        self.registry_manager = RegistryManager(
            base_path / "_gaia" / "registry.json"
        )

    def create_project(self, questionnaire: VulcanQuestionnaire) -> Path:
        """Create a new GAIA-compliant project"""

        # 1. Create project directory
        project_path = self.base_path / questionnaire.identity.name
        project_path.mkdir(parents=True, exist_ok=True)

        # 2. Create base GAIA structure
        self._create_base_structure(project_path, questionnaire)

        # 3. Select and execute adapter
        adapter = self._get_adapter(
            questionnaire.identity.type,
            project_path,
            questionnaire
        )
        adapter.execute()

        # 4. Update registry
        self._register_project(questionnaire, project_path)

        # 5. Validate
        from vulcan_forge.project_validator import ProjectValidator
        validator = ProjectValidator(project_path)
        validator.validate()

        return project_path

    def _get_adapter(self, adapter_type: str, project_path: Path,
                     questionnaire: VulcanQuestionnaire):
        """Get appropriate adapter based on project type"""
        if adapter_type == "deterministic":
            return DeterministicAdapter(project_path, questionnaire.dict())
        elif adapter_type == "creative":
            return CreativeAdapter(project_path, questionnaire.dict())
        elif adapter_type == "processor":
            return ProcessorAdapter(project_path, questionnaire.dict())
        else:
            raise ValueError(f"Unknown adapter type: {adapter_type}")

    def _create_base_structure(self, project_path: Path,
                               questionnaire: VulcanQuestionnaire):
        """Create base GAIA project structure"""
        # Create directories
        (project_path / questionnaire.identity.name).mkdir()
        (project_path / questionnaire.identity.name / "core").mkdir()
        (project_path / questionnaire.identity.name / "ui").mkdir()
        (project_path / questionnaire.identity.name / "llm").mkdir()
        (project_path / questionnaire.identity.name / "utils").mkdir()
        (project_path / "pages").mkdir()
        (project_path / "data").mkdir()
        (project_path / "logs").mkdir()
        (project_path / "tests").mkdir()
        (project_path / "docs").mkdir()

        # Create files
        self._create_config_py(project_path, questionnaire)
        self._create_launch_py(project_path, questionnaire)
        self._create_env_example(project_path, questionnaire)
        self._create_claude_md(project_path, questionnaire)
        self._create_readme(project_path, questionnaire)
        self._create_gitignore(project_path)
        self._create_requirements_txt(project_path, questionnaire)

    def _register_project(self, questionnaire: VulcanQuestionnaire,
                          project_path: Path):
        """Register project in GAIA registry"""
        project_data = {
            "path": str(project_path),
            "version": "0.1.0",
            "status": "development",
            "git": questionnaire.gaia.init_git,
            "providers": [questionnaire.llm.primary_provider],
            "tags": [questionnaire.identity.type],
            "created": datetime.now().isoformat(),
            "last_updated": datetime.now().isoformat(),
            "type": questionnaire.identity.type
        }
        self.registry_manager.register_project(
            questionnaire.identity.name, project_data
        )
```

---

## Design Patterns Used Throughout GAIA

### Pattern 1: Adapter Pattern

**Used for:** Project type customization

**Implementation:** BaseAdapter with subclasses for each type

**Benefits:**
- Easy to add new project types
- Type-specific logic isolated
- Common logic in base class
- Follows open/closed principle

### Pattern 2: Factory Pattern

**Used for:** LLM client creation, adapter selection

**Implementation:**
```python
def create_llm_client(provider: str) -> BaseClient:
    if provider == "openai":
        return OpenAIClient(...)
    elif provider == "anthropic":
        return AnthropicClient(...)
    elif provider == "gemini":
        return GeminiClient(...)
```

**Benefits:**
- Centralized object creation
- Easy to add new providers
- Consumer code doesn't know implementation details

### Pattern 3: Settings Pattern (Pydantic)

**Used for:** Configuration management

**Implementation:** BaseSettings with inheritance hierarchy

**Benefits:**
- Type-safe configuration
- .env file support
- Validation at creation time
- Hierarchical inheritance (Global → Project → Adapter)

### Pattern 4: Registry Pattern

**Used for:** Project discovery

**Implementation:** Single JSON file, CRUD operations

**Benefits:**
- Simple, no database required
- Human-readable format
- Easy to backup and version
- ARGUS can discover all projects

### Pattern 5: Pipeline Pattern

**Used for:** Deterministic projects (stages)

**Implementation:** Stage base class with execute() method

**Benefits:**
- Stages can be tested independently
- Easy to add/remove/reorder stages
- Confidence scoring between stages
- Clear data flow

### Pattern 6: Glass-Box Pattern (Proposed for LOOM Phase 3)

**Used for:** Explainability and transparency

**Benefits:**
- User sees exactly what happened
- Failures are educational, not mysterious
- Trust builds through understanding
- Adjustments become possible

---

## Runtime Governance: The Authority Graph

**Critical Insight:** GAIA currently orchestrates **creation**, not **runtime cognition**. The authority graph defines who can decide, mutate, observe, and ratify at runtime.

### The Authority Hierarchy

```
GAIA (constitutional authority)
│
├── Project Agent (accountable unit)
│   │
│   ├── Execution Agents (task-bounded)
│   │   └── Sub-agents (ephemeral, stateless)
│   │
│   ├── Process Observer (non-intervening)
│   └── Technical PM Agent (translator, Phase 3)
│
└── ARGUS (observer only, never actor)
```

### Authority Rules (Constitutional)

#### Rule 1: Only Project Agents Can Mutate State

**What this means:**
- Project Agents are the sole accountable unit
- Sub-agents can **propose** changes, but cannot **apply** them
- All mutations traced to Project Agent level

**Why this matters:**
- Single point of accountability
- No distributed blame
- Clear audit trail

**Example:**
```
❌ Sub-agent directly modifies memory
✅ Sub-agent proposes → Project Agent evaluates → Project Agent mutates
```

---

#### Rule 2: Sub-agents Cannot Persist Memory

**What this means:**
- Sub-agents are ephemeral and stateless
- Any memory created by sub-agent expires when sub-agent terminates
- To persist, sub-agent must **propose promotion** to Project Agent

**Why this matters:**
- Prevents memory pollution
- Prevents silent drift
- Forces explicit promotion decisions

**Example:**
```python
# Sub-agent creates ephemeral memory
sub_agent.create_memory(content="Pattern X detected", scope="agent")

# Sub-agent proposes promotion (requires approval)
sub_agent.propose_promotion(
    memory_id="pattern_x",
    to_scope="project",
    rationale="Seen in 5/10 executions, likely recurring pattern"
)

# Project Agent evaluates and decides
project_agent.evaluate_promotion(proposal_id) → [accept|reject]
```

---

#### Rule 3: Observers Cannot Issue Commands

**What this means:**
- Process Observer agents are **read-only**
- Can analyze execution traces, detect patterns, identify regressions
- **Cannot:** Execute tools, modify code, update memory, issue commands

**Why this matters:**
- Prevents self-reinforcing loops
- Prevents bias accumulation
- Observers produce **hypotheses**, not actions

**Output:** Structured reports, pattern hypotheses, suggested constraints
**Destination:** Reports go to GAIA for human/GAIA-level ratification

**Example:**
```python
# Process Observer analyzes execution traces
observer = ProcessObserver(project="hart_os")
report = observer.analyze_last_30_days()

# Report structure
{
  "pattern_detected": "Confidence scores drifting downward",
  "evidence": [
    "Stage 3 average confidence: 0.82 → 0.76 (7% decline)",
    "5 instances of <0.70 threshold violations"
  ],
  "hypothesis": "Model prompt may have regressed, or data quality declined",
  "suggested_constraints": [
    "Add minimum confidence threshold to Stage 3",
    "Add data quality check before Stage 1"
  ],
  "escalation": "Requires human review - structural issue detected"
}

# Observer CANNOT apply suggested constraints
# Report goes to GAIA → Human reviews → Human decides
```

---

#### Rule 4: GAIA Never Executes, Only Ratifies

**What this means:**
- GAIA is **legislative**, not **executive**
- Execution happens at Project level
- GAIA enforces contracts, not behaviors

**Why this matters:**
- Separation of powers (like government branches)
- GAIA remains constitutional layer
- Projects remain autonomous within contracts

**Example:**
```
❌ GAIA directly modifies project code
✅ GAIA defines contract → Project implements → GAIA validates compliance
```

**GAIA's Role:**
- Define GAIA project structure (contract)
- Validate project structure (compliance check)
- Ratify memory promotions (approval gate)
- Never execute tools or modify project code

---

### New Agent Classes (Phase 2 & 3)

#### Process Observer Agent (Phase 2: ARGUS)

**Charter:**
- Read-only access to all project state
- Analyze execution traces
- Detect pattern drift
- Identify structural regressions

**Cannot:**
- Execute tools
- Modify code
- Update memory
- Issue commands

**Outputs:**
- Structured post-mortem reports
- Pattern hypotheses (not conclusions)
- Suggested constraints (not commands)
- Escalation triggers

**Integration Point:** Reports go to GAIA for human ratification

**Why This Works:**
- Mimics senior TPM/retrospective role in human teams
- Non-interventionist (can't cause harm)
- Explicit in uncertainty (proposes, doesn't declare)
- Builds trust through transparency

**Example Use Case:**
```
Process Observer detects:
"5 projects now using OpenAI gpt-4o-mini instead of gpt-4o.
Cost savings: $2,340/month.
Accuracy impact: -3% on deterministic projects, negligible on creative.
Hypothesis: Cost-driven model downgrade may be hurting HART OS quality.
Suggested: Restore gpt-4o for therapy domain specifically."

→ Human reviews
→ Human decides: "Accept for HART, keep mini for others"
→ GAIA logs decision with rationale
```

---

#### Technical PM Agent (Phase 3: LOOM)

**Charter:**
- Translate across agent boundaries
- Coordinate multi-agent workflows
- Detect communication breakdowns
- **Cannot:** Override agent decisions

**Outputs:**
- Coordination plans
- Translation artifacts
- Escalation triggers

**Integration Point:** Operates at Project Agent level, reports to GAIA when stuck

**Why This Works:**
- Addresses coordination tax in multi-agent systems
- Clear authority (coordinate, not command)
- Escalation path preserves human agency

**Example Use Case:**
```
Multi-agent workflow in LOOM:
Agent 1 (Research): Finds 50 papers
Agent 2 (Summarize): Expects structured list
Agent 3 (Synthesize): Expects semantic graph

Technical PM Agent:
- Detects format mismatch
- Translates Agent 1 output → Agent 2 input
- Coordinates data flow
- Does NOT change agent behavior, only facilitates communication
```

---

### Memory Hierarchy & Access Contracts (Phase 3: MNEMIS)

**Three Memory Tiers:**
1. **GAIA Memory** - Ecosystem-wide, eternal
2. **Project Memory** - Project-scoped, persistent
3. **Agent Memory** - Execution-scoped, ephemeral

**Access Rules:**

```python
class MemoryAccessLevel(Enum):
    GAIA = "gaia"           # Ecosystem-wide
    PROJECT = "project"     # Project-scoped
    AGENT = "agent"         # Ephemeral

class MemoryContract:
    def can_read(self, agent_level, memory_scope):
        """Agents can read at their level or below"""
        hierarchy = {GAIA: 3, PROJECT: 2, AGENT: 1}
        return hierarchy[agent_level] >= hierarchy[memory_scope]

    def can_write(self, agent_level, memory_scope):
        """Agents can only write at their exact level"""
        return agent_level == memory_scope

    def can_propose_promotion(self, agent_level):
        """Only PROJECT agents can propose to GAIA"""
        return agent_level == MemoryAccessLevel.PROJECT
```

**Memory Promotion Protocol:**

```
Agent creates memory → stored in AGENT tier (ephemeral)
    ↓
Agent proposes promotion → PROJECT tier
    ↓
Project Agent evaluates → [accept|reject]
    ↓ (if pattern repeats across projects)
Project Agent proposes → GAIA tier
    ↓
GAIA + Human ratify → ecosystem memory
```

**Why This Works:**
- Explicit promotion (no silent drift)
- Human in loop at GAIA tier
- Provenance tracked at every step
- Reversible (demote if wrong)

---

### Sense-Making vs. Monitoring

**Current ARGUS Plan (Phase 2):**
- Telemetry collection ✅
- Dashboard visualization ✅
- Cost tracking ✅
- Error aggregation ✅
- Execution board (Kanban) ✅

**Required Extension: Sense-Making Layer**
- Pattern detection across failures (NEW)
- Structural regression identification (NEW)
- Cross-project anti-pattern surfacing (NEW)
- Post-mortem synthesis without blame (NEW)

**ARGUS becomes:**
- Not just a watcher (telemetry)
- But a reflector (pattern learning)

**Critical Distinction:**
```
Monitoring:   "Project X had 5 errors yesterday"
Sense-Making: "Project X errors increased 40% after dependency update.
               Pattern seen in 3 other projects. Hypothesis: Breaking change
               in rag-intelligence v0.3.2. Suggested: Pin to v0.3.1 until fixed."
```

**Implementation:**
- Process Observer analyzes telemetry
- Detects patterns humans would miss
- Produces hypotheses (not conclusions)
- Escalates to human for decision

---

### Reflective Cognition vs. Executive Cognition

**Critical Question:** How much cognition should GAIA allow itself without becoming the thing it's trying to protect the user from?

**Answer:** GAIA should have **reflective cognition**, not **executive cognition**.

**Allowed (Reflective):**
- Pattern detection (observe trends)
- Hypothesis generation (suggest explanations)
- Proposal creation (recommend changes)
- Sense-making (synthesize post-mortems)

**Prohibited (Executive):**
- Autonomous execution (GAIA never runs code)
- Silent learning (all learning requires approval)
- Self-modification (GAIA structure is constitutional)
- Intervention (GAIA observes, Project Agents execute)

**Boundary Example:**
```
✅ Reflective Cognition:
   "I noticed pattern X across 5 projects. Should we address it?"
   [User: Yes/No/Explain More]

❌ Executive Cognition:
   "I noticed pattern X. I fixed it automatically across all projects."
   ↑ THIS IS PROHIBITED
```

**Why This Works:**
- GAIA remains transparent (reflective, not autonomous)
- User retains agency (approves proposals)
- System learns safely (explicit confirmation)
- Trust is preserved (no black-box behavior)

---

### Escalation Paths

**When uncertainty persists, GAIA escalates through defined paths:**

**Level 1: Project Agent Stuck**
```
Project Agent encounters uncertainty
    → Escalates to Process Observer (sense-making)
    → Process Observer analyzes context, produces hypothesis
    → Returns to Project Agent with recommendation
```

**Level 2: Process Observer Stuck**
```
Process Observer cannot determine root cause
    → Escalates to GAIA with evidence
    → GAIA presents to human with options
    → Human decides
    → GAIA logs decision with rationale
```

**Level 3: GAIA Boundary Reached**
```
Task requires authority GAIA doesn't have
    → GAIA explicitly states limitation
    → Provides context for why task is out of scope
    → Suggests alternative approaches
    → Does NOT attempt workaround
```

**Example:**
```
User: "Fix this bug in project X"

Project Agent: "Bug is in rag-intelligence library, not project code.
                I cannot modify shared library from project level.
                Escalating to GAIA."

GAIA: "This requires modifying MYCEL (shared library).
       I can: (A) Create issue in MYCEL tracker
              (B) Suggest workaround in project X
              (C) Wait for MYCEL maintainer
       I cannot: Modify MYCEL directly (outside project scope)
       What would you like?"
```

---

## Integration Contracts

### Contract 1: VULCAN → Projects

**VULCAN Guarantees (What it creates):**
- Standard directory structure
- config.py with GaiaSettings
- Streamlit launcher
- MYCEL LLM client integration
- Tests directory with templates
- Documentation scaffold
- .gitignore with secrets protection
- CLAUDE.md context anchor
- Registry entry
- logs/ directory for Phase 2

**Projects Must Provide (for ARGUS Phase 2):**
- Structured logging using telemetry hooks
- CLAUDE.md kept up-to-date
- config.py inherits GaiaSettings
- Regular git commits with messages

### Contract 2: MYCEL ↔ All Projects

**MYCEL Provides:**
- GaiaSettings configuration class
- create_llm_client() factory
- Core algorithms (chunking, embedding, retrieval)
- Telemetry hooks (Phase 2)

**Projects Provide:**
- Implement config.py inheriting GaiaSettings
- Use create_llm_client() instead of direct API calls
- Emit telemetry (Phase 2)

### Contract 3: ARGUS → Projects

**ARGUS Expects (Phase 2):**
- Telemetry written to logs/{project}/*.jsonl
- Registry entry with current path/version
- CLAUDE.md with project metadata
- config.py with GaiaSettings

**ARGUS Provides:**
- Cost tracking dashboard
- Error aggregation
- Execution board (Kanban)
- Project health status

---

## Lifecycle of a GAIA Project

### Creation Phase (Day 1)

1. User runs `streamlit run vulcan/ui/main.py`
2. Answers 7-step questionnaire
3. VULCAN creates project with:
   - Standard GAIA structure
   - Appropriate adapter installed
   - tests/ and docs/ templates
   - MYCEL integration configured
4. User clones project folder, runs `pip install -r requirements.txt`
5. User runs `streamlit run launch_{project}.py` - app starts

### Development Phase (Week 1-4)

1. User modifies core/ logic
2. Extends stages or components
3. Runs tests: `pytest tests/`
4. Commits to git: `git commit -m "feat: add stage 4"`
5. Tests pass before commit (pre-commit hooks)

### Monitoring Phase (Day 1+, Phase 2 onward)

1. App emits telemetry via MYCEL
2. ARGUS collects from logs/ directory
3. User sees costs, errors, execution status in ARGUS dashboard
4. User gets notifications if thresholds exceeded

### Iteration Phase (Ongoing)

1. User identifies needed changes via ARGUS dashboard
2. Opens project, modifies adapter/stages/config
3. Tests locally, commits, deploys
4. ARGUS shows impact of changes (cost reduction, error decrease)

### Teaching Phase (Month 3+)

1. User documents workflow in CLAUDE.md and docs/
2. Creates custom adapter for team use
3. Shares template in ecosystem
4. Team members use as starting point

---

## Why This Architecture Works

### For the Creator (Fed)

- **Day 1:** "I have tools and structure"
- **Month 1:** "I understand why structure matters"
- **Month 3:** "I can modify structures for my needs"
- **Year 1:** "I design new structures others will use"

### For the Ecosystem

- **Unified:** All projects follow same pattern
- **Discoverable:** Registry shows what exists
- **Governable:** WARDEN can enforce standards
- **Observable:** ARGUS can see everything
- **Scalable:** Adding components follows same pattern

### For AI Integration

- **Transparent:** User sees all code generation
- **Modular:** Changes are isolated to stages/components
- **Testable:** Each module can be validated
- **Learnable:** User understands what was built

---

---

## Appendix: Key Files Reference

### GAIA Meta-Layer Files

| File | Purpose | Size | Format |
|------|---------|------|--------|
| `X:\Projects\_gaia\registry.json` | All projects with metadata | 136 lines | JSON |
| `X:\Projects\_gaia\VERSION_LOG.md` | Version history and roadmap | 173 lines | Markdown |
| `X:\Projects\_gaia\PHASE_1_HANDOFF.md` | Phase 1 → Phase 2 transition | 551 lines | Markdown |
| `X:\Projects\_gaia\PHASE_1_COMPLETE.md` | VULCAN delivery details | 855 lines | Markdown |
| `X:\Projects\_gaia\v0_baseline.md` | Pre-GAIA snapshot | 144 lines | Markdown |

### VULCAN Core Files

| File | Purpose | Lines | Status |
|------|---------|-------|--------|
| `vulcan_forge/project_creator.py` | Orchestrator | 595 | ✅ |
| `vulcan_forge/questionnaire.py` | HITL intake forms | 180 | ✅ |
| `vulcan_forge/registry_manager.py` | Registry CRUD | 120 | ✅ |
| `vulcan_forge/project_validator.py` | GAIA compliance | 185 | ✅ |
| `vulcan_forge/adapters/base_adapter.py` | Abstract interface | 50 | ✅ |
| `vulcan_forge/adapters/deterministic_adapter.py` | HART-like | 1,047 | ✅ |
| `vulcan_forge/adapters/creative_adapter.py` | VIA-like | 938 | ✅ |
| `vulcan_forge/adapters/processor_adapter.py` | DATA FORGE-like | 1,758 | ✅ |

### MYCEL Spine Files

| File | Purpose | Status |
|------|---------|--------|
| `rag_intelligence/config.py` | GaiaSettings base | ✅ |
| `rag_intelligence/integrations/base_client.py` | Abstract LLM | ✅ |
| `rag_intelligence/integrations/openai_client.py` | OpenAI wrapper | ✅ |
| `rag_intelligence/integrations/anthropic_client.py` | Anthropic wrapper | ✅ |
| `rag_intelligence/integrations/gemini_client.py` | Gemini wrapper | ✅ |
| `rag_intelligence/integrations/llm_factory.py` | Factory | ✅ |
| `rag_intelligence/core/models.py` | Chunk, Document, Embedding | ✅ |

---

## Navigation Guide

**For First-Time Readers:**
1. Start with Chapter 0 (this ecosystem status)
2. Read Chapter 1 (vision and problem)
3. Skim Chapter 2 (architecture overview)

**For Project Creators:**
1. Review Chapter 0 (naming and three pillars)
2. Jump to Chapter 3 (VULCAN guide)
3. Refer to Chapter 5 (API reference)

**For System Designers:**
1. Study Chapter 2 (architecture)
2. Review Chapter 4 (adapter patterns)
3. Consult Appendices for details

**For Ecosystem Managers:**
1. Chapter 0 (current status)
2. Appendix A (registry)
3. Appendix B (history)

---

## Version Control

**Bible Version:** 0.4.0
**Last Updated:** February 4, 2026
**Status:** Phase 1 Complete ✅
**Next Update:** When Phase 2 (ARGUS) begins

**Maintained by:** GAIA Ecosystem Team
**Constitutional Frequency:** Updated at every major phase transition

---

*This is a living document. As GAIA evolves, so does this Bible. It consolidates all canonical knowledge about the ecosystem and serves as the authoritative source of truth for all decisions, designs, and integrations.*

*Every component added to GAIA should update this document. Every decision made should reference this document. Every user onboarded should read this document.*

*GAIA is transparent. Its rules, structures, and principles are all visible here.*

---

# CHAPTER 3: Using VULCAN - Project Creation Guide

## Overview

VULCAN is The Forge of the GAIA Ecosystem. It creates GAIA-compliant projects from day one with proper structure, configuration, ecosystem integration, and adapter-specific customizations.

**Key Features:**
- 7-Step Interactive Questionnaire
- Three project type adapters (Deterministic, Creative, Processor)
- Automatic GAIA ecosystem integration
- Streamlit-ready multi-page templates
- Automatic registry management
- Post-creation validation

## The 7-Step Questionnaire

### Step 1: Project Identity

Define what the project is and why it exists.

**Fields:**
- **Name** (snake_case): `sentiment_analyzer`, `data_processor_v2`
- **Display Name** (human-readable): "Sentiment Analyzer", "Data Processor v2"
- **Project Type**:
  - **Deterministic**: HART-like pipelines with stages and scoring
  - **Creative**: VIA-like RAG and synthesis engines
  - **Processor**: DATA FORGE-like compilation and taxonomy
- **Description** (one sentence): "Analyzes customer feedback for sentiment"

### Step 2: LLM Configuration

Configure LLM provider and model settings.

**Fields:**
- **Primary Provider**: OpenAI (GPT-4o), Anthropic (Claude Sonnet), or Gemini
- **Secondary Provider** (optional): Fallback if primary fails
- **Temperature** (0.0-2.0, default 0.7):
  - 0.0-0.3: Deterministic
  - 0.4-0.7: Balanced
  - 0.8-2.0: Creative

### Step 3: Streamlit Configuration

Configure web UI settings.

**Fields:**
- **Port** (8000-9000, default 8501)
- **Multi-Page** (default True): Creates pages/ directory
- **Theme**: material_dark (default), material_light, or custom

### Step 4: GAIA Integration

Connect to GAIA ecosystem services.

**Fields:**
- **Claude Code Template** (default True): Adds .clproj configuration
- **ARGUS Telemetry** (default True): Enables monitoring hooks
- **Git Init** (default True): Initializes git repository
- **Register in Ecosystem** (default True): Adds to GAIA registry

### Step 5: Development Options

Configure development and testing setup.

**Fields:**
- **Create Tests** (default True): Creates tests/ with pytest
- **Add Sample Data** (default False): Includes sample files
- **Documentation Level**: minimal, standard (default), or comprehensive
- **Pre-Commit Hooks** (default True): black, ruff, pytest

### Step 6: Project Type Specifics

Adapter-specific configuration (varies by project type).

**For Deterministic:**
```python
enable_stages=True
enable_scoring=True
confidence_threshold=0.75
```

**For Creative:**
```python
enable_rag=True
enable_synthesis=True
enable_corpus_management=True
```

**For Processor:**
```python
enable_compiler=True
enable_taxonomy=True
enable_memory_store=True
```

### Step 7: Confirmation

Review all settings and confirm project creation.

---

## Creating Projects Programmatically

### Basic Project Creation

```python
from vulcan_forge import ProjectCreator, VulcanQuestionnaire
from vulcan_forge.questionnaire import (
    ProjectIdentity, LLMConfiguration, StreamlitConfiguration,
    GAIAIntegration, DevelopmentOptions, ProjectTypeSpecifics,
    ProjectType, LLMProvider
)

questionnaire = VulcanQuestionnaire(
    identity=ProjectIdentity(
        name="sentiment_analyzer",
        display_name="Sentiment Analyzer",
        project_type=ProjectType.DETERMINISTIC,
        description="Analyzes sentiment in customer feedback"
    ),
    llm_config=LLMConfiguration(
        primary_provider=LLMProvider.ANTHROPIC,
        temperature=0.7
    ),
    streamlit_config=StreamlitConfiguration(
        port=8501,
        enable_multipage=True,
        theme="material_dark"
    ),
    gaia_integration=GAIAIntegration(
        enable_claude_code_template=True,
        enable_git_init=True,
        register_in_ecosystem=True
    ),
    dev_options=DevelopmentOptions(
        create_tests=True,
        documentation_level="standard"
    ),
    type_specifics=ProjectTypeSpecifics(
        enable_stages=True,
        enable_scoring=True,
        confidence_threshold=0.75
    )
)

creator = ProjectCreator()
project_path = creator.create_project(questionnaire)
print(f"Project created at: {project_path}")
```

## Registering Existing Projects

Register GAIA-compliant projects created outside VULCAN:

```python
from vulcan_forge import RegistryManager

registry = RegistryManager()

registry.register_project(
    project_key="my_existing_project",
    name="My Existing Project",
    path="/absolute/path/to/project",
    version="1.0.0",
    status="production",
    git=True,
    providers=["anthropic"],
    depends_on=["mycel"],
    tags=["analysis", "nlp"]
)
```

---

# CHAPTER 4: VULCAN Adapter Architecture & Development

## Adapter Pattern Philosophy

The Adapter Pattern allows customization of project creation based on project type. Adapters:

1. Customize directory structure
2. Generate type-specific files
3. Customize configuration
4. Specify dependencies
5. Create UI pages
6. Perform post-creation hooks

## BaseAdapter Interface

All adapters implement the BaseAdapter abstract class:

```python
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any

class BaseAdapter(ABC):
    """Base adapter for project type customization."""

    def __init__(self, questionnaire: dict[str, Any]):
        self.questionnaire = questionnaire
        self.type_specifics = questionnaire.get("type_specifics", {})

    @abstractmethod
    def get_additional_directories(self) -> list[str]:
        """Return list of relative directory paths to create."""
        pass

    @abstractmethod
    def get_additional_files(self) -> dict[str, str]:
        """Return dict of relative_path -> file_content."""
        pass

    @abstractmethod
    def customize_config(self, base_config: dict[str, Any]) -> dict[str, Any]:
        """Customize configuration for this adapter type."""
        pass

    @abstractmethod
    def get_requirements(self) -> list[str]:
        """Return list of pip requirements."""
        pass

    @abstractmethod
    def get_ui_pages(self) -> dict[str, str]:
        """Return dict of page_filename -> page_content."""
        pass

    def get_readme_sections(self) -> list[tuple[str, str]]:
        """Return list of (section_title, section_content) tuples (optional)."""
        return []

    def post_creation_hook(self, project_path: Path) -> None:
        """Hook called after project creation (optional)."""
        pass
```

## The Three Adapters

### DeterministicAdapter (HART-like)

For structured, rule-based projects with multi-stage pipelines and confidence scoring.

**Creates:**
- Pipeline stages infrastructure (core/stages/)
- Scoring system (core/scoring/)
- Validation framework (core/validation/)
- Streamlit pages for pipeline, scoring, validation

**Key Classes:**
- **StageBase**: Base class for pipeline stages
- **ScoringEngine**: Scores results against quality metrics
- **BasePipeline**: Orchestrates stage execution

### CreativeAdapter (VIA-like)

For exploratory, document-centric projects with RAG and insight synthesis.

**Creates:**
- RAG pipeline (rag/)
- Insight synthesis engines (insight_engines/)
- Corpus management (corpus/)
- Streamlit pages for corpus and insights

**Key Classes:**
- **RAGPipeline**: Semantic search and retrieval
- **InsightSynthesizer**: Generate hypotheses and detect contradictions
- **CorpusManager**: Manage document collections

### ProcessorAdapter (DATA FORGE-like)

For data transformation, batch processing, and hierarchical classification.

**Creates:**
- Compiler pipeline (compiler/)
- Taxonomy system (taxonomy/)
- Memory store (memory/)
- Processors base (processors/)
- Streamlit pages for all systems

**Key Classes:**
- **CompilerPipeline**: Multi-stage compilation
- **TaxonomyManager**: Hierarchical classification
- **MemoryStore**: Persistent key-value store with TTL
- **BaseProcessor**: Data processors

## Creating Custom Adapters

### Minimal Custom Adapter

```python
from vulcan_forge.adapters.base_adapter import BaseAdapter
from typing import Any

class MyCustomAdapter(BaseAdapter):
    """Custom adapter for specialized projects."""

    def get_additional_directories(self) -> list[str]:
        return ["src/my_project/custom", "data/custom"]

    def get_additional_files(self) -> dict[str, str]:
        project_name = self.questionnaire.get("identity", {}).get("name")
        return {
            f"src/{project_name}/custom/__init__.py": '"""Custom module."""\n',
        }

    def customize_config(self, base_config: dict[str, Any]) -> dict[str, Any]:
        config = base_config.copy()
        config["custom_settings"] = {"feature_enabled": True}
        return config

    def get_requirements(self) -> list[str]:
        return ["custom-package>=1.0.0"]

    def get_ui_pages(self) -> dict[str, str]:
        return {"pages/1_custom.py": '"""Custom page."""\nimport streamlit as st\nst.title("Custom")'}
```

## Best Practices

1. **Always validate input** in adapter methods
2. **Use template methods** to keep code clean
3. **Be conditional with configuration** based on type_specifics
4. **Document configuration options** in comments
5. **Test post-creation hooks** with error handling
6. **Keep adapters focused** on single responsibility

---

# CHAPTER 5: VULCAN API Reference & Interfaces

## Core Models

### ProjectType (Enum)

```python
class ProjectType(str, Enum):
    DETERMINISTIC = "deterministic"  # HART-like
    CREATIVE = "creative"            # VIA-like
    PROCESSOR = "processor"          # DATA FORGE-like
```

### LLMProvider (Enum)

```python
class LLMProvider(str, Enum):
    OPENAI = "openai"
    ANTHROPIC = "anthropic"
    GEMINI = "gemini"
```

### Key Pydantic Models

**ProjectIdentity**: Step 1 - Basic project information
- name (str): Project identifier (snake_case)
- display_name (str): Human-readable name
- project_type (ProjectType): Determines adapter
- description (str): One-sentence summary

**LLMConfiguration**: Step 2 - LLM settings
- primary_provider (LLMProvider): Main provider
- secondary_provider (Optional): Fallback
- temperature (float): 0.0-2.0

**StreamlitConfiguration**: Step 3 - UI settings
- port (int): 8000-9000
- enable_multipage (bool): Default True
- theme (str): material_dark, material_light, custom

**GAIAIntegration**: Step 4 - Ecosystem integration
- enable_claude_code_template (bool)
- enable_argus_telemetry (bool)
- enable_git_init (bool)
- register_in_ecosystem (bool)

**DevelopmentOptions**: Step 5 - Development setup
- create_tests (bool)
- add_sample_data (bool)
- documentation_level (str): minimal, standard, comprehensive
- add_pre_commit_hooks (bool)

**ProjectTypeSpecifics**: Step 6 - Adapter-specific options
- enable_stages, enable_scoring, confidence_threshold (Deterministic)
- enable_rag, enable_synthesis, enable_corpus_management (Creative)
- enable_compiler, enable_taxonomy, enable_memory_store (Processor)

**VulcanQuestionnaire**: Complete questionnaire
- Combines all 6 steps
- Provides `.summary` property
- Converts to dict with `.to_dict()`

## ProjectCreator

Main engine for creating GAIA-compliant projects.

```python
class ProjectCreator:
    """Create GAIA-compliant projects from questionnaire."""

    def __init__(self, registry_manager: Optional[RegistryManager] = None):
        """Initialize ProjectCreator."""
        pass

    def create_project(self, questionnaire: VulcanQuestionnaire) -> Path:
        """
        Create a GAIA-compliant project.

        Args:
            questionnaire: Complete questionnaire data

        Returns:
            Path to created project directory

        Raises:
            ValueError: If project already exists or invalid configuration
            OSError: If filesystem operations fail
        """
        pass
```

## RegistryManager

Manages GAIA ecosystem project registration.

```python
class RegistryManager:
    """Manages GAIA ecosystem registry."""

    def register_project(
        self,
        project_key: str,
        name: str,
        path: str,
        version: str,
        status: str = "development",
        git: bool = True,
        providers: Optional[list[str]] = None,
        depends_on: Optional[list[str]] = None,
        tags: Optional[list[str]] = None,
    ) -> None:
        """Register a new project."""
        pass

    def get_project(self, project_key: str) -> Optional[dict]:
        """Get project data."""
        pass

    def list_projects(self, status: Optional[str] = None, tag: Optional[str] = None) -> dict[str, dict]:
        """List projects with optional filtering."""
        pass

    def project_exists(self, project_key: str) -> bool:
        """Check if project is registered."""
        pass

    def update_project(self, project_key: str, **updates) -> None:
        """Update existing project."""
        pass

    def unregister_project(self, project_key: str) -> None:
        """Remove project from registry."""
        pass
```

## ProjectValidator

Validates GAIA-compliant project structure.

```python
@dataclass
class ValidationResult:
    """Result of project validation."""
    is_valid: bool
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

class ProjectValidator:
    """Validates GAIA-compliant project structure."""

    def validate(
        self,
        project_path: Path,
        check_registry: bool = True
    ) -> ValidationResult:
        """Validate project structure."""
        pass

    def validate_and_report(
        self,
        project_path: Path,
        check_registry: bool = True
    ) -> bool:
        """Validate and print formatted report."""
        pass
```

---

# CHAPTER 6: VULCAN Integration Patterns & Workflows

## Python API Integration

### Basic Usage

```python
from vulcan_forge import ProjectCreator, VulcanQuestionnaire
from vulcan_forge.questionnaire import (
    ProjectIdentity, LLMConfiguration, StreamlitConfiguration,
    GAIAIntegration, DevelopmentOptions, ProjectTypeSpecifics,
    ProjectType, LLMProvider
)

questionnaire = VulcanQuestionnaire(
    identity=ProjectIdentity(
        name="data_pipeline",
        display_name="Data Pipeline",
        project_type=ProjectType.PROCESSOR,
        description="Extract, transform, load data"
    ),
    llm_config=LLMConfiguration(
        primary_provider=LLMProvider.ANTHROPIC,
        temperature=0.5
    ),
    streamlit_config=StreamlitConfiguration(port=8501, enable_multipage=True),
    gaia_integration=GAIAIntegration(),
    dev_options=DevelopmentOptions(),
    type_specifics=ProjectTypeSpecifics(
        enable_compiler=True,
        enable_taxonomy=True,
        enable_memory_store=True
    )
)

creator = ProjectCreator()
project_path = creator.create_project(questionnaire)
```

### Batch Project Creation

Create multiple projects in a loop:

```python
projects_config = [
    {"name": "nlp_analyzer", "display_name": "NLP Analyzer",
     "project_type": ProjectType.CREATIVE, "description": "NLP analysis"},
    {"name": "data_processor", "display_name": "Data Processor",
     "project_type": ProjectType.PROCESSOR, "description": "Data processing"},
]

creator = ProjectCreator()
created_projects = []

for config in projects_config:
    try:
        questionnaire = VulcanQuestionnaire(
            identity=ProjectIdentity(
                name=config["name"],
                display_name=config["display_name"],
                project_type=ProjectType(config["project_type"]),
                description=config["description"]
            ),
            llm_config=LLMConfiguration(primary_provider=LLMProvider.ANTHROPIC),
            streamlit_config=StreamlitConfiguration(),
            gaia_integration=GAIAIntegration(),
            dev_options=DevelopmentOptions(),
            type_specifics=ProjectTypeSpecifics()
        )

        project_path = creator.create_project(questionnaire)
        created_projects.append({"name": config["name"], "path": str(project_path)})
        print(f"✓ Created: {config['name']}")

    except ValueError as e:
        print(f"✗ Failed: {config['name']} - {e}")
```

### Dynamic Configuration from JSON

```python
import json
from pathlib import Path

config_file = Path("project_config.json")
config = json.loads(config_file.read_text())

questionnaire = VulcanQuestionnaire(
    identity=ProjectIdentity(
        name=config["identity"]["name"],
        display_name=config["identity"]["display_name"],
        project_type=ProjectType(config["identity"]["project_type"]),
        description=config["identity"]["description"]
    ),
    llm_config=LLMConfiguration(
        primary_provider=LLMProvider(config["llm"]["primary_provider"]),
        temperature=config["llm"].get("temperature", 0.7)
    ),
    streamlit_config=StreamlitConfiguration(
        port=config["streamlit"].get("port", 8501),
        enable_multipage=config["streamlit"].get("multipage", True),
        theme=config["streamlit"].get("theme", "material_dark")
    ),
    gaia_integration=GAIAIntegration(**config.get("gaia", {})),
    dev_options=DevelopmentOptions(**config.get("dev_options", {})),
    type_specifics=ProjectTypeSpecifics(**config.get("type_specifics", {}))
)

creator = ProjectCreator()
project_path = creator.create_project(questionnaire)
```

## Claude Code Integration

### Project Context

Every VULCAN project includes `CLAUDE.md` with project information for Claude Code.

### Using Configuration in Claude Code

```python
from config import get_settings
from rag_intelligence import create_llm_client

settings = get_settings()

llm = create_llm_client(
    provider=settings.primary_provider,
    model=settings.anthropic_model
)

async def analyze(text: str):
    response = await llm.generate(text)
    return response
```

## CI/CD Integration

### GitHub Actions Workflow

```yaml
name: Create VULCAN Projects

on:
  push:
    paths:
      - 'projects/*.json'

jobs:
  create-projects:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - run: pip install vulcan-forge
      - run: python scripts/create_projects.py
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
      - run: python scripts/validate_projects.py
```

## Custom Workflows

### Project Factory Pattern

Create projects from predefined templates:

```python
from dataclasses import dataclass
from vulcan_forge import ProjectCreator, VulcanQuestionnaire

@dataclass
class ProjectTemplate:
    name: str
    project_type: ProjectType
    description: str
    llm_provider: LLMProvider = LLMProvider.ANTHROPIC

class ProjectFactory:
    TEMPLATES = {
        "nlp": ProjectTemplate(
            name="nlp_template",
            project_type=ProjectType.CREATIVE,
            description="NLP analysis project",
        ),
        "etl": ProjectTemplate(
            name="etl_template",
            project_type=ProjectType.PROCESSOR,
            description="ETL pipeline",
        ),
        "decision": ProjectTemplate(
            name="decision_template",
            project_type=ProjectType.DETERMINISTIC,
            description="Decision engine",
        ),
    }

    @classmethod
    def create_from_template(cls, template_name: str, custom_name: str):
        if template_name not in cls.TEMPLATES:
            raise ValueError(f"Unknown template: {template_name}")

        template = cls.TEMPLATES[template_name]
        questionnaire = VulcanQuestionnaire(
            identity=ProjectIdentity(
                name=custom_name,
                display_name=custom_name.replace("_", " ").title(),
                project_type=template.project_type,
                description=template.description
            ),
            llm_config=LLMConfiguration(primary_provider=template.llm_provider),
            streamlit_config=StreamlitConfiguration(),
            gaia_integration=GAIAIntegration(),
            dev_options=DevelopmentOptions(),
            type_specifics=ProjectTypeSpecifics()
        )

        creator = ProjectCreator()
        return creator.create_project(questionnaire)
```

### Multi-Tenant Project Creation

```python
class MultiTenantProjectCreator:
    def __init__(self, base_path: Path = Path(r"X:\Projects")):
        self.base_path = base_path
        self.creator = ProjectCreator()

    def create_user_project(
        self,
        user_id: str,
        project_name: str,
        project_type: ProjectType,
        description: str
    ) -> Path:
        user_project_name = f"{user_id}_{project_name}"

        questionnaire = VulcanQuestionnaire(
            identity=ProjectIdentity(
                name=user_project_name,
                display_name=f"{project_name} ({user_id})",
                project_type=project_type,
                description=description
            ),
            llm_config=LLMConfiguration(primary_provider=LLMProvider.ANTHROPIC),
            streamlit_config=StreamlitConfiguration(
                port=self._allocate_port(user_id)
            ),
            gaia_integration=GAIAIntegration(register_in_ecosystem=True),
            dev_options=DevelopmentOptions(),
            type_specifics=ProjectTypeSpecifics()
        )

        return self.creator.create_project(questionnaire)

    def _allocate_port(self, user_id: str) -> int:
        base_port = 8500
        port_offset = abs(hash(user_id)) % 500
        return base_port + port_offset
```

## Best Practices

1. Always validate questionnaire before creating projects
2. Check project_exists() before creating to avoid duplicates
3. Use registry for project discovery instead of filesystem
4. Validate created projects immediately after creation
5. Handle exceptions gracefully in CI/CD
6. Log all operations for debugging and audit trails
7. Test with custom configurations before production use
8. Keep configuration files version controlled
9. Document custom adapters thoroughly
10. Monitor project creation metrics and performance

---

## Troubleshooting Integration

### Debugging Project Creation

```python
import logging
from vulcan_forge import ProjectCreator

logging.basicConfig(level=logging.DEBUG)

creator = ProjectCreator()

try:
    project_path = creator.create_project(questionnaire)
except Exception as e:
    logging.error(f"Project creation failed: {e}", exc_info=True)
    raise
```

### Validating Configurations

```python
from vulcan_forge.questionnaire import VulcanQuestionnaire

try:
    questionnaire = VulcanQuestionnaire(
        identity=identity,
        llm_config=llm_config,
        # ... rest of fields
    )
    print("✓ Configuration is valid")

except ValueError as e:
    print(f"✗ Configuration error: {e}")
```

---

## References

**VULCAN Documentation Sources:**
- X:\Projects\vulcan\docs\VULCAN_GUIDE.md (v0.4.0-dev, 733 lines)
- X:\Projects\vulcan\docs\ADAPTER_GUIDE.md (v0.4.0-dev, 1,688 lines)
- X:\Projects\vulcan\docs\API_REFERENCE.md (v0.4.0-dev, 1,389 lines)
- X:\Projects\vulcan\docs\INTEGRATION_GUIDE.md (v0.4.0-dev, 1,039 lines)

**Total Consolidated:** 4,849 lines of VULCAN documentation integrated into Chapters 3-6

---

**GAIA BIBLE - Complete Operational Tier (Chapters 3-6)**
**Last Updated:** February 4, 2026
**Status:** Operational documentation fully consolidated

---

---

# APPENDIX A: GAIA Registry Schema & Format

## Registry Purpose & Location

**Location:** `X:\Projects\_gaia\registry.json`

**Purpose:** Single authoritative source of truth for all ecosystem projects

**Responsibility:** Updated by VULCAN when projects created, manually maintained for retroactive registrations

**Access:** Read by ARGUS (Phase 2), LOOM (Phase 3), WARDEN (governance), and ecosystem browsers

---

## Registry JSON Schema

### Root Structure

```json
{
  "$schema": "gaia-registry-v1",
  "updated": "2026-02-04",
  "projects": {
    "project_key": { /* project data */ }
  }
}
```

### Project Entry Fields

Each project in the registry has these fields:

```json
{
  "project_key": {
    "name": "Human-readable name",
    "path": "X:/Projects/path/to/project",
    "version": "6.2.8",
    "status": "production|development|design-only|stale|complete|archived",
    "git": true,
    "git_remote": "https://github.com/user/repo.git",
    "python": "3.9+",
    "framework": "streamlit|library|static-html|api",
    "port": 8503,
    "gaia_role": "optional: describes ecosystem role",
    "providers": ["openai", "anthropic"],
    "depends_on": ["mycel"],
    "tags": ["tag1", "tag2"]
  }
}
```

---

## Field Definitions

### name (string, required)

**Description:** Human-readable project name

**Examples:**
- `"HART OS"`
- `"VIA Intelligence"`
- `"MYCEL"`

**Note:** May differ from `project_key` (filename-safe key)

---

### path (string, required)

**Description:** Absolute file system path to project

**Format:** Use forward slashes (cross-platform compatible)

**Examples:**
- `"X:/Projects/hart_os_v6"`
- `"X:/Projects/Python tools/rag-intelligence"`
- `"X:/Projects/vulcan"`

**Validation:** Path must exist or project is considered disconnected

---

### version (string, required)

**Description:** Semantic version of the project

**Format:** MAJOR.MINOR.PATCH or dev versions

**Examples:**
- `"6.2.8"` - production
- `"0.4.0"` - stable development version
- `"0.4.0-dev"` - development pre-release
- `"0.0.0"` - design-only (no implementation)

**Convention:** VULCAN-created projects start at v0.1.0

---

### status (string, required)

**Description:** Current lifecycle status of project

**Valid Values:**
- `"production"` - Running in regular use, fully tested
- `"development"` - Active development, tests passing
- `"design-only"` - Specification complete, no code yet
- `"stale"` - Functional but not actively maintained
- `"complete"` - Finished, no further development planned
- `"archived"` - Moved to archive, no longer active
- `"planned"` - Scheduled for future development

**Examples:**
- HART OS, VIA, DATA FORGE: `"production"`
- VULCAN: `"development"`
- LOOM, ARGUS: `"planned"`
- ECHO: `"stale"`

---

### git (boolean, required)

**Description:** Whether project is under version control

**Impact:**
- `true` - Project has .git directory, committed to repository
- `false` - No version control or not initialized

**Note:** WARDEN Phase 2 will enforce `git: true` for production projects

---

### git_remote (string, optional)

**Description:** Remote repository URL

**Format:** GitHub, GitLab, or other git hosting URL

**Examples:**
- `"https://github.com/ZoeDepthTokyo/hart-os.git"`
- `null` - No remote repository

**Note:** Useful for ecosystem-wide backup/sync strategies

---

### python (string, required if applicable)

**Description:** Python version requirement

**Format:** Version range (e.g., "3.9+", "3.10-3.12")

**Examples:**
- `"3.9+"` - Python 3.9 or higher
- `"3.10+"` - Requires 3.10+
- `null` - Non-Python project

---

### framework (string, required)

**Description:** UI/execution framework used

**Valid Values:**
- `"streamlit"` - Streamlit multi-page app
- `"library"` - Python library (no UI)
- `"static-html"` - Static HTML/CSS/JS
- `"api"` - REST API (FastAPI, Flask, etc.)
- `"cli"` - Command-line interface
- `"jupyter"` - Jupyter notebooks

---

### port (integer, optional)

**Description:** Default port for local development

**Purpose:** Quick reference for running multiple services

**Examples:**
- `8501` - Streamlit default
- `8503` - VIA Intelligence
- `null` - No port (library or static)

**Convention:** Ports 8501-8599 reserved for local Streamlit apps

---

### gaia_role (string, optional)

**Description:** Describes project's role in GAIA ecosystem

**Purpose:** Clarifies how project fits into larger architecture

**Examples:**
- `"Shared Intelligence Library"` - MYCEL
- `"Project Creator (The Forge)"` - VULCAN
- `"Monitoring + Kanban (The Watchman)"` - ARGUS

**Note:** Required for GAIA core components (VULCAN, LOOM, ARGUS, MYCEL, MNEMIS, WARDEN)

---

### providers (array of strings)

**Description:** LLM providers used by project

**Valid Values:**
- `"openai"` - OpenAI (GPT models)
- `"anthropic"` - Anthropic (Claude models)
- `"gemini"` - Google Gemini
- `"local"` - Local LLM (ollama, llama.cpp)

**Examples:**
- `["openai"]` - Single provider
- `["gemini", "openai", "anthropic"]` - Multi-provider
- `[]` - No LLM integration (utility/library)

---

### depends_on (array of strings)

**Description:** Other ecosystem projects this depends on

**Purpose:** Understand project dependencies for deployment/updates

**Examples:**
- `["mycel"]` - Depends only on MYCEL
- `["mycel"]` - VIA depends on MYCEL
- `[]` - Standalone or legacy

**Convention:** Should match project_key of dependency

---

### tags (array of strings)

**Description:** Searchable tags for categorization

**Purpose:** Filter/search projects by capability or domain

**Common Tags:**
- **Capability:** `"rag"`, `"chunking"`, `"embedding"`, `"retrieval"`, `"streaming"`
- **Domain:** `"therapy"`, `"investment"`, `"data-processing"`, `"medical"`
- **Architecture:** `"deterministic-pipeline"`, `"creative-synthesis"`, `"processor"`
- **Quality:** `"production"`, `"testing"`, `"monitoring"`, `"governance"`
- **Integration:** `"gaia-core"`, `"project-creator"`, `"shared-lib"`

**Examples:**
```json
"tags": ["therapy", "deterministic-pipeline", "scoring"]
"tags": ["investment", "rag", "semantic-claims", "synthesis"]
"tags": ["gaia-core", "project-creator", "tooling"]
```

---

## Registry Operations

### Reading the Registry

```python
# Load registry
import json
from pathlib import Path

registry_path = Path("X:/Projects/_gaia/registry.json")
with open(registry_path) as f:
    registry = json.load(f)

# List all projects
for project_key, data in registry['projects'].items():
    print(f"{project_key}: {data['name']} ({data['status']})")

# Find by status
production = [p for p in registry['projects'].values() if p['status'] == 'production']

# Find by provider
openai_projects = [p for p in registry['projects'].values() if 'openai' in p['providers']]

# Find by tag
rag_projects = [p for p in registry['projects'].values() if 'rag' in p['tags']]
```

### Querying via RegistryManager

```python
from vulcan_forge.registry_manager import RegistryManager

manager = RegistryManager(Path("X:/Projects/_gaia/registry.json"))

# List all projects
all_projects = manager.list_projects()

# Get single project
project_data = manager.get_project("hart_os")

# Register new project
project_data = {
    "name": "My New Project",
    "path": "X:/Projects/my_project",
    "version": "0.1.0",
    "status": "development",
    "git": True,
    "providers": ["openai"],
    "depends_on": ["mycel"],
    "tags": ["custom", "project"]
}
manager.register_project("my_project", project_data)
```

---

## Best Practices for Registry Management

### 1. Project Key Naming

**Convention:** Lowercase, hyphen-separated, filesystem-safe

```
✅ CORRECT:
hart_os, via, data_forge, my_project, thing_v2

❌ INCORRECT:
HART OS, My-Project!, thing@v2
```

### 2. Path Consistency

**Rule:** Always use forward slashes, absolute paths

```
✅ X:/Projects/hart_os
❌ X:\Projects\hart_os
❌ /relative/path
```

### 3. Version Numbering

**Convention:** Semantic versioning (MAJOR.MINOR.PATCH)

```
Production:      6.2.8, 1.0.0
Development:     0.4.0, 0.2.1
Pre-release:     0.4.0-dev, 1.0.0-rc1
Design-only:     0.0.0
```

### 4. Status Transitions

**Valid Transitions:**

```
planned → design-only → development → production
                    ↓        ↓
                  stale    stale
                    ↓        ↓
                  archived archived
```

### 5. Tags Best Practices

- Keep tags lowercase
- Use hyphens for multi-word tags
- Limit to 5-8 tags per project
- Ensure tags are searchable and meaningful
- Document tag meanings in team documentation

### 6. Dependency Management

**Rule:** List only direct dependencies

```
✅ CORRECT: "depends_on": ["mycel"]
❌ INCORRECT: "depends_on": ["mycel", "pydantic", "openai"]
              (pydantic and openai are transitive)
```

### 7. Manual Registry Edits

**When needed:**
- Update paths when projects move
- Update versions manually if git tags lag
- Update status when project lifecycle changes
- Add missing git_remote entries

**After manual edits:**
1. Validate JSON syntax
2. Verify all paths exist
3. Commit change to _gaia repo
4. Notify ARGUS if deployed

---

## Querying Examples

### Use Case 1: Find All Production Projects

```python
production = [
    (k, v) for k, v in registry['projects'].items()
    if v['status'] == 'production'
]
# Result: HART OS, VIA, DATA FORGE
```

### Use Case 2: Find Projects Using OpenAI

```python
openai_users = [
    (k, v) for k, v in registry['projects'].items()
    if 'openai' in v.get('providers', [])
]
# Result: HART OS, VIA, DATA FORGE, MYCEL
```

### Use Case 3: Find GAIA Core Components

```python
gaia_core = [
    (k, v) for k, v in registry['projects'].items()
    if 'gaia-core' in v.get('tags', [])
]
# Result: VULCAN
```

### Use Case 4: Find Projects with Python 3.10+

```python
py310 = [
    (k, v) for k, v in registry['projects'].items()
    if v.get('python', '').startswith('3.10')
]
# Result: VIA, DATA FORGE, MYCEL, VULCAN
```

---

---

# APPENDIX B: GAIA History & Evolution

## The Pre-GAIA Era (v0.0.0) - February 3, 2026

### Fragmented Reality

**The Numbers:**
- 7+ Python AI projects running in isolation
- No shared infrastructure or standards
- 5 duplicate LLM client implementations
- 3 conflicting HART OS locations
- 3/7 projects unversioned (no git)
- Zero cross-project observability

### Technical Landscape

| System | Git | Tests | Config | LLM Clients | Location Issues |
|--------|-----|-------|--------|-------------|-----------------|
| HART OS | ✅ | ✅ 92 | JSON + dataclass | 1 (OpenAI) | 3 locations! |
| VIA | ❌ | ✅ 4 | Hand-rolled .env | 2 (Gemini, OpenAI) | Canonical |
| DATA FORGE | ❌ | ? | pydantic-settings | 1 (OpenAI) | Canonical |
| MYCEL | ❌ | ✅ 200+ | None (skeleton) | 0 (skeleton) | Canonical |
| ECHO | ❌ | ❌ | .env + hardcoded | 1 (Gemini) | Stale |

### Key Problems

**Problem 1: Location Conflict (HART OS)**
- Canonical: X:\Projects\hart_os_v6
- Copy 1: C:\Claude\reference_app (divergent)
- Copy 2: C:\hart_os_v6 (empty, deleted)
- Result: Confusion about which version is authoritative

**Problem 2: No Version Control**
- HART OS only one with git
- VIA, DATA FORGE, MYCEL unversioned
- Risk: No rollback, no history, no collaboration safety

**Problem 3: Configuration Inconsistency**
- HART OS: api_keys.json + dataclass
- VIA: Hand-rolled .env parser
- DATA FORGE: pydantic-settings (best practice)
- MYCEL: None (skeleton only)

**Problem 4: LLM Client Duplication**

5 implementations with no coordination:
1. HART OS llm_gateway.py (OpenAI, PHI filter)
2. VIA rag_adapter.py + custom (Gemini, OpenAI)
3. DATA FORGE llm_client.py (OpenAI, tiered)
4. MYCEL skeleton (non-functional)
5. ECHO gemini_client.py (Gemini)

**Problem 5: Zero Observability**
- Can't track LLM costs across projects
- No error aggregation
- No health monitoring
- No ecosystem visibility

---

## GAIA Genesis (v0.1.0) - February 3-4, 2026

### The Decision

**Statement:** "Instead of fixing fragmentation piecemeal, build a master layer that governs the entire ecosystem"

### Three Core Principles Established

1. **Glass-Box Transparency** - Never hide complexity, always explain trade-offs
2. **Pedagogical AI** - Users learn as ecosystem grows, climbing a capability ladder
3. **Thin Spine Architecture** - Minimal shared core, products pull what they need

### Naming System (Locked)

**GAIA Components (8 systems):**
- VULCAN - The Forge
- LOOM - The Workbench
- ARGUS - The Watchman
- MYCEL - The Intelligence
- MNEMIS - The Memory
- WARDEN - The Governance
- RAVEN - The Research (deferred)
- ECHO - The Archaeologist (existing, stale)

**Metaphor Strategy:**
All names tie to natural/mythological systems that govern ecosystems:
- MYCEL = mycelium (nature's neural network)
- GAIA = earth goddess (living system)
- VULCAN = forge (creation)
- LOOM = weaver of fate (modification)
- ARGUS = 100-eyed watchman (observation)

---

## Stabilization Era (v0.2.0) - February 4, 2026

### Objective: Safety Net First

**Principle:** Secure what exists before building new features

### Completed Actions

**Git Initialization (All 7 projects)**
```
Before: 3/7 versioned
After:  7/7 versioned
Impact: 100% version control coverage
```

**HART OS Location Resolution**
```
Canonical: X:\Projects\hart_os_v6
Removed:   C:\Claude\reference_app (archived)
Removed:   C:\hart_os_v6 (empty, deleted)
```

**Secrets Audit**
```
Finding: 1 OpenAI key in HART OS git history
Action:  User revokes key at OpenAI dashboard
Fix:     .gitignore properly configured going forward
```

**v0 Baseline Recorded**
- File: v0_baseline.md
- Content: Every project's state captured
- Dependencies documented
- Locations recorded
- Duplications mapped

---

## Spine Era (v0.3.0) - February 4, 2026

### Objective: Build Shared Intelligence Layer

**Decision:** Create MYCEL before VULCAN (infrastructure before features)

### MYCEL v0.2.0 Achievements

**Configuration Standardization**

```
Before: 3 approaches
After:  1 unified pattern via pydantic-settings
```

```python
# Every GAIA project now uses:
from rag_intelligence.config import GaiaSettings

class MyProjectSettings(GaiaSettings):
    # Automatically inherits:
    # - openai_api_key
    # - anthropic_api_key
    # - gemini_api_key
    # - All model defaults
    pass
```

**Unified LLM Client**

```python
# Before: 5 different implementations
# After: Single interface
from rag_intelligence.integrations import create_llm_client

client = create_llm_client(provider="openai")
response = client.complete(system="...", user="...")

# Switch providers = same code
client = create_llm_client(provider="anthropic")
response = client.complete(system="...", user="...")
```

**Core Algorithms in MYCEL**
- Chunking (configurable overlap)
- Embedding (OpenAI cached)
- Retrieval (vector similarity)
- Models (Chunk, Document, RetrievalResult)

**Test Status: 200+ tests passing**

---

## Critical Fix Era (v0.3.1) - February 4, 2026

### Issue: VIA Needed Chunk.source

**Problem:** VIA codebase had 76 locations accessing `chunk.source` property that didn't exist

**Solution:** Add to MYCEL (correct level) not VIA (consumer level)

**File:** X:\Projects\Python tools\rag-intelligence\rag_intelligence\core\models.py

**Changes:**
```python
class Chunk(BaseModel):
    # ... existing fields ...
    source: Optional[str] = None  # ✅ NEW
    timestamp: Optional[datetime] = None  # ✅ NEW
```

**Impact:**
- Unblocked 76 VIA locations
- No VIA code changes needed
- Backward compatible
- Enables time-aware retrieval

**Key Lesson:** Hierarchical fixes scale across ecosystem

---

## Forge Era (v0.4.0) - February 4, 2026

### Objective: Project Creator Operational

**Decision:** VULCAN is the gateway - all new projects created through it

### Delivered

**Core Components:**
- Framework: 3,247 LOC
- Adapters: 1,156 LOC (3 types)
- Questionnaire: 2,184 LOC (7 steps)
- UI: 687 LOC (Streamlit)
- Validators: 1,189 LOC (3-tier)
- Tests: 5,428 LOC (137 tests, 85% coverage)
- Docs: 31,000+ LOC (5 comprehensive guides)

**Total: 19,830+ lines of production code**

### Three Project Type Adapters

**DeterministicAdapter (HART-like)**
- Structured pipelines with confidence scoring
- Example: HART OS therapy assistant

**CreativeAdapter (VIA-like)**
- RAG and synthesis engines
- Example: VIA investment research

**ProcessorAdapter (DATA FORGE-like)**
- Data processing and ETL
- Example: DATA FORGE compilation

### Integration Points Ready

**MYCEL Integration**
✅ Every project uses GaiaSettings
✅ Every project calls create_llm_client()
✅ requirements.txt includes rag-intelligence>=0.2.1

**Registry Integration**
✅ New projects auto-registered
✅ Retroactive registration modes
✅ Project validation functional

**Claude Code Integration**
✅ CLAUDE.md context anchor
✅ .clproj/ template structure
✅ Pre-built prompts

---

## Version Timeline Summary

| Version | Date | Component | Status | LOC |
|---------|------|-----------|--------|-----|
| v0.0.0 | Feb 3 | Baseline | Complete | N/A |
| v0.1.0 | Feb 3-4 | Genesis | Complete | Design |
| v0.2.0 | Feb 4 | Stabilization | Complete | 0 |
| v0.3.0 | Feb 4 | MYCEL Spine | Complete | 4,450 |
| v0.3.1 | Feb 4 | Chunk.source Fix | Complete | 50 |
| v0.4.0 | Feb 4 | VULCAN | Complete | 19,830 |
| v0.5.0 | TBD | ARGUS (Phase 2) | Planned | 10,000+ |
| v1.0.0 | TBD | LOOM + MNEMIS (Phase 3) | Planned | 30,000+ |

---

## Lessons Learned

### What Worked

1. **Thin Spine Principle** - Infrastructure stayed minimal
2. **Naming System** - Mythological metaphors made architecture memorable
3. **Version Discipline** - Each version had specific objective
4. **Documentation First** - Architecture designed before code
5. **Test-Driven** - Tests written with code, not after

### What Nearly Failed

1. **HART OS Duplication** - Location conflict almost caused data loss
2. **No Version Control** - VIA, DATA FORGE nearly lost history
3. **Secrets Exposure** - Discovered OpenAI key in git history
4. **LLM Client Duplication** - 5 implementations only discovered during Phase 0.5

### Sacred Rules

1. Don't create infrastructure without products to use it
2. Don't assume projects know about shared capabilities
3. Don't skip version control "for now"
4. Don't hide API keys in git history
5. Don't create duplicate implementations without consolidation

---

---

# APPENDIX C: Phase Completion Reports

## Phase 0: Stabilization

**Date:** February 4, 2026 | **Status:** COMPLETE

### Deliverables

- [x] Git initialized on all 7 projects
- [x] HART OS location unified to X:\Projects\hart_os_v6
- [x] Secrets audit complete (1 key in history, user action required)
- [x] v0 baseline recorded (v0_baseline.md)

### Success Criteria: MET

Phase 0 unblocks Phase 0.5 without risk to existing projects.

---

## Phase 0.5: MYCEL Spine

**Date:** February 4, 2026 | **Status:** COMPLETE

### Deliverables

- [x] GaiaSettings (pydantic-settings base class)
- [x] Unified LLM client (OpenAI, Anthropic, Gemini)
- [x] Core algorithms (chunking, embedding, retrieval)
- [x] Public API documented
- [x] 200+ tests passing
- [x] Chunk.source critical fix (v0.3.1)

### Integration Readiness

- ✅ MYCEL v0.2.1 stable
- ✅ All major components functional
- ✅ Backward compatible
- ✅ Ready for VULCAN to consume

### Success Criteria: MET

MYCEL is stable and ready to serve as infrastructure for VULCAN.

---

## Phase 1: VULCAN - The Forge

**Date:** February 4, 2026 | **Status:** COMPLETE

### Deliverables Summary

| Category | Files | LOC | Tests | Status |
|----------|-------|-----|-------|--------|
| Framework | 8 | 3,247 | Core | ✅ |
| Adapters | 4 | 1,156 | 31 | ✅ |
| Questionnaire | 8 | 2,184 | 28 | ✅ |
| UI | 1 | 687 | N/A | ✅ |
| Validators | 3 | 1,189 | 19 | ✅ |
| Tests | 19 | 5,428 | 137 | ✅ |
| Documentation | 5 | 31,000+ | N/A | ✅ |
| **TOTAL** | **39** | **19,830+** | **137** | **✅** |

### Test Coverage

```
Questionnaire:       28 tests (92% coverage)
Adapters:           31 tests (88% coverage)
Configuration:      23 tests (85% coverage)
Project Builder:    26 tests (83% coverage)
Validators:         19 tests (89% coverage)
Integrations:       18 tests (76% coverage)
────────────────────────────────────────
TOTAL:             137 tests (85% coverage)
Status:            ALL PASSING ✅
```

### Integration Contracts Ready

**VULCAN Creates:**
- ✅ logs/ directory for Phase 2 telemetry
- ✅ CLAUDE.md context anchor
- ✅ Standard GAIA structure
- ✅ Registry entry
- ✅ MYCEL integration (GaiaSettings)

**ARGUS Can Rely On:**
- ✅ X:\Projects\_gaia\registry.json
- ✅ X:\Projects\{project}\logs\*.jsonl
- ✅ X:\Projects\{project}\CLAUDE.md
- ✅ X:\Projects\{project}\config.py

### Success Criteria: MET

- ✅ 19,830 lines delivered
- ✅ 137 tests passing (85% coverage)
- ✅ 31,000+ lines documentation
- ✅ Phase 2 ready to begin

---

## Phase 2: ARGUS - The Watchman (Planned)

**Status:** Ready to begin

### Planned Scope

**Telemetry Layer (MYCEL)**
- Location: rag_intelligence/telemetry/
- Methods: log_llm_call, log_error, log_event, log_agent_step
- Output: JSONL to X:\Projects\_gaia\logs\{project}\{date}.jsonl

**ARGUS Dashboard (Streamlit)**
- Location: X:\Projects\_gaia\argus\
- Pages: Ecosystem View, Cost Tracker, Error Feed, Execution Board, Project Watcher

**WARDEN Governance**
- Location: X:\Projects\_gaia\warden\
- Validates: Git, tests, secrets, dependencies, documentation

### Dependencies Satisfied

- ✅ MYCEL stable (v0.2.1)
- ✅ VULCAN creates Phase 2-ready projects
- ✅ Registry operational
- ✅ Standard project structure enforced

### Estimated Timeline

4-6 weeks for Phase 2 completion

---

## Phase 3: LOOM + MNEMIS (Complete - v1.0.0)

**Status:** Operational (Feb 4, 2026)

### Components Delivered

**LOOM - Workflow Engine**
- Agent authority system (levels 0-4)
- Workflow state management
- Memory-aware execution
- Integration with ARGUS mental models

**MNEMIS - Memory Hierarchy**
- 5-tier memory system (Ephemeral → Permanent)
- Memory contracts with runtime enforcement
- Promotion protocol with criteria validation
- Cross-project memory sharing
- JSONL persistence for long-term/permanent tiers

### Implementation Summary

**Code Delivered:**
- ~3,570 lines of implementation
- ~4,670 lines of documentation
- Memory manager with tier-based access
- Workflow engine with agent authority
- Thread-safe memory operations
- Automatic expiration handling

**Key Features:**
- Agents cannot write above their authority tier
- Memory promotion requires validated criteria
- Cross-tier reads allowed (hierarchical)
- Integration with ARGUS mental model selection
- Glass-box explainability for all operations

### Integration

LOOM workflow engine coordinates agent execution
MNEMIS enforces memory contracts at runtime
ARGUS provides mental models for reasoning
Full loop: Create (VULCAN) → Execute (LOOM) → Remember (MNEMIS) → Reason (ARGUS)

### Completion Date

Completed February 4, 2026 (v1.0.0)

---

---

# APPENDIX D: Coordination & Cross-Project Records

## Coordination Philosophy

**Goal:** Transparent hierarchical coordination with minimal friction

**Rule:** Fixes belong at correct architectural level

**Example:** When VIA needed Chunk.source, fix went to MYCEL (library), not VIA (consumer). All consumers now benefit automatically.

---

## Key Coordinations Completed

### 1. MYCEL Chunk.source Fix (v0.3.1)

**Parties:** GAIA Ecosystem Team ← → VIA Team

**Issue:** 76 VIA locations accessing non-existent `chunk.source`

**Solution:** Add to MYCEL Chunk model

**Impact:**
- ✅ VIA unblocked
- ✅ No VIA code changes needed
- ✅ Backward compatible
- ✅ Hierarchically correct

---

### 2. VIA v6.4 Integration

**Parties:** VIA-Fixer ← → GAIA Ecosystem

**Completed:**
- [x] Query synthesis unblocked (source field added)
- [x] Cost reduction (61% savings via model optimization)
- [x] Graph integration enhanced
- [x] Evolution PDF generation implemented

**Files Modified:** 6 files, ~150 LOC changes

**Status:** ✅ Ready for pipeline validation

---

### 3. Phase 1 → Phase 2 Handoff

**Date:** February 4, 2026

**From:** VULCAN Complete (Phase 1)
**To:** ARGUS Ready (Phase 2)

**VULCAN Guarantees:**
- ✅ logs/ directory for telemetry
- ✅ CLAUDE.md with context
- ✅ Standard GAIA structure
- ✅ Registry entry
- ✅ MYCEL integration

**ARGUS Can Rely On:**
- ✅ Registry operational
- ✅ Project locations known
- ✅ Configuration standardized
- ✅ Telemetry hooks in place

---

### 4. Phase 2 & 3 Completion (v0.5.0 & v1.0.0)

**Date:** February 4, 2026

**Parties:** GAIA Core Team

**Phase 2 Delivered (ARGUS v0.5.0):**
- ✅ Mental Model Library (59 models, 6 categories)
- ✅ Context-aware model selection algorithm
- ✅ Layered explainability (4 levels)
- ✅ Growth Rung mapping (Rungs 1-4)
- ✅ GAIA Subconscious (external memory, pattern detection)
- ✅ HART OS therapeutic framework integration points

**Phase 3 Delivered (LOOM/MNEMIS v1.0.0):**
- ✅ MNEMIS memory hierarchy (5 tiers)
- ✅ Memory contracts with runtime enforcement
- ✅ Memory promotion protocol
- ✅ LOOM workflow engine
- ✅ Agent authority system (levels 0-4)
- ✅ Cross-project memory sharing
- ✅ Glass-box explainability integration

**Implementation Stats:**
- 66 files committed
- ~6,770 lines implementation
- ~9,170 lines documentation
- ~15,940 total lines

**Impact:**
- Complete GAIA ecosystem architecture operational
- Mental models enable context-aware reasoning
- Memory hierarchy enforces knowledge management discipline
- Workflow engine coordinates multi-agent execution
- Cross-project learning now possible via MNEMIS

**Status:** ✅ Phases 2 & 3 complete, ready for production integration

---

## Inter-Project Dependency Matrix

### Current Dependencies

```
HART OS
├── Depends: (none, standalone)
├── Integration: ARGUS (mental models, explainability)
└── Used by: (reference)

VIA
├── Depends: MYCEL (rag_adapter.py)
├── Integration: ARGUS (mental models), MNEMIS (cross-project memory)
└── Used by: (reference)

DATA FORGE
├── Depends: (none, standalone)
└── Used by: (reference)

MYCEL
├── Depends: (none, base library)
└── Used by: VIA, VULCAN, ARGUS, LOOM

VULCAN
├── Depends: MYCEL (config, LLM clients)
└── Used by: (creates projects)

ARGUS (Mental Models + Subconscious)
├── Depends: MYCEL (configuration)
├── Integrates with: HART OS, VIA, LOOM
└── Provides: Mental models, explainability, pattern detection

LOOM (Workflow Engine)
├── Depends: MYCEL, ARGUS (mental models), MNEMIS
└── Provides: Agent coordination, workflow execution

MNEMIS (Memory Hierarchy)
├── Depends: MYCEL
├── Integrates with: LOOM, ARGUS
└── Provides: Cross-project memory, promotion protocol
```

---

## Coordination Best Practices

### Rule 1: Correct Architectural Level

```
❌ Wrong: Fix in consumer
✅ Right: Fix in shared library
Result: All consumers benefit automatically
```

### Rule 2: Version Discipline

When component changes:
1. Update version (semver)
2. Document in VERSION_LOG.md
3. Update registry
4. Notify dependents

### Rule 3: Registry as Source of Truth

All coordination flows through registry:
- Who depends on what?
- What versions deployed?
- What's production vs development?
- Who uses which providers?

### Rule 4: Documentation is Coordination

Every change documented:
- WHY (business case)
- WHERE (file, lines)
- WHEN (date, session)
- WHO (team)
- WHAT (impact analysis)

### Rule 5: Transparent Handoffs

Never hide:
- Design decisions
- Known limitations
- User action items
- Integration dependencies
- Deployment instructions

---

---

# INDEX & NAVIGATION

## Alphabetical Quick Reference

**Adapters** - Chapter 2, Layer 4 / Chapters 4-5 / Appendix A
**ARGUS** - Chapter 0, Phase 2 Planned / Appendix C
**Baseline** - Appendix B, v0.0.0
**CLAUDE.md** - Chapter 2, Critical Files / Chapter 3-6
**Config.py** - Chapter 2, Layer 3 / Chapter 5
**Dependencies** - Appendix D, Matrix
**Deterministic** - Chapter 2, Layer 4 / Chapter 4
**ECHO** - Chapter 0, Stale
**GAIA Bible** - This Document
**GaiaSettings** - Chapter 2, Layer 1 / Chapter 5
**Glass-Box** - Chapter 1, Principles
**HART OS** - Chapter 0, Production
**Integration** - Chapter 2, Contracts
**LOOM** - Chapter 0, Phase 3 Planned / Appendix C
**MYCEL** - Chapter 0, 2, Appendix B
**Registry** - Chapter 2, Layer 2 / Appendix A
**Registry Operations** - Appendix A, Operations
**Spine, Thin** - Chapter 2, Architecture
**Three Pillars** - Chapter 0
**VIA** - Chapter 0, Production / Appendix D
**VULCAN** - Chapter 0, Phase 1 Complete / Chapters 3-6
**Warden** - Chapter 0, Phase 2

---

## Quick Reference by User Role

### For Creators
1. Chapter 0 - Overview
2. Chapters 3-6 - VULCAN usage
3. Appendix A - Registry schema
**Time:** 30-45 minutes to productivity

### For Developers
1. Chapter 2 - Architecture
2. Chapters 4-6 - Integration patterns
3. Appendix D - Coordination
**Time:** 60-90 minutes to understand system

### For DevOps
1. Chapter 0 - Status
2. Appendix A - Registry operations
3. Appendix D - Coordination
**Time:** 45-60 minutes for operational knowledge

### For Architects
1. Chapters 0-2 - Foundation
2. Appendices B-D - History and coordination
3. Chapters 4-5 - Extension patterns
**Time:** 2-3 hours for system design

---

## Quick Glossary

**Adapter:** Custom project type (Deterministic/Creative/Processor)
**ARGUS:** Phase 2 monitoring system
**Baseline:** Pre-GAIA snapshot (v0.0.0)
**Config.py:** GaiaSettings subclass per project
**Deterministic:** HART-like pipelines with scoring
**GAIA:** Generative AI Adaptation Initiative
**GaiaSettings:** Pydantic config base class
**Integration Contract:** Guarantee between components
**Metadata:** Project information in registry
**MYCEL:** Shared intelligence library (spine)
**Phase 0:** Stabilization (git, secrets, baseline)
**Phase 0.5:** Spine (MYCEL config & LLM clients)
**Phase 1:** VULCAN project creator
**Phase 2:** ARGUS monitoring
**Phase 3:** LOOM visual editor + MNEMIS memory
**Registry:** JSON file listing all projects
**Telemetry:** Structured logging of LLM calls
**Three Pillars:** VULCAN creates → LOOM edits → ARGUS monitors
**Thin Spine:** Minimal infrastructure, products pull what needed
**Version Discipline:** Semantic versioning (MAJOR.MINOR.PATCH)
**VULCAN:** The Forge - project creator

---

## Navigation Guide

### Reading Sequences

**First-Time (45 min):**
1. Chapter 0 - Status & Vision
2. Chapter 1 - Problem & Solution
3. Skim Chapter 2 - Architecture

**Creator (60 min):**
1. Chapter 0 - Overview
2. Chapters 3-6 - Project Creation
3. Appendix A - Registry schema

**Developer (90 min):**
1. Chapter 2 - Architecture
2. Chapters 4-6 - Integration patterns
3. Appendix D - Coordination

**Architect (120 min):**
1. Chapters 0-2 - Foundation
2. Appendices B-D - History
3. Chapters 4-5 - Extension patterns

---

## Document Map

**Foundation Tier (Chapters 0-2):**
- Philosophy and principles
- Architecture and design
- Strategic direction

**Operational Tier (Chapters 3-6):**
- User guides and walkthroughs
- API references
- Integration patterns

**Reference Tier (Appendices A-D + Index):**
- Registry schema and operations
- History and evolution
- Phase completion reports
- Coordination records
- Navigation and glossary

---

---

## Final Notes

**GAIA Bible Version:** v0.4.0
**Status:** Phase 1 Complete ✅
**Next Update:** When Phase 2 begins

**This document is:**
- Constitutional guide for ecosystem
- Source of truth for all decisions
- Learning resource for progression
- Coordination hub for teams

**Sacred Principles (Do Not Compromise):**
1. Glass-Box Transparency
2. Pedagogical Growth
3. Hierarchical Architecture
4. Registry as Source of Truth
5. Documentation is Sacred

**Maintenance:**
- Update at every phase completion
- Add sections as ecosystem grows
- Keep architecture decisions visible
- Document all coordination

---

*GAIA Bible: The constitutional document of an ecosystem where creativity meets structure, where transparency builds trust, and where users grow from creators to architects.*

*This is not a reference manual. This is a living constitution. Read it, question it, extend it, and one day, you will help write the next chapter.*
