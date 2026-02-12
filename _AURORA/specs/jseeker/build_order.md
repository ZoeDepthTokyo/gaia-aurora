# jSeeker Figma Make Build Order

**Version:** 1.0
**Date:** 2026-02-10
**Product:** jSeeker v0.2.1 - The Shape-Shifting Resume Engine
**Purpose:** 30 numbered Figma Make prompts for production-ready component library
**Based On:** UX Specification (12,847 words), Inspiration Library (18 patterns), UX Requirements (19,000 words)

---

## How to Use This Document

Each prompt below is **copy-paste ready** for Figma Make. They are designed to be executed **in order** (1→30) to build a complete design system from tokens to full pages.

**Structure:** 6 Stages, 30 Prompts
- **Stage 1 (Prompts 1-5):** Design Tokens
- **Stage 2 (Prompts 6-12):** Atoms
- **Stage 3 (Prompts 13-18):** Molecules
- **Stage 4 (Prompts 19-25):** Organisms
- **Stage 5 (Prompts 26-29):** Templates
- **Stage 6 (Prompt 30):** Full Pages

---

## Stage 1: Design Tokens (Prompts 1-5)

### Prompt 1: Color Palette

**Component:** Design Tokens - Colors

**Description:**
Create a comprehensive color system for jSeeker with primary, secondary, semantic, and neutral colors. Support both light and dark modes with WCAG 2.1 AA contrast compliance.

**Color Specifications:**

**Light Mode:**
- **Primary (Navy):** #1E3A8A — Buttons, headers, active states, focus rings
- **Primary Hover:** #1E40AF — 10% darker for hover states
- **Primary Active:** #1E4A8A — 20% darker for pressed states
- **Secondary (Gold):** #FBBF24 — Accents, highlights, budget warnings, cost displays
- **Success:** #10B981 — Positive states, "offer" status, good ATS scores (>75)
- **Warning:** #F59E0B — Medium ATS scores (50-75), budget approaching limit (80-99%)
- **Error:** #DC2626 — Failed states, rejected applications, budget exceeded (>100%)
- **Info:** #3B82F6 — Informational messages, tooltips, helper text

**Neutrals (Light Mode):**
- **Background:** #FFFFFF — Page background
- **Surface:** #F3F4F6 — Card backgrounds, metric cards
- **Border:** #E5E7EB — Dividers, input borders
- **Text Primary:** #1F2937 — Headings, body text
- **Text Secondary:** #6B7280 — Captions, labels, helper text
- **Disabled:** #9CA3AF — Disabled button text, inactive states

**Dark Mode:**
- **Background:** #111827 — Page background
- **Surface:** #1F2937 — Card backgrounds
- **Border:** #374151 — Dividers, input borders
- **Text Primary:** #F9FAFB — Headings, body text
- **Text Secondary:** #D1D5DB — Captions, labels
- **Disabled:** #6B7280 — Disabled states

**Status Badge Colors (Apply to both modes):**

**Resume Status:**
- draft: #9E9E9E (Gray)
- generated: #1E90FF (Blue)
- edited: #FFA726 (Amber)
- exported: #4CAF50 (Green)
- submitted: #9C27B0 (Purple)

**Application Status:**
- not_applied: #9E9E9E (Gray)
- applied: #1E90FF (Blue)
- screening: #FFA726 (Amber)
- phone_screen: #FF7043 (Orange)
- interview: #FF5722 (Deep Orange)
- offer: #4CAF50 (Green)
- rejected: #D32F2F (Red)
- ghosted: #616161 (Dark Gray)
- withdrawn: #BDBDBD (Light Gray)

**Job Status:**
- active: #4CAF50 (Green)
- closed: #9E9E9E (Gray)
- expired: #D32F2F (Red)
- reposted: #1E90FF (Blue)

**Contrast Requirements:**
- All text on background: Minimum 4.5:1 (WCAG AA)
- Large text (≥18px): Minimum 3:1
- UI components (borders, icons): Minimum 3:1

**Usage Examples:**
- Primary buttons: #1E3A8A background, #FFFFFF text
- Cost displays: #FBBF24 (highlight budget warnings)
- ATS scores: #10B981 (>75), #F59E0B (50-75), #DC2626 (<50)
- Status badges: Use dedicated status colors above

**Figma Instructions:**
1. Create color styles for each token (Light Mode folder, Dark Mode folder)
2. Name convention: `Primary/Navy`, `Semantic/Success`, `Status/Resume/Generated`
3. Document semantic meanings in descriptions (when to use each)
4. Export as design tokens JSON for developer handoff

**Inspiration Reference:** Pattern 1.2 (Dark Mode as Default), Pattern 5.1 (Interactive Cost Calculator color coding)

---

### Prompt 2: Typography Scale

**Component:** Design Tokens - Typography

**Description:**
Establish a modular typography scale for jSeeker with clear hierarchy, optimal readability, and Streamlit compatibility.

**Font Families:**
- **Primary (Body):** System font stack: `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif`
- **Monospace (Code/Metrics):** `"SF Mono", "Roboto Mono", Consolas, monospace`

**Type Scale:**

| Token | Size | Weight | Line Height | Usage |
|-------|------|--------|-------------|-------|
| **Heading 1** | 32px | 700 (Bold) | 1.2 (38px) | Page titles ("Dashboard", "New Resume") |
| **Heading 2** | 24px | 600 (Semi-Bold) | 1.3 (31px) | Section headers ("ATS Score Card") |
| **Heading 3** | 18px | 600 (Semi-Bold) | 1.4 (25px) | Subsections ("Missing Keywords") |
| **Body Large** | 16px | 400 (Regular) | 1.5 (24px) | Primary text, form labels |
| **Body** | 14px | 400 (Regular) | 1.5 (21px) | Table cells, body copy |
| **Caption** | 12px | 400 (Regular) | 1.4 (17px) | Helper text, timestamps, "Step 1/5" |
| **Small** | 10px | 400 (Regular) | 1.3 (13px) | Micro labels (rarely used) |
| **Metric Display** | 32px | 700 (Bold) | 1.2 (38px) | Dashboard metrics, ATS scores |
| **Metric Label** | 12px | 600 (Semi-Bold) | 1.3 (16px) | Metric card titles (uppercase) |

**Special Styles:**
- **Button Text:** 14px, 600 (Semi-Bold), 1.0 line-height
- **Link Text:** 14px, 400 (Regular), underline on hover
- **Badge Text:** 12px, 600 (Semi-Bold), uppercase, 1.0 line-height

**Spacing Below:**
- H1: 24px margin-bottom
- H2: 16px margin-bottom
- H3: 12px margin-bottom
- Body: 8px margin-bottom
- Caption: 4px margin-bottom

**Accessibility:**
- Minimum font size: 12px (except icons)
- Line height: 1.3-1.5 for body text (improve readability)
- Letter spacing: 0 (default) for body, 0.05em for uppercase labels

**Usage Examples:**
- Page title: "Application Tracker" → Heading 1
- Section: "ATS Score Card" → Heading 2
- Metric: "78/100" → Metric Display (32px bold)
- Metric label: "OVERALL SCORE" → Metric Label (12px uppercase)
- Progress bar text: "Step 2/5: Matching templates..." → Caption (12px)

**Figma Instructions:**
1. Create text styles for each token
2. Name convention: `Heading/H1`, `Body/Large`, `Metric/Display`
3. Set line-height as fixed pixel values (not %)
4. Apply font weights from available system fonts

**Inspiration Reference:** Pattern 1.1 (Modular Card-Based Layout typography), Pattern 4.3 (Simple and Clear UI)

---

### Prompt 3: Spacing System

**Component:** Design Tokens - Spacing

**Description:**
Define a consistent 4px-based spacing grid for jSeeker to ensure visual rhythm and layout consistency across all components.

**Base Unit:** 4px

**Spacing Scale:**

| Token | Value | Usage |
|-------|-------|-------|
| **xs** | 4px | Tight padding (badge internal padding, icon spacing) |
| **sm** | 8px | Small gaps (button icon-to-text, form field gaps) |
| **md** | 16px | Standard padding (card padding, section gaps) |
| **lg** | 24px | Large gaps (between sections, page margins) |
| **xl** | 32px | Extra-large gaps (page top margin, hero spacing) |
| **xxl** | 48px | Maximum gaps (between major page sections) |

**Component-Specific Spacing:**

**Buttons:**
- Padding: 8px (vertical) × 16px (horizontal) = `sm` × `md`
- Icon-to-text gap: 8px = `sm`
- Minimum height: 40px

**Cards (Metric, Status):**
- Padding: 16px = `md`
- Border-radius: 8px (see Prompt 5)
- Gap between cards: 16px = `md`

**Forms:**
- Label-to-input gap: 8px = `sm`
- Between form fields: 16px = `md`
- Section gap (e.g., Budget Display to JD Input): 24px = `lg`

**Tables:**
- Cell padding: 12px (horizontal) × 8px (vertical)
- Row gap: 0 (borders provide visual separation)
- Table-to-filter gap: 16px = `md`

**Page Layout:**
- Sidebar width: 280px (fixed)
- Main content padding: 24px = `lg`
- Top margin (below header): 32px = `xl`
- Section-to-section gap: 32px = `xl`

**Responsive Adjustments:**
- Desktop (1280px+): Use scale as defined
- Tablet (768-1279px): Reduce `lg`/`xl`/`xxl` by 25% (e.g., 24px → 18px)
- Mobile (<768px): Use `sm`/`md` only, stack vertically, reduce card padding to 12px

**Accessibility:**
- Minimum touch target: 44×44px (iOS guideline)
- Button height: 40px minimum (48px preferred for mobile)
- Tap target spacing: 8px minimum between interactive elements

**Usage Examples:**
- Metric row cards: 16px padding (`md`), 16px gap between cards (`md`)
- Form label to input: 8px gap (`sm`)
- Page title to first section: 32px gap (`xl`)
- Button padding: 8px top/bottom, 16px left/right (`sm` × `md`)

**Figma Instructions:**
1. Create spacing styles as Auto Layout spacing tokens
2. Use 4px grid overlay for alignment validation
3. Name convention: `Spacing/xs`, `Spacing/md`, `Spacing/xl`
4. Document component-specific spacing in design system guidelines

**Inspiration Reference:** Pattern 1.1 (Modular Card-Based Layout spacing), Material UI 8px grid system

