# GAIA Ecosystem References

Central knowledge base for all URLs, documentation links, and external references used across the GAIA ecosystem.

**Last Updated:** February 9, 2026
**Maintained by:** GECO (GAIA Ecosystem Control Operations)

---

## GitHub Repositories

### Organization: ZoeDepthTokyo

| Component | Type | URL | Status |
|-----------|------|-----|--------|
| GAIA (parent) | Governance | https://github.com/ZoeDepthTokyo/GAIA | Active |
| ABIS | Shared Service | https://github.com/ZoeDepthTokyo/gaia-abis | Planning |
| ARGUS | Shared Service | https://github.com/ZoeDepthTokyo/gaia-argus | Active |
| LOOM | Shared Service | https://github.com/ZoeDepthTokyo/gaia-loom | Active |
| MNEMIS | Shared Service | https://github.com/ZoeDepthTokyo/gaia-mnemis | Active |
| MYCEL | Shared Service | https://github.com/ZoeDepthTokyo/gaia-mycel | Active |
| RAVEN | Shared Service | https://github.com/ZoeDepthTokyo/gaia-raven | Planning |
| VULCAN | Shared Service | https://github.com/ZoeDepthTokyo/gaia-vulcan | Active |
| WARDEN | Shared Service | https://github.com/ZoeDepthTokyo/gaia-warden | Active |
| HART OS | Product | https://github.com/ZoeDepthTokyo/hart-os | Complete |

### Repository Naming Convention

- **Shared Services:** `gaia-{name}` (e.g., `gaia-mycel`, `gaia-argus`)
- **Products:** plain name (e.g., `jseeker`, `hart-os`, `data-forge`)
- **Governance:** `gaia-core` for Bible, PRD, registry, architecture docs

---

## Framework Documentation

### Python Ecosystem

| Framework | URL | Used By |
|-----------|-----|---------|
| Python | https://docs.python.org/3/ | All components |
| Streamlit | https://docs.streamlit.io | HART OS, VIA, DATA FORGE, jSeeker, VULCAN, ARGUS |
| Pydantic v2 | https://docs.pydantic.dev/latest/ | All components (data models) |
| pytest | https://docs.pytest.org | All components (testing) |
| FastAPI | https://fastapi.tiangolo.com | ABIS |
| Jinja2 | https://jinja.palletsprojects.com | jSeeker (template rendering) |
| Playwright | https://playwright.dev/python/ | jSeeker (PDF generation) |
| python-docx | https://python-docx.readthedocs.io | jSeeker (DOCX generation) |

### Developer Tools

| Tool | URL | Purpose |
|------|-----|---------|
| Ruff | https://docs.astral.sh/ruff/ | Linting and formatting |
| pre-commit | https://pre-commit.com | Git hook management |
| GitHub Actions | https://docs.github.com/en/actions | CI/CD pipelines |
| GitHub CLI (gh) | https://cli.github.com | Repository management |

---

## API Providers

### LLM Providers

| Provider | Documentation URL | Used By | Models |
|----------|------------------|---------|--------|
| Anthropic (Claude) | https://docs.anthropic.com | jSeeker, RAVEN, DOS | Haiku, Sonnet, Opus |
| OpenAI | https://platform.openai.com/docs | HART OS, VIA, DATA FORGE | GPT-4o, GPT-4o-mini |
| Google Gemini | https://ai.google.dev | VIA, GPT_ECHO | Gemini Pro, Gemini Flash |

### Embedding and Vector Providers

| Provider | Documentation URL | Used By |
|----------|------------------|---------|
| Pinecone | https://docs.pinecone.io | MYCEL (vector storage) |
| OpenAI Embeddings | https://platform.openai.com/docs/guides/embeddings | MYCEL |

---

## GAIA Internal Docs

### Root-Level Documents

| Document | Path | Purpose |
|----------|------|---------|
| GAIA Bible | `GAIA_BIBLE.md` | Constitutional principles, architecture, component specs |
| GECO Audit | `GECO_AUDIT.md` | Ecosystem diagnostic (27 questions traced) |
| Calibration | `CALIBRATION.md` | Reality vs documentation gap tracker |
| Version Log | `VERSION_LOG.md` | Release history (v0.0.0 through v0.5.2) |
| Registry | `registry.json` | Component status, metadata, dependencies for 17 projects |

