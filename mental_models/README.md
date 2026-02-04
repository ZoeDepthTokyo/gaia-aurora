# Mental Models Library

**Version:** 1.0.0
**Status:** Operational
**Last Updated:** February 4, 2026

---

## Overview

The Mental Models Library provides 59 structured analytical frameworks across 7 categories for consistent, auditable reasoning in the GAIA ecosystem.

**Core Principle:** Make thinking explicit, structured, and inspectable.

---

## Quick Start

```python
from mental_models import MentalModelSelector, get_model

# Context-aware selection
selector = MentalModelSelector()
result = selector.select_for_context("performance degradation detected")

for model in result.models:
    print(f"{model.name}: {model.description}")

# Direct model access
model = get_model("feedback_loops")
print(f"Apply when: {', '.join(model.when_to_use)}")
```

---

## Categories & Models

### Systems Thinking (8 models)

Understanding complex systems and their emergent behaviors.

| Model | ID | When to Use |
|-------|-----|------------|
| Feedback Loops | `feedback_loops` | Circular dependencies, self-reinforcing patterns |
| Emergence | `emergence` | Unexpected behaviors from component interactions |
| Bottlenecks & Constraints | `bottlenecks` | Performance limits, resource exhaustion |
| Leverage Points | `leverage_points` | High-impact optimization opportunities |
| System Boundaries | `system_boundaries` | Scope definition, authority limits |
| Stocks and Flows | `stocks_and_flows` | Resource tracking, accumulation |
| Resilience & Antifragility | `resilience` | Failure recovery, stress testing |
| Second-Order Effects | `second_order_effects` | Indirect consequences, downstream impacts |

### Decision Making (8 models)

Structured frameworks for making choices under uncertainty.

| Model | ID | When to Use |
|-------|-----|------------|
| First Principles Thinking | `first_principles` | Fundamental redesign, root cause analysis |
| Inversion | `inversion` | Risk analysis, failure mode detection |
| Opportunity Cost | `opportunity_cost` | Prioritization, resource allocation |
| Reversibility | `reversibility` | Architectural choices, experimental features |
| Margin of Safety | `margin_of_safety` | Capacity planning, error budgets |
| Pareto Principle (80/20) | `pareto_principle` | Optimization focus, high-impact identification |
| Occam's Razor | `occams_razor` | Simplification, debugging hypotheses |
| Regret Minimization | `regret_minimization` | Long-term decisions, irreversible choices |

### Cognitive Biases (7 models)

Awareness and mitigation of systematic thinking errors.

| Model | ID | When to Use |
|-------|-----|------------|
| Confirmation Bias | `confirmation_bias` | Pattern validation, hypothesis testing |
| Availability Heuristic | `availability_heuristic` | Risk assessment, recency bias checks |
| Anchoring | `anchoring` | Baseline setting, comparative analysis |
| Sunk Cost Fallacy | `sunk_cost_fallacy` | Refactor decisions, feature deprecation |
| Survivorship Bias | `survivorship_bias` | Success analysis, pattern detection |
| Dunning-Kruger Effect | `dunning_kruger` | Confidence calibration, expertise assessment |
| Planning Fallacy | `planning_fallacy` | Estimation, timeline planning |

### Learning & Pedagogy (8 models)

Frameworks for effective knowledge transfer and skill development.

| Model | ID | When to Use |
|-------|-----|------------|
| Scaffolding | `scaffolding` | User onboarding, progressive disclosure |
| Zone of Proximal Development | `zone_of_proximal_development` | Tutorial design, challenge calibration |
| Spaced Repetition | `spaced_repetition` | Concept reinforcement, skill retention |
| Deliberate Practice | `deliberate_practice` | Skill development, expertise building |
| Worked Examples | `worked_examples` | Teaching patterns, best practice sharing |
| Cognitive Load Theory | `cognitive_load_theory` | UI design, information presentation |
| Transfer of Learning | `transfer_of_learning` | Cross-domain application, abstraction |
| Metacognition | `metacognition` | Self-awareness, reflective practice |

### Quality & Reliability (8 models)

Engineering practices for robust, maintainable systems.

| Model | ID | When to Use |
|-------|-----|------------|
| Defense in Depth | `defense_in_depth` | Security, validation layers |
| Fail Fast | `fail_fast` | Error handling, early detection |
| Graceful Degradation | `graceful_degradation` | Failure modes, fallback strategies |
| Idempotency | `idempotency` | API design, retry logic |
| Blast Radius | `blast_radius` | Deployment planning, failure isolation |
| Observability | `observability` | Debugging, monitoring design |
| Poka-Yoke (Error Proofing) | `poka_yoke` | UI/API design, configuration |
| Circuit Breaker | `circuit_breaker` | External API calls, cascade prevention |

### Communication (6 models)

Effective knowledge sharing and expectation management.

| Model | ID | When to Use |
|-------|-----|------------|
| Curse of Knowledge | `curse_of_knowledge` | Documentation, onboarding |
| Progressive Disclosure | `progressive_disclosure` | UI design, complexity management |
| Signal to Noise Ratio | `signal_to_noise` | Log design, alert configuration |
| Shared Mental Models | `shared_mental_models` | Team coordination, knowledge transfer |
| Principle of Least Surprise | `principle_of_least_surprise` | API/UI design, consistency |
| Empathy Mapping | `empathy_mapping` | UX design, error messages |

### Temporal (6 models)

Understanding time-dependent effects and patterns.

