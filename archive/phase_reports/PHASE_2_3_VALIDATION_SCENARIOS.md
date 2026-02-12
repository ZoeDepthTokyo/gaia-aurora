# PHASE 2/3 VALIDATION SCENARIOS

**Version:** 1.0.0
**Status:** Active Testing Framework
**Created:** February 4, 2026
**Purpose:** Concrete validation scenarios with measurable outcomes for Phase 2/3 components

---

## Overview

This document defines 18 concrete validation scenarios across 5 Phase 2/3 components. Each scenario includes setup, expected behavior, success metrics, and risk analysis for empirical validation of GAIA's observability, memory, and workflow capabilities.

**Validation Principles:**
1. **Observable outcomes**: Every scenario produces measurable results
2. **Constitutional compliance**: All scenarios validate trust principles
3. **Edge case coverage**: Failure modes explicitly tested
4. **User feedback loops**: Human validation checkpoints included
5. **Quantitative + qualitative**: Both hard metrics and subjective quality

---

## Component 1: Mental Model Library

### Scenario 1.1: Context-Aware Model Selection Accuracy

**Setup:**
- Initialize MentalModelSelector with 59-model registry
- Prepare 20 diverse context strings across all categories
- Include ambiguous cases (e.g., "system is slow" - could be performance OR cognitive load)

**Action:**
```python
selector = MentalModelSelector()
contexts = [
    "performance degradation detected over 30 days",
    "user struggling to understand explanation",
    "recurring error in Stage 3 validation",
    "should we refactor this adapter?",
    "cost increased 40% this month"
]

for context in contexts:
    result = selector.select_for_context(context, max_models=3)
    print(f"Context: {context}")
    print(f"Models: {[m.name for m in result.models]}")
    print(f"Confidence: {result.confidence}")
```

**Expected Behavior:**
1. "performance degradation" → selects `bottlenecks`, `compounding`, `rate_of_change`
2. "user struggling" → selects `cognitive_load_theory`, `scaffolding`, `curse_of_knowledge`
3. "recurring error" → selects `defense_in_depth`, `fail_fast`, `root_cause_analysis`
4. "refactor decision" → selects `first_principles`, `reversibility`, `sunk_cost_fallacy`
5. "cost increase" → selects `pareto_principle`, `opportunity_cost`, `stocks_and_flows`

**Success Criteria:**
- **Quantitative:**
  - Top-3 model accuracy ≥85% (human expert agreement)
  - Context pattern match latency <100ms
  - Confidence calibration: high confidence (>0.8) → 90%+ accurate
  - Confidence calibration: medium confidence (0.5-0.8) → 70%+ accurate

- **Qualitative:**
  - Selected models are relevant to domain experts
  - Rationale explanations are clear and actionable
  - No obviously wrong selections in top-3

**Measurement Methods:**
1. Expert panel (3+ raters) scores each selection 0-10
2. Latency measured via `time.perf_counter()`
3. Confidence vs accuracy correlation (Brier score)
4. False positive rate: ambiguous contexts selecting conflicting models

**Edge Cases:**
1. **Empty context string** → Should return error or default set, not crash
2. **Non-English context** → Should gracefully degrade (English-only notice)
3. **Context with no matching patterns** → Should return generic models + low confidence
4. **Extremely long context (10K+ chars)** → Should truncate or summarize, not timeout

**Risk Analysis:**
- **Risk:** Over-confidence on ambiguous contexts (high confidence, wrong models)
- **Mitigation:** Calibration dataset with known ambiguous cases, threshold tuning
- **Detection:** Monitor confidence vs expert agreement correlation

**Constitutional Checkpoint:**
- ✅ Admits limits: Returns confidence score + rationale
- ✅ Never lies: Uncertainty explicitly communicated
- ✅ Inspectable: Shows which patterns matched

---

### Scenario 1.2: Pedagogical Explanation Adaptation (4 Levels)

**Setup:**
- Select 5 core mental models: `feedback_loops`, `first_principles`, `cognitive_load_theory`, `bottlenecks`, `confirmation_bias`
- Prepare user personas at each Growth Rung (1: Creator → 5: Mentor)

**Action:**
```python
explainer = Explainer()
model_id = "feedback_loops"

for rung in range(1, 6):
    explanation = explainer.explain_for_user(model_id, growth_rung=rung)
    print(f"\n=== Growth Rung {rung} ===")
    print(explanation.content)
    print(f"Complexity: {explanation.get_readability_score()}")
```

**Expected Behavior:**

| Growth Rung | Level | Example Output (feedback_loops) |
|-------------|-------|--------------------------------|
| 1 (Creator) | SIMPLE | "A feedback loop is when the output of a process feeds back as input, creating a cycle." |
| 2 (Explorer) | METAPHOR | "Like a thermostat: temperature affects heating, heating affects temperature." |
| 3 (Adapter) | DEFAULT | "Feedback loops have two types: reinforcing (amplify change) and balancing (stabilize). Example: compound interest vs. room temperature regulation." |
| 4-5 (Architect/Mentor) | ADVANCED | "Transfer functions, pole-zero analysis, stability criteria. See Control Theory (Åström & Murray, 2008). Code example: PID controller implementation." |

**Success Criteria:**
- **Quantitative:**
  - Flesch-Kincaid reading level: SIMPLE (grade 6-8), METAPHOR (grade 8-10), DEFAULT (grade 10-12), ADVANCED (college+)
  - Word count progression: SIMPLE (<50 words), METAPHOR (50-100), DEFAULT (100-200), ADVANCED (200-500)
  - Technical term density: SIMPLE (0%), METAPHOR (5%), DEFAULT (15%), ADVANCED (30%+)
  - User comprehension test: 80%+ can answer 3 follow-up questions correctly at their level

- **Qualitative:**
  - SIMPLE: No jargon, conversational, single concept
  - METAPHOR: Relatable analogies, concrete examples
  - DEFAULT: Balanced depth, key distinctions, actionable
  - ADVANCED: References, code, mathematical notation acceptable

**Measurement Methods:**
1. Automated readability scoring (Flesch-Kincaid, SMOG index)
2. User testing: 5 users per rung, comprehension quiz
3. Expert review: educators rate pedagogical quality
4. A/B test: users choose preferred explanation

**Edge Cases:**
1. **Model has no SIMPLE explanation** → Auto-generate or flag for human authoring
2. **User growth rung unknown** → Default to METAPHOR (safer than SIMPLE or ADVANCED)
3. **Non-technical model (e.g., empathy_mapping)** → All levels should avoid code/math

**Risk Analysis:**
- **Risk:** SIMPLE explanations are patronizing or oversimplified
- **Mitigation:** User testing with actual Rung 1 users (non-technical)
- **Detection:** Negative feedback rate, user preference for higher levels

**Constitutional Checkpoint:**
- ✅ Scaffolding: Progressive disclosure, user agency in choosing level
- ✅ Curse of knowledge: Explicitly designed to avoid expert assumptions
- ✅ Inspectable: User can see all 4 levels side-by-side

---

### Scenario 1.3: Real-World Decision Support Integration

**Setup:**
- Integrate Mental Model Library into VULCAN questionnaire (Stage 2: Adapter selection)
- Test on 10 diverse project types (web scraper, therapy tool, data pipeline, chatbot, etc.)

**Action:**
```python
# In VULCAN questionnaire
user_input = "I need to process therapy session transcripts and detect patterns"

# Mental model invocation
selector = MentalModelSelector()
decision_context = selector.select_for_context(
    "adapter selection for unstructured text pattern detection",
    max_models=5
)

# VULCAN uses models to frame suggestions
suggested_adapter = "CreativeAdapter"  # Based on first_principles, pattern_recognition
rationale = f"Selected {suggested_adapter} because:\n"
for model in decision_context.models:
    rationale += f"- {model.name}: {model.application_to_context}\n"
```

**Expected Behavior:**
- VULCAN suggests `CreativeAdapter` for therapy transcript analysis
- Rationale cites `pattern_recognition`, `first_principles`, `uncertainty_quantification`
- User sees transparent reasoning, can override suggestion

**Success Criteria:**
- **Quantitative:**
  - Suggestion acceptance rate ≥70% (users choose recommended adapter)
  - Rationale helpfulness rating ≥7/10 (user survey)
  - Time to decision reduced by 30% vs. no suggestions
  - Incorrect suggestion rate <15% (user reports issue)

- **Qualitative:**
  - Suggestions feel appropriate to domain experts
  - Rationale is actionable, not generic
  - User feels empowered to override (not coerced)

**Measurement Methods:**
1. VULCAN telemetry: track suggestion acceptance/override
2. Post-project survey: "Was the adapter suggestion helpful?"
3. Time measurement: questionnaire completion with vs without suggestions
4. Issue reports: users flag inappropriate suggestions

**Edge Cases:**
1. **Novel project type (no matching patterns)** → Generic suggestion + low confidence
2. **Conflicting mental models** → Show trade-offs, let user choose
3. **User overrides suggestion** → Log override reason, learn from it (MNEMIS)

**Risk Analysis:**
- **Risk:** Over-reliance on suggestions (users stop thinking)
- **Mitigation:** Require explicit confirmation, show reasoning, allow override
- **Detection:** Monitor override rate, survey questions on "feeling pressured"

