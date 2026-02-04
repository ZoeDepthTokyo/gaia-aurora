"""
Background pattern detection for GAIA subconscious.

Analyzes external memory to detect patterns in observations,
errors, and behaviors without intervening in execution.
"""

from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional
from collections import Counter, defaultdict
from enum import Enum

from argus.subconscious.memory import (
    ExternalMemory,
    MemoryEntry,
    MemoryType,
    MemoryScope
)


class PatternType(Enum):
    """Types of detected patterns."""

    RECURRING_ERROR = "recurring_error"
    PERFORMANCE_DEGRADATION = "performance_degradation"
    COST_SPIKE = "cost_spike"
    USAGE_PATTERN = "usage_pattern"
    CONFIDENCE_DRIFT = "confidence_drift"
    ANTI_PATTERN = "anti_pattern"
    SUCCESS_PATTERN = "success_pattern"
    CORRELATION = "correlation"


@dataclass
class DetectedPattern:
    """
    A pattern detected in memory/telemetry.

    Args:
        type: Pattern type
        description: Human-readable description
        evidence: List of memory entry IDs supporting pattern
        confidence: Detection confidence (0.0-1.0)
        first_seen: When pattern first appeared
        last_seen: When pattern last appeared
        frequency: How often pattern occurs
        severity: Severity level (0.0-1.0)
        recommended_actions: Suggested responses
        metadata: Additional pattern-specific data

    Returns:
        DetectedPattern instance
    """

    type: PatternType
    description: str
    evidence: List[str]
    confidence: float
    first_seen: datetime
    last_seen: datetime
    frequency: int
    severity: float = 0.5
    recommended_actions: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        """Validate after initialization."""
        if not 0.0 <= self.confidence <= 1.0:
            raise ValueError(f"confidence must be in [0, 1], got {self.confidence}")
        if not 0.0 <= self.severity <= 1.0:
            raise ValueError(f"severity must be in [0, 1], got {self.severity}")

        if isinstance(self.type, str):
            self.type = PatternType(self.type)

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return {
            "type": self.type.value,
            "description": self.description,
            "evidence": self.evidence,
            "confidence": self.confidence,
            "first_seen": self.first_seen.isoformat(),
            "last_seen": self.last_seen.isoformat(),
            "frequency": self.frequency,
            "severity": self.severity,
            "recommended_actions": self.recommended_actions,
            "metadata": self.metadata
        }


