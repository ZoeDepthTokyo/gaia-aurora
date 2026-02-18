# Agent Types, Prompt Template, and Examples

## Agent Type Reference

| Agent Type | Use When |
|---|---|
| `Bash` | Git operations, CLI commands, system tasks |
| `general-purpose` | Multi-step tasks needing all tools |
| `build-error-resolver` | Build failures, test failures, import errors |
| `senior-python-ml-engineer` | Python implementation, ML pipelines |
| `code-reviewer` | Post-implementation quality review |
| `security-reviewer` | Security audit, vulnerability scan |
| `Explore` | Codebase search, architecture understanding |
| `Plan` | Design decisions, implementation strategy |

## Agent Prompt Template

When writing agent prompts, include:

```
You are on team "{team_name}", your name is "{agent_name}".

TASK: {clear description of what to do}

CONTEXT:
- Working directory: {path}
- Key files: {relevant files}
- Constraints: {any rules or limitations}

SUCCESS CRITERIA:
- {specific, verifiable outcome}

REPORT BACK:
- {what information to include in the response}
```

## Examples

### Cross-component investigation
```
/olympus Investigate why ARGUS dashboard shows stale data
```
Spawns: explorer (search codebase), dash-reader (read dashboard code), data-tracer (trace data pipeline)

### Multi-repo commit + push
```
/olympus Commit and push all dirty submodules
```
Spawns: one agent per dirty submodule (parallel), then root-committer (sequential)

### Feature implementation
```
/olympus Add cost tracking sidebar to SIM v2
```
Spawns: planner (design approach), then implementer + test-writer (parallel), then reviewer (sequential)