**Constitutional Checkpoint:**
- ✅ User agency: Suggestions, not mandates
- ✅ Transparent reasoning: Shows which models informed decision
- ✅ Explicit learning: Override reason captured for improvement

---

### Scenario 1.4: Combination Pattern Effectiveness (Complex Analysis)

**Setup:**
- Use predefined combination patterns: `trust_audit`, `architectural_review`, `cost_optimization`
- Apply to 5 existing GAIA projects (HART OS, VIA, DATA FORGE, VULCAN, ARGUS)

**Action:**
```python
selector = MentalModelSelector()

# Perform trust audit on HART OS
project_state = load_project_state("hart_os")
trust_models = selector.get_combination_pattern("trust_audit")

audit_report = {}
for model in trust_models:
    analysis = apply_mental_model(model, project_state)
    audit_report[model.name] = analysis

# Expected sequence:
# 1. defense_in_depth: "Stage 3 validation lacks input sanitization"
# 2. graceful_degradation: "LLM timeout causes silent failure"
# 3. observability: "No structured logging in Stage 2"
# 4. principle_of_least_surprise: "Error messages are cryptic"
# 5. poka_yoke: "Config allows invalid threshold values"
```

**Expected Behavior:**
- `trust_audit` applies 5 models in sequence: defense_in_depth → graceful_degradation → observability → principle_of_least_surprise → poka_yoke
- Each model produces 3-5 findings with severity (LOW/MEDIUM/HIGH)
- Combined report shows trust gaps across multiple dimensions

**Success Criteria:**
- **Quantitative:**
  - Findings accuracy: 80%+ confirmed by manual code review
  - False positive rate: <20%
  - Coverage: All 5 models surface at least 1 finding per project
  - Time to audit: <10 minutes per project (vs. 2+ hours manual)

- **Qualitative:**
  - Findings are actionable (not generic advice)
  - Sequence makes logical sense (builds on previous findings)
  - No redundant findings across models

**Measurement Methods:**
1. Expert review: compare automated findings to manual audit
2. False positive tracking: developer verification of findings
3. Time measurement: automated vs manual audit duration
4. Actionability survey: developers rate finding usefulness

**Edge Cases:**
1. **All models find nothing** → Report "No issues detected" + confidence caveat
2. **Conflicting findings** → Surface conflict explicitly, don't hide
3. **Model not applicable to project type** → Skip with explanation

**Risk Analysis:**
- **Risk:** False negatives (missed issues give false confidence)
- **Mitigation:** Confidence thresholds, "absence of evidence ≠ evidence of absence" warnings
- **Detection:** Compare to manual audits, track missed issues over time

**Constitutional Checkpoint:**
- ✅ Graceful degradation: No silent failures if model can't analyze
- ✅ Inspectable: Shows which model produced which finding
- ✅ Admits limits: Confidence scores per finding

---

## Component 2: ARGUS Subconscious (Pattern Detection)

### Scenario 2.1: Pattern Detection Accuracy (External Memory)

**Setup:**
- Seed ExternalMemory database with 90 days of synthetic telemetry:
  - 50 observations (normal operations)
  - 15 observations (recurring error pattern, 3 instances)
  - 10 observations (performance degradation trend)
  - 5 observations (cost spike pattern, 2 instances over threshold)
- Initialize PatternDetector with lookback_days=30

**Action:**
```python
memory = ExternalMemory("test_memory.db")
detector = PatternDetector(memory)

# Seed data
for day in range(90):
    # Normal
    memory.store(MemoryEntry(
        type=MemoryType.OBSERVATION,
        content=f"Stage 3 confidence: 0.85",
        timestamp=datetime.now() - timedelta(days=90-day)
    ))

    # Recurring error (days 80, 85, 89)
    if day in [80, 85, 89]:
        memory.store(MemoryEntry(
            type=MemoryType.ERROR,
            content="Stage 3 validation timeout",
            confidence=0.9
        ))

    # Performance degradation (days 75-90)
    if day >= 75:
        latency = 2.0 + ((day - 75) * 0.1)  # 2.0s → 3.5s
        memory.store(MemoryEntry(
            type=MemoryType.OBSERVATION,
            content=f"Stage 3 latency: {latency}s"
        ))

# Detect patterns
patterns = detector.detect_patterns(
    lookback_days=30,
    min_frequency=3,
    min_confidence=0.6
)
```

**Expected Behavior:**
1. **RECURRING_ERROR detected**: "Stage 3 validation timeout (3 instances in 30 days)"
   - Confidence: 0.85-0.90
   - Severity: MEDIUM
   - Recommended actions: ["Check timeout threshold", "Review Stage 3 complexity"]

2. **PERFORMANCE_DEGRADATION detected**: "Stage 3 latency increasing (2.0s → 3.5s)"
   - Confidence: 0.75-0.85
   - Severity: HIGH
   - Trend: +75% over 15 days

3. **No false positives**: Normal operations (50 observations) do not trigger patterns

