# Operable — WCAG 2.1 Detailed Checks

## Keyboard Navigation (WCAG 2.1.1)
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

## Focus Indicators (WCAG 2.4.7)
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

## Link Purpose (WCAG 2.4.4)
**Requirement**: Link text describes destination

```html
<!-- Good -->
<a href="...">View GAIA documentation</a>

<!-- Bad -->
<a href="...">Click here</a>  <!-- Non-descriptive -->
```

**Check**: Every link must be understandable out of context (e.g., when a screen reader lists all links on the page).