| Model | ID | When to Use |
|-------|-----|------------|
| Compounding | `compounding` | Long-term impact, technical debt |
| Half-Life | `half_life` | Knowledge decay, pattern staleness |
| Critical Path | `critical_path` | Project planning, dependency analysis |
| Lead vs Lag Indicators | `lead_lag_indicators` | Metric design, early warning systems |
| Rate of Change | `rate_of_change` | Trend analysis, acceleration detection |
| Hysteresis | `hysteresis` | State management, context preservation |

---

## Context Patterns

The selector automatically matches context to mental models using 12 predefined patterns:

1. **performance_degradation**: Bottlenecks, compounding, rate of change
2. **unexpected_behavior**: Emergence, second-order effects, feedback loops
3. **error_patterns**: Defense in depth, fail fast, circuit breaker
4. **cost_management**: Pareto principle, stocks & flows, compounding
5. **architectural_decision**: First principles, reversibility, system boundaries
6. **user_learning**: Scaffolding, ZPD, cognitive load theory
7. **pattern_detection**: Confirmation bias, availability heuristic, survivorship bias
8. **trust_violation**: Defense in depth, observability, graceful degradation
9. **estimation_accuracy**: Planning fallacy, margin of safety, anchoring
10. **knowledge_transfer**: Curse of knowledge, progressive disclosure, empathy mapping
11. **failure_analysis**: First principles, inversion, Occam's razor
12. **scaling_challenges**: Emergence, bottlenecks, resilience

---

## Combination Patterns

Predefined sequences for complex analysis:

### systems_diagnosis
Complete system health assessment before major changes.

Models: observability → bottlenecks → feedback_loops → resilience → blast_radius

### trust_audit
Evaluating system trustworthiness.

Models: defense_in_depth → graceful_degradation → observability → principle_of_least_surprise → poka_yoke

### learning_path_design
Creating pedagogical experiences.

Models: zone_of_proximal_development → scaffolding → cognitive_load_theory → progressive_disclosure → transfer_of_learning

### architectural_review
Evaluating design decisions.

Models: first_principles → system_boundaries → leverage_points → reversibility → regret_minimization

### cost_optimization
Reducing costs while maintaining quality.

Models: pareto_principle → opportunity_cost → margin_of_safety → leverage_points → stocks_and_flows

---

## Advanced Usage

### Custom Context Patterns

```python
# Select multiple models for complex analysis
result = selector.select_for_context(
    context="recurring errors with performance degradation and cost spike",
    max_models=10,
    min_confidence=0.5
)

print(f"Selected {len(result.models)} models")
print(f"Overall confidence: {result.confidence:.0%}")
print(f"Rationale: {result.rationale}")
```

### Combination Patterns

```python
# Use predefined combination for trust audit
trust_models = selector.get_combination_pattern("trust_audit")

for model in trust_models:
    print(f"Apply {model.name}")
    print(f"  Output: {model.output_format}")
```

### Category-Based Selection

```python
from mental_models.models import ModelCategory

# Get all learning pedagogy models
learning_models = selector.get_models_by_category(
    ModelCategory.LEARNING_PEDAGOGY
)

for model in learning_models:
    print(f"{model.name}: {model.description}")
```

---

## Integration with GAIA

### Process Observer

The Process Observer uses mental models to structure its analysis:

```python
from argus.process_observer import ProcessObserver
from mental_models import MentalModelSelector

observer = ProcessObserver(memory)
selector = MentalModelSelector()

# Detect pattern
pattern = observer.detect_pattern()

# Select appropriate mental models for analysis
models = selector.select_for_context(pattern.description)

# Apply models to generate structured insights
for model in models.models:
    analysis = apply_mental_model(model, pattern)
    observer.record_analysis(analysis)
```

### Explainability System

Mental models are explained at different complexity levels:

```python
from argus.explainability import Explainer

explainer = Explainer()

# Explain mental model at user's level
explanation = explainer.explain("feedback_loops", level=ExplanationLevel.DEFAULT)
print(explanation.content)
```

---

## Best Practices

### 1. Start with Context Patterns

Don't manually select models. Use context-aware selection:

```python
# Good: Let selector choose based on context
result = selector.select_for_context("performance issue")

# Less good: Manually selecting without context
model = selector.get_model("bottlenecks")
```

### 2. Check Confidence Scores

Use confidence thresholds to avoid false positives:

```python
result = selector.select_for_context(
    context,
    min_confidence=0.7  # Only high-confidence matches
)
```

### 3. Use Combination Patterns for Complex Analysis

For multi-faceted problems, use predefined combinations:

```python
# For architectural decisions
models = selector.get_combination_pattern("architectural_review")

# Apply in sequence
for model in models:
    analysis = analyze_with_model(model, decision_context)
```

### 4. Avoid Over-Application

Don't force mental models onto every situation:

- Check if context actually matches (confidence > 0.6)
- Start with 1-2 models, add more only if needed
- Prefer simpler models when appropriate (Occam's Razor)

---

## Testing

```bash
# Run mental model tests
pytest tests/mental_models/ -v

# With coverage
pytest tests/mental_models/ --cov=mental_models
```

---

## References

- Munger, C. (1994). A Lesson on Elementary, Worldly Wisdom
- Kahneman, D. (2011). Thinking, Fast and Slow
- Meadows, D. (2008). Thinking in Systems
- GAIA_BIBLE.md - Constitutional principles
- SR_COUNCIL_ANALYSIS.md - Process Observer design

---

**Maintained by:** GAIA Constitutional Team
**License:** Internal GAIA Ecosystem
