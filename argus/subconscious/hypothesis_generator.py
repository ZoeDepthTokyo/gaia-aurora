"""
Hypothesis generator for GAIA subconscious.

Generates testable hypotheses from detected patterns and observations.
This is reflective cognition - proposing possibilities, not executing actions.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Dict, Any, Optional
from enum import Enum

from argus.subconscious.pattern_detector import DetectedPattern, PatternType
from argus.subconscious.memory import MemoryEntry, MemoryType


class HypothesisStatus(Enum):
    """Status of hypothesis."""

    PENDING = "pending"  # Generated, not yet tested
    TESTING = "testing"  # Currently being tested
    CONFIRMED = "confirmed"  # Evidence supports hypothesis
    REJECTED = "rejected"  # Evidence contradicts hypothesis
    INCONCLUSIVE = "inconclusive"  # Insufficient evidence


@dataclass
class Hypothesis:
    """
    A testable hypothesis about system behavior.

    Args:
        description: Human-readable hypothesis statement
        pattern_type: Related pattern type
        evidence_for: Supporting evidence (memory IDs)
        evidence_against: Contradicting evidence (memory IDs)
        confidence: Confidence in hypothesis (0.0-1.0)
        status: Current hypothesis status
        proposed_test: How to test this hypothesis
        implications: What it means if true
        created_at: When hypothesis was generated
        tested_at: When hypothesis was tested
        metadata: Additional data

    Returns:
        Hypothesis instance
    """

    description: str
    pattern_type: PatternType
    evidence_for: List[str] = field(default_factory=list)
    evidence_against: List[str] = field(default_factory=list)
    confidence: float = 0.5
    status: HypothesisStatus = HypothesisStatus.PENDING
    proposed_test: str = ""
    implications: List[str] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.now)
    tested_at: Optional[datetime] = None
    metadata: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        """Validate after initialization."""
        if not 0.0 <= self.confidence <= 1.0:
            raise ValueError(f"confidence must be in [0, 1], got {self.confidence}")

        if isinstance(self.status, str):
            self.status = HypothesisStatus(self.status)
        if isinstance(self.pattern_type, str):
            self.pattern_type = PatternType(self.pattern_type)

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return {
            "description": self.description,
            "pattern_type": self.pattern_type.value,
            "evidence_for": self.evidence_for,
            "evidence_against": self.evidence_against,
            "confidence": self.confidence,
            "status": self.status.value,
            "proposed_test": self.proposed_test,
            "implications": self.implications,
            "created_at": self.created_at.isoformat(),
            "tested_at": self.tested_at.isoformat() if self.tested_at else None,
            "metadata": self.metadata
        }


class HypothesisGenerator:
    """
    Generates testable hypotheses from patterns.

    This is pure reflective cognition - generates possibilities
    without executing or intervening.

    Usage:
        generator = HypothesisGenerator()
        hypotheses = generator.generate_from_pattern(pattern)

        for hyp in hypotheses:
            print(f"Hypothesis: {hyp.description}")
            print(f"Test: {hyp.proposed_test}")
    """

    def __init__(self) -> None:
        """Initialize hypothesis generator."""
        # Hypothesis templates by pattern type
        self.templates = self._initialize_templates()

    def _initialize_templates(self) -> Dict[PatternType, List[Dict[str, Any]]]:
        """Initialize hypothesis templates for each pattern type."""
        return {
            PatternType.RECURRING_ERROR: [
                {
                    "template": "Error '{error}' is caused by {cause}",
                    "causes": [
                        "input data quality issues",
                        "prompt regression",
                        "API rate limiting",
                        "configuration change",
                        "dependency update"
                    ],
                    "test": "Review {error} context and compare with successful cases",
                    "implications": [
                        "If input data: implement validation",
                        "If prompt: rollback and review changes",
                        "If API: implement rate limiting",
                        "If config: audit recent changes"
                    ]
                },
                {
                    "template": "Error frequency correlates with {factor}",
                    "factors": [
                        "time of day",
                        "project load",
                        "specific user actions",
                        "data volume"
                    ],
                    "test": "Analyze error timestamps against {factor}",
                    "implications": ["Adjust capacity planning", "Schedule maintenance windows"]
                }
            ],
            PatternType.PERFORMANCE_DEGRADATION: [
                {
                    "template": "Performance degradation due to {cause}",
                    "causes": [
                        "accumulating technical debt",
                        "increasing data volume",
                        "memory leaks",
                        "inefficient queries",
                        "external API slowdown"
                    ],
                    "test": "Profile system and identify bottlenecks",
                    "implications": [
                        "Implement caching",
                        "Optimize queries",
                        "Add resource monitoring"
                    ]
                },
                {
                    "template": "Specific component {component} is bottleneck",
                    "components": [
                        "LLM API calls",
                        "database queries",
                        "memory retrieval",
                        "file I/O"
                    ],
                    "test": "Measure latency by component",
                    "implications": ["Optimize specific component", "Consider architectural change"]
                }
            ],
            PatternType.COST_SPIKE: [
                {
                    "template": "Cost spike caused by {cause}",
                    "causes": [
                        "inefficient prompts",
                        "missing caching",
                        "duplicate API calls",
                        "increased usage",
                        "model upgrade"
                    ],
                    "test": "Analyze token usage by operation",
                    "implications": [
                        "Optimize prompts",
                        "Implement caching",
                        "Add usage limits"
                    ]
                }
            ],
            PatternType.CONFIDENCE_DRIFT: [
                {
                    "template": "Confidence drift due to {cause}",
                    "causes": [
                        "data quality decline",
                        "prompt degradation",
                        "model behavior change",
                        "threshold miscalibration"
                    ],
                    "test": "Compare recent outputs with historical baseline",
                    "implications": [
                        "Review data pipeline",
                        "Audit prompt changes",
                        "Recalibrate thresholds"
                    ]
                }
            ]
        }

    def generate_from_pattern(self, pattern: DetectedPattern) -> List[Hypothesis]:
        """
        Generate hypotheses from detected pattern.

        Args:
            pattern: Detected pattern

        Returns:
            List of hypotheses to test
        """
        hypotheses: List[Hypothesis] = []

        templates = self.templates.get(pattern.type, [])

        for template_data in templates:
            # Generate variations based on template
            if "causes" in template_data:
                for cause in template_data["causes"]:
                    description = template_data["template"].format(
                        error=pattern.description,
                        cause=cause,
                        factor=cause,
                        component=cause
                    )

                    proposed_test = template_data["test"].format(
                        error=pattern.description,
                        factor=cause,
                        component=cause
                    )

                    hypothesis = Hypothesis(
                        description=description,
                        pattern_type=pattern.type,
                        evidence_for=pattern.evidence[:5],  # Sample of evidence
                        confidence=pattern.confidence * 0.7,  # Lower than pattern confidence
                        proposed_test=proposed_test,
                        implications=template_data.get("implications", []),
                        metadata={
                            "pattern_frequency": pattern.frequency,
                            "pattern_severity": pattern.severity,
                            "cause_category": cause
                        }
                    )

                    hypotheses.append(hypothesis)

            elif "factors" in template_data:
                for factor in template_data["factors"]:
                    description = template_data["template"].format(
                        factor=factor
                    )

                    proposed_test = template_data["test"].format(
                        factor=factor
                    )

                    hypothesis = Hypothesis(
                        description=description,
                        pattern_type=pattern.type,
                        evidence_for=pattern.evidence[:5],
                        confidence=pattern.confidence * 0.6,
                        proposed_test=proposed_test,
                        implications=template_data.get("implications", []),
                        metadata={
                            "pattern_frequency": pattern.frequency,
                            "factor": factor
                        }
                    )

                    hypotheses.append(hypothesis)

        # Limit to top 3 most confident hypotheses
        hypotheses.sort(key=lambda h: h.confidence, reverse=True)
        return hypotheses[:3]

    def generate_from_observations(
        self,
        observations: List[MemoryEntry],
        min_confidence: float = 0.5
    ) -> List[Hypothesis]:
        """
        Generate hypotheses from raw observations.

        Args:
            observations: List of memory entries
            min_confidence: Minimum confidence threshold

        Returns:
            List of hypotheses
        """
        hypotheses: List[Hypothesis] = []

        # Look for correlations
        if len(observations) >= 5:
            # Group by time windows (simplified)
            # In production, would use statistical correlation

            # Check for time-based patterns
            time_pattern = self._detect_time_pattern(observations)
            if time_pattern and time_pattern["confidence"] >= min_confidence:
                hypothesis = Hypothesis(
                    description=time_pattern["description"],
                    pattern_type=PatternType.USAGE_PATTERN,
                    evidence_for=[o.id for o in observations if o.id],
                    confidence=time_pattern["confidence"],
                    proposed_test="Analyze observations by time of day",
                    implications=[
                        "Adjust resource allocation by time",
                        "Schedule maintenance during low usage"
                    ],
                    metadata=time_pattern["metadata"]
                )
                hypotheses.append(hypothesis)

        return hypotheses

    def _detect_time_pattern(
        self,
        observations: List[MemoryEntry]
    ) -> Optional[Dict[str, Any]]:
        """Detect time-based patterns in observations."""
        if not observations:
            return None

        # Group by hour of day
        by_hour = [0] * 24

        for obs in observations:
            hour = obs.timestamp.hour
            by_hour[hour] += 1

        # Find peak hour
        peak_hour = by_hour.index(max(by_hour))
        peak_count = by_hour[peak_hour]
        total = sum(by_hour)

        if total == 0:
            return None

        # If >40% of observations in single hour, that's a pattern
        concentration = peak_count / total

        if concentration >= 0.4:
            return {
                "description": f"Observations concentrated around hour {peak_hour}:00",
                "confidence": concentration,
                "metadata": {
                    "peak_hour": peak_hour,
                    "peak_count": peak_count,
                    "total": total,
                    "concentration": concentration
                }
            }

        return None

    def refine_hypothesis(
        self,
        hypothesis: Hypothesis,
        new_evidence_for: List[str] = None,
        new_evidence_against: List[str] = None
    ) -> Hypothesis:
        """
        Refine hypothesis with new evidence.

        Args:
            hypothesis: Hypothesis to refine
            new_evidence_for: New supporting evidence
            new_evidence_against: New contradicting evidence

        Returns:
            Refined hypothesis
        """
        if new_evidence_for:
            hypothesis.evidence_for.extend(new_evidence_for)

        if new_evidence_against:
            hypothesis.evidence_against.extend(new_evidence_against)

        # Recalculate confidence based on evidence balance
        total_evidence = len(hypothesis.evidence_for) + len(hypothesis.evidence_against)

        if total_evidence > 0:
            support_ratio = len(hypothesis.evidence_for) / total_evidence
            hypothesis.confidence = support_ratio

            # Update status based on evidence
            if support_ratio >= 0.8:
                hypothesis.status = HypothesisStatus.CONFIRMED
            elif support_ratio <= 0.2:
                hypothesis.status = HypothesisStatus.REJECTED
            elif support_ratio >= 0.4 and support_ratio <= 0.6:
                hypothesis.status = HypothesisStatus.INCONCLUSIVE

        return hypothesis
