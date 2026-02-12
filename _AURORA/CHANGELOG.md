# AURORA Changelog

## [0.2.0] - 2026-02-11

### Added - Creative Direction System 🎨

**Major Enhancement**: AURORA now has systematic creative intelligence

#### 1. Style Extraction
- New directory: `creative_direction/extracted_styles/`
- Template: `creative_direction/templates/style_extraction.md`
- Skill: `/aurora-extract-style <url>`
- **Capability**: Analyze successful websites, extract design tokens (colors, typography, spacing, borders, shadows), identify interaction patterns, document creative observations
- **Output**: analysis.md, tokens.json, observations.md
- **Use case**: Learn from successful brands, build mood boards, competitive analysis

#### 2. Mood Board Generation
- New directory: `creative_direction/mood_boards/{project}/`
- Templates: `creative_brief.md`, `mood_board.md`
- Skill: `/aurora-mood <project>`
- **Capability**: Generate creative briefs, curate visual references (5-7 sites), extract style direction, output design tokens ready for brand kit
- **Checkpoints**: 3 user approval points (brief, references, mood board)
- **Output**: Complete creative foundation for project
- **Use case**: Establish visual language before UX specification

#### 3. Quick Design Tasks
- Skill: `/aurora-quick "<description>"`
- **Capability**: Single component design in < 5 minutes, design system aware, uses existing tokens automatically
- **Output**: Component code + rationale + accessibility notes + integration guidance
- **Use case**: Quick UI fixes, single components, small enhancements without full workflow

#### 4. Creative Direction Framework
- New directory structure for systematic creative work
- Templates for creative briefs, mood boards, style extraction
- Trend analysis documented in `learnings/trends.md`
- Integration with existing 6-phase workflow (Phase 2 enhanced)

### Changed
- Updated agent definition (`~/.claude/agents/aurora-ux-lead.md`)
- Enhanced Phase 2 (Inspiration) workflow to include creative direction
- Added 8th core principle: "Creative direction first"

### Workflow Improvements
- **Before**: Phase 2 was generic "find inspiration"
- **After**: Phase 2 includes systematic creative brief → references → mood board → tokens
- **Before**: No way to extract learnings from successful sites
- **After**: `/aurora-extract-style` documents patterns for reuse
- **Before**: Full 6-phase workflow required for any task
- **After**: `/aurora-quick` for simple tasks, full workflow for complex projects

### Directory Structure Added
```
creative_direction/
├── README.md                    # Creative direction system overview
├── templates/
│   ├── creative_brief.md        # Brand personality, audience, constraints
│   ├── mood_board.md            # Visual references, style direction
│   └── style_extraction.md      # Analyze successful sites
├── extracted_styles/            # Style guides from analyzed sites
│   └── {site_name}/
│       ├── analysis.md
│       ├── tokens.json
│       └── observations.md
├── mood_boards/                 # Project creative direction
│   └── {project}/
│       ├── creative_brief.md
│       ├── mood_board.md
│       └── references.json
└── learnings/
    ├── trends.md                # Current design trends (2026)
    ├── patterns.md              # Successful patterns
    └── anti_patterns.md         # What to avoid
```

### Skills Added
1. `aurora-extract-style` — Extract design tokens from URLs
2. `aurora-mood` — Generate mood board and creative direction
3. `aurora-quick` — Quick component design

### Rationale
**User feedback**: "Aurora lacks creative understanding, creative direction, and a way to look at many successful brands and web pages to create style guides. She also lacked simplicity of assigning design of simple items."

**Solution**:
- ✅ Creative understanding: Systematic framework for creative briefs and mood boards
- ✅ Learning from brands: Style extraction tools to analyze successful sites
- ✅ Simplicity: `/aurora-quick` for fast turnaround on simple tasks

---

## [0.1.0] - 2026-02-09

### Initial Release
- 6-phase workflow (Intake → Inspire → Spec → Build → Refine → Deploy)
- Design system (30% master DNA, 70% brand variation)
- Atomic design hierarchy (Tokens → Atoms → Molecules → Organisms)
- RAVEN integration for research
- Figma integration (MCP)
- MNEMIS integration for learning storage
- Master design tokens
- Inspiration library (8 curated references)
- 7-pass UX analysis framework

---

## Version History

- **0.2.0** (2026-02-11): Creative Direction System — style extraction, mood boards, quick tasks
- **0.1.0** (2026-02-09): Initial release — 6-phase workflow, design system, integrations
