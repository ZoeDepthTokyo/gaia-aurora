---
name: design-review
description: Review UI designs against AURORA design system and GAIA brand guidelines
disable-model-invocation: false
---

# Design Review

Reviews UI designs, prototypes, or implemented components against AURORA's design system (30% master DNA + 70% brand variation) and GAIA constitutional principles.

## Usage
```
/design-review <component_name> [--phase spec|prototype|implementation]
/design-review --figma <url> [--export-feedback]
```

## Review Phases

### Spec Phase (Design Documents)
Reviews UX specifications before implementation:
- Interaction flows documented?
- Edge cases considered?
- State transitions defined?
- Responsive breakpoints planned?

### Prototype Phase (Wireframes/Mockups)
Reviews visual designs:
- Design system compliance (30% DNA)
- Brand variation appropriate (70%)
- Visual hierarchy clear?
- Accessibility considered?

### Implementation Phase (Live Code)
Reviews implemented UI:
- Matches design spec?
- Responsive implementation correct?
- Interactions polished?
- Performance acceptable?

## AURORA Design System Checklist

### 30% Master DNA (Enforced)

**Must Match:**
- ✅ Typography scale (16px base, 1.25 ratio)
- ✅ Spacing grid (4px base unit)
- ✅ Breakpoints (mobile 320px, tablet 768px, desktop 1024px)
- ✅ Accessibility (WCAG 2.1 AA minimum)
- ✅ Motion timing (200ms quick, 400ms standard, 600ms slow)
- ✅ Layout grid (12-column, 24px gutters)

**Violations**: Flagged as CRITICAL (blocks approval)

### 70% Brand Variation (Flexible)

**Can Customize:**
- Colors (primary, secondary, accent)
- Font families (but keep scale ratio)
- Border radii (but maintain consistency)
- Shadows (depth levels 1-3)
- Component skins (visual treatment)
- Imagery style

**Guidelines**: Should align with brand personality

## Process

1. **Load Design Context**
   - Read AURORA design system tokens
   - Load brand kit (if exists): `design_system/brands/{component}/`
   - Check CLAUDE.md for component role

2. **Token Validation**
   ```javascript
   // Check master tokens compliance
   designTokens.spacing.base === 4  // Must be 4px
   designTokens.typography.scale === 1.25  // Must be 1.25
   ```

3. **Brand Consistency**
   - Compare with other GAIA components
   - Flag inconsistencies across products
   - Suggest brand kit if missing

4. **Constitutional Validation**
   - Glass-box: Controls explainable?
   - HITL: Destructive actions require confirmation?
   - Progressive disclosure: Complexity hidden?

5. **Generate Feedback**
   - Pass/fail for 30% DNA
   - Suggestions for 70% variation
   - Wireframe annotations (if needed)

## Example Output

