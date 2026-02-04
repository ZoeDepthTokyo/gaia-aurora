"""
Context enricher for GAIA subconscious.

Pre-loads relevant context from external memory before analysis,
enriching understanding without intervening in execution.
"""

from typing import List, Dict, Any, Optional
from datetime import datetime, timedelta

from argus.subconscious.memory import ExternalMemory, MemoryEntry, MemoryType, MemoryScope
from argus.subconscious.pattern_detector import PatternDetector, DetectedPattern


class ContextEnricher:
    """
    Context enrichment from external memory.

    Pre-loads relevant historical context, patterns, and observations
    to enrich analysis without requiring explicit queries.

    Usage:
        enricher = ContextEnricher(memory)

        # Enrich context for a new observation
        context = enricher.enrich_for_observation(
            "HART OS confidence scores declining"
        )

        print(f"Related patterns: {len(context['patterns'])}")
        print(f"Historical context: {len(context['history'])}")
    """

    def __init__(self, memory: ExternalMemory) -> None:
        """
        Initialize context enricher.

        Args:
            memory: ExternalMemory instance

        Returns:
            None
        """
        self.memory = memory
        self.pattern_detector = PatternDetector(memory)

    def enrich_for_observation(
        self,
        observation: str,
        project: Optional[str] = None,
        lookback_days: int = 30
    ) -> Dict[str, Any]:
        """
        Enrich context for new observation.

        Args:
            observation: Observation text
            project: Project name (optional)
            lookback_days: How far back to search

        Returns:
            Dictionary with enriched context
        """
        # Extract keywords
        keywords = self._extract_keywords(observation)

        # Find related observations
        related_observations = self._find_related_observations(
            keywords,
            project,
            lookback_days
        )

        # Find related patterns
        related_patterns = self._find_related_patterns(
            keywords,
            lookback_days
        )

        # Find related errors
        related_errors = self._find_related_errors(
            keywords,
            lookback_days
        )

        # Find related successes (for comparison)
        related_successes = self._find_related_successes(
            keywords,
            lookback_days
        )

        # Build enriched context
        context = {
            "observation": observation,
            "keywords": keywords,
            "related_observations": [
                self._summarize_memory(m) for m in related_observations
            ],
            "related_patterns": [
                p.to_dict() for p in related_patterns
            ],
            "related_errors": [
                self._summarize_memory(m) for m in related_errors
            ],
            "related_successes": [
                self._summarize_memory(m) for m in related_successes
            ],
            "temporal_context": self._get_temporal_context(
                related_observations + related_errors
            ),
            "project_context": self._get_project_context(project) if project else None,
            "enriched_at": datetime.now().isoformat()
        }

        return context

    def enrich_for_decision(
        self,
        decision_context: str,
        project: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Enrich context for decision-making.

        Args:
            decision_context: Decision context description
            project: Project name (optional)

        Returns:
            Enriched context with historical decisions
        """
        keywords = self._extract_keywords(decision_context)

        # Find similar past decisions
        past_decisions = self.memory.search(
            type=MemoryType.DECISION,
            limit=50
        )

        # Find outcomes of past decisions
        past_outcomes = self.memory.search(
            type=MemoryType.OUTCOME,
            limit=50
        )

        # Find relevant patterns
        patterns = self._find_related_patterns(keywords, lookback_days=90)

        context = {
            "decision_context": decision_context,
            "keywords": keywords,
            "past_decisions": [
                self._summarize_memory(m) for m in past_decisions[:10]
            ],
            "past_outcomes": [
                self._summarize_memory(m) for m in past_outcomes[:10]
            ],
            "relevant_patterns": [
                p.to_dict() for p in patterns
            ],
            "success_rate": self._calculate_success_rate(past_outcomes),
            "enriched_at": datetime.now().isoformat()
        }

        return context

    def _find_related_observations(
        self,
        keywords: List[str],
        project: Optional[str],
        lookback_days: int
    ) -> List[MemoryEntry]:
        """Find observations related to keywords."""
        related: List[MemoryEntry] = []

        for keyword in keywords:
            results = self.memory.search(
                query=keyword,
                type=MemoryType.OBSERVATION,
                source=project,
                limit=20
            )
            related.extend(results)

        # Deduplicate
        seen_ids = set()
        unique = []
        for mem in related:
            if mem.id and mem.id not in seen_ids:
                seen_ids.add(mem.id)
                unique.append(mem)

        # Filter by timeframe
        cutoff = datetime.now() - timedelta(days=lookback_days)
        recent = [m for m in unique if m.timestamp >= cutoff]

        # Sort by recency
        recent.sort(key=lambda m: m.timestamp, reverse=True)

        return recent[:10]

    def _find_related_patterns(
        self,
        keywords: List[str],
        lookback_days: int
    ) -> List[DetectedPattern]:
        """Find patterns related to keywords."""
        # Get recent patterns
        all_patterns = self.pattern_detector.detect_patterns(
            lookback_days=lookback_days,
            min_frequency=2,
            min_confidence=0.5
        )

        # Filter by keyword relevance
        related = []
        for pattern in all_patterns:
            if any(kw.lower() in pattern.description.lower() for kw in keywords):
                related.append(pattern)

        return related[:5]

    def _find_related_errors(
        self,
        keywords: List[str],
        lookback_days: int
    ) -> List[MemoryEntry]:
        """Find errors related to keywords."""
        related: List[MemoryEntry] = []

        for keyword in keywords:
            results = self.memory.search(
                query=keyword,
                type=MemoryType.ERROR,
                limit=20
            )
            related.extend(results)

        # Deduplicate and filter
        seen_ids = set()
        unique = []
        for mem in related:
            if mem.id and mem.id not in seen_ids:
                seen_ids.add(mem.id)
                unique.append(mem)

        cutoff = datetime.now() - timedelta(days=lookback_days)
        recent = [m for m in unique if m.timestamp >= cutoff]

        recent.sort(key=lambda m: m.timestamp, reverse=True)
        return recent[:5]

    def _find_related_successes(
        self,
        keywords: List[str],
        lookback_days: int
    ) -> List[MemoryEntry]:
        """Find successes related to keywords (for comparison)."""
        related: List[MemoryEntry] = []

        for keyword in keywords:
            results = self.memory.search(
                query=keyword,
                type=MemoryType.SUCCESS,
                limit=20
            )
            related.extend(results)

        # Deduplicate and filter
        seen_ids = set()
        unique = []
        for mem in related:
            if mem.id and mem.id not in seen_ids:
                seen_ids.add(mem.id)
                unique.append(mem)

        cutoff = datetime.now() - timedelta(days=lookback_days)
        recent = [m for m in unique if m.timestamp >= cutoff]

        recent.sort(key=lambda m: m.timestamp, reverse=True)
        return recent[:5]

    def _get_temporal_context(
        self,
        memories: List[MemoryEntry]
    ) -> Dict[str, Any]:
        """Analyze temporal patterns in memories."""
        if not memories:
            return {"trend": "insufficient_data"}

        # Sort by timestamp
        memories = sorted(memories, key=lambda m: m.timestamp)

        first = memories[0].timestamp
        last = memories[-1].timestamp
        span_days = (last - first).days

        # Group by week
        by_week: Dict[int, int] = {}
        for mem in memories:
            week = mem.timestamp.isocalendar()[1]
            by_week[week] = by_week.get(week, 0) + 1

        # Detect trend
        if len(by_week) >= 2:
            weeks = sorted(by_week.keys())
            first_half = weeks[:len(weeks)//2]
            second_half = weeks[len(weeks)//2:]

            first_half_count = sum(by_week[w] for w in first_half)
            second_half_count = sum(by_week[w] for w in second_half)

            if second_half_count > first_half_count * 1.3:
                trend = "increasing"
            elif second_half_count < first_half_count * 0.7:
                trend = "decreasing"
            else:
                trend = "stable"
        else:
            trend = "insufficient_data"

        return {
            "span_days": span_days,
            "total_entries": len(memories),
            "trend": trend,
            "first_seen": first.isoformat(),
            "last_seen": last.isoformat()
        }

    def _get_project_context(self, project: str) -> Dict[str, Any]:
        """Get context specific to project."""
        # Count memories by type for this project
        observations = self.memory.count(
            type=MemoryType.OBSERVATION
        )

        errors = self.memory.count(
            type=MemoryType.ERROR
        )

        successes = self.memory.count(
            type=MemoryType.SUCCESS
        )

        # Calculate health score
        total = observations + errors + successes
        if total > 0:
            health_score = (successes - errors) / total
            health_score = max(0.0, min(1.0, (health_score + 1) / 2))  # Normalize to 0-1
        else:
            health_score = 0.5

        return {
            "project": project,
            "observations": observations,
            "errors": errors,
            "successes": successes,
            "health_score": health_score
        }

    def _calculate_success_rate(self, outcomes: List[MemoryEntry]) -> float:
        """Calculate success rate from outcomes."""
        if not outcomes:
            return 0.5

        success_keywords = ["success", "completed", "achieved", "resolved"]
        failure_keywords = ["failed", "error", "unsuccessful", "abandoned"]

        successes = sum(
            1 for outcome in outcomes
            if any(kw in outcome.content.lower() for kw in success_keywords)
        )

        failures = sum(
            1 for outcome in outcomes
            if any(kw in outcome.content.lower() for kw in failure_keywords)
        )

        total = successes + failures
        if total == 0:
            return 0.5

        return successes / total

    def _summarize_memory(self, memory: MemoryEntry) -> Dict[str, Any]:
        """Create summary of memory entry."""
        return {
            "id": memory.id,
            "type": memory.type.value,
            "content_preview": memory.content[:200],
            "timestamp": memory.timestamp.isoformat(),
            "source": memory.source,
            "confidence": memory.confidence,
            "tags": memory.tags
        }

    def _extract_keywords(self, text: str) -> List[str]:
        """Extract keywords from text."""
        words = text.lower().split()

        # Remove stop words
        stop_words = {
            "the", "a", "an", "and", "or", "but", "in", "on", "at",
            "to", "for", "of", "with", "by", "from", "is", "are", "was", "were"
        }

        keywords = [
            w.strip(".,!?;:")
            for w in words
            if w not in stop_words and len(w) > 3
        ]

        return keywords[:10]  # Limit to 10 keywords
