# AURORA Organism Library

**Version:** 0.1.0 | **Last Updated:** February 9, 2026

Organisms are complex UI patterns composed of molecules and atoms. They represent distinct sections of an interface.

---

## Catalog

| Organism | Use Case | Status | Notes |
|----------|----------|--------|-------|
| Dashboard Layout | Sidebar + header + content grid | Planned | Primary app shell. Collapsible sidebar, responsive grid. |
| Data Table | Header + rows + pagination + filters + sort | Planned | Supports column resize, row selection, bulk actions, export. |
| Wizard/Stepper | Steps + content panel + navigation | Planned | Linear or branching. Auto-advance or manual. Progress indicator. |
| Node Editor | Canvas + nodes + edges + toolbar | Planned | For ABIS. Pan/zoom canvas, drag-connect, property panels. |
| Form Builder | Field groups + validation + submission | Planned | Multi-section forms with collapsible groups. Server-side validation. |
| Settings Panel | Sections + toggles + save actions | Planned | Grouped settings with section headers. Unsaved changes warning. |
| Modal/Dialog | Overlay + header + content + actions | Planned | Sizes: sm (400px), md (560px), lg (720px). Trap focus inside. |
| Sidebar Navigation | Logo + nav groups + user menu + collapse | Planned | Grouped nav items with section labels. Persistent or collapsible. |
| Command Palette | Search input + results list + keyboard nav | Planned | Cmd+K trigger. Fuzzy search. Recent items. Categorized results. |
| Toast Stack | Notification queue + auto-dismiss | Planned | Bottom-right position. Max 3 visible. 5s auto-dismiss default. |
| Detail Panel | Header + metadata + content + actions | Planned | Slide-out or inline. For viewing/editing record details. |
| Filter Bar | Filter chips + add filter + clear all | Planned | Persistent filters shown as removable chips above content. |

---

## Composition Rules

1. **Organisms compose molecules and atoms** — They represent page sections, not full pages
2. **Self-contained** — Each organism manages its own internal state and layout
3. **Page-agnostic** — Organisms should work in any page context
4. **GAIA-compliant** — Complex organisms must include human-in-the-loop gates for AI actions
