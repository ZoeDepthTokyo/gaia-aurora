---
name: reviewing-design
description: "[CONTEXT] Reviews UI designs, prototypes, and implemented components against AURORA's design system (30% master DNA + 70% brand variation) and GAIA constitutional principles. Use at spec, prototype, or implementation phase. Triggers on: review design, check UI, design feedback, design system, Figma review. Why: enforces 30% master DNA compliance across all GAIA UIs."
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

- **30% Master DNA** (enforced): typography scale, spacing grid, breakpoints, WCAG AA, motion timing, layout grid — violations block approval
- **70% Brand Variation** (flexible): colors, font families, border radii, shadows, component skins, imagery

For full token specs and violation rules, see references/design-system-checklist.md.

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

For a full annotated example (VULCAN Streamlit UI review), see references/example-output.md.

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