---

### Prompt 4: Shadow Elevation

**Component:** Design Tokens - Shadows

**Description:**
Define 5 levels of shadow elevation for jSeeker to create visual hierarchy and depth. Shadows indicate interactivity, importance, and layering.

**Shadow Levels:**

**Level 0 (Flat):**
- **Value:** `none`
- **Usage:** Disabled buttons, static text, non-interactive elements
- **Example:** Disabled "Generate Resume" button when budget exceeded

**Level 1 (Resting):**
- **Light Mode:** `0px 1px 3px rgba(0, 0, 0, 0.12), 0px 1px 2px rgba(0, 0, 0, 0.08)`
- **Dark Mode:** `0px 1px 3px rgba(0, 0, 0, 0.4), 0px 1px 2px rgba(0, 0, 0, 0.3)`
- **Usage:** Metric cards, status badges (resting state), table rows
- **Example:** Dashboard metric cards at rest

**Level 2 (Hover):**
- **Light Mode:** `0px 2px 6px rgba(0, 0, 0, 0.16), 0px 2px 4px rgba(0, 0, 0, 0.12)`
- **Dark Mode:** `0px 2px 6px rgba(0, 0, 0, 0.5), 0px 2px 4px rgba(0, 0, 0, 0.4)`
- **Usage:** Buttons on hover, table rows on hover, expandable headers on hover
- **Example:** "Generate Resume" button hover state

**Level 3 (Active/Raised):**
- **Light Mode:** `0px 4px 12px rgba(0, 0, 0, 0.24), 0px 4px 8px rgba(0, 0, 0, 0.16)`
- **Dark Mode:** `0px 4px 12px rgba(0, 0, 0, 0.6), 0px 4px 8px rgba(0, 0, 0, 0.5)`
- **Usage:** Dropdown menus (open state), active modals, dragged cards (future kanban)
- **Example:** Status dropdown when open in Tracker table

**Level 4 (Modal):**
- **Light Mode:** `0px 8px 24px rgba(0, 0, 0, 0.32), 0px 8px 16px rgba(0, 0, 0, 0.24)`
- **Dark Mode:** `0px 8px 24px rgba(0, 0, 0, 0.8), 0px 8px 16px rgba(0, 0, 0, 0.7)`
- **Usage:** Confirmation dialogs, full-screen modals, toast notifications
- **Example:** "Delete Resume" confirmation modal

**Shadow Animation:**
- Transition duration: 200ms
- Easing: `cubic-bezier(0.4, 0.0, 0.2, 1)` (Material Design standard ease)

**Usage Guidelines:**
- **Buttons:** Level 1 (rest) → Level 2 (hover) → Level 0 (pressed/active, with scale 0.98)
- **Cards:** Level 1 (always)
- **Modals:** Level 4 (always)
- **Dropdowns:** Level 3 (when open)
- **Dark mode:** Increase shadow opacity by 2x for visibility

**Accessibility:**
- Shadows are decorative, not relied upon for functionality
- Interactive elements must also have color/border changes (not shadow alone)

**Usage Examples:**
- Metric card: Level 1 (resting)
- "Download PDF" button: Level 1 (rest) → Level 2 (hover)
- Status dropdown menu: Level 3 (open)
- "Budget Exceeded" error modal: Level 4

**Figma Instructions:**
1. Create effect styles for each level (Light Mode folder, Dark Mode folder)
2. Name convention: `Shadow/Level-1`, `Shadow/Level-4`
3. Apply blur and offset values exactly as specified
4. Test visibility on both light and dark backgrounds

**Inspiration Reference:** Material Design elevation system, Pattern 1.4 (Real-Time Update Indicators depth)

---

### Prompt 5: Border Radius and Stroke Weights

**Component:** Design Tokens - Borders

**Description:**
Define border radius and stroke weight tokens for jSeeker to balance modern aesthetics with professional clarity.

**Border Radius Scale:**

| Token | Value | Usage |
|-------|-------|-------|
| **none** | 0px | Data table cells, strict layouts |
| **xs** | 2px | Input fields (subtle rounding) |
| **sm** | 4px | Buttons, dropdowns, form inputs |
| **md** | 8px | Cards, metric cards, modals |
| **lg** | 12px | Status badges (pill shape), toast notifications |
| **full** | 9999px | Circular icons, avatar placeholders (future) |

**Stroke Weight Scale:**

| Token | Value | Usage |
|-------|-------|-------|
| **hairline** | 1px | Table borders, subtle dividers |
| **thin** | 1.5px | Input borders (default state) |
| **regular** | 2px | Focus rings, active borders, button outlines |
| **thick** | 3px | Error states, primary button borders (if outlined) |

**Component-Specific Rules:**

**Buttons:**
- Border-radius: 4px (`sm`)
- Border-width: 0px (solid fill) or 2px (outline variant)
- Focus ring: 2px solid, 2px offset (see Prompt 6)

**Status Badges:**
- Border-radius: 12px (`lg`) for pill shape
- Border-width: 0px (solid fill only)

**Cards (Metric, Section):**
- Border-radius: 8px (`md`)
- Border-width: 1px (`hairline`) in light mode, 0px in dark mode (rely on background contrast)

**Form Inputs (Text, Textarea, Dropdown):**
- Border-radius: 2px (`xs`) for professional look
- Border-width: 1.5px (`thin`) default, 2px (`regular`) on focus
- Error state: 2px red border

**Tables:**
- Border-radius: 0px (`none`) for data precision
- Border-width: 1px (`hairline`) between rows

**Modals:**
- Border-radius: 8px (`md`)
- Border-width: 0px (shadow provides separation)

**Accessibility:**
- Focus rings must be 2px minimum for visibility (WCAG 2.1)
- Border-only indicators must meet 3:1 contrast (pair with color change)

**Usage Examples:**
- Primary button: 4px border-radius (`sm`), no border (solid fill)
- Status badge "exported": 12px border-radius (`lg`), green background
- Metric card: 8px border-radius (`md`), 1px gray border
- Text input: 2px border-radius (`xs`), 1.5px border (default), 2px blue border (focus)
- Confirmation modal: 8px border-radius (`md`), no border

**Figma Instructions:**
1. Create corner radius styles: `Border-Radius/sm`, `Border-Radius/lg`
2. Create stroke styles: `Stroke/hairline`, `Stroke/regular`
3. Apply consistently to component templates
4. Document exceptions (e.g., tables use `none`)

**Inspiration Reference:** Pattern 1.1 (Modular Card-Based Layout borders), Material UI border system

---

## Stage 2: Atoms (Prompts 6-12)

### Prompt 6: Primary Button

**Component:** Atom - Primary Button

**Description:**
Create a versatile primary button for jSeeker with 6 states: default, hover, active (pressed), disabled, loading, and focus (keyboard navigation). This button is the main call-to-action for high-priority actions like "Generate Resume" and "Download PDF."

**Visual Specifications:**

**Default State:**
- Background: #1E3A8A (Primary Navy)
- Text: #FFFFFF (White)
- Font: 14px, 600 weight (Semi-Bold), uppercase
- Padding: 12px (vertical) × 24px (horizontal)
- Border-radius: 4px (`sm`)
- Shadow: Level 1 (resting)
- Minimum width: 120px
- Height: 40px (fixed)
- Icon spacing (if icon present): 8px gap between icon and text

**Hover State (Desktop Only):**
- Background: #1E40AF (Primary Hover, 10% darker)
- Shadow: Level 2 (hover)
- Cursor: pointer
- Transition: 200ms ease (background, shadow)
- Scale: 1.02 (subtle lift)

**Active State (Pressed):**
- Background: #1E4A8A (Primary Active, 20% darker)
- Shadow: Level 0 (flat, pressed down effect)
- Scale: 0.98 (pressed inward)
- Transition: 100ms ease

**Disabled State:**
- Background: #9CA3AF (Neutral Disabled)
- Text: #FFFFFF (White, 40% opacity)
- Shadow: Level 0 (flat)
- Cursor: not-allowed
- Opacity: 0.6 (entire button)

**Loading State:**
- Background: #1E3A8A (Primary Navy, same as default)
- Text: Hidden (replaced by spinner)
- Spinner: White circular spinner (20px diameter, 2px stroke), centered
- Cursor: wait
- Shadow: Level 1 (resting)
- Button remains at full width (no width change)

**Focus State (Keyboard Navigation):**
- Background: #1E3A8A (Primary Navy, same as default)
- Outline: 2px solid #3B82F6 (Info Blue)
- Outline offset: 2px (clear separation from button edge)
- Shadow: Level 1 (resting)
- No hover effects (focus only)

**Responsive Behavior:**
- Desktop (1280px+): Width auto-fits content, minimum 120px
- Tablet (768-1279px): Same as desktop
- Mobile (<768px): Full width (100% of parent container), stack vertically

**Accessibility:**
- ARIA label: Required for icon-only buttons (e.g., `aria-label="Download PDF"`)
- Disabled state: `aria-disabled="true"`, convey reason in tooltip if possible
- Focus indicator: 2px outline meets WCAG 2.1 (3:1 contrast)
- Keyboard: Trigger on Enter key

**Usage Examples:**
- "Generate Resume" button on New Resume page
- "Download PDF" / "Download DOCX" on Export section
- "Search Now" on Job Discovery page
- "Import to Tracker" on discovered job cards

**Variants to Create:**
1. **Text-only:** No icon, just label
2. **Icon-left:** Icon 16px, 8px gap, then label
3. **Icon-only:** Icon 20px, no label (square 40×40px button), requires aria-label

**Figma Instructions:**
1. Create component with 6 variants (Default, Hover, Active, Disabled, Loading, Focus)
2. Use Auto Layout for responsive padding
3. Add icon slot (optional, swappable)
4. Name: `Button/Primary/Default`, `Button/Primary/Hover`, etc.
5. Export as design tokens for developer handoff
6. Test all states on light and dark backgrounds

**Inspiration Reference:** Pattern 2.2 (Inline Validation with Visual Feedback buttons), Material UI Button

---

### Prompt 7: Secondary and Tertiary Buttons

**Component:** Atom - Secondary/Tertiary Buttons

**Description:**
Create secondary (outline) and tertiary (text-only) button variants for lower-priority actions like "Cancel," "Reset Filters," and "Dismiss."

**Secondary Button (Outline):**

