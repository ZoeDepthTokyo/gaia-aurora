"""
MNEMIS - Cross-Project Memory System for GAIA Ecosystem.

Provides hierarchical memory management with enforcement of access contracts,
promotion discipline, and provenance tracking across the GAIA ecosystem.

Constitutional Principles:
- Three-tier hierarchy: GAIA (ecosystem) > PROJECT > AGENT (ephemeral)
- Memory promotion requires explicit approval
- Provenance tracked at every level
- No silent memory drift
"""

__version__ = "0.1.0"
__author__ = "GAIA Ecosystem"

from mnemis.models.memory_models import (
    MemoryAccessLevel,
    MemoryEntry,
    MemoryContract,
    MemoryPromotionProposal,
    MemoryScope,
    MemoryAccessViolation,
)

from mnemis.core.memory_store import MnemisStore
from mnemis.core.contracts import MemoryAccessController
from mnemis.core.promotion import MemoryPromotionEngine
from mnemis.core.search import MemorySearchEngine

__all__ = [
    # Models
    "MemoryAccessLevel",
    "MemoryEntry",
    "MemoryContract",
    "MemoryPromotionProposal",
    "MemoryScope",
    "MemoryAccessViolation",
    # Core
    "MnemisStore",
    "MemoryAccessController",
    "MemoryPromotionEngine",
    "MemorySearchEngine",
]
