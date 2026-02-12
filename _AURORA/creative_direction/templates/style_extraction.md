# Style Extraction: {SITE_NAME}

**URL**: {URL}
**Category**: {CATEGORY} (e.g., SaaS, Developer Tool, E-commerce, Dashboard)
**Analyzed**: {DATE}
**Extracted By**: AURORA v0.1.0

---

## Visual Analysis

### Color System

**Primary Palette:**
- Primary: `{HEX}` — {USAGE_NOTES}
- Secondary: `{HEX}` — {USAGE_NOTES}
- Accent: `{HEX}` — {USAGE_NOTES}

**Neutral Palette:**
- Background: `{HEX}`
- Surface: `{HEX}`
- Border: `{HEX}`
- Text Primary: `{HEX}`
- Text Secondary: `{HEX}`
- Text Muted: `{HEX}`

**Semantic Colors:**
- Success: `{HEX}`
- Error: `{HEX}`
- Warning: `{HEX}`
- Info: `{HEX}`

**Observations:**
- {COLOR_USAGE_PATTERNS}
- {CONTRAST_STRATEGY}
- {DARK_MODE_SUPPORT}

---

### Typography System

**Font Families:**
- Headings: `{FONT_STACK}`
- Body: `{FONT_STACK}`
- Code: `{FONT_STACK}` (if applicable)

**Type Scale:**
```
Display: {SIZE}/{WEIGHT}/{LINE_HEIGHT}
H1:      {SIZE}/{WEIGHT}/{LINE_HEIGHT}
H2:      {SIZE}/{WEIGHT}/{LINE_HEIGHT}
H3:      {SIZE}/{WEIGHT}/{LINE_HEIGHT}
H4:      {SIZE}/{WEIGHT}/{LINE_HEIGHT}
Body:    {SIZE}/{WEIGHT}/{LINE_HEIGHT}
Small:   {SIZE}/{WEIGHT}/{LINE_HEIGHT}
Caption: {SIZE}/{WEIGHT}/{LINE_HEIGHT}
```

**Observations:**
- {HIERARCHY_CLARITY}
- {READABILITY_NOTES}
- {RESPONSIVE_BEHAVIOR}

---

### Spacing System

**Scale:** {BASE_UNIT} (e.g., 4px, 8px)

**Common Values:**
```
xs:  {VALUE}
sm:  {VALUE}
md:  {VALUE}
lg:  {VALUE}
xl:  {VALUE}
2xl: {VALUE}
```

**Layout Grid:**
- Columns: {NUMBER}
- Gutter: {VALUE}
- Max Width: {VALUE}
- Breakpoints: {MOBILE, TABLET, DESKTOP, WIDE}

**Observations:**
- {SPACING_RHYTHM_PATTERNS}
- {WHITESPACE_USAGE}
- {DENSITY_APPROACH}

---

### Border System

**Radius:**
- None: `0px` — {WHERE_USED}
- Small: `{VALUE}` — {WHERE_USED}
- Medium: `{VALUE}` — {WHERE_USED}
- Large: `{VALUE}` — {WHERE_USED}
- Full: `9999px` — {WHERE_USED}

**Border Widths:**
- Default: `{VALUE}`
- Thick: `{VALUE}`
- Focus: `{VALUE}`

**Observations:**
- {ROUNDNESS_PERSONALITY}
- {BORDER_USAGE_PATTERNS}

---

### Shadow System

**Elevation Tokens:**
```
sm:  {BOX_SHADOW_VALUE}
md:  {BOX_SHADOW_VALUE}
lg:  {BOX_SHADOW_VALUE}
xl:  {BOX_SHADOW_VALUE}
```

**Observations:**
- {SHADOW_USAGE_STRATEGY}
- {DEPTH_PERCEPTION}

---

## Interaction Patterns

### Navigation
- **Pattern**: {SIDEBAR, TOP_NAV, TABS, BREADCRUMBS}
- **Behavior**: {COLLAPSIBLE, STICKY, RESPONSIVE}
- **Search**: {CMD_K, INLINE, NONE}

### Buttons
- **Primary**: {STYLE_DESCRIPTION}
- **Secondary**: {STYLE_DESCRIPTION}
- **Ghost/Text**: {STYLE_DESCRIPTION}
- **Icon Only**: {STYLE_DESCRIPTION}
- **Sizes**: {SM, MD, LG}

### Forms
- **Input Style**: {OUTLINED, FILLED, UNDERLINED}
- **Validation**: {INLINE, ON_BLUR, ON_SUBMIT}
- **Error Display**: {BELOW_INPUT, TOOLTIP, MODAL}
- **Required Fields**: {ASTERISK, LABEL_TEXT, NONE}

