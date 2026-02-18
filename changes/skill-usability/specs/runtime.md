# Delta Specs: runtime/scripts/ -- Skill Usability System

## ADDED: skill_guard.py

### Scenario: Block edit without active change spec
Given: User attempts to edit a file in `_[A-Z]+/` path
When: No `changes/*/tasks.md` file exists with unchecked items
Then: Output BLOCKED message with rule name, why, and fix instructions
And: Exit with code 1 to block the edit

### Scenario: Allow edit with active change spec
Given: User attempts to edit a file in `_[A-Z]+/` path
When: An active `changes/*/tasks.md` file exists
Then: Allow the edit silently (exit 0)

### Scenario: Suppress with environment variable
Given: SKIP_SPEC_GUARD=1 is set in environment
When: Any file edit is attempted
Then: Allow the edit silently (exit 0)

## ADDED: skill_suggester.py

### Scenario: AURORA file triggers auditing-ux tip
Given: A file matching `_AURORA/**` is written
When: SKIP_SKILL_TIPS is not set
Then: Output 3-line Announce->Explain->Escape message for /auditing-ux

### Scenario: Dashboard file triggers auditing-ux tip
Given: A file matching `_ARGUS/dashboard/**` is written
When: SKIP_SKILL_TIPS is not set
Then: Output 3-line Announce->Explain->Escape message for /auditing-ux

### Scenario: tasks.md edit triggers archiving-change tip
Given: A file matching `changes/*/tasks.md` is written
When: SKIP_SKILL_TIPS is not set
Then: Output 3-line Announce->Explain->Escape message for /archiving-change

### Scenario: Component CLAUDE.md edit triggers reconciling-gaia tip
Given: A file matching `_*/CLAUDE.md` is written
When: SKIP_SKILL_TIPS is not set
Then: Output 3-line Announce->Explain->Escape message for /reconciling-gaia

### Scenario: Spec test edit triggers validating-specs tip
Given: A file matching `tests/test_spec_*.py` is written
When: SKIP_SKILL_TIPS is not set
Then: Output 3-line Announce->Explain->Escape message for /validating-specs

### Scenario: No match produces no output
Given: A file not matching any pattern is written
When: skill_suggester.py is invoked
Then: Output nothing (zero lines)

### Scenario: Suppress with environment variable
Given: SKIP_SKILL_TIPS=1 is set in environment
When: Any file edit triggers a pattern
Then: Output nothing (zero lines)

## ADDED: session_exit_check.py

### Scenario: Non-empty .gaia_changes triggers reconcile advisory
Given: .gaia_changes file exists and is non-empty
When: session_exit_check.py runs on session exit
Then: Print SESSION RECAP with change count
And: Print ADVISORIES section with /reconciling-gaia advisory + why explanation

### Scenario: Unchecked tasks.md items trigger advisory
Given: changes/*/tasks.md has lines matching `- [ ]`
When: session_exit_check.py runs on session exit
Then: Print advisory listing the change name and unchecked count

### Scenario: Empty state prints clean summary
Given: .gaia_changes is empty or absent
And: No unchecked tasks.md items
When: session_exit_check.py runs on session exit
Then: Print SESSION RECAP with zero entries and no ADVISORIES section

### Scenario: Always exits 0 (never blocks)
Given: Any state
When: session_exit_check.py runs
Then: Exit with code 0

## ADDED: skill_health.py

### Scenario: Detect skill missing from component CLAUDE.md
Given: A skill exists in .claude/skills/
When: That skill name appears in zero component CLAUDE.md files
Then: Report it as unreferenced

### Scenario: Detect CLAUDE.md table entry with no skill directory
Given: A skill name appears in root CLAUDE.md Relevant Skills table
When: No matching .claude/skills/<name>/ directory exists
Then: Report it as phantom

### Scenario: Detect SKILL.md exceeding 500 lines
Given: A .claude/skills/*/SKILL.md file exists
When: It contains more than 500 lines
Then: Report it as oversized

### Scenario: Detect missing phase tag
Given: A .claude/skills/*/SKILL.md file exists
When: Its description field does not contain [OPENING], [CLOSING], or [CONTEXT]
Then: Report it as missing phase tag

### Scenario: Clean state produces no warnings
Given: All skills are referenced, have directories, are under 500 lines, and have phase tags
When: skill_health.py runs
Then: Exit 0 and print a clean summary
