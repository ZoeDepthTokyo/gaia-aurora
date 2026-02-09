# GAIA

**Constitutional AI governance framework for multi-project ecosystems.**

GAIA is a local-first meta-layer that sits above 17 AI projects, providing constitutional governance, shared intelligence, cross-project memory, and runtime observability. It solves the fragmentation problem of running multiple AI-powered tools with different APIs, architectures, and deployment patterns.

**Current version: v0.5.1**

---

## Architecture: Three Pillars

GAIA organizes its core workflow around three operational pillars:

```
VULCAN (Create)  -->  LOOM (Modify)  -->  ARGUS (Monitor)
    The Forge          The Workbench        The Watchman
```

**VULCAN** scaffolds new projects through a guided questionnaire, generating code, configs, and registry entries that comply with GAIA's constitutional rules.

**LOOM** provides a visual agent editor for modifying workflows, agent definitions, and execution graphs across any GAIA-governed project.

**ARGUS** monitors the ecosystem with telemetry, mental model-powered sense-making, layered explainability, and a real-time dashboard.

Supporting these pillars:

- **MYCEL** -- Shared intelligence library (LLM clients, RAG, embeddings)
- **MNEMIS** -- Three-tier cross-project memory with promotion protocol
- **WARDEN** -- Governance enforcement (pre-commit hooks, secrets scanning, compliance)
- **RAVEN** -- Autonomous research agent for investigations and audits

---

## Components

### Shared Services

| Component | Role | Version | Status |
|-----------|------|---------|--------|
| **VULCAN** | Project Creator (The Forge) | 0.4.0-dev | :large_blue_circle: Development |
| **LOOM** | Visual Agent Editor (The Workbench) | 0.1.0 | :large_blue_circle: Development |
| **ARGUS** | Monitoring, Telemetry & Dashboard (The Watchman) | 0.5.1 | :large_blue_circle: Development |
| **MYCEL** | Shared Intelligence Library (LLM, RAG, Embeddings) | 0.2.0 | :green_circle: Active |
| **MNEMIS** | Cross-Project Memory (Mnemosyne) | 0.1.0 | :large_blue_circle: Development |
| **WARDEN** | Governance & Compliance (Secrets, Hooks, Validation) | 0.3.0 | :green_circle: Active |
| **RAVEN** | Autonomous Research Agent | 0.1.0 | :yellow_circle: Defined |
| **AURORA** | UX/UI Lead & Design Systems | 0.1.0 | :large_blue_circle: Development |
| **Mental Models** | Decision Support Framework (59 models) | 1.0.0 | :green_circle: Active |

### Products

| Product | Domain | Version | Status |
|---------|--------|---------|--------|
| **HART OS** | AI-Assisted Therapy | 6.2.8 | :green_circle: Production |
| **VIA Intelligence** | Investment Research & Synthesis | 6.4 | :green_circle: Production |
| **DATA FORGE** | Data Processing & Compilation | 1.1 | :green_circle: Production |
| **jSeeker** | Resume Adaptation & ATS Optimization | 0.2.1 | :green_circle: Active |
| **GPT_ECHO** | ChatGPT Conversation Archaeology | 0.1.0 | :orange_circle: Stale |
| **THE PALACE** | Multi-Agent Case Study | 1.0 | :white_check_mark: Complete |
| **DOS** | Multi-Agent Decision System | 0.0.1 | :yellow_circle: Planning |
| **ABIS** | No-Code Agent System Builder | 0.0.1 | :yellow_circle: Planning |

---

## Submodules

GAIA uses git submodules for its core shared services. Each submodule has its own repository under [ZoeDepthTokyo](https://github.com/ZoeDepthTokyo/).

| Submodule | Repository |
|-----------|------------|
| `_ABIS` | [gaia-abis](https://github.com/ZoeDepthTokyo/gaia-abis) |
| `_ARGUS` | [gaia-argus](https://github.com/ZoeDepthTokyo/gaia-argus) |
| `_LOOM` | [gaia-loom](https://github.com/ZoeDepthTokyo/gaia-loom) |
| `_MNEMIS` | [gaia-mnemis](https://github.com/ZoeDepthTokyo/gaia-mnemis) |
| `_MYCEL` | [gaia-mycel](https://github.com/ZoeDepthTokyo/gaia-mycel) |
| `_RAVEN` | [gaia-raven](https://github.com/ZoeDepthTokyo/gaia-raven) |
| `_VULCAN` | [gaia-vulcan](https://github.com/ZoeDepthTokyo/gaia-vulcan) |
| `_WARDEN` | [gaia-warden](https://github.com/ZoeDepthTokyo/gaia-warden) |

---

## Getting Started

Clone the repository with all submodules:

```bash
git clone --recurse-submodules https://github.com/ZoeDepthTokyo/GAIA.git
cd GAIA
```

If you already cloned without submodules:

```bash
git submodule update --init --recursive
```

### Requirements

- Python 3.10+
- Each component has its own `requirements.txt`

---

## Key Documents

| Document | Description |
|----------|-------------|
| [`GAIA_BIBLE.md`](GAIA_BIBLE.md) | Constitutional master document -- 11 chapters covering vision, architecture, trust contracts, and operational guides (~41K tokens) |
| [`CALIBRATION.md`](CALIBRATION.md) | Reality check -- maps claims vs. operational state, tracks the gap between design and implementation |
| [`GECO_AUDIT.md`](GECO_AUDIT.md) | Full ecosystem diagnostic -- 27-question audit across all components with phased remediation plan |
| [`VERSION_LOG.md`](VERSION_LOG.md) | Detailed changelog from v0.0.0 (pre-GAIA) through current release |
| [`registry.json`](registry.json) | Machine-readable registry of all 17 projects with versions, status, dependencies, and paths |

---

## Constitutional Principles

GAIA operates under five trust contracts, mechanically enforced:

1. **GAIA Never Lies** -- Explicit uncertainty, immutable logs, confidence tracking
2. **GAIA Admits Limits** -- Authority boundaries, read-only contracts, escalation paths
3. **GAIA Degrades Gracefully** -- No silent failures, structured fallbacks
4. **GAIA Learns Explicitly** -- Proposal-based learning, approval gates, provenance
5. **GAIA Remains Inspectable** -- Decision trails, rationale logging, transparency metrics

GAIA has reflective cognition (observe, propose, surface patterns) but is prohibited from executive cognition (autonomous action, silent modification). The human always decides.

---

## License

Private repository. All rights reserved.
