# ARGUS Phase 2 Quick Start Guide

**Get up and running with ARGUS in 5 minutes**

---

## Installation

```bash
# Navigate to GAIA directory
cd X:\Projects\_gaia

# No installation needed - pure Python, no external dependencies (Phase 2.0)
```

---

## 1. Mental Models - Context-Aware Analysis

```python
from mental_models import MentalModelSelector

# Initialize selector
selector = MentalModelSelector()

# Describe your situation
context = "performance is degrading over time"

# Get recommended mental models
result = selector.select_for_context(context, max_models=3)

# Apply models
for model in result.models:
    print(f"Apply: {model.name}")
    print(f"  {model.description}")
    print(f"  When: {', '.join(model.when_to_use[:2])}")
```

**Output:**
```
Apply: Bottlenecks & Constraints
  Points in a system that limit overall throughput or performance
  When: performance degradation, resource exhaustion

Apply: Compounding
  Effects that accumulate and multiply over time
  When: long-term impact, technical debt

Apply: Rate of Change
  Speed at which something is changing, not just current value
  When: trend analysis, early warning
```

---

## 2. External Memory - Persistent Observations

```python
from argus.subconscious import ExternalMemory, MemoryEntry, MemoryType, MemoryScope

# Initialize memory
memory = ExternalMemory("X:/Projects/_gaia/argus/memory.db")

# Store observation
entry = MemoryEntry(
    type=MemoryType.OBSERVATION,
    scope=MemoryScope.PROJECT,
    content="HART OS confidence declining: 0.85 → 0.78",
    source="hart_os",
    confidence=0.9,
    tags=["hart_os", "performance"]
)

memory.store(entry)

# Search memory
results = memory.search(
    query="confidence",
    type=MemoryType.OBSERVATION,
    limit=10
)

for result in results:
    print(f"{result.timestamp}: {result.content}")
```

---

## 3. Pattern Detection - Automatic Analysis

```python
from argus.subconscious import PatternDetector

# Initialize detector
detector = PatternDetector(memory)

# Detect patterns in last 30 days
patterns = detector.detect_patterns(
    lookback_days=30,
    min_frequency=3,
    min_confidence=0.6
)

# Review patterns
for pattern in patterns:
    print(f"{pattern.type.value}: {pattern.description}")
    print(f"  Confidence: {pattern.confidence:.0%}")
    print(f"  Actions: {', '.join(pattern.recommended_actions)}")
```

**Output:**
```
performance_degradation: Performance degradation detected over time
  Confidence: 75%
  Actions: Profile system performance, Identify bottlenecks, Review recent changes
```

---

## 4. Hypothesis Generation - Testable Explanations

```python
from argus.subconscious import HypothesisGenerator

# Initialize generator
generator = HypothesisGenerator()

# Generate hypotheses from pattern
hypotheses = generator.generate_from_pattern(patterns[0])

# Review hypotheses
for hyp in hypotheses:
    print(f"Hypothesis: {hyp.description}")
    print(f"  Test: {hyp.proposed_test}")
    print(f"  Confidence: {hyp.confidence:.0%}")
```

**Output:**
```
Hypothesis: Performance degradation due to accumulating technical debt
  Test: Profile system and identify bottlenecks
  Confidence: 53%

Hypothesis: Specific component LLM API calls is bottleneck
  Test: Measure latency by component
  Confidence: 45%
```

---

## 5. Context Enrichment - Automatic Context Loading

```python
from argus.subconscious import ContextEnricher

# Initialize enricher
enricher = ContextEnricher(memory)

# Enrich context for new observation
context = enricher.enrich_for_observation(
    observation="HART OS Stage 3 failing",
    project="hart_os",
    lookback_days=30
)

# Review enriched context
print(f"Related patterns: {len(context['related_patterns'])}")
print(f"Related errors: {len(context['related_errors'])}")
print(f"Trend: {context['temporal_context']['trend']}")
```

**Output:**
```
Related patterns: 2
Related errors: 5
Trend: increasing
```

---

## 6. Layered Explainability - User-Adapted Explanations

```python
from argus.explainability import Explainer, ExplanationLevel

# Initialize explainer
explainer = Explainer()

# Explain at beginner level
simple = explainer.explain("feedback_loops", ExplanationLevel.SIMPLE)
print(simple.content)

# Explain at expert level
advanced = explainer.explain("feedback_loops", ExplanationLevel.ADVANCED)
print(advanced.content[:200])
```

**Output:**
```
Simple:
A feedback loop is when the output of a process feeds back as input, creating a cycle.

Advanced:
Feedback loops in control systems theory are characterized by:

Transfer Function: H(s) = G(s) / (1 + G(s)H(s))

Where G(s) is forward path gain and H(s) is feedback path gain...
```

---

## Complete Example - All Components Together

