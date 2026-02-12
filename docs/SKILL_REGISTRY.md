# GAIA Skill Registry

Auto-discovery registry for all Claude Code skills, agents, plugins, and commands available in the GAIA ecosystem.

**Last Updated:** February 9, 2026
**Source:** Scanned from `C:\Users\Fede\.claude\` (skills, agents, plugins)

---

## User-Level Skills (Global)

Custom skills installed at `C:\Users\Fede\.claude\skills\`:

| Skill | Path | Type | Model | Description |
|-------|------|------|-------|-------------|
| **explain-only** | `~/.claude/skills/explain-only/` | Response Style | - | Forces verbal explanations only. No file creation, no plan mode, no Write/Edit tools. Keeps responses under 500 words unless asked for detail. Use code blocks for examples but never save them |
| **phase-update** | `~/.claude/skills/phase-update/` | Documentation | - | Workflow for updating project phases: checks status of current phase docs, updates CHANGELOG.md with completed items, generates next phase plan with dependencies/blockers, and verifies all changes saved |
| **debug-explorer** | `~/.claude/skills/debug-explorer/` | Debugging | - | Deep exploration of complex bugs. Spawns Task agent (Explore type) to identify bottlenecks, blocking I/O, and memory issues. Reports findings BEFORE making changes. Proposes fix and waits for user approval |
| **doc-sync** | `~/.claude/skills/doc-sync/` | Documentation | - | Automatically syncs documentation with code changes. Updates relevant docs/ files, adds CHANGELOG.md entries, updates README sections, and ensures docstrings match implementation |

---

## GAIA Agent Definitions

Custom agents installed at `C:\Users\Fede\.claude\agents\`:

### GAIA Ecosystem Agents

| Agent | File | Model | Tools | Description |
|-------|------|-------|-------|-------------|
| **aurora-ux-lead** | `aurora-ux-lead.md` | Sonnet | Read, Write, Edit, Grep, Glob, Bash, WebSearch, WebFetch | AURORA -- GAIA UX/UI Lead. Oversees design systems, creates UX specifications, manages inspiration libraries, builds prototypes, and learns from user feedback. 6-phase workflow: PRD Intake, Inspiration, UX Spec, Build Order, Refine, Deploy. Integrates with RAVEN for research and MNEMIS for pattern storage |

### HART OS Agents

| Agent | File | Model | Tools | Description |
|-------|------|-------|-------|-------------|
| **product-owner** | `product-owner.md` | Sonnet | Read, Grep, Glob | Strategic product owner for HART OS. Guards product vision, maintains PRD, prioritizes features using RICE/MoSCoW, defines success criteria, prevents scope creep. Uses Feature Assessment output format with recommendation, priority, rationale, and success criteria |
| **planner** | `planner.md` | Sonnet | Read, Grep, Glob | Implementation planning specialist. Analyzes requirements, breaks complex features into manageable steps, identifies dependencies and risks, suggests optimal implementation order. Outputs structured Implementation Plans with phases and step breakdowns |
| **architect** | `architect.md` | Sonnet | Read, Grep, Glob | Software architect for HART OS. Designs system architecture, evaluates technical trade-offs, ensures codebase consistency, plans for scalability. Outputs Architecture Decision Records (ADRs) with context, options, decision, and consequences |
| **senior-python-ml-engineer** | `senior-python-ml-engineer.md` | Sonnet | Read, Write, Edit, Bash, Grep, Glob | Expert Python/ML engineer. Implements business logic, writes type-safe documented code, reviews for quality and security, optimizes performance. Enforces 80%+ test coverage, 100% type hints, zero Spanish in Python, no hardcoded keys |
| **ux-design-lead** | `ux-design-lead.md` | Sonnet | Read, Write, Edit, Grep, Glob | Senior UX/UI design lead for HART OS. Designs user flows, creates wireframes, implements Streamlit UI, ensures WCAG 2.1 AA accessibility. Focused on reducing friction for the primary user (Spanish-speaking art therapist) |
| **tdd-guide** | `tdd-guide.md` | Sonnet | Read, Write, Edit, Bash, Grep | Test-Driven Development specialist. Enforces write-tests-first methodology, guides Red-Green-Refactor cycle, writes comprehensive test suites, ensures 80%+ coverage. Covers edge cases: null/empty, boundaries, errors, invalid types |
| **code-reviewer** | `code-reviewer.md` | Sonnet | Read, Grep, Glob, Bash | Code review specialist. Categorizes findings as CRITICAL (blocks merge), WARNING (should fix), or SUGGESTION (consider). Checks for hardcoded secrets, SQL injection, missing validation, Spanish in Python, missing tests. Outputs verdict: APPROVE / APPROVE WITH CONCERNS / BLOCK |
| **security-reviewer** | `security-reviewer.md` | Sonnet | Read, Grep, Glob, Bash | Security specialist for healthcare applications. OWASP Top 10 compliance, PHI protection, API key audit, injection scanning. Outputs security verdicts: PASS / CAUTION / BLOCK with CVSS-style severity estimates |
| **doc-updater** | `doc-updater.md` | Haiku | Read, Write, Edit, Grep, Glob | Documentation specialist. Keeps docs in sync with code after feature implementation, bug fixes, API changes, config changes, and version bumps. Maintains PRD version history and changelog. Uses lightweight Haiku model for cost efficiency |
| **build-error-resolver** | `build-error-resolver.md` | Sonnet | Read, Write, Edit, Bash, Grep, Glob | Build and test error specialist. Quickly resolves CI failures, import errors, test issues, type errors, and linting errors. Follows identify-locate-fix-verify process. Includes quick fix lookup table for common errors |
| **quick-helper** | `quick-helper.md` | Haiku | Read, Grep, Glob, WebSearch, WebFetch | Quick-response assistant for verbal answers only. Never creates files or enters plan mode. User-invokable only (not auto-triggered). Concise direct answers with code block examples when helpful |

---

## AURORA Slash Commands

AURORA's 6-phase workflow provides these invokable commands:

| Command | Phase | Description |
|---------|-------|-------------|
| `/aurora-intake` | Phase 1 | PRD intake and UX requirements extraction. Analyzes product requirements document to identify UX-relevant features, user personas, and constraints |
| `/aurora-inspire` | Phase 2 | Inspiration and reference gathering. Curates design references from the inspiration library, tasks RAVEN for missing sources, aligns direction with user |
| `/aurora-spec` | Phase 3 | UX specification creation. 7-pass analysis: mental model, information architecture, affordance, progressive disclosure, feedback, interaction, accessibility |
| `/aurora-build` | Phase 4 | Frontend prototyping. Translates UX spec into numbered build prompts for implementation |
| `/aurora-refine` | Phase 5 | Usability refinement. UX engineering loop: build, review, gather feedback, iterate |
| `/aurora-brand` | Phase 6 | Brand kit creation. Finalizes design tokens, Figma sync, documentation, and handoff |

---

## Plugin Skills (Installed)

### Anthropic Official Plugins

#### claude-code-setup (v1.0.0)

| Skill/Command | Type | Description |
|---------------|------|-------------|
| `/claude-automation-recommender` | Skill | Analyzes codebases and recommends tailored Claude Code automations: hooks, skills, MCP servers, and subagent templates |

#### claude-md-management (v1.0.0)

| Skill/Command | Type | Description |
|---------------|------|-------------|
| `/revise-claude-md` | Command | Revise and update CLAUDE.md files with improved instructions |
| `claude-md-improver` | Skill | Audit CLAUDE.md quality, capture session learnings, keep project memory current with quality criteria and templates |

#### code-review (latest)

| Skill/Command | Type | Description |
|---------------|------|-------------|
| `/code-review` | Command | Automated PR code review using multiple specialized agents with confidence-based scoring |

### Figma Plugin (v1.0.0)

| Skill/Command | Type | Description |
|---------------|------|-------------|
| `implement-design` | Skill | Implement a Figma design in code. Reads Figma file via MCP, generates matching frontend code |
| `code-connect-components` | Skill | Map Figma components to code components for design-to-code consistency |
| `create-design-system-rules` | Skill | Create design system rules from Figma files for consistent implementation |

### Notion Plugin (v0.1.0)

**Commands:**

| Command | Description |
|---------|-------------|
| `/create-task` | Create a task in Notion with properties and content |
| `/create-page` | Create a new Notion page with rich content |
| `/create-database-row` | Insert a new row into a Notion database |
| `/database-query` | Query a Notion database with filters and sorts |
| `/find` | Find a specific Notion page or database by name |
| `/search` | Search across Notion workspace for pages and databases |

**Skills:**

| Skill | Description |
|-------|-------------|
| `knowledge-capture` | Capture and organize knowledge from conversations into Notion pages |
| `meeting-intelligence` | Process meeting notes and extract action items into Notion |
| `research-documentation` | Document research findings with structured Notion pages |
| `spec-to-implementation` | Convert Notion specs into implementation tasks and tracking |

### Pinecone Plugin (v1.1.2)

**Commands:**

| Command | Description |
|---------|-------------|
| `/quickstart` | Generate AGENTS.md files and initialize Python projects for Pinecone development |
| `/query` | Quickly explore and query Pinecone indexes |
| `/assistant-create` | Create a new Pinecone assistant |
| `/assistant-chat` | Chat with a Pinecone assistant |
| `/assistant-upload` | Upload files to a Pinecone assistant |
| `/assistant-sync` | Sync data with a Pinecone assistant |
| `/assistant-context` | Manage assistant context |
| `/assistant-list` | List available Pinecone assistants |
| `/join-discord` | Join the Pinecone Discord community |
| `/help` | Show Pinecone plugin help and available commands |

**Skills:**

| Skill | Description |
|-------|-------------|
| `assistant` | Build and manage Pinecone assistants for RAG applications |

**MCP Tools:**

| Tool | Description |
|------|-------------|
| `search-docs` | Search Pinecone documentation |
| `list-indexes` | List all Pinecone indexes |
| `describe-index` | Describe index configuration |
| `describe-index-stats` | Get index statistics and namespace info |
| `create-index-for-model` | Create index with integrated embedding inference |
| `upsert-records` | Insert or update records in an index |
| `search-records` | Semantic search for similar records |
| `rerank-documents` | Rerank documents against a query |
| `cascading-search` | Search across multiple indexes with deduplication and reranking |

### Hugging Face Skills (v1.0.0)

| Skill | Description |
|-------|-------------|
| `hugging-face-cli` | Hugging Face CLI operations for hub interaction |
| `hugging-face-datasets` | Create and manage datasets on Hugging Face Hub |
| `hugging-face-evaluation` | Evaluate model performance with benchmarks and metrics |
| `hugging-face-jobs` | Manage training and inference jobs on HF infrastructure |
| `hugging-face-model-trainer` | Fine-tune and train models with HF Transformers |
| `hugging-face-paper-publisher` | Publish research papers on Hugging Face |
| `hugging-face-tool-builder` | Build custom tools for HF ecosystem |
| `hugging-face-trackio` | Track experiments and metrics with TrackIO |
| `hf-mcp` | Hugging Face MCP server integration |

### Greptile Plugin (latest)

**MCP Tools:**

| Tool | Description |
|------|-------------|
| `list_custom_context` | List organization custom context with filtering |
| `get_custom_context` | Get detailed custom context with evidence and comments |
| `search_custom_context` | Search custom context by text content |
| `list_merge_requests` | List PRs/MRs with filters (repo, branch, author, state) |
| `list_pull_requests` | Alias for list_merge_requests |
| `get_merge_request` | Get detailed PR info with review analysis |
| `list_merge_request_comments` | Get all comments for a PR including Greptile reviews |
| `list_code_reviews` | List code reviews with status filtering |
| `get_code_review` | Get detailed code review body and progress |
| `trigger_code_review` | Trigger a new code review for a PR |
| `search_greptile_comments` | Search across all Greptile review comments |
| `create_custom_context` | Create new custom context for the organization |

### Context7 Plugin (latest)

**MCP Tools:**

| Tool | Description |
|------|-------------|
| `resolve-library-id` | Resolve a library name to a Context7-compatible library ID |
| `query-docs` | Retrieve up-to-date documentation and code examples for any library |

### Serena Plugin (latest)

Semantic code analysis MCP server providing:
- Intelligent code understanding via Language Server Protocol
- Refactoring suggestions
- Codebase navigation and symbol resolution

---

## Planned Skills (Not Yet Implemented)

These skills are planned for future GAIA phases:

| Skill | Component | Description | Priority |
|-------|-----------|-------------|----------|
| WARDEN scan | WARDEN | Invoke compliance scan on demand. Check for secrets, validate CLAUDE.md, run pre-commit hooks across selected projects | High |
| ARGUS telemetry | ARGUS | Query ecosystem health metrics. Pull cost tracking, build status, test coverage from ARGUS dashboard data | High |
| MNEMIS memory | MNEMIS | Cross-session pattern retrieval. Query the memory hierarchy for patterns, decisions, and learnings from past sessions | Medium |
| VULCAN scaffold | VULCAN | Create new project from template. Run VULCAN's questionnaire flow and generate project scaffolding with adapters | Medium |
| RAVEN research | RAVEN | Autonomous research task. Dispatch ad-hoc investigations (competitive analysis, dependency audits, best practices) | Medium |
| LOOM workflow | LOOM | Visual workflow execution. Trigger and monitor agent workflows defined in LOOM's workflow engine | Low |
| ABIS builder | ABIS | No-code system builder. Visual agent composition and pipeline construction | Low |
| ECHO search | GPT_ECHO | ChatGPT conversation archaeology. Search and retrieve insights from historical ChatGPT conversations | Low |

---

## Skill Discovery Protocol

When a new skill, agent, or plugin is added to the GAIA ecosystem:

1. **Install** the skill/agent/plugin in the appropriate directory
2. **Document** it in this registry with: name, path, type, model, tools, and description
3. **Verify** it works by invoking it in a test session
4. **Cross-reference** any URLs in `docs/references.md`

### Directory Conventions

| Type | Location | Naming |
|------|----------|--------|
| User Skills | `~/.claude/skills/{skill-name}/SKILL.md` | Lowercase, hyphenated |
| User Agents | `~/.claude/agents/{agent-name}.md` | Lowercase, hyphenated |
| Plugins | `~/.claude/plugins/cache/claude-plugins-official/{name}/` | Plugin-defined |
| Project Skills | `{project}/.claude/skills/{name}/SKILL.md` | Per-project scope |

### Agent YAML Frontmatter Schema

```yaml
---
name: agent-name              # Lowercase, hyphenated identifier
description: >                # Multi-line description (shown in agent picker)
  What this agent does...
tools: Read, Write, Edit      # Comma-separated tool list
model: sonnet                 # sonnet, haiku, or opus
user-invokable: true          # Optional: only user can trigger (not auto)
disable-model-invocation: true # Optional: prevent model from auto-triggering
---
```

---

## Summary Statistics

| Category | Count |
|----------|-------|
| User Skills | 4 |
| User Agents | 12 |
| AURORA Slash Commands | 6 |
| Installed Plugins | 10 |
| Plugin Skills | 18 |
| Plugin Commands | 20 |
| Plugin MCP Tools | 27 |
| Planned Skills | 8 |
| **Total Registered Capabilities** | **105** |
