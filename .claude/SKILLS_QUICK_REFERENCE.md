# GAIA Skills Quick Reference

## Overview
This guide helps you discover and learn GAIA skills progressively. Skills are organized by use case and difficulty level.

**How to use a skill**: Type `/skill-name` in Claude Code chat

---

## 🎯 Start Here (Essential Skills)

### `/component-overview <component>`
**When to use**: First time working with a GAIA component
**What it does**: Quick orientation showing status, version, quick start, key commands
**Example**: `/component-overview _ARGUS`
**Learn more**: `X:\Projects\_GAIA\.claude\skills\component-overview\SKILL.md`

### `/registry-sync`
**When to use**: After updating component versions or registry.json
**What it does**: Validates registry schema, runs WARDEN checks, updates VERSION_LOG
**Example**: `/registry-sync --validate-only`
**Learn more**: `X:\Projects\_GAIA\.claude\skills\registry-sync\SKILL.md`

### `/geco-status`
**When to use**: Weekly sprint planning, before releases
**What it does**: Dashboard showing progress on 27 GECO requirements
**Example**: `/geco-status --component _MYCEL`
**Learn more**: `X:\Projects\_GAIA\.claude\skills\geco-status\SKILL.md`

---

## 📚 Learning & Understanding

### `/explain-code [file|function] [--level simple|detailed|expert]`
**When to use**: Understanding GAIA code patterns, integration points
**What it does**: GAIA-aware code explanations with constitutional context
**Examples**:
- `/explain-code utils.py:calculate` — Simple function explanation
- `/explain-code jseeker/adapter.py --level detailed` — Module deep dive
- `/explain-code --level expert` — System architecture
**Learn more**: `X:\Projects\_GAIA\.claude\skills\explain-code\SKILL.md`

---

## 🎨 AURORA UX/UI Design

### `/ux-audit <component>`
**When to use**: Before launching new UI, after UX feedback sessions
**What it does**: 7-pass UX analysis + constitutional compliance
**Passes**:
1. Mental Model Alignment
2. Information Architecture
3. Affordance & Action
4. Progressive Disclosure
5. System Feedback
6. Interaction Patterns
7. Accessibility (WCAG 2.1 AA)
**Example**: `/ux-audit _ARGUS`
**Learn more**: `X:\Projects\_GAIA\.claude\skills\ux-audit\SKILL.md`

### `/design-review <component> [--phase spec|prototype|implementation]`
**When to use**: Reviewing designs against AURORA design system
**What it does**: Validates 30% master DNA + 70% brand variation
**Checks**:
- Typography scale (16px base, 1.25 ratio)
- Spacing grid (4px base)
- Breakpoints (mobile/tablet/desktop)
- WCAG 2.1 AA compliance
- Brand consistency
**Example**: `/design-review _VULCAN --phase implementation`
**Learn more**: `X:\Projects\_GAIA\.claude\skills\design-review\SKILL.md`

### `/accessibility-check <component> [--level AA|AAA]`
**When to use**: Before production launch, after UI changes
**What it does**: WCAG 2.1 compliance audit (8 automated checks + manual guide)
**Checks**:
1. Color Contrast (4.5:1 for normal, 3:1 for large)
2. Keyboard Navigation (Tab, Enter, Escape)
3. Focus Indicators (≥2px, high contrast)
4. Alt Text (images, icons, charts)
5. Form Labels (all inputs labeled)
6. Semantic HTML (proper elements, ARIA)
7. Heading Hierarchy (h1 → h2 → h3)
8. Link Purpose (descriptive text)
**Example**: `/accessibility-check _ARGUS`
**Learn more**: `X:\Projects\_GAIA\.claude\skills\accessibility-check\SKILL.md`

---

## 🛠️ Utilities (Claude Code)

### `/claude-md-improver`
**When to use**: Setting up new project, maintaining CLAUDE.md
**What it does**: Audits CLAUDE.md quality, adds Quick Start/Setup/Gotchas
**Example**: `/claude-md-improver` (auto-detects CLAUDE.md in current directory)
**Learn more**: Built-in skill from claude-md-management plugin

### `/revise-claude-md`
**When to use**: End of session, after learning new patterns
**What it does**: Updates CLAUDE.md with learnings from current session
**Example**: `/revise-claude-md`
**Learn more**: Built-in skill from claude-md-management plugin

