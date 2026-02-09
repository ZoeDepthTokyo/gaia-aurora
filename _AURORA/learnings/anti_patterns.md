# AURORA Anti-Patterns

UX decisions that failed. Learn from these to avoid repeating mistakes across GAIA products.

---

## Template

```markdown
# Anti-Pattern: {Name}
**ID:** ANTI-{NNN}
**Project:** {where discovered}
**Date:** {date}

## What Happened
{Description of the bad UX decision}

## Why It Failed
{User feedback or usability issue}

## What To Do Instead
{Link to correct pattern or description of better approach}
```

---

## ANTI-001: Too Many Sequential Clicks

**ID:** ANTI-001
**Project:** jSeeker (PROTEUS v0.1.0)
**Date:** 2026-02-06

### What Happened
Resume generation required 6 sequential button clicks across different sections. Each step had its own "Run" button: parse JD, match templates, adapt content, score ATS, generate PDF, export.

### Why It Failed
User wanted 1-click generation. Sequential steps felt like busywork without clear value at each gate. The intermediate results were not actionable — users just clicked through them.

### What To Do Instead
Combine related actions into a single pipeline trigger. Use a wizard with auto-advance or a single "Generate" button that runs the full pipeline. Show progress and traceability in collapsible expanders, not mandatory gates. Only interrupt the flow when user input is genuinely required.
