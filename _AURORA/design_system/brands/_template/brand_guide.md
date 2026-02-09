# {Project Name} Brand Guide

**Created by AURORA** | **Date:** {date} | **Version:** 0.1.0

---

## Brand Personality

{To be defined during `/aurora-brand`. Describe the brand in 3-5 adjectives and a brief personality statement.}

---

## Color Palette

### Primary
{Main brand color. Used for primary actions, key UI elements, brand identity.}
- See `brand_tokens.json` for full scale (50-900)

### Secondary
{Supporting color. Used for secondary actions, backgrounds, subtle accents.}
- See `brand_tokens.json` for full scale (50-900)

### Accent
{Highlight color. Used sparingly for emphasis, notifications, special elements.}
- See `brand_tokens.json` for full scale (50-900)

### Usage Guidelines
- Primary buttons: `primary.600` background, white text
- Secondary buttons: `secondary.100` background, `secondary.700` text
- Links: `primary.600` default, `primary.700` hover
- Backgrounds: `neutral.0` (light), `neutral.50` (subtle), `primary.50` (tinted)

---

## Typography

**Font Family Override:** {Font name or "Inherits master (Inter)"}

Usage follows master guidelines. Override only the font family if brand requires a different typeface.

---

## Component Personality

| Aspect | Value | Notes |
|--------|-------|-------|
| Corner radius | {rounded / sharp / mixed} | {e.g., "lg radius for cards, md for inputs"} |
| Shadow depth | {subtle / medium / pronounced} | {e.g., "sm shadows only, flat design preference"} |
| Content density | {spacious / comfortable / compact} | {e.g., "comfortable for general use"} |
| Border style | {none / subtle / prominent} | {e.g., "subtle borders on cards, none on sections"} |

---

## Imagery Direction

- **Illustration style:** {To be defined}
- **Photography direction:** {To be defined}
- **Iconography:** {Lucide default or custom set}

---

## Micro-Copy Tone

| Context | Tone | Example |
|---------|------|---------|
| Success messages | {encouraging / neutral / formal} | {To be defined} |
| Error messages | {helpful / technical / casual} | {To be defined} |
| Empty states | {inviting / instructional / minimal} | {To be defined} |
| Button labels | {action-oriented / descriptive / concise} | {To be defined} |

---

## GAIA 30% DNA Compliance

The following MUST inherit from master (cannot be overridden):

- [ ] Typography scale (sizes and line heights)
- [ ] Spacing grid (base unit and scale)
- [ ] Breakpoint definitions
- [ ] Accessibility standards (contrast ratios, focus states)
- [ ] Motion timing curves
- [ ] Layout grid (12 columns, 24px gutters)
- [ ] Semantic colors (success, warning, error, info)

The following CAN be overridden (70% variation):

- [x] Color palettes (primary, secondary, accent)
- [x] Font families
- [x] Border radii
- [x] Shadow styles
- [x] Component skins
- [x] Imagery and iconography
- [x] Micro-copy tone
- [x] Animation personality (within timing constraints)