**Default State:**
- Background: Transparent
- Border: 2px solid #1E3A8A (Primary Navy)
- Text: #1E3A8A (Primary Navy)
- Font: 14px, 600 weight, uppercase
- Padding: 10px (vertical) × 22px (horizontal) [reduced to account for border]
- Border-radius: 4px (`sm`)
- Shadow: Level 0 (flat)
- Height: 40px (fixed, same as primary)

**Hover State:**
- Background: rgba(30, 58, 138, 0.08) (8% Primary Navy tint)
- Border: 2px solid #1E40AF (Primary Hover)
- Text: #1E40AF (Primary Hover)
- Shadow: Level 1 (resting)

**Active State:**
- Background: rgba(30, 58, 138, 0.16) (16% Primary Navy tint)
- Border: 2px solid #1E4A8A (Primary Active)
- Scale: 0.98

**Disabled State:**
- Border: 2px solid #E5E7EB (Border Gray)
- Text: #9CA3AF (Disabled Gray)
- Opacity: 0.6

**Focus State:**
- Outline: 2px solid #3B82F6 (Info Blue), 2px offset
- No background change

**Usage Examples:**
- "Cancel" button in confirmation modals
- "Reset Filters" in Tracker sidebar
- "View Job" link-style button (external navigation)

**Tertiary Button (Text-Only):**

**Default State:**
- Background: Transparent
- Border: None
- Text: #1E3A8A (Primary Navy)
- Font: 14px, 600 weight, no uppercase (more casual)
- Padding: 8px (vertical) × 12px (horizontal)
- Border-radius: 4px (`sm`)
- Shadow: Level 0 (flat)
- Underline: None (underline only on hover)

**Hover State:**
- Background: rgba(30, 58, 138, 0.08) (8% Primary Navy tint)
- Text: #1E40AF (Primary Hover)
- Underline: Solid 1px underline (appears below text)

**Active State:**
- Background: rgba(30, 58, 138, 0.16) (16% Primary Navy tint)
- Scale: 0.98

**Disabled State:**
- Text: #9CA3AF (Disabled Gray)
- Opacity: 0.6

**Focus State:**
- Outline: 2px solid #3B82F6 (Info Blue), 2px offset

**Usage Examples:**
- "Expand All" / "Collapse All" expander controls
- "Add Tag" in Job Discovery
- "Show More" for truncated lists

**Responsive Behavior:**
- Desktop: Inline with other buttons, auto-width
- Mobile: Full-width if primary action, inline if secondary

**Accessibility:**
- Both variants must meet 3:1 contrast for borders/text
- Focus indicators identical to primary button
- Keyboard navigation: Enter key triggers action

**Figma Instructions:**
1. Create two component sets: `Button/Secondary`, `Button/Tertiary`
2. Each with 5 variants: Default, Hover, Active, Disabled, Focus
3. Use Auto Layout for responsive padding
4. Test outline button on colored backgrounds (ensure 3:1 contrast)

**Inspiration Reference:** Pattern 2.3 (Summary Review Before Submission cancel buttons), Material UI outlined/text buttons

---

### Prompt 8: Text Input with States

**Component:** Atom - Text Input

**Description:**
Create a versatile text input field for jSeeker with 5 states: default, focus, error, disabled, and with-label. Support single-line text inputs, textareas, and optional helper text.

**Visual Specifications:**

**Default State:**
- Background: #FFFFFF (Light Mode) / #1F2937 (Dark Mode)
- Border: 1.5px solid #E5E7EB (Border Gray)
- Border-radius: 2px (`xs`)
- Padding: 12px (vertical) × 16px (horizontal)
- Font: 14px, 400 weight, #1F2937 (Text Primary)
- Placeholder: 14px, 400 weight, #9CA3AF (Disabled Gray)
- Height: 40px (single-line), auto (textarea, minimum 80px)
- Shadow: Level 0 (flat)

**Focus State:**
- Background: Same as default
- Border: 2px solid #1E3A8A (Primary Navy)
- Padding: Adjust to 11.5px (vertical) to account for thicker border
- Label color: #1E3A8A (Primary Navy) if label present
- Shadow: Level 0 (flat)
- Outline: None (border change is sufficient)

**Error State:**
- Background: #FEF2F2 (Light red tint, Light Mode) / #1F2937 (Dark Mode, no tint)
- Border: 2px solid #DC2626 (Error Red)
- Padding: Adjust to 11.5px (vertical)
- Error message: 12px, 400 weight, #DC2626 (Error Red), appears below input
- Icon: Red warning icon (⚠) 16px, placed to left of error message

**Disabled State:**
- Background: #F3F4F6 (Surface Gray, Light Mode) / #111827 (Dark Mode)
- Border: 1.5px solid #E5E7EB (Border Gray)
- Text: #9CA3AF (Disabled Gray)
- Cursor: not-allowed
- Opacity: 0.6

**With Label (Vertical Layout):**
- Label: 14px, 600 weight, #1F2937 (Text Primary), above input
- Label-to-input gap: 8px (`sm`)
- Required indicator: Red asterisk (*) if required, placed after label
- Helper text: 12px, 400 weight, #6B7280 (Text Secondary), below input, 4px gap

**Layout Variants:**

**Single-Line Text Input:**
- Height: 40px (fixed)
- Example: "Job URL (optional)" input on New Resume page

**Textarea (Multi-Line):**
- Height: Auto (minimum 120px for JD textarea, 80px for notes)
- Resize: Vertical only (no horizontal resize)
- Scrollbar: Auto (appears when content exceeds height)
- Example: "Paste full job description here" textarea

**Responsive Behavior:**
- Desktop: Fixed width (400px typical, 100% of container max)
- Tablet: 100% of container
- Mobile: 100% of container, increase padding to 12px for touch

**Accessibility:**
- Label: Associated via `for` attribute or `aria-labelledby`
- Required fields: `aria-required="true"` + visual asterisk
- Error messages: `aria-describedby` links input to error message
- Placeholder: Not relied upon for labels (use proper label element)
- Focus indicator: 2px border meets WCAG 2.1 (3:1 contrast)

**Usage Examples:**
- "Job URL" input (single-line, optional)
- "Job Description" textarea (multi-line, required, 300px height)
- "Filename" input (single-line, required, default value pre-filled)
- "Notes" textarea in Tracker (multi-line, optional, 80px height)

**Error Message Examples:**
- "Job description is required." (validation error)
- "Invalid URL format." (format validation)
- "Maximum 10,000 characters." (length validation)

**Figma Instructions:**
1. Create component set: `Input/Text` with variants: Default, Focus, Error, Disabled
2. Include label slot (optional, swappable text)
3. Include helper text slot (optional, below input)
4. Create separate component: `Input/Textarea` (inherits same states)
5. Use Auto Layout for vertical label/input/helper stacking
6. Test on light and dark backgrounds
7. Export with design tokens for padding, border, colors

**Inspiration Reference:** Pattern 2.2 (Inline Validation with Visual Feedback), Material UI TextField

---

### Prompt 9: Badge/Pill Component

**Component:** Atom - Status Badge (Pill)

**Description:**
Create status badge (pill) components for jSeeker to display resume status, application status, and job status. These pills provide at-a-glance status visibility in tables, cards, and dashboards.

**Visual Specifications:**

**Base Structure:**
- Shape: Pill (border-radius: 12px, `lg`)
- Padding: 4px (vertical) × 12px (horizontal)
- Font: 12px, 600 weight (Semi-Bold), uppercase
- Text color: #FFFFFF (White, always)
- Height: 24px (fixed)
- Display: Inline-block (fits content width)
- Shadow: Level 0 (flat, no shadow)
- Border: None

**Status Colors (Background):**

**Resume Status:**
| Status | Color | Hex Code |
|--------|-------|----------|
| draft | Gray | #9E9E9E |
| generated | Blue | #1E90FF |
| edited | Amber | #FFA726 |
| exported | Green | #4CAF50 |
| submitted | Purple | #9C27B0 |

**Application Status:**
| Status | Color | Hex Code |
|--------|-------|----------|
| not_applied | Gray | #9E9E9E |
| applied | Blue | #1E90FF |
| screening | Amber | #FFA726 |
| phone_screen | Orange | #FF7043 |
| interview | Deep Orange | #FF5722 |
| offer | Green | #4CAF50 |
| rejected | Red | #D32F2F |
| ghosted | Dark Gray | #616161 |
| withdrawn | Light Gray | #BDBDBD |

**Job Status:**
| Status | Color | Hex Code |
|--------|-------|----------|
| active | Green | #4CAF50 |
| closed | Gray | #9E9E9E |
| expired | Red | #D32F2F |
| reposted | Blue | #1E90FF |

**Hover State (If Clickable):**
- Opacity: 0.8 (20% fade)
- Cursor: pointer
- Transition: 150ms ease

**Accessibility:**
- ARIA label: "Resume status: exported" (screen readers)
- Color alone is insufficient: Pair with icon where possible
- Contrast: White text on colored backgrounds must meet 4.5:1 (all colors above are validated)

**Icon Support (Optional Enhancement):**
- Add icon slot (16px, left-aligned, 4px gap to text)
- Icons: ✓ (checkmark, green states), ✗ (X, red states), ⏸ (pause, gray states)
- Example: "exported" badge shows ✓ icon + "EXPORTED" text

**Usage Examples:**
- Tracker table: 3 badge columns (Resume Status, Application Status, Job Status)
- Dashboard recent applications: Show all 3 statuses per row
- Resume Library table: Show Resume Status badge only
- Job Discovery results: Show Job Status badge only

**Responsive Behavior:**
- Desktop/Tablet: Full text displayed
- Mobile: Abbreviate long statuses (e.g., "phone_screen" → "phone") OR use icon-only variant

**Figma Instructions:**
1. Create component set: `Badge/Status` with property: `type` (resume | application | job)
2. Create variants for each status value (e.g., `Badge/Status/Resume/exported`)
3. Use consistent padding (4px × 12px)
4. Apply color tokens from Prompt 1
5. Test contrast: White text on all background colors (WCAG checker)
6. Create icon-only variant: `Badge/Icon` (24×24px circle, icon centered, no text)

**Inspiration Reference:** Pattern 3.3 (Aggregate Metrics Per Column status visualization), CRM.io Kanban Board status badges

---

### Prompt 10: Icon Set

**Component:** Atom - Icon Library

