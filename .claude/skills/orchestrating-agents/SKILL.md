---
name: orchestrating-agents
description: "[CONTEXT] Decomposes complex tasks into parallelizable subtasks, spawns specialized agent teams with full permissions, and coordinates their work via task lists. Use for multi-file changes, cross-component investigations, or any task benefiting from concurrent agent execution. Triggers on: spawn agents, multi-agent, team, parallel, decompose, coordinate. Why: enables parallel execution of complex multi-component tasks."
---

# /olympus — GAIA Agent Team Orchestrator

## Usage
```
/olympus <task description> [--agents <count>] [--bg]
```

**Flags:**
- `--agents <N>`: Override auto-detected agent count (default: auto)
- `--bg`: Run all agents in background, report when done

## Description

Olympus decomposes a complex task into parallelizable subtasks, spawns a team of specialized agents with full permissions, tracks progress via the task list, and delivers a consolidated result. It handles the full lifecycle: plan, spawn, monitor, learn, shutdown.

Use when: multi-file changes, cross-component work, investigations requiring parallel exploration, any task that benefits from concurrent agent execution.

## Workflow

### Step 0: When to Decompose (Decision Tree)

Before spawning agents, answer these 5 questions in order:

1. **Does the task touch 3+ files in different components?**
   - YES -> Decompose. Agents work on independent components in parallel.
   - NO -> Continue to Q2.

2. **Does the task require 2+ distinct skill types (research + coding, testing + writing)?**
   - YES -> Decompose. Match agents to skill types.
   - NO -> Continue to Q3.

3. **Would a single agent take 10+ minutes on this?**
   - YES -> Decompose if subtasks are independent. Split by file/module boundaries.
   - NO -> Continue to Q4.

4. **Does the task involve exploring unknown territory (research, investigation)?**
   - YES -> Decompose into scout + analyst agents.
   - NO -> Continue to Q5.

5. **Is the task a simple, linear sequence?**
   - YES -> Do NOT decompose. Single agent is more efficient.
   - NO -> Decompose if you can identify parallel work streams.

If you answered NO to all: execute the task directly without agent orchestration.

### Step 1: DECOMPOSE the Task

Analyze the user's request and break it into independent subtasks:

1. **Parse the intent** — What is the user trying to achieve?
2. **Identify parallelism** — Which subtasks have no dependencies on each other?
3. **Identify sequencing** — Which subtasks must wait for others?
4. **Choose agent types** — Match each subtask to the best `subagent_type`. For the full agent type table, see references/agent-types.md.

### Step 2: CREATE Team + Tasks

```
1. TeamCreate with descriptive team_name
2. TaskCreate for each subtask with:
   - subject: imperative verb phrase ("Fix auth bug in login")
   - description: full context an agent needs to work independently
   - activeForm: present continuous ("Fixing auth bug")
3. TaskUpdate to set dependencies (addBlockedBy) for sequential tasks
```

### Step 3: SPAWN Agents

For each independent subtask, spawn a teammate:

```
Task tool with:
  - subagent_type: matched to subtask type
  - mode: "bypassPermissions"
  - team_name: the team name from Step 2
  - name: short descriptive name (e.g., "auth-fixer", "test-runner")
  - prompt: Include:
    1. Team name and agent name
    2. Full task context (don't assume agents know anything)
    3. Success criteria
    4. What to report back
```

**Rules:**
- Launch ALL independent agents in a SINGLE message (parallel tool calls)
- Use `run_in_background: true` for long-running agents when you need to continue working
- Grant `mode: "bypassPermissions"` — agents get full Bash, Edit, Read, Glob, Grep, Write access
- Each agent gets WebSearch + WebFetch for any URL research needed

### Step 4: MONITOR + COORDINATE

As agents report back:
1. Mark their tasks completed via `TaskUpdate`
2. Check if blocked tasks are now unblocked
3. Spawn next-wave agents for newly unblocked tasks
4. If an agent fails, assess whether to:
   - Retry with adjusted instructions
   - Reassign to a different agent type
   - Escalate to user

### Step 5: LEARN + IMPROVE

After all agents complete:
1. **Consolidate results** — Merge findings from all agents into a coherent summary
2. **Detect patterns** — If recurring issues found, note them
3. **Update memory** — If a reusable lesson was learned, write to `MEMORY.md` or topic file in `~/.claude/projects/X--projects--GAIA/memory/`
4. **Quality gate** — If code was written, consider spawning a `code-reviewer` agent

### Step 6: SHUTDOWN + CLEANUP

1. Send `shutdown_request` to ALL idle teammates
2. Wait for shutdown confirmations
3. `TeamDelete` to clean up team + task files
4. Report final summary to user with:
   - What was accomplished
   - What was learned
   - Any remaining follow-ups

## Status Line

Throughout execution, keep the user informed via task status:
- Pending tasks show what's queued
- In-progress tasks show what's active (with `activeForm` spinners)
- Completed tasks show progress

## Agent Prompt Template and Examples

For the full agent prompt template and concrete spawn examples, see references/agent-types.md.

## Guardrails

- **Max agents**: 6 concurrent (prevents resource exhaustion)
- **Timeout awareness**: If an agent hasn't reported in 5 minutes, check its output file
- **No orphans**: Always shut down agents when done — never leave teammates running
- **Error escalation**: If 2+ agents fail on the same issue, stop and ask the user
- **Memory hygiene**: Only write to memory files when a lesson is confirmed across multiple interactions
