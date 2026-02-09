# GAIA User Flows — Complete Interaction Patterns

**Version:** 1.0.0
**Date:** February 8, 2026
**Status:** Reference Documentation
**Audience:** Product managers, developers, system architects, UX designers

---

## Table of Contents

1. [Flow 1: GAIA Creating a New Project (via VULCAN)](#flow-1-gaia-creating-a-new-project-via-vulcan)
2. [Flow 2: Editing an Existing Project via ABIS](#flow-2-editing-an-existing-project-via-abis)
3. [Flow 3: Product Evolution Flow](#flow-3-product-evolution-flow)
4. [Flow 4: Python Tools Governance Flow](#flow-4-python-tools-governance-flow)
5. [Flow 5: RAVEN Research Flow](#flow-5-raven-research-flow)
6. [Services Interaction Summary](#services-interaction-summary)

---

## Flow 1: GAIA Creating a New Project (via VULCAN)

### Overview
This flow demonstrates how a user creates a completely new project from scratch using VULCAN. Every shared service interaction is shown, from initial intent to running project with full telemetry.

### Complete Flow Diagram

```
USER INTENT: "I want to build a customer sentiment analyzer"
     │
     │ (User navigates to localhost:8501)
     │
     ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ STEP 1: VULCAN — The Forge (Project Creation)                              │
│ Location: X:\Projects\_GAIA\_VULCAN\vulcan_forge\project_creator.py        │
│                                                                             │
│ WHAT USER SEES:                                                             │
│   Streamlit UI: "Welcome to VULCAN — The Forge"                            │
│   7-step HITL questionnaire form displayed                                  │
│                                                                             │
│ USER INTERACTION:                                                           │
│   Step 1: "What does this project do?"                                      │
│   → User: "Analyze customer reviews for sentiment and themes"               │
│                                                                             │
│   Step 2: "Which LLM providers will you use?"                               │
│   → User: [✓] OpenAI  [✓] Anthropic  [ ] Gemini                            │
│                                                                             │
│   Step 3: "What's your project type?"                                       │
│   → User: "Creative" (needs nuanced understanding, not deterministic)       │
│                                                                             │
│   Step 4: "Do you need automated testing?"                                  │
│   → User: "Yes" (production-grade quality)                                  │
│                                                                             │
│   Step 5: "Documentation level?"                                            │
│   → User: "Full" (comprehensive docs, team collaboration)                   │
│                                                                             │
│   Step 6: "What are your data sources?"                                     │
│   → User: "CSV files, REST APIs"                                            │
│                                                                             │
│   Step 7: "Deployment target?"                                              │
│   → User: "Cloud" (AWS/GCP deployment planned)                              │
│                                                                             │
│ WHAT HAPPENS BEHIND THE SCENES:                                             │
│   def select_adapter(questionnaire: Dict) -> ProjectAdapter:               │
│       # Analyzes answers 1-7                                                │
│       if questionnaire["project_type"] == "Creative":                       │
│           return CreativeAdapter()  # Uses Sonnet for reasoning             │
│       elif questionnaire["project_type"] == "Deterministic":                │
│           return DeterministicAdapter()  # Pipeline-based                   │
│       else:                                                                 │
│           return ProcessorAdapter()  # Data-heavy workflows                 │
│                                                                             │
│   selected_adapter = CreativeAdapter()                                      │
│   project_name = "sentiment-analyzer"                                       │
│   project_path = "X:/Projects/sentiment-analyzer"                           │
│                                                                             │
│ VULCAN STATE:                                                               │
│   questionnaire_complete = True                                             │
│   adapter_selected = CreativeAdapter                                        │
│   providers = ["openai", "anthropic"]                                       │
│   requires_testing = True                                                   │
│   documentation_level = "full"                                              │
└─────────────────┬───────────────────────────────────────────────────────────┘
                  │
                  │ VULCAN → MYCEL: "I need LLM client configuration"
                  ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ STEP 2: MYCEL — Shared Intelligence (LLM + Config)                         │
│ Location: X:\Projects\_GAIA\_MYCEL\rag_intelligence\                       │
│                                                                             │
│ WHAT USER SEES:                                                             │
│   Progress indicator: "Configuring LLM clients... [##########] 100%"        │
│                                                                             │
│ WHAT HAPPENS BEHIND THE SCENES:                                             │
│   VULCAN calls MYCEL integration:                                           │
│                                                                             │
│   from rag_intelligence.config import GaiaSettings                          │
│   from rag_intelligence.llm import create_llm_client                        │
│                                                                             │
│   # Generate project-specific settings subclass                             │
│   class SentimentAnalyzerSettings(GaiaSettings):                            │
│       """Configuration for sentiment-analyzer project."""                   │
│                                                                             │
│       # OpenAI Configuration                                                │
│       openai_model: str = "gpt-4o"                                          │
│       openai_model_fast: str = "gpt-4o-mini"                                │
│                                                                             │
│       # Anthropic Configuration                                             │
│       anthropic_model: str = "claude-sonnet-4-5-20250929"                   │
│       anthropic_model_fast: str = "claude-haiku-4-5-20251001"               │
│                                                                             │
│       # Project-specific                                                    │
│       max_monthly_budget_usd: float = 50.0                                  │
│       enable_prompt_cache: bool = True                                      │
│                                                                             │
│   # Generate .env template                                                  │
│   .env.example file created:                                                │
│   ┌─────────────────────────────────────────────────┐                       │
│   │ # LLM Provider API Keys                         │                       │
│   │ OPENAI_API_KEY=sk-...                           │                       │
│   │ ANTHROPIC_API_KEY=sk-ant-...                    │                       │
│   │                                                  │                       │
│   │ # Project Configuration                         │                       │
│   │ MAX_MONTHLY_BUDGET_USD=50.0                     │                       │
│   │ ENABLE_PROMPT_CACHE=true                        │                       │
│   └─────────────────────────────────────────────────┘                       │
│                                                                             │
│   # Generate config.py with MYCEL integration                               │
│   src/sentiment_analyzer/config.py:                                         │
│   ┌─────────────────────────────────────────────────┐                       │
│   │ from rag_intelligence.config import GaiaSettings│                       │
│   │                                                  │                       │
│   │ class Settings(GaiaSettings):                   │                       │
│   │     """Inherits MYCEL's unified config."""      │                       │
│   │     pass                                         │                       │
│   │                                                  │                       │
│   │ settings = Settings()                            │                       │
│   └─────────────────────────────────────────────────┘                       │
│                                                                             │
│   # Generate LLM client factory                                             │
│   src/sentiment_analyzer/llm_client.py:                                     │
│   ┌─────────────────────────────────────────────────┐                       │
│   │ from rag_intelligence.llm import (              │                       │
│   │     create_llm_client,                          │                       │
│   │     LLMProvider                                 │                       │
│   │ )                                                │                       │
│   │                                                  │                       │
│   │ def get_sentiment_client():                     │                       │
│   │     return create_llm_client(                   │                       │
│   │         provider=LLMProvider.ANTHROPIC,         │                       │
│   │         model="claude-sonnet-4-5-20250929"      │                       │
│   │     )                                            │                       │
│   └─────────────────────────────────────────────────┘                       │
│                                                                             │
│ MYCEL PROVIDED:                                                             │
│   [✓] LLM client factory (unified interface across OpenAI/Anthropic)        │
│   [✓] GaiaSettings subclass with provider configs                           │
│   [✓] .env template for API key management                                  │
│   [✓] RAG intelligence library access (chunking, embedding, retrieval)      │
│   [✓] Budget enforcement hooks                                              │
└─────────────────┬───────────────────────────────────────────────────────────┘
                  │
                  │ VULCAN → WARDEN: "Validate project spec against rules"
                  ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ STEP 3: WARDEN — Governance & Validation                                   │
│ Location: X:\Projects\_GAIA\_WARDEN\ (planned implementation)              │
│                                                                             │
│ WHAT USER SEES:                                                             │
│   Progress indicator: "Validating project configuration... [####] 40%"      │
│                                                                             │
│ WHAT HAPPENS BEHIND THE SCENES:                                             │
│   WARDEN validates against GAIA constitutional principles:                  │
│                                                                             │
│   def validate_project_spec(spec: ProjectSpec) -> ValidationResult:        │
│       checks = [                                                            │
│           check_no_hardcoded_secrets(spec),                                 │
│           check_test_coverage_config(spec),                                 │
│           check_gitignore_includes_env(spec),                               │
│           check_absolute_imports_enforced(spec),                            │
│           check_mycel_integration_present(spec),                            │
│           check_argus_telemetry_hooks(spec),                                │
│       ]                                                                     │
│                                                                             │
│       return ValidationResult(                                              │
│           passed=all(checks),                                               │
│           violations=[c for c in checks if not c.passed]                    │
│       )                                                                     │
│                                                                             │
│ VALIDATION CHECKS PERFORMED:                                                │
│   [✓] No API keys in project files                                          │
│   [✓] .env files excluded from git (.gitignore configured)                  │
│   [✓] pytest configured for 80%+ coverage requirement                       │
│   [✓] MYCEL integration properly configured                                 │
│   [✓] ARGUS telemetry hooks registered                                      │
│   [✓] Absolute imports enforced (no relative imports)                       │
│   [✓] Type hints required on all function signatures                        │
│                                                                             │
│ WARDEN OUTPUT:                                                              │
│   validation_result = ValidationResult(                                     │
│       passed=True,                                                          │
│       violations=[],                                                        │
│       warnings=[]                                                           │
│   )                                                                         │
└─────────────────┬───────────────────────────────────────────────────────────┘
                  │
                  │ VULCAN: "Register project in GAIA registry"
                  ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ STEP 4: Registry Registration                                              │
│ Location: X:\Projects\_GAIA\registry.json                                  │
│                                                                             │
│ WHAT USER SEES:                                                             │
│   Progress indicator: "Registering project... [######] 60%"                 │
│                                                                             │
│ WHAT HAPPENS BEHIND THE SCENES:                                             │
│   VULCAN updates registry.json with new project entry:                      │
│                                                                             │
│   registry = load_registry("X:/Projects/_GAIA/registry.json")              │
│   registry["projects"]["sentiment_analyzer"] = {                            │
│       "name": "Sentiment Analyzer",                                         │
│       "path": "X:/Projects/sentiment-analyzer",                             │
│       "version": "0.1.0",                                                   │
│       "status": "development",                                              │
│       "git": True,                                                          │
│       "git_remote": None,                                                   │
│       "python": "3.10+",                                                    │
│       "framework": "streamlit",                                             │
│       "port": None,                                                         │
│       "providers": ["openai", "anthropic"],                                 │
│       "depends_on": ["mycel", "mnemis", "argus"],                           │
│       "tags": [                                                             │
│           "product",                                                        │
│           "sentiment-analysis",                                             │
│           "nlp",                                                            │
│           "creative-adapter"                                                │
│       ]                                                                     │
│   }                                                                         │
│   save_registry(registry)                                                   │
│                                                                             │
│ REGISTRY STATE:                                                             │
│   Total projects: 14 (was 13)                                               │
│   New project ID: "sentiment_analyzer"                                      │
│   Dependencies tracked: MYCEL, MNEMIS, ARGUS                                │
└─────────────────┬───────────────────────────────────────────────────────────┘
                  │
                  │ VULCAN: "Generate project CLAUDE.md"
                  ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ STEP 5: CLAUDE.md Generation                                               │
│ Location: X:\Projects\sentiment-analyzer\.claude\CLAUDE.md                 │
│                                                                             │
│ WHAT USER SEES:                                                             │
│   Progress indicator: "Generating project instructions... [########] 80%"   │
│                                                                             │
│ WHAT HAPPENS BEHIND THE SCENES:                                             │
│   VULCAN generates custom CLAUDE.md from template:                          │
│   (See project_creator.py:581-647 for full implementation)                  │
│                                                                             │
│   def generate_claude_md(adapter: CreativeAdapter) -> str:                  │
│       template = load_template("templates/claude_md_creative.jinja2")       │
│       return template.render(                                               │
│           project_name="Sentiment Analyzer",                                │
│           project_type="Creative",                                          │
│           framework="Streamlit",                                            │
│           providers=["OpenAI", "Anthropic"],                                │
│           gaia_dependencies=["MYCEL", "MNEMIS", "ARGUS"],                   │
│           testing_required=True,                                            │
│           documentation_level="full"                                        │
│       )                                                                     │
│                                                                             │
│ GENERATED CLAUDE.md CONTENTS:                                               │
│   ┌───────────────────────────────────────────────────┐                     │
│   │ # Sentiment Analyzer - Project Instructions       │                     │
│   │                                                    │                     │
│   │ ## Project Overview                               │                     │
│   │ Creative sentiment analysis system using          │                     │
│   │ nuanced LLM reasoning for customer reviews.       │                     │
│   │                                                    │                     │
│   │ ## Tech Stack                                      │                     │
│   │ - Framework: Streamlit                            │                     │
│   │ - LLM: OpenAI, Anthropic (via MYCEL)              │                     │
│   │ - Testing: pytest (80%+ coverage)                 │                     │
│   │ - Memory: MNEMIS integration                       │                     │
│   │ - Telemetry: ARGUS event emission                 │                     │
│   │                                                    │                     │
│   │ ## Code Standards                                  │                     │
│   │ - Absolute imports only                           │                     │
│   │ - Type hints on all functions                     │                     │
│   │ - Docstrings on public functions                  │                     │
│   │ - No hardcoded secrets                            │                     │
│   │                                                    │                     │
│   │ ## GAIA Integration                                │                     │
│   │ - Use MYCEL for all LLM calls                     │                     │
│   │ - Emit telemetry to ARGUS                         │                     │
│   │ - Store patterns in MNEMIS                        │                     │
│   └───────────────────────────────────────────────────┘                     │
└─────────────────┬───────────────────────────────────────────────────────────┘
                  │
                  │ VULCAN: "Generate project scaffold"
                  ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ STEP 6: Project Scaffold Creation                                          │
│ Location: X:\Projects\sentiment-analyzer\                                  │
│                                                                             │
│ WHAT USER SEES:                                                             │
│   Progress indicator: "Creating project structure... [##########] 100%"     │
│   File tree displayed in UI:                                                │
│                                                                             │
│   sentiment-analyzer/                                                       │
│   ├── .claude/                                                              │
│   │   └── CLAUDE.md                     (project-specific instructions)     │
│   ├── .github/                                                              │
│   │   └── workflows/                                                        │
│   │       └── ci.yml                    (pytest, ruff, coverage checks)     │
│   ├── src/                                                                  │
│   │   └── sentiment_analyzer/                                               │
│   │       ├── __init__.py                                                   │
│   │       ├── config.py                 (GaiaSettings subclass)             │
│   │       ├── llm_client.py             (MYCEL integration)                 │
│   │       ├── models.py                 (Pydantic schemas)                  │
│   │       ├── services/                                                     │
│   │       │   ├── __init__.py                                               │
│   │       │   ├── sentiment_service.py  (business logic)                    │
│   │       │   └── telemetry.py          (ARGUS integration)                 │
│   │       ├── ui/                                                           │
│   │       │   ├── __init__.py                                               │
│   │       │   └── streamlit_app.py      (UI components)                     │
│   │       └── utils/                                                        │
│   │           ├── __init__.py                                               │
│   │           └── helpers.py                                                │
│   ├── tests/                                                                │
│   │   ├── __init__.py                                                       │
│   │   ├── conftest.py                   (pytest fixtures)                   │
│   │   ├── test_sentiment_service.py                                         │
│   │   └── test_integration.py                                               │
│   ├── docs/                                                                 │
│   │   ├── ARCHITECTURE.md                                                   │
│   │   ├── API.md                                                            │
│   │   └── USER_GUIDE.md                                                     │
│   ├── .env.example                      (API key template)                  │
│   ├── .gitignore                        (.env excluded)                     │
│   ├── pyproject.toml                    (dependencies)                      │
│   ├── pytest.ini                        (80% coverage enforced)             │
│   ├── README.md                                                             │
│   └── requirements.txt                                                      │
│                                                                             │
│ WHAT HAPPENS BEHIND THE SCENES:                                             │
│   def create_scaffold(project_path: Path, adapter: CreativeAdapter):        │
│       # Create directory structure                                          │
│       for dir_path in adapter.get_directory_structure():                    │
│           dir_path.mkdir(parents=True, exist_ok=True)                       │
│                                                                             │
│       # Generate files from templates                                       │
│       for template_name, output_path in adapter.get_file_templates():       │
│           content = render_template(template_name, context)                 │
│           write_file(output_path, content)                                  │
│                                                                             │
│       # Initialize git repository                                           │
│       subprocess.run(["git", "init"], cwd=project_path)                     │
│       subprocess.run(["git", "add", "."], cwd=project_path)                 │
│       subprocess.run([                                                      │
│           "git", "commit", "-m",                                            │
│           "Initial commit via VULCAN"                                       │
│       ], cwd=project_path)                                                  │
│                                                                             │
│ KEY FILES GENERATED:                                                        │
│   [✓] config.py with MYCEL GaiaSettings inheritance                         │
│   [✓] llm_client.py with create_llm_client imports                          │
│   [✓] telemetry.py with ARGUS event emission                                │
│   [✓] pytest.ini with 80% coverage requirement                              │
│   [✓] .gitignore excluding .env files                                       │
│   [✓] pyproject.toml with MYCEL dependency                                  │
└─────────────────┬───────────────────────────────────────────────────────────┘
                  │
                  │ VULCAN → ARGUS: "Register project for telemetry"
                  ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ STEP 7: ARGUS — Telemetry Setup                                            │
│ Location: X:\Projects\_GAIA\_ARGUS\                                        │
│                                                                             │
│ WHAT USER SEES:                                                             │
│   Console output: "Telemetry configured for sentiment_analyzer"             │
│   "Event stream: sentiment_analyzer.jsonl created"                          │
│                                                                             │
│ WHAT HAPPENS BEHIND THE SCENES:                                             │
│   ARGUS creates telemetry infrastructure:                                   │
│                                                                             │
│   def register_project_telemetry(project_id: str) -> TelemetryConfig:      │
│       config = TelemetryConfig(                                             │
│           project_id=project_id,                                            │
│           event_stream_path=(                                               │
│               f"X:/Projects/_GAIA/_ARGUS/streams/"                          │
│               f"{project_id}.jsonl"                                         │
│           ),                                                                │
│           mental_models_enabled=True,                                       │
│           cost_tracking_enabled=True,                                       │
│           subconscious_detection_enabled=True                               │
│       )                                                                     │
│                                                                             │
│       # Create event stream file                                            │
│       create_event_stream(config.event_stream_path)                         │
│                                                                             │
│       # Register with event bus                                             │
│       event_bus.register_project(project_id, config)                        │
│                                                                             │
│       return config                                                         │
│                                                                             │
│ TELEMETRY INFRASTRUCTURE CREATED:                                           │
│   [✓] Event stream file: sentiment_analyzer.jsonl                           │
│   [✓] Cost tracking database initialized                                    │
│   [✓] Mental model library linked (59 models available)                     │
│   [✓] Subconscious pattern detector configured                              │
│   [✓] Event bus subscription registered                                     │
│                                                                             │
│ GENERATED TELEMETRY CODE:                                                   │
│   src/sentiment_analyzer/services/telemetry.py:                             │
│   ┌─────────────────────────────────────────────────┐                       │
│   │ from datetime import datetime                   │                       │
│   │ import json                                      │                       │
│   │                                                  │                       │
│   │ STREAM_PATH = (                                  │                       │
│   │     "X:/Projects/_GAIA/_ARGUS/streams/"         │                       │
│   │     "sentiment_analyzer.jsonl"                  │                       │
│   │ )                                                │                       │
│   │                                                  │                       │
│   │ def emit_event(event_type: str, data: dict):    │                       │
│   │     event = {                                    │                       │
│   │         "timestamp": datetime.utcnow().isoformat(),│                     │
│   │         "project": "sentiment_analyzer",         │                       │
│   │         "event_type": event_type,                │                       │
│   │         "data": data                             │                       │
│   │     }                                            │                       │
│   │     with open(STREAM_PATH, "a") as f:           │                       │
│   │         f.write(json.dumps(event) + "\n")       │                       │
│   └─────────────────────────────────────────────────┘                       │
└─────────────────┬───────────────────────────────────────────────────────────┘
                  │
                  │ VULCAN → MNEMIS: "Initialize memory contracts"
                  ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ STEP 8: MNEMIS — Memory Initialization                                     │
│ Location: X:\Projects\_GAIA\_MNEMIS\                                       │
│                                                                             │
│ WHAT USER SEES:                                                             │
│   Console output: "Memory hierarchy configured"                             │
│   "5-tier memory system initialized"                                        │
│                                                                             │
│ WHAT HAPPENS BEHIND THE SCENES:                                             │
│   MNEMIS creates memory contracts for the new project:                      │
│                                                                             │
│   from mnemis.models.memory_models import (                                 │
│       MemoryContract,                                                       │
│       MemoryAccessLevel                                                     │
│   )                                                                         │
│   from mnemis.core.memory_store import MemoryStore                          │
│                                                                             │
│   def initialize_project_memory(project_id: str) -> MemoryStore:           │
│       # Create PROJECT-level memory contract                                │
│       contract = MemoryContract(                                            │
│           agent_id=f"{project_id}_system",                                  │
│           access_level=MemoryAccessLevel.PROJECT,                           │
│           project_id=project_id,                                            │
│           read_permissions=[                                                │
│               MemoryAccessLevel.PROJECT,                                    │
│               MemoryAccessLevel.AGENT                                       │
│           ],                                                                │
│           write_permissions=[                                               │
│               MemoryAccessLevel.PROJECT                                     │
│           ]                                                                 │
│       )                                                                     │
│                                                                             │
│       # Create memory store                                                 │
│       store = MemoryStore(                                                  │
│           project_id=project_id,                                            │
│           storage_path=(                                                    │
│               f"X:/Projects/_GAIA/_MNEMIS/stores/"                          │
│               f"{project_id}.db"                                            │
│           )                                                                 │
│       )                                                                     │
│                                                                             │
│       return store                                                          │
│                                                                             │
│ MEMORY INFRASTRUCTURE CREATED:                                              │
│   [✓] Memory store: sentiment_analyzer.db (SQLite)                          │
│   [✓] 5-tier hierarchy configured:                                          │
│       - Ephemeral: Function-level scratch space                             │
│       - Working: Agent execution context                                    │
│       - Session: User session data                                          │
│       - Long-term: Project patterns                                         │
│       - Permanent: Cross-project knowledge (GAIA-level)                     │
│   [✓] Memory contracts enforced (read down, write at level)                 │
│   [✓] Promotion protocol configured                                         │
│                                                                             │
│ GENERATED MEMORY CODE:                                                      │
│   src/sentiment_analyzer/services/memory_client.py:                         │
│   ┌─────────────────────────────────────────────────┐                       │
│   │ from mnemis.core.memory_store import MemoryStore│                       │
│   │ from mnemis.models.memory_models import (       │                       │
│   │     MemoryTier,                                 │                       │
│   │     MemoryEntry                                 │                       │
│   │ )                                                │                       │
│   │                                                  │                       │
│   │ store = MemoryStore(                            │                       │
│   │     project_id="sentiment_analyzer",            │                       │
│   │     storage_path=(                              │                       │
│   │         "X:/Projects/_GAIA/_MNEMIS/stores/"     │                       │
│   │         "sentiment_analyzer.db"                 │                       │
│   │     )                                            │                       │
│   │ )                                                │                       │
│   │                                                  │                       │
│   │ def store_pattern(key: str, value: Any):        │                       │
│   │     entry = MemoryEntry(                        │                       │
│   │         tier=MemoryTier.LONG_TERM,              │                       │
│   │         key=key,                                 │                       │
│   │         value=value,                             │                       │
│   │         project_id="sentiment_analyzer"          │                       │
│   │     )                                            │                       │
│   │     store.write(entry)                          │                       │
│   └─────────────────────────────────────────────────┘                       │
└─────────────────┬───────────────────────────────────────────────────────────┘
                  │
                  │ VULCAN: "Final verification and handoff"
                  ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ STEP 9: Final Verification & Project Handoff                               │
│                                                                             │
│ WHAT USER SEES:                                                             │
│   ┌──────────────────────────────────────────────────────┐                  │
│   │ PROJECT CREATION COMPLETE!                           │                  │
│   │                                                       │                  │
│   │ Name: Sentiment Analyzer                             │                  │
│   │ Location: X:\Projects\sentiment-analyzer             │                  │
│   │ Type: Creative (CreativeAdapter)                     │                  │
│   │ Status: Ready for development                        │                  │
│   │                                                       │                  │
│   │ GAIA Services Configured:                            │                  │
│   │   [✓] MYCEL: LLM clients ready (OpenAI, Anthropic)  │                  │
│   │   [✓] ARGUS: Telemetry active                        │                  │
│   │   [✓] MNEMIS: Memory store initialized               │                  │
│   │   [✓] WARDEN: Governance rules applied               │                  │
│   │                                                       │                  │
│   │ Next Steps:                                          │                  │
│   │   1. Copy .env.example to .env                       │                  │
│   │   2. Add your API keys                               │                  │
│   │   3. Run: streamlit run src/sentiment_analyzer/      │                  │
│   │            ui/streamlit_app.py                       │                  │
│   │   4. Review .claude/CLAUDE.md for project rules      │                  │
│   │                                                       │                  │
│   │ Documentation:                                        │                  │
│   │   - Architecture: docs/ARCHITECTURE.md               │                  │
│   │   - User Guide: docs/USER_GUIDE.md                   │                  │
│   │   - API Reference: docs/API.md                       │                  │
│   └──────────────────────────────────────────────────────┘                  │
│                                                                             │
│ WHAT HAPPENS BEHIND THE SCENES:                                             │
│   VULCAN performs final verification:                                       │
│                                                                             │
│   def verify_project_complete(project_path: Path) -> VerificationResult:   │
│       checks = [                                                            │
│           verify_directory_structure(project_path),                         │
│           verify_mycel_integration(project_path),                           │
│           verify_argus_telemetry(project_path),                             │
│           verify_mnemis_memory(project_path),                               │
│           verify_git_initialized(project_path),                             │
│           verify_tests_configured(project_path),                            │
│           verify_claude_md_present(project_path),                           │
│       ]                                                                     │
│                                                                             │
│       return VerificationResult(                                            │
│           success=all(c.passed for c in checks),                            │
│           checks=checks                                                     │
│       )                                                                     │
│                                                                             │
│   verification = verify_project_complete(                                   │
│       Path("X:/Projects/sentiment-analyzer")                                │
│   )                                                                         │
│                                                                             │
│   if verification.success:                                                  │
│       # Log to ARGUS                                                        │
│       emit_event("project_created", {                                       │
│           "project_id": "sentiment_analyzer",                               │
│           "adapter": "CreativeAdapter",                                     │
│           "services": ["MYCEL", "ARGUS", "MNEMIS"],                         │
│           "timestamp": datetime.utcnow().isoformat()                        │
│       })                                                                    │
│                                                                             │
│       # Update registry status                                              │
│       update_registry_status("sentiment_analyzer", "ready")                 │
│                                                                             │
│ PROJECT STATE:                                                              │
│   Status: READY FOR DEVELOPMENT                                             │
│   Registry entry: Created                                                   │
│   Git repository: Initialized (1 commit)                                    │
│   MYCEL integration: Active                                                 │
│   ARGUS telemetry: Listening                                                │
│   MNEMIS memory: Initialized                                                │
│   WARDEN rules: Enforced                                                    │
│   CLAUDE.md: Generated                                                      │
│   Tests: Configured (80% coverage required)                                 │
│   Documentation: Generated (3 files)                                        │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Services Involved in Flow 1

| Service | Role | Touch Points | Data Flow |
|---------|------|--------------|-----------|
| **VULCAN** | Orchestrator | Steps 1, 4-6, 9 | User input → Project specification → Scaffold generation |
| **MYCEL** | LLM Configuration | Step 2 | Project requirements → LLM client configs → Generated code |
| **WARDEN** | Validation | Step 3 | Project spec → Validation checks → Pass/fail result |
| **ARGUS** | Telemetry Setup | Step 7 | Project ID → Event stream creation → Telemetry code |
| **MNEMIS** | Memory Setup | Step 8 | Project ID → Memory contracts → Memory store |

### What Gets Created

**Files Generated:** 35+
**Lines of Code:** ~2,000 (scaffold + configs + tests)
**Services Integrated:** 4 (MYCEL, ARGUS, MNEMIS, WARDEN)
**Time to Complete:** ~30 seconds
**Manual Setup Saved:** ~4 hours of configuration work

---

## Flow 2: Editing an Existing Project via ABIS

### Overview
This flow demonstrates how a user visually modifies an existing agent system using ABIS (Visual System Builder). The user adds a new "Skeptic Agent" to an existing sentiment analyzer pipeline.

### Complete Flow Diagram

```
USER INTENT: "I want to add a skeptic agent to challenge positive sentiment scores"
     │
     │ (User opens ABIS web UI)
     │
     ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ STEP 1: ABIS — Visual System Builder (Project Loading)                     │
│ Location: X:\Projects\_GAIA\_ABIS\ (planned implementation)                │
│                                                                             │
│ WHAT USER SEES:                                                             │
│   ┌──────────────────────────────────────────────────────┐                  │
│   │ ABIS Visual System Builder                           │                  │
│   │                                                       │                  │
│   │ Project: sentiment_analyzer                          │                  │
│   │ [Load System] [Save] [Deploy]                        │                  │
│   │                                                       │                  │
│   │ Canvas:                                              │                  │
│   │                                                       │                  │
│   │   ┌─────────┐                                        │                  │
│   │   │ Input   │ (receives review text)                 │                  │
│   │   │  Agent  │                                        │                  │
│   │   └────┬────┘                                        │                  │
│   │        │                                             │                  │
│   │        ▼                                             │                  │
│   │   ┌─────────┐                                        │                  │
│   │   │Extract  │ (extracts entities, themes)            │                  │
│   │   │  Agent  │                                        │                  │
│   │   └────┬────┘                                        │                  │
│   │        │                                             │                  │
│   │        ▼                                             │                  │
│   │   ┌─────────┐                                        │                  │
│   │   │Classify │ (determines sentiment)                 │                  │
│   │   │  Agent  │                                        │                  │
│   │   └────┬────┘                                        │                  │
│   │        │                                             │                  │
│   │        ▼                                             │                  │
│   │   ┌─────────┐                                        │                  │
│   │   │ Score   │ (assigns 0-100 score)                  │                  │
│   │   │  Agent  │                                        │                  │
│   │   └────┬────┘                                        │                  │
│   │        │                                             │                  │
│   │        ▼                                             │                  │
│   │   ┌─────────┐                                        │                  │
│   │   │ Output  │ (formats results)                      │                  │
│   │   │  Agent  │                                        │                  │
│   │   └─────────┘                                        │                  │
│   │                                                       │                  │
│   │ Node Library:                                        │                  │
│   │   [Observer] [Executor] [Coordinator] [Transformer]  │                  │
│   └──────────────────────────────────────────────────────┘                  │
│                                                                             │
│ WHAT HAPPENS BEHIND THE SCENES:                                             │
│   ABIS queries registry for project system graph:                           │
│                                                                             │
│   def load_system_graph(project_id: str) -> SystemGraph:                   │
│       # Load from LOOM workflow definition                                  │
│       workflow_path = (                                                     │
│           f"X:/Projects/{project_id}/workflows/main.json"                   │
│       )                                                                     │
│       workflow = load_workflow(workflow_path)                               │
│                                                                             │
│       # Convert to visual graph representation                              │
│       graph = SystemGraph(                                                  │
│           project_id=project_id,                                            │
│           nodes=[                                                           │
│               GraphNode.from_agent(agent)                                   │
│               for agent in workflow.agents                                  │
│           ],                                                                │
│           edges=[                                                           │
│               GraphEdge.from_connection(conn)                               │
│               for conn in workflow.connections                              │
│           ]                                                                 │
│       )                                                                     │
│                                                                             │
│       return graph                                                          │
│                                                                             │
│ LOADED SYSTEM STATE:                                                        │
│   Project: sentiment_analyzer                                               │
│   Current agents: 5 (Input, Extract, Classify, Score, Output)               │
│   Current connections: 4 (linear pipeline)                                  │
│   Agent types: 2 Executors, 2 Transformers, 1 Observer                      │
└─────────────────┬───────────────────────────────────────────────────────────┘
                  │
                  │ USER ACTION: Drags "Observer Agent" from node library
                  ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ STEP 2: Agent Creation & Mental Model Selection                            │
│                                                                             │
│ WHAT USER SEES:                                                             │
│   ┌──────────────────────────────────────────────────────┐                  │
│   │ Create New Agent                                     │                  │
│   │                                                       │                  │
│   │ Name: Skeptic Agent                                  │                  │
│   │ Type: [Observer ▼]                                   │                  │
│   │ Role: Challenge positive sentiment classifications   │                  │
│   │                                                       │                  │
│   │ Mental Models (select from ARGUS library):           │                  │
│   │   [Search 59 models...]                              │                  │
│   │                                                       │                  │
│   │   Suggested for "skeptical analysis":                │                  │
│   │   [ ] Devil's Advocate                               │                  │
│   │   [ ] Red Team Thinking                              │                  │
│   │   [ ] Confirmation Bias Detection                    │                  │
│   │   [ ] Inversion (via negativa)                       │                  │
│   │   [ ] Steel Man Argument                             │                  │
│   │                                                       │                  │
│   │ [Cancel] [Create Agent]                              │                  │
│   └──────────────────────────────────────────────────────┘                  │
│                                                                             │
│ USER INTERACTION:                                                           │
│   User names agent: "Skeptic Agent"                                         │
│   User selects type: "Observer" (read-only, no external calls)              │
│   User clicks "Search mental models"                                        │
│   User searches: "skeptical analysis"                                       │
│                                                                             │
│ WHAT HAPPENS BEHIND THE SCENES:                                             │
│   ABIS → ARGUS: "Query mental models for skeptical reasoning"               │
│                                                                             │
│   from argus.mental_models.query import search_models                       │
│                                                                             │
│   def search_mental_models(query: str) -> List[MentalModel]:               │
│       # Semantic search across 59 mental models                             │
│       results = search_models(                                              │
│           query=query,                                                      │
│           top_k=5,                                                          │
│           embedding_model="text-embedding-3-small"                          │
│       )                                                                     │
│                                                                             │
│       return [                                                              │
│           MentalModel(                                                      │
│               id=r.id,                                                      │
│               name=r.name,                                                  │
│               description=r.description,                                    │
│               use_cases=r.use_cases,                                        │
│               prompt_template=r.prompt_template                             │
│           )                                                                 │
│           for r in results                                                  │
│       ]                                                                     │
│                                                                             │
│   # Returns:                                                                │
│   [                                                                         │
│       MentalModel(                                                          │
│           id="devils_advocate",                                             │
│           name="Devil's Advocate",                                          │
│           description="Argue against prevailing conclusion",                │
│           use_cases=["Challenge assumptions", "Find blind spots"],          │
│           prompt_template=(                                                 │
│               "Challenge this conclusion: {conclusion}\n"                   │
│               "Find potential flaws, biases, or overlooked risks."          │
│           )                                                                 │
│       ),                                                                    │
│       # ... 4 more models                                                   │
│   ]                                                                         │
│                                                                             │
│ USER INTERACTION (continued):                                               │
│   User selects: "Devil's Advocate"                                          │
│   User clicks: "Create Agent"                                               │
└─────────────────┬───────────────────────────────────────────────────────────┘
                  │
                  │ USER ACTION: Connects Skeptic Agent into pipeline
                  ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ STEP 3: Visual Connection & Data Flow Configuration                        │
│                                                                             │
│ WHAT USER SEES:                                                             │
│   Canvas updated with new agent:                                            │
│                                                                             │
│   ┌─────────┐                                                               │
│   │ Input   │                                                               │
│   └────┬────┘                                                               │
│        │                                                                    │
│        ▼                                                                    │
│   ┌─────────┐                                                               │
│   │Extract  │                                                               │
│   └────┬────┘                                                               │
│        │                                                                    │
│        ▼                                                                    │
│   ┌─────────┐                                                               │
│   │Classify │                                                               │
│   └────┬────┘                                                               │
│        │                                                                    │
│        ├──────────────┐                                                     │
│        │              │ (user drags connection)                             │
│        ▼              ▼                                                     │
│   ┌─────────┐   ┌─────────┐                                                │
│   │Skeptic  │   │ Score   │                                                │
│   │ Agent   │   │  Agent  │                                                │
│   └────┬────┘   └────┬────┘                                                │
│        │              │                                                     │
│        └──────┬───────┘                                                     │
│               │                                                             │
│               ▼                                                             │
│          ┌─────────┐                                                        │
│          │ Output  │                                                        │
│          └─────────┘                                                        │
│                                                                             │
│ USER INTERACTION:                                                           │
│   User clicks Classify Agent output port                                    │
│   User drags connection line to Skeptic Agent input port                    │
│   User clicks Skeptic Agent output port                                     │
│   User drags connection line to Score Agent (already connected)             │
│                                                                             │
│   ABIS prompts: "Configure data mapping"                                    │
│   ┌──────────────────────────────────────────────────────┐                  │
│   │ Data Mapping: Classify → Skeptic                     │                  │
│   │                                                       │                  │
│   │ Source fields (Classify output):                     │                  │
│   │   - sentiment: "positive" | "negative" | "neutral"   │                  │
│   │   - confidence: float (0.0-1.0)                      │                  │
│   │   - reasoning: str                                   │                  │
│   │                                                       │                  │
│   │ Target fields (Skeptic input):                       │                  │
│   │   - conclusion: str                                  │                  │
│   │   - evidence: str                                    │                  │
│   │                                                       │                  │
│   │ Mapping:                                             │                  │
│   │   conclusion ← sentiment + confidence                │                  │
│   │   evidence ← reasoning                               │                  │
│   │                                                       │                  │
│   │ [Cancel] [Save Mapping]                              │                  │
│   └──────────────────────────────────────────────────────┘                  │
│                                                                             │
│ WHAT HAPPENS BEHIND THE SCENES:                                             │
│   ABIS creates connection spec:                                             │
│                                                                             │
│   connection = AgentConnection(                                             │
│       source_agent_id="classify_agent",                                     │
│       target_agent_id="skeptic_agent",                                      │
│       mapping={                                                             │
│           "conclusion": "f'{sentiment} ({confidence:.0%} confident)'",      │
│           "evidence": "reasoning"                                           │
│       }                                                                     │
│   )                                                                         │
│                                                                             │
│   # Validates connection against agent schemas                              │
│   validation = validate_connection(connection)                              │
│   if not validation.valid:                                                  │
│       show_error(validation.errors)                                         │
└─────────────────┬───────────────────────────────────────────────────────────┘
                  │
                  │ USER ACTION: Clicks "Generate Workflow"
                  ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ STEP 4: System Graph → LOOM Workflow Compilation                           │
│                                                                             │
│ WHAT USER SEES:                                                             │
│   Progress indicator: "Compiling workflow... [####] 40%"                    │
│   Console output:                                                           │
│     "Generating System Graph Spec v1 JSON..."                               │
│     "Validating agent definitions..."                                       │
│     "Validating connections..."                                             │
│     "Compiling to LOOM workflow..."                                         │
│                                                                             │
│ WHAT HAPPENS BEHIND THE SCENES:                                             │
│   ABIS → LOOM: "Compile visual graph to executable workflow"                │
│                                                                             │
│   from loom.models.agent_models import (                                    │
│       AgentWorkflow,                                                        │
│       AgentNode,                                                            │
│       AgentConnection,                                                      │
│       AgentType                                                             │
│   )                                                                         │
│                                                                             │
│   def compile_to_workflow(                                                  │
│       graph: SystemGraph                                                    │
│   ) -> AgentWorkflow:                                                       │
│       """Convert visual graph to LOOM workflow."""                          │
│                                                                             │
│       # Create agent nodes                                                  │
│       agents = []                                                           │
│       for node in graph.nodes:                                              │
│           agent = AgentNode(                                                │
│               id=node.id,                                                   │
│               name=node.name,                                               │
│               agent_type=AgentType(node.type),                              │
│               input_schema=node.input_schema,                               │
│               output_schema=node.output_schema,                             │
│               implementation=node.implementation,                           │
│               mental_models=node.mental_models,                             │
│               governance_rules={                                            │
│                   "memory_tier": "WORKING",                                 │
│                   "max_llm_calls": 5,                                       │
│                   "budget_limit_usd": 0.10                                  │
│               }                                                             │
│           )                                                                 │
│           agents.append(agent)                                              │
│                                                                             │
│       # Create connections                                                  │
│       connections = []                                                      │
│       for edge in graph.edges:                                              │
│           conn = AgentConnection(                                           │
│               source_agent_id=edge.source_id,                               │
│               target_agent_id=edge.target_id,                               │
│               mapping=edge.data_mapping                                     │
│           )                                                                 │
│           connections.append(conn)                                          │
│                                                                             │
│       # Create workflow                                                     │
│       workflow = AgentWorkflow(                                             │
│           id="sentiment_analyzer_v2",                                       │
│           name="Sentiment Analyzer with Skeptic",                           │
│           agents=agents,                                                    │
│           connections=connections,                                          │
│           entry_points=["input_agent"]                                      │
│       )                                                                     │
│                                                                             │
│       # Validate workflow                                                   │
│       errors = workflow.validate_workflow()                                 │
│       if errors:                                                            │
│           raise ValidationError(errors)                                     │
│                                                                             │
│       return workflow                                                       │
│                                                                             │
│   workflow = compile_to_workflow(system_graph)                              │
│                                                                             │
│ GENERATED WORKFLOW JSON:                                                    │
│   X:/Projects/sentiment-analyzer/workflows/main_v2.json:                    │
│   ┌─────────────────────────────────────────────────┐                       │
│   │ {                                                │                       │
│   │   "id": "sentiment_analyzer_v2",                │                       │
│   │   "name": "Sentiment Analyzer with Skeptic",    │                       │
│   │   "version": "2.0.0",                            │                       │
│   │   "agents": [                                    │                       │
│   │     {                                            │                       │
│   │       "id": "skeptic_agent",                    │                       │
│   │       "name": "Skeptic Agent",                  │                       │
│   │       "type": "observer",                       │                       │
│   │       "mental_models": ["devils_advocate"],     │                       │
│   │       "input_schema": {                         │                       │
│   │         "conclusion": "str",                    │                       │
│   │         "evidence": "str"                       │                       │
│   │       },                                         │                       │
│   │       "output_schema": {                        │                       │
│   │         "critique": "str",                      │                       │
│   │         "risk_score": "float"                   │                       │
│   │       },                                         │                       │
│   │       "governance_rules": {                     │                       │
│   │         "memory_tier": "WORKING",               │                       │
│   │         "max_llm_calls": 5                      │                       │
│   │       }                                          │                       │
│   │     }                                            │                       │
│   │     // ... other agents                         │                       │
│   │   ],                                             │                       │
│   │   "connections": [                               │                       │
│   │     {                                            │                       │
│   │       "source": "classify_agent",               │                       │
│   │       "target": "skeptic_agent",                │                       │
│   │       "mapping": {                              │                       │
│   │         "conclusion": "f'{sentiment} ...'",     │                       │
│   │         "evidence": "reasoning"                 │                       │
│   │       }                                          │                       │
│   │     }                                            │                       │
│   │   ]                                              │                       │
│   │ }                                                │                       │
│   └─────────────────────────────────────────────────┘                       │
└─────────────────┬───────────────────────────────────────────────────────────┘
                  │
                  │ ABIS → WARDEN: "Validate modified workflow"
                  ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ STEP 5: WARDEN — Workflow Validation                                       │
│                                                                             │
│ WHAT USER SEES:                                                             │
│   Progress indicator: "Validating workflow... [########] 80%"               │
│   Validation results displayed:                                             │
│   ┌──────────────────────────────────────────────────────┐                  │
│   │ Validation Results                                   │                  │
│   │                                                       │                  │
│   │ [✓] All agents have valid schemas                    │                  │
│   │ [✓] All connections map compatible types             │                  │
│   │ [✓] No circular dependencies detected                │                  │
│   │ [✓] Memory access rules enforced                     │                  │
│   │ [✓] Budget limits configured                         │                  │
│   │ [✓] Mental models exist in ARGUS library             │                  │
│   │ [!] Warning: Observer agent has no output consumers  │                  │
│   │     (Skeptic output not used downstream)             │                  │
│   │                                                       │                  │
│   │ [Ignore Warning] [Fix] [Cancel]                      │                  │
│   └──────────────────────────────────────────────────────┘                  │
│                                                                             │
│ USER INTERACTION:                                                           │
│   User clicks "Fix"                                                         │
│   ABIS suggests: "Connect Skeptic output to Score Agent input"              │
│   User accepts suggestion                                                   │
│   ABIS adds connection: Skeptic → Score                                     │
│   User re-validates                                                         │
│                                                                             │
│ WHAT HAPPENS BEHIND THE SCENES:                                             │
│   def validate_workflow_modifications(                                      │
│       original: AgentWorkflow,                                              │
│       modified: AgentWorkflow                                               │
│   ) -> ValidationResult:                                                    │
│       """Ensure modifications don't break system."""                        │
│                                                                             │
│       checks = [                                                            │
│           # Constitutional checks                                           │
│           check_memory_hierarchy_respected(modified),                       │
│           check_budget_limits_set(modified),                                │
│           check_no_hardcoded_secrets(modified),                             │
│                                                                             │
│           # Workflow integrity                                              │
│           check_no_orphaned_agents(modified),                               │
│           check_no_circular_dependencies(modified),                         │
│           check_type_compatibility(modified),                               │
│                                                                             │
│           # GAIA integration                                                │
│           check_mental_models_exist(modified),                              │
│           check_telemetry_configured(modified),                             │
│       ]                                                                     │
│                                                                             │
│       return ValidationResult(                                              │
│           passed=all(c.passed for c in checks),                             │
│           violations=[c for c in checks if not c.passed],                   │
│           warnings=[c for c in checks if c.is_warning]                      │
│       )                                                                     │
│                                                                             │
│ VALIDATION RESULT:                                                          │
│   All checks passed after fix                                               │
│   Warnings resolved                                                         │
│   Workflow ready for deployment                                             │
└─────────────────┬───────────────────────────────────────────────────────────┘
                  │
                  │ ABIS → MNEMIS: "Update memory contracts for new agent"
                  ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ STEP 6: MNEMIS — Memory Contract Setup                                     │
│                                                                             │
│ WHAT USER SEES:                                                             │
│   Progress indicator: "Configuring memory access... [##########] 100%"      │
│                                                                             │
│ WHAT HAPPENS BEHIND THE SCENES:                                             │
│   MNEMIS creates memory contract for new Skeptic Agent:                     │
│                                                                             │
│   from mnemis.models.memory_models import (                                 │
│       MemoryContract,                                                       │
│       MemoryAccessLevel,                                                    │
│       MemoryTier                                                            │
│   )                                                                         │
│                                                                             │
│   def create_agent_memory_contract(                                         │
│       agent: AgentNode,                                                     │
│       project_id: str                                                       │
│   ) -> MemoryContract:                                                      │
│       """Create memory contract based on agent type."""                     │
│                                                                             │
│       # Observer agents: read-only, AGENT-level access                      │
│       if agent.agent_type == AgentType.OBSERVER:                            │
│           return MemoryContract(                                            │
│               agent_id=agent.id,                                            │
│               access_level=MemoryAccessLevel.AGENT,                         │
│               project_id=project_id,                                        │
│               read_permissions=[                                            │
│                   MemoryAccessLevel.AGENT                                   │
│               ],                                                            │
│               write_permissions=[                                           │
│                   MemoryAccessLevel.AGENT                                   │
│               ],                                                            │
│               allowed_tiers=[                                               │
│                   MemoryTier.EPHEMERAL,                                     │
│                   MemoryTier.WORKING                                        │
│               ]                                                             │
│           )                                                                 │
│                                                                             │
│   contract = create_agent_memory_contract(                                  │
│       skeptic_agent,                                                        │
│       "sentiment_analyzer"                                                  │
│   )                                                                         │
│                                                                             │
│   # Register contract with memory store                                     │
│   memory_store.register_contract(contract)                                  │
│                                                                             │
│ MEMORY CONTRACT CREATED:                                                    │
│   Agent: skeptic_agent                                                      │
│   Access Level: AGENT (execution-scoped)                                    │
│   Read Permissions: AGENT tier only                                         │
│   Write Permissions: AGENT tier only                                        │
│   Allowed Tiers: Ephemeral, Working                                         │
│   Constitutional Rule: "Read down hierarchy, write at level"                │
└─────────────────┬───────────────────────────────────────────────────────────┘
                  │
                  │ ABIS → ARGUS: "Register telemetry for new agent"
                  ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ STEP 7: ARGUS — Telemetry Registration                                     │
│                                                                             │
│ WHAT USER SEES:                                                             │
│   Console output: "Telemetry configured for skeptic_agent"                  │
│   "Mental model 'devils_advocate' registered"                               │
│                                                                             │
│ WHAT HAPPENS BEHIND THE SCENES:                                             │
│   ARGUS registers new agent for monitoring:                                 │
│                                                                             │
│   def register_agent_telemetry(                                             │
│       agent: AgentNode,                                                     │
│       project_id: str                                                       │
│   ) -> TelemetryConfig:                                                     │
│       config = TelemetryConfig(                                             │
│           agent_id=agent.id,                                                │
│           project_id=project_id,                                            │
│           mental_models=agent.mental_models,                                │
│           track_cost=True,                                                  │
│           track_latency=True,                                               │
│           track_quality=True,                                               │
│           explainability_level="full"                                       │
│       )                                                                     │
│                                                                             │
│       # Register with event bus                                             │
│       event_bus.register_agent(agent.id, config)                            │
│                                                                             │
│       # Link mental models                                                  │
│       for model_id in agent.mental_models:                                  │
│           link_mental_model(agent.id, model_id)                             │
│                                                                             │
│       return config                                                         │
│                                                                             │
│ TELEMETRY EVENTS TO BE TRACKED:                                             │
│   - skeptic_agent.execution_start                                           │
│   - skeptic_agent.execution_complete                                        │
│   - skeptic_agent.mental_model_applied (devils_advocate)                    │
│   - skeptic_agent.llm_call (model, cost, tokens)                            │
│   - skeptic_agent.critique_generated                                        │
│   - skeptic_agent.risk_score_calculated                                     │
└─────────────────┬───────────────────────────────────────────────────────────┘
                  │
                  │ USER ACTION: Clicks "Deploy Workflow"
                  ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ STEP 8: Runtime Execution with Monitoring                                  │
│                                                                             │
│ WHAT USER SEES:                                                             │
│   ┌──────────────────────────────────────────────────────┐                  │
│   │ Workflow Deployed Successfully!                      │                  │
│   │                                                       │                  │
│   │ Version: sentiment_analyzer_v2                       │                  │
│   │ Changes:                                             │                  │
│   │   + Added: Skeptic Agent (Observer)                  │                  │
│   │   + Mental Model: Devil's Advocate                   │                  │
│   │   + Connection: Classify → Skeptic → Score           │                  │
│   │                                                       │                  │
│   │ [Run Test] [View Telemetry] [Close]                  │                  │
│   └──────────────────────────────────────────────────────┘                  │
│                                                                             │
│ USER INTERACTION:                                                           │
│   User clicks "Run Test"                                                    │
│   ABIS submits test review: "This product is amazing!"                      │
│                                                                             │
│ WHAT HAPPENS BEHIND THE SCENES:                                             │
│   from loom.core.workflow_engine import WorkflowEngine                      │
│                                                                             │
│   engine = WorkflowEngine(                                                  │
│       mycel_bridge=MycelAgentBridge(),                                      │
│       mnemis_bridge=MnemisAgentBridge()                                     │
│   )                                                                         │
│                                                                             │
│   workflow = load_workflow("main_v2.json")                                  │
│   context = engine.execute_workflow(                                        │
│       workflow=workflow,                                                    │
│       initial_inputs={"review_text": "This product is amazing!"}            │
│   )                                                                         │
│                                                                             │
│ EXECUTION TRACE:                                                            │
│   [00:00.012] input_agent: Received review text                             │
│   [00:00.045] extract_agent: Extracted entities (0 issues)                  │
│   [00:00.201] classify_agent: Classified as POSITIVE (0.92 confidence)      │
│   [00:00.203] skeptic_agent: STARTED                                        │
│   [00:00.204]   Using mental model: devils_advocate                         │
│   [00:00.205]   Prompt: "Challenge this conclusion: positive (92% conf...)" │
│   [00:00.850]   LLM call: claude-haiku-4-5-20251001 ($0.002)                │
│   [00:00.851]   Critique generated: "Consider: might be promotional..."     │
│   [00:00.852]   Risk score: 0.35 (moderate skepticism)                      │
│   [00:00.853] skeptic_agent: COMPLETE                                       │
│   [00:00.920] score_agent: Adjusted score 92 → 87 (skeptic input)           │
│   [00:00.955] output_agent: Formatted results                               │
│   [00:00.956] Workflow COMPLETE (944ms total)                               │
│                                                                             │
│ TEST RESULTS DISPLAYED:                                                     │
│   ┌──────────────────────────────────────────────────────┐                  │
│   │ Test Execution Results                               │                  │
│   │                                                       │                  │
│   │ Review: "This product is amazing!"                   │                  │
│   │                                                       │                  │
│   │ Classification: POSITIVE (92% confident)             │                  │
│   │ Original Score: 92                                   │                  │
│   │                                                       │                  │
│   │ Skeptic Critique:                                    │                  │
│   │ "Consider: Language suggests promotional content.    │                  │
│   │  Lacks specific details. High confidence may be      │                  │
│   │  overestimation given brevity."                      │                  │
│   │                                                       │                  │
│   │ Risk Score: 0.35 (moderate skepticism)               │                  │
│   │ Adjusted Score: 87 (-5 points)                       │                  │
│   │                                                       │                  │
│   │ Total Time: 944ms                                    │                  │
│   │ Total Cost: $0.003                                   │                  │
│   └──────────────────────────────────────────────────────┘                  │
└─────────────────┬───────────────────────────────────────────────────────────┘
                  │
                  │ USER ACTION: Clicks "View Telemetry"
                  ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ STEP 9: ARGUS Dashboard — Review Telemetry & Performance                   │
│                                                                             │
│ WHAT USER SEES:                                                             │
│   ARGUS Dashboard opens, showing real-time metrics:                         │
│                                                                             │
│   ┌──────────────────────────────────────────────────────────────┐          │
│   │ ARGUS Telemetry Dashboard                                    │          │
│   │ Project: sentiment_analyzer                                  │          │
│   │ Workflow: sentiment_analyzer_v2                              │          │
│   │ Time Range: Last Hour                                        │          │
│   │                                                               │          │
│   │ Agent Performance:                                            │          │
│   │   ┌─────────────────┬──────┬──────┬────────┬────────┐        │          │
│   │   │ Agent           │Calls │ Avg  │ Cost   │ Quality│        │          │
│   │   │                 │      │Time  │        │        │        │          │
│   │   ├─────────────────┼──────┼──────┼────────┼────────┤        │          │
│   │   │ input_agent     │  12  │ 15ms │ $0.000 │  N/A   │        │          │
│   │   │ extract_agent   │  12  │ 78ms │ $0.012 │  0.94  │        │          │
│   │   │ classify_agent  │  12  │156ms │ $0.024 │  0.89  │        │          │
│   │   │ skeptic_agent   │  12  │645ms │ $0.024 │  0.87  │ NEW    │          │
│   │   │ score_agent     │  12  │ 42ms │ $0.006 │  0.92  │        │          │
│   │   │ output_agent    │  12  │ 18ms │ $0.000 │  N/A   │        │          │
│   │   └─────────────────┴──────┴──────┴────────┴────────┘        │          │
│   │                                                               │          │
│   │ Mental Model Usage:                                           │          │
│   │   devils_advocate: 12 invocations                            │          │
│   │   Avg impact: -4.2 points per review                         │          │
│   │   Variance: 2.3 points                                        │          │
│   │                                                               │          │
│   │ Cost Impact:                                                  │          │
│   │   Before Skeptic: $0.042 per review                          │          │
│   │   After Skeptic:  $0.066 per review (+57%)                   │          │
│   │   Monthly projection: $19.80 (within $50 budget)             │          │
│   │                                                               │          │
│   │ Quality Trend:                                                │          │
│   │   Score variance reduced by 18% (more conservative)          │          │
│   │   False positive rate: reduced from 23% → 14%                │          │
│   │                                                               │          │
│   │ [Export Data] [View Pattern Analysis] [Close]                │          │
│   └──────────────────────────────────────────────────────────────┘          │
│                                                                             │
│ ARGUS SUBCONSCIOUS PATTERN DETECTION:                                       │
│   Pattern detected after 12 executions:                                     │
│   - Skeptic agent consistently lowers scores on short reviews                │
│   - Average adjustment: -5.2 points (σ=2.1)                                  │
│   - Mental model effective at detecting promotional language                 │
│   - Recommendation: Promote this pattern to Long-term memory                 │
│                                                                             │
│ WHAT HAPPENS BEHIND THE SCENES:                                             │
│   ARGUS analyzes event stream:                                              │
│                                                                             │
│   events = load_events("sentiment_analyzer.jsonl")                          │
│   patterns = detect_patterns(events)                                        │
│                                                                             │
│   for pattern in patterns:                                                  │
│       if pattern.confidence > 0.85:                                         │
│           # Eligible for promotion to MNEMIS                                │
│           recommend_promotion(pattern)                                      │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Services Involved in Flow 2

| Service | Role | Touch Points | Data Flow |
|---------|------|--------------|-----------|
| **ABIS** | Visual Editor | Steps 1-3, 8 | User interactions → Visual graph → System spec |
| **ARGUS** | Mental Models + Telemetry | Steps 2, 7, 9 | Mental model search → Agent registration → Performance monitoring |
| **LOOM** | Workflow Compilation | Step 4 | System graph → Validated workflow → Executable spec |
| **WARDEN** | Validation | Step 5 | Workflow spec → Validation checks → Pass/fail |
| **MNEMIS** | Memory Contracts | Step 6 | Agent definition → Memory contract → Access rules |
| **MYCEL** | LLM Execution | Step 8 (runtime) | Agent calls → LLM client → Responses |

### What Changes with This Flow

**Files Modified:** 2 (workflow JSON, telemetry config)
**New Agent Code Generated:** ~200 lines
**Services Touched:** 6 (ABIS, LOOM, WARDEN, MNEMIS, ARGUS, MYCEL)
**Time to Deploy:** ~2 minutes (including validation)
**Code-free Workflow Changes:** 100% (visual editor only)

---

## Flow 3: Product Evolution Flow

### Overview
This flow demonstrates how user feedback or GAIA-detected patterns trigger automatic product evolution through the promotion protocol.

### Flow Diagram

```
USER FEEDBACK or ARGUS PATTERN DETECTION
     │
     │ Example: "Skeptic agent is too aggressive on neutral reviews"
     │
     ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ STEP 1: ARGUS — Pattern Detection                                          │
│                                                                             │
│ ARGUS Subconscious monitors event stream:                                   │
│   sentiment_analyzer.jsonl (24 hours of telemetry)                          │
│                                                                             │
│   from argus.subconscious.pattern_detector import detect_anomalies         │
│                                                                             │
│   def analyze_agent_behavior(agent_id: str) -> List[Pattern]:              │
│       events = load_events(agent_id)                                        │
│       patterns = []                                                         │
│                                                                             │
│       # Statistical analysis                                                │
│       if detect_outlier_behavior(events):                                   │
│           patterns.append(Pattern(                                          │
│               type="outlier",                                               │
│               description=(                                                 │
│                   "Skeptic agent reduces neutral review "                   │
│                   "scores by 12 points on average (expected: 2-5)"          │
│               ),                                                            │
│               confidence=0.92,                                              │
│               severity="moderate",                                          │
│               recommendation="Adjust mental model weighting"                │
│           ))                                                                │
│                                                                             │
│       return patterns                                                       │
│                                                                             │
│ DETECTED PATTERN:                                                           │
│   Type: Behavioral anomaly                                                  │
│   Agent: skeptic_agent                                                      │
│   Issue: Over-penalizing neutral sentiment                                  │
│   Confidence: 92%                                                           │
│   Sample size: 347 reviews                                                  │
│   Impact: False negative rate increased 18%                                 │
└─────────────────┬───────────────────────────────────────────────────────────┘
                  │
                  │ ARGUS → MNEMIS: "Store detected pattern"
                  ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ STEP 2: MNEMIS — Pattern Storage & Analysis                                │
│                                                                             │
│ MNEMIS receives pattern from ARGUS:                                         │
│                                                                             │
│   from mnemis.models.memory_models import (                                 │
│       MemoryEntry,                                                          │
│       MemoryTier                                                            │
│   )                                                                         │
│                                                                             │
│   pattern_entry = MemoryEntry(                                              │
│       tier=MemoryTier.LONG_TERM,  # Project-level pattern                   │
│       key="skeptic_neutral_overpenalty",                                    │
│       value={                                                               │
│           "pattern_type": "behavioral_anomaly",                             │
│           "agent_id": "skeptic_agent",                                      │
│           "description": "Over-penalizes neutral reviews",                  │
│           "metrics": {                                                      │
│               "avg_penalty_neutral": 12.3,                                  │
│               "avg_penalty_positive": 5.1,                                  │
│               "avg_penalty_negative": 3.2,                                  │
│               "false_negative_rate": 0.18                                   │
│           },                                                                │
│           "sample_size": 347,                                               │
│           "confidence": 0.92,                                               │
│           "detected_at": "2026-02-08T14:23:11Z"                             │
│       },                                                                    │
│       project_id="sentiment_analyzer",                                      │
│       access_level=MemoryAccessLevel.PROJECT                                │
│   )                                                                         │
│                                                                             │
│   memory_store.write(pattern_entry)                                         │
│                                                                             │
│ MNEMIS checks for cross-project patterns:                                   │
│   Query: "Has this pattern appeared in other projects?"                     │
│   Result: No similar patterns found in other products                       │
│   Conclusion: Project-specific issue, not ecosystem-wide                    │
└─────────────────┬───────────────────────────────────────────────────────────┘
                  │
                  │ MNEMIS → User: "Pattern detected, propose solution"
                  ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ STEP 3: MNEMIS — Promotion Protocol (HITL Decision)                        │
│                                                                             │
│ MNEMIS proposes promotion to user:                                          │
│                                                                             │
│   ┌──────────────────────────────────────────────────────────────┐          │
│   │ MNEMIS Memory Promotion Request                              │          │
│   │                                                               │          │
│   │ Pattern Detected:                                            │          │
│   │   Skeptic agent over-penalizes neutral reviews               │          │
│   │   (avg -12 pts, expected -2 to -5 pts)                       │          │
│   │                                                               │          │
│   │ Evidence:                                                     │          │
│   │   - 347 reviews analyzed                                      │          │
│   │   - 92% confidence                                            │          │
│   │   - False negative rate: 18% (was 7%)                        │          │
│   │                                                               │          │
│   │ Proposed Solution:                                            │          │
│   │   Adjust Devil's Advocate mental model weighting:             │          │
│   │   - For NEUTRAL sentiment: reduce weight 0.8 → 0.3            │          │
│   │   - For POSITIVE sentiment: keep weight 0.8                   │          │
│   │   - For NEGATIVE sentiment: keep weight 0.5                   │          │
│   │                                                               │          │
│   │ Impact Projection:                                            │          │
│   │   - False negative rate: 18% → 9% (expected)                 │          │
│   │   - Avg neutral penalty: -12 pts → -4 pts                    │          │
│   │   - Overall accuracy: +6.2%                                   │          │
│   │                                                               │          │
│   │ Promotion Path:                                               │          │
│   │   [Store as Long-term memory (project-only)]                 │          │
│   │   [Promote to Permanent (share across GAIA)]                 │          │
│   │                                                               │          │
│   │ Apply Change:                                                 │          │
│   │   [○] Approve and apply immediately                           │          │
│   │   [○] Approve but schedule for next version                   │          │
│   │   [○] Reject (explain why)                                    │          │
│   │                                                               │          │
│   │ [Approve] [Reject] [Need More Data]                           │          │
│   └──────────────────────────────────────────────────────────────┘          │
│                                                                             │
│ USER INTERACTION:                                                           │
│   User selects: "Approve and apply immediately"                             │
│   User selects: "Store as Long-term memory (project-only)"                  │
│   User clicks: "Approve"                                                    │
└─────────────────┬───────────────────────────────────────────────────────────┘
                  │
                  │ MNEMIS → LOOM: "Apply approved modification"
                  ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ STEP 4: LOOM — Apply Configuration Change                                  │
│                                                                             │
│ LOOM receives modification request:                                         │
│                                                                             │
│   from loom.core.workflow_engine import modify_agent_config                │
│                                                                             │
│   def apply_mental_model_adjustment(                                        │
│       agent_id: str,                                                        │
│       adjustment: Dict[str, Any]                                            │
│   ) -> ModificationResult:                                                  │
│       # Load current workflow                                               │
│       workflow = load_workflow("main_v2.json")                              │
│       agent = workflow.get_agent(agent_id)                                  │
│                                                                             │
│       # Apply adjustment                                                    │
│       agent.governance_rules["mental_model_weights"] = {                    │
│           "devils_advocate": {                                              │
│               "sentiment_positive": 0.8,  # unchanged                       │
│               "sentiment_neutral": 0.3,   # reduced from 0.8                │
│               "sentiment_negative": 0.5   # unchanged                       │
│           }                                                                 │
│       }                                                                     │
│                                                                             │
│       # Increment version                                                   │
│       workflow.version = "2.1.0"                                            │
│                                                                             │
│       # Save updated workflow                                               │
│       save_workflow(workflow, "main_v2.1.json")                             │
│                                                                             │
│       return ModificationResult(                                            │
│           success=True,                                                     │
│           new_version="2.1.0"                                               │
│       )                                                                     │
│                                                                             │
│ MODIFICATION APPLIED:                                                       │
│   Workflow version: 2.0.0 → 2.1.0                                           │
│   Agent: skeptic_agent                                                      │
│   Change: Mental model weighting adjusted                                   │
│   Config file: main_v2.1.json                                               │
└─────────────────┬───────────────────────────────────────────────────────────┘
                  │
                  │ LOOM → WARDEN: "Validate modification"
                  ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ STEP 5: WARDEN — Validate Modified Workflow                                │
│                                                                             │
│ WARDEN validates the configuration change:                                  │
│                                                                             │
│   validation = validate_workflow_modifications(                             │
│       original=load_workflow("main_v2.json"),                               │
│       modified=load_workflow("main_v2.1.json")                              │
│   )                                                                         │
│                                                                             │
│   Checks performed:                                                         │
│   [✓] No breaking changes to agent contracts                                │
│   [✓] Mental model weights sum correctly                                    │
│   [✓] No security regressions                                               │
│   [✓] Budget limits unchanged                                               │
│   [✓] Memory access unchanged                                               │
│                                                                             │
│ VALIDATION RESULT: PASSED                                                   │
└─────────────────┬───────────────────────────────────────────────────────────┘
                  │
                  │ LOOM: "Deploy updated workflow"
                  ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ STEP 6: Production Deployment                                              │
│                                                                             │
│ Updated workflow deployed to production:                                    │
│   sentiment_analyzer_v2.1 is now active                                     │
│                                                                             │
│ ARGUS begins monitoring new version:                                        │
│   Telemetry stream: sentiment_analyzer.jsonl                                │
│   Version tag: v2.1.0                                                       │
│   Comparison baseline: v2.0.0                                               │
└─────────────────┬───────────────────────────────────────────────────────────┘
                  │
                  │ Monitor for 24-48 hours
                  ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ STEP 7: ARGUS — Monitor New Behavior                                       │
│                                                                             │
│ After 48 hours, 412 reviews processed:                                      │
│                                                                             │
│   Performance Comparison (v2.0.0 → v2.1.0):                                 │
│   ┌──────────────────────────────┬──────────┬──────────┐                    │
│   │ Metric                       │  v2.0.0  │  v2.1.0  │                    │
│   ├──────────────────────────────┼──────────┼──────────┤                    │
│   │ Avg penalty (neutral)        │ -12.3 pts│  -3.8 pts│ ✓ IMPROVED        │
│   │ Avg penalty (positive)       │  -5.1 pts│  -5.0 pts│ ✓ STABLE          │
│   │ Avg penalty (negative)       │  -3.2 pts│  -3.1 pts│ ✓ STABLE          │
│   │ False negative rate          │   18%    │    8%    │ ✓ IMPROVED        │
│   │ Overall accuracy             │   82%    │   88%    │ ✓ IMPROVED        │
│   │ Cost per review              │  $0.066  │  $0.065  │ ✓ STABLE          │
│   └──────────────────────────────┴──────────┴──────────┘                    │
│                                                                             │
│ ARGUS verdict: "Modification successful, metrics improved"                  │
│                                                                             │
│ MNEMIS action: Promote pattern to Long-term memory with success marker      │
└─────────────────────────────────────────────────────────────────────────────┘

CYCLE CONTINUES:
  ARGUS monitors → Patterns detected → MNEMIS stores →
  User approves → LOOM applies → WARDEN validates →
  Production deployment → ARGUS monitors new behavior
```

### Evolution Triggers

| Trigger Type | Source | Example | Action |
|--------------|--------|---------|--------|
| **User Feedback** | Direct input | "Agent too aggressive" | MNEMIS proposes adjustment |
| **Pattern Detection** | ARGUS Subconscious | Anomaly in metrics | ARGUS alerts, MNEMIS analyzes |
| **Cross-Project Pattern** | MNEMIS promotion | Same issue in 3+ projects | Promote to GAIA-level knowledge |
| **Cost Threshold** | ARGUS cost tracking | Monthly budget 80% used | Suggest model downgrade |
| **Quality Degradation** | ARGUS quality metrics | Accuracy drops 5%+ | Flag for investigation |

---

## Flow 4: Python Tools Governance Flow

### Overview
This flow shows how standalone Python tools (outside formal products) still contribute to GAIA intelligence while maintaining governance.

### Flow Diagram

```
STANDALONE PYTHON TOOL: data_cleaner.py
     │
     │ Purpose: One-off script to clean customer review dataset
     │
     ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ DEVELOPER WRITES SCRIPT                                                     │
│                                                                             │
│ X:\Projects\Python tools\data_cleaner.py:                                   │
│ ┌────────────────────────────────────────────────┐                          │
│ │ # Standard Python tool structure               │                          │
│ │                                                 │                          │
│ │ from rag_intelligence.config import GaiaSettings│                          │
│ │ from rag_intelligence.llm import create_llm_client│                        │
│ │ import json                                     │                          │
│ │ from datetime import datetime                   │                          │
│ │                                                 │                          │
│ │ # ARGUS telemetry (optional but recommended)   │                          │
│ │ ARGUS_STREAM = (                                │                          │
│ │     "X:/Projects/_GAIA/_ARGUS/streams/"        │                          │
│ │     "python_tools.jsonl"                       │                          │
│ │ )                                               │                          │
│ │                                                 │                          │
│ │ def emit_event(event_type, data):              │                          │
│ │     event = {                                   │                          │
│ │         "timestamp": datetime.utcnow(),        │                          │
│ │         "tool": "data_cleaner",                │                          │
│ │         "event_type": event_type,              │                          │
│ │         "data": data                           │                          │
│ │     }                                           │                          │
│ │     with open(ARGUS_STREAM, "a") as f:         │                          │
│ │         f.write(json.dumps(event) + "\n")      │                          │
│ │                                                 │                          │
│ │ # Use MYCEL for LLM calls                      │                          │
│ │ settings = GaiaSettings()                       │                          │
│ │ client = create_llm_client(                    │                          │
│ │     provider="openai",                         │                          │
│ │     model=settings.openai_model_fast           │                          │
│ │ )                                               │                          │
│ │                                                 │                          │
│ │ # Main logic                                    │                          │
│ │ def clean_reviews(file_path):                  │                          │
│ │     emit_event("cleaning_started", {...})      │                          │
│ │                                                 │                          │
│ │     reviews = load_csv(file_path)              │                          │
│ │     for review in reviews:                     │                          │
│ │         # Use LLM to detect spam                │                          │
│ │         result = client.complete(               │                          │
│ │             prompt=f"Is this spam? {review}"   │                          │
│ │         )                                       │                          │
│ │         emit_event("review_classified", {...}) │                          │
│ │                                                 │                          │
│ │     emit_event("cleaning_complete", {...})     │                          │
│ │     return cleaned_reviews                     │                          │
│ └────────────────────────────────────────────────┘                          │
└─────────────────┬───────────────────────────────────────────────────────────┘
                  │
                  │ Developer runs: python data_cleaner.py
                  ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ RUNTIME: MYCEL Integration                                                  │
│                                                                             │
│ Script uses MYCEL for LLM calls:                                            │
│   - Unified API across providers                                            │
│   - Automatic cost tracking                                                 │
│   - Prompt caching (if enabled)                                             │
│   - Error handling and retries                                              │
│                                                                             │
│ Benefits:                                                                   │
│   [✓] No need to import openai/anthropic directly                           │
│   [✓] Consistent error handling across tools                                │
│   [✓] Automatic budget warnings                                             │
│   [✓] Unified configuration via .env                                        │
└─────────────────┬───────────────────────────────────────────────────────────┘
                  │
                  │ Script emits telemetry
                  ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ RUNTIME: ARGUS Telemetry Collection                                        │
│                                                                             │
│ Events written to python_tools.jsonl:                                       │
│   {"timestamp": "...", "tool": "data_cleaner", "event": "started"}         │
│   {"timestamp": "...", "tool": "data_cleaner", "event": "classified", ...} │
│   {"timestamp": "...", "tool": "data_cleaner", "event": "complete", ...}   │
│                                                                             │
│ ARGUS processes stream:                                                     │
│   - Cost tracking (LLM calls)                                               │
│   - Pattern detection (spam classification accuracy)                        │
│   - Usage metrics (how often tool is run)                                   │
└─────────────────┬───────────────────────────────────────────────────────────┘
                  │
                  │ Patterns detected over time
                  ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ MNEMIS: Pattern Storage                                                    │
│                                                                             │
│ ARGUS detects: "data_cleaner consistently identifies promotional reviews"   │
│                                                                             │
│ Pattern stored in MNEMIS Long-term memory:                                  │
│   Key: "spam_detection_promotional_language"                                │
│   Value: {                                                                  │
│       "pattern": "Reviews with 'amazing', 'best ever', 'highly             │
│                   recommend' are 87% likely to be promotional",             │
│       "confidence": 0.91,                                                   │
│       "sample_size": 1247,                                                  │
│       "source": "python_tools/data_cleaner"                                 │
│   }                                                                         │
│                                                                             │
│ MNEMIS promotion protocol:                                                  │
│   "This pattern is relevant to sentiment_analyzer product"                  │
│   "Recommend: Add promotional language filter to classifier agent"          │
└─────────────────┬───────────────────────────────────────────────────────────┘
                  │
                  │ Cross-project intelligence sharing
                  ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ CROSS-PROJECT BENEFIT                                                       │
│                                                                             │
│ Pattern from Python tool → Applied to Product:                              │
│                                                                             │
│   sentiment_analyzer (product) benefits from data_cleaner (tool) insights   │
│                                                                             │
│   MNEMIS suggests to sentiment_analyzer developer:                          │
│   "A Python tool discovered promotional language patterns that could        │
│    improve your classifier. Would you like to integrate this knowledge?"    │
│                                                                             │
│ User approves → LOOM adds filter → Product improved                          │
└─────────────────────────────────────────────────────────────────────────────┘

GOVERNANCE MAINTAINED:
  [✓] WARDEN validates: No secrets in code (uses .env)
  [✓] WARDEN validates: LLM calls go through MYCEL (budget tracked)
  [✓] ARGUS monitors: Cost and usage metrics available
  [✓] MNEMIS stores: Patterns shared across ecosystem
  [✓] Registry tracks: Tool version and dependencies
```

### Python Tools Integration Checklist

| Requirement | Purpose | Implementation |
|-------------|---------|----------------|
| **Use MYCEL for LLM** | Unified API, cost tracking | `from rag_intelligence.llm import create_llm_client` |
| **Emit ARGUS telemetry** | Track usage, detect patterns | Write JSON events to `python_tools.jsonl` |
| **No hardcoded secrets** | Security | Use `os.getenv("API_KEY")` |
| **WARDEN validation** | Pre-commit hooks | `.git/hooks/pre-commit` runs `ruff`, secret detection |
| **Registry entry** | Track versions | Optional for one-off tools, required for reusable |

---

## Flow 5: RAVEN Research Flow

### Overview
RAVEN is an autonomous research agent that conducts multi-source investigations and stores findings in MNEMIS for cross-project use.

### Flow Diagram

```
RESEARCH QUESTION: "What are best practices for skeptical sentiment analysis?"
     │
     │ (User submits via RAVEN CLI or UI)
     │
     ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ STEP 1: RAVEN — Research Task Initialization                               │
│ Location: X:\Projects\_GAIA\_RAVEN\ (planned implementation)               │
│                                                                             │
│ RAVEN receives research question:                                           │
│                                                                             │
│   from raven.core.research_agent import ResearchAgent                       │
│   from raven.models.research_task import ResearchTask                       │
│                                                                             │
│   task = ResearchTask(                                                      │
│       question="What are best practices for skeptical sentiment analysis?", │
│       context={                                                             │
│           "related_project": "sentiment_analyzer",                          │
│           "trigger": "performance_improvement",                             │
│           "current_approach": "devils_advocate_mental_model"                │
│       },                                                                    │
│       depth="comprehensive",  # quick | standard | comprehensive            │
│       max_sources=15,                                                       │
│       max_cost_usd=2.00                                                     │
│   )                                                                         │
│                                                                             │
│   agent = ResearchAgent(                                                    │
│       llm_provider="anthropic",                                             │
│       model="claude-sonnet-4-5-20250929"  # PROJECT-level model             │
│   )                                                                         │
│                                                                             │
│   result = agent.research(task)                                             │
└─────────────────┬───────────────────────────────────────────────────────────┘
                  │
                  │ RAVEN → MYCEL: "Retrieve relevant documents"
                  ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ STEP 2: MYCEL — RAG Retrieval Across Sources                               │
│                                                                             │
│ MYCEL performs semantic search across multiple sources:                     │
│                                                                             │
│   from rag_intelligence.rag import RAGPipeline                              │
│   from rag_intelligence.embedding import create_embedder                    │
│                                                                             │
│   def retrieve_relevant_docs(                                               │
│       query: str,                                                           │
│       sources: List[str]                                                    │
│   ) -> List[Document]:                                                      │
│       embedder = create_embedder("text-embedding-3-small")                  │
│       query_embedding = embedder.embed(query)                               │
│                                                                             │
│       documents = []                                                        │
│       for source in sources:                                                │
│           # Search in document stores                                       │
│           results = search_vector_store(                                    │
│               query_embedding,                                              │
│               source,                                                       │
│               top_k=10                                                      │
│           )                                                                 │
│           documents.extend(results)                                         │
│                                                                             │
│       # Re-rank by relevance                                                │
│       documents = rerank_documents(documents, query)                        │
│       return documents[:15]  # max_sources limit                            │
│                                                                             │
│ SOURCES SEARCHED:                                                           │
│   1. GAIA documentation (GECO_ARCHITECTURE.md, GAIA_BIBLE.md)               │
│   2. Mental Model Library (59 models)                                       │
│   3. MNEMIS cross-project memory (related patterns)                         │
│   4. External knowledge base (papers, articles - if configured)             │
│   5. Project documentation (sentiment_analyzer/docs/)                       │
│                                                                             │
│ RETRIEVED DOCUMENTS:                                                        │
│   - Mental Model: "Red Team Thinking"                                       │
│   - Mental Model: "Steel Man Argument"                                      │
│   - Mental Model: "Inversion (via negativa)"                                │
│   - MNEMIS pattern: "Skeptic overpenalty on neutral sentiment"              │
│   - Architecture doc: "Agent Authority Levels"                              │
│   - Previous research: "Sentiment Analysis Bias Detection"                  │
│   ... (15 total documents)                                                  │
└─────────────────┬───────────────────────────────────────────────────────────┘
                  │
                  │ RAVEN: "Analyze retrieved documents"
                  ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ STEP 3: RAVEN — Cross-Source Analysis                                      │
│                                                                             │
│ RAVEN uses LLM to synthesize findings across sources:                       │
│                                                                             │
│   def analyze_sources(                                                      │
│       question: str,                                                        │
│       documents: List[Document]                                             │
│   ) -> ResearchFindings:                                                    │
│       # Build context from documents                                        │
│       context = "\n\n".join([                                               │
│           f"Source: {doc.source}\n{doc.content}"                            │
│           for doc in documents                                              │
│       ])                                                                    │
│                                                                             │
│       # LLM analysis with mental model reasoning                            │
│       prompt = f"""                                                         │
│       Research Question: {question}                                         │
│                                                                             │
│       Available Sources:                                                    │
│       {context}                                                             │
│                                                                             │
│       Task:                                                                 │
│       1. Synthesize key insights across sources                             │
│       2. Identify best practices                                            │
│       3. Flag contradictions or gaps                                        │
│       4. Provide actionable recommendations                                 │
│       5. Rate confidence level (0.0-1.0)                                    │
│       """                                                                   │
│                                                                             │
│       response = llm_client.complete(prompt)                                │
│       return parse_research_findings(response)                              │
│                                                                             │
│ LLM ANALYSIS OUTPUT:                                                        │
│   ┌──────────────────────────────────────────────────────┐                  │
│   │ Research Findings                                    │                  │
│   │                                                       │                  │
│   │ KEY INSIGHTS:                                        │                  │
│   │   1. Skeptical analysis should be sentiment-aware    │                  │
│   │      - Neutral reviews need lighter touch            │                  │
│   │      - Positive reviews need stronger challenge      │                  │
│   │      - Negative reviews may already be skeptical     │                  │
│   │                                                       │                  │
│   │   2. Multiple mental models can be combined:         │                  │
│   │      - Devil's Advocate for challenging claims       │                  │
│   │      - Steel Man for finding strongest interpretation│                  │
│   │      - Inversion for spotting missing evidence       │                  │
│   │                                                       │                  │
│   │   3. MNEMIS pattern confirms:                        │                  │
│   │      - Current skeptic agent over-penalizes neutral  │                  │
│   │      - Sentiment-based weighting is recommended      │                  │
│   │                                                       │                  │
│   │ BEST PRACTICES:                                      │                  │
│   │   - Use graduated skepticism (sentiment-dependent)   │                  │
│   │   - Combine 2-3 complementary mental models          │                  │
│   │   - Monitor false positive/negative rates            │                  │
│   │   - A/B test different weighting schemes             │                  │
│   │                                                       │                  │
│   │ CONTRADICTIONS:                                      │                  │
│   │   - Mental Model Library suggests "always challenge" │                  │
│   │   - MNEMIS patterns show "selective challenge" works │                  │
│   │   Resolution: Context-dependent approach             │                  │
│   │                                                       │                  │
│   │ ACTIONABLE RECOMMENDATIONS:                          │                  │
│   │   1. Implement sentiment-aware weighting             │                  │
│   │   2. Add Steel Man model alongside Devil's Advocate  │                  │
│   │   3. A/B test: 50% with new weights, 50% control     │                  │
│   │   4. Monitor for 7 days, compare metrics             │                  │
│   │                                                       │                  │
│   │ CONFIDENCE: 0.87 (high)                              │                  │
│   │ SOURCES CITED: 12/15                                 │                  │
│   │ COST: $0.47 (well under $2.00 budget)                │                  │
│   └──────────────────────────────────────────────────────┘                  │
└─────────────────┬───────────────────────────────────────────────────────────┘
                  │
                  │ RAVEN → MNEMIS: "Store research findings"
                  ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ STEP 4: MNEMIS — Store Research Findings                                   │
│                                                                             │
│ MNEMIS stores findings in Long-term or Permanent tier:                      │
│                                                                             │
│   research_entry = MemoryEntry(                                             │
│       tier=MemoryTier.PERMANENT,  # Cross-project knowledge                 │
│       key="best_practices_skeptical_sentiment_analysis",                    │
│       value={                                                               │
│           "question": "What are best practices...",                         │
│           "findings": {                                                     │
│               "key_insights": [...],                                        │
│               "best_practices": [...],                                      │
│               "recommendations": [...]                                      │
│           },                                                                │
│           "confidence": 0.87,                                               │
│           "sources_cited": 12,                                              │
│           "researched_by": "raven",                                         │
│           "researched_at": "2026-02-08T15:42:33Z",                          │
│           "cost_usd": 0.47,                                                 │
│           "related_projects": ["sentiment_analyzer"]                        │
│       },                                                                    │
│       access_level=MemoryAccessLevel.GAIA  # Available to all projects      │
│   )                                                                         │
│                                                                             │
│   memory_store.write(research_entry)                                        │
│                                                                             │
│ CROSS-PROJECT LINKING:                                                      │
│   MNEMIS automatically tags related projects:                               │
│   - sentiment_analyzer (original requester)                                 │
│   - Any future sentiment analysis projects                                  │
│   - Projects using Devil's Advocate mental model                            │
└─────────────────┬───────────────────────────────────────────────────────────┘
                  │
                  │ RAVEN: "Generate research report"
                  ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ STEP 5: Report Generation & Delivery                                       │
│                                                                             │
│ RAVEN generates markdown report:                                            │
│                                                                             │
│   X:\Projects\_GAIA\_RAVEN\reports\2026-02-08_skeptical_sentiment.md       │
│                                                                             │
│   ┌─────────────────────────────────────────────────┐                       │
│   │ # Research Report: Skeptical Sentiment Analysis │                       │
│   │                                                  │                       │
│   │ **Date:** 2026-02-08                            │                       │
│   │ **Researcher:** RAVEN                            │                       │
│   │ **Confidence:** 87%                              │                       │
│   │ **Cost:** $0.47                                  │                       │
│   │                                                  │                       │
│   │ ## Executive Summary                             │                       │
│   │ [3-sentence summary]                             │                       │
│   │                                                  │                       │
│   │ ## Key Findings                                  │                       │
│   │ [Detailed findings]                              │                       │
│   │                                                  │                       │
│   │ ## Recommendations                               │                       │
│   │ [Actionable steps]                               │                       │
│   │                                                  │                       │
│   │ ## Sources                                       │                       │
│   │ [Bibliography with links]                        │                       │
│   └─────────────────────────────────────────────────┘                       │
│                                                                             │
│ USER NOTIFICATION:                                                          │
│   "Research complete! Report saved to _RAVEN/reports/"                      │
│   "Findings stored in MNEMIS (available to all projects)"                   │
│   "Recommendations ready for implementation"                                │
└─────────────────┬───────────────────────────────────────────────────────────┘
                  │
                  │ Cross-project insights promoted
                  ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ STEP 6: ARGUS — Track Research Quality Over Time                           │
│                                                                             │
│ ARGUS monitors RAVEN's research effectiveness:                              │
│                                                                             │
│   Metrics tracked:                                                          │
│   - Research questions answered                                             │
│   - Average confidence scores                                               │
│   - Implementation rate (were recommendations adopted?)                     │
│   - Cost efficiency (findings value vs. research cost)                      │
│   - Cross-project reuse (how often findings referenced)                     │
│                                                                             │
│   Pattern detection:                                                        │
│   "RAVEN research on sentiment analysis led to 8% accuracy improvement"     │
│   "Recommendation: Increase RAVEN budget for high-value research"           │
└─────────────────────────────────────────────────────────────────────────────┘

CYCLE CONTINUES:
  Research question → MYCEL RAG retrieval → RAVEN analysis →
  Findings stored in MNEMIS → Report generated →
  ARGUS tracks quality → Cross-project insights promoted
```

### RAVEN Research Capabilities

| Capability | Implementation | Benefit |
|------------|----------------|---------|
| **Multi-source RAG** | MYCEL semantic search | Finds relevant docs across GAIA ecosystem |
| **Cross-project memory** | MNEMIS PERMANENT tier | Research benefits all future projects |
| **Mental model reasoning** | ARGUS integration | Uses 59 mental models for analysis |
| **Cost-controlled** | Budget limits per research task | Prevents runaway LLM costs |
| **Quality tracking** | ARGUS telemetry | Improves research methodology over time |

---

## Services Interaction Summary

### Service Dependency Graph

```
                    ┌─────────────────┐
                    │      GAIA       │
                    │  (Governance)   │
                    └────────┬────────┘
                             │
            ┌────────────────┼────────────────┐
            │                │                │
            ▼                ▼                ▼
    ┌───────────┐    ┌───────────┐    ┌───────────┐
    │   MYCEL   │    │  WARDEN   │    │  Registry │
    │  (LLM/RAG)│    │(Governance)│    │  (Index)  │
    └─────┬─────┘    └─────┬─────┘    └─────┬─────┘
          │                │                  │
    ┌─────┴──────┬─────────┴───────┬──────────┴─────┐
    │            │                 │                  │
    ▼            ▼                 ▼                  ▼
┌───────┐   ┌───────┐         ┌───────┐         ┌───────┐
│ LOOM  │   │MNEMIS │         │ ARGUS │         │ ABIS  │
│(Agents)│   │(Memory)│         │(Observe)│        │(Visual)│
└───┬───┘   └───┬───┘         └───┬───┘         └───┬───┘
    │           │                 │                  │
    │           │                 │                  │
    └───────────┴─────────────────┴──────────────────┘
                          │
                          ▼
                ┌─────────────────┐
                │    PRODUCTS     │
                │  (7 projects)   │
                └─────────────────┘
```

### Service Call Matrix

| Caller | Calls | Purpose | Frequency |
|--------|-------|---------|-----------|
| **VULCAN** | MYCEL, WARDEN, Registry | Project creation | Per new project |
| **ABIS** | LOOM, ARGUS, MNEMIS, WARDEN | Visual editing | Per workflow change |
| **LOOM** | MYCEL, MNEMIS | Agent execution | Per agent invocation |
| **ARGUS** | MYCEL, MNEMIS | Pattern detection | Continuous (background) |
| **MNEMIS** | MYCEL | Memory operations | Per read/write |
| **RAVEN** | MYCEL, MNEMIS, ARGUS | Research tasks | On-demand |
| **Products** | MYCEL, MNEMIS, ARGUS | Runtime operations | Continuous |
| **Python Tools** | MYCEL, ARGUS | Ad-hoc tasks | As needed |

### Data Flow Patterns

| Pattern | Flow | Example |
|---------|------|---------|
| **Creation** | User → VULCAN → Services → Product | New project via VULCAN |
| **Modification** | User → ABIS → LOOM → WARDEN → Deploy | Add agent via ABIS |
| **Execution** | Product → LOOM → MYCEL → Response | Agent workflow runs |
| **Monitoring** | Product → ARGUS → MNEMIS → Insights | Telemetry collection |
| **Evolution** | ARGUS → MNEMIS → User → LOOM → Deploy | Pattern-driven improvement |
| **Research** | User → RAVEN → MYCEL/MNEMIS → Report | Knowledge acquisition |

---

## Conclusion

These user flows demonstrate how the GAIA ecosystem provides:

1. **Rapid project creation** (Flow 1): 30 seconds to production-ready scaffold
2. **Visual system editing** (Flow 2): No-code agent composition and modification
3. **Autonomous evolution** (Flow 3): Pattern-driven product improvement
4. **Governance everywhere** (Flow 4): Even standalone tools follow GAIA principles
5. **Cross-project intelligence** (Flow 5): Research benefits entire ecosystem

**Key Principle:** Every interaction strengthens the ecosystem through shared intelligence (MNEMIS), continuous monitoring (ARGUS), and validated evolution (WARDEN).
