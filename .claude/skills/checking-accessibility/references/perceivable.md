# Perceivable — WCAG 2.1 Detailed Checks

## Color Contrast (WCAG 1.4.3)
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

**Quick Fix**:
```css
/* Before (2.5:1) */
color: #888;
background: #fff;

/* After (7.0:1) */
color: #333;
background: #fff;
```

## Alt Text (WCAG 1.1.1)
**Requirement**: Text alternatives for non-text content

```html
<!-- Good -->
<img src="chart.png" alt="Bar chart showing 60% increase in users">

<!-- Bad -->
<img src="chart.png" alt="chart">  <!-- Too vague -->
<img src="chart.png">  <!-- Missing alt -->
```

**Check**:
- Images have alt attribute
- Decorative images have alt=""
- Icons have ARIA labels
- Charts have text descriptions

**Quick Fix**:
```html
<img src="chart.png" alt="Line chart showing user growth from 100 to 500 over 6 months">
```

## Heading Hierarchy (WCAG 1.3.1)
**Requirement**: Logical heading structure (h1 → h2 → h3)

```
✅ h1 → h2 → h3
❌ h1 → h3 (skipped h2)
❌ h3 → h2 (backwards)
```

**Streamlit note**: Use `st.subheader()` instead of `st.markdown("### ...")` to maintain proper heading levels in the generated HTML.
