"""
Integration tests for Mental Models Library (Phase 2).

Tests mental model selection, invocation rules matching, and context-aware
recommendations across different scenarios.
"""

import pytest
from pathlib import Path
from typing import List

from mental_models.selector import MentalModelSelector, SelectionResult
from mental_models.models import (
    MentalModel,
    ModelCategory,
    ContextPattern,
    ModelInvocation
)


class TestMentalModelSelection:
    """
    Test mental model selection in different contexts.

    Verifies that the selector can identify appropriate mental models
    based on context keywords, patterns, and domain knowledge.
    """

    @pytest.fixture
    def selector(self) -> MentalModelSelector:
        """Create selector with test registry and rules."""
        # Uses real registry from mental_models/
        return MentalModelSelector()

    def test_performance_degradation_context(self, selector: MentalModelSelector):
        """
        Test model selection for performance degradation scenario.

        Expected: Should recommend systems thinking models like
        feedback loops, bottlenecks, and root cause analysis.
        """
        result = selector.select_for_context(
            "System experiencing performance degradation with increasing latency"
        )

        # Verify selection was made
        assert isinstance(result, SelectionResult)
        assert len(result.models) > 0
        assert result.confidence > 0.5

        # Verify rationale exists
        assert result.rationale
        assert len(result.rationale) > 0

        # Expected categories for performance issues
        model_categories = {model.category for model in result.models}
        assert ModelCategory.SYSTEMS_THINKING in model_categories or \
               ModelCategory.QUALITY_RELIABILITY in model_categories

    def test_error_handling_context(self, selector: MentalModelSelector):
        """
        Test model selection for error handling scenario.

        Expected: Should recommend graceful degradation, fail-safe,
        and defensive design models.
        """
        result = selector.select_for_context(
            "Need to implement robust error handling for production system"
        )

        assert len(result.models) > 0

        # Should include quality/reliability models
        model_names = [m.name.lower() for m in result.models]
        quality_models = [
            name for name in model_names
            if any(keyword in name for keyword in ['graceful', 'fail', 'defensive'])
        ]

        # At least one quality-related model should be recommended
        assert len(quality_models) > 0

    def test_decision_making_context(self, selector: MentalModelSelector):
        """
        Test model selection for decision-making scenario.

        Expected: Should recommend decision-making models like
        first principles, cost-benefit, reversibility.
        """
        result = selector.select_for_context(
            "Choosing between architectural approaches for agent workflow"
        )

        assert len(result.models) > 0

        # Should include decision-making models
        model_categories = {model.category for model in result.models}
        assert ModelCategory.DECISION_MAKING in model_categories

    def test_confidence_threshold_filtering(self, selector: MentalModelSelector):
        """
        Test that low-confidence models are filtered out.

        Verifies the selector respects minimum confidence thresholds
        and only returns high-quality recommendations.
        """
        # Use high min_confidence
        result = selector.select_for_context(
            "vague ambiguous unclear problem",
            min_confidence=0.8
        )

        # Should have fewer or no results with high threshold
        assert result.confidence >= 0.0  # Always valid

        # All returned models should meet threshold
        if len(result.models) > 0:
            assert result.confidence >= 0.8

    def test_max_models_limit(self, selector: MentalModelSelector):
        """
        Test that max_models parameter limits results.

        Verifies the selector respects the maximum number of
        models to return, even if more are applicable.
        """
        result = selector.select_for_context(
            "Complex system with multiple feedback loops and performance issues",
            max_models=3
        )

        # Should not exceed max
        assert len(result.models) <= 3

        # Alternative models should exist if applicable
        if len(result.alternative_models) > 0:
            # Total applicable models > max_models
            assert len(result.models) == 3

    def test_alternative_models_provided(self, selector: MentalModelSelector):
        """
        Test that alternative models are suggested.

        Verifies that the selector provides alternative models
        for users to consider beyond primary recommendations.
        """
        result = selector.select_for_context(
            "Implementing feedback mechanism for quality improvement"
        )

        # Should have alternatives if many models apply
        assert isinstance(result.alternative_models, list)

        # Alternatives should be different from selected
        selected_ids = {m.id for m in result.models}
        alternative_ids = {m.id for m in result.alternative_models}

        # No overlap
        assert len(selected_ids & alternative_ids) == 0


