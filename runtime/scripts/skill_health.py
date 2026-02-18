#!/usr/bin/env python3
"""
skill_health.py -- Audit skill health: references, size, phase tags.
Exit 0: clean (or warnings only). Exit 1: issues found (errors).
"""
import re
import sys
from pathlib import Path

PHASE_TAGS = ["[OPENING]", "[CLOSING]", "[CONTEXT]"]
MAX_LINES = 500


def main():
    # Find GAIA root
    gaia_root = Path.cwd()
    for candidate in [Path.cwd(), Path(__file__).parent.parent.parent]:
        if (candidate / "registry.json").exists():
            gaia_root = candidate
            break

    skills_dir = gaia_root / ".claude" / "skills"
    issues = []
    warnings = []

    if not skills_dir.exists():
        print(f"[WARN] No .claude/skills/ directory found at {gaia_root}", flush=True)
        sys.exit(0)

    # Gather all skill names from directories
    skill_dirs = {d.name: d for d in skills_dir.iterdir() if d.is_dir()}

    # Gather all CLAUDE.md content for reference checking
    claude_md_content = ""
    for claude_md in gaia_root.rglob("CLAUDE.md"):
        try:
            claude_md_content += (
                claude_md.read_text(encoding="utf-8", errors="ignore") + "\n"
            )
        except Exception:
            pass

    # Check each skill
    for skill_name, skill_dir in sorted(skill_dirs.items()):
        skill_md = skill_dir / "SKILL.md"

        if not skill_md.exists():
            warnings.append(f"[WARN] {skill_name}: no SKILL.md found")
            continue

        content = skill_md.read_text(encoding="utf-8", errors="ignore")
        lines = content.splitlines()

        # Check line count
        if len(lines) > MAX_LINES:
            issues.append(
                f"[ERR] {skill_name}: SKILL.md is {len(lines)} lines (max {MAX_LINES})"
            )

        # Check phase tag in description
        has_phase = any(tag in content for tag in PHASE_TAGS)
        if not has_phase:
            warnings.append(
                f"[WARN] {skill_name}: missing phase tag"
                " ([OPENING], [CLOSING], or [CONTEXT])"
            )

        # Check if referenced in any CLAUDE.md
        if skill_name not in claude_md_content:
            warnings.append(f"[WARN] {skill_name}: not referenced in any CLAUDE.md")

    # Check for phantom skills (in CLAUDE.md but no directory)
    skill_table_matches = re.findall(r"`/([a-z][a-z0-9-]+)`", claude_md_content)
    for skill_ref in set(skill_table_matches):
        if skill_ref not in skill_dirs:
            warnings.append(
                f"[WARN] phantom skill: /{skill_ref} referenced in CLAUDE.md"
                f" but no .claude/skills/{skill_ref}/ exists"
            )

    # -- Report ---------------------------------------------------------------
    print(f"SKILL HEALTH REPORT -- {gaia_root}", flush=True)
    print(f"Skills found: {len(skill_dirs)}", flush=True)
    print("-" * 60, flush=True)

    for w in warnings:
        print(w, flush=True)
    for e in issues:
        print(e, flush=True)

    if not warnings and not issues:
        print("[OK] All skills healthy.", flush=True)
        sys.exit(0)
    else:
        print(
            f"\nSummary: {len(issues)} error(s), {len(warnings)} warning(s)",
            flush=True,
        )
        sys.exit(1 if issues else 0)


if __name__ == "__main__":
    main()
