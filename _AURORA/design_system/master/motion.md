# AURORA Motion Language

**Version:** 0.1.0 | **Last Updated:** February 9, 2026

---

## Principles

1. **Purposeful** — Every animation has a reason. If removing it loses no information, remove it.
2. **Subtle** — Motion enhances, never distracts. The user should feel it, not see it.
3. **Responsive** — Respect `prefers-reduced-motion`. No exceptions.
4. **Consistent** — Same actions produce same animations across all GAIA products.

---

## Duration Scale

| Token | Duration | Use Case |
|-------|----------|----------|
| `instant` | 75ms | Immediate feedback (checkbox, toggle) |
| `fast` | 150ms | Micro-interactions (hover, focus, tooltip) |
| `normal` | 300ms | UI changes (expand, collapse, slide, fade) |
| `slow` | 500ms | Page transitions, modal entrance |
| `glacial` | 1000ms | Complex orchestrated animations (staggered lists) |

---

## Easing Curves

| Token | Value | Use Case |
|-------|-------|----------|
| `default` | `cubic-bezier(0.4, 0, 0.2, 1)` | General purpose (ease-in-out) |
| `in` | `cubic-bezier(0.4, 0, 1, 1)` | Exit animations (accelerate out) |
| `out` | `cubic-bezier(0, 0, 0.2, 1)` | Entrance animations (decelerate in) |
| `inOut` | `cubic-bezier(0.4, 0, 0.2, 1)` | Symmetric transitions |
| `bounce` | `cubic-bezier(0.68, -0.55, 0.27, 1.55)` | Playful emphasis (use sparingly) |

---

## Usage Guide

### Micro-Interactions
- **Hover states**: `fast` + `default` easing
- **Focus rings**: `fast` + `default` easing
- **Tooltips**: `fast` + `out` easing (appear), `fast` + `in` easing (dismiss)
- **Button press**: `instant` scale transform

### UI Changes
- **Accordion expand/collapse**: `normal` + `default` easing
- **Sidebar toggle**: `normal` + `default` easing
- **Tab switch**: `fast` + `default` easing
- **Dropdown open/close**: `fast` + `out` easing (open), `fast` + `in` easing (close)

### Page Transitions
- **Route change**: `slow` + `out` easing
- **Modal entrance**: `normal` + `out` easing
- **Modal exit**: `fast` + `in` easing
- **Drawer slide**: `normal` + `default` easing

### Entrance Animations
- **Fade in**: `normal` + `out` easing
- **Slide up**: `normal` + `out` easing, translate from 8px below
- **Staggered list**: `normal` + `out` easing, 50ms delay between items (max 10 items)

### Exit Animations
- **Fade out**: `fast` + `in` easing
- **Slide down**: `fast` + `in` easing

---

## Reduced Motion

When `prefers-reduced-motion: reduce` is active:
- Replace ALL motion with instant opacity changes (0 to 1, no duration)
- Disable parallax effects
- Disable auto-playing animations
- Keep essential state transitions (loading spinners) but simplify

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

---

## Streamlit Considerations

Streamlit has limited animation support:
- Use CSS transitions in `st.markdown` with `unsafe_allow_html=True` for custom components
- Use `st.spinner` for loading states (framework-native)
- Use `st.progress` for determinate progress
- For complex animations, consider custom Streamlit components with JavaScript
- Avoid animations that conflict with Streamlit's re-render cycle
