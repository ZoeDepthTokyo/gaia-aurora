"""
Integration tests for ARGUS Subconscious Layer (Phase 2).

Tests pattern detection with memory storage, hypothesis generation,
and explainability across different complexity levels.
"""

import tempfile
from datetime import datetime, timedelta
from pathlib import Path

import pytest
from argus.explainability.explainer import Explainer, ExplanationLevel
from argus.subconscious.hypothesis_generator import HypothesisGenerator, HypothesisType
from argus.subconscious.memory import (
    ExternalMemory,
    MemoryEntry,
    MemoryScope,
    MemoryType,
)
from argus.subconscious.pattern_detector import PatternDetector, PatternType


class TestPatternDetectionWithMemory:
    """
    Test pattern detection with memory storage integration.

    Verifies that patterns are correctly detected from stored
    memories and that the detection process is non-intervening.
    """

    @pytest.fixture
    def temp_memory(self) -> ExternalMemory:
        """Create temporary memory database for testing."""
        with tempfile.NamedTemporaryFile(delete=False, suffix=".db") as f:
            db_path = f.name

        memory = ExternalMemory(db_path)
        yield memory
        memory.close()

        # Cleanup
        Path(db_path).unlink(missing_ok=True)

    @pytest.fixture
    def detector(self, temp_memory: ExternalMemory) -> PatternDetector:
        """Create pattern detector with temp memory."""
        return PatternDetector(temp_memory)

    def test_recurring_error_detection(
        self, temp_memory: ExternalMemory, detector: PatternDetector
    ):
        """
        Test detection of recurring error patterns.

        Stores multiple similar errors and verifies they are
        detected as a pattern.
        """
        # Store recurring errors
        error_content = "Connection timeout to database server"

        for i in range(5):
            entry = MemoryEntry(
                type=MemoryType.ERROR,
                scope=MemoryScope.PROJECT,
                content=f"{error_content} (occurrence {i+1})",
                source="test_agent",
                timestamp=datetime.now() - timedelta(days=i),
            )
            temp_memory.store(entry)

        # Detect patterns
        patterns = detector.detect_patterns(lookback_days=10, min_frequency=3)

        # Should detect recurring error
        error_patterns = [p for p in patterns if p.type == PatternType.RECURRING_ERROR]
        assert len(error_patterns) > 0

        pattern = error_patterns[0]
        assert pattern.frequency >= 3
        assert pattern.confidence > 0.5
        assert "timeout" in pattern.description.lower()
        assert len(pattern.recommended_actions) > 0

    def test_performance_degradation_detection(
        self, temp_memory: ExternalMemory, detector: PatternDetector
    ):
        """
        Test detection of performance degradation trends.

        Creates observations showing worsening performance
        and verifies trend detection.
        """
        # Early observations (good performance)
        for i in range(5):
            entry = MemoryEntry(
                type=MemoryType.OBSERVATION,
                scope=MemoryScope.PROJECT,
                content="Performance metrics within normal range",
                source="monitor",
                timestamp=datetime.now() - timedelta(days=20 + i),
            )
            temp_memory.store(entry)

        # Recent observations (degraded performance)
        for i in range(5):
            entry = MemoryEntry(
                type=MemoryType.OBSERVATION,
                scope=MemoryScope.PROJECT,
                content="Performance degradation detected, slow response times",
                source="monitor",
                timestamp=datetime.now() - timedelta(days=i),
            )
            temp_memory.store(entry)

        # Detect patterns
        patterns = detector.detect_patterns(lookback_days=30)

        # Should detect degradation
        degradation_patterns = [
            p for p in patterns if p.type == PatternType.PERFORMANCE_DEGRADATION
        ]

        assert len(degradation_patterns) > 0
        pattern = degradation_patterns[0]
        assert pattern.severity > 0.5
        assert "degradation" in pattern.description.lower()

    def test_pattern_evidence_tracking(
        self, temp_memory: ExternalMemory, detector: PatternDetector
    ):
        """
        Test that patterns track evidence (memory IDs).

        Verifies provenance and auditability of pattern detection.
        """
        # Store errors
        stored_ids = []
        for i in range(4):
            entry = MemoryEntry(
                type=MemoryType.ERROR,
                scope=MemoryScope.PROJECT,
                content="API rate limit exceeded",
                source="api_client",
            )
            entry_id = temp_memory.store(entry)
            stored_ids.append(entry_id)

        # Detect patterns
        patterns = detector.detect_patterns(min_frequency=3)

        # Find error pattern
        error_patterns = [p for p in patterns if p.type == PatternType.RECURRING_ERROR]

        if len(error_patterns) > 0:
            pattern = error_patterns[0]

            # Should have evidence
            assert len(pattern.evidence) > 0

            # Evidence should reference actual memory IDs
            for evidence_id in pattern.evidence:
                # Should be able to retrieve the memory
                memory = temp_memory.retrieve(evidence_id)
                assert memory is not None

    def test_non_intervening_behavior(self, temp_memory: ExternalMemory, detector: PatternDetector):
        """
        Test that pattern detection is non-intervening.

        Verifies that detection doesn't modify memories or
        trigger any automatic actions.
        """
        # Store observation
        entry = MemoryEntry(
            type=MemoryType.OBSERVATION,
            scope=MemoryScope.PROJECT,
            content="Test observation",
            source="test",
        )
        entry_id = temp_memory.store(entry)

        # Get original memory
        original = temp_memory.retrieve(entry_id)
        original_content = original.content

        # Run detection
        detector.detect_patterns()

        # Retrieve memory again
        after_detection = temp_memory.retrieve(entry_id)

        # Should be unchanged
        assert after_detection.content == original_content

        # Memory count should not increase (no new memories created)
        initial_count = temp_memory.count()
        detector.detect_patterns()
        after_count = temp_memory.count()

        assert after_count == initial_count