**Success Criteria:**
- **Quantitative:**
  - True positive rate: ≥90% (detects known seeded patterns)
  - False positive rate: ≤10% (normal operations don't trigger alerts)
  - Detection latency: <5 seconds for 30-day lookback
  - Confidence calibration: HIGH confidence (>0.8) → 85%+ confirmed patterns

- **Qualitative:**
  - Pattern descriptions are clear and specific
  - Recommended actions are relevant to pattern type
  - Severity ratings align with human judgment

**Measurement Methods:**
1. Confusion matrix: TP, FP, TN, FN for each pattern type
2. Latency benchmarks: median, p95, p99 detection time
3. Human validation: experts rate 20 detected patterns for relevance
4. Confidence calibration curve: confidence score vs confirmation rate

**Edge Cases:**
1. **Insufficient data** (<3 observations) → Returns empty list + low confidence warning
2. **Noisy data** (high variance) → Increases confidence threshold, reduces sensitivity
3. **Multiple overlapping patterns** → Returns both, flags correlation
4. **Stale patterns** (last instance >30 days ago) → Marks as "historical", lower priority

**Risk Analysis:**
- **Risk:** Alert fatigue from false positives
- **Mitigation:** High min_frequency (3), confidence threshold (0.6), severity filtering
- **Detection:** Track false positive reports, user dismissal rate

**Constitutional Checkpoint:**
- ✅ Read-only: Pattern detector never modifies memory, only reads
- ✅ Observable only: Reports facts (timestamps, counts), not inferences about "why"
- ✅ Transparent confidence: Every pattern includes confidence score + evidence count

---

### Scenario 2.2: Hypothesis Generation Quality

**Setup:**
- Use patterns detected in Scenario 2.1
- Initialize HypothesisGenerator
- Test hypothesis generation for each pattern type (RECURRING_ERROR, PERFORMANCE_DEGRADATION, COST_SPIKE)

**Action:**
```python
generator = HypothesisGenerator()
pattern = Pattern(
    type=PatternType.RECURRING_ERROR,
    description="Stage 3 validation timeout (3 instances)",
    evidence=["mem_001", "mem_015", "mem_029"],
    confidence=0.88
)

hypotheses = generator.generate_from_pattern(pattern)

for hyp in hypotheses:
    print(f"\nHypothesis: {hyp.description}")
    print(f"Confidence: {hyp.confidence}")
    print(f"Type: {hyp.type}")
    print(f"Test: {hyp.proposed_test}")
    print(f"Implications: {hyp.implications}")
```

**Expected Behavior:**

For `RECURRING_ERROR` pattern:
1. **Primary hypothesis**: "Stage 3 timeout threshold too low"
   - Confidence: 0.75
   - Type: CAUSAL
   - Test: "Increase timeout from 5s → 10s, monitor error rate"
   - Implications: ["Longer response time", "Fewer errors"]

2. **Alternative hypothesis**: "Stage 3 complexity increasing over time"
   - Confidence: 0.60
   - Type: CAUSAL
   - Test: "Profile Stage 3 execution, measure complexity growth"
   - Implications: ["Refactor needed", "Performance degradation continues"]

3. **Null hypothesis**: "Errors are random network timeouts"
   - Confidence: 0.40
   - Type: NULL
   - Test: "Correlate with network telemetry"
   - Implications: ["No code changes needed", "Infrastructure issue"]

**Success Criteria:**
- **Quantitative:**
  - Hypothesis relevance: 75%+ rated "plausible" by experts
  - Coverage: Generate 2-4 hypotheses per pattern (primary + alternatives + null)
  - Testability: 90%+ hypotheses have actionable test procedures
  - Confidence ordering: Primary hypothesis has highest confidence

- **Qualitative:**
  - Hypotheses are mutually exclusive (test one, can reject others)
  - Tests are practical and specific (not "investigate more")
  - Implications are concrete and useful for decision-making
  - Null hypothesis present to avoid confirmation bias

**Measurement Methods:**
1. Expert panel: rate each hypothesis for plausibility (0-10 scale)
2. Testability check: developers attempt to execute proposed tests
3. Ranking validation: experts reorder hypotheses by likelihood
4. Real-world validation: track which hypotheses are later confirmed

**Edge Cases:**
1. **Low-confidence pattern** (<0.6) → Generate fewer hypotheses, flag uncertainty
2. **Novel pattern type** (no templates) → Generic "investigate X" hypothesis + low confidence
3. **Conflicting evidence** → Generate competing hypotheses, flag contradiction

**Risk Analysis:**
- **Risk:** Over-confident hypotheses lead to premature conclusions
- **Mitigation:** Always generate null hypothesis, confidence penalties for low evidence
- **Detection:** Track hypothesis confirmation rate, calibrate confidence thresholds

**Constitutional Checkpoint:**
- ✅ Hypothesis, not certainty: Explicitly labeled as possibilities to test
- ✅ Inspectable reasoning: Shows evidence IDs that led to hypothesis
- ✅ Falsifiable: Every hypothesis includes test that could reject it

---

### Scenario 2.3: Non-Interventional Behavior Validation

**Setup:**
- Deploy Process Observer with read-only access to 3 projects (HART OS, VIA, DATA FORGE)
- Configure Observer with AGENT-tier memory scope (cannot write to PROJECT/GAIA)
- Monitor for 48 hours of normal operations

**Action:**
```python
observer = ProcessObserver(memory)

# Constitutional constraint validation
assert observer.can_execute_tools() == False, "Observer must be read-only"
assert observer.can_modify_code() == False, "Observer cannot change code"
assert observer.can_write_project_memory() == False, "Observer writes AGENT-tier only"

# Normal operation
for _ in range(48):  # 48 hours
    # Observer scans projects
    observations = observer.scan_ecosystem()

    # Observer detects patterns
    patterns = observer.detect_patterns(observations)

    # Observer generates hypotheses
    hypotheses = observer.generate_hypotheses(patterns)

    # Observer PROPOSES to user (never executes)
    if patterns:
        observer.propose_to_user(patterns, hypotheses)

    # Validate constraints
    assert_no_tool_executions()
    assert_no_code_modifications()
    assert_memory_tier_boundaries_respected()

    time.sleep(3600)  # Wait 1 hour
```

**Expected Behavior:**
1. Observer reads telemetry, logs, memory across 3 projects
2. Observer detects patterns, generates hypotheses
3. Observer stores findings in AGENT-tier memory only
4. Observer PROPOSES findings to user (via dashboard or notification)
5. Observer WAITS for user decision, does not auto-execute

**Success Criteria:**
- **Quantitative:**
  - Zero tool executions: 100% constraint compliance
  - Zero code modifications: 100% read-only guarantee
  - Zero PROJECT/GAIA memory writes without proposal: 100% tier boundary compliance
  - Proposal latency: User sees findings within 5 minutes of detection

- **Qualitative:**
  - Proposals are actionable but not pushy
  - User feels in control (not automated away)
  - Proposals include "ignore" and "remind later" options

**Measurement Methods:**
1. Audit log review: grep for any tool execution, code changes
2. Memory tier validation: check all Observer writes are AGENT-scoped
3. User survey: "Do you feel GAIA acts autonomously?" (target: 0% "yes")
4. Constitutional compliance report: automated checks every hour

**Edge Cases:**
1. **Critical issue detected** → Observer escalates urgency, but still no auto-execution
2. **User unavailable** → Observer queues proposal, retries notification
3. **Memory promotion proposed** → Observer submits to PROJECT agent for review

**Risk Analysis:**
- **Risk:** Observer finds loophole to execute actions
- **Mitigation:** Tool access mechanically removed, not policy-based
- **Detection:** Real-time monitoring, immediate shutdown on violation

**Constitutional Checkpoint:**
- ✅ Non-interventional: Reflective cognition only, never executive
- ✅ Memory boundaries: AGENT-tier only, proposals for promotion
- ✅ Transparent: All observations + reasoning logged with provenance

---

### Scenario 2.4: Context Enrichment for Decision Support

**Setup:**
- Populate ExternalMemory with 90 days of HART OS project history:
  - 30 observations (confidence scores)
  - 10 errors (Stage 3 validation failures)
  - 5 decisions (past threshold adjustments)
  - 3 patterns (confidence drift detected)
- Initialize ContextEnricher

**Action:**
```python
enricher = ContextEnricher(memory)

# New observation arrives
current_observation = "HART OS Stage 3 confidence: 0.78 (down from 0.85)"

# Enrich context
context = enricher.enrich_for_observation(
    observation=current_observation,
    project="hart_os",
    lookback_days=30
)

print(f"Related patterns: {len(context['related_patterns'])}")
print(f"Related errors: {len(context['related_errors'])}")
print(f"Past decisions: {len(context['past_decisions'])}")
print(f"Temporal trend: {context['temporal_context']['trend']}")
print(f"Project health: {context['project_context']['health_score']}")
```

**Expected Behavior:**
- `related_patterns`: Returns 1 pattern ("confidence drift detected 15 days ago")
- `related_errors`: Returns 3 Stage 3 validation failures (possibly causal)
- `past_decisions`: Returns 1 decision ("threshold lowered from 0.85 → 0.80")
- `temporal_trend`: "DECLINING (0.85 → 0.78 over 30 days)"
- `health_score`: 0.72 (based on error rate, confidence trend)

**Success Criteria:**
- **Quantitative:**
  - Context retrieval latency: <200ms for 30-day lookback
  - Relevance: 80%+ retrieved items rated "relevant" by domain expert
  - Completeness: Retrieves 90%+ of manually identified related items
  - False inclusion rate: <15% irrelevant items in context

- **Qualitative:**
  - Context helps user understand observation (not just data dump)
  - Temporal trend is accurate and useful
  - Past decisions provide valuable precedent

**Measurement Methods:**
1. Latency benchmark: median, p95, p99 retrieval time
2. Expert evaluation: rate relevance of each retrieved item
3. Completeness check: compare to manual search results
4. User survey: "Was the context helpful for decision-making?"

**Edge Cases:**
1. **No related history** → Returns empty context + message
2. **Ambiguous observation** → Returns broader context, flags ambiguity
3. **Conflicting past decisions** → Surfaces both, highlights conflict

**Risk Analysis:**
- **Risk:** Context overload (too much information)
- **Mitigation:** Limit to top-N most relevant items, summarize trends
- **Detection:** User dismissal rate, feedback on "too much context"

**Constitutional Checkpoint:**
- ✅ Inspectable: Shows provenance of every context item
- ✅ Transparent: Confidence scores on relevance matching
- ✅ Graceful degradation: No context found → says so explicitly

---

## Component 3: Explainability System

### Scenario 3.1: 4-Level Explanation Clarity

**Setup:**
- Prepare 5 complex GAIA decisions requiring explanation:
  1. Why VULCAN suggested CreativeAdapter
  2. Why ARGUS flagged "confidence drift" pattern
  3. Why MNEMIS rejected memory promotion
  4. Why LOOM halted workflow execution
  5. Why mental model selector chose "feedback_loops"
- Generate explanations at all 4 levels (SIMPLE, METAPHOR, DEFAULT, ADVANCED)

**Action:**
```python
explainer = Explainer()

decision_id = "vulcan_adapter_suggestion_001"
decision_data = {
    "suggestion": "CreativeAdapter",
    "rationale": "Unstructured text analysis requires flexible LLM reasoning",
    "confidence": 0.82,
    "alternatives": ["DeterministicAdapter", "ProcessorAdapter"]
}

# Generate 4 levels
for level in [ExplanationLevel.SIMPLE, ExplanationLevel.METAPHOR,
              ExplanationLevel.DEFAULT, ExplanationLevel.ADVANCED]:
    explanation = explainer.explain_decision(decision_id, decision_data, level)
    print(f"\n=== {level.name} ===")
    print(explanation.content)
```

**Expected Behavior:**

**SIMPLE**: "VULCAN suggested CreativeAdapter because your project needs flexible text analysis."

**METAPHOR**: "Think of adapters like tools: a hammer (DeterministicAdapter) for nails, a screwdriver (ProcessorAdapter) for screws. Your unstructured text is like clay - you need flexible hands (CreativeAdapter) to shape it."

**DEFAULT**: "VULCAN suggested CreativeAdapter (confidence: 82%) because:
1. Your project processes therapy transcripts (unstructured text)
2. Pattern detection requires flexible LLM reasoning
3. DeterministicAdapter is too rigid for this use case
4. CreativeAdapter uses gpt-4o for nuanced interpretation

You can override this suggestion if you prefer rule-based processing."

**ADVANCED**: "Decision tree:
```
IF input_type == "unstructured_text" AND task == "pattern_detection"
  THEN rank adapters by flexibility_score
  WHERE flexibility_score = f(llm_capability, prompt_complexity, output_variance)

CreativeAdapter: flexibility=0.95, confidence=0.82
DeterministicAdapter: flexibility=0.30, confidence=0.45
ProcessorAdapter: flexibility=0.60, confidence=0.55
```

Mental models applied: first_principles (task decomposition), pattern_recognition (text analysis), opportunity_cost (alternative evaluation).

Override path: Set adapter='DeterministicAdapter' in config.py if deterministic rules preferred."

**Success Criteria:**
- **Quantitative:**
  - Reading level: SIMPLE (grade 6-8), METAPHOR (8-10), DEFAULT (10-12), ADVANCED (college+)
  - Comprehension test: 85%+ users answer 3 follow-up questions correctly at their level
  - Time to understanding: SIMPLE (10s), METAPHOR (20s), DEFAULT (45s), ADVANCED (90s)
  - User satisfaction: 80%+ rate explanation as "helpful" for their level

- **Qualitative:**
  - SIMPLE: No jargon, direct answer, one concept
  - METAPHOR: Relatable analogy, concrete comparison
  - DEFAULT: Balanced, shows alternatives, actionable override path
  - ADVANCED: Technical depth, decision logic, code/formulas included

**Measurement Methods:**
1. Automated readability analysis (Flesch-Kincaid, Gunning Fog)
2. User testing: 5 users per level, comprehension quiz + timed
3. Expert review: educators + developers rate quality
4. A/B testing: compare 4-level vs. single-level explanations

**Edge Cases:**
1. **Decision has no simple explanation** → SIMPLE level says "This decision is complex, try METAPHOR level"
2. **Metaphor database empty** → Falls back to DEFAULT, flags for human authoring
3. **User switches levels mid-explanation** → Maintains context, shows same decision at new level

**Risk Analysis:**
- **Risk:** SIMPLE is too simplistic (patronizing), ADVANCED is too dense (intimidating)
- **Mitigation:** User testing with real Rung 1 and Rung 5 users, iteration based on feedback
- **Detection:** User preference surveys, level switching patterns

**Constitutional Checkpoint:**
- ✅ Progressive disclosure: User chooses depth, not system
- ✅ Inspectable: All 4 levels available, no hidden reasoning
- ✅ Admits limits: Flags when explanation incomplete or uncertain

---

### Scenario 3.2: Growth Rung Mapping Accuracy

**Setup:**
- Create 5 synthetic user profiles with known Growth Rung levels (1-5)
- Each profile has interaction history (actions, questions, code modifications)
- Initialize Growth Rung classifier

**Action:**
```python
classifier = GrowthRungClassifier()

profiles = [
    {  # Rung 1: Creator
        "actions": ["used_vulcan_wizard", "clicked_defaults", "ran_tests"],
        "questions": ["how_do_I_run_this", "what_is_an_adapter"],
        "code_mods": []
    },
    {  # Rung 2: Explorer
        "actions": ["viewed_config", "modified_thresholds", "read_docs"],
        "questions": ["why_this_threshold", "how_does_stage_3_work"],
        "code_mods": ["config.py"]
    },
    {  # Rung 3: Adapter
        "actions": ["extended_adapter", "wrote_custom_stage", "contributed_PR"],
        "questions": ["adapter_interface_details", "stage_testing_patterns"],
        "code_mods": ["adapters/", "stages/"]
    },
    {  # Rung 4: Architect
        "actions": ["designed_adapter", "refactored_pipeline", "mentored_users"],
        "questions": ["architectural_tradeoffs", "performance_optimization"],
        "code_mods": ["core/", "adapters/", "tests/"]
    },
    {  # Rung 5: Mentor
        "actions": ["created_tutorials", "answered_forum", "gave_talks"],
        "questions": ["teaching_strategies", "onboarding_improvements"],
        "code_mods": ["docs/", "examples/", "tutorials/"]
    }
]

for i, profile in enumerate(profiles):
    predicted_rung = classifier.classify(profile)
    print(f"Profile {i+1}: Predicted Rung {predicted_rung}, Actual Rung {i+1}")
```

**Expected Behavior:**
- All 5 profiles correctly classified to their ground truth Growth Rung
- Confidence scores reflect feature clarity (Rung 1 and 5 high confidence, Rung 2-4 medium)
- Reasoning explains which features influenced classification

**Success Criteria:**
- **Quantitative:**
  - Classification accuracy: ≥80% exact match, ≥95% within ±1 rung
  - Confidence calibration: High confidence (>0.8) → 90%+ accurate
  - Progression detection: Correctly identifies rung transitions (e.g., 2→3)
  - Feature importance: Top 3 features account for 70%+ of decision

- **Qualitative:**
  - Classification reasoning is intuitive to users
  - Rung assignments feel fair and non-judgmental
  - Users agree with their assigned rung (self-assessment)

**Measurement Methods:**
1. Confusion matrix: actual vs predicted rungs
2. Confidence calibration: plot confidence vs accuracy
3. Feature ablation: remove features, measure impact on accuracy
4. User validation: survey users on rung assignment agreement

**Edge Cases:**
1. **New user (no history)** → Default to Rung 1, low confidence, prompt for self-assessment
2. **Regressive behavior** (Rung 3 user only using defaults) → Flag anomaly, don't auto-demote
3. **Multi-modal profile** (Rung 1 actions + Rung 4 questions) → Average or flag for manual review

**Risk Analysis:**
- **Risk:** Rung labels feel judgmental or gatekeeping
- **Mitigation:** Frame as "current focus" not "skill level", allow self-override
- **Detection:** User feedback surveys, rung override rate

**Constitutional Checkpoint:**
- ✅ Pedagogical intent: Rung used for helpful suggestions, not gatekeeping
- ✅ User agency: Can override assigned rung, see reasoning
- ✅ Non-judgmental: Labels are descriptive ("Creator") not evaluative ("Beginner")

---

### Scenario 3.3: User Preference Adaptation

**Setup:**
- Track 20 users over 30 days of GAIA interactions
- Log explanation level preferences (which level they choose/read)
- Train preference model to predict preferred level based on user actions

**Action:**
```python
preference_tracker = ExplanationPreferenceTracker()

# User 001: Consistently chooses SIMPLE, rarely expands to DEFAULT
user_001_interactions = [
    {"decision_id": "dec_001", "levels_viewed": ["SIMPLE"], "satisfaction": 9},
    {"decision_id": "dec_002", "levels_viewed": ["SIMPLE"], "satisfaction": 8},
    {"decision_id": "dec_003", "levels_viewed": ["SIMPLE", "DEFAULT"], "satisfaction": 7},
    # ... 30 days of interactions
]

# User 002: Starts at DEFAULT, progresses to ADVANCED
user_002_interactions = [
    {"decision_id": "dec_001", "levels_viewed": ["DEFAULT"], "satisfaction": 7},
    {"decision_id": "dec_002", "levels_viewed": ["DEFAULT", "ADVANCED"], "satisfaction": 8},
    {"decision_id": "dec_010", "levels_viewed": ["ADVANCED"], "satisfaction": 9},
    # ... progression visible
]

# Predict preferred level
user_001_prediction = preference_tracker.predict_preferred_level("user_001")
user_002_prediction = preference_tracker.predict_preferred_level("user_002")

print(f"User 001 predicted: {user_001_prediction}")  # Expected: SIMPLE
print(f"User 002 predicted: {user_002_prediction}")  # Expected: ADVANCED
```

**Expected Behavior:**
- User 001 consistently prefers SIMPLE → system defaults to SIMPLE for new decisions
- User 002 progresses DEFAULT → ADVANCED → system defaults to ADVANCED
- System detects preference changes and updates recommendations

**Success Criteria:**
- **Quantitative:**
  - Prediction accuracy: 75%+ match user's actual choice
  - Adaptation speed: Detects preference change within 5 interactions
  - Satisfaction improvement: Users with adapted defaults rate 15%+ higher satisfaction
  - False adaptation rate: <10% (incorrectly changing default)

- **Qualitative:**
  - Defaults feel "right" to users (not surprising)
  - Adaptation is gradual, not jarring
  - Users can easily override default if wrong

**Measurement Methods:**
1. Prediction accuracy: actual choice vs predicted default
2. Adaptation latency: number of interactions to detect change
3. Satisfaction comparison: adapted vs. non-adapted users
4. User feedback: "Does the default level feel right?"

**Edge Cases:**
1. **No clear preference** (uses all levels equally) → Default to METAPHOR (middle ground)
2. **Conflicting signals** (high SIMPLE usage but low satisfaction) → Prompt user to choose
3. **Rapid switching** (SIMPLE then ADVANCED) → Interpret as exploration, don't adapt yet

**Risk Analysis:**
- **Risk:** System "traps" user in one level (doesn't encourage growth)
- **Mitigation:** Periodic prompts to try other levels, growth rung suggestions
- **Detection:** Monitor level diversity over time, flag stagnation

**Constitutional Checkpoint:**
- ✅ User agency: Adaptation is suggestion, not restriction
- ✅ Transparent: User can see why default changed
- ✅ Reversible: Can revert to any level at any time

---

## Component 4: MNEMIS Memory System

### Scenario 4.1: Memory Promotion Workflow (AGENT → PROJECT → GAIA)

**Setup:**
- Initialize MNEMIS with 3-tier hierarchy
- Create execution agent with AGENT-tier access
- Create project agent with PROJECT-tier access
- Human/GAIA-agent has GAIA-tier access

**Action:**
```python
store = MnemisStore()
controller = MemoryAccessController()

# 1. Execution agent discovers pattern
agent_contract = controller.register_agent(
    agent_id="execution_agent_001",
    access_level=MemoryAccessLevel.AGENT,
    project_id="hart_os"
)

agent_memory_id = store.write(
    content={"pattern": "confidence scores stabilize after 3 runs"},
    scope=controller.create_agent_scope("execution_agent_001"),
    contract=agent_contract,
    tags=["pattern", "confidence"]
)

# 2. Agent proposes promotion to PROJECT tier
promotion_engine = MemoryPromotionEngine(store, controller)
proposal_id = promotion_engine.propose_promotion(
    memory_id=agent_memory_id,
    to_scope=controller.create_project_scope("hart_os"),
    agent_id="execution_agent_001",
    rationale="Pattern observed 12 times, useful for all HART OS agents"
)

# 3. Project agent reviews and approves
project_contract = controller.register_agent(
    agent_id="project_agent_hart_os",
    access_level=MemoryAccessLevel.PROJECT,
    project_id="hart_os"
)

project_memory_id = promotion_engine.approve_promotion(
    proposal_id=proposal_id,
    reviewer="project_agent_hart_os",
    notes="Confirmed - stabilization pattern applies to all executions"
)

# 4. Project agent proposes to GAIA tier (ecosystem-wide)
gaia_proposal_id = promotion_engine.propose_promotion(
    memory_id=project_memory_id,
    to_scope=controller.create_gaia_scope(),
    agent_id="project_agent_hart_os",
    rationale="Pattern confirmed in HART OS, VIA, DATA FORGE (3 projects)"
)

# 5. Human/GAIA reviews and approves
gaia_memory_id = promotion_engine.approve_promotion(
    proposal_id=gaia_proposal_id,
    reviewer="human",
    notes="Approved - useful cross-project pattern"
)

# 6. Verify memory is accessible ecosystem-wide
all_projects = ["hart_os", "via", "data_forge", "new_project"]
for project_id in all_projects:
    new_agent_contract = controller.register_agent(
        agent_id=f"agent_{project_id}",
        access_level=MemoryAccessLevel.PROJECT,
        project_id=project_id
    )
    memory = store.read(gaia_memory_id, new_agent_contract)
    assert memory is not None, f"GAIA memory should be readable by {project_id}"
```

**Expected Behavior:**
1. Agent writes to AGENT tier (ephemeral)
2. Agent proposes promotion to PROJECT tier
3. Project agent approves → memory promoted to PROJECT tier
4. Project agent proposes promotion to GAIA tier
5. Human approves → memory promoted to GAIA tier
6. All projects can now read GAIA-tier memory

**Success Criteria:**
- **Quantitative:**
  - Promotion latency: <2 seconds per tier transition
  - Approval workflow: 100% require explicit approval (no auto-promotion)
  - Access control: 100% tier boundary enforcement (no unauthorized reads/writes)
  - Audit trail: 100% promotions logged with who/when/why

- **Qualitative:**
  - Promotion rationale is clear and specific
  - Reviewers can make informed decisions (not rubber-stamping)
  - Rejected promotions have clear reasoning
  - Promoted memory is actually useful to downstream projects

**Measurement Methods:**
1. Latency benchmarks: time from proposal to approval
2. Compliance testing: attempt unauthorized access, verify rejection
3. Audit log review: check completeness and clarity
4. Usefulness survey: downstream projects rate promoted memories

**Edge Cases:**
1. **Promotion rejected** → Memory stays at current tier, rejection reason logged
2. **Proposal times out** (no review for 7 days) → Escalates to higher authority
3. **Conflicting promotions** (same pattern from 2 projects) → Merge or choose canonical
4. **Demote memory** (promoted by mistake) → Requires reverse proposal + approval

**Risk Analysis:**
- **Risk:** Promotion becomes bottleneck (waiting for approvals)
- **Mitigation:** Async workflow, notification system, timeout escalation
- **Detection:** Monitor promotion latency, pending proposal queue length

**Constitutional Checkpoint:**
- ✅ Explicit learning: Every promotion requires approval, never automatic
- ✅ Provenance: Full audit trail of who promoted when and why
- ✅ Inspectable: Users can see all proposals, approved and rejected

---

### Scenario 4.2: Access Contract Enforcement

**Setup:**
- Create 3 agents with different access levels (AGENT, PROJECT, GAIA)
- Create memory entries at each tier
- Attempt valid and invalid read/write operations

**Action:**
```python
store = MnemisStore()
controller = MemoryAccessController()

# Create agents
agent_low = controller.register_agent(
    agent_id="agent_low",
    access_level=MemoryAccessLevel.AGENT,
    project_id="project_a"
)

agent_mid = controller.register_agent(
    agent_id="agent_mid",
    access_level=MemoryAccessLevel.PROJECT,
    project_id="project_a"
)

agent_high = controller.register_agent(
    agent_id="agent_high",
    access_level=MemoryAccessLevel.GAIA,
    project_id=None  # GAIA-level, not project-specific
)

# Create memories at each tier
gaia_memory = store.write(
    content={"pattern": "ecosystem_standard"},
    scope=controller.create_gaia_scope(),
    contract=agent_high,
    tags=["standard"]
)

project_memory = store.write(
    content={"pattern": "project_specific"},
    scope=controller.create_project_scope("project_a"),
    contract=agent_mid,
    tags=["local"]
)

agent_memory = store.write(
    content={"context": "execution_state"},
    scope=controller.create_agent_scope("agent_low"),
    contract=agent_low,
    tags=["ephemeral"]
)

# Test READ permissions (down hierarchy)
assert store.read(gaia_memory, agent_high) is not None  # ✓ GAIA reads GAIA
assert store.read(gaia_memory, agent_mid) is not None   # ✓ PROJECT reads GAIA
assert store.read(gaia_memory, agent_low) is None       # ✗ AGENT cannot read GAIA

assert store.read(project_memory, agent_mid) is not None  # ✓ PROJECT reads PROJECT
assert store.read(project_memory, agent_low) is None      # ✗ AGENT cannot read PROJECT

assert store.read(agent_memory, agent_low) is not None  # ✓ AGENT reads own memory

# Test WRITE permissions (exact level only)
try:
    store.write(
        content={"illegal": "write"},
        scope=controller.create_gaia_scope(),
        contract=agent_low,  # AGENT-level trying to write GAIA
        tags=[]
    )
    assert False, "Should have raised PermissionError"
except PermissionError as e:
    assert "AGENT cannot write to GAIA tier" in str(e)
```

**Expected Behavior:**
- **Read permissions**: Agents can read DOWN the hierarchy (GAIA → PROJECT → AGENT)
- **Write permissions**: Agents can write ONLY at their exact level
- **Violations**: Explicit PermissionError with clear message
- **Logging**: All violations logged to ARGUS telemetry

**Success Criteria:**
- **Quantitative:**
  - Access control accuracy: 100% correct allow/deny decisions
  - Violation detection: 100% violations logged
  - Performance: <10ms overhead for access checks
  - Zero bypasses: No loopholes found in security testing

- **Qualitative:**
  - Error messages are clear and actionable
  - Legitimate use cases are not blocked
  - Violation logs contain sufficient detail for auditing

**Measurement Methods:**
1. Comprehensive test matrix: all combinations of agent levels and memory tiers
2. Security audit: attempt to bypass access controls
3. Performance benchmarking: access check overhead
4. Log completeness: verify all violations captured

**Edge Cases:**
1. **Agent contract expires** → All subsequent operations denied until re-registration
2. **Agent switches projects** → Access to old project memory revoked
3. **Memory tier changes** (promotion) → Access rights update automatically
4. **Concurrent access** (race condition) → Atomic checks prevent TOCTOU bugs

**Risk Analysis:**
- **Risk:** Access control bypass allows unauthorized memory access
- **Mitigation:** Mechanical enforcement (not policy), comprehensive testing
- **Detection:** Regular security audits, penetration testing

**Constitutional Checkpoint:**
- ✅ No silent failures: All violations explicit and logged
- ✅ Inspectable: Access logs available for audit
- ✅ Graceful degradation: Violations don't crash system, just deny access

---

### Scenario 4.3: Cross-Project Memory Utility

**Setup:**
- Create 3 projects (hart_os, via, data_forge) with different domains
- Each project discovers useful patterns independently
- Promote selected patterns to GAIA tier
- Measure utility of shared memories for new project (therapy_assistant)

**Action:**
```python
# Project 1 (HART OS): Discovers confidence stabilization pattern
hart_pattern = store.write(
    content={
        "pattern": "Confidence scores stabilize after 3 validation runs",
        "domain": "therapy assessment",
        "evidence_count": 45
    },
    scope=controller.create_project_scope("hart_os"),
    contract=hart_contract,
    tags=["confidence", "validation", "stabilization"]
)

# Promote to GAIA
promote_to_gaia(hart_pattern, "Useful for all confidence-based systems")

# Project 2 (VIA): Discovers retry strategy
via_pattern = store.write(
    content={
        "pattern": "Retry with temperature=0.5 fixes malformed JSON 80% of time",
        "domain": "structured output",
        "evidence_count": 32
    },
    scope=controller.create_project_scope("via"),
    contract=via_contract,
    tags=["retry", "json", "temperature"]
)

# Promote to GAIA
promote_to_gaia(via_pattern, "Confirmed across VIA and DATA FORGE")

# Project 3 (DATA FORGE): Discovers timeout threshold
forge_pattern = store.write(
    content={
        "pattern": "95th percentile latency + 2 std dev = optimal timeout",
        "domain": "performance",
        "evidence_count": 67
    },
    scope=controller.create_project_scope("data_forge"),
    contract=forge_contract,
    tags=["performance", "timeout", "latency"]
)

# Promote to GAIA
promote_to_gaia(forge_pattern, "Statistical approach works across all projects")

# NEW PROJECT: therapy_assistant (creates with VULCAN)
therapy_contract = controller.register_agent(
    agent_id="therapy_assistant_agent",
    access_level=MemoryAccessLevel.PROJECT,
    project_id="therapy_assistant"
)

# Search GAIA tier for relevant patterns
search_engine = MemorySearchEngine(store)
relevant_patterns = search_engine.search_by_tags(
    tags=["confidence", "validation", "timeout"],
    contract=therapy_contract,
    scope=controller.create_gaia_scope()
)

print(f"Found {len(relevant_patterns)} relevant GAIA patterns")
for pattern in relevant_patterns:
    print(f"- {pattern.content['pattern']}")
    print(f"  Evidence: {pattern.content['evidence_count']} instances")
```

**Expected Behavior:**
- New project (therapy_assistant) inherits 3 GAIA-tier patterns
- Patterns are immediately applicable (confidence validation, retry strategy, timeout calculation)
- New project saves development time (doesn't rediscover patterns)
- New project avoids known pitfalls (learns from others' experience)

**Success Criteria:**
- **Quantitative:**
  - Inheritance rate: 90%+ GAIA patterns accessible to new projects
  - Relevance: 70%+ inherited patterns rated "useful" by new project
  - Time savings: 30%+ faster project setup vs. no shared memory
  - Error reduction: 25%+ fewer common mistakes in new projects

- **Qualitative:**
  - Inherited patterns are actionable and specific
  - Patterns don't feel generic or obvious
  - New projects understand provenance (where pattern came from)
  - Patterns don't conflict with project-specific needs

**Measurement Methods:**
1. New project survey: rate utility of each inherited pattern
2. Time tracking: project setup with vs without GAIA memories
3. Error comparison: new projects vs historical baseline
4. Relevance scoring: human evaluation of pattern applicability

**Edge Cases:**
1. **Pattern not applicable to new project** → Filtered by tag relevance, domain mismatch
2. **Conflicting patterns** (two approaches to same problem) → Surface both, let project choose
3. **Outdated patterns** (promoted 2 years ago) → Include staleness metadata, review periodically

**Risk Analysis:**
- **Risk:** Cargo-cult learning (applying patterns without understanding)
- **Mitigation:** Include provenance, evidence count, domain context
- **Detection:** Monitor pattern usage, survey for understanding

**Constitutional Checkpoint:**
- ✅ Knowledge inheritance: New projects benefit from ecosystem learnings
- ✅ Provenance: Patterns show origin project and evidence count
- ✅ User agency: Inherited patterns are suggestions, not mandates

---

### Scenario 4.4: Memory Expiration and Cleanup (AGENT Tier)

**Setup:**
- Create 20 AGENT-tier memories with varying ages (0-60 days old)
- Configure TTL: AGENT tier = 30 days
- Run cleanup process

**Action:**
```python
store = MnemisStore()
controller = MemoryAccessController()

# Seed AGENT-tier memories
agent_contract = controller.register_agent(
    agent_id="test_agent",
    access_level=MemoryAccessLevel.AGENT,
    project_id="test_project"
)

memory_ids = []
for days_ago in range(0, 65, 5):  # 0, 5, 10, ..., 60 days
    memory_id = store.write(
        content={"execution": f"run_{days_ago}_days_ago"},
        scope=controller.create_agent_scope("test_agent"),
        contract=agent_contract,
        tags=["execution"],
        timestamp=datetime.now() - timedelta(days=days_ago)
    )
    memory_ids.append((memory_id, days_ago))

# Run cleanup (TTL = 30 days)
bridge = MycelMemoryBridge(store, controller)
cleaned_count = bridge.cleanup_expired_sessions(ttl_days=30)

print(f"Cleaned {cleaned_count} expired memories")

# Verify: memories >30 days deleted, <=30 days retained
for memory_id, days_ago in memory_ids:
    memory = store.read(memory_id, agent_contract)
    if days_ago > 30:
        assert memory is None, f"Memory {days_ago} days old should be deleted"
    else:
        assert memory is not None, f"Memory {days_ago} days old should be retained"
```

**Expected Behavior:**
- Memories 0-30 days old: RETAINED
- Memories 35-60 days old: DELETED
- PROJECT and GAIA tier memories: NEVER auto-deleted (must be explicit)
- Cleanup logs: Deletion events logged to ARGUS telemetry

**Success Criteria:**
- **Quantitative:**
  - Cleanup accuracy: 100% correct delete/retain decisions
  - Performance: <5 seconds to clean 1000+ memories
  - No false deletions: 0% PROJECT/GAIA memories deleted
  - Audit trail: 100% deletions logged with reason

- **Qualitative:**
  - TTL policy is clear and predictable
  - No surprises (users expect AGENT memories to expire)
  - Cleanup doesn't degrade system performance

**Measurement Methods:**
1. Accuracy testing: verify correct memories deleted
2. Performance benchmarking: cleanup time vs database size
3. Safety testing: attempt to trigger false deletion
4. Log review: verify all deletions captured

**Edge Cases:**
1. **Memory promoted after expiration** → Promotion timestamp resets TTL
2. **Memory accessed near expiration** → Optional: extend TTL on access (configurable)
3. **Cleanup during active execution** → Cleanup skips memories with active sessions
4. **Clock skew** → Use creation timestamp, not system time for TTL calculation

**Risk Analysis:**
- **Risk:** Premature deletion of important AGENT memories
- **Mitigation:** Propose promotion before expiration (automated reminder)
- **Detection:** User reports of missing context, restoration requests

**Constitutional Checkpoint:**
- ✅ Explicit policy: TTL clearly communicated to agents
- ✅ Graceful degradation: Cleanup failures logged, don't block operations
- ✅ Audit trail: All deletions logged for accountability

---

## Component 5: LOOM Workflow Engine

### Scenario 5.1: Agent Authority Validation

**Setup:**
- Define 4 agents: OBSERVER (read-only), TRANSFORMER (pure function), EXECUTOR (side effects), COORDINATOR (manages others)
- Create workflow connecting all 4 types
- Validate authority constraints are enforced

**Action:**
```python
# Define agents
observer = AgentNode(
    id="observer_001",
    agent_type=AgentType.OBSERVER,
    name="Pattern Detector",
    implementation="detect_patterns"
)

transformer = AgentNode(
    id="transformer_001",
    agent_type=AgentType.TRANSFORMER,
    name="Data Validator",
    implementation="validate_data"
)

executor = AgentNode(
    id="executor_001",
    agent_type=AgentType.EXECUTOR,
    name="LLM Caller",
    implementation="call_llm"
)

coordinator = AgentNode(
    id="coordinator_001",
    agent_type=AgentType.COORDINATOR,
    name="Workflow Manager",
    implementation="manage_workflow"
)

# Register implementations
def detect_patterns(inputs):
    # Attempt to write to memory (should fail for OBSERVER)
    memory.write(...)  # ❌ Should raise PermissionError
    return {"patterns": []}

def validate_data(inputs):
    # Pure function, no side effects (allowed)
    return {"valid": inputs["data"] is not None}

def call_llm(inputs):
    # Side effects allowed for EXECUTOR
    llm_client.chat(...)  # ✓ Allowed
    return {"response": "..."}

def manage_workflow(inputs):
    # Coordinator can orchestrate, but not execute tools directly
    agent_1_result = execute_agent("transformer_001")  # ✓ Allowed
    agent_1_result.tools.run(...)  # ❌ Should fail
    return {"status": "complete"}

# Execute workflow
engine = WorkflowEngine()
engine.register_agent_implementation("observer_001", detect_patterns)
engine.register_agent_implementation("transformer_001", validate_data)
engine.register_agent_implementation("executor_001", call_llm)
engine.register_agent_implementation("coordinator_001", manage_workflow)

workflow = AgentWorkflow(
    id="test_workflow",
    agents=[observer, transformer, executor, coordinator],
    connections=[...],
    entry_points=["observer_001"]
)

context = engine.execute_workflow(workflow, initial_inputs={})
```

**Expected Behavior:**
- **OBSERVER**: Read-only, cannot write to memory or execute tools → PermissionError
- **TRANSFORMER**: Pure function, no external calls → Allowed
- **EXECUTOR**: Can execute tools, call APIs, write state → Allowed
- **COORDINATOR**: Can orchestrate, but not execute tools directly → Mixed enforcement

**Success Criteria:**
- **Quantitative:**
  - Authority enforcement: 100% violations detected and blocked
  - False positives: <5% (legitimate actions blocked)
  - Detection latency: <50ms overhead per agent execution
  - Audit trail: 100% authority checks logged

- **Qualitative:**
  - Error messages clearly explain authority violation
  - Legitimate use cases are not blocked
  - Agent type definitions are intuitive

**Measurement Methods:**
1. Violation testing: attempt invalid operations, verify blocking
2. Performance benchmarking: overhead of authority checks
3. False positive testing: verify legitimate operations allowed
4. Log review: check completeness of authority audit trail

**Edge Cases:**
1. **OBSERVER tries indirect write** (via COORDINATOR) → Both levels checked, violation detected
2. **EXECUTOR exceeds cost limit** → Governance rule halts execution
3. **TRANSFORMER with non-deterministic code** → Static analysis warning, runtime allowed

**Risk Analysis:**
- **Risk:** Authority bypass via indirect call chains
- **Mitigation:** Multi-level checking, call stack analysis
- **Detection:** Audit logs, runtime monitoring

**Constitutional Checkpoint:**
- ✅ Glass-box authority: Agent types explicitly defined and enforced
- ✅ No silent violations: All authority checks explicit
- ✅ Inspectable: Users can see authority graph

---

### Scenario 5.2: Workflow Execution Transparency

**Setup:**
- Create multi-stage workflow (3 agents connected sequentially)
- Execute workflow with dry-run mode
- Execute workflow for real
- Compare execution traces

**Action:**
```python
# Define workflow
agent_1 = AgentNode(id="agent_1", name="Data Fetcher", ...)
agent_2 = AgentNode(id="agent_2", name="Data Processor", ...)
agent_3 = AgentNode(id="agent_3", name="Result Writer", ...)

workflow = AgentWorkflow(
    id="data_pipeline",
    agents=[agent_1, agent_2, agent_3],
    connections=[
        AgentConnection(source="agent_1", target="agent_2", ...),
        AgentConnection(source="agent_2", target="agent_3", ...)
    ],
    entry_points=["agent_1"]
)

# Dry run (validation only)
dry_context = engine.execute_workflow(workflow, initial_inputs={}, dry_run=True)

print("=== DRY RUN ===")
print(f"Execution plan: {dry_context.execution_plan}")
print(f"Estimated cost: ${dry_context.estimated_cost}")
print(f"Estimated time: {dry_context.estimated_time_seconds}s")
print(f"Risks: {dry_context.identified_risks}")

# Real execution
real_context = engine.execute_workflow(workflow, initial_inputs={"data": [1, 2, 3]})

print("\n=== REAL EXECUTION ===")
print(f"Actual cost: ${real_context.total_cost}")
print(f"Actual time: {real_context.total_time_seconds}s")
print(f"Execution trace:")
for step in real_context.execution_trace:
    print(f"  {step.timestamp}: {step.agent_id} - {step.status}")
    print(f"    Input: {step.input_data}")
    print(f"    Output: {step.output_data}")
    if step.errors:
        print(f"    Errors: {step.errors}")
```

**Expected Behavior:**
- **Dry run**: Validates workflow, estimates cost/time, identifies risks (no execution)
- **Real execution**: Executes agents, logs all inputs/outputs, captures errors
- **Execution trace**: Complete audit trail of every step
- **Cost tracking**: Actual cost vs estimated (variance < 20%)

**Success Criteria:**
- **Quantitative:**
  - Trace completeness: 100% agent executions logged
  - Cost estimation accuracy: ±20% of actual cost
  - Time estimation accuracy: ±30% of actual time
  - Error capture: 100% errors logged with context

- **Qualitative:**
  - Execution trace is human-readable
  - Dry run identifies realistic risks
  - Cost breakdown shows per-agent costs
  - Time breakdown shows bottlenecks

**Measurement Methods:**
1. Trace completeness: verify all agents logged
2. Estimation accuracy: compare dry run vs real execution
3. Error handling: inject errors, verify capture
4. Readability: user survey on trace understandability

**Edge Cases:**
1. **Agent crashes mid-execution** → Trace shows partial execution, error context
2. **Infinite loop** (circular connections) → Dry run detects, warns user
3. **Conditional branching** → Trace shows which path taken
4. **Parallel execution** → Trace shows temporal ordering

**Risk Analysis:**
- **Risk:** Incomplete traces hide execution details
- **Mitigation:** Atomic logging, fail-safe defaults (log before execution)
- **Detection:** Trace validation, audit log gaps

**Constitutional Checkpoint:**
- ✅ Glass-box transparency: Every execution step visible
- ✅ Inspectable: Full trace available for audit
- ✅ Graceful degradation: Partial execution logged even on failure

---

### Scenario 5.3: Glass-Box Explainability (Decision Trails)

**Setup:**
- Create workflow with conditional logic (if-then branching)
- Execute workflow multiple times with different inputs
- Explain why each execution took its specific path

**Action:**
```python
# Workflow with conditional logic
validator = AgentNode(
    id="validator",
    name="Input Validator",
    implementation="validate_input",
    output_schema=[
        AgentOutputSchema(name="is_valid", type="bool"),
        AgentOutputSchema(name="confidence", type="float")
    ]
)

# Branch 1: High confidence path
high_confidence_processor = AgentNode(
    id="high_conf_processor",
    name="Standard Processor",
    implementation="process_standard"
)

# Branch 2: Low confidence path (requires human review)
low_confidence_processor = AgentNode(
    id="low_conf_processor",
    name="Manual Review",
    implementation="process_manual",
    governance_rules=[
        GovernanceRule(
            rule_id="human_approval",
            rule_type="approval_required",
            constraint={"requires_human": True},
            action_on_violation="halt"
        )
    ]
)

workflow = AgentWorkflow(
    id="conditional_workflow",
    agents=[validator, high_confidence_processor, low_confidence_processor],
    connections=[
        AgentConnection(
            source="validator",
            target="high_conf_processor",
            condition="confidence >= 0.8"
        ),
        AgentConnection(
            source="validator",
            target="low_conf_processor",
            condition="confidence < 0.8"
        )
    ],
    entry_points=["validator"]
)

# Execute with high confidence input
context_1 = engine.execute_workflow(workflow, initial_inputs={"data": "clear_case"})

# Execute with low confidence input
context_2 = engine.execute_workflow(workflow, initial_inputs={"data": "ambiguous_case"})

# Explain decisions
explainer = WorkflowExplainer()

explanation_1 = explainer.explain_execution(context_1)
print("=== Execution 1: Clear case ===")
print(explanation_1.content)
# Expected: "Validator returned confidence=0.92 → Standard Processor (threshold: 0.8)"

explanation_2 = explainer.explain_execution(context_2)
print("\n=== Execution 2: Ambiguous case ===")
print(explanation_2.content)
# Expected: "Validator returned confidence=0.65 → Manual Review (threshold: 0.8)"
# "Human approval required (governance rule: human_approval)"
```

**Expected Behavior:**
- **Execution 1**: Validator outputs confidence=0.92 → takes high confidence path
- **Execution 2**: Validator outputs confidence=0.65 → takes low confidence path, halts for human approval
- **Explanations**: Clearly state why each path was taken, show threshold comparisons

**Success Criteria:**
- **Quantitative:**
  - Decision reasoning accuracy: 100% explanations match actual conditions
  - Explanation completeness: All decision points covered
  - Latency: <100ms to generate explanation from trace
  - Comprehension: 85%+ users understand why path taken

- **Qualitative:**
  - Explanations are specific (not generic)
  - Conditional logic is clearly stated
  - Thresholds and rules are visible
  - Alternative paths are mentioned

**Measurement Methods:**
1. Accuracy testing: verify explanations match execution trace
2. Completeness: check all decision points explained
3. Performance: benchmark explanation generation time
4. User testing: comprehension quiz on explanations

**Edge Cases:**
1. **No conditions met** (unreachable paths) → Dry run detects, warns user
2. **Multiple conditions true** (ambiguous branching) → Explain priority/order
3. **Dynamic conditions** (based on runtime state) → Show evaluated values

**Risk Analysis:**
- **Risk:** Explanations mislead users about execution logic
- **Mitigation:** Explanations generated from trace, not code comments
- **Detection:** Cross-check explanations vs execution trace

**Constitutional Checkpoint:**
- ✅ Glass-box: All decision logic visible and explainable
- ✅ Inspectable: Users can see conditions and thresholds
- ✅ Transparent: No hidden logic or magic branching

---

### Scenario 5.4: Governance Rule Enforcement (Cost Limits)

**Setup:**
- Create workflow with cost-sensitive agent (LLM calls)
- Set governance rule: max_cost = $2.00
- Execute workflow, trigger cost limit
- Verify enforcement and graceful handling

**Action:**
```python
# Define expensive agent
llm_agent = AgentNode(
    id="llm_agent",
    name="Multi-Shot LLM",
    agent_type=AgentType.EXECUTOR,
    implementation="multi_shot_llm",
    governance_rules=[
        GovernanceRule(
            rule_id="cost_limit",
            rule_type="cost_limit",
            constraint={"max_cost": 2.00},
            action_on_violation="halt"
        )
    ]
)

# Implementation makes 10 LLM calls @ $0.30 each = $3.00 total
def multi_shot_llm(inputs):
    results = []
    for i in range(10):
        # Each call costs $0.30
        result = llm_client.chat(
            model="gpt-4o",
            messages=[...],
            max_tokens=500
        )
        results.append(result)
    return {"results": results}

engine.register_agent_implementation("llm_agent", multi_shot_llm)

workflow = AgentWorkflow(
    id="expensive_workflow",
    agents=[llm_agent],
    connections=[],
    entry_points=["llm_agent"]
)

# Execute workflow
context = engine.execute_workflow(workflow, initial_inputs={})

print(f"Status: {context.status}")  # Expected: HALTED
print(f"Cost: ${context.total_cost}")  # Expected: ~$2.10 (stopped after 7 calls)
print(f"Errors: {context.errors}")  # Expected: CostLimitExceededError
```

**Expected Behavior:**
- Workflow starts execution
- After 7 LLM calls (~$2.10), cost limit exceeded
- Governance engine halts execution
- Error logged: "Cost limit exceeded: $2.10 > $2.00 (rule: cost_limit)"
- Context shows partial results (7 calls completed)

**Success Criteria:**
- **Quantitative:**
  - Enforcement accuracy: 100% violations detected and halted
  - Overshoot: <10% over limit (e.g., $2.10 vs $2.00 is 5% overshoot)
  - Detection latency: <100ms after limit breach
  - Graceful handling: 100% partial results preserved

- **Qualitative:**
  - Error message clearly states limit and actual cost
  - Partial results are usable (workflow didn't waste work)
  - User can adjust limit and retry
  - Alternative actions presented (e.g., "increase limit to $5?")

**Measurement Methods:**
1. Enforcement testing: trigger violations, verify halting
2. Overshoot measurement: track cost after halt vs limit
3. Latency benchmarking: time from breach to halt
4. User survey: clarity of error messages, recovery options

**Edge Cases:**
1. **Cost estimation unavailable** → Warn user, proceed with caution
2. **Parallel agent execution** → Aggregate cost, halt all when limit hit
3. **Limit hit mid-call** → Complete current call, then halt (avoid partial state)
4. **User override** → Require explicit confirmation, log override reason

**Risk Analysis:**
- **Risk:** Overshoot causes significant cost overrun
- **Mitigation:** Preemptive checks, buffer margin (e.g., halt at 95% of limit)
- **Detection:** Monitor overshoot percentage, adjust buffer

**Constitutional Checkpoint:**
- ✅ Graceful degradation: Partial results preserved, not discarded
- ✅ Transparent limits: Rule visible before execution (dry run shows it)
- ✅ User agency: Can adjust limit or cancel workflow

---

## Cross-Component Integration Scenarios

### Scenario 6.1: Mental Models → ARGUS Subconscious Integration

**Setup:**
- ARGUS detects performance degradation pattern
- Mental Model Library selects relevant models (`bottlenecks`, `compounding`)
- Subconscious generates hypotheses using mental model frameworks
- Explainability system presents findings at user's rung level

**Action:**
```python
# 1. ARGUS detects pattern
detector = PatternDetector(memory)
patterns = detector.detect_patterns(lookback_days=30)
perf_pattern = [p for p in patterns if p.type == PatternType.PERFORMANCE_DEGRADATION][0]

# 2. Mental Models select relevant frameworks
selector = MentalModelSelector()
models = selector.select_for_context(perf_pattern.description)

# 3. Subconscious generates hypotheses using models
generator = HypothesisGenerator()
hypotheses = generator.generate_from_pattern(perf_pattern, mental_models=models.models)

# 4. Explainability adapts to user
explainer = Explainer()
user_rung = 2  # Explorer
explanation = explainer.explain_pattern_and_hypotheses(
    pattern=perf_pattern,
    hypotheses=hypotheses,
    mental_models=models.models,
    growth_rung=user_rung
)

print(explanation.content)
```

**Expected Behavior:**
- Pattern detected: "Stage 3 latency increased 45% over 30 days"
- Mental models: `bottlenecks` (constraint analysis), `compounding` (cumulative effect)
- Hypotheses:
  1. "Bottleneck in Stage 3 validation (blocking I/O)"
  2. "Compounding data growth (processing time scales with data)"
- Explanation (Rung 2 - METAPHOR): "Think of Stage 3 like a highway toll booth..."

**Success Criteria:**
- **Integration correctness**: Pattern → Models → Hypotheses → Explanation pipeline works
- **Relevance**: Selected mental models appropriate for pattern type
- **Coherence**: Explanation references mental models naturally
- **User comprehension**: 80%+ users understand recommendation

**Constitutional Checkpoint:**
- ✅ End-to-end transparency: User can trace pattern → models → hypotheses → explanation
- ✅ User agency: User chooses which hypothesis to test

---

### Scenario 6.2: MNEMIS → LOOM → ARGUS Feedback Loop

**Setup:**
- MNEMIS stores pattern: "Stage 3 validation timeout → retry with longer threshold"
- LOOM creates workflow using MNEMIS suggestion
- Workflow executes, ARGUS monitors success
- Success outcome promoted back to MNEMIS (feedback loop)

**Action:**
```python
# 1. MNEMIS retrieves pattern
search_engine = MemorySearchEngine(store)
patterns = search_engine.search_by_tags(
    tags=["timeout", "validation"],
    contract=project_contract
)

timeout_pattern = patterns[0]  # "Increase timeout from 5s → 10s fixes 80% of errors"

# 2. LOOM applies pattern to workflow
workflow_builder = WorkflowBuilder()
workflow = workflow_builder.load("hart_os_pipeline")

# Apply MNEMIS suggestion
validator_agent = workflow.get_agent("validator")
validator_agent.config["timeout"] = timeout_pattern.content["suggested_timeout"]  # 10s

# 3. Execute workflow
engine = WorkflowEngine()
context = engine.execute_workflow(workflow, initial_inputs={...})

# 4. ARGUS monitors outcome
telemetry = WorkflowTelemetryHooks()
telemetry.log_workflow_complete(context)

# 5. Outcome analysis
if context.status == "SUCCESS" and context.error_count == 0:
    # Promote success to MNEMIS
    success_memory = store.write(
        content={
            "pattern_id": timeout_pattern.id,
            "outcome": "SUCCESS",
            "error_reduction": "100%",
            "confidence": 0.95
        },
        scope=controller.create_project_scope("hart_os"),
        contract=project_contract,
        tags=["success", "validation", "timeout"]
    )

    # Propose pattern reinforcement to GAIA tier
    promotion_engine.propose_promotion(
        memory_id=success_memory,
        to_scope=controller.create_gaia_scope(),
        rationale="Timeout pattern confirmed across HART OS executions"
    )
```

**Expected Behavior:**
- MNEMIS suggests timeout increase (based on past pattern)
- LOOM applies suggestion to workflow
- Workflow executes successfully (error rate drops 100%)
- ARGUS logs success
- Success outcome stored in MNEMIS
- Pattern promoted to GAIA tier (confirmed effective)

**Success Criteria:**
- **Feedback loop completeness**: MNEMIS → LOOM → ARGUS → MNEMIS cycle works
- **Outcome tracking**: Success/failure tied back to MNEMIS pattern
- **Pattern reinforcement**: Successful patterns gain confidence, promoted
- **Learning propagation**: Effective patterns shared ecosystem-wide

**Constitutional Checkpoint:**
- ✅ Explicit learning: Pattern application requires user approval
- ✅ Feedback transparency: Outcome tracked and attributable to pattern
- ✅ Promotion discipline: Successful patterns promoted via proposal

---

## User Feedback Collection

### Survey Instrument (Post-Testing)

**For each scenario, collect:**

1. **Functional Correctness** (Scale: 1-10)
   - "Did the component behave as expected?"

2. **Usefulness** (Scale: 1-10)
   - "Would this feature help your workflow?"

3. **Clarity** (Scale: 1-10)
   - "Were explanations/outputs easy to understand?"

4. **Trust** (Scale: 1-10)
   - "Do you trust the system's recommendations?"

5. **Constitutional Compliance** (Binary: Yes/No + Comments)
   - "Did you observe any violations of GAIA principles?"
   - If yes: Describe violation

6. **Qualitative Feedback** (Open-ended)
   - "What worked well?"
   - "What needs improvement?"
   - "Any unexpected behavior?"

### Validation Checkpoints

**Weekly review:**
- Quantitative metrics: Track against success criteria
- Qualitative themes: Cluster user feedback
- Constitutional compliance: Review violations
- Risk mitigation: Adjust thresholds/policies

**Go/No-Go criteria:**
- 80%+ scenarios meet quantitative success criteria
- 0 unresolved constitutional violations
- 75%+ user satisfaction (average of Usefulness + Trust)
- All edge cases documented and handled

---

## Appendix: Measurement Tools

### Automated Testing Infrastructure

```python
# test_validation_scenarios.py

import pytest
from validation_scenarios import *

@pytest.mark.parametrize("scenario", [
    "mental_models_context_selection",
    "mental_models_explanation_levels",
    "argus_pattern_detection",
    "argus_hypothesis_generation",
    "mnemis_promotion_workflow",
    "mnemis_access_control",
    "loom_authority_validation",
    "loom_execution_transparency"
])
def test_scenario(scenario):
    """Run scenario and validate success criteria"""
    scenario_runner = ScenarioRunner()
    results = scenario_runner.run(scenario)

    # Quantitative checks
    assert results.metrics["accuracy"] >= results.success_criteria["accuracy"]
    assert results.metrics["latency"] <= results.success_criteria["max_latency"]

    # Constitutional compliance
    assert results.constitutional_violations == []

    # Qualitative checks (require human review)
    if results.requires_human_validation:
        print(f"⚠️  Scenario {scenario} requires human validation")
        print(f"Review: {results.validation_url}")
```

### Metrics Dashboard

**Real-time tracking:**
- Scenario pass/fail rates
- Success criteria attainment (%)
- User satisfaction scores
- Constitutional violations (count + severity)
- Edge case coverage (%)

**Export formats:**
- JSON (machine-readable)
- Markdown (human-readable reports)
- CSV (spreadsheet analysis)

---

## Document Maintenance

**Ownership:** GAIA Validation Team
**Review Cadence:** Weekly during Phase 2/3 implementation
**Update Trigger:** New scenarios added, success criteria adjusted, edge cases discovered
**Versioning:** Semantic versioning (1.0.0 → 1.1.0 for new scenarios, 1.0.0 → 1.0.1 for criteria adjustments)

---

**Last Updated:** February 4, 2026
**Next Review:** February 11, 2026
**Status:** Active validation in progress