### docs/ Directory

| Document | Path | Purpose |
|----------|------|---------|
| Logging Standard | `docs/LOGGING_STANDARD.md` | Ecosystem-wide structured logging conventions |
| Logging Rollout | `docs/LOGGING_ROLLOUT.md` | Implementation plan for logging standard |
| Logging Summary | `docs/LOGGING_IMPLEMENTATION_SUMMARY.md` | Logging implementation status |
| GitHub Setup | `docs/GITHUB_SETUP.md` | GitHub organization and repository setup guide |
| GECO Architecture | `docs/GECO_ARCHITECTURE.md` | GECO system design and audit framework |
| Dashboard First | `docs/DASHBOARD_FIRST_APPROACH.md` | Strategy for dashboard-centric development |
| User Flows | `docs/USER_FLOWS.md` | End-to-end user flow definitions |
| Feedback Evaluation | `docs/FEEDBACK_EVALUATION.md` | User feedback analysis framework |
| AURORA Plan | `docs/AURORA_IMPLEMENTATION_PLAN.md` | AURORA component implementation roadmap |
| Dev Session Context | `docs/GAIA_DEV_SESSION_CONTEXT.md` | Session continuity document |
| References KB | `docs/references.md` | This document |
| Skill Registry | `docs/SKILL_REGISTRY.md` | Claude Code skill auto-discovery registry |

### Phase Reports (docs/phase_reports/)

| Document | Purpose |
|----------|---------|
| `PHASE_1_COMPLETE.md` | Phase 1 completion report |
| `PHASE_1_HANDOFF.md` | Phase 1 handoff notes |
| `PHASE_2_IMPLEMENTATION_STATUS.md` | Phase 2 progress tracking |
| `PHASE_2_IMPLEMENTATION_SUMMARY.md` | Phase 2 summary |
| `PHASE_3_IMPLEMENTATION_STATUS.md` | Phase 3 progress tracking |
| `PHASE_3_IMPLEMENTATION_REPORT.md` | Phase 3 detailed report |
| `PHASE_3_HANDOFF.md` | Phase 3 handoff notes |
| `PHASE_3_COMPLETE.md` | Phase 3 completion report |
| `PHASE_3_INDEX.md` | Phase 3 document index |
| `PHASE_2_3_IMPLEMENTATION_SUMMARY.md` | Combined Phases 2-3 summary |
| `PHASE_2_3_CODE_REVIEW.md` | Code review for Phases 2-3 |
| `PHASE_2_3_VALIDATION_SCENARIOS.md` | Validation test scenarios |
| `INTEGRATION_TESTS_SUMMARY.md` | Integration test results |
| `APPENDICES_SUMMARY.md` | GAIA Bible appendix summary |
| `BIBLE_COMPLETION_REPORT.md` | Bible document completion status |

### Strategic Documents (docs/strategic/)

| Document | Purpose |
|----------|---------|
| `SR_COUNCIL_ANALYSIS.md` | Strategic review council analysis |
| `PREDICTIVE_GAIA_SPEC.md` | Predictive specification for GAIA evolution |
| `COUNCIL_COMPETITIVE_ANALYSIS.md` | Competitive landscape analysis |

### Coordination Documents (docs/coordination/)

| Document | Purpose |
|----------|---------|
| `COORDINATION_VIA_CHUNK_SOURCE.md` | Cross-project coordination via chunk sourcing |
| `COORDINATION_VIA_FIXES_COMPLETE.md` | Coordination fix completion tracking |

---

## MCP Plugins (Installed)

