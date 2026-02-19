"""
Mental model selector - context-aware mental model recommendation.

Analyzes context and selects appropriate mental models for analysis.
"""

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Set

from mental_models.models import ContextPattern, MentalModel, ModelCategory


@dataclass
class SelectionResult:
    """
    Result of mental model selection.

    Args:
        models: Selected mental models in priority order
        confidence: Overall confidence in selection
        rationale: Why these models were selected
        alternative_models: Other models that could apply

    Returns:
        SelectionResult instance
    """

    models: List[MentalModel]
    confidence: float
    rationale: str
    alternative_models: List[MentalModel]


class MentalModelSelector:
    """
    Context-aware mental model selector.

    Analyzes context (text, keywords, situation) and recommends
    appropriate mental models for structured analysis.

    Usage:
        selector = MentalModelSelector()
        result = selector.select_for_context("performance degradation")

        for model in result.models:
            print(f"Apply {model.name}: {model.description}")
    """

    def __init__(
        self, registry_path: Optional[Path] = None, rules_path: Optional[Path] = None
    ) -> None:
        """
        Initialize mental model selector.

        Args:
            registry_path: Path to mental models registry JSON
            rules_path: Path to invocation rules JSON

        Returns:
            None

        Raises:
            FileNotFoundError: If registry or rules files not found
        """
        base_dir = Path(__file__).parent

        if registry_path is None:
            registry_path = base_dir / "registry.json"
        if rules_path is None:
            rules_path = base_dir / "invocation_rules.json"

        self.registry_path = registry_path
        self.rules_path = rules_path

        # Load registry and rules
        self.models: Dict[str, MentalModel] = {}
        self.patterns: Dict[str, ContextPattern] = {}
        self.combination_patterns: Dict[str, List[str]] = {}

        self._load_registry()
        self._load_rules()

    def _load_registry(self) -> None:
        """Load mental models from registry JSON."""
        with open(self.registry_path, "r") as f:
            data = json.load(f)

        for category, models in data["mental_models"].items():
            for model_data in models:
                model = MentalModel(
                    id=model_data["id"],
                    name=model_data["name"],
                    category=ModelCategory(model_data["category"]),
                    description=model_data["description"],
                    when_to_use=model_data["when_to_use"],
                    output_format=model_data["output_format"],
                    confidence_threshold=model_data["confidence_threshold"],
                    examples=model_data.get("examples", []),
                )
                self.models[model.id] = model

    def _load_rules(self) -> None:
        """Load invocation rules from rules JSON."""
        with open(self.rules_path, "r") as f:
            data = json.load(f)

        # Load context patterns
        for pattern_id, pattern_data in data["invocation_rules"]["context_patterns"].items():
            pattern = ContextPattern(
                id=pattern_id,
                description=pattern_data["description"],
                trigger_keywords=pattern_data["trigger_keywords"],
                recommended_models=pattern_data["recommended_models"],
                explanation=pattern_data["explanation"],
            )
            self.patterns[pattern_id] = pattern

        # Load combination patterns
        for combo_id, combo_data in data["invocation_rules"]["combination_patterns"].items():
            self.combination_patterns[combo_id] = combo_data["model_sequence"]

    def select_for_context(
        self, context: str, max_models: int = 5, min_confidence: float = 0.5
    ) -> SelectionResult:
        """
        Select mental models for given context.

        Args:
            context: Context description (e.g., "performance degradation")
            max_models: Maximum models to return
            min_confidence: Minimum confidence threshold

        Returns:
            SelectionResult with recommended models

        Raises:
            None
        """
        # Extract keywords from context
        keywords = self._extract_keywords(context)

        # Find matching patterns
        pattern_matches: List[tuple[ContextPattern, float]] = []
        for pattern in self.patterns.values():
            score = pattern.matches(context, keywords)
            if score > 0:
                pattern_matches.append((pattern, score))

        # Sort by match score
        pattern_matches.sort(key=lambda x: x[1], reverse=True)

        # Collect recommended models from top patterns
        recommended_model_ids: Set[str] = set()
        rationale_parts: List[str] = []

        for pattern, score in pattern_matches[:3]:  # Top 3 patterns
            recommended_model_ids.update(pattern.recommended_models)
            rationale_parts.append(f"{pattern.description} (match: {score:.0%})")

        # Score each recommended model against context
        model_scores: List[tuple[MentalModel, float]] = []
        for model_id in recommended_model_ids:
            if model_id in self.models:
                model = self.models[model_id]
                # Combine pattern-based confidence with model-specific confidence
                pattern_confidence = max(
                    score
                    for pattern, score in pattern_matches
                    if model_id in pattern.recommended_models
                )
                context_confidence = model.applies_to_context(context, keywords)
                combined_confidence = (pattern_confidence + context_confidence) / 2

                if combined_confidence >= min_confidence:
                    model_scores.append((model, combined_confidence))

        # Sort by confidence
        model_scores.sort(key=lambda x: x[1], reverse=True)

        # Select top models
        selected_models = [m for m, _ in model_scores[:max_models]]
        avg_confidence = (
            sum(s for _, s in model_scores[:max_models]) / len(selected_models)
            if selected_models
            else 0.0
        )

        # Alternative models (next tier)
        alternative_models = [m for m, _ in model_scores[max_models : max_models + 3]]

        rationale = (
            "; ".join(rationale_parts)
            if rationale_parts
            else "No strong pattern match, using keyword-based selection"
        )

        return SelectionResult(
            models=selected_models,
            confidence=avg_confidence,
            rationale=rationale,
            alternative_models=alternative_models,
        )

    def get_combination_pattern(self, pattern_name: str) -> Optional[List[MentalModel]]:
        """
        Get predefined combination of mental models.

        Args:
            pattern_name: Name of combination pattern (e.g., "trust_audit")

        Returns:
            List of mental models in sequence, or None if not found
        """
        if pattern_name not in self.combination_patterns:
            return None

        model_ids = self.combination_patterns[pattern_name]
        return [self.models[mid] for mid in model_ids if mid in self.models]

    def get_model(self, model_id: str) -> Optional[MentalModel]:
        """
        Get mental model by ID.

        Args:
            model_id: Model identifier

        Returns:
            MentalModel or None if not found
        """
        return self.models.get(model_id)

    def get_models_by_category(self, category: ModelCategory) -> List[MentalModel]:
        """
        Get all models in a category.

        Args:
            category: Model category

        Returns:
            List of mental models in category
        """
        return [m for m in self.models.values() if m.category == category]

    def _extract_keywords(self, context: str) -> List[str]:
        """
        Extract keywords from context.

        Args:
            context: Context string

        Returns:
            List of keywords
        """
        # Simple keyword extraction (can be enhanced with NLP)
        words = context.lower().split()

        # Remove common stop words
        stop_words = {
            "the",
            "a",
            "an",
            "and",
            "or",
            "but",
            "in",
            "on",
            "at",
            "to",
            "for",
            "of",
            "with",
            "by",
            "from",
            "is",
            "are",
            "was",
            "were",
        }

        keywords = [w.strip(".,!?;:") for w in words if w not in stop_words]
        return keywords

    def list_all_models(self) -> Dict[str, List[str]]:
        """
        List all available mental models by category.

        Returns:
            Dictionary mapping category names to model names
        """
        result: Dict[str, List[str]] = {}

        for category in ModelCategory:
            models = self.get_models_by_category(category)
            result[category.value] = [m.name for m in models]

        return result


# Convenience function for quick access
_global_selector: Optional[MentalModelSelector] = None


def get_model(model_id: str) -> Optional[MentalModel]:
    """
    Get mental model by ID (convenience function).

    Args:
        model_id: Model identifier

    Returns:
        MentalModel or None if not found
    """
    global _global_selector
    if _global_selector is None:
        _global_selector = MentalModelSelector()

    return _global_selector.get_model(model_id)
