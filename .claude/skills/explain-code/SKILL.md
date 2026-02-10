---
name: explain-code
description: Explain code architecture, patterns, and design decisions with GAIA context
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

### Example 1: File-Level Explanation
```
/explain-code _MYCEL/rag_intelligence/core/retrieval.py
```

**Output:**
```
Retrieval Engine (MYCEL Core)
==============================

Purpose: Semantic search over embedded documents with reranking.

Key Functions:
1. retrieve(query, top_k) → Performs vector similarity search
2. rerank(candidates, query) → Scores candidates with cross-encoder
3. hybrid_search(query, alpha) → Combines semantic + keyword search

GAIA Integration:
- Uses ARGUS mental models for search strategy selection
- Stores results in MNEMIS (PROJECT tier) for cross-session caching
- Respects constitutional constraint: Read-only operations (no data modification)

Design Pattern: Strategy Pattern
- Allows swapping embedding models (OpenAI, Anthropic, local)
- Configurable reranking strategies

Performance: Optimized for <100ms retrieval on 10K docs
```

### Example 2: Component Architecture
```
/explain-code _VULCAN --architecture
```

**Output:**
```
VULCAN Architecture (The Forge)
================================

High-Level Flow:
User → HITL Questionnaire → Adapter Selection → Scaffold Generation → Registry Update

Components:
1. ui/main.py (Streamlit)
   ├─ Presents 7-step questionnaire
   └─ Collects project requirements

2. vulcan/questionnaire.py
   ├─ Question logic and validation
   └─ Maps answers to project type

3. vulcan/adapters/ (Strategy Pattern)
   ├─ hart_adapter.py (Deterministic projects)
   ├─ via_adapter.py (Creative/RAG projects)
   └─ forge_adapter.py (Processor projects)

4. vulcan/scaffolder.py
   ├─ Generates directory structure
   ├─ Populates templates (Jinja2)
   └─ Creates CLAUDE.md, README, tests

5. vulcan/integrations/registry_manager.py
   └─ Adds entry to GAIA registry.json

Constitutional Alignment:
✅ Glass-box: All generation steps inspectable
✅ HITL: User approves before scaffold creation
✅ Sovereignty: User can modify generated code freely

Three Pillars Position: VULCAN (Create) → LOOM (Edit) → ARGUS (Monitor)
```

### Example 3: Pattern Explanation
```
/explain-code _ARGUS/subconscious/pattern_detector.py --level expert
```

**Output:**
```
Pattern Detector (ARGUS Subconscious Layer)
============================================

Core Algorithm: Sliding Window + Mental Model Matching

1. Temporal Windowing
   - Analyzes events in 5-minute windows
   - Overlapping windows (50% overlap) for edge detection

2. Feature Extraction
   - Event types (file edits, tests, commits)
   - Frequency distributions
   - Sequential patterns (A → B → C)

3. Mental Model Selection
   - Queries ARGUS mental model library (59 models)
   - Selects models matching event characteristics
   - Applies model heuristics to detect patterns

4. Hypothesis Generation
   - Outputs DetectedPattern dataclass
   - Includes confidence score (0.0-1.0)
   - Suggests interventions (if applicable)

Constitutional Constraints:
- Read-only: Never modifies state
- Hypothesis-driven: Returns possibilities, not certainties
- Transparent: Includes reasoning in output

Performance Optimizations:
- Caches mental model selections (LRU cache, 100 entries)
- Debounces high-frequency events (max 10 events/sec)
- Async pattern detection (doesn't block main workflow)

Trade-offs:
- Chose sliding window over real-time stream processing
  Reason: Better pattern detection for bursty events
  Cost: 5-minute delay in pattern detection
- Chose local pattern detection over distributed
  Reason: GAIA is local-first architecture
  Cost: Cannot aggregate patterns across machines
```

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
