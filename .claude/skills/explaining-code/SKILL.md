---
name: explaining-code
description: "[CONTEXT] Explains GAIA ecosystem code with architectural reasoning, constitutional compliance notes, and design decision context. Use when onboarding to a component, reviewing unfamiliar code, debugging errors, or understanding why a pattern was chosen. Supports simple, detailed, and expert levels. Triggers on: explain, how does this work, what is this, walk me through, debug, error. Why: accelerates onboarding and debugging with architecture context."
disable-model-invocation: false
---

# Explain Code

Provides clear, context-aware explanations of GAIA ecosystem code with architectural reasoning and constitutional compliance notes.

## Usage
```
/explain-code <file_path> [--level simple|detailed|expert]
/explain-code <component_name> [--architecture]
```

## Explanation Levels

### Simple (Default)
- What the code does (1-2 sentences)
- Key inputs and outputs
- Where it fits in GAIA ecosystem

### Detailed
- Line-by-line walkthrough
- Design patterns used
- Integration points with other components
- Constitutional constraints honored

### Expert
- Architectural trade-offs
- Performance considerations
- Scalability implications
- Alternative approaches considered
- Error-handling analysis: exception paths, recovery strategies, failure modes

## Debug Mode

```
/explain-code <file_path> --debug
```

When `--debug` is specified:
1. Focus on error paths and exception handling
2. Identify missing try/except blocks around I/O, network, and file operations
3. Trace error propagation through call chains
4. Flag silent error swallowing (bare `except: pass`)
5. Suggest defensive patterns for uncovered failure modes

## Process

1. **Context Gathering**
   - Identify component (_ARGUS, _MYCEL, etc.)
   - Read CLAUDE.md for component role
   - Check imports for dependencies

2. **Code Analysis**
   - Parse structure (classes, functions, modules)
   - Identify patterns (adapters, bridges, observers)
   - Map to GAIA constitutional principles

3. **Explanation Generation**
   - Start with high-level purpose
   - Break down key sections
   - Highlight GAIA-specific patterns
   - Note integration points

4. **Visual Aids** (when helpful)
   - Flow diagrams for workflows
   - Dependency trees
   - Sequence diagrams for interactions

## Examples

Three output formats demonstrated in references/examples.md:
- File-level: `_MYCEL/rag_intelligence/core/retrieval.py` (simple level)
- Architecture: `_VULCAN --architecture` (component flow)
- Expert: `_ARGUS/subconscious/pattern_detector.py --level expert` (trade-offs + perf)

## GAIA-Specific Explanations

### Constitutional Principles
Always notes which principles the code honors:
- Glass-box transparency
- Human-in-the-loop
- Progressive trust
- Sovereignty
- Memory tier boundaries

### Integration Points
Highlights connections to:
- MYCEL (LLM access)
- MNEMIS (memory storage)
- ARGUS (telemetry)
- WARDEN (governance)

### Design Patterns
Common GAIA patterns explained:
- Bridge pattern (MYCEL/ARGUS/MNEMIS bridges)
- Adapter pattern (VULCAN project types)
- Observer pattern (ARGUS monitoring)
- Strategy pattern (mental model selection)

## Output Formats

**Markdown** (default): Human-readable
**Mermaid Diagrams**: For visualizations
**JSON**: For automation/tooling