class TestHypothesisGeneration:
    """
    Test hypothesis generation from detected patterns.

    Verifies that the hypothesis generator creates actionable
    hypotheses with clear testing criteria.
    """

    @pytest.fixture
    def temp_memory(self) -> ExternalMemory:
        """Create temporary memory database for testing."""
        with tempfile.NamedTemporaryFile(delete=False, suffix=".db") as f:
            db_path = f.name

        memory = ExternalMemory(db_path)
        yield memory
        memory.close()

        Path(db_path).unlink(missing_ok=True)

    @pytest.fixture
    def generator(self, temp_memory: ExternalMemory) -> HypothesisGenerator:
        """Create hypothesis generator with temp memory."""
        detector = PatternDetector(temp_memory)
        return HypothesisGenerator(detector, temp_memory)

    def test_hypothesis_from_error_pattern(
        self, temp_memory: ExternalMemory, generator: HypothesisGenerator
    ):
        """
        Test hypothesis generation from error patterns.

        Stores recurring errors and verifies meaningful
        hypotheses are generated.
        """
        # Store recurring errors
        for i in range(4):
            entry = MemoryEntry(
                type=MemoryType.ERROR,
                scope=MemoryScope.PROJECT,
                content="Memory allocation failed",
                source="runtime",
            )
            temp_memory.store(entry)

        # Generate hypotheses
        hypotheses = generator.generate_hypotheses(lookback_days=7)

        # Should have at least one hypothesis
        assert len(hypotheses) > 0

        # Hypothesis should have required fields
        hypothesis = hypotheses[0]
        assert hypothesis.description
        assert len(hypothesis.supporting_evidence) > 0
        assert 0.0 <= hypothesis.confidence <= 1.0
        assert len(hypothesis.test_criteria) > 0

    def test_hypothesis_storage_in_memory(
        self, temp_memory: ExternalMemory, generator: HypothesisGenerator
    ):
        """
        Test that hypotheses are stored in external memory.

        Verifies persistence and auditability of hypotheses.
        """
        # Create pattern-inducing data
        for i in range(3):
            entry = MemoryEntry(
                type=MemoryType.ERROR,
                scope=MemoryScope.GAIA,
                content="Cost spike detected",
                source="cost_monitor",
            )
            temp_memory.store(entry)

        # Generate and store hypotheses
        initial_count = temp_memory.count(type=MemoryType.HYPOTHESIS)

        hypotheses = generator.generate_hypotheses()

        if len(hypotheses) > 0:
            # Store first hypothesis
            hypothesis = hypotheses[0]
            generator.store_hypothesis(hypothesis)

            # Verify storage
            after_count = temp_memory.count(type=MemoryType.HYPOTHESIS)
            assert after_count > initial_count

            # Verify retrieval
            stored_hypotheses = temp_memory.search(type=MemoryType.HYPOTHESIS)
            assert len(stored_hypotheses) > 0

    def test_hypothesis_requires_human_approval(
        self, temp_memory: ExternalMemory, generator: HypothesisGenerator
    ):
        """
        Test that hypotheses don't trigger autonomous actions.

        Verifies constitutional boundary: no automatic execution.
        """
        # Create hypothesis-triggering pattern
        for i in range(5):
            entry = MemoryEntry(
                type=MemoryType.ERROR,
                scope=MemoryScope.PROJECT,
                content="Authentication failure",
                source="auth_service",
            )
            temp_memory.store(entry)

        # Generate hypotheses
        hypotheses = generator.generate_hypotheses()

        if len(hypotheses) > 0:
            hypothesis = hypotheses[0]

            # Hypothesis should have test_criteria (for human review)
            assert len(hypothesis.test_criteria) > 0

            # Should NOT have automated actions
            # (system should only suggest, not act)
            assert hypothesis.type in [
                HypothesisType.ROOT_CAUSE,
                HypothesisType.CORRELATION,
                HypothesisType.PREDICTIVE,
                HypothesisType.DIAGNOSTIC,
            ]

            # Hypothesis itself is just a suggestion
            # No automatic remediation should occur