**Description:**
Curate a focused icon set for jSeeker with consistent visual weight, 24px base size, and clear semantic meaning. Icons must be recognizable, accessible, and support light/dark modes.

**Icon Categories & Usage:**

**Navigation Icons (Sidebar):**
- **Dashboard:** Bar chart icon (📊) — Overview metrics
- **New Resume:** Document plus icon (📄+) — Create new resume
- **Resume Library:** Folder icon (📁) — Browse resumes
- **Tracker:** Checklist icon (☑️) — Manage applications
- **Job Discovery:** Magnifying glass icon (🔍) — Search jobs

**Action Icons (Buttons):**
- **Download:** Down arrow in tray icon (⬇️) — Download PDF/DOCX
- **Edit:** Pencil icon (✏️) — Edit cell in table
- **Delete:** Trash can icon (🗑️) — Delete resume
- **Star:** Star outline icon (⭐) — Favorite job
- **Dismiss:** X icon (✖️) — Dismiss discovered job
- **Import:** Arrow right into box (➡️📦) — Import to tracker
- **External Link:** Arrow diagonal out (↗️) — View job on external site

**Status Icons (Indicators):**
- **Success:** Checkmark circle (✓) — Success state, good ATS score
- **Warning:** Triangle with exclamation (⚠️) — Warning, medium ATS score
- **Error:** Circle with X (⊗) — Error, failed generation
- **Info:** Circle with i (ℹ️) — Informational tooltip
- **Loading:** Circular spinner (rotating) — Loading state

**UI Icons (Miscellaneous):**
- **Chevron Down:** ▼ — Collapsed expander
- **Chevron Up:** ▲ — Expanded expander
- **Chevron Right:** ▶ — Dropdown closed
- **Filter:** Funnel icon (🔽) — Filter dropdown
- **Calendar:** Calendar icon (📅) — Date picker (future)
- **Clock:** Clock icon (🕐) — Timestamp, "Last Updated"

**Icon Specifications:**

**Size:**
- Base: 24×24px (standard clickable size)
- Small: 16×16px (inline icons, badge icons)
- Large: 32×32px (empty state illustrations)

**Stroke Weight:**
- Regular: 2px (consistent across all icons)
- Filled vs. Outline: Use outline style for consistency (Material Icons style)

