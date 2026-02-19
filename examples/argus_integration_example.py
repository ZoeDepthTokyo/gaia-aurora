"""
ARGUS Phase 2 Integration Example.

Demonstrates complete workflow:
1. External memory storage
2. Pattern detection
3. Hypothesis generation
4. Mental model selection
5. Context enrichment
6. Layered explanation

This example shows how all components work together.
"""

import sys
from datetime import datetime, timedelta
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from argus.explainability import Explainer, ExplanationLevel
from argus.subconscious import (
    ContextEnricher,
    ExternalMemory,
    HypothesisGenerator,
    MemoryEntry,
    MemoryScope,
    MemoryType,
    PatternDetector,
)

from mental_models import MentalModelSelector


def main():
    """Run complete ARGUS integration example."""

    print("=" * 80)
    print("ARGUS Phase 2 Integration Example")
    print("=" * 80)
    print()

    # =========================================================================
    # Step 1: Initialize Components
    # =========================================================================
    print("Step 1: Initializing components...")
    print("-" * 80)

    # Create temporary memory database
    memory_path = Path(__file__).parent / "example_memory.db"
    memory = ExternalMemory(str(memory_path))

    pattern_detector = PatternDetector(memory)
    hypothesis_generator = HypothesisGenerator()
    context_enricher = ContextEnricher(memory)
    model_selector = MentalModelSelector()
    explainer = Explainer()

    print(f"✓ External memory initialized: {memory_path}")
    print("✓ Pattern detector ready")
    print("✓ Hypothesis generator ready")
    print("✓ Context enricher ready")
    print(f"✓ Mental model selector ready ({len(model_selector.models)} models)")
    print("✓ Explainer ready")
    print()

    # =========================================================================
    # Step 2: Simulate Observations
    # =========================================================================
    print("Step 2: Storing observations in external memory...")
    print("-" * 80)

    # Simulate HART OS confidence score observations over 30 days
    base_time = datetime.now() - timedelta(days=30)

    observations = [
        ("HART OS Stage 3 confidence score: 0.85", 0, 0.85),
        ("HART OS Stage 3 confidence score: 0.84", 5, 0.84),
        ("HART OS Stage 3 confidence score: 0.82", 10, 0.82),
        ("HART OS Stage 3 confidence score: 0.80", 15, 0.80),
        ("HART OS Stage 3 confidence score: 0.78", 20, 0.78),
        ("HART OS Stage 3 confidence score: 0.78", 25, 0.78),
    ]

    for content, days_offset, confidence in observations:
        entry = MemoryEntry(
            type=MemoryType.OBSERVATION,
            scope=MemoryScope.PROJECT,
            content=content,
            source="hart_os",
            confidence=confidence,
            tags=["hart_os", "confidence", "stage_3"],
            context={"project": "hart_os", "stage": 3},
        )
        entry.timestamp = base_time + timedelta(days=days_offset)
        memory.store(entry)

    print(f"✓ Stored {len(observations)} observations")

    # Add some error observations
    errors = [
        "Stage 3 failed: confidence below threshold (0.75)",
        "Stage 3 retry: still below threshold",
        "Stage 3 failed: confidence below threshold (0.75)",
    ]

    for error_content in errors:
        entry = MemoryEntry(
            type=MemoryType.ERROR,
            scope=MemoryScope.PROJECT,
            content=error_content,
            source="hart_os",
            confidence=1.0,
            tags=["hart_os", "error", "stage_3"],
        )
        entry.timestamp = datetime.now() - timedelta(days=3)
        memory.store(entry)

    print(f"✓ Stored {len(errors)} error observations")
    print()

    # =========================================================================
    # Step 3: Detect Patterns
    # =========================================================================
    print("Step 3: Detecting patterns...")
    print("-" * 80)

    patterns = pattern_detector.detect_patterns(
        lookback_days=30, min_frequency=2, min_confidence=0.5
    )

    print(f"✓ Detected {len(patterns)} patterns")
    print()

    for i, pattern in enumerate(patterns, 1):
        print(f"Pattern {i}: {pattern.type.value}")
        print(f"  Description: {pattern.description}")
        print(f"  Confidence: {pattern.confidence:.0%}")
        print(f"  Severity: {pattern.severity:.0%}")
        print(f"  Frequency: {pattern.frequency}")
        print(f"  Evidence: {len(pattern.evidence)} memory entries")
        print("  Recommended actions:")
        for action in pattern.recommended_actions:
            print(f"    - {action}")
        print()

    # =========================================================================
    # Step 4: Generate Hypotheses
    # =========================================================================
    if patterns:
        print("Step 4: Generating hypotheses...")
        print("-" * 80)

        for pattern in patterns[:2]:  # First 2 patterns
            hypotheses = hypothesis_generator.generate_from_pattern(pattern)

            print(f"Hypotheses for pattern: {pattern.type.value}")
            print()

            for i, hyp in enumerate(hypotheses, 1):
                print(f"  Hypothesis {i}: {hyp.description}")
                print(f"    Confidence: {hyp.confidence:.0%}")
                print(f"    Status: {hyp.status.value}")
                print(f"    Proposed test: {hyp.proposed_test}")
                print("    Implications:")
                for impl in hyp.implications[:3]:  # First 3
                    print(f"      - {impl}")
                print()

    # =========================================================================
    # Step 5: Select Mental Models
    # =========================================================================
    print("Step 5: Selecting appropriate mental models...")
    print("-" * 80)

    # Use the first pattern's description as context
    if patterns:
        context = patterns[0].description
    else:
        context = "confidence scores declining over time"

    result = model_selector.select_for_context(context=context, max_models=5, min_confidence=0.5)

    print(f"Context: {context}")
    print(f"Overall confidence: {result.confidence:.0%}")
    print(f"Rationale: {result.rationale}")
    print()
    print(f"Selected {len(result.models)} mental models:")
    print()

    for i, model in enumerate(result.models, 1):
        print(f"  {i}. {model.name} ({model.category.value})")
        print(f"     {model.description}")
        print(f"     Output format: {model.output_format}")
        print()

    # =========================================================================
    # Step 6: Enrich Context
    # =========================================================================
    print("Step 6: Enriching context...")
    print("-" * 80)

    enriched = context_enricher.enrich_for_observation(
        observation="HART OS confidence scores declining",
        project="hart_os",
        lookback_days=30,
    )

    print(f"Enriched context for: {enriched['observation']}")
    print(f"Keywords: {', '.join(enriched['keywords'])}")
    print()
    print(f"Related observations: {len(enriched['related_observations'])}")
    print(f"Related patterns: {len(enriched['related_patterns'])}")
    print(f"Related errors: {len(enriched['related_errors'])}")
    print()
    print("Temporal context:")
    print(f"  Span: {enriched['temporal_context']['span_days']} days")
    print(f"  Trend: {enriched['temporal_context']['trend']}")
    print(f"  Total entries: {enriched['temporal_context']['total_entries']}")
    print()

    # =========================================================================
    # Step 7: Generate Layered Explanations
    # =========================================================================
    print("Step 7: Generating explanations at different levels...")
    print("-" * 80)

    # Explain feedback loops at different levels
    levels = [
        (ExplanationLevel.SIMPLE, "Beginner (Growth Rung 1)"),
        (ExplanationLevel.METAPHOR, "Intermediate (Growth Rung 2)"),
        (ExplanationLevel.DEFAULT, "Proficient (Growth Rung 3)"),
        (ExplanationLevel.ADVANCED, "Expert (Growth Rung 4-5)"),
    ]

    for level, audience in levels:
        explanation = explainer.explain("feedback_loops", level)

        if explanation:
            print(f"{audience}:")
            print(f"  {explanation.content[:200]}...")
            if explanation.examples:
                print(f"  Examples: {len(explanation.examples)}")
            print()

    # =========================================================================
    # Step 8: Summary Report
    # =========================================================================
    print("=" * 80)
    print("Summary Report")
    print("=" * 80)
    print()

    total_memories = memory.count()
    observations_count = memory.count(type=MemoryType.OBSERVATION)
    errors_count = memory.count(type=MemoryType.ERROR)

    print("External Memory:")
    print(f"  Total entries: {total_memories}")
    print(f"  Observations: {observations_count}")
    print(f"  Errors: {errors_count}")
    print()

    print("Pattern Detection:")
    print(f"  Patterns detected: {len(patterns)}")
    if patterns:
        print(f"  Highest severity: {max(p.severity for p in patterns):.0%}")
    print()

    print("Mental Models:")
    print(f"  Models selected: {len(result.models)}")
    print(f"  Selection confidence: {result.confidence:.0%}")
    print()

    print("Context Enrichment:")
    print(
        f"  Related context items: {len(enriched['related_observations']) + len(enriched['related_patterns'])}"
    )
    print(f"  Temporal trend: {enriched['temporal_context']['trend']}")
    print()

    # =========================================================================
    # Cleanup
    # =========================================================================
    print("Cleaning up...")
    memory.close()
    if memory_path.exists():
        memory_path.unlink()
    print("✓ Temporary database removed")
    print()

    print("=" * 80)
    print("ARGUS Phase 2 Integration Example Complete")
    print("=" * 80)


if __name__ == "__main__":
    main()
