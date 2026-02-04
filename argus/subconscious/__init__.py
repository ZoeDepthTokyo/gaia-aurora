"""
GAIA Subconscious Layer.

The subconscious layer provides:
- External memory system (SQLite + ChromaDB)
- Background pattern detection agent
- Context enrichment and pre-loading
- Hypothesis generation

This layer operates transparently in the background, enriching
GAIA's analytical capabilities without intervening in execution.
"""

from argus.subconscious.memory import ExternalMemory, MemoryEntry
from argus.subconscious.pattern_detector import PatternDetector, DetectedPattern
from argus.subconscious.context_enricher import ContextEnricher
from argus.subconscious.hypothesis_generator import HypothesisGenerator, Hypothesis

__version__ = "1.0.0"
__all__ = [
    "ExternalMemory",
    "MemoryEntry",
    "PatternDetector",
    "DetectedPattern",
    "ContextEnricher",
    "HypothesisGenerator",
    "Hypothesis"
]
