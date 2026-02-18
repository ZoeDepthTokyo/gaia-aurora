---
name: checking-accessibility
description: "[CONTEXT] Performs comprehensive WCAG 2.1 AA accessibility audit with automated checks and manual testing guidance. Use after UI changes, before launches, or when reviewing Streamlit dashboards for accessibility compliance. Triggers on: accessibility, WCAG, a11y, screen reader, contrast, keyboard navigation. Why: ensures GAIA UIs are usable by everyone."
disable-model-invocation: false
---

# Accessibility Check

Performs comprehensive WCAG 2.1 AA accessibility audit with automated checks and manual testing guidance. Ensures GAIA components are usable by everyone.

## Usage
```
/accessibility-check <component_name> [--level AA|AAA]
/accessibility-check --url <demo_url> [--automated-only]
```

## WCAG 2.1 Coverage

### Level AA (Required)
- Perceivable: Color contrast, alt text, heading hierarchy
- Operable: Keyboard navigation, focus indicators, link purpose
- Understandable: Form labels, error instructions, consistent navigation
- Robust: Semantic HTML, ARIA labels, assistive technology compatibility

### Level AAA (Aspirational)
- Enhanced contrast requirements
- Extended audio descriptions
- Sign language interpretation

For detailed checks, see:
- references/perceivable.md — Color contrast, alt text, heading hierarchy
- references/operable.md — Keyboard navigation, focus indicators, link purpose
- references/understandable.md — Form labels, manual testing guide
- references/robust.md — Semantic HTML, ARIA, example output

## Process Summary

1. **Run automated checks** — Color contrast, keyboard nav, focus indicators, alt text, form labels, semantic HTML, heading hierarchy, link purpose
2. **Manual testing** — Screen reader (NVDA/VoiceOver), keyboard-only navigation, color blindness simulation
3. **Prioritize violations** — Critical (WCAG AA blockers) → High (usability) → Medium (enhancements)
4. **Generate report** — Score, violations list, priority fixes, recommendations

## Options

- `--level <AA|AAA>`: Target WCAG level (AA default, AAA aspirational)
- `--automated-only`: Skip manual testing guidance
- `--url <demo_url>`: Test live URL (requires browser)
- `--export-report`: Save detailed markdown report
- `--ci`: Exit with code 1 if violations found (for CI/CD)

## Integration

### Pre-Launch Checklist
```
/ux-audit <component>
/accessibility-check <component>
/design-review <component>
```

### With AURORA Agent
```
claude --agent aurora-ux-lead
/accessibility-check _ARGUS
```

## Quick Fixes Reference

### Color Contrast
```css
/* Before (2.5:1) */ color: #888; background: #fff;
/* After (7.0:1)  */ color: #333; background: #fff;
```

### Focus Indicators
```css
button:focus { outline: 2px solid #0066CC; outline-offset: 2px; }
```

### Alt Text
```html
<img src="chart.png" alt="Line chart showing user growth from 100 to 500 over 6 months">
```

### ARIA Labels
```html
<button aria-label="Close dialog"><span class="icon-x"></span></button>
```
