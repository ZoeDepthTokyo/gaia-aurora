# ARGUS - The Watchman (Phase 2)

**Status:** Phase 2 Implementation In Progress
**Version:** 0.5.0 (Pre-release)
**Last Updated:** February 4, 2026

---

## Executive Summary

ARGUS is GAIA's monitoring and sense-making layer. Phase 2 implementation focuses on:

1. **Mental Models Library** (59 models across 7 categories)
2. **Subconscious Layer** (external memory, pattern detection, hypothesis generation)
3. **Layered Explainability** (4-level explanation system)
4. **Process Observer** (non-intervening sense-making agent)
5. **Trust Dashboard** (transparency metrics)

**Core Principle:** Glass-box observability with reflective cognition (observe → propose → never execute)

---

## Directory Structure

```
X:\Projects\_gaia\
├── mental_models/                    # Mental models library
│   ├── __init__.py                   # Package initialization
│   ├── models.py                     # Core data structures
│   ├── selector.py                   # Context-aware selection
│   ├── registry.json                 # 59 mental models catalog
│   └── invocation_rules.json         # Selection rules
│
├── argus/
│   ├── subconscious/                 # Subconscious layer
│   │   ├── __init__.py
│   │   ├── memory.py                 # External memory (SQLite)
│   │   ├── pattern_detector.py       # Background pattern detection
│   │   ├── hypothesis_generator.py   # Hypothesis generation
│   │   └── context_enricher.py       # Context pre-loading
│   │
│   ├── explainability/               # Layered explainability
│   │   ├── __init__.py
│   │   └── explainer.py              # 4-level explanation system
│   │
│   ├── process_observer/             # Process Observer agent
│   │   ├── __init__.py
│   │   ├── observer.py               # Main observer (TBD)
│   │   └── post_mortem.py            # Post-mortem analysis (TBD)
│   │
│   ├── trust_dashboard/              # Trust metrics
│   │   └── (TBD)
│   │
│   └── README.md                     # This file
```

---

## Component 1: Mental Models Library

### Overview

59 mental models across 7 categories provide structured analytical frameworks.

### Categories

1. **Systems Thinking** (8 models)
   - Feedback loops, Emergence, Bottlenecks, Leverage points, System boundaries, Stocks & flows, Resilience, Second-order effects

2. **Decision Making** (8 models)
   - First principles, Inversion, Opportunity cost, Reversibility, Margin of safety, Pareto principle, Occam's razor, Regret minimization

3. **Cognitive Biases** (7 models)
   - Confirmation bias, Availability heuristic, Anchoring, Sunk cost fallacy, Survivorship bias, Dunning-Kruger, Planning fallacy

4. **Learning & Pedagogy** (8 models)
   - Scaffolding, Zone of proximal development, Spaced repetition, Deliberate practice, Worked examples, Cognitive load theory, Transfer of learning, Metacognition

5. **Quality & Reliability** (8 models)
   - Defense in depth, Fail fast, Graceful degradation, Idempotency, Blast radius, Observability, Poka-yoke, Circuit breaker

6. **Communication** (6 models)
   - Curse of knowledge, Progressive disclosure, Signal to noise, Shared mental models, Principle of least surprise, Empathy mapping

7. **Temporal** (6 models)
   - Compounding, Half-life, Critical path, Lead vs lag indicators, Rate of change, Hysteresis

### Usage

```python
from mental_models import MentalModelSelector, get_model

# Context-aware selection
selector = MentalModelSelector()
result = selector.select_for_context("performance degradation detected")

for model in result.models:
    print(f"{model.name}: {model.description}")
    print(f"When to use: {', '.join(model.when_to_use)}")

# Direct model access
feedback_loops = get_model("feedback_loops")
print(f"Confidence threshold: {feedback_loops.confidence_threshold}")

# Combination patterns
trust_audit_models = selector.get_combination_pattern("trust_audit")
# Returns: [defense_in_depth, graceful_degradation, observability, ...]
```

### Invocation Rules

Mental models are selected based on:
- Context patterns (12 patterns defined)
- Trigger keywords
- Confidence thresholds
- Combination patterns for complex analysis

See `mental_models/invocation_rules.json` for full specification.

---

## Component 2: Subconscious Layer

### Overview

The subconscious layer operates transparently in the background, enriching GAIA's analytical capabilities without intervening in execution.

### 2.1 External Memory (SQLite)

Persistent storage for observations, patterns, hypotheses, decisions, and outcomes.

