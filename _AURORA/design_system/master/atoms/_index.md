# AURORA Atom Library

**Version:** 0.1.0 | **Last Updated:** February 9, 2026

Atoms are the smallest UI building blocks. They cannot be decomposed further. All atoms inherit master design tokens. Brand kits override colors, radii, and font family only.

---

## Catalog

| Atom | Variants | Status | Brand Override | Notes |
|------|----------|--------|---------------|-------|
| Button | primary, secondary, ghost, danger, icon-only | Planned | Color, radius | Primary action = filled, secondary = outlined |
| Input | text, number, date, search, password | Planned | Color, radius | Always pair with label (accessibility) |
| Select/Dropdown | single, multi, searchable | Planned | Color, radius | Use native select for simple cases |
| Checkbox | default, indeterminate | Planned | Color | Group with fieldset for related options |
| Radio | default | Planned | Color | Use for mutually exclusive choices (2-5 options) |
| Toggle/Switch | default, with label | Planned | Color | Use for binary on/off settings |
| Badge | status, count, label | Planned | Color | Status: success/warning/error/info/neutral |
| Icon | system set (Lucide) | Planned | Color only | 24x24 default, 16x16 inline, 32x32 hero |
| Tag/Chip | removable, static | Planned | Color, radius | For categories, filters, selections |
| Avatar | image, initials, placeholder | Planned | Radius | Circle default, square for groups |
| Tooltip | text, rich | Planned | None | Max 80 characters. Use for supplementary info only. |
| Divider | horizontal, vertical | Planned | Color | Use `neutral.200` default |
| Spinner/Loader | small, medium, large | Planned | Color | Use within buttons, cards, or as page overlay |
| Link | inline, standalone | Planned | Color | Underline on hover, visited state optional |
| Label | default, required | Planned | Color | Pair with every form input |

---

## Design Principles for Atoms

1. **Single responsibility** — Each atom does one thing
2. **Stateless by default** — State is managed by the consuming component
3. **Accessible** — Every atom meets WCAG 2.1 AA independently
4. **Composable** — Atoms combine into molecules without modification