### `/claude-automation-recommender`
**When to use**: New project setup, optimizing workflows
**What it does**: Recommends hooks, subagents, skills, plugins for your codebase
**Example**: `/claude-automation-recommender`
**Learn more**: Built-in skill from claude-code-setup plugin

---

## 🔧 Advanced (As Needed)

### Pinecone Assistant Skills
**When to use**: Working with vector databases, document Q&A

- `/pinecone:assistant-create` — Create assistant for doc Q&A
- `/pinecone:assistant-upload` — Upload files to knowledge base
- `/pinecone:assistant-chat` — Chat with assistant (citations included)
- `/pinecone:query` — Query index directly

**Learn more**: Use `/pinecone:help` for quickstart

### Notion Integration Skills
**When to use**: Task tracking, documentation publishing

- `/Notion:create-task` — Create task in Notion
- `/Notion:search` — Search Notion workspace
- `/Notion:database-query` — Query Notion database

**Learn more**: Built-in Notion plugin skills

### Hugging Face Skills
**When to use**: ML model training, dataset management

- `/hugging-face-model-trainer` — Train/fine-tune models on HF Jobs
- `/hugging-face-datasets` — Create and manage datasets
- `/hugging-face-evaluation` — Add eval results to model cards

**Learn more**: Built-in huggingface-skills plugin

### Figma Integration Skills
**When to use**: Design-to-code workflows (AURORA)

- `/figma:implement-design` — Translate Figma to code
- `/figma:code-connect-components` — Connect designs to components
- `/figma:create-design-system-rules` — Generate design rules

**Prerequisites**: Install Figma MCP server (see COMPREHENSIVE_AUTOMATION_IMPLEMENTATION.md)

---

## 🎯 Skill Learning Path

### Week 1: Essentials
1. Try `/component-overview` on each GAIA component
2. Run `/registry-sync --validate-only` to check status
3. Check `/geco-status` to see compliance gaps
4. Use `/explain-code` on a simple function

### Week 2: Quality & Review
5. Run `/ux-audit` on a Streamlit dashboard
6. Try `/accessibility-check` on the same dashboard
7. Use `/design-review` to validate design system compliance
8. Run `/claude-md-improver` on your project

### Week 3: Automation
9. Use `/claude-automation-recommender` to optimize setup
10. Try `/revise-claude-md` after a learning session
11. Explore Pinecone skills if using vector search
12. Explore Notion skills if using task tracking

### Week 4: Advanced
13. Try Figma skills if doing AURORA work
14. Explore Hugging Face skills if doing ML work
15. Create your own custom skill (see COMPREHENSIVE_AUTOMATION_IMPLEMENTATION.md)

---

## 📋 Skill Cheat Sheet

### Quick Validation
```bash
/geco-status --component _MYCEL
/registry-sync --validate-only
/accessibility-check _ARGUS --automated-only
```

### Pre-Release Checklist
```bash
/ux-audit <component>
/accessibility-check <component>
/design-review <component> --phase implementation
/geco-status --component <component>
```

### New Component Setup
```bash
/component-overview <component>
/claude-md-improver
/claude-automation-recommender
```

### Learning Codebase
```bash
/component-overview <component>
/explain-code <file> --level detailed
/explain-code --level expert  # System architecture
```

### AURORA Workflow
```bash
# Full 6-phase design process (use AURORA agent):
claude --agent aurora-ux-lead
/aurora-intake my-project
/aurora-inspire my-project
/aurora-spec my-project
/aurora-build my-project
/design-review my-project --phase prototype
/aurora-refine my-project
```

---

## 🔍 Finding the Right Skill

### "I need to..."

**...understand this code** → `/explain-code`
**...check if my UI is accessible** → `/accessibility-check`
**...validate my design** → `/design-review`
**...see what's broken in GECO** → `/geco-status`
**...update the registry** → `/registry-sync`
**...learn about a component** → `/component-overview`
**...improve my CLAUDE.md** → `/claude-md-improver`
**...audit UX before launch** → `/ux-audit`
**...set up Claude Code** → `/claude-automation-recommender`
**...save what I learned** → `/revise-claude-md`