```python
from argus.subconscious import ExternalMemory, MemoryEntry, MemoryType, MemoryScope

# Initialize memory
memory = ExternalMemory("X:/Projects/_gaia/argus/memory.db")

# Store observation
entry = MemoryEntry(
    type=MemoryType.OBSERVATION,
    scope=MemoryScope.PROJECT,
    content="HART OS confidence scores declining over 30 days",
    source="process_observer",
    confidence=0.85,
    tags=["hart_os", "confidence", "performance"]
)

memory.store(entry)

# Search memory
results = memory.search(
    query="confidence",
    type=MemoryType.OBSERVATION,
    min_confidence=0.7,
    limit=10
)

# Get recent memories
recent = memory.get_recent(limit=50, type=MemoryType.ERROR)
```

**Memory Types:**
- OBSERVATION: Observable facts
- PATTERN: Detected patterns
- HYPOTHESIS: Generated hypotheses
- DECISION: Decisions made
- OUTCOME: Results of actions
- ERROR: Errors or failures
- SUCCESS: Successful operations

**Memory Scopes:**
- GAIA: Ecosystem-wide (requires user approval)
- PROJECT: Project-specific (persistent)
- AGENT: Agent-specific (ephemeral, auto-expires after 30 days)

### 2.2 Pattern Detector

Background pattern detection in memory/telemetry.

```python
from argus.subconscious import PatternDetector

detector = PatternDetector(memory)

# Detect patterns in recent history
patterns = detector.detect_patterns(
    lookback_days=30,
    min_frequency=3,
    min_confidence=0.6
)

for pattern in patterns:
    print(f"{pattern.type}: {pattern.description}")
    print(f"Confidence: {pattern.confidence:.0%}")
    print(f"Severity: {pattern.severity:.0%}")
    print(f"Recommended actions: {', '.join(pattern.recommended_actions)}")
```

**Pattern Types:**
- RECURRING_ERROR
- PERFORMANCE_DEGRADATION
- COST_SPIKE
- USAGE_PATTERN
- CONFIDENCE_DRIFT
- ANTI_PATTERN
- SUCCESS_PATTERN
- CORRELATION

### 2.3 Hypothesis Generator

Generates testable hypotheses from detected patterns.

```python
from argus.subconscious import HypothesisGenerator

generator = HypothesisGenerator()

# Generate from pattern
hypotheses = generator.generate_from_pattern(pattern)

for hyp in hypotheses:
    print(f"Hypothesis: {hyp.description}")
    print(f"Confidence: {hyp.confidence:.0%}")
    print(f"Test: {hyp.proposed_test}")
    print(f"Implications: {', '.join(hyp.implications)}")

# Refine with new evidence
refined = generator.refine_hypothesis(
    hyp,
    new_evidence_for=["memory_id_1", "memory_id_2"],
    new_evidence_against=["memory_id_3"]
)
```

**Hypothesis Status:**
- PENDING: Generated, not yet tested
- TESTING: Currently being tested
- CONFIRMED: Evidence supports hypothesis
- REJECTED: Evidence contradicts hypothesis
- INCONCLUSIVE: Insufficient evidence

### 2.4 Context Enricher

Pre-loads relevant context from external memory.

```python
from argus.subconscious import ContextEnricher

enricher = ContextEnricher(memory)

# Enrich context for new observation
context = enricher.enrich_for_observation(
    observation="HART OS confidence scores declining",
    project="hart_os",
    lookback_days=30
)

print(f"Related patterns: {len(context['related_patterns'])}")
print(f"Related errors: {len(context['related_errors'])}")
print(f"Temporal trend: {context['temporal_context']['trend']}")

# Enrich for decision-making
decision_context = enricher.enrich_for_decision(
    decision_context="Should we refactor Stage 3?",
    project="hart_os"
)

print(f"Past decisions: {len(decision_context['past_decisions'])}")
print(f"Success rate: {decision_context['success_rate']:.0%}")
```

---

## Component 3: Layered Explainability

### Overview

4-level explanation system adapting to user's growth ladder position.

### Explanation Levels

1. **SIMPLE**: One sentence, no jargon (Growth Rung 1: Creator)
2. **METAPHOR**: Uses analogies and comparisons (Growth Rung 2: Explorer)
3. **DEFAULT**: Balanced explanation with key points (Growth Rung 3: Adapter)
4. **ADVANCED**: Deep technical details with references (Growth Rung 4-5: Architect/Mentor)

### Usage