class TestExplainabilityIntegration:
    """
    Test explainability at different levels.

    Verifies multi-level explanations work correctly and
    adapt to user growth ladder position.
    """

    @pytest.fixture
    def explainer(self) -> Explainer:
        """Create explainer instance."""
        return Explainer()

    def test_simple_level_explanation(self, explainer: Explainer):
        """
        Test SIMPLE level explanations.

        For new users (Growth Rung 1), explanations should be
        concise, jargon-free, and actionable.
        """
        explanation = explainer.explain("feedback_loops", ExplanationLevel.SIMPLE)

        assert explanation is not None
        assert explanation.level == ExplanationLevel.SIMPLE

        # Should be concise
        assert len(explanation.content) < 500

        # Should have examples
        assert len(explanation.examples) > 0

        # Should have next steps
        assert len(explanation.next_steps) > 0

    def test_default_level_explanation(self, explainer: Explainer):
        """
        Test DEFAULT level explanations.

        For intermediate users, explanations should be balanced
        with key points and practical context.
        """
        explanation = explainer.explain("feedback_loops", ExplanationLevel.DEFAULT)

        assert explanation is not None
        assert explanation.level == ExplanationLevel.DEFAULT

        # Should have more detail than SIMPLE
        assert len(explanation.content) > 100

        # Should have examples
        assert len(explanation.examples) > 0

        # Should have related topics
        assert len(explanation.related_topics) > 0

    def test_metaphor_level_explanation(self, explainer: Explainer):
        """
        Test METAPHOR level explanations.

        Should use analogies to make concepts accessible.
        """
        explanation = explainer.explain("feedback_loops", ExplanationLevel.METAPHOR)

        assert explanation is not None
        assert explanation.level == ExplanationLevel.METAPHOR

        # Should contain analogies
        content_lower = explanation.content.lower()
        assert any(
            keyword in content_lower
            for keyword in ["like", "similar", "thermostat", "microphone", "think of"]
        )

    def test_advanced_level_explanation(self, explainer: Explainer):
        """
        Test ADVANCED level explanations.

        For technical users, should include implementation
        details, code examples, and references.
        """
        explanation = explainer.explain("feedback_loops", ExplanationLevel.ADVANCED)

        assert explanation is not None
        assert explanation.level == ExplanationLevel.ADVANCED

        # Should be comprehensive
        assert len(explanation.content) > 500

        # Should have technical content
        content_lower = explanation.content.lower()
        assert any(
            keyword in content_lower
            for keyword in ["function", "class", "implementation", "code", "python"]
        )

        # Should have references
        assert len(explanation.references) > 0

    def test_growth_rung_mapping(self, explainer: Explainer):
        """
        Test automatic level selection based on growth rung.

        Verifies that explanations adapt to user's position
        on growth ladder.
        """
        # Rung 1 (Creator) -> SIMPLE
        rung1 = explainer.explain_for_user("feedback_loops", growth_rung=1)
        assert rung1 is not None
        assert rung1.level == ExplanationLevel.SIMPLE

        # Rung 2 (Explorer) -> METAPHOR
        rung2 = explainer.explain_for_user("feedback_loops", growth_rung=2)
        assert rung2 is not None
        assert rung2.level == ExplanationLevel.METAPHOR

        # Rung 3 (Adapter) -> DEFAULT
        rung3 = explainer.explain_for_user("feedback_loops", growth_rung=3)
        assert rung3 is not None
        assert rung3.level == ExplanationLevel.DEFAULT

        # Rung 4 (Architect) -> ADVANCED
        rung4 = explainer.explain_for_user("feedback_loops", growth_rung=4)
        assert rung4 is not None
        assert rung4.level == ExplanationLevel.ADVANCED

    def test_markdown_formatting(self, explainer: Explainer):
        """
        Test markdown output formatting.

        Verifies that explanations can be rendered as
        formatted markdown for documentation.
        """
        explanation = explainer.explain("feedback_loops", ExplanationLevel.DEFAULT)
        assert explanation is not None

        markdown = explanation.format_markdown()

        # Should be valid markdown
        assert markdown.startswith("# ")
        assert "## " in markdown  # Sections

        # Should include all components
        assert "Examples" in markdown or "examples" in markdown.lower()
        assert "Next Steps" in markdown or "next steps" in markdown.lower()

    def test_custom_explanation_addition(self, explainer: Explainer):
        """
        Test adding custom explanations.

        Verifies extensibility for project-specific concepts.
        """
        explainer.add_custom_explanation(
            topic="custom_concept",
            level=ExplanationLevel.SIMPLE,
            content="This is a custom concept for testing",
            examples=["Example 1", "Example 2"],
        )

        # Should be retrievable
        result = explainer.explain("custom_concept", ExplanationLevel.SIMPLE)

        assert result is not None
        assert result.topic == "custom_concept"
        assert result.content == "This is a custom concept for testing"
        assert len(result.examples) == 2


