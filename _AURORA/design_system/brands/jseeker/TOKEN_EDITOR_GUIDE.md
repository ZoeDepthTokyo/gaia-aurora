# jSeeker Design Token Editor - Quick Start Guide

## What is the Token Editor?

An interactive UI tool that lets you **tweak jSeeker's design system in real-time** using sliders and color pickers. No code editing required—just drag, adjust, and see changes instantly in the live preview.

---

## How to Access

1. **Launch the jSeeker design system:**
   ```bash
   cd X:\Projects\_GAIA\_AURORA\design_system\brands\jseeker
   npm install  # if first time
   npm run dev
   ```

2. **Navigate to Token Editor:**
   - Click **🎨 Token Editor** in the top navigation
   - Or visit: `http://localhost:5173` (then click Token Editor)

---

## Features

### 🎨 **Color Editing**
- **RGB Sliders** - Fine-tune red, green, blue channels individually
- **Hex Input** - Paste hex codes directly (e.g., #0057ff)
- **Color Picker** - Visual color selector for quick adjustments
- **Real-time Preview** - See changes instantly in component previews

### 🔤 **Typography Controls**
- **H1-H3 Sizes** - Adjust heading sizes from 24px-72px
- **Body Text** - Fine-tune readability (12px-20px)
- **Caption Text** - Adjust small text (10px-16px)
- **Live Examples** - See typography changes in preview panel

### 📏 **Spacing Adjustments**
- **Scale Tweaking** - Adjust xs, sm, md, lg, xl, xxl values
- **Component Spacing** - See how changes affect cards, buttons, forms
- **Grid Visualization** - Preview spacing scale as colored bars

### 🌓 **Light/Dark Mode Toggle**
- Switch between light and dark themes instantly
- Edit colors for each mode independently
- See mode-specific previews

---

## How to Use

### 1. Experiment with Colors

**Goal:** Try the Behance CRM bright blue as primary.

1. Navigate to **Colors tab** (left sidebar)
2. Find **Primary** color section
3. **Option A - Use Color Picker:**
   - Click the color square
   - Select your new blue
   - Watch preview update

4. **Option B - Paste Hex Code:**
   - Type `#0057ff` in hex input
   - Press Enter
   - See change instantly

5. **Option C - Use RGB Sliders:**
   - Drag R to 0
   - Drag G to 87
   - Drag B to 255
   - Fine-tune to taste

### 2. Adjust Typography

**Goal:** Increase H1 from 32px to 40px (Behance-inspired).

1. Navigate to **Typography tab**
2. Find **H1 Size** slider
3. Drag from 32 → 40
4. Check live preview below
5. Too big? Adjust to 36px or 38px

### 3. Test Spacing

**Goal:** Try slightly tighter card padding.

1. Navigate to **Spacing tab**
2. Find **MD Spacing** (used for card padding)
3. Reduce from 16px → 12px
4. See cards compress in preview
5. Decide if you like it

### 4. Compare Light vs Dark

1. Toggle **Light Mode / Dark Mode** (top right)
2. Adjust colors for dark mode separately
3. Ensure both modes look good
4. Export when satisfied

---

## Workflow: Adapting Behance CRM Design

### Step 1: Analyze Behance Design
Read `DESIGN_SYSTEM_COMPARISON.md` (created for you) to see:
- Color differences
- Typography scale comparison
- Recommendations

### Step 2: Try Conservative Changes (Recommended)

**Typography Evolution:**
```
H1: 32px → 40px
H2: 24px → 28px
Body: 14px → 15px
```

**In Token Editor:**
1. Go to Typography tab
2. Set H1 to 40, H2 to 28, Body to 15
3. Check preview - is it more readable?
4. Export if you like it

**Add Accent Color:**
```
accent-primary: #0057ff (Behance bright blue)
```

**In Token Editor:**
1. Go to Colors tab
2. Scroll to bottom (or edit Secondary to create accent slot)
3. Set Secondary to `#0057ff`
4. See buttons/CTAs get brighter
5. Export if you like it

### Step 3: Export Your Tokens

1. Click **Export JSON** (top right)
2. Save as `jseeker-tokens-v2.json`
3. Compare with original `tokens/colors.json`
4. Decide: Keep? Revert? Iterate?

### Step 4: Apply to Production (Optional)

**Manual Application:**
```bash
# Backup originals
cp src/tokens/colors.json src/tokens/colors.json.bak
cp src/tokens/typography.json src/tokens/typography.json.bak

# Replace with exports from Token Editor
# (You'll need to split the combined JSON into separate files)
```

**Or:** Use Token Editor values as reference to manually update token files.

---

## Tips & Tricks

### 🎯 **A/B Testing**
1. Export **Variant A** (conservative)
2. Make dramatic changes
3. Export **Variant B** (bold)
4. Compare side-by-side
5. Choose winner

### 🔄 **Iterative Design**
1. Start with small changes (1-2px adjustments)
2. Test with real content
3. Get user feedback
4. Iterate incrementally
5. Never change everything at once

### 🚨 **Accessibility Check**
When adjusting colors:
- Ensure contrast ratio ≥ 4.5:1 (AA) or 7:1 (AAA)
- Test with text colors on backgrounds
- Use WebAIM contrast checker if needed

### 💾 **Save Iterations**
Export multiple versions:
- `jseeker-tokens-original.json`
- `jseeker-tokens-behance-inspired.json`
- `jseeker-tokens-final.json`

### 🎨 **Color Harmony**
When creating new colors:
- Stay within current hue family (blues)
- Maintain saturation consistency
- Use complementary colors sparingly

---

## Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `Tab` | Navigate between inputs |
| `Arrow Up/Down` | Fine-tune slider values |
| `Enter` | Apply hex code |
| `Cmd/Ctrl + S` | Export tokens (trigger Export button) |

---

## Common Use Cases

### 1. "I want Behance's bright blue for buttons only"

**Solution:**
1. Keep Primary at `#1E3A8A` (navy)
2. Change Secondary to `#0057ff` (bright blue)
3. Update Button component to use `var(--js-secondary)` for primary variant
4. Export tokens

### 2. "Text feels too small on my 4K monitor"

**Solution:**
1. Increase all typography by 10-20%:
   - H1: 32px → 38px
   - H2: 24px → 28px
   - Body: 14px → 16px
2. Check preview on your actual monitor
3. Export if readable

### 3. "I want warmer colors (less blue, more orange)"

**Solution:**
1. Adjust Primary blue:
   - Increase R (red) channel by 20-30
   - Decrease B (blue) channel by 20-30
   - Result: Warmer, purple-ish blue
2. Keep Secondary amber (already warm)
3. Export and test

### 4. "Cards feel too cramped"

**Solution:**
1. Navigate to Spacing tab
2. Increase LG spacing from 24px → 32px
3. Cards use LG for padding
4. Check preview - better?
5. Export

---

## Troubleshooting

### Changes don't appear in preview

**Fix:**
- Check if you're on the correct tab
- Ensure light/dark mode matches your preview
- Refresh page if needed

### Exported JSON doesn't work

**Issue:** Token Editor exports ALL tokens as one file, but jSeeker needs separate files.

**Fix:**
1. Open exported JSON
2. Copy `colors` section → save to `colors.json`
3. Copy `typography` section → save to `typography.json`
4. Copy `spacing` section → save to `spacing.json`

### Colors look different in production

**Cause:** Browser rendering, monitor calibration, or incomplete CSS variable application.

**Fix:**
- Ensure all CSS variables are updated in `globals.css`
- Check for hardcoded colors in components
- Test on multiple browsers/devices

---

## Advanced: Creating Custom Color Schemes

### Monochromatic Scheme (All Blues)
```
Primary: #1E3A8A (dark blue)
Light: #60A5FA (sky blue)
Lighter: #DBEAFE (pale blue)
Dark: #1E3A8A (navy)
Darker: #1E293B (midnight)
```

### Analogous Scheme (Blue + Purple)
```
Primary: #3B82F6 (blue)
Secondary: #8B5CF6 (purple)
Accent: #06B6D4 (cyan)
```

### Complementary Scheme (Blue + Orange)
```
Primary: #1E3A8A (navy)
Secondary: #F59E0B (amber) [already have this!]
Accent: #EF4444 (red-orange)
```

---

## Next Steps

1. ✅ **Read** `DESIGN_SYSTEM_COMPARISON.md` to understand recommendations
2. 🎨 **Experiment** with Token Editor - try Behance-inspired changes
3. 📊 **Compare** original vs evolved design side-by-side
4. 👥 **Test** with real users (if possible)
5. 💾 **Export** final tokens and update production

---

## Support

**Issues?**
- Token Editor bugs: Report in `#design-system` channel
- Design questions: Consult AURORA documentation
- Color theory: Check `DESIGN_SYSTEM_COMPARISON.md`

**Resources:**
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
- [Color Hunt - Palettes](https://colorhunt.co/)
- [Type Scale Generator](https://type-scale.com/)

---

**Happy Designing! 🎨**

*Last Updated: 2026-02-10*
