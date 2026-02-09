# AURORA Master Design Guidelines

**Version:** 0.1.0 | **Last Updated:** February 9, 2026

These guidelines define the 30% Visual DNA that ALL GAIA products inherit. Brand kits can override the remaining 70% but MUST preserve these foundations.

---

## 1. Core Principles

### 1.1 Clarity Over Cleverness
Every interface element must communicate its purpose immediately. If a user needs to think about what something does, redesign it.

### 1.2 Progressive Disclosure
Show the minimum viable interface first. Reveal complexity through deliberate user actions (expand, hover, navigate deeper). Never overwhelm.

### 1.3 Consistency Within, Personality Across
Products share foundational patterns (spacing, typography scale, interaction models) but express unique brand personality through color, imagery, and tone.

### 1.4 Accessible by Default
WCAG 2.1 AA is the minimum. Design for keyboard-first navigation, screen reader compatibility, and sufficient color contrast (4.5:1 for text, 3:1 for UI elements).

### 1.5 Feedback Always
Every user action gets a response: loading states, success confirmations, error explanations, empty state guidance. Silence is failure.

---

## 2. Typography

### 2.1 Type Scale

| Token | Size | Use Case |
|-------|------|----------|
| `xs` | 0.75rem (12px) | Captions, badges, metadata |
| `sm` | 0.875rem (14px) | Secondary text, table cells |
| `base` | 1rem (16px) | Body text, form inputs |
| `lg` | 1.125rem (18px) | Lead paragraphs, emphasis |
| `xl` | 1.25rem (20px) | Section headers (h4) |
| `2xl` | 1.5rem (24px) | Page sub-headers (h3) |
| `3xl` | 1.875rem (30px) | Page headers (h2) |
| `4xl` | 2.25rem (36px) | Hero headers (h1) |
| `5xl` | 3rem (48px) | Display text |

Use the token scale exclusively. No arbitrary font sizes.

### 2.2 Font Stacks
- **Primary**: Inter (or brand override) with system-ui fallback
- **Monospace**: JetBrains Mono for code, technical content, and data

### 2.3 Line Height
- `tight` (1.25): Headings, single-line labels
- `normal` (1.5): Body text, paragraphs
- `relaxed` (1.75): Long-form reading, documentation

---

## 3. Spacing

### 3.1 Base Unit
All spacing uses a 4px base unit. Use token values only — never arbitrary pixel values.

### 3.2 Common Patterns
- **Inline spacing** (between related items): `scale.2` (8px)
- **Element gap** (between form fields): `scale.4` (16px)
- **Section gap** (between content sections): `scale.8` (32px)
- **Page padding**: `scale.6` (24px) minimum

### 3.3 Component Internal Spacing
- Button padding: `scale.2` vertical, `scale.4` horizontal
- Card padding: `scale.4` to `scale.6`
- Modal padding: `scale.6`
- Table cell padding: `scale.2` vertical, `scale.3` horizontal

---

## 4. Color

### 4.1 Neutral Palette
The neutral scale (0-950) is shared across all products. Brand kits override primary, secondary, and accent colors only.

### 4.2 Semantic Colors (Fixed — Never Override)
| Token | Hex | Use |
|-------|-----|-----|
| `success` | #16a34a | Confirmations, completed states |
| `warning` | #d97706 | Caution, needs attention |
| `error` | #dc2626 | Failures, destructive actions |
| `info` | #2563eb | Informational, neutral highlights |

### 4.3 Contrast Requirements
- Text on background: minimum 4.5:1 ratio
- Large text (18px+ or 14px+ bold): minimum 3:1 ratio
- UI elements (borders, icons): minimum 3:1 ratio
- Focus indicators: minimum 3:1 against adjacent colors

---

## 5. Layout

### 5.1 Grid System
12-column grid with 24px gutters. Content max-width: 1280px.

### 5.2 Responsive Breakpoints

| Breakpoint | Width | Target |
|-----------|-------|--------|
| `sm` | 640px | Mobile landscape |
| `md` | 768px | Tablet |
| `lg` | 1024px | Desktop |
| `xl` | 1280px | Large desktop |
| `2xl` | 1536px | Ultra-wide |

### 5.3 Content Density
- **Spacious**: Clinical/therapeutic contexts (HART OS)
- **Comfortable**: General applications (default)
- **Compact**: Data-heavy interfaces (trackers, tables)

---

## 6. Interaction

### 6.1 Hover States
All interactive elements must have visible hover states. Use opacity, background color shift, or subtle shadow change.

### 6.2 Focus States
Visible focus ring on all focusable elements. Use `outline` with 2px offset, contrasting color. Never use `outline: none` without replacement.

### 6.3 Transitions
Use motion tokens for all transitions:
- **Micro-interactions** (hover, focus): `fast` (150ms)
- **UI changes** (expand, collapse): `normal` (300ms)
- **Page transitions**: `slow` (500ms)
- Easing: `default` for most, `bounce` for playful elements only

### 6.4 Loading States
- Skeleton screens preferred over spinners for content areas
- Spinners for discrete actions (button loading, form submission)
- Progress bars for multi-step processes with known duration

---

## 7. Component Patterns

### 7.1 Empty States
Every view that can be empty MUST have:
1. An illustration or icon
2. A clear message explaining WHY it's empty
3. A primary action to resolve the empty state

### 7.2 Error States
1. Inline validation: show below the field, in `error` color
2. Toast notifications: for async errors (API failures)
3. Error pages: for unrecoverable states (404, 500)
4. Always include: what happened + what the user can do

### 7.3 Confirmation Dialogs
Required before any destructive action (delete, overwrite, discard). Include:
- Clear description of what will happen
- Consequence statement
- Cancel (default focus) + Confirm (destructive style)

---

## 8. Accessibility Checklist

For every component and page:
- [ ] Keyboard navigable (Tab, Enter, Escape, Arrow keys)
- [ ] Screen reader labels (aria-label, alt text)
- [ ] Color contrast passes (4.5:1 text, 3:1 UI)
- [ ] Focus order matches visual order
- [ ] No information conveyed by color alone
- [ ] Touch targets minimum 44x44px
- [ ] Motion respects `prefers-reduced-motion`
- [ ] Form inputs have associated labels
