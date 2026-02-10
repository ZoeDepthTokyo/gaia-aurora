# GAIA - Constitutional AI Governance Framework

## Role
GAIA is the master meta-layer orchestrating 17 AI projects with constitutional governance, shared intelligence, cross-project memory, and runtime observability. It solves fragmentation by providing unified architecture, shared components, and ecosystem-wide governance.

**Current Version:** v0.5.2 (Phases 1-3 Complete + GECO v1.1.0)

## Constitutional Constraints
1. **Glass-box Transparency**: All agent logic must be inspectable; no opaque black boxes
2. **Human-in-Loop (HITL)**: Destructive operations require explicit user confirmation
3. **Progressive Trust**: System complexity scales with user confidence; start simple, unlock advanced features gradually
4. **Sovereignty**: Users can override any autonomous decision; agents suggest, humans decide
5. **Memory Tier Boundaries**: Memory promotion follows AGENT → PROJECT → GAIA hierarchy; never skip tiers
6. **Governance at Design Time**: Rules and constraints defined before execution, not discovered during runtime
7. **Three Pillars Architecture**: VULCAN creates, LOOM modifies, ARGUS monitors - no overlap, clear boundaries
8. **GECO Compliance**: All components must satisfy 27 GECO requirements before production status
9. **Cost Accountability**: All LLM calls tracked, logged, and attributed to component (via MYCEL)
10. **Immutable Past**: Never rewrite commit history on main branch; destructive git operations require explicit user request

## Quick Start
1. View registry: `cat registry.json`
2. Install pre-commit: `python install_precommit.py`
3. Run GECO audit: `grep "TODO\|FIXME" GECO_AUDIT.md`
4. Launch ARGUS dashboard: `cd _ARGUS && streamlit run dashboard/app.py --server.port 8501`
5. Create new project: `cd _VULCAN && streamlit run ui/main.py`

## Setup & Launch

### Initial Setup
```bash
# From GAIA root
cd /x/Projects/_GAIA

# Install pre-commit hooks for all submodules
python install_precommit.py

# Initialize git submodules (if needed)
git submodule update --init --recursive

# Install core shared libraries
pip install -e _MYCEL  # RAG Intelligence library
pip install -e _LOOM   # Workflow engine
pip install -e _MNEMIS # Memory system
pip install -e _WARDEN # Governance scanner
```

### Registry Management
```bash
# View all registered projects
cat registry.json | jq '.projects[] | {name, version, status}'

# Validate registry schema
python -c "import json; json.load(open('registry.json'))"

# Add new project to registry
# Edit registry.json manually, then validate with WARDEN
python -m warden.cli validate --project .
```

### GECO (Ecosystem Governance) Workflows
```bash
# View GECO audit status
cat GECO_AUDIT.md | grep -A 3 "Status:"

# View GECO review matrix
cat GECO_REVIEW_MATRIX.md

# Check TODO/FIXME items
grep -rn "TODO\|FIXME" . --include="*.py" --include="*.md"
```

### Component Launch Commands
```bash
# ARGUS Dashboard (monitoring + mental models)
cd _ARGUS && streamlit run dashboard/app.py --server.port 8501

# VULCAN Project Creator
cd _VULCAN && streamlit run ui/main.py

# Run WARDEN governance scan
python -m warden.cli validate --project .
```

## Three Pillars Architecture

```
VULCAN (Create)  →  LOOM (Modify)  →  ARGUS (Monitor)
   The Forge         The Workbench       The Watchman
```

**VULCAN** scaffolds new projects with GAIA compliance
**LOOM** provides visual workflow editing and agent orchestration
**ARGUS** monitors ecosystem health and provides mental models

## Directory Structure
```
_GAIA/
├── registry.json              # 17 registered projects
├── GAIA_BIBLE.md             # Constitutional document
├── GAIA_PRD.md               # Product requirements
├── GECO_AUDIT.md             # Governance audit
├── GECO_REVIEW_MATRIX.md     # Implementation matrix
├── VERSION_LOG.md            # Version history
├── CALIBRATION.md            # Phase completion tracking
├── _ARGUS/                   # Monitoring + Mental Models
├── _AURORA/                  # UX/UI Design Lead
├── _LOOM/                    # Workflow Engine
├── _MNEMIS/                  # Cross-Project Memory
├── _MYCEL/                   # Shared RAG Intelligence
├── _VULCAN/                  # Project Creator
├── _WARDEN/                  # Governance & Compliance
├── _RAVEN/                   # Research Agent (spec)
├── _ABIS/                    # Visual System Builder (planning)
└── docs/                     # Ecosystem documentation
```