class PatternDetector:
    """
    Background pattern detector.

    Analyzes external memory to detect recurring patterns,
    trends, and anomalies in ecosystem behavior.

    This is a non-intervening observer - it produces hypotheses,
    not actions.

    Usage:
        detector = PatternDetector(memory)
        patterns = detector.detect_patterns(lookback_days=30)

        for pattern in patterns:
            print(f"{pattern.type}: {pattern.description}")
    """

    def __init__(self, memory: ExternalMemory) -> None:
        """
        Initialize pattern detector.

        Args:
            memory: ExternalMemory instance

        Returns:
            None
        """
        self.memory = memory

    def detect_patterns(
        self,
        lookback_days: int = 30,
        min_frequency: int = 3,
        min_confidence: float = 0.6
    ) -> List[DetectedPattern]:
        """
        Detect patterns in recent memory.

        Args:
            lookback_days: How far back to analyze
            min_frequency: Minimum occurrences to be considered pattern
            min_confidence: Minimum confidence threshold

        Returns:
            List of detected patterns
        """
        patterns: List[DetectedPattern] = []

        # Detect recurring errors
        patterns.extend(
            self._detect_recurring_errors(lookback_days, min_frequency)
        )

        # Detect performance degradation
        patterns.extend(
            self._detect_performance_degradation(lookback_days)
        )

        # Detect cost spikes
        patterns.extend(
            self._detect_cost_patterns(lookback_days)
        )

        # Detect confidence drift
        patterns.extend(
            self._detect_confidence_drift(lookback_days)
        )

        # Detect usage patterns
        patterns.extend(
            self._detect_usage_patterns(lookback_days, min_frequency)
        )

        # Filter by confidence
        patterns = [p for p in patterns if p.confidence >= min_confidence]

        # Sort by severity * confidence
        patterns.sort(key=lambda p: p.severity * p.confidence, reverse=True)

        return patterns

    def _detect_recurring_errors(
        self,
        lookback_days: int,
        min_frequency: int
    ) -> List[DetectedPattern]:
        """Detect recurring error patterns."""
        # Search for error memories
        errors = self.memory.search(
            type=MemoryType.ERROR,
            limit=1000
        )

        if not errors:
            return []

        # Group by error content similarity (simple: exact match for now)
        error_groups: Dict[str, List[MemoryEntry]] = defaultdict(list)

        for error in errors:
            # Simple grouping by first 100 chars of content
            key = error.content[:100]
            error_groups[key].append(error)

        patterns: List[DetectedPattern] = []

        for key, group in error_groups.items():
            if len(group) >= min_frequency:
                # Calculate time span
                timestamps = [e.timestamp for e in group]
                first_seen = min(timestamps)
                last_seen = max(timestamps)

                # Calculate severity (more recent = higher severity)
                days_since_last = (datetime.now() - last_seen).days
                severity = max(0.0, 1.0 - (days_since_last / lookback_days))

                pattern = DetectedPattern(
                    type=PatternType.RECURRING_ERROR,
                    description=f"Recurring error: {group[0].content[:100]}",
                    evidence=[e.id for e in group if e.id],
                    confidence=min(1.0, len(group) / (min_frequency * 3)),
                    first_seen=first_seen,
                    last_seen=last_seen,
                    frequency=len(group),
                    severity=severity,
                    recommended_actions=[
                        "Investigate root cause",
                        "Add error handling",
                        "Create issue ticket"
                    ],
                    metadata={
                        "error_preview": group[0].content[:200],
                        "sources": list(set(e.source for e in group))
                    }
                )

                patterns.append(pattern)

        return patterns

    def _detect_performance_degradation(
        self,
        lookback_days: int
    ) -> List[DetectedPattern]:
        """Detect performance degradation trends."""
        # Look for observations about performance
        observations = self.memory.search(
            type=MemoryType.OBSERVATION,
            query="performance",
            limit=500
        )

        if len(observations) < 5:
            return []

        # Simple trend detection: compare first half vs second half
        observations.sort(key=lambda o: o.timestamp)
        mid = len(observations) // 2

        first_half = observations[:mid]
        second_half = observations[mid:]

        # Count negative performance indicators
        negative_keywords = ["slow", "degradation", "latency", "timeout"]

        first_half_negatives = sum(
            1 for obs in first_half
            if any(kw in obs.content.lower() for kw in negative_keywords)
        )

        second_half_negatives = sum(
            1 for obs in second_half
            if any(kw in obs.content.lower() for kw in negative_keywords)
        )

        # If second half has significantly more negatives, it's degradation
        if second_half_negatives > first_half_negatives * 1.5:
            confidence = min(1.0, second_half_negatives / len(second_half))

            return [DetectedPattern(
                type=PatternType.PERFORMANCE_DEGRADATION,
                description="Performance degradation detected over time",
                evidence=[o.id for o in second_half if o.id],
                confidence=confidence,
                first_seen=first_half[0].timestamp,
                last_seen=second_half[-1].timestamp,
                frequency=second_half_negatives,
                severity=0.7,
                recommended_actions=[
                    "Profile system performance",
                    "Identify bottlenecks",
                    "Review recent changes"
                ],
                metadata={
                    "first_half_issues": first_half_negatives,
                    "second_half_issues": second_half_negatives,
                    "trend": "worsening"
                }
            )]

        return []

    def _detect_cost_patterns(self, lookback_days: int) -> List[DetectedPattern]:
        """Detect cost spike patterns."""
        # Look for cost-related observations
        cost_observations = self.memory.search(
            query="cost",
            limit=500
        )

        if len(cost_observations) < 5:
            return []

        # Check for sudden increases
        # (This is simplified - production would parse actual cost values)

        patterns: List[DetectedPattern] = []

        spike_keywords = ["spike", "increase", "expensive", "high"]
        recent_spikes = [
            obs for obs in cost_observations
            if any(kw in obs.content.lower() for kw in spike_keywords)
            and (datetime.now() - obs.timestamp).days <= 7
        ]

        if len(recent_spikes) >= 3:
            patterns.append(DetectedPattern(
                type=PatternType.COST_SPIKE,
                description="Recent cost spike detected",
                evidence=[o.id for o in recent_spikes if o.id],
                confidence=0.8,
                first_seen=min(o.timestamp for o in recent_spikes),
                last_seen=max(o.timestamp for o in recent_spikes),
                frequency=len(recent_spikes),
                severity=0.8,
                recommended_actions=[
                    "Review token usage by project",
                    "Check for inefficient prompts",
                    "Consider caching strategies"
                ],
                metadata={
                    "spike_count": len(recent_spikes)
                }
            ))

        return patterns

    def _detect_confidence_drift(self, lookback_days: int) -> List[DetectedPattern]:
        """Detect confidence score drift."""
        # Look for confidence-related observations
        confidence_obs = self.memory.search(
            query="confidence",
            limit=500
        )

        if len(confidence_obs) < 10:
            return []

        # Check for declining trend
        decline_keywords = ["declining", "decreasing", "drop", "lower"]

        recent_declines = [
            obs for obs in confidence_obs
            if any(kw in obs.content.lower() for kw in decline_keywords)
            and (datetime.now() - obs.timestamp).days <= lookback_days
        ]

        if len(recent_declines) >= 3:
            return [DetectedPattern(
                type=PatternType.CONFIDENCE_DRIFT,
                description="Confidence scores showing decline",
                evidence=[o.id for o in recent_declines if o.id],
                confidence=0.75,
                first_seen=min(o.timestamp for o in recent_declines),
                last_seen=max(o.timestamp for o in recent_declines),
                frequency=len(recent_declines),
                severity=0.6,
                recommended_actions=[
                    "Review prompt quality",
                    "Check input data quality",
                    "Compare recent vs historical outputs"
                ],
                metadata={
                    "decline_observations": len(recent_declines)
                }
            )]

        return []

    def _detect_usage_patterns(
        self,
        lookback_days: int,
        min_frequency: int
    ) -> List[DetectedPattern]:
        """Detect usage patterns."""
        # Get all observations
        observations = self.memory.search(
            type=MemoryType.OBSERVATION,
            limit=1000
        )

        if len(observations) < min_frequency:
            return []

        # Group by source (project)
        by_source: Dict[str, List[MemoryEntry]] = defaultdict(list)

        for obs in observations:
            by_source[obs.source].append(obs)

        patterns: List[DetectedPattern] = []

        # Find high-frequency sources
        for source, entries in by_source.items():
            if len(entries) >= min_frequency * 2:
                # High usage pattern
                patterns.append(DetectedPattern(
                    type=PatternType.USAGE_PATTERN,
                    description=f"High activity from {source}",
                    evidence=[e.id for e in entries[:20] if e.id],
                    confidence=0.9,
                    first_seen=min(e.timestamp for e in entries),
                    last_seen=max(e.timestamp for e in entries),
                    frequency=len(entries),
                    severity=0.3,  # Low severity, just informational
                    recommended_actions=[
                        "Monitor resource usage",
                        "Ensure adequate capacity"
                    ],
                    metadata={
                        "source": source,
                        "observation_count": len(entries)
                    }
                ))

        return patterns
