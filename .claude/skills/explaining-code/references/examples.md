# Explain Code — Detailed Examples

## Example 1: File-Level Explanation (Simple)

```
/explaining-code _MYCEL/rag_intelligence/core/retrieval.py
```

Output:
```
Retrieval Engine (MYCEL Core)
==============================

Purpose: Semantic search over embedded documents with reranking.

Key Functions:
1. retrieve(query, top_k)      → Vector similarity search
2. rerank(candidates, query)   → Cross-encoder scoring
3. hybrid_search(query, alpha) → Semantic + keyword combined

GAIA Integration:
- Uses ARGUS mental models for search strategy selection
- Stores results in MNEMIS (PROJECT tier) for caching
- Constitutional: Read-only (no data modification)

Design Pattern: Strategy (swappable embedding models)
Performance: <100ms retrieval on 10K docs
```

## Example 2: Component Architecture

```
/explaining-code _VULCAN --architecture
```

Output:
```
VULCAN Architecture (The Forge)
================================

Flow: User → HITL Questionnaire → Adapter → Scaffold → Registry

Components:
1. ui/main.py         — 7-step questionnaire (Streamlit)
2. questionnaire.py   — Question logic, maps to project type
3. adapters/          — Strategy pattern (hart/via/forge)
4. scaffolder.py      — Generates dirs, templates, CLAUDE.md
5. registry_manager.py — Adds entry to registry.json

Constitutional:
✅ Glass-box: All generation steps visible
✅ HITL: User approves before creation
✅ Sovereignty: User can modify output freely

Position: VULCAN (Create) → LOOM (Edit) → ARGUS (Monitor)
```

## Example 3: Expert-Level Pattern Analysis

```
/explaining-code _ARGUS/subconscious/pattern_detector.py --level expert
```

Output:
```
Pattern Detector (ARGUS Subconscious)
======================================

Algorithm: Sliding Window + Mental Model Matching

1. Temporal Windowing — 5-min windows, 50% overlap
2. Feature Extraction — event types, frequencies, sequences
3. Mental Model Selection — 59 models, heuristic matching
4. Hypothesis Generation — DetectedPattern + confidence (0.0-1.0)

Constitutional:
- Read-only (never modifies state)
- Hypothesis-driven (possibilities, not certainties)
- Transparent (reasoning included in output)

Optimizations:
- LRU cache (100 entries) for mental model selections
- Debounce: max 10 events/sec
- Async: doesn't block main workflow

Trade-offs:
- Sliding window vs real-time streaming
  → Better for bursty events; cost: 5-min detection delay
- Local vs distributed
  → GAIA is local-first; cost: no cross-machine aggregation
```
