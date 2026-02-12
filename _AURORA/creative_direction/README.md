# Creative Direction System

AURORA's creative intelligence layer — systematic approach to analyzing successful designs, establishing creative direction, and generating style guides.

## Quick Start

```bash
# Extract style guide from a URL
/aurora-extract-style <url>

# Generate mood board for a project
/aurora-mood <project_name>

# Quick creative brief
/aurora-brief <project_name>
```

## Directory Structure

```
creative_direction/
├── README.md                  # This file
├── templates/
│   ├── creative_brief.md      # Template for creative briefs
│   ├── mood_board.md          # Mood board structure
│   └── style_extraction.md    # Style analysis template
├── extracted_styles/          # Style guides from analyzed sites
│   └── {site_name}/
│       ├── analysis.json      # Extracted design tokens
│       ├── screenshots/       # Visual references
│       └── notes.md           # Creative observations
├── mood_boards/               # Project mood boards
│   └── {project}/
│       ├── mood_board.md      # Visual direction
│       ├── references.json    # Curated references
│       └── creative_brief.md  # Creative constraints
└── learnings/
    ├── trends.md              # Current design trends
    ├── patterns.md            # Successful patterns
    └── anti_patterns.md       # What to avoid
```

## Creative Direction Workflow

### 1. Creative Brief (Input)
- Brand personality (adjectives: modern, playful, professional, bold, minimal)
- Target audience (demographics, technical literacy, use case)
- Constraints (technical limitations, brand guidelines, accessibility needs)
- Success criteria (what makes this design "work"?)

### 2. Trend Analysis (Research)
- Analyze 5-10 successful sites in the same category
- Extract common patterns, interactions, visual language
- Identify what makes them successful
- Document anti-patterns to avoid

### 3. Mood Board (Synthesis)
- Curate 5-7 visual references that align with brief
- Extract color palettes, typography systems, spacing rhythms
- Identify key interaction patterns
- Define creative "north star" for the project

### 4. Style Guide (Output)
- Design tokens extracted from mood board
- Component patterns inspired by references
- Clear creative rationale for every decision
- Ready to translate into master/brand tokens

## Style Extraction Process

When analyzing a successful site:

### Visual Extraction
- **Colors**: Primary, secondary, accent, semantic (success/error/warning)
- **Typography**: Font families, scale (h1-h6, body, caption), weights
- **Spacing**: Grid system, padding/margin rhythm, component spacing
- **Borders**: Radius values, border widths, divider patterns
- **Shadows**: Elevation system, shadow tokens
- **Layout**: Max-widths, breakpoints, grid columns

### Interaction Patterns
- Navigation pattern (sidebar, top nav, breadcrumbs)
- Button hierarchy (primary, secondary, ghost, icon)
- Form patterns (input styles, validation, error states)
- Loading states (skeletons, spinners, progress bars)
- Empty states (no data, error, onboarding)
- Animation/transitions (hover, focus, page transitions)

### Creative Observations
- What makes this site feel premium/fast/trustworthy?
- What patterns create delight?
- What's the information hierarchy?
- How does it guide user attention?
- What's the emotional tone?

## Mood Board Structure

A good mood board answers:
1. **What does this project FEEL like?** (emotional tone)
2. **What does success LOOK like?** (visual references)
3. **What patterns should we BORROW?** (interaction references)
4. **What constraints GUIDE us?** (creative boundaries)

## Integration with 6-Phase Workflow

- **Phase 1 (Intake)**: Extract creative constraints from PRD
- **Phase 2 (Inspire)**: Creative brief + mood board generation
- **Phase 2.5 (NEW)**: Style extraction from references
- **Phase 3 (Spec)**: 7-pass analysis informed by creative direction
- **Phase 4 (Build)**: Build order references mood board and style guides

## Tools AURORA Uses

### For Style Extraction
- **WebFetch**: Analyze live websites
- **WebSearch**: Find category-specific references
- **RAVEN**: Deep research on trends, articles, best practices
- **Read**: Analyze saved screenshots

### For Creative Direction
- **Write**: Generate creative briefs, mood boards
- **Edit**: Refine and iterate on direction
- **Glob/Grep**: Search existing patterns and learnings

## Example: Extracting Style from Linear.app

```json
{
  "site": "Linear.app",
  "category": "Project Management / Developer Tool",
  "extracted_tokens": {
    "colors": {
      "primary": "#5E6AD2",
      "background": "#0F0F10",
      "surface": "#1A1A1E",
      "text_primary": "#FFFFFF",
      "text_secondary": "#8A8F98"
    },
    "typography": {
      "font_family": "Inter, system-ui",
      "scale": {
        "h1": "32px / 600",
        "h2": "24px / 600",
        "body": "14px / 400",
        "caption": "12px / 400"
      }
    },
    "spacing": {
      "scale": "4px base (4, 8, 12, 16, 24, 32, 48, 64)"
    },
    "radius": {
      "sm": "4px",
      "md": "6px",
      "lg": "8px"
    }
  },
  "patterns": {
    "navigation": "Sidebar with collapsible sections, cmd+k search",
    "empty_states": "Centered, illustrated, with clear CTA",
    "keyboard_shortcuts": "Extensive, visible in tooltips"
  },
  "creative_observations": [
    "Dark theme creates focus and reduces eye strain",
    "Keyboard-first UX makes it feel blazingly fast",
    "Subtle animations on hover create premium feel without distraction",
    "High information density without feeling cramped (spacing rhythm)",
    "Command palette is the hero interaction — always accessible"
  ]
}
```

## Creative Decision Framework

When making creative decisions, AURORA asks:

1. **Does this align with the creative brief?**
2. **Is there precedent in successful products?** (reference extracted styles)
3. **Does this serve the user's mental model?**
4. **Is this pattern accessible and inclusive?**
5. **Can this scale across the design system?**

## Output: Creative Direction Document

Every project gets a `creative_direction.md` with:
- Creative brief (personality, audience, constraints)
- Mood board (references, rationale, extracted tokens)
- Style guide (design tokens ready for brand kit)
- Pattern library (interaction patterns to adopt)
- Creative rationale (why these choices serve users)