```python
import sys
from pathlib import Path
sys.path.insert(0, "X:/Projects/_gaia")

from argus.subconscious import (
    ExternalMemory, MemoryEntry, MemoryType, MemoryScope,
    PatternDetector, HypothesisGenerator, ContextEnricher
)
from mental_models import MentalModelSelector
from argus.explainability import Explainer, ExplanationLevel

# 1. Initialize
memory = ExternalMemory("memory.db")
detector = PatternDetector(memory)
generator = HypothesisGenerator()
enricher = ContextEnricher(memory)
selector = MentalModelSelector()
explainer = Explainer()

# 2. Store observation
entry = MemoryEntry(
    type=MemoryType.OBSERVATION,
    scope=MemoryScope.PROJECT,
    content="Performance degrading: response time increased 40%",
    source="my_project",
    confidence=0.9,
    tags=["performance", "degradation"]
)
memory.store(entry)

# 3. Detect patterns
patterns = detector.detect_patterns(lookback_days=7, min_frequency=2)
print(f"Detected {len(patterns)} patterns")

# 4. Generate hypotheses
if patterns:
    hypotheses = generator.generate_from_pattern(patterns[0])
    print(f"Generated {len(hypotheses)} hypotheses")

# 5. Enrich context
context = enricher.enrich_for_observation(
    "Performance issues detected",
    lookback_days=7
)
print(f"Context enriched with {len(context['related_observations'])} observations")

# 6. Select mental models
result = selector.select_for_context("performance degradation", max_models=3)
print(f"Selected models: {[m.name for m in result.models]}")

# 7. Get explanation
explanation = explainer.explain("feedback_loops", ExplanationLevel.DEFAULT)
print(f"Explanation: {explanation.content[:100]}...")

# Cleanup
memory.close()
```

---

## Common Patterns

### Pattern 1: Store and Analyze

```python
# Store observations over time
for observation in daily_observations:
    memory.store(MemoryEntry(
        type=MemoryType.OBSERVATION,
        scope=MemoryScope.PROJECT,
        content=observation,
        source="my_project"
    ))

# Detect patterns weekly
patterns = detector.detect_patterns(lookback_days=7)
```

### Pattern 2: Investigate Issue

```python
# 1. Enrich context
context = enricher.enrich_for_observation(
    "Users reporting errors",
    project="my_project"
)

# 2. Select analytical frameworks
models = selector.select_for_context(context['observation'])

# 3. Generate hypotheses
if context['related_patterns']:
    hypotheses = generator.generate_from_pattern(
        context['related_patterns'][0]
    )
```

### Pattern 3: Learn from History

```python
# Search past similar issues
past_errors = memory.search(
    query="error",
    type=MemoryType.ERROR,
    limit=10
)

# Find what worked before
past_successes = memory.search(
    type=MemoryType.SUCCESS,
    tags=["error_resolution"],
    limit=5
)
```

---

## Tips & Best Practices

### 1. Memory Organization

- Use **tags** liberally for easy retrieval
- Set **confidence** scores honestly (don't default to 1.0)
- Use appropriate **scope** (AGENT for temp, PROJECT for persistent)
- Include **context** dict for structured data

### 2. Pattern Detection

- Run weekly, not real-time (avoid noise)
- Set `min_frequency` to at least 3
- Set `min_confidence` to 0.6+ for actionable patterns
- Review `severity` to prioritize

### 3. Mental Models

- Let selector choose (don't manually pick)
- Use `combination_patterns` for complex analysis
- Check `confidence` before applying
- Apply 1-2 models first, add more if needed

### 4. Explainability

- Map to user's growth rung:
  - Rung 1 (Beginner) → SIMPLE
  - Rung 2-3 (Learning) → METAPHOR/DEFAULT
  - Rung 4-5 (Expert) → ADVANCED
- Use `explain_for_user()` for automatic level selection

---

## Troubleshooting

### "No patterns detected"

- Check `min_frequency` (default 3) - reduce if needed
- Check `lookback_days` - may need longer window
- Verify memory has enough observations (at least 5-10)

### "Low confidence selections"

- Context may be too vague - be more specific
- Try different keywords
- Check invocation_rules.json for trigger keywords

### "Memory database locked"

- Close previous memory connections: `memory.close()`
- Only one connection per process for SQLite

---

## Next Steps

1. **Run the integration example:**
   ```bash
   python examples/argus_integration_example.py
   ```

2. **Read full documentation:**
   - `argus/README.md` - Complete guide
   - `mental_models/README.md` - Mental models reference

3. **Integrate with your project:**
   - Add memory storage to your telemetry
   - Run pattern detection weekly
   - Use mental models in decision-making

4. **Contribute:**
   - Add new mental model explanations
   - Extend pattern detection
   - Share your combination patterns

---

## Support

- Documentation: `X:\Projects\_gaia\argus\README.md`
- Examples: `X:\Projects\_gaia\examples\`
- Issues: Track in GAIA ecosystem

---

**Quick Start Version:** 1.0.0
**Last Updated:** February 4, 2026