```
Design Review: _VULCAN Streamlit UI
====================================

Component: VULCAN Project Creator
Reviewer: AURORA UX/UI Lead
Phase: Implementation
Date: Feb 9, 2026

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Overall Score: 78/100 (B+)
Status: ✅ APPROVED (with minor suggestions)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

30% Master DNA Compliance
─────────────────────────

✅ Typography Scale: Correct (16px base, 1.25 ratio)
✅ Spacing Grid: Correct (4px base, consistent usage)
✅ Breakpoints: Not applicable (desktop-only Streamlit)
✅ Accessibility: WCAG 2.1 AA met (contrast checked)
✅ Motion: Streamlit defaults acceptable
✅ Layout: 12-column grid implicit in Streamlit

Master DNA: ✅ 100% COMPLIANT

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

70% Brand Variation
───────────────────

Brand Kit: _VULCAN (exists at design_system/brands/vulcan/)

Colors:
✅ Primary: #FF6B35 (Forge Orange) - Appropriate for creation tool
✅ Secondary: #004E89 (GAIA Blue) - Ecosystem consistency
⚠️  Accent: #F7C59F (Warm Beige) - Low contrast with white background
   → Suggest: Darken to #D4A574 for better readability

Typography:
✅ Headings: Inter Bold (matches GAIA standard)
✅ Body: Inter Regular
💡 Suggestion: Consider monospace for code previews

Shadows:
✅ Card depth: Level 2 (8px blur, 2px offset) - Consistent
✅ Modal depth: Level 3 (16px blur, 4px offset) - Good hierarchy

Component Skins:
✅ Buttons: Streamlit default (acceptable)
⚠️  Inputs: Default styling (consider custom CSS for brand)

Brand Variation: 🟡 85% GOOD (minor improvements suggested)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

UX Patterns
───────────

✅ 7-step wizard: Clear progression
✅ Preview before generation: Good HITL practice
✅ Back/forward navigation: Intuitive
⚠️  Step indicators: Could be more visual (numbered circles)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Constitutional Compliance
─────────────────────────

✅ Glass-box: Scaffold preview shown before creation
✅ HITL: User must approve before file generation
✅ Progressive disclosure: Advanced options in expanders
✅ Sovereignty: User can cancel at any step

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Cross-Component Consistency
────────────────────────────

Compared with: _ARGUS, _AURORA, jSeeker

✅ Color palette consistent with GAIA ecosystem
✅ Typography matches ARGUS dashboard
⚠️  Button styles differ from jSeeker
   → Note: Acceptable (different products, different personalities)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Recommendations
───────────────

🎯 High Priority
1. Darken accent color for WCAG compliance
2. Add visual step indicators (numbered circles)

💡 Nice to Have
3. Consider monospace font for code previews
4. Add custom CSS for input styling (brand alignment)
5. Add micro-animations on step transitions

🏆 Strengths to Maintain
- Excellent HITL implementation
- Clear wizard flow
- Good preview functionality

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Decision
────────

✅ APPROVED for production

Conditions:
- Fix accent color contrast (MUST before launch)
- Step indicators improvement (SHOULD for v0.5.0)

Signed: AURORA UX/UI Lead
Date: 2026-02-09
```

## Review Criteria

### Critical (Must Pass)
- 30% master DNA compliance
- WCAG 2.1 AA accessibility
- Constitutional principles honored
- No blocking usability issues

### High (Should Pass)
- 70% brand consistency
- Cross-component patterns maintained
- Good interaction design
- Responsive if applicable

### Medium (Nice to Have)
- Polish and delight details
- Micro-interactions
- Advanced accessibility (beyond AA)

## Options

- `--phase <phase>`: Specify review phase (spec/prototype/implementation)
- `--figma <url>`: Review Figma designs (requires Figma MCP)
- `--export-feedback`: Save feedback as markdown + annotated screenshots
- `--strict`: Enforce strict 30% DNA (fail on any violation)
- `--compare <component>`: Compare with another component's design

## Integration

### With UX Audit
```
/ux-audit _VULCAN
/design-review _VULCAN --phase implementation
```

### With AURORA Agent (Full Workflow)
```
claude --agent aurora-ux-lead
/aurora-intake my-project
/aurora-inspire my-project
/aurora-spec my-project
/aurora-build my-project
/design-review my-project --phase prototype
/aurora-refine my-project
```

### With Figma (When Available)
```
/design-review --figma https://figma.com/file/...
```

## Design System References

**Master DNA Tokens**:
- Location: `_AURORA/design_system/master/tokens.json`
- Guidelines: `_AURORA/design_system/master/guidelines.md`

**Brand Kits**:
- Template: `_AURORA/design_system/brands/_template/`
- VULCAN: `_AURORA/design_system/brands/vulcan/`
- ARGUS: `_AURORA/design_system/brands/argus/`

**Inspiration Library**:
- Curated refs: `_AURORA/inspiration/library.json`
- Component examples: `_AURORA/inspiration/components/`
