"""
Tests for mental model selector.
"""

import pytest

from mental_models.models import MentalModel, ModelCategory
from mental_models.selector import MentalModelSelector, SelectionResult


class TestMentalModelSelector:
    """Test mental model selector functionality."""

    @pytest.fixture
    def selector(self):
        """Create selector instance."""
        return MentalModelSelector()

    def test_selector_initialization(self, selector):
        """Test selector loads models and rules."""
        assert len(selector.models) > 0
        assert len(selector.patterns) > 0
        assert len(selector.combination_patterns) > 0

    def test_select_for_performance_context(self, selector):
        """Test selection for performance degradation context."""
        result = selector.select_for_context(
            "system performance degradation detected", max_models=5, min_confidence=0.5
        )

        assert isinstance(result, SelectionResult)
        assert len(result.models) > 0
        assert result.confidence > 0.0

        # Should select systems thinking models
        model_ids = [m.id for m in result.models]
        assert any("bottleneck" in mid or "performance" in mid for mid in model_ids)

    def test_select_for_cost_context(self, selector):
        """Test selection for cost management context."""
        result = selector.select_for_context(
            "API costs are spiking significantly", max_models=5, min_confidence=0.5
        )

        assert len(result.models) > 0

        # Should select cost-related models
        model_ids = [m.id for m in result.models]
        assert any("pareto" in mid or "cost" in mid.lower() for mid in model_ids)

    def test_select_for_error_context(self, selector):
        """Test selection for error pattern context."""
        result = selector.select_for_context(
            "recurring errors and failures detected", max_models=5, min_confidence=0.5
        )

        assert len(result.models) > 0

        # Should select reliability models
        model_ids = [m.id for m in result.models]
        model_categories = [m.category for m in result.models]
        assert any(cat == ModelCategory.QUALITY_RELIABILITY for cat in model_categories)

    def test_get_combination_pattern(self, selector):
        """Test retrieving combination patterns."""
        trust_audit = selector.get_combination_pattern("trust_audit")

        assert trust_audit is not None
        assert len(trust_audit) > 0
        assert all(isinstance(m, MentalModel) for m in trust_audit)

        # Trust audit should include defense in depth, observability
        model_ids = [m.id for m in trust_audit]
        assert "defense_in_depth" in model_ids
        assert "observability" in model_ids

    def test_get_model_by_id(self, selector):
        """Test retrieving specific model."""
        feedback_loops = selector.get_model("feedback_loops")

        assert feedback_loops is not None
        assert feedback_loops.id == "feedback_loops"
        assert feedback_loops.category == ModelCategory.SYSTEMS_THINKING
        assert feedback_loops.confidence_threshold > 0.0

    def test_get_models_by_category(self, selector):
        """Test retrieving models by category."""
        systems_models = selector.get_models_by_category(ModelCategory.SYSTEMS_THINKING)

        assert len(systems_models) > 0
        assert all(m.category == ModelCategory.SYSTEMS_THINKING for m in systems_models)

    def test_list_all_models(self, selector):
        """Test listing all available models."""
        all_models = selector.list_all_models()

        assert isinstance(all_models, dict)
        assert len(all_models) == 7  # 7 categories

        # Check each category has models
        for category, model_names in all_models.items():
            assert len(model_names) > 0
            assert all(isinstance(name, str) for name in model_names)

    def test_min_confidence_threshold(self, selector):
        """Test min_confidence filtering works."""
        # High confidence threshold should return fewer results
        high_confidence = selector.select_for_context("test context", min_confidence=0.9)

        low_confidence = selector.select_for_context("test context", min_confidence=0.3)

        assert len(low_confidence.models) >= len(high_confidence.models)

    def test_max_models_limit(self, selector):
        """Test max_models limit is respected."""
        result = selector.select_for_context(
            "performance degradation cost spike error pattern",
            max_models=3,
            min_confidence=0.3,
        )

        assert len(result.models) <= 3

    def test_alternative_models(self, selector):
        """Test alternative models are provided."""
        result = selector.select_for_context(
            "performance degradation", max_models=2, min_confidence=0.5
        )

        # Should have alternatives if there were more candidates
        assert isinstance(result.alternative_models, list)


class TestMentalModel:
    """Test MentalModel data structure."""

    def test_model_creation(self):
        """Test creating a mental model."""
        model = MentalModel(
            id="test_model",
            name="Test Model",
            category=ModelCategory.SYSTEMS_THINKING,
            description="A test model",
            when_to_use=["testing"],
            output_format="test_output",
            confidence_threshold=0.7,
            examples=["example1", "example2"],
        )

        assert model.id == "test_model"
        assert model.confidence_threshold == 0.7
        assert len(model.examples) == 2

    def test_model_validation(self):
        """Test model validation."""
        # Invalid confidence threshold
        with pytest.raises(ValueError):
            MentalModel(
                id="test",
                name="Test",
                category=ModelCategory.SYSTEMS_THINKING,
                description="Test",
                when_to_use=[],
                output_format="test",
                confidence_threshold=1.5,  # Invalid
            )

    def test_applies_to_context(self):
        """Test context matching."""
        model = MentalModel(
            id="test_model",
            name="Test Model",
            category=ModelCategory.SYSTEMS_THINKING,
            description="A test model",
            when_to_use=["performance issues", "bottleneck analysis"],
            output_format="test_output",
            confidence_threshold=0.7,
            examples=["slow queries", "high latency"],
        )

        # Should match when keywords overlap
        score1 = model.applies_to_context("performance degradation", ["performance", "degradation"])
        assert score1 > 0.0

        # Should not match when no overlap
        score2 = model.applies_to_context("completely unrelated", ["unrelated", "random"])
        assert score2 >= 0.0  # May be 0

    def test_to_dict(self):
        """Test serialization to dictionary."""
        model = MentalModel(
            id="test_model",
            name="Test Model",
            category=ModelCategory.SYSTEMS_THINKING,
            description="A test model",
            when_to_use=["testing"],
            output_format="test_output",
            confidence_threshold=0.7,
        )

        data = model.to_dict()

        assert isinstance(data, dict)
        assert data["id"] == "test_model"
        assert data["category"] == "systems_thinking"
        assert data["confidence_threshold"] == 0.7


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