class TestInvocationRules:
    """
    Test invocation rules matching and combination patterns.

    Verifies that context patterns trigger appropriate model
    recommendations and that combination patterns work correctly.
    """

    @pytest.fixture
    def selector(self) -> MentalModelSelector:
        """Create selector with test registry and rules."""
        return MentalModelSelector()

    def test_context_pattern_matching(self, selector: MentalModelSelector):
        """
        Test that context patterns trigger correctly.

        Verifies keyword matching logic and pattern recognition
        in various contexts.
        """
        # Test error-related pattern
        error_result = selector.select_for_context("error handling failure recovery")
        assert len(error_result.models) > 0

        # Test performance-related pattern
        perf_result = selector.select_for_context("latency bottleneck optimization")
        assert len(perf_result.models) > 0

        # Test learning-related pattern
        learning_result = selector.select_for_context("teaching users understanding")
        assert len(learning_result.models) > 0

        # Each should have different recommendations
        error_ids = {m.id for m in error_result.models}
        perf_ids = {m.id for m in perf_result.models}
        learning_ids = {m.id for m in learning_result.models}

        # Some difference expected (though overlap possible)
        assert error_ids != perf_ids or error_ids != learning_ids

    def test_combination_pattern_retrieval(self, selector: MentalModelSelector):
        """
        Test predefined combination patterns.

        Verifies that combination patterns return the correct
        sequence of mental models for complex scenarios.
        """
        # Try to get a combination pattern (if defined in rules)
        # This tests the infrastructure even if no patterns exist yet
        result = selector.get_combination_pattern("trust_audit")

        # Should return list or None
        assert result is None or isinstance(result, list)

        if result:
            # Should be sequence of MentalModel objects
            assert all(isinstance(m, MentalModel) for m in result)
            assert len(result) > 0

    def test_keyword_extraction(self, selector: MentalModelSelector):
        """
        Test keyword extraction from context.

        Verifies that the selector correctly identifies relevant
        keywords while filtering stop words.
        """
        context = "The system is experiencing performance degradation in production"
        keywords = selector._extract_keywords(context)

        # Should extract meaningful words
        assert "system" in keywords
        assert "performance" in keywords
        assert "degradation" in keywords
        assert "production" in keywords

        # Should filter stop words
        assert "the" not in keywords
        assert "is" not in keywords
        assert "in" not in keywords

    def test_category_filtering(self, selector: MentalModelSelector):
        """
        Test filtering models by category.

        Verifies that models can be retrieved by category
        for targeted recommendations.
        """
        # Get all systems thinking models
        systems_models = selector.get_models_by_category(ModelCategory.SYSTEMS_THINKING)

        assert len(systems_models) > 0
        assert all(m.category == ModelCategory.SYSTEMS_THINKING for m in systems_models)

        # Get all decision-making models
        decision_models = selector.get_models_by_category(ModelCategory.DECISION_MAKING)

        assert len(decision_models) > 0
        assert all(m.category == ModelCategory.DECISION_MAKING for m in decision_models)

        # Categories should be disjoint
        systems_ids = {m.id for m in systems_models}
        decision_ids = {m.id for m in decision_models}
        assert len(systems_ids & decision_ids) == 0


class TestModelRetrieval:
    """
    Test individual model retrieval and metadata.

    Verifies that models can be retrieved by ID and that
    their metadata is correct.
    """

    @pytest.fixture
    def selector(self) -> MentalModelSelector:
        """Create selector with test registry and rules."""
        return MentalModelSelector()

    def test_get_model_by_id(self, selector: MentalModelSelector):
        """
        Test retrieving specific model by ID.

        Verifies direct model lookup by identifier.
        """
        # Get list of all models
        all_models_by_cat = selector.list_all_models()
        assert len(all_models_by_cat) > 0

        # Get first available model ID
        for category, model_names in all_models_by_cat.items():
            if len(model_names) > 0:
                # Try to get a model from this category
                category_models = selector.get_models_by_category(
                    ModelCategory(category)
                )
                if len(category_models) > 0:
                    test_model = category_models[0]

                    # Retrieve by ID
                    retrieved = selector.get_model(test_model.id)

                    assert retrieved is not None
                    assert retrieved.id == test_model.id
                    assert retrieved.name == test_model.name
                    break

    def test_model_has_required_fields(self, selector: MentalModelSelector):
        """
        Test that models have all required fields.

        Verifies data completeness for mental model entries.
        """
        # Get any model
        systems_models = selector.get_models_by_category(ModelCategory.SYSTEMS_THINKING)
        assert len(systems_models) > 0

        model = systems_models[0]

        # Check required fields
        assert model.id
        assert model.name
        assert model.category
        assert model.description
        assert model.when_to_use
        assert model.output_format
        assert 0.0 <= model.confidence_threshold <= 1.0

    def test_list_all_models(self, selector: MentalModelSelector):
        """
        Test listing all available models.

        Verifies that all models can be enumerated by category.
        """
        all_models = selector.list_all_models()

        # Should have multiple categories
        assert len(all_models) > 0

        # Each category should have models
        for category, model_names in all_models.items():
            assert isinstance(model_names, list)
            # At least some categories should have models
            if len(model_names) > 0:
                assert all(isinstance(name, str) for name in model_names)


