---
name: auditing-ux
description: "[CONTEXT] Performs AURORA's 7-pass UX analysis on any GAIA component or product UI. Use before launches, after major UI changes, or when reviewing usability, information architecture, or interaction flows. Triggers on: UX audit, usability, review UI, user experience, interaction design. Why: systematic UX quality assurance aligned with GAIA constitutional principles."
disable-model-invocation: false
---

# UX Audit

Performs AURORA's 7-pass UX analysis on any GAIA component or external product. Identifies usability issues, accessibility gaps, and UX improvements aligned with GAIA constitutional principles.

## Usage
```
/ux-audit <component_name> [--pass <1-7>] [--export-report]
/ux-audit --url <demo_url> [--screenshot]
```

## AURORA's 7-Pass Analysis Framework

1. **Mental Model Alignment** — Does UI match what users expect?
2. **Information Architecture** — Is navigation intuitive, groupings logical?
3. **Affordance & Action** — Are interactive elements obviously clickable?
4. **Progressive Disclosure** — Is complexity hidden until needed?
5. **System Feedback** — Are loading, empty, error, and success states clear?
6. **Interaction Patterns** — Keyboard, touch, responsive, shortcuts?
7. **Accessibility (WCAG 2.1 AA)** — Color contrast, screen readers, focus?

For detailed checks and outputs per pass, see references/7-pass-framework.md.

## Process

1. **Component Discovery**
   - Identify UI files (Streamlit, HTML, or screenshot)
   - Load CLAUDE.md for context
   - Understand component role in GAIA

2. **Run 7 Passes**
   - Execute each pass sequentially
   - Document findings with severity (Critical/High/Medium/Low)
   - Screenshot examples (if applicable)

3. **GAIA Constitutional Validation**
   - Glass-box: Is reasoning visible?
   - HITL: Are destructive actions gated?
   - Progressive trust: Does complexity scale?
   - Sovereignty: Can user override?

4. **Generate Report**
   - Executive summary
   - Pass-by-pass findings
   - Prioritized recommendations
   - Wireframe suggestions (if needed)

## Example Output

For a full annotated example (ARGUS Dashboard audit), see references/example-output.md.

## Options

- `--pass <1-7>`: Run only specific pass (for focused audits)
- `--export-report`: Save markdown report to component's docs/
- `--url <demo_url>`: Audit external URL (requires screenshots)
- `--screenshot`: Capture screenshots for visual issues
- `--wcag-only`: Run only Pass 7 (accessibility)

## Integration

### With AURORA Agent
```
claude --agent aurora-ux-lead
/ux-audit _ARGUS
```

### With Design Review
```
/ux-audit _VULCAN
/design-review _VULCAN --findings ux_audit_report.md
```

### Before Launch
```
# Pre-launch UX checklist
/ux-audit <component>
/accessibility-check <component>
```

## Anti-Patterns Detected

AURORA automatically flags common anti-patterns:
- ANTI-001: Too many clicks (jSeeker v0.1.0)
- ANTI-002: Hidden primary actions
- ANTI-003: No loading feedback
- ANTI-004: Technical error messages shown to users
- ANTI-005: Poor color contrast

## Output Artifacts

- Markdown report (detailed findings)
- Issue list (GitHub-ready)
- Wireframe suggestions (if needed)
- Before/after mockups (for critical fixes)
