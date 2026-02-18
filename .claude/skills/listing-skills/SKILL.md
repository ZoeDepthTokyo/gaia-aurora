---
name: listing-skills
description: "[OPENING] Displays a quick-reference table mapping common GAIA tasks to their corresponding skills with phase tags and trigger keywords. Use when unsure which skill to invoke, during onboarding, or when asking 'what skills are available'. Triggers on: list skills, what skills, help, onboarding, which skill. Why: skill discovery prevents forgotten capabilities."
---

# GAIA Skills Quick Reference

Outputs the skill index for the current GAIA ecosystem, organized by session phase.

## Usage
```
/listing-skills [--open] [--context <topic>] [--health] [--explain <skill>]
```

## Flags

### `--open` (Opening Phase Skills Only)
Shows only skills tagged [OPENING] — useful at session start:
```
/listing-skills --open
```

### `--context <topic>` (Context-Filtered)
Shows skills relevant to a specific topic or file pattern:
```
/listing-skills --context testing
/listing-skills --context UX
```

### `--health` (Skill Health Report)
Runs `python runtime/scripts/skill_health.py` and shows the report:
```
/listing-skills --health
```

### `--explain <skill>` (Skill Deep Dive)
Shows the full description, triggers, and usage for a specific skill:
```
/listing-skills --explain reconciling-gaia
```

## Output

When invoked without flags, display this table organized by session phase:

```
GAIA Skills Quick Reference (16 skills)
========================================

OPENING (run at session start)
------------------------------
TASK                          SKILL
Starting a new feature     -> /creating-change
Component orientation      -> /orienting-to-component
List all skills            -> /listing-skills

CLOSING (run at session end)
-----------------------------
TASK                          SKILL
End of session             -> /reconciling-gaia
Archive completed change   -> /archiving-change
Validate spec format       -> /validating-specs

CONTEXT (triggered by task)
----------------------------
TASK                          SKILL
Check governance status    -> /checking-geco-status
Review UI design           -> /reviewing-design
UX quality audit           -> /auditing-ux
Accessibility check        -> /checking-accessibility
Explain unfamiliar code    -> /explaining-code
Autonomous iteration       -> /running-autonomous-loop
Registry validation        -> /syncing-registry
Multi-agent coordination   -> /orchestrating-agents
External research          -> /researching
E2E testing (Streamlit)    -> /testing-webapp
```

## Notes
- Skills use gerund naming (action-oriented)
- Each skill has YAML frontmatter with trigger keywords and phase tags
- Run `/orienting-to-component` for component-specific skill recommendations
- Run `/listing-skills --health` to check for phantom or oversized skills
- Hook scripts auto-suggest skills when relevant files are edited
