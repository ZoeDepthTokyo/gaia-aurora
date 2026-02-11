# jSeeker Design System - Quick Start

## 🚀 Launch Token Editor in 3 Steps

### Step 1: Install Dependencies
```bash
cd X:\Projects\_GAIA\_AURORA\design_system\brands\jseeker
npm install
```

### Step 2: Start Dev Server
```bash
npm run dev
```

### Step 3: Open Token Editor
- Browser will open automatically to `http://localhost:5173`
- Click **🎨 Token Editor** in the navigation
- Start tweaking colors, typography, spacing!

---

## 📚 What's Included

### Design Tokens (JSON)
```
src/tokens/
├── colors.json         # Light/dark mode colors
├── typography.json     # Font sizes, weights, line heights
├── spacing.json        # 4px grid spacing scale
├── shadows.json        # 4-level elevation system
├── borders.json        # Border radii and widths
└── icons.json          # Icon sizes
```

### React Components
```
src/components/
├── atoms/              # Button, Input, Checkbox, etc.
├── molecules/          # Card, Badge, Alert, Modal
├── organisms/          # DataTable, Header, StatCard
└── templates/          # DashboardLayout, ListViewTemplate
```

### Token Editor
```
src/components/DesignTokenEditor.tsx
```
Interactive UI for real-time token editing.

---

## 🎨 How to Use Token Editor

1. **Edit Colors** - RGB sliders, hex input, color picker
2. **Adjust Typography** - Sliders for H1-H3, body, caption
3. **Tweak Spacing** - Fine-tune xs, sm, md, lg, xl, xxl
4. **Toggle Light/Dark** - Test both modes
5. **Export JSON** - Save your customizations

**See `TOKEN_EDITOR_GUIDE.md` for detailed walkthrough.**

---

## 📖 Documentation

- **DESIGN_SYSTEM_COMPARISON.md** - jSeeker vs Behance CRM analysis
- **TOKEN_EDITOR_GUIDE.md** - Complete Token Editor tutorial
- **SYSTEM_DOCUMENTATION.md** - Full design system reference
- **COMPLETION_SUMMARY.md** - Figma Make implementation notes

---

## 🎯 Quick Tasks

### Task 1: Try Behance CRM Colors
```
1. Open Token Editor
2. Navigate to Colors tab
3. Change Primary to #0057ff (Behance blue)
4. See buttons get brighter
5. Export if you like it
```

### Task 2: Increase Readability
```
1. Open Token Editor
2. Navigate to Typography tab
3. Increase Body from 14px → 15px
4. Check preview - better?
5. Export if readable
```

### Task 3: Tighten Spacing
```
1. Open Token Editor
2. Navigate to Spacing tab
3. Reduce LG from 24px → 20px
4. See cards get more compact
5. Export if you prefer it
```

---

## 🔧 Development Commands

```bash
# Start dev server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview

# Type check
npm run typecheck

# Lint
npm run lint
```

---

## 📦 What's Next?

1. **Phase 1:** Experiment with Token Editor
2. **Phase 2:** Finalize token values
3. **Phase 3:** Apply to jSeeker Python/Streamlit app
4. **Phase 4:** React migration (when ready)

---

**Need Help?** Read `TOKEN_EDITOR_GUIDE.md` for complete instructions.

**Questions?** Check `DESIGN_SYSTEM_COMPARISON.md` for design rationale.
