# Design: GAIA Skill Usability System

## Architecture: 3 Pillars

### Pillar 1: AUTOMATE (4 hook scripts)
- `skill_guard.py` — PreToolUse guard blocks component edits without active change spec
- `skill_suggester.py` — PostToolUse hook suggests relevant skill for edited file
- `session_exit_check.py` — Stop hook prints session recap + advisories on exit
- `skill_health.py` — Audit skill health: references, size, phase tags

### Pillar 2: SURFACE (phase-aware listing + transparency)
- All 15+ skills get phase tags ([OPENING], [CLOSING], [CONTEXT])
- Trigger keywords added to description fields
- "Why" statements explain when each skill is useful
- `/listing-skills` overhauled with phase sections and flags

### Pillar 3: REDUCE (content improvements)
- Deep updates to 6 key skills (explaining-code, orchestrating-agents, etc.)
- New `/testing-webapp` skill for Playwright E2E testing
- Root CLAUDE.md gaps fixed (Phase column, missing skill refs)

## Hook Format: Announce -> Explain -> Escape
All hook messages follow 3-line format:
```
[HOOK: <name>] <trigger description>
-> TIP: /<skill> — <reason>
-> Manual: <example invocation>
```

## Session Phase Classification
- OPENING: creating-change, orienting-to-component, listing-skills
- CLOSING: reconciling-gaia, archiving-change, validating-specs
- CONTEXT: all others (triggered by file patterns, not session phase)

## Dependencies
Phase 0 -> Phase 1 -> Phase 2 -> Phase 3 -> {Phase 4, 5, 6} -> Phase 7 -> Phase 8
