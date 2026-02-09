# AURORA Molecule Library

**Version:** 0.1.0 | **Last Updated:** February 9, 2026

Molecules are groups of atoms that function as a unit. They represent the first level of meaningful UI composition.

---

## Catalog

| Molecule | Composed Of | Status | Notes |
|----------|------------|--------|-------|
| Card | Container + header + body + footer | Planned | Primary content container. Supports elevation via shadow tokens. |
| Form Group | Label + input + help text + error message | Planned | Standard form field pattern. Error replaces help text when active. |
| Nav Item | Icon + label + badge (optional) | Planned | Sidebar and top-nav building block. Active/hover/disabled states. |
| Search Bar | Input + search icon + clear button | Planned | Debounced input recommended (300ms). |
| Data Row | Cells + row actions | Planned | Building block for data tables. Supports selection checkbox. |
| Metric Card | Label + value + trend indicator | Planned | Dashboard KPI display. Trend: up/down/neutral with color coding. |
| Alert/Banner | Icon + message + action (optional) | Planned | Semantic variants: success, warning, error, info. Dismissible. |
| Breadcrumb | Link items + separators | Planned | Max 4 levels. Truncate middle items on overflow. |
| Tabs | Tab items + active indicator | Planned | Horizontal default. Use for switching views within a page section. |
| Pagination | Previous + page numbers + next | Planned | Show max 7 page buttons. Ellipsis for gaps. |
| Toolbar | Action buttons + dividers + overflow menu | Planned | Context-sensitive actions for selected items. |
| Status Indicator | Icon/dot + label | Planned | Color-coded status with text label (never color alone). |

---

## Composition Rules

1. **Molecules combine atoms** — Never nest molecules inside molecules (that's an organism)
2. **Predictable structure** — Same molecule type should have consistent internal layout
3. **Brand-aware** — Molecules inherit atom styling, which inherits brand tokens
4. **Responsive** — Molecules should stack or simplify at smaller breakpoints
