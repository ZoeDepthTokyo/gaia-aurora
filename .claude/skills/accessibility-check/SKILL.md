---
name: accessibility-check
description: WCAG 2.1 AA compliance check with automated and manual testing guidance
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
- ✅ Perceivable: Can users perceive content?
- ✅ Operable: Can users operate controls?
- ✅ Understandable: Can users understand content and controls?
- ✅ Robust: Does it work with assistive technologies?

### Level AAA (Aspirational)
- Enhanced contrast requirements
- Extended audio descriptions
- Sign language interpretation

## Automated Checks

### 1. Color Contrast (WCAG 1.4.3)
**Requirement**: 4.5:1 for normal text, 3:1 for large text

```python
# Check all text elements
for element in ui_elements:
    contrast = calculate_contrast(fg_color, bg_color)
    if contrast < 4.5:
        flag_violation(element, f"Contrast {contrast}:1 < 4.5:1")
```

**Common violations**:
- Light gray text on white (#CCCCCC on #FFFFFF = 1.6:1) ❌
- Blue links on dark background (insufficient contrast)

### 2. Keyboard Navigation (WCAG 2.1.1)
**Requirement**: All functionality via keyboard

```
Test:
1. Tab through all interactive elements
2. Shift+Tab reverses direction
3. Enter/Space activates buttons/links
4. Escape closes modals
5. Arrow keys navigate menus/lists
```

**Check**:
- Can reach all controls?
- Tab order logical?
- Focus visible?
- Keyboard traps avoided?

### 3. Focus Indicators (WCAG 2.4.7)
**Requirement**: Visible focus indicator (≥2px, high contrast)

```css
/* Good */
button:focus {
    outline: 2px solid #0066CC;
    outline-offset: 2px;
}

/* Bad */
button:focus {
    outline: none;  /* ❌ Removes indicator */
}
```

### 4. Alt Text (WCAG 1.1.1)
**Requirement**: Text alternatives for non-text content

```html
<!-- Good -->
<img src="chart.png" alt="Bar chart showing 60% increase in users">

<!-- Bad -->
<img src="chart.png" alt="chart">  <!-- Too vague -->
<img src="chart.png">  <!-- Missing alt -->
```

**Check**:
- Images have alt=""
- Decorative images have alt=""
- Icons have ARIA labels
- Charts have text descriptions

### 5. Form Labels (WCAG 3.3.2)
**Requirement**: Labels or instructions for inputs

```html
<!-- Good -->
<label for="email">Email Address</label>
<input id="email" type="email">

<!-- Bad -->
<input placeholder="Email">  <!-- Placeholder not a label -->
```

### 6. Semantic HTML (WCAG 4.1.2)
**Requirement**: Proper HTML5 elements and ARIA

```html
<!-- Good -->
<button>Submit</button>
<nav><ul><li><a href="...">Link</a></li></ul></nav>

<!-- Bad -->
<div onclick="...">Submit</div>  <!-- Not semantic -->
```

### 7. Heading Hierarchy (WCAG 1.3.1)
**Requirement**: Logical heading structure (h1 → h2 → h3)

```
✅ h1 → h2 → h3
❌ h1 → h3 (skipped h2)
❌ h3 → h2 (backwards)
```

### 8. Link Purpose (WCAG 2.4.4)
**Requirement**: Link text describes destination

```html
<!-- Good -->
<a href="...">View GAIA documentation</a>

<!-- Bad -->
<a href="...">Click here</a>  <!-- Non-descriptive -->
```

## Manual Testing Guide

### Screen Reader Testing

**NVDA (Windows - Free)**
```
1. Install NVDA: https://www.nvaccess.org/
2. Start NVDA (Ctrl+Alt+N)
3. Navigate page:
   - H: Jump to headings
   - K: Jump to links
   - F: Jump to form fields
   - B: Jump to buttons
4. Listen: Is content understandable?
5. Check: Can you complete all tasks?
```

**VoiceOver (Mac - Built-in)**
```
1. Enable: System Settings → Accessibility → VoiceOver
2. Start: Cmd+F5
3. Navigate: VO+Right Arrow (VO = Ctrl+Option)
4. Interact: VO+Space
```

### Keyboard-Only Testing
```
1. Unplug mouse (literally)
2. Complete all tasks using only keyboard
3. Check:
   - Can you navigate entire UI?
   - Can you activate all buttons?
   - Can you fill all forms?
   - Can you close all modals?
4. Note any keyboard traps
```

### Color Blindness Testing
```
Tools:
- Chromium DevTools → Rendering → Emulate vision deficiencies
- Stark plugin (Figma)

Test:
- Protanopia (red-blind)
- Deuteranopia (green-blind)
- Tritanopia (blue-blind)
- Achromatopsia (monochrome)

Check: Is information still conveyed without color?
```

## Example Output

```
Accessibility Audit: _ARGUS Dashboard
======================================

Component: ARGUS Streamlit Dashboard
Standard: WCAG 2.1 Level AA
Date: Feb 9, 2026

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Overall Score: 68/100 (C+)
Status: ⚠️  NEEDS WORK (8 violations found)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Automated Checks
────────────────

1. Color Contrast (WCAG 1.4.3)
   ❌ FAIL: 3 violations found

   • Sidebar text (rgb(128,128,128) on rgb(255,255,255))
     Contrast: 2.1:1 (required: 4.5:1)
     Location: Sidebar navigation labels
     Fix: Change to rgb(51,51,51) for 8.6:1 ratio

   • Chart legend (rgb(180,180,180) on rgb(240,240,240))
     Contrast: 1.4:1 (required: 3.0:1 for large text)
     Location: Ecosystem graph legend
     Fix: Use darker colors or thicker borders

   • Disabled button text (rgb(200,200,200) on rgb(230,230,230))
     Contrast: 1.2:1 (required: 4.5:1)
     Location: "Run Scenario" when inactive
     Fix: Streamlit default acceptable (informational only)

2. Keyboard Navigation (WCAG 2.1.1)
   ✅ PASS: All controls reachable via Tab
   ⚠️  ISSUE: Tab order skips mental model selector
     Fix: Ensure st.selectbox in logical tab sequence

3. Focus Indicators (WCAG 2.4.7)
   ✅ PASS: Streamlit provides default focus outlines
   💡 Enhancement: Could add custom :focus styles for brand

4. Alt Text (WCAG 1.1.1)
   ❌ FAIL: Ecosystem graph missing alt text
     Location: Networkx visualization
     Fix: Add st.caption() below chart with text description

5. Form Labels (WCAG 3.3.2)
   ✅ PASS: All inputs have labels (Streamlit automatic)

6. Semantic HTML (WCAG 4.1.2)
   ✅ PASS: Streamlit generates semantic HTML

7. Heading Hierarchy (WCAG 1.3.1)
   ⚠️  ISSUE: Skips from h1 to h3 in sidebar
     Location: "Mental Models" section
     Fix: Use st.subheader() instead of st.markdown("### ...")

8. Link Purpose (WCAG 2.4.4)
   ✅ PASS: Links descriptive (minimal links in dashboard)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Manual Testing Results
──────────────────────

Screen Reader (NVDA):
⚠️  Partial support
   - Navigation works
   - Headings announced correctly
   - Graph not announced (missing alt text)
   - Button states unclear ("Run Scenario" button)

Keyboard-Only:
✅ Mostly functional
   - Can navigate with Tab
   - Can activate buttons with Enter
   - ⚠️  Can't dismiss some error toasts (minor)

Color Blindness:
⚠️  Some issues
   - Protanopia: Red error messages hard to distinguish
   - Deuteranopia: Green success icons unclear
   - Fix: Add icons/text alongside color

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Priority Fixes
──────────────

🔴 Critical (WCAG AA Blockers)
1. Fix sidebar text contrast (2.1:1 → 4.5:1+)
2. Add alt text to ecosystem graph
3. Fix heading hierarchy (h1 → h3 skip)

🟠 High (Usability Issues)
4. Improve disabled button contrast
5. Fix keyboard tab order
6. Add text labels for color-coded status

🟡 Medium (Enhancements)
7. Custom focus styles for brand consistency
8. Improve screen reader announcements
9. Add ARIA landmarks for page regions

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Testing Checklist
─────────────────

Automated:
✅ Color contrast analyzer
✅ HTML validator
✅ ARIA validator
✅ Keyboard navigation test

Manual:
✅ Screen reader (NVDA)
⏳ Screen reader (VoiceOver) - TODO
✅ Keyboard-only test
✅ Color blindness emulation
⏳ Zoom to 200% - TODO

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Recommendations
───────────────

Short-term (This Sprint):
- Address all Critical and High priority fixes
- Re-test with screen reader after fixes
- Document accessible interaction patterns

Long-term (Backlog):
- Create AURORA accessibility component library
- Establish automated CI checks for contrast
- Add accessibility testing to GECO audit

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Resources
─────────────

- WCAG 2.1 Quick Reference: https://www.w3.org/WAI/WCAG21/quickref/
- Contrast Checker: https://contrast-ratio.com/
- NVDA Download: https://www.nvaccess.org/
- Streamlit A11y Guide: https://docs.streamlit.io/library/advanced-features/accessibility

Report saved to: _ARGUS/docs/A11Y_AUDIT_2026-02-09.md
```

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

### CI/CD Integration
```yaml
# .github/workflows/accessibility.yml
- name: A11y Check
  run: |
    claude -p "/accessibility-check --ci --automated-only" --allowedTools Read,Grep
```

### With AURORA Agent
```
claude --agent aurora-ux-lead
/accessibility-check _ARGUS
```

## Quick Fixes Reference

### Color Contrast
```css
/* Before (2.5:1) */
color: #888;
background: #fff;

/* After (7.0:1) */
color: #333;
background: #fff;
```

### Focus Indicators
```css
button:focus {
    outline: 2px solid #0066CC;
    outline-offset: 2px;
}
```

### Alt Text
```html
<img src="chart.png" alt="Line chart showing user growth from 100 to 500 over 6 months">
```

### ARIA Labels
```html
<button aria-label="Close dialog">
    <span class="icon-x"></span>
</button>
```