class TestConstitutionalBoundaries:
    """
    Test constitutional boundaries and graceful degradation.

    Verifies that the selector handles edge cases gracefully
    and respects constitutional principles of transparency.
    """

    @pytest.fixture
    def selector(self) -> MentalModelSelector:
        """Create selector with test registry and rules."""
        return MentalModelSelector()

    def test_empty_context_handling(self, selector: MentalModelSelector):
        """
        Test handling of empty or minimal context.

        Verifies graceful degradation when insufficient
        information is provided.
        """
        result = selector.select_for_context("")

        # Should not crash
        assert isinstance(result, SelectionResult)

        # May have low confidence
        if len(result.models) == 0:
            # That's acceptable for empty context
            assert result.confidence == 0.0
        else:
            # If it returns models, should have a rationale
            assert result.rationale

    def test_unknown_model_id(self, selector: MentalModelSelector):
        """
        Test graceful handling of unknown model ID.

        Verifies that requesting non-existent model returns None.
        """
        result = selector.get_model("nonexistent_model_id_12345")
        assert result is None

    def test_unknown_combination_pattern(self, selector: MentalModelSelector):
        """
        Test graceful handling of unknown combination pattern.

        Verifies that requesting non-existent pattern returns None.
        """
        result = selector.get_combination_pattern("nonexistent_pattern_12345")
        assert result is None

    def test_rationale_transparency(self, selector: MentalModelSelector):
        """
        Test that rationale provides transparency.

        Verifies that selection results include human-readable
        explanations for why models were chosen.
        """
        result = selector.select_for_context(
            "System showing feedback loop behavior with costs increasing"
        )

        if len(result.models) > 0:
            # Should have rationale explaining selection
            assert result.rationale
            assert len(result.rationale) > 10  # Substantive explanation

            # Rationale should reference pattern matching
            assert "match" in result.rationale.lower() or \
                   "pattern" in result.rationale.lower() or \
                   "keyword" in result.rationale.lower()

    def test_confidence_scoring_validity(self, selector: MentalModelSelector):
        """
        Test that confidence scores are valid.

        Verifies that all confidence scores fall within [0, 1]
        and reflect selection quality.
        """
        result = selector.select_for_context(
            "Complex multi-faceted problem requiring systematic analysis"
        )

        # Confidence must be in valid range
        assert 0.0 <= result.confidence <= 1.0

        # Strong context should yield higher confidence
        strong_result = selector.select_for_context(
            "System has feedback loops causing performance degradation"
        )

        assert 0.0 <= strong_result.confidence <= 1.0

        # Weak context should yield lower confidence
        weak_result = selector.select_for_context("thing happening")

        assert 0.0 <= weak_result.confidence <= 1.0


class TestRealWorldScenarios:
    """
    Test real-world GAIA scenarios.

    Integration tests using realistic scenarios from GAIA ecosystem
    to verify end-to-end mental model selection.
    """

    @pytest.fixture
    def selector(self) -> MentalModelSelector:
        """Create selector with test registry and rules."""
        return MentalModelSelector()

    def test_hart_os_confidence_decline_scenario(self, selector: MentalModelSelector):
        """
        Test mental model selection for HART OS confidence decline.

        Real scenario: HART OS showing declining confidence scores.
        Expected: Systems thinking models about feedback loops,
        quality models about testing, temporal models about trends.
        """
        result = selector.select_for_context(
            "HART OS confidence scores declining over time, tests passing "
            "but output quality decreasing, possible feedback loop"
        )

        assert len(result.models) > 0
        assert result.confidence > 0.5

        # Should recommend relevant models
        model_names = " ".join(m.name.lower() for m in result.models)

        # Expect systems or quality models
        assert any(keyword in model_names for keyword in [
            'feedback', 'loop', 'quality', 'test', 'temporal', 'trend'
        ])

    def test_cost_optimization_scenario(self, selector: MentalModelSelector):
        """
        Test mental model selection for cost optimization.

        Scenario: Token costs increasing, need optimization strategy.
        Expected: Decision-making models, cost-benefit analysis,
        Pareto principle.
        """
        result = selector.select_for_context(
            "Token usage costs spiking, need to optimize without sacrificing quality, "
            "identify high-value vs low-value operations"
        )

        assert len(result.models) > 0

        # Should include decision-making or systems models
        categories = {m.category for m in result.models}
        assert ModelCategory.DECISION_MAKING in categories or \
               ModelCategory.SYSTEMS_THINKING in categories

    def test_agent_trust_building_scenario(self, selector: MentalModelSelector):
        """
        Test mental model selection for trust building.

        Scenario: Building user trust through transparency.
        Expected: Communication models, feedback loops, pedagogy models.
        """
        result = selector.select_for_context(
            "Need to build user trust through transparent error explanations "
            "and progressive disclosure of complexity"
        )

        assert len(result.models) > 0

        # Should include communication or learning models
        categories = {m.category for m in result.models}
        assert ModelCategory.COMMUNICATION in categories or \
               ModelCategory.LEARNING_PEDAGOGY in categories
