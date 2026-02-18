# GAIA - Constitutional AI Governance Framework

## Role
GAIA is the master meta-layer orchestrating 18 projects (9 shared services + 8 products + 1 library) with constitutional governance, shared intelligence, cross-project memory, and runtime observability. It solves fragmentation by providing unified architecture, shared components, and ecosystem-wide governance.

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
6. Launch GAIA Simulator: `cd _ARGUS/sim && python -m streamlit run gaia_sim.py --server.port 8503`

## Agent Onboarding Protocol

When starting work on any GAIA component:

1. **Read GAIA_MANIFEST.md** — canonical state, architecture, cascade rules (~120 lines)
2. **Read target component CLAUDE.md** — component-specific constraints and cascade map
3. **Check MANIFEST "Active Priorities"** — understand current focus
4. **Before finishing**: Run `/reconciling-gaia` or remind user to run it

Do NOT read GAIA_BIBLE.md, GAIA_PRD.md, or GECO_AUDIT.md unless:
- The task specifically requires constitutional interpretation (use BIBLE)
- The task requires product requirements detail (use PRD)
- The task requires governance audit status (use GECO_AUDIT)

If MANIFEST `last_reconciled` is more than 3 days old, run `/reconciling-gaia --dry-run` first to check for drift.

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

# GAIA Ecosystem Simulator (test any intent against governance rules)
cd _ARGUS/sim && python -m streamlit run gaia_sim.py --server.port 8503

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
├── GAIA_MANIFEST.md          # Canonical state (~120 lines, read FIRST)
├── registry.json              # 18 registered projects
├── GAIA_BIBLE.md             # Constitutional document
├── GAIA_PRD.md               # Product requirements
├── GECO_AUDIT.md             # Governance audit
├── GECO_REVIEW_MATRIX.md     # Implementation matrix
├── VERSION_LOG.md            # Version history
├── CALIBRATION.md            # Phase completion tracking (archived)
├── runtime/                   # Background tasks + change tracker
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

For full component list with versions, status, and dependencies see **GAIA_MANIFEST.md** Component State Table.

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
# - ARGUS: 80% target (--cov-fail-under=50 in CI)
# - LOOM: 50% minimum (enforced in CI)
# - MNEMIS: 50% minimum (enforced in CI)
# - WARDEN: 50% minimum (enforced in CI)

# Run spec tests across all components (avoid module name collisions)
pytest _ARGUS/tests/test_spec_core_behaviors.py _LOOM/tests/test_spec_core_behaviors.py _MNEMIS/tests/test_spec_behaviors.py _AURORA/tests/test_spec_core_behaviors.py --import-mode=importlib
```

## Integration Points

- **Cascade Propagation**: `/reconciling-gaia` skill propagates component changes to ecosystem docs
- **Registry**: All components read `registry.json` for ecosystem state
- **MYCEL Bridge**: All components use MYCEL for LLM access
- **MNEMIS Integration**: Pattern storage via memory promotion workflow
- **ARGUS Telemetry**: Build/runtime logging via `argus_telemetry.py`
- **WARDEN Validation**: Pre-commit hooks enforce governance

## Key Files

- `GAIA_MANIFEST.md` - Canonical state document (~120 lines, read FIRST)
- `registry.json` - Central source of truth for 18 projects
- `GAIA_BIBLE.md` - Constitutional document (149KB, comprehensive)
- `GECO_AUDIT.md` - Governance audit with 27 requirements
- `GECO_REVIEW_MATRIX.md` - Implementation tracking matrix
- `.pre-commit-config.yaml` - Root pre-commit template
- `install_precommit.py` - Automated hook installation script

## Gotchas

- **Registry hook**: `registry.json` edits are BLOCKED by PreToolUse hook — get user approval first
- **Change tracking**: Edits to `_[A-Z]+/` paths auto-log to `.gaia_changes` via PostToolUse hook
- **Cascade maps**: Component CLAUDE.md files have `<!-- CASCADE_MAP -->` sections parsed by `/reconciling-gaia`
- **Submodules**: Some components (_ARGUS, _MYCEL, etc.) are git submodules - use `git submodule update`
- **Submodule commits**: Commit inside submodule first (`cd _ARGUS && git commit`), then `git add _ARGUS && git commit` from GAIA root
- **Pre-commit Python**: Some submodule hooks require Python 3.11; `--no-verify` needed on Python 3.14 systems
- **MYCEL dependency**: Most projects require MYCEL installed as editable: `pip install -e _MYCEL`
- **Port conflicts**: ARGUS=8501, jSeeker=8502, Simulator=8503, JobPulse=8504 — avoid collisions
- **JobPulse Dashboard**: `X:\Projects\JobPulse\` — standalone Streamlit+Plotly app, reads RAVEN data, port 8504
- **Registry sync**: Manual updates to registry.json require WARDEN validation
- **Pre-commit scope**: Root `.pre-commit-config.yaml` is template - each component has own config
- **GECO audit**: 27 requirements, currently 10/27 resolved (v0.5.2)
- **Version management**: VERSION_LOG.md must be updated with each ecosystem release
- **pytest cross-submodule**: Same-named test files across submodules cause import collisions — use `--import-mode=importlib`
- **`.claude/` gitignored**: Skills/settings files need `git add -f` to stage
- **GWT coverage**: Run `python runtime/scripts/gwt_coverage.py` (or `--json`) to check spec-test coverage ratio

## Relevant Skills

| Task | Skill | Phase |
|------|-------|-------|
| Starting a new feature | `/creating-change` | OPENING |
| Component orientation | `/orienting-to-component` | OPENING |
| List all skills | `/listing-skills` | OPENING |
| End of session | `/reconciling-gaia` | CLOSING |
| Archive completed change | `/archiving-change` | CLOSING |
| Validate spec format | `/validating-specs` | CLOSING |
| Check governance status | `/checking-geco-status` | CONTEXT |
| Review UI design | `/reviewing-design` | CONTEXT |
| UX quality audit | `/auditing-ux` | CONTEXT |
| Accessibility check | `/checking-accessibility` | CONTEXT |
| Explain unfamiliar code | `/explaining-code` | CONTEXT |
| Autonomous iteration | `/running-autonomous-loop` | CONTEXT |
| Registry validation | `/syncing-registry` | CONTEXT |
| Multi-agent coordination | `/orchestrating-agents` | CONTEXT |
| External research | `/researching` | CONTEXT |
| E2E testing (Streamlit) | `/testing-webapp` | CONTEXT |

## DO NOT

- Modify registry.json directly (blocked by hook) — use `/syncing-registry` or get user approval
- Skip pre-commit hooks installation for new components
- Use Opus model at runtime (budget constraint across ecosystem)
- Write to GAIA-tier memory without explicit promotion workflow
- Create projects outside VULCAN (breaks governance)
- Commit secrets (WARDEN scans for `sk-*` patterns)
