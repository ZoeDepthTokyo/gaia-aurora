# Robust — WCAG 2.1 Detailed Checks

## Semantic HTML (WCAG 4.1.2)
**Requirement**: Proper HTML5 elements and ARIA

```html
<!-- Good -->
<button>Submit</button>
<nav><ul><li><a href="...">Link</a></li></ul></nav>

<!-- Bad -->
<div onclick="...">Submit</div>  <!-- Not semantic -->
```

## ARIA Labels
```html
<button aria-label="Close dialog">
    <span class="icon-x"></span>
</button>
```

**When to use ARIA**:
- Icon-only buttons need `aria-label`
- Dynamic content regions need `aria-live`
- Custom widgets need `role` attribute
- Always prefer native HTML elements over ARIA when possible

## CI/CD Integration

```yaml
# .github/workflows/accessibility.yml
- name: A11y Check
  run: |
    claude -p "/accessibility-check --ci --automated-only" --allowedTools Read,Grep
```

Exit code 1 on violations when `--ci` flag is set.

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