```python
from argus.explainability import Explainer, ExplanationLevel

explainer = Explainer()

# Explain at specific level
simple = explainer.explain("feedback_loops", ExplanationLevel.SIMPLE)
print(simple.content)
# "A feedback loop is when the output of a process feeds back as input, creating a cycle."

advanced = explainer.explain("feedback_loops", ExplanationLevel.ADVANCED)
print(advanced.content)
# Includes transfer functions, code examples, references

# Auto-select level based on user's growth rung
explanation = explainer.explain_for_user("feedback_loops", growth_rung=3)

# Format as markdown
markdown = explanation.format_markdown()

# Add custom explanation
explainer.add_custom_explanation(
    topic="custom_adapter",
    level=ExplanationLevel.DEFAULT,
    content="Custom adapters extend BaseAdapter...",
    examples=["DeterministicAdapter", "CreativeAdapter"],
    next_steps=["Read adapter interface", "Review existing adapters"]
)
```

### Available Topics

- `feedback_loops`
- `mental_models`
- (More topics to be added)

---

## Component 4: Process Observer (TBD)

### Overview

Non-intervening sense-making agent with read-only access to ecosystem state.

### Constitutional Constraints

1. **Read-only**: Cannot execute tools or modify code
2. **Memory boundaries**: Cannot write above AGENT tier without proposal
3. **Non-intervening**: Produces hypotheses, not actions
4. **Transparent**: Must explain reasoning for all observations
5. **Hypothesis-driven**: Proposes possibilities, never certainties

### Planned Capabilities

- Ecosystem-wide pattern detection
- Cross-project anti-pattern surfacing
- Structural regression identification
- Post-mortem synthesis
- Trust metric computation

---

## Component 5: Trust Dashboard (TBD)

### Overview

Monitors trust principles across ecosystem.

### Trust Metrics

1. **Transparency Score**: Percentage of decisions with explicit reasoning
2. **Graceful Degradation Score**: Percentage of failures that degraded gracefully
3. **Learning Explicitness Score**: Ratio of confirmed learning vs inferred patterns
4. **Inspectability Score**: Percentage of execution traces with complete provenance

### Planned Features

- Real-time trust scoring per project
- Trust trend analysis
- Trust violation alerts
- Audit trail export

---

## Integration with GAIA Ecosystem

### Phase 1 → Phase 2 Handoff

ARGUS relies on VULCAN guarantees:
- `X:\Projects\_gaia\registry.json` - All registered projects
- `X:\Projects\{project}\logs\*.jsonl` - Telemetry data
- `X:\Projects\{project}\CLAUDE.md` - Project context
- `X:\Projects\{project}\config.py` - Configuration

### Constitutional Alignment

ARGUS operates under GAIA's 5 Trust Principles:
1. GAIA Never Lies (explicit uncertainty)
2. GAIA Admits Limits (read-only boundaries)
3. GAIA Degrades Gracefully (failure visibility)
4. GAIA Learns Explicitly (proposal-based learning)
5. GAIA Remains Inspectable (decision trails)

### Authority Graph Position

```
GAIA (constitutional) → Project Agent (accountable) → Execution Agents (task-bounded)
                     ↓
                  Process Observer (non-intervening, sense-making)
                     ↓
                  ARGUS (observer only, never actor)
```

---

## Development Status

### ✅ Completed (Phase 2 In Progress)

- [x] Mental Models Library (59 models)
- [x] Mental Model Registry (JSON)
- [x] Mental Model Invocation Rules (JSON)
- [x] Mental Model Selector (Python)
- [x] External Memory System (SQLite)
- [x] Pattern Detector
- [x] Hypothesis Generator
- [x] Context Enricher
- [x] Layered Explainability (4 levels)
- [x] Explanation templates for core concepts

### 📋 In Progress

- [ ] Process Observer implementation
- [ ] Post-mortem analyzer
- [ ] Trust Dashboard
- [ ] Integration with HART OS telemetry
- [ ] Integration with VIA telemetry
- [ ] WARDEN v0 governance script
- [ ] Unit tests (target 80%+ coverage)
- [ ] Integration examples

### 📋 Planned (Future Phases)

- [ ] ChromaDB semantic search (Phase 2.1)
- [ ] Real-time dashboard UI (Streamlit)
- [ ] Cross-project pattern detection
- [ ] Predictive suggestions (per PREDICTIVE_GAIA_SPEC.md)
- [ ] Mental model learning system

---

## Usage Examples

### Example 1: Detect and Explain Pattern