### "I'm working on..."

**...a new UI component** → `/ux-audit`, `/design-review`, `/accessibility-check`
**...a bug fix** → `/explain-code`, `/component-overview`
**...a new feature** → `/geco-status` (check compliance), `/component-overview`
**...a release** → `/ux-audit`, `/accessibility-check`, `/geco-status`, `/registry-sync`
**...documentation** → `/claude-md-improver`, `/revise-claude-md`
**...design system work** → `/design-review`, AURORA skills
**...onboarding someone** → `/component-overview`, `/explain-code --level simple`

---

## ⚙️ Skill Options Reference

### Common Options Across Skills

| Option | Description | Example |
|--------|-------------|---------|
| `--component <name>` | Target specific component | `--component _ARGUS` |
| `--validate-only` | Check without changes | `--validate-only` |
| `--verbose` | Detailed output | `--verbose` |
| `--export-report` | Save markdown report | `--export-report` |
| `--ci` | CI/CD mode (exit 1 on fail) | `--ci` |
| `--level <level>` | Complexity level | `--level expert` |
| `--phase <phase>` | Design phase | `--phase implementation` |

### Skill-Specific Options

**`/geco-status`**:
- `--priority <high|medium|low>` — Filter by priority
- `--json` — JSON output for automation

**`/registry-sync`**:
- `--fix` — Auto-fix issues
- `--component <name>` — Sync specific component

**`/explain-code`**:
- `--level <simple|detailed|expert>` — Explanation depth
- `<file|function>` — Target to explain

**`/design-review`**:
- `--phase <spec|prototype|implementation>` — Review phase
- `--strict` — Enforce strict 30% DNA compliance
- `--compare <component>` — Compare with another component

**`/accessibility-check`**:
- `--level <AA|AAA>` — WCAG level (AA default)
- `--automated-only` — Skip manual testing guide
- `--url <url>` — Test live URL

---

## 🎓 Skill Mastery Tips

### 1. Start Small
Don't try to learn all skills at once. Master essentials first:
- `/component-overview`
- `/explain-code`
- `/geco-status`

### 2. Use Context
Skills work better with context. Before running:
- Read the component's CLAUDE.md
- Check git status
- Review recent changes

### 3. Chain Skills
Combine skills for workflows:
```bash
# Pre-launch workflow:
/ux-audit _VULCAN
/accessibility-check _VULCAN
/design-review _VULCAN --phase implementation
/geco-status --component _VULCAN
```

### 4. Read the Reports
Skills generate detailed reports. Don't just look at pass/fail:
- Read recommendations
- Understand why things failed
- Learn patterns to avoid

### 5. Customize for Your Project
Fork skills and adapt them:
```bash
# Copy skill:
cp .claude/skills/ux-audit .claude/skills/my-custom-audit

# Edit SKILL.md to customize
```

### 6. Check Documentation
Each skill has detailed docs:
```bash
# Read full documentation:
cat .claude/skills/<skill-name>/SKILL.md
```

### 7. Use Skills in CI/CD
Automate quality checks:
```yaml
# .github/workflows/quality.yml
- name: GECO Status
  run: claude -p "/geco-status --ci" --allowedTools Read,Grep

- name: Accessibility Check
  run: claude -p "/accessibility-check --ci --automated-only"
```

---

## 🚀 Advanced: Creating Custom Skills

### When to Create a Skill
- Repeated workflow (>3 times)
- Team needs it
- Cross-component pattern
- Complex automation

### Skill Template
```markdown
---
name: my-skill
description: Brief description
disable-model-invocation: false
---

# My Skill

## Usage
\`\`\`
/my-skill <args> [--option]
\`\`\`

## What It Does
[Description]

## Options
- `--option`: [Description]

## Examples
\`\`\`
/my-skill example-input
\`\`\`

## Output Format
[What user will see]
```

### Create Skill
```bash
mkdir -p .claude/skills/my-skill
# Write SKILL.md with frontmatter
```

**Learn more**: `X:\Projects\_GAIA\.claude\COMPREHENSIVE_AUTOMATION_IMPLEMENTATION.md` (Section: "Creating Custom Skills")

---

## 📊 Skills Dashboard (ARGUS Integration)