## Constitutional Principles

1. **Glass-Box Transparency** - All agent logic must be inspectable
2. **Human-in-the-Loop** - No irreversible autonomous actions
3. **Progressive Trust** - Complexity scales with confidence
4. **Sovereignty** - User always has override capability
5. **Three-Tier Memory** - Explicit promotion workflow (AGENT → PROJECT → GAIA)
6. **Governance at Design Time** - Rules defined before execution

## Shared Services (9)

1. **MYCEL** - RAG Intelligence & LLM routing (v0.2.0)
2. **VULCAN** - Project creator & scaffolder (v0.4.0-dev)
3. **LOOM** - Visual workflow engine (v0.1.0)
4. **MNEMIS** - Cross-project memory (v0.1.0)
5. **ARGUS** - Monitoring & mental models (v0.5.1)
6. **WARDEN** - Governance & compliance (v0.3.0)
7. **RAVEN** - Autonomous research (v0.1.0 spec)
8. **AURORA** - UX/UI design lead (v0.1.0)
9. **Mental Model Library** - 59 decision models (v1.0.0)

## Products (8)

1. HART OS (v6.2.8) - Production
2. VIA Intelligence (v6.4) - Production
3. DATA FORGE (v1.1) - Production
4. ABIS Visual Builder (v0.0.1) - Planning
5. PROTEUS/jSeeker (v0.2.1) - Active development
6. GPT_ECHO (v0.1.0) - Active
7. Semantic RM (v2.0.8) - Production
8. Data Cleansing RAG (v0.6) - Active

## Development Workflow

### Creating New Projects
```bash
cd _VULCAN
streamlit run ui/main.py
# Follow HITL questionnaire (7 steps)
# VULCAN auto-generates scaffold + registry entry
```

### Pre-Commit Hooks (All Repos)
```bash
# Install hooks
pre-commit install

# Run manually
pre-commit run --all-files

# Hooks run automatically on git commit:
# - Black (formatting)
# - Ruff (linting)
# - WARDEN validate
# - YAML/JSON validation
```

### Testing Strategy
```bash
# Run tests for specific component
cd _ARGUS && pytest tests/ --cov=argus -v
cd _MYCEL && pytest tests/ --cov=rag_intelligence -v

# Coverage targets:
# - MYCEL: 80% minimum (enforced in CI)
# - VULCAN: 60% minimum (enforced in CI)
# - ARGUS: 80% target
# - WARDEN: TBD
```

## Integration Points

- **Registry**: All components read `registry.json` for ecosystem state
- **MYCEL Bridge**: All components use MYCEL for LLM access
- **MNEMIS Integration**: Pattern storage via memory promotion workflow
- **ARGUS Telemetry**: Build/runtime logging via `argus_telemetry.py`
- **WARDEN Validation**: Pre-commit hooks enforce governance

## Key Files

- `registry.json` - Central source of truth for 17 projects
- `GAIA_BIBLE.md` - Constitutional document (149KB, comprehensive)
- `GECO_AUDIT.md` - Governance audit with 27 requirements
- `GECO_REVIEW_MATRIX.md` - Implementation tracking matrix
- `.pre-commit-config.yaml` - Root pre-commit template
- `install_precommit.py` - Automated hook installation script

## Gotchas

- **Submodules**: Some components (_ARGUS, _MYCEL, etc.) are git submodules - use `git submodule update`
- **MYCEL dependency**: Most projects require MYCEL installed as editable: `pip install -e _MYCEL`
- **Port conflicts**: ARGUS uses 8501, jSeeker uses 8502, avoid collisions
- **Registry sync**: Manual updates to registry.json require WARDEN validation
- **Pre-commit scope**: Root `.pre-commit-config.yaml` is template - each component has own config
- **GECO audit**: 27 requirements, currently 10/27 resolved (v0.5.2)
- **Version management**: VERSION_LOG.md must be updated with each ecosystem release

## DO NOT

- Modify registry.json without running WARDEN validation
- Skip pre-commit hooks installation for new components
- Use Opus model at runtime (budget constraint across ecosystem)
- Write to GAIA-tier memory without explicit promotion workflow
- Create projects outside VULCAN (breaks governance)
- Commit secrets (WARDEN scans for `sk-*` patterns)