### Data Display
- **Tables**: {STRIPED, BORDERED, HOVERABLE, SORTABLE}
- **Cards**: {SHADOW, BORDER, PADDING, HOVER_EFFECTS}
- **Lists**: {DIVIDERS, SPACING, ICONS}

### Feedback States
- **Loading**: {SKELETON, SPINNER, PROGRESS_BAR}
- **Empty**: {ILLUSTRATION, TEXT_ONLY, CTA_INCLUDED}
- **Error**: {INLINE, TOAST, MODAL, PAGE_LEVEL}
- **Success**: {TOAST, INLINE, MODAL}

---

## Animation & Motion

**Transition Speed:**
- Fast: `{MS}` — {USAGE}
- Normal: `{MS}` — {USAGE}
- Slow: `{MS}` — {USAGE}

**Easing Functions:**
- {EASE_FUNCTION} — {WHERE_USED}

**Key Animations:**
- {ANIMATION_1} — {PURPOSE}
- {ANIMATION_2} — {PURPOSE}

**Observations:**
- {MOTION_PHILOSOPHY}
- {DELIGHT_MOMENTS}
- {PERFORMANCE_CONSIDERATIONS}

---

## Creative Observations

### What Makes This Site Successful?

1. **{OBSERVATION_1}**
   - Example: {SPECIFIC_PATTERN_OR_MOMENT}
   - Why it works: {PSYCHOLOGICAL_OR_UX_PRINCIPLE}

2. **{OBSERVATION_2}**
   - Example: {SPECIFIC_PATTERN_OR_MOMENT}
   - Why it works: {PSYCHOLOGICAL_OR_UX_PRINCIPLE}

3. **{OBSERVATION_3}**
   - Example: {SPECIFIC_PATTERN_OR_MOMENT}
   - Why it works: {PSYCHOLOGICAL_OR_UX_PRINCIPLE}

### Patterns to Borrow

✅ **{PATTERN_1}** — {WHY_THIS_FITS_OUR_PROJECT}
✅ **{PATTERN_2}** — {WHY_THIS_FITS_OUR_PROJECT}
✅ **{PATTERN_3}** — {WHY_THIS_FITS_OUR_PROJECT}

### Patterns to Avoid

❌ **{PATTERN_1}** — {WHY_THIS_DOESNT_FIT}
❌ **{PATTERN_2}** — {WHY_THIS_DOESNT_FIT}

---

## Extracted Design Tokens (JSON)

```json
{
  "site": "{SITE_NAME}",
  "url": "{URL}",
  "category": "{CATEGORY}",
  "extracted": "{DATE}",
  "tokens": {
    "colors": {
      "primary": "{HEX}",
      "secondary": "{HEX}",
      "accent": "{HEX}",
      "background": "{HEX}",
      "surface": "{HEX}",
      "border": "{HEX}",
      "text": {
        "primary": "{HEX}",
        "secondary": "{HEX}",
        "muted": "{HEX}"
      },
      "semantic": {
        "success": "{HEX}",
        "error": "{HEX}",
        "warning": "{HEX}",
        "info": "{HEX}"
      }
    },
    "typography": {
      "fontFamily": {
        "heading": "{FONT_STACK}",
        "body": "{FONT_STACK}",
        "code": "{FONT_STACK}"
      },
      "scale": {
        "display": "{SIZE}/{WEIGHT}/{LINE_HEIGHT}",
        "h1": "{SIZE}/{WEIGHT}/{LINE_HEIGHT}",
        "h2": "{SIZE}/{WEIGHT}/{LINE_HEIGHT}",
        "h3": "{SIZE}/{WEIGHT}/{LINE_HEIGHT}",
        "body": "{SIZE}/{WEIGHT}/{LINE_HEIGHT}",
        "small": "{SIZE}/{WEIGHT}/{LINE_HEIGHT}"
      }
    },
    "spacing": {
      "base": "{BASE_UNIT}",
      "scale": ["{XS}", "{SM}", "{MD}", "{LG}", "{XL}"]
    },
    "radius": {
      "sm": "{VALUE}",
      "md": "{VALUE}",
      "lg": "{VALUE}",
      "full": "9999px"
    },
    "shadows": {
      "sm": "{BOX_SHADOW}",
      "md": "{BOX_SHADOW}",
      "lg": "{BOX_SHADOW}",
      "xl": "{BOX_SHADOW}"
    }
  },
  "patterns": {
    "navigation": "{DESCRIPTION}",
    "buttons": "{DESCRIPTION}",
    "forms": "{DESCRIPTION}",
    "dataDisplay": "{DESCRIPTION}",
    "feedback": "{DESCRIPTION}"
  },
  "observations": [
    "{OBSERVATION_1}",
    "{OBSERVATION_2}",
    "{OBSERVATION_3}"
  ]
}
```

---

## Next Steps

- Adapt extracted tokens to project brand kit
- Incorporate successful patterns into UX spec
- Document creative rationale in mood board