View skill usage analytics in ARGUS:
```bash
cd X:\Projects\_GAIA\_ARGUS
streamlit run dashboard/app.py --server.port 8501
# Navigate to: "Skills Analytics" tab
```

Tracks:
- Most used skills
- Success/failure rates
- Average execution time
- Cost per skill (model usage)

---

## 🆘 Troubleshooting

### Skill Not Found
```
Error: Skill 'my-skill' not found
```
**Fix**: Check skill exists at `.claude/skills/my-skill/SKILL.md`

### Skill Fails to Execute
```
Error: Skill execution failed
```
**Fix**:
1. Check skill frontmatter (YAML must be valid)
2. Read skill output for specific error
3. Try with `--verbose` flag

### MCP Server Required
```
Error: This skill requires Figma MCP server
```
**Fix**: Install required MCP server (see COMPREHENSIVE_AUTOMATION_IMPLEMENTATION.md)

### Permission Denied
```
Error: Permission denied for file operation
```
**Fix**: Check Claude Code permission mode (use `--bypassPermissions` if safe)

---

## 📚 Further Learning

### Documentation Locations
- **Skills docs**: `X:\Projects\_GAIA\.claude\skills\*/SKILL.md`
- **Agent docs**: `X:\Projects\_GAIA\.claude\agents\*.md`
- **Automation guide**: `X:\Projects\_GAIA\.claude\COMPREHENSIVE_AUTOMATION_IMPLEMENTATION.md`
- **Model optimization**: `X:\Projects\_GAIA\.claude\MODEL_EFFORT_OPTIMIZATION.md`

### GAIA-Specific Guides
- **GAIA Bible**: `X:\Projects\_GAIA\GAIA_BIBLE.md` (Constitutional principles)
- **GECO Audit**: `X:\Projects\_GAIA\GECO_AUDIT.md` (27 requirements)
- **Registry**: `X:\Projects\_GAIA\registry.json` (Component catalog)
- **Version Log**: `X:\Projects\_GAIA\VERSION_LOG.md` (Release history)

### Component CLAUDE.md Files
Each component has setup instructions:
- `X:\Projects\_GAIA\CLAUDE.md` (Root)
- `X:\Projects\_GAIA\_ARGUS\CLAUDE.md`
- `X:\Projects\_GAIA\_AURORA\CLAUDE.md`
- `X:\Projects\_GAIA\_MYCEL\CLAUDE.md`
- (etc. for all 11 components)

---

## 🎯 Quick Start Checklist

New to GAIA skills? Complete this checklist:

- [ ] Run `/component-overview _ARGUS` to learn about ARGUS
- [ ] Run `/geco-status` to see ecosystem compliance
- [ ] Run `/registry-sync --validate-only` to check registry
- [ ] Run `/explain-code X:\Projects\_GAIA\registry.json` to understand registry
- [ ] Run `/ux-audit _ARGUS` to see UX analysis
- [ ] Run `/accessibility-check _ARGUS` to see accessibility report
- [ ] Run `/claude-md-improver` on your project
- [ ] Read `MODEL_EFFORT_OPTIMIZATION.md` to optimize costs
- [ ] Bookmark this file for quick reference!

---

## 💡 Pro Tips

1. **Use tab completion**: Type `/` and start typing skill name
2. **Check examples**: Every SKILL.md has examples section
3. **Chain with `&&`**: Run multiple validations at once
4. **Save reports**: Use `--export-report` for documentation
5. **CI/CD integration**: Use `--ci` flag to fail builds on violations
6. **Cost awareness**: Check MODEL_EFFORT_OPTIMIZATION.md before heavy usage
7. **Learn progressively**: Master essentials before advanced skills
8. **Read outputs**: Skills generate detailed reports - study them
9. **Customize**: Fork and adapt skills to your needs
10. **Share learnings**: Use `/revise-claude-md` to document patterns

---

**Last Updated**: Feb 9, 2026
**Version**: 1.0
**Maintained by**: GAIA Core Team

**Quick Help**:
- "I need to..." → See "Finding the Right Skill" section
- "I'm working on..." → See "Finding the Right Skill" section
- "How do I..." → See skill-specific SKILL.md files
- "This skill failed" → See "Troubleshooting" section