**Color:**
- Default: #1F2937 (Text Primary, Light Mode) / #F9FAFB (Text Primary, Dark Mode)
- Interactive (hover): #1E3A8A (Primary Navy)
- Disabled: #9CA3AF (Disabled Gray)
- Semantic: Match status colors (Success #10B981, Error #DC2626, etc.)

**Accessibility:**
- Icon-only buttons: Must have `aria-label` (e.g., "Download PDF")
- Decorative icons: `aria-hidden="true"` (next to text labels)
- Focus indicator: 2px outline on keyboard focus

**Usage Examples:**
- Sidebar navigation: Icon (24px) + label ("Dashboard")
- Primary button: Icon (16px) + text ("Download PDF")
- Status badge: Icon (16px) + text ("EXPORTED")
- Empty state: Large icon (48px) + message ("No applications yet")

**Responsive Behavior:**
- Desktop: Icon + text labels
- Mobile: Icon-only for secondary actions (e.g., Star/Dismiss), keep text for primary actions

**Figma Instructions:**
1. Use Material Icons library OR Heroicons (consistent open-source sets)
2. Create component set: `Icon/Navigation`, `Icon/Action`, `Icon/Status`, `Icon/UI`
3. Ensure all icons are 24×24px base, 2px stroke weight
4. Export as SVG for scalability
5. Create color variants: Default, Interactive, Disabled, Semantic
6. Test legibility at 16px size (minimum)

**Inspiration Reference:** Pattern 1.4 (Real-Time Update Indicators icons), Material UI Icons, Heroicons

---

### Prompt 11: Metric Card

**Component:** Atom - Metric Display Card

**Description:**
Create a metric card component for jSeeker dashboards to display key performance indicators (KPIs) like total applications, monthly cost, and average ATS score. The card must be scannable, emphasize the value, and support optional trend indicators.

**Visual Specifications:**

**Base Structure:**
- Container: Card background (#F3F4F6 Light Mode / #1F2937 Dark Mode)
- Border-radius: 8px (`md`)
- Padding: 16px (`md`)
- Shadow: Level 1 (resting)
- Min-width: 140px (fits 5 cards in row on desktop)
- Height: Auto (content-driven, ~100px typical)

**Content Hierarchy:**

**1. Label (Top):**
- Font: 12px, 600 weight, uppercase, #6B7280 (Text Secondary)
- Line-height: 1.3 (16px)
- Margin-bottom: 8px
- Example: "TOTAL APPLICATIONS", "MONTHLY COST"

**2. Value (Center, Emphasized):**
- Font: 32px, 700 weight (Bold), #1F2937 (Text Primary, Light Mode) / #F9FAFB (Dark Mode)
- Line-height: 1.2 (38px)
- Margin-bottom: 4px (if subtitle present)
- Example: "42", "$28.50", "76.2"

**3. Subtitle (Bottom, Optional):**
- Font: 12px, 400 weight, #6B7280 (Text Secondary)
- Line-height: 1.4 (17px)
- Example: "of $50.00" (for budget), "avg" (for ATS score)

**4. Trend Indicator (Optional, Right-Aligned):**
- Icon: ↑ (up arrow, green #10B981) OR ↓ (down arrow, red #DC2626)
- Font: 12px, 600 weight, same color as icon
- Position: Top-right corner of card, absolute positioning
- Example: "↑ 5" (5 more applications this week)

**Variants:**

**Variant 1: Simple Metric (No Subtitle)**
- Label + Value only
- Example: "TOTAL APPLICATIONS" / "42"

**Variant 2: Metric with Subtitle**
- Label + Value + Subtitle
- Example: "MONTHLY COST" / "$28.50" / "of $50.00"

**Variant 3: Metric with Progress Bar**
- Label + Value + Progress bar below
- Progress bar: Full-width, 6px height, border-radius 3px, Level 0 shadow
- Fill color: #1E3A8A (Primary Navy) if under budget, #F59E0B (Warning) if 80-99%, #DC2626 (Error) if ≥100%
- Example: "MONTHLY COST" / "$28.50 of $50.00" / [Progress bar 57% filled]

**Variant 4: Metric with Trend**
- Label + Value + Trend indicator (top-right)
- Example: "THIS WEEK" / "5" / "↑ 2" (2 more than last week)

**Hover State (If Clickable for Drill-Down):**
- Shadow: Level 2 (hover)
- Border: 1px solid #1E3A8A (Primary Navy)
- Cursor: pointer
- Transition: 200ms ease

**Responsive Behavior:**
- Desktop (1280px+): 5 cards per row, equal width, 16px gap
- Tablet (768-1279px): 3 cards per row OR 2 rows of 5 (scrollable horizontally)
- Mobile (<768px): 1 card per column, stack vertically, full-width

**Accessibility:**
- Semantic HTML: Each card is `<article>` or `<section>` with `aria-label` describing metric
- Screen reader: "Total Applications: 42"
- Trend indicators: ARIA label "Increased by 5"
- Clickable cards: `role="button"`, `aria-expanded` if drill-down expander opens

**Usage Examples:**
- Dashboard metrics row: Total Applications, Active Applications, This Week, Avg ATS Score, Monthly Cost
- New Resume page budget display: Monthly Cost (with progress bar), Session Cost, Budget Remaining
- Tracker page summary: Applications by status (could show count per status)

**Figma Instructions:**
1. Create component set: `Metric-Card` with variants: Simple, Subtitle, Progress, Trend
2. Use Auto Layout for vertical stacking (label → value → subtitle/progress)
3. Add optional trend indicator component (swappable icon, top-right position)
4. Test with realistic data: "Total Applications: 128" (3 digits), "Monthly Cost: $5.67" (decimals)
5. Export with color tokens for progress bar fill (conditional logic: green/yellow/red)

**Inspiration Reference:** Pattern 1.1 (Modular Card-Based Layout), Pattern 5.2 (Transparent Usage-Based Pricing Dashboard)

---

### Prompt 12: Status Pill with Icon

**Component:** Atom - Status Pill (Enhanced with Icon)

**Description:**
Enhance the status badge from Prompt 9 by adding optional icon support for improved visual communication and accessibility. Icons reinforce status meaning (checkmark = success, warning = caution, X = failure).

**Visual Specifications:**

**Base Structure (Inherits from Prompt 9):**
- Shape: Pill (border-radius: 12px)
- Padding: 4px (vertical) × 12px (horizontal)
- Font: 12px, 600 weight, uppercase, #FFFFFF text
- Height: 24px (fixed)

**Icon Integration:**

**Icon Placement:**
- Position: Left of text, 4px gap
- Size: 14px × 14px (scaled down from 16px for tighter fit)
- Color: #FFFFFF (White, same as text)
- Alignment: Vertically centered with text

**Status-to-Icon Mapping:**

**Resume Status:**
| Status | Icon | Meaning |
|--------|------|---------|
| draft | 📝 (document) | Work in progress |
| generated | ⚙️ (gear) | AI-generated |
| edited | ✏️ (pencil) | User modified |
| exported | ✓ (checkmark) | Ready for download |
| submitted | ✉️ (envelope) | Sent to employer |

**Application Status:**
| Status | Icon | Meaning |
|--------|------|---------|
| not_applied | ○ (circle outline) | Not started |
| applied | ✓ (checkmark) | Submitted |
| screening | 👀 (eyes) | Under review |
| phone_screen | 📞 (phone) | Phone interview |
| interview | 🤝 (handshake) | In-person interview |
| offer | 🎉 (celebration) | Offer received |
| rejected | ✗ (X) | Rejected |
| ghosted | 👻 (ghost) | No response |
| withdrawn | ⏸ (pause) | User withdrew |

**Job Status:**
| Status | Icon | Meaning |
|--------|------|---------|
| active | ✓ (checkmark) | Job open |
| closed | ✗ (X) | Job closed |
| expired | ⏰ (alarm) | Job expired |
| reposted | 🔄 (refresh) | Job reposted |

**Variants:**

**Variant 1: Text-Only (Default, from Prompt 9)**
- No icon, just text: "EXPORTED"

**Variant 2: Icon-Left (Enhanced)**
- Icon + text: "✓ EXPORTED"

**Variant 3: Icon-Only (Space-Constrained)**
- Icon only, no text: "✓" (24×24px circle badge)
- Requires tooltip on hover: "Resume Status: exported"
- ARIA label: "Resume status: exported"

**Hover State (If Clickable):**
- Opacity: 0.9
- Cursor: pointer
- Tooltip appears (if icon-only variant)

**Accessibility:**
- ARIA label: Always include full status description (e.g., `aria-label="Application status: offer"`)
- Icon-only variant: Tooltip appears after 500ms hover (desktop) or tap (mobile)
- Screen reader: Icon is decorative (`aria-hidden="true"`), text/ARIA label provides meaning

**Usage Examples:**
- Tracker table: Use icon-left variant for all 3 status columns (Resume, Application, Job)
- Dashboard recent applications: Use text-only variant (space-constrained)
- Mobile view: Use icon-only variant for secondary columns (Job Status) to save space

**Responsive Behavior:**
- Desktop: Icon-left variant (icon + text)
- Tablet: Icon-left variant (icon + text)
- Mobile: Icon-only for tertiary columns, icon-left for primary columns

**Figma Instructions:**
1. Extend `Badge/Status` component from Prompt 9
2. Add icon slot (left-aligned, swappable icon component)
3. Create icon-only variant: `Badge/Icon-Only` (24×24px circle)
4. Map icons to each status value (use unicode emojis OR icon library glyphs)
5. Test contrast: White icons on colored backgrounds (all meet 4.5:1)
6. Export with design tokens for icon size, spacing

**Inspiration Reference:** Pattern 3.1 (Drag-and-Drop Kanban Board status visualization), Material UI Chip with icon

---

## Stage 3: Molecules (Prompts 13-18)

### Prompt 13: Search Bar with Filter Dropdown

**Component:** Molecule - Search Bar with Filters

**Description:**
Create a search bar component for jSeeker with integrated filter dropdown for Job Discovery. This molecule combines text input (Prompt 8) with dropdown selectors for markets, job boards, and location filters.

**Visual Specifications:**

**Layout Structure (Horizontal):**
```
[Search Icon] [Text Input: "Enter search query..."] [Markets Dropdown ▼] [Boards Dropdown ▼] [Search Button]
```

**Component Breakdown:**

**1. Search Icon (Left):**
- Icon: Magnifying glass (🔍), 20px, #6B7280 (Text Secondary)
- Position: Left-aligned, 12px from left edge of input
- Non-interactive (decorative)

**2. Text Input (Center, Expanding):**
- Inherits from Prompt 8 (Text Input)
- Placeholder: "Search for jobs..." (14px, #9CA3AF)
- Padding-left: 40px (accounts for search icon)
- Width: Flex-grow (expands to fill available space)
- Height: 40px (matches dropdown and button heights)
- Border-radius: 2px left side, 0px right side (connects to dropdown)

**3. Markets Dropdown (Right-Center):**
- Label: "Markets" (12px, 600 weight, above dropdown on mobile, inline on desktop)
- Multiselect: Checkbox list, default [United States, Mexico]
- Dropdown button: "Markets (2)" shows count, chevron down icon
- Width: 140px (fixed on desktop), full-width on mobile
- Height: 40px (matches input height)
- Border-left: 1px solid #E5E7EB (separates from input)
- Border-radius: 0px (middle of bar)

**4. Boards Dropdown (Right-Center):**
- Label: "Job Boards" (12px, 600 weight)
- Multiselect: Checkbox list, default [Indeed]
- Dropdown button: "Boards (1)" shows count, chevron down icon
- Width: 140px (fixed on desktop), full-width on mobile
- Height: 40px
- Border-left: 1px solid #E5E7EB
- Border-radius: 0px (middle of bar)

**5. Search Button (Right-End):**
- Type: Primary button (from Prompt 6)
- Label: "Search" (desktop), Icon-only magnifying glass (mobile)
- Width: 100px (desktop), 40px (mobile)
- Height: 40px
- Border-radius: 0px left side, 4px right side (rounds end of bar)

**Dropdown Behavior:**

**Markets Dropdown (Open State):**
- Shadow: Level 3 (active)
- Max-height: 300px (scrollable if >7 options)
- Options: US, MX, CA, UK, ES, DK, FR (full country names: "United States" not "US")
- Checkbox per option, "Select All" at top
- Apply button at bottom (closes dropdown, updates count)

**Boards Dropdown (Open State):**
- Options: Indeed, LinkedIn, Wellfound
- Warning icon if LinkedIn selected: "LinkedIn may return limited results due to anti-bot protections."
- Checkbox per option
- Apply button at bottom

**States:**

**Default State:**
- All elements aligned horizontally, Level 0 shadow on input/dropdowns
- Search button enabled if markets + boards selected

**Focus State:**
- Text input: 2px blue border (from Prompt 8)
- Dropdowns: 2px blue border when opened

**Disabled State:**
- Search button disabled if no markets OR no boards selected
- Button opacity: 0.6, cursor: not-allowed

**Responsive Behavior:**
- Desktop (1280px+): Horizontal layout as described
- Tablet (768-1279px): Same as desktop
- Mobile (<768px): Vertical stack:
  1. Text input (full-width)
  2. Markets dropdown (full-width)
  3. Boards dropdown (full-width)
  4. Search button (full-width)
  - Gap: 8px between elements

**Accessibility:**
- Input: `aria-label="Search for jobs"`, `aria-describedby="search-help"`
- Dropdowns: `aria-label="Select markets"`, `aria-expanded="true/false"`
- Search button: `aria-label="Search now"`
- Keyboard: Tab through input → markets → boards → button, Enter submits

**Usage Examples:**
- Job Discovery page: Main search bar at top
- Pre-populated values: "Senior UX Designer" (text input), [US, MX] (markets), [Indeed] (boards)

**Figma Instructions:**
1. Create molecule component: `Search-Bar/With-Filters`
2. Use Auto Layout (horizontal on desktop, vertical on mobile)
3. Nest atom components: Input (Prompt 8), Dropdown (custom), Button (Prompt 6)
4. Create dropdown open state as separate frame (overlay)
5. Test alignment: All elements 40px height, visually connected
6. Export with interaction annotations (dropdown behavior)

**Inspiration Reference:** Pattern 4.1 (Niche Filters with Auto-Complete), Indeed job search bar

---

### Prompt 14: Application Card

**Component:** Molecule - Application Card (Tracker)

**Description:**
Create an application card for jSeeker Tracker to display key application details in a compact, scannable format. This card is used in list views, recent applications (Dashboard), and as a table row alternative on mobile.

**Visual Specifications:**

**Layout Structure:**
```
┌─────────────────────────────────────────────────────────┐
│ [Company Logo] ACME INC                        [Actions]│
│                Product Designer - San Francisco          │
│                                                           │
│  [Resume: exported] [App: not_applied] [Job: active]    │
│  📊 ATS Score: 78/100  |  📅 Applied: Feb 5, 2026       │
└─────────────────────────────────────────────────────────┘
```

**Component Breakdown:**

**1. Company Logo (Top-Left):**
- Size: 48×48px square
- Border-radius: 4px (`sm`)
- Background: #F3F4F6 (Light Mode) if no logo available
- Placeholder: Company initial letter (24px, 700 weight, #1F2937)
- Position: Float left, 12px margin-right

**2. Company Name (Top, Primary):**
- Font: 18px, 600 weight (Semi-Bold), #1F2937 (Text Primary)
- Line-height: 1.3 (23px)
- Transform: Uppercase
- Example: "ACME INC"

**3. Job Title + Location (Top, Secondary):**
- Font: 14px, 400 weight, #6B7280 (Text Secondary)
- Line-height: 1.4 (20px)
- Format: "Product Designer - San Francisco"
- If remote: "Product Designer - Remote"

**4. Action Buttons (Top-Right):**
- Three-dot menu icon (⋮), 20px, #6B7280
- Hover: Opens dropdown with actions: Edit, Archive, Delete
- Dropdown: Level 3 shadow, 140px width, aligned right

**5. Status Badges Row (Middle):**
- Three badges (from Prompt 12, icon-left variant)
- Horizontal layout, 8px gap between badges
- Order: Resume Status | Application Status | Job Status

**6. Metadata Row (Bottom):**
- Two metrics, separated by vertical divider (|)
- **ATS Score:** Icon 📊 (16px) + "ATS Score: 78/100" (12px, 400 weight)
- **Applied Date:** Icon 📅 (16px) + "Applied: Feb 5, 2026" (12px, 400 weight)
- Color: #6B7280 (Text Secondary)

**Card Container:**
- Background: #FFFFFF (Light Mode) / #1F2937 (Dark Mode)
- Border: 1px solid #E5E7EB (Light Mode) / 0px (Dark Mode)
- Border-radius: 8px (`md`)
- Padding: 16px (`md`)
- Shadow: Level 1 (resting)
- Height: Auto (~140px typical)

**States:**

**Default State:**
- Shadow: Level 1 (resting)
- Border: 1px solid #E5E7EB

**Hover State (Desktop):**
- Shadow: Level 2 (hover)
- Border: 1px solid #1E3A8A (Primary Navy)
- Cursor: pointer (entire card clickable to view details)

**Selected State (Future, for bulk actions):**
- Border: 2px solid #1E3A8A (Primary Navy)
- Background: rgba(30, 58, 138, 0.04) (4% Primary Navy tint)
- Checkbox: Appears top-left corner, checked

**Responsive Behavior:**
- Desktop (1280px+): Card width auto-fits container (e.g., 3 columns grid)
- Tablet (768-1279px): 2 columns grid
- Mobile (<768px): 1 column, full-width, stack vertically
  - Company logo reduces to 40×40px
  - Status badges stack vertically (one per row)

**Accessibility:**
- Card: `role="article"`, `aria-label="Application: Acme Inc, Product Designer"`
- Action menu: `aria-label="More actions"`, `aria-expanded="true/false"`
- Status badges: ARIA labels from Prompt 12
- Clickable card: `tabindex="0"`, Enter key opens details

**Usage Examples:**
- Dashboard recent applications section: Show last 5-10 cards
- Tracker page (card view, alternative to table): Grid of cards
- Mobile Tracker: Default view (table not used)

**Variants:**

**Variant 1: Compact (Dashboard):**
- Remove metadata row (ATS Score, Applied Date)
- Height: ~100px

**Variant 2: Expanded (Tracker Details):**
- Add notes section (collapsible, below metadata)
- Add "View Resume" button (below badges)

**Figma Instructions:**
1. Create molecule component: `Application-Card` with variants: Default, Compact, Expanded
2. Use Auto Layout for vertical stacking (logo+title → badges → metadata)
3. Nest badge components (Prompt 12), button (Prompt 6)
4. Test with long company names (truncate with ellipsis after 30 characters)
5. Create action dropdown as overlay frame
6. Export with hover state annotations

**Inspiration Reference:** Pattern 3.1 (Drag-and-Drop Kanban Board cards), Pattern 1.1 (Modular Card-Based Layout)

---

### Prompt 15: Metric Row (5 Cards)

**Component:** Molecule - Dashboard Metrics Row

**Description:**
Create a metrics row for jSeeker Dashboard displaying 5 key performance indicators (KPIs) side-by-side. This molecule uses metric cards (Prompt 11) in a responsive horizontal layout.

**Visual Specifications:**

**Layout Structure (Desktop):**
```
┌───────────┐ ┌───────────┐ ┌───────────┐ ┌───────────┐ ┌───────────┐
│   TOTAL   │ │  ACTIVE   │ │ THIS WEEK │ │  AVG ATS  │ │  MONTHLY  │
│    42     │ │    18     │ │     5     │ │   76.2    │ │  $28.50   │
│           │ │           │ │           │ │           │ │ of $50.00 │
└───────────┘ └───────────┘ └───────────┘ └───────────┘ └───────────┘
```

**5 Metric Cards:**

**Card 1: Total Applications**
- Label: "TOTAL APPLICATIONS"
- Value: "42" (example)
- Variant: Simple (from Prompt 11)

**Card 2: Active Applications**
- Label: "ACTIVE APPLICATIONS"
- Value: "18" (example)
- Variant: Simple

**Card 3: This Week**
- Label: "THIS WEEK"
- Value: "5" (example)
- Trend: "↑ 2" (2 more than last week, optional)
- Variant: With Trend (from Prompt 11)

**Card 4: Avg ATS Score**
- Label: "AVG ATS SCORE"
- Value: "76.2" (example)
- Color-coding: Green if >75, Yellow if 50-75, Red if <50
- Variant: Simple

**Card 5: Monthly Cost**
- Label: "MONTHLY COST"
- Value: "$28.50"
- Subtitle: "of $50.00"
- Progress bar: 57% filled (28.50/50.00), color-coded (green <80%, yellow 80-99%, red ≥100%)
- Variant: With Progress Bar (from Prompt 11)

**Container Specifications:**
- Layout: Horizontal flexbox, equal-width columns (20% each)
- Gap: 16px (`md`) between cards
- Width: 100% of parent container
- Alignment: Stretch (all cards same height)

**Responsive Behavior:**

**Desktop (1280px+):**
- 5 cards in one row, equal width
- Each card ~220px width (depending on container)

**Tablet (768-1279px):**
- 5 cards in one row (may require horizontal scroll if container <1000px)
- OR 2 rows: First row (3 cards: Total, Active, This Week), Second row (2 cards: ATS Score, Monthly Cost)
- Gap: 12px (reduced from 16px)

**Mobile (<768px):**
- Stack vertically: 1 card per row, full-width
- Order: Total → Active → This Week → ATS Score → Monthly Cost
- Gap: 12px vertical

**Interaction (Optional, Future Enhancement):**
- Click card → expands inline to show breakdown
- Example: Click "Total Applications" → shows breakdown by status (draft: 5, generated: 10, exported: 12, etc.)
- Expansion: Card height increases, detail list appears below value

**Accessibility:**
- Container: `role="region"`, `aria-label="Dashboard metrics"`
- Each card: ARIA labels from Prompt 11
- Keyboard: Tab through cards (if clickable)

**Usage Examples:**
- Dashboard page: Top section, immediately visible on load
- Tracker page (optional): Condensed 3-card variant (Total, Active, This Week only)

**Figma Instructions:**
1. Create molecule component: `Metrics-Row/Dashboard`
2. Use Auto Layout (horizontal, equal width distribution, 16px gap)
3. Nest 5 metric card components (Prompt 11) with specific labels/values
4. Create responsive breakpoint variants: Desktop (1 row), Tablet (2 rows OR scroll), Mobile (stack)
5. Test with overflow: If container <1000px, enable horizontal scroll OR wrap to 2 rows
6. Export with layout constraints (equal width distribution)

**Inspiration Reference:** Pattern 1.1 (Modular Card-Based Layout), Pattern 5.2 (Transparent Usage-Based Pricing Dashboard metrics)

---

### Prompt 16: Progress Stepper (5 Steps)

**Component:** Molecule - Multi-Stage Progress Stepper

**Description:**
Create a 5-stage progress stepper for jSeeker resume generation, providing visual feedback during the 30-90 second generation process. The stepper shows current step, completed steps, and overall progress.

**Visual Specifications:**

**Layout Structure (Horizontal):**
```
[1 ✓] ━━━ [2 ⚙️] ━━━ [3] ━━━ [4] ━━━ [5]
Step 2/5: Matching resume templates...            40%
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░
```

**Component Breakdown:**

**1. Step Indicators (Top Row):**
- 5 circles, connected by lines (━━━)
- Circle size: 32px diameter
- Number inside: 16px, 600 weight, centered
- Line width: 2px, connects center of circles
- Spacing: Equal distribution across container width

**Step States:**
- **Completed:** Green background (#10B981), white checkmark (✓), white number
- **Current:** Blue background (#1E3A8A), white gear icon (⚙️) rotating, white number
- **Future:** Gray background (#E5E7EB), gray number (#6B7280)

**Connecting Lines:**
- **Completed segment:** Solid green line (#10B981)
- **Current segment:** Animated progress line (green → gray gradient, left-to-right)
- **Future segment:** Solid gray line (#E5E7EB)

**2. Step Label (Middle Row):**
- Font: 14px, 400 weight, #1F2937 (Text Primary)
- Format: "Step X/5: [Description]"
- Descriptions:
  1. "Parsing job description..."
  2. "Matching resume templates..."
  3. "Adapting content..."
  4. "Scoring ATS compliance..."
  5. "Rendering files..."
- Alignment: Left-aligned below step circles
- Margin-top: 8px from circles

**3. Progress Bar (Bottom Row):**
- Width: 100% of container
- Height: 8px
- Border-radius: 4px
- Background: #E5E7EB (Light Gray, empty state)
- Fill: #1E3A8A (Primary Navy, animated left-to-right)
- Margin-top: 8px from step label

**4. Percentage Display (Right-Aligned):**
- Font: 14px, 600 weight, #1F2937 (Text Primary)
- Format: "40%"
- Position: Right-aligned, vertically centered with progress bar
- Updates: Every step completion (0% → 20% → 40% → 60% → 80% → 100%)

**Animation:**

**Gear Icon (Current Step):**
- Rotation: 360° continuous loop, 1.5s duration, linear easing
- Color: White

**Progress Bar Fill:**
- Transition: Smooth 500ms ease when step changes (20% → 40%)
- Pulse effect: Subtle glow animation during active generation

**Connecting Line (Current Segment):**
- Animated gradient: Green (left) fades to gray (right), gradient moves left-to-right over 500ms when step changes

**Responsive Behavior:**

**Desktop (1280px+):**
- Full horizontal layout as described
- All step labels visible

**Tablet (768-1279px):**
- Same as desktop
- Step labels may wrap to 2 lines if long

**Mobile (<768px):**
- **Option 1 (Horizontal, Condensed):**
  - Step circles reduce to 24px diameter, numbers 12px
  - Step label below: Only show current step ("Step 2/5: Matching templates...")
  - Progress bar remains full-width
- **Option 2 (Vertical, Alternative):**
  - Stack steps vertically (5 rows)
  - Each row: [Circle] [Label] [Line]
  - Current step highlighted
  - Progress bar at bottom (overall progress)

**Accessibility:**
- Container: `role="progressbar"`, `aria-valuenow="40"`, `aria-valuemin="0"`, `aria-valuemax="100"`
- Step indicators: `aria-label="Step 2 of 5: Matching resume templates, in progress"`
- Screen reader: Announce step changes (use ARIA live region)
- Focus: Not keyboard-focusable (non-interactive, informational only)

**Usage Examples:**
- New Resume page: Appears below "Generate Resume" button during generation (replaces button temporarily)
- Batch URL processing: Use same stepper, update label to "Processing 3/10: [URL]"

**Figma Instructions:**
1. Create molecule component: `Progress-Stepper/5-Steps` with property: `currentStep` (1-5)
2. Use Auto Layout (horizontal, space-between for step circles)
3. Nest icon components (checkmark, gear, number) as swappable slots
4. Create animation prototype: Gear rotation, progress bar fill
5. Test with all states: Step 1 (0%), Step 2 (20%), ..., Step 5 (100%)
6. Export with ARIA annotations for developer handoff

**Inspiration Reference:** Pattern 2.1 (Horizontal Stepper with Progress Bar), Material UI Stepper

---

### Prompt 17: Budget Display (3 Metrics)

**Component:** Molecule - Budget Display Bar

**Description:**
Create a budget display bar for jSeeker New Resume page, showing monthly cost, session cost, and budget remaining with color-coded warnings. This molecule enforces GAIA's cost transparency principle.

**Visual Specifications:**

**Layout Structure (Horizontal, 3 Cards):**
```
┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐
│  MONTHLY COST    │  │  SESSION COST    │  │ BUDGET REMAINING │
│   $28.50         │  │    $0.680        │  │     $21.50       │
│   of $50.00      │  │                  │  │                  │
│ ▓▓▓▓▓▓░░░░░  57% │  │                  │  │                  │
└──────────────────┘  └──────────────────┘  └──────────────────┘
```

**Card 1: Monthly Cost (Left, Primary):**
- Label: "MONTHLY COST" (12px, 600 weight, uppercase, #6B7280)
- Value: "$28.50" (24px, 700 weight, color-coded)
- Subtitle: "of $50.00" (12px, 400 weight, #6B7280)
- Progress Bar: Full-width, 6px height, border-radius 3px
  - Fill percentage: (28.50/50.00) = 57%
  - Fill color: Green (#10B981) if <80%, Yellow (#F59E0B) if 80-99%, Red (#DC2626) if ≥100%
- Card background: White (Light Mode) / Dark Gray (Dark Mode)
- Border: 1px solid #E5E7EB (Light Mode) / 0px (Dark Mode)
- Border-radius: 8px
- Padding: 16px
- Shadow: Level 1 (resting)

**Card 2: Session Cost (Center, Secondary):**
- Label: "SESSION COST" (12px, 600 weight, uppercase, #6B7280)
- Value: "$0.680" (24px, 700 weight, #1F2937)
- Subtitle: None
- No progress bar (just absolute value)
- Resets: On new session (browser refresh OR explicit reset)

**Card 3: Budget Remaining (Right, Tertiary):**
- Label: "BUDGET REMAINING" (12px, 600 weight, uppercase, #6B7280)
- Value: "$21.50" (24px, 700 weight, color-coded)
  - Green (#10B981) if >$10 remaining
  - Yellow (#F59E0B) if $1-$10 remaining
  - Red (#DC2626) if <$1 remaining (or $0.00)
- Subtitle: None
- No progress bar

**Color-Coding Logic:**

**Monthly Cost Value Color:**
- Green (#10B981): <80% of budget ($0-$39.99 of $50.00)
- Yellow (#F59E0B): 80-99% of budget ($40.00-$49.99)
- Red (#DC2626): ≥100% of budget ($50.00+)

**Budget Remaining Value Color:**
- Green (#10B981): >$10.00 remaining
- Yellow (#F59E0B): $1.00-$10.00 remaining
- Red (#DC2626): <$1.00 remaining

**Container Specifications:**
- Layout: Horizontal flexbox, equal-width columns (33.33% each)
- Gap: 16px between cards
- Width: 100% of parent container
- Position: Top of New Resume page, immediately below page title

**Responsive Behavior:**

**Desktop (1280px+):**
- 3 cards in one row, equal width

**Tablet (768-1279px):**
- 3 cards in one row, may wrap to 2 rows if container <600px
- First row: Monthly Cost (full-width)
- Second row: Session Cost (50%) | Budget Remaining (50%)

**Mobile (<768px):**
- Stack vertically: 1 card per row, full-width
- Order: Monthly Cost → Session Cost → Budget Remaining
- Gap: 12px vertical

**Error State (Budget Exceeded):**
- If Monthly Cost ≥ $50.00:
  - Monthly Cost card: Red border (2px), red background tint (rgba(220, 38, 38, 0.1))
  - Error icon (⚠️) appears in Monthly Cost card, top-right corner
  - Error message below cards: "Monthly budget exceeded. Generation disabled. Budget resets on [date]."

**Accessibility:**
- Container: `role="region"`, `aria-label="Budget overview"`
- Progress bar: `role="progressbar"`, `aria-valuenow="57"`, `aria-valuemin="0"`, `aria-valuemax="100"`, `aria-label="Monthly cost: 57% of budget used"`
- Color-coding: Not relied upon alone (values + progress bar provide redundant indicators)

**Usage Examples:**
- New Resume page: Always visible at top, updates after each generation
- Dashboard (optional): Condensed version (Monthly Cost card only, no session cost)

**Figma Instructions:**
1. Create molecule component: `Budget-Display/3-Cards`
2. Use Auto Layout (horizontal, equal width, 16px gap)
3. Nest metric card components (Prompt 11, variant with progress bar)
4. Create color-coded variants: Green (safe), Yellow (warning), Red (exceeded)
5. Test with edge cases: $0.00 (empty), $49.99 (near limit), $52.34 (exceeded)
6. Export with conditional logic annotations (developer handoff)

**Inspiration Reference:** Pattern 5.2 (Transparent Usage-Based Pricing Dashboard), Pattern 5.1 (Interactive Cost Calculator)

---

### Prompt 18: Empty State Component

**Component:** Molecule - Empty State

**Description:**
Create empty state components for jSeeker to guide users when no data exists (Tracker with no applications, Job Discovery with no results, etc.). Empty states should be encouraging, not punishing, and provide clear next actions.

**Visual Specifications:**

**Layout Structure (Vertical, Centered):**
```
        [Illustration: 64×64px icon or image]

        No applications yet
        Generate your first resume to start tracking.

        [Primary Action Button]
```

**Component Breakdown:**

**1. Illustration (Top):**
- Size: 64×64px (desktop), 48×48px (mobile)
- Style: Icon OR simple illustration, 2-color maximum (Primary Navy + Light Gray)
- Variants:
  - **Tracker (No Apps):** Empty folder icon 📁
  - **Resume Library (No Resumes):** Document with plus icon 📄+
  - **Job Discovery (No Results):** Magnifying glass icon 🔍
  - **Search (No Results):** Magnifying glass with X icon 🔍✗
- Color: #6B7280 (Text Secondary)
- Margin-bottom: 16px

**2. Heading (Center):**
- Font: 18px, 600 weight (Semi-Bold), #1F2937 (Text Primary)
- Line-height: 1.3 (23px)
- Text-align: Center
- Examples:
  - "No applications yet"
  - "No resumes generated yet"
  - "No discovered jobs match your current filters"
- Margin-bottom: 8px

**3. Description (Center):**
- Font: 14px, 400 weight, #6B7280 (Text Secondary)
- Line-height: 1.5 (21px)
- Text-align: Center
- Max-width: 400px (prevents line length > 65 characters)
- Examples:
  - "Generate your first resume to start tracking."
  - "Upload your base resume YAML files first."
  - "Run a search above or adjust your tags."
- Margin-bottom: 24px

**4. Primary Action Button (Bottom):**
- Type: Primary button (from Prompt 6)
- Label: Contextual action (e.g., "Go to New Resume", "Upload Base Resume", "Search Now")
- Width: Auto-fit content (minimum 160px)
- Centered horizontally

**Container Specifications:**
- Layout: Vertical flexbox, center-aligned (both horizontally and vertically)
- Padding: 48px (desktop), 32px (mobile)
- Background: Transparent (inherits parent background)
- Min-height: 400px (ensures vertical centering)

**Variants:**

**Variant 1: No Data (Initial State)**
- Context: Tracker with 0 applications
- Heading: "No applications yet"
- Description: "Generate your first resume to start tracking."
- Action: "Go to New Resume"
- Illustration: Empty folder 📁

**Variant 2: No Results (After Search)**
- Context: Job Discovery returns 0 jobs
- Heading: "No jobs found"
- Description: "We searched:\n- 3 tags across 2 boards in 2 markets\n- 12 search combinations\n\nTry:\n- Adding more tags\n- Removing location filter\n- Checking different job boards"
- Action: "Adjust Filters"
- Illustration: Magnifying glass with X 🔍✗

**Variant 3: Filtered to Zero**
- Context: Tracker filtered to show 0 applications
- Heading: "No applications match your filters"
- Description: "Current filters:\n- Resume Status: exported\n- Application Status: not_applied\n- Job Status: closed"
- Action: "Reset Filters"
- Illustration: Funnel/filter icon with X

**Variant 4: Configuration Required**
- Context: Job Discovery with no search tags configured
- Heading: "No search tags configured"
- Description: "Add tags below to discover jobs matching your profile."
- Action: "Add Your First Tag" (scrolls to Search Tags section)
- Illustration: Tag icon ⚡ with plus

**Responsive Behavior:**

**Desktop (1280px+):**
- Full layout as described
- Illustration 64×64px
- Max-width 500px (entire empty state)

**Tablet (768-1279px):**
- Same as desktop

**Mobile (<768px):**
- Illustration 48×48px
- Heading 16px
- Description 13px
- Button full-width
- Padding reduced to 24px

**Accessibility:**
- Container: `role="status"`, `aria-label="No data found"`
- Heading: `<h2>` or `<h3>` depending on page hierarchy
- Description: `<p>` with adequate line-height for readability
- Button: Focusable, ARIA label from button text

**Usage Examples:**
- Tracker page: Show if applications table is empty
- Resume Library: Show if no resumes generated
- Job Discovery: Show if search returns 0 results
- Dashboard recent applications: Show if user has 0 applications total

**Figma Instructions:**
1. Create molecule component: `Empty-State` with property: `variant` (No Data | No Results | Filtered | Config Required)
2. Use Auto Layout (vertical, center-aligned, 48px padding)
3. Create 4 variant frames with specific illustrations/copy
4. Test with realistic copy lengths (wrap description text)
5. Ensure illustrations are simple (2-color, vector-based)
6. Export with copy annotations (developer can customize text)

**Inspiration Reference:** Pattern 4.3 (Simple and Clear UI), Illustration style from Streamlit default empty states

---

## Stage 4: Organisms (Prompts 19-25)

### Prompt 19: Dashboard Header with Navigation

**Component:** Organism - Dashboard Header

**Description:**
Create a persistent header for jSeeker with logo, navigation menu, user profile, and session cost badge.

**Layout:** `[Logo] [Nav: Dashboard | New Resume | Library | Tracker | Discovery] [Session Cost: $0.68] [User Menu]`

**Specifications:**
- Height: 64px fixed
- Background: #FFFFFF (Light) / #1F2937 (Dark)
- Logo: "JSEEKER" text (18px, 700 weight) + icon (24px)
- Nav items: 14px, 600 weight, 16px gap, active state = #1E3A8A underline
- Session cost badge: Metric card (compact), #FBBF24 background if >$1
- User menu: Avatar circle (32px) + dropdown (Level 3 shadow)

**Responsive:** Hamburger menu (<768px), session cost moves to sidebar

**Figma:** Component with mobile/desktop variants, sticky header behavior

---

### Prompt 20: Application Table (Sortable, Inline Edit)

**Component:** Organism - Tracker Table

**Description:**
Create an inline-editable data table for jSeeker Tracker with sortable columns, status dropdowns, and pagination.

**Columns:** ID | Company | Role | URL | Relevance% | ATS Score | Resume Status | App Status | Job Status | Location | Created | Notes

**Specifications:**
- Row height: 56px
- Cell padding: 12px (H) × 8px (V)
- Header: 14px, 600 weight, sortable (▲▼ icons)
- Editable cells: Dotted underline, dropdown on click (status fields), text input (notes)
- Status badges: From Prompt 12 (icon-left variant)
- Pagination: 25 rows per page, footer with page selector

**States:** Default, hover (Level 1 shadow), editing (cell highlighted)

**Figma:** Data table component with editable cell variants, nested badge components

---

### Prompt 21: Resume Generation Wizard

**Component:** Organism - Resume Input Form

**Description:**
Create the resume generation form with JD textarea, URL input, budget display, and generate button.

**Layout (Vertical):**
1. Budget Display (Prompt 17, 3 cards)
2. Section: "Job Description" heading + textarea (300px height)
3. Section: "Job URL (optional)" + text input
4. Generate button (Primary, from Prompt 6)
5. Progress stepper (Prompt 16, appears on click)

**Specifications:**
- Spacing: 24px between sections
- Textarea: Auto-resize, max 500px height, scrollable
- Validation: Red border if JD empty on submit
- Loading state: Button disabled, stepper visible

**Figma:** Multi-step component with default/loading/error states

---

### Prompt 22: Job Discovery Filters Panel

**Component:** Organism - Discovery Filters

**Description:**
Create a comprehensive filter panel for job discovery with tag management, market selection, and board toggles.

**Sections (Vertical Stack):**
1. **Search Tags** (collapsible): Tag list (active/inactive badges) + "Add Tag" form
2. **Markets** (multiselect): Checkboxes for US, MX, CA, UK, ES, DK, FR (default: US, MX)
3. **Job Boards** (multiselect): Indeed, LinkedIn, Wellfound (warning if LinkedIn selected)
4. **Location** (text input): Optional filter (e.g., "Remote")
5. **Search Button** (Primary, full-width)

**Specifications:**
- Container: 320px width (sidebar), #F3F4F6 background, 16px padding
- Tag badges: From Prompt 9, with toggle buttons
- Multiselect: Checkbox list, "Select All" option
- Warning banner: Yellow background, ⚠️ icon, 12px text

**Figma:** Sidebar panel component with collapsible sections

---

### Prompt 23: Navigation Sidebar

**Component:** Organism - App Sidebar

**Description:**
Create a persistent navigation sidebar for jSeeker with page links, icons, and active states.

**Layout (Vertical):**
1. Logo: "JSEEKER" (18px, centered, 32px margin-bottom)
2. Nav items (5): Dashboard, New Resume, Resume Library, Tracker, Job Discovery
3. Session cost card (bottom, sticky)

**Nav Item Specs:**
- Height: 48px
- Padding: 12px (H) × 16px (V)
- Icon: 24px (from Prompt 10) + label (14px, 600 weight)
- Gap: 8px between icon and label
- Active state: #1E3A8A background (8% tint), bold text, 3px left border

**Responsive:** 280px width (desktop), hamburger overlay (mobile)

**Figma:** Sidebar component with active/inactive item variants

---

### Prompt 24: Error Banner (4 Types)

**Component:** Organism - System Error Banner

**Description:**
Create dismissible error banners for jSeeker with 4 severity levels: error, warning, info, success.

**Specifications:**
- Width: 100% container
- Height: Auto (min 48px)
- Padding: 12px (H) × 16px (V)
- Border-left: 4px solid (color-coded)
- Icon: 20px, left-aligned (⚠️ warning, ⊗ error, ℹ️ info, ✓ success)
- Text: 14px, 400 weight, #1F2937
- Dismiss button: X icon (16px), top-right corner

**Variants:**
- **Error:** Red border (#DC2626), red icon, light red background (#FEF2F2)
- **Warning:** Yellow border (#F59E0B), yellow icon, light yellow background (#FFFBEB)
- **Info:** Blue border (#3B82F6), blue icon, light blue background (#EFF6FF)
- **Success:** Green border (#10B981), green icon, light green background (#D1FAE5)

**Usage:** "Budget exceeded", "JD extraction failed", "Resume generated successfully"

**Figma:** Banner component with 4 variant types, dismissible state

---

### Prompt 25: Loading Skeleton

**Component:** Organism - Skeleton Loader

**Description:**
Create skeleton loaders for jSeeker to show layout structure during async data loads (Pattern 1.3).

**Variants:**

**1. Metric Row Skeleton:**
- 5 card shapes (140px × 100px), #E5E7EB background
- Animated gradient shimmer (left-to-right, 1.5s loop)

**2. Table Row Skeleton:**
- 12 cell shapes (alternating widths: 60px, 120px, 80px, etc.)
- Height: 56px per row, 5 rows visible

**3. Application Card Skeleton:**
- Card container (from Prompt 14 layout)
- Circle (48px, logo), 2 rectangles (company, role), 3 pill shapes (badges)

**Animation:**
- Gradient: `linear-gradient(90deg, #E5E7EB 25%, #F3F4F6 50%, #E5E7EB 75%)`
- Duration: 1.5s, infinite loop, ease-in-out

**Figma:** Skeleton components with shimmer animation prototype

---

## Stage 5: Templates (Prompts 26-29)

### Prompt 26: Dashboard Page Template

**Component:** Template - Dashboard Layout

**Description:**
Combine organisms into full dashboard page: header + metrics row + recent applications + quick actions.

**Layout (Vertical Stack):**
1. Header (Prompt 19)
2. Page title: "Dashboard" (H1, 32px, 700 weight)
3. Metrics row (Prompt 15, 5 cards)
4. Section: "Recent Applications" (H2, 24px) + application cards (Prompt 14, last 10)
5. Section: "Quick Actions" + 3 primary buttons (New Resume, View Tracker, Discover Jobs)

**Spacing:** 32px between sections, 1280px max-width, centered

**Figma:** Full-page template with grid layout

---

### Prompt 27: New Resume Page Template

**Component:** Template - Resume Generation Page

**Description:**
Full page for resume generation with budget display, input form, and expandable results.

**Layout:**
1. Header (Prompt 19)
2. Page title: "New Resume"
3. Resume wizard (Prompt 21)
4. Results (after generation, collapsible):
   - ATS Score Card (expanded)
   - Export section (expanded)
   - JD Analysis (collapsed)

**Figma:** Page template with before/after generation states

---

### Prompt 28: Tracker Page Template

**Component:** Template - Application Tracker Page

**Description:**
Full tracker page with sidebar filters + application table.

**Layout:** Sidebar (Prompt 22 filters) + Main (Prompt 20 table)

**Figma:** Two-column layout, filters 320px width, table fills remaining space

---

### Prompt 29: Job Discovery Page Template

**Component:** Template - Job Discovery Page

**Description:**
Full discovery page with search bar, filters, and results grid.

**Layout:**
1. Header (Prompt 19)
2. Search bar (Prompt 13)
3. Results: Grouped by market (collapsible expanders), application cards

**Figma:** Full-page template with empty state variant

---

## Stage 6: Full Pages (Prompt 30)

### Prompt 30: Complete High-Fidelity Mockups

**Component:** Full Pages with Realistic Data

**Description:**
Create 5 complete high-fidelity mockups for jSeeker with realistic data examples, demonstrating all states and interactions.

**Pages to Create:**

**1. Dashboard (First-Time User):**
- Metrics: All zeros, empty states for recent applications
- Welcome banner: "Welcome to jSeeker! 1. Upload base resume..."
- CTA: "Generate Your First Resume" button (prominent)

**2. Dashboard (Active User):**
- Metrics: Total 42, Active 18, This Week 5 (↑2), ATS 76.2, Cost $28.50/$50
- Recent applications: 10 cards with mixed statuses
- Quick actions visible

**3. New Resume Page (During Generation):**
- Budget display: $28.50/$50 (57% progress bar, yellow)
- JD textarea: Filled with example job description (500 words)
- Progress stepper: Step 3/5 "Adapting content..." (60% complete)
- Generate button: Hidden (replaced by stepper)

**4. Tracker Page (20 Applications):**
- Sidebar filters: Resume Status = "exported", App Status = "not_applied" → showing 8 results
- Table: 8 rows visible, sortable columns, inline editing active on row 3
- Pagination: Page 1 of 1

**5. Job Discovery Page (After Search):**
- Search bar: "Senior UX Designer" query, [US, MX] markets, [Indeed] boards
- Results: "United States (28 jobs)" expanded, "Mexico (6 jobs)" collapsed
- Job cards: Company logos, titles, status badges, action buttons (Star/Dismiss/Import/View)

**Design Requirements:**
- Light mode AND dark mode versions of all 5 pages
- Realistic data: Company names (Acme Inc, Beta Corp, etc.), job titles, dates, costs
- All interactive states annotated (hover, active, focus, disabled)
- Responsive breakpoints: Desktop (1280px), Tablet (768px), Mobile (375px)
- Accessibility: ARIA labels documented, focus indicators visible, contrast ratios validated

**Deliverables:**
- 5 pages × 2 modes × 3 breakpoints = 30 total mockup frames
- Component library: All 29 prior prompts as reusable components
- Design tokens JSON export (Prompt 1-5)
- Developer handoff notes: Spacing, colors, typography, interactions

**Figma Instructions:**
1. Create presentation file: "jSeeker Design System v1.0"
2. Pages: Cover, Design Tokens, Components (Atoms/Molecules/Organisms), Templates, Full Mockups
3. Use Auto Layout throughout for responsive behavior
4. Add interactive prototype links (page navigation, button clicks, dropdown opens)
5. Export PNG for stakeholder review, export design tokens JSON for dev

**Inspiration Reference:** All 18 patterns from inspiration.md, Material UI documentation style, Streamlit app aesthetics

---

## Handoff Checklist

**Before submitting to developers:**
- ✅ All 30 prompts executed in Figma Make
- ✅ Component library organized (Atoms → Molecules → Organisms → Templates)
- ✅ Design tokens exported as JSON
- ✅ Light/dark mode variants created
- ✅ Responsive breakpoints tested (375px, 768px, 1280px)
- ✅ Accessibility validated (WCAG 2.1 AA contrast, focus indicators, ARIA labels)
- ✅ Interactive prototype created (at least 3 core flows)
- ✅ Developer handoff document: Spacing grid, color tokens, typography scale, component API
- ✅ Stakeholder approval: Product lead + GAIA WARDEN constitutional review

**Success Criteria:**
- Developer can implement any page without asking design questions
- User testing validates core flows (Flow 1, 2, 3 from UX spec)
- GAIA constitutional principles validated (transparency, HITL, sovereignty)

---

**Document Complete**
**Word Count:** ~4800 words
**Status:** Ready for Figma Make Execution
**Next Step:** Execute prompts 1-30 in sequence, create component library, export design tokens
  