Claude Code plugins installed in `C:\Users\Fede\.claude\plugins\`:

| # | Plugin | Author | Version | Description |
|---|--------|--------|---------|-------------|
| 1 | **Context7** | Upstash | latest | Up-to-date documentation lookup. Pulls version-specific docs and code examples from source repositories into LLM context |
| 2 | **Greptile** | Greptile | latest | AI code review agent for GitHub/GitLab. View and resolve PR review comments directly from Claude Code |
| 3 | **Serena** | Oraios | latest | Semantic code analysis via Language Server Protocol. Intelligent code understanding, refactoring suggestions, and codebase navigation |
| 4 | **Figma** | Figma | 1.0.0 | Figma MCP server with skills for implementing designs, Code Connect components, and creating design system rules |
| 5 | **Notion** | Notion Labs | 0.1.0 | Notion Skills + MCP server. Page/database CRUD, task creation, search, and knowledge management |
| 6 | **Pinecone** | Pinecone | 1.1.2 | Vector database integration. Index management, querying, upserting, semantic search, RAG applications, and assistant workflows |
| 7 | **Hugging Face Skills** | Hugging Face | 1.0.0 | AI/ML task skills: dataset creation, model training, evaluation, paper publishing, tool building, and experiment tracking on HF Hub |
| 8 | **Claude Code Setup** | Anthropic | 1.0.0 | Codebase analysis and automation recommendations (hooks, skills, MCP servers, subagents) |
| 9 | **Claude MD Management** | Anthropic | 1.0.0 | CLAUDE.md file maintenance: audit quality, capture session learnings, keep project memory current |
| 10 | **Code Review** | Anthropic | latest | Automated PR code review with multiple specialized agents and confidence-based scoring |

---

## Design References (AURORA)

### Inspiration Library

From `X:\Projects\_GAIA\_AURORA\inspiration\library.json`:

| ID | Name | URL | Tags | Notes |
|----|------|-----|------|-------|
| ref-001 | Godly.website | https://godly.website | landing-pages, premium-design, animation | Curated gallery of premium web designs. Great for landing page inspiration |
| ref-002 | Dribbble | https://dribbble.com | ui-design, components, dashboards, mobile | Design community with high-quality UI shots. Filter by Product Design and Web Design |
| ref-003 | Awwwards | https://www.awwwards.com | premium-design, animation, interaction | Award-winning websites. Focus on Sites of the Day for top-tier execution |
| ref-004 | 21st.dev | https://21st.dev | components, react, shadcn, tailwind | Community component library. Excellent for production-ready UI patterns |
| ref-005 | shadcn/ui | https://ui.shadcn.com | components, react, accessible, design-system | Accessible component library built on Radix UI. Gold standard for component patterns |
| ref-006 | Streamlit Gallery | https://streamlit.io/gallery | streamlit, dashboards, data-apps | Official Streamlit showcase. Useful for understanding framework capabilities |
| ref-007 | OpenHands.dev | https://openhands.dev | node-editor, dark-theme, developer-tool, canvas | Agent IDE with canvas interaction. Reference for ABIS node editor UX |
| ref-008 | Linear | https://linear.app | project-management, keyboard-nav, minimal, fast | Best-in-class keyboard-first UI. Reference for command palette, shortcuts, speed |

### AURORA Sources Catalog

From `X:\Projects\_GAIA\_AURORA\inspiration\sources.md`:

**Design Galleries:**

| Source | URL | When to Use |
|--------|-----|-------------|
| Godly.website | https://godly.website | Premium landing pages, hero sections, marketing sites |
| Dribbble | https://dribbble.com | UI components, dashboards, mobile patterns |
| Awwwards | https://www.awwwards.com | Award-winning interaction design, animation references |
| Mobbin | https://mobbin.com | Mobile app patterns, native UI references |
| Lapa.ninja | https://www.lapa.ninja | Landing page gallery, SaaS design patterns |
| Refero Design | https://refero.design | Real product screenshots categorized by pattern |

**Component Libraries:**

| Source | URL | When to Use |
|--------|-----|-------------|
| 21st.dev | https://21st.dev | Community components, ready-to-adapt UI blocks |
| shadcn/ui | https://ui.shadcn.com | Accessible React components, gold standard patterns |
| Radix UI | https://www.radix-ui.com | Headless accessible primitives |
| Headless UI | https://headlessui.com | Tailwind-integrated accessible components |
| Ant Design | https://ant.design | Enterprise component patterns, data-heavy UIs |

**Streamlit-Specific:**

| Source | URL | When to Use |
|--------|-----|-------------|
| Streamlit Gallery | https://streamlit.io/gallery | Framework capabilities, community apps |
| Streamlit Components | https://streamlit.io/components | Custom component registry |
| Streamlit Extras | https://github.com/arnaudmiribel/streamlit-extras | Community extensions and utilities |

**Icons and Assets:**

| Source | URL | When to Use |
|--------|-----|-------------|
| Lucide Icons | https://lucide.dev | Default icon set for AURORA (consistent, open source) |
| Heroicons | https://heroicons.com | Alternative icon set (Tailwind ecosystem) |
| Phosphor Icons | https://phosphoricons.com | Flexible weight system, good for varied density |

**Color Tools:**

| Source | URL | When to Use |
|--------|-----|-------------|
| Realtime Colors | https://www.realtimecolors.com | Visualize full color palettes on real UI |
| Coolors.co | https://coolors.co | Generate and explore color palettes |
| Color Hunt | https://colorhunt.co | Curated color palette collections |
| WebAIM Contrast | https://webaim.org/resources/contrastchecker | Verify WCAG contrast ratios |

**Typography:**

| Source | URL | When to Use |
|--------|-----|-------------|
| Google Fonts | https://fonts.google.com | Font selection and pairing |
| FontPair | https://www.fontpair.co | Curated font combinations |

**Motion and Animation:**

| Source | URL | When to Use |
|--------|-----|-------------|
| Motion | https://motion.dev | Production animation library, easing references |
| Lottie Files | https://lottiefiles.com | Lightweight JSON animations for loading states |

**Accessibility:**

| Source | URL | When to Use |
|--------|-----|-------------|
| WebAIM | https://webaim.org | Contrast checker, screen reader testing guides |
| Axe DevTools | https://www.deque.com/axe | Automated accessibility auditing |
| WAVE | https://wave.webaim.org | Visual accessibility evaluation |
| A11y Project | https://www.a11yproject.com | Accessibility checklist and resources |

---

## Design System References

| System | URL | Relevance |
|--------|-----|-----------|
| Google Material Design 3 | https://m3.material.io | General component patterns, motion guidelines |
| Apple Human Interface Guidelines | https://developer.apple.com/design/human-interface-guidelines | Platform UX standards, accessibility patterns |
| Ant Design System | https://ant.design | Enterprise data-heavy UI patterns |
| Carbon Design System (IBM) | https://carbondesignsystem.com | Enterprise design tokens, complex data visualization |

---

## Product-Specific References

### jSeeker (Resume Engine)

| Reference | URL/Path | Purpose |
|-----------|----------|---------|
| Anthropic SDK | https://docs.anthropic.com/en/docs/sdks | Claude API calls for resume adaptation |
| Playwright Python | https://playwright.dev/python/ | PDF rendering from HTML templates |
| python-docx | https://python-docx.readthedocs.io | DOCX resume generation |
| ATS Research | `X:\Projects\jSeeker\docs\` | ATS platform profiles and scoring research |

### HART OS (Therapy Scoring)

| Reference | URL/Path | Purpose |
|-----------|----------|---------|
| OpenAI API | https://platform.openai.com/docs | LLM gateway for therapy reasoning |
| Streamlit Docs | https://docs.streamlit.io | Frontend framework |
| PubMed API | https://www.ncbi.nlm.nih.gov/books/NBK25501/ | Evidence validation for therapy techniques |

### VIA Intelligence (Investment Research)

| Reference | URL/Path | Purpose |
|-----------|----------|---------|
| Google Gemini API | https://ai.google.dev | Multi-provider LLM access |
| MYCEL Library | `X:\Projects\_GAIA\_MYCEL` | RAG and embedding for document analysis |

---

## Infrastructure References

| Service | URL | Purpose |
|---------|-----|---------|
| GitHub Organizations | https://docs.github.com/en/organizations | GAIA org management |
| GitHub Secrets | https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions | CI/CD secret management |
| SQLite | https://www.sqlite.org/docs.html | Local persistence (jSeeker, ARGUS) |
| YAML Spec | https://yaml.org/spec/ | Resume blocks, configuration files |

---

## How to Add References

When adding new URLs or references to this knowledge base:

1. Identify the correct section (or create a new one)
2. Include: Name, URL, Purpose/Notes, and which GAIA component uses it
3. Verify the URL is accessible
4. Update the "Last Updated" date at the top

This document is the canonical source for all external references across the GAIA ecosystem. If a URL appears in component code or docs, it should be cataloged here.
