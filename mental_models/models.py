"""
Core mental model data structures.

Defines mental model schemas and categories for GAIA analytical framework.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import List, Dict, Any, Optional
from datetime import datetime


class ModelCategory(Enum):
    """Categories of mental models."""

    SYSTEMS_THINKING = "systems_thinking"
    DECISION_MAKING = "decision_making"
    COGNITIVE_BIASES = "cognitive_biases"
    LEARNING_PEDAGOGY = "learning_pedagogy"
    QUALITY_RELIABILITY = "quality_reliability"
    COMMUNICATION = "communication"
    TEMPORAL = "temporal"


@dataclass
class MentalModel:
    """
    A mental model for structured analysis.

    Mental models provide frameworks for understanding and analyzing
    complex situations in consistent, documented ways.

    Args:
        id: Unique identifier (e.g., "feedback_loops")
        name: Human-readable name
        category: Model category
        description: What this model explains
        when_to_use: List of situations where model applies
        output_format: Expected analysis output format
        confidence_threshold: Minimum confidence to auto-apply (0.0-1.0)
        examples: Concrete examples of model application

    Returns:
        MentalModel instance

    Raises:
        ValueError: If confidence_threshold not in [0, 1]
    """

    id: str
    name: str
    category: ModelCategory
    description: str
    when_to_use: List[str]
    output_format: str
    confidence_threshold: float
    examples: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        """Validate mental model after initialization."""
        if not 0.0 <= self.confidence_threshold <= 1.0:
            raise ValueError(
                f"confidence_threshold must be in [0, 1], got {self.confidence_threshold}"
            )

        # Convert category string to enum if needed
        if isinstance(self.category, str):
            self.category = ModelCategory(self.category)

    def applies_to_context(self, context: str, keywords: List[str]) -> float:
        """
        Calculate confidence that this model applies to given context.

        Args:
            context: Context description (e.g., "performance degradation")
            keywords: Keywords from context

        Returns:
            Confidence score (0.0-1.0)
        """
        # Check when_to_use descriptions
        relevance_score = 0.0
        matches = 0

        for use_case in self.when_to_use:
            if any(keyword.lower() in use_case.lower() for keyword in keywords):
                matches += 1

        if self.when_to_use:
            relevance_score = matches / len(self.when_to_use)

        # Check examples for keyword matches
        example_matches = 0
        for example in self.examples:
            if any(keyword.lower() in example.lower() for keyword in keywords):
                example_matches += 1

        if self.examples:
            example_score = example_matches / len(self.examples)
            relevance_score = (relevance_score + example_score) / 2

        return min(1.0, relevance_score)

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for serialization."""
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category.value,
            "description": self.description,
            "when_to_use": self.when_to_use,
            "output_format": self.output_format,
            "confidence_threshold": self.confidence_threshold,
            "examples": self.examples,
            "metadata": self.metadata
        }


@dataclass
class ModelInvocation:
    """
    Record of mental model being invoked for analysis.

    Args:
        model: The mental model being invoked
        context: Context that triggered invocation
        confidence: Confidence score for this invocation
        rationale: Why this model was selected
        timestamp: When invocation occurred
        auto_applied: Whether model was applied automatically

    Returns:
        ModelInvocation instance
    """

    model: MentalModel
    context: str
    confidence: float
    rationale: str
    timestamp: datetime = field(default_factory=datetime.now)
    auto_applied: bool = False
    user_confirmed: Optional[bool] = None
    analysis_result: Optional[Dict[str, Any]] = None

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for logging."""
        return {
            "model_id": self.model.id,
            "model_name": self.model.name,
            "context": self.context,
            "confidence": self.confidence,
            "rationale": self.rationale,
            "timestamp": self.timestamp.isoformat(),
            "auto_applied": self.auto_applied,
            "user_confirmed": self.user_confirmed,
            "analysis_result": self.analysis_result
        }


@dataclass
class ContextPattern:
    """
    A pattern for matching context to mental models.

    Args:
        id: Pattern identifier
        description: What this pattern represents
        trigger_keywords: Keywords that activate this pattern
        recommended_models: Models to apply for this pattern
        explanation: Why these models are recommended

    Returns:
        ContextPattern instance
    """

    id: str
    description: str
    trigger_keywords: List[str]
    recommended_models: List[str]
    explanation: str

    def matches(self, context: str, keywords: List[str]) -> float:
        """
        Calculate match score for given context.

        Args:
            context: Context description
            keywords: Extracted keywords

        Returns:
            Match score (0.0-1.0)
        """
        matches = sum(
            1 for trigger in self.trigger_keywords
            if trigger.lower() in context.lower() or
            any(trigger.lower() in kw.lower() for kw in keywords)
        )

        return matches / len(self.trigger_keywords) if self.trigger_keywords else 0.0