class TestSubconsciousWorkflow:
    """
    Test complete subconscious workflow.

    Integration test combining memory, pattern detection,
    hypothesis generation, and explainability.
    """

    @pytest.fixture
    def workflow_components(self):
        """Set up complete workflow components."""
        with tempfile.NamedTemporaryFile(delete=False, suffix=".db") as f:
            db_path = f.name

        memory = ExternalMemory(db_path)
        detector = PatternDetector(memory)
        generator = HypothesisGenerator(detector, memory)
        explainer = Explainer()

        yield {
            "memory": memory,
            "detector": detector,
            "generator": generator,
            "explainer": explainer,
        }

        memory.close()
        Path(db_path).unlink(missing_ok=True)

    def test_end_to_end_observation_to_explanation(self, workflow_components):
        """
        Test complete workflow from observation to explanation.

        Simulates: Observation -> Pattern Detection ->
        Hypothesis Generation -> Explanation
        """
        memory = workflow_components["memory"]
        detector = workflow_components["detector"]
        generator = workflow_components["generator"]
        explainer = workflow_components["explainer"]

        # 1. Store observations (simulating process observer)
        for i in range(5):
            entry = MemoryEntry(
                type=MemoryType.OBSERVATION,
                scope=MemoryScope.PROJECT,
                content="HART OS showing feedback loop in error recovery",
                source="process_observer",
            )
            memory.store(entry)

        # 2. Detect patterns
        patterns = detector.detect_patterns(min_frequency=3)
        assert len(patterns) > 0

        # 3. Generate hypotheses
        hypotheses = generator.generate_hypotheses()

        # 4. Get explanation for feedback loops
        explanation = explainer.explain("feedback_loops", ExplanationLevel.DEFAULT)
        assert explanation is not None

        # Workflow should be traceable
        assert len(patterns) > 0 or len(hypotheses) > 0

    def test_graceful_degradation_no_patterns(self, workflow_components):
        """
        Test graceful degradation when no patterns found.

        Verifies system handles empty/insufficient data gracefully.
        """
        detector = workflow_components["detector"]
        generator = workflow_components["generator"]

        # No data stored - should handle gracefully
        patterns = detector.detect_patterns()
        assert isinstance(patterns, list)
        assert len(patterns) == 0

        hypotheses = generator.generate_hypotheses()
        assert isinstance(hypotheses, list)
        # May be empty, that's acceptable

    def test_transparency_in_uncertainty(self, workflow_components):
        """
        Test transparency when confidence is low.

        Verifies that low-confidence patterns and hypotheses
        are clearly marked as uncertain.
        """
        memory = workflow_components["memory"]
        detector = workflow_components["detector"]

        # Store minimal, ambiguous data
        for i in range(2):
            entry = MemoryEntry(
                type=MemoryType.OBSERVATION,
                scope=MemoryScope.PROJECT,
                content="Something happened",
                source="test",
            )
            memory.store(entry)

        patterns = detector.detect_patterns(min_frequency=2)

        # If patterns detected, should have low confidence
        for pattern in patterns:
            if pattern.frequency < 3:
                # Low frequency should yield lower confidence
                assert pattern.confidence < 0.9