```python
from argus.subconscious import ExternalMemory, PatternDetector, HypothesisGenerator
from argus.explainability import Explainer, ExplanationLevel
from mental_models import MentalModelSelector

# Initialize components
memory = ExternalMemory("memory.db")
detector = PatternDetector(memory)
generator = HypothesisGenerator()
explainer = Explainer()
selector = MentalModelSelector()

# Detect patterns
patterns = detector.detect_patterns(lookback_days=30)

for pattern in patterns:
    # Generate hypotheses
    hypotheses = generator.generate_from_pattern(pattern)

    # Select appropriate mental models
    models = selector.select_for_context(pattern.description)

    # Explain pattern at user's level
    explanation = explainer.explain_for_user(
        topic="feedback_loops",  # Based on pattern type
        growth_rung=3
    )

    print(f"Pattern: {pattern.description}")
    print(f"Mental models: {[m.name for m in models.models]}")
    print(f"\nExplanation:\n{explanation.content}")
    print(f"\nHypotheses:")
    for hyp in hypotheses:
        print(f"- {hyp.description}")
        print(f"  Test: {hyp.proposed_test}")
```

### Example 2: Context-Enriched Analysis

```python
from argus.subconscious import ExternalMemory, ContextEnricher

memory = ExternalMemory("memory.db")
enricher = ContextEnricher(memory)

# New observation arrives
observation = "HART OS Stage 3 confidence scores: 0.85 → 0.78 over 30 days"

# Enrich context
context = enricher.enrich_for_observation(
    observation=observation,
    project="hart_os",
    lookback_days=30
)

# Context now includes:
# - Related historical observations
# - Detected patterns matching keywords
# - Related errors and successes
# - Temporal trend analysis
# - Project health metrics

print(f"Temporal trend: {context['temporal_context']['trend']}")
print(f"Related patterns: {len(context['related_patterns'])}")
print(f"Project health: {context['project_context']['health_score']:.0%}")
```

---

## Testing

### Unit Tests

```bash
# Run all tests
pytest tests/

# Run specific component
pytest tests/test_mental_models.py
pytest tests/test_subconscious.py
pytest tests/test_explainability.py

# With coverage
pytest --cov=mental_models --cov=argus tests/
```

### Test Data

Test data fixtures are in `tests/fixtures/`:
- Sample memory database
- Test patterns
- Test hypotheses
- Explanation templates

---

## Performance Considerations

### Memory Database

- SQLite for structured queries
- Indexed on: type, scope, timestamp, source
- Auto-cleanup of AGENT-scoped memories (30-day TTL)
- Typical query latency: <10ms for recent searches

### Pattern Detection

- Runs asynchronously in background
- Configurable lookback window (default 30 days)
- Minimum frequency threshold prevents noise (default 3)
- Confidence filtering reduces false positives

### Context Enrichment

- Keyword-based retrieval (O(log n) with indexes)
- Result limit prevents memory exhaustion
- Deduplication prevents redundant processing

---

## Security & Privacy

### Data Storage

- All telemetry stored locally (no external transmission)
- SQLite database permissions: user-only read/write
- No API keys or secrets in memory database
- Automatic cleanup of ephemeral data

### Access Control

- Process Observer: read-only access enforced
- Memory tier boundaries enforced programmatically
- Promotion to GAIA tier requires user approval
- Audit trail for all memory promotions

---

## Roadmap

### v0.5.0 (Phase 2 Complete)

- [ ] Process Observer operational
- [ ] Trust Dashboard MVP
- [ ] WARDEN v0 integration
- [ ] Full test suite (80%+ coverage)
- [ ] Documentation complete

### v0.6.0 (Phase 2.1)

- [ ] ChromaDB semantic search
- [ ] Advanced pattern detection (statistical correlation)
- [ ] Real-time dashboard UI
- [ ] Cross-project analysis

### v1.0.0 (Phase 3)

- [ ] LOOM integration
- [ ] MNEMIS cross-project memory
- [ ] Predictive suggestions
- [ ] Full ecosystem monitoring

---

## References

- `X:\Projects\_gaia\GAIA_BIBLE.md` - Constitutional foundation
- `X:\Projects\_gaia\SR_COUNCIL_ANALYSIS.md` - Runtime governance
- `X:\Projects\_gaia\PREDICTIVE_GAIA_SPEC.md` - Predictive capability
- `X:\Projects\_gaia\COUNCIL_COMPETITIVE_ANALYSIS.md` - Strategic positioning
- `X:\Projects\_gaia\VERSION_LOG.md` - Version history

---

**Maintained by:** GAIA Constitutional Team
**Status:** Phase 2 Active Development
**Last Updated:** February 4, 2026
