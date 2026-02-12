# Contract Testing in GAIA Ecosystem

**Owner**: WARDEN
**Updated**: 2026-02-09
**Status**: Active

---

## Overview

Contract testing ensures that Pydantic models serving as interfaces between GAIA modules remain compatible. When VIA imports `Chunk` from MYCEL, or jSeeker imports `Document`, these shared contracts must not break.

**Contract**: A shared Pydantic model that defines the interface between producer and consumer modules.

---

## Cross-Module Contracts

### MYCEL as Producer

MYCEL exports core RAG models used across the ecosystem:

#### 1. `Document` Model
```python
# Producer: X:\Projects\_GAIA\_MYCEL\rag_intelligence\core\models.py
class Document(BaseModel):
    id: str
    content: str
    metadata: Optional[dict[str, Any]] = None
    source: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
```

**Consumers**:
- **VIA** (`X:\Projects\VIA\rag\document_processor.py`) - Imports for investment memo ingestion
- **jSeeker** (`X:\Projects\jSeeker\jseeker\integrations\mycel_bridge.py`) - Imports for resume block indexing
- **DATA FORGE** (planned) - Document compilation pipeline

**Contract Requirements**:
- `id`, `content` must always be present (required fields)
- `metadata` must accept `dict[str, Any]` or None
- `source` and `created_at` are optional but must maintain type signature

---

#### 2. `Chunk` Model
```python
# Producer: X:\Projects\_GAIA\_MYCEL\rag_intelligence\core\models.py
class Chunk(BaseModel):
    id: str
    document_id: str
    content: str
    start_idx: int
    end_idx: int
    metadata: Optional[dict[str, Any]] = None
    source: Optional[str] = None
    timestamp: Optional[datetime] = None
    similarity_score: Optional[float] = None

    @property
    def chunk_id(self) -> str:
        """Alias for id to maintain backward compatibility with synthesizer."""
        return self.id
```

**Consumers**:
- **VIA** (`X:\Projects\VIA\rag\synthesizer.py`) - Imports for claim extraction
- **jSeeker** (planned) - Resume block retrieval

**Contract Requirements**:
- Required fields: `id`, `document_id`, `content`, `start_idx`, `end_idx`
- `chunk_id` property must remain for VIA backward compatibility
- `similarity_score` is optional (set during retrieval, not ingestion)

---

#### 3. `RetrievalResult` Model
```python
# Producer: X:\Projects\_GAIA\_MYCEL\rag_intelligence\core\models.py
class RetrievalResult(BaseModel):
    chunk_id: str
    content: str
    similarity_score: float
    source: Optional[str] = None
    metadata: Optional[dict[str, Any]] = None
```

**Consumers**:
- **VIA** - Query pipeline
- **jSeeker** - Resume block matching

**Contract Requirements**:
- `chunk_id`, `content`, `similarity_score` required
- `similarity_score` must be float (0.0 to 1.0 range expected but not enforced)

---

### jSeeker as Producer

jSeeker models are internal but could be promoted to MYCEL if reusable:

#### `ParsedJD` Model (Internal)
```python
# X:\Projects\jSeeker\jseeker\models.py
class ParsedJD(BaseModel):
    raw_text: str
    pruned_text: str = ""
    title: str = ""
    company: str = ""
    requirements: list[JDRequirement] = Field(default_factory=list)
    ats_keywords: list[str] = Field(default_factory=list)
    # ...
```

**Potential Promotion**: If other projects need JD parsing (e.g., VIA for role-based research), promote to `MYCEL/rag_intelligence/parsing/job_description.py`.

---

### ARGUS as Producer

ARGUS exports telemetry and cost tracking models:

#### `CostEvent` Model (Proposed)
```python
# X:\Projects\_GAIA\_ARGUS\subconscious\models.py (to be created)
class CostEvent(BaseModel):
    timestamp: datetime
    project: str
    model: str
    tokens_in: int
    tokens_out: int
    cost_usd: float
    operation: str  # "chunking", "embedding", "generation", etc.
```

**Consumers**:
- **VIA** - Track Claude Sonnet costs in synthesis
- **jSeeker** - Track resume adaptation LLM costs
- **RAVEN** - Autonomous research cost monitoring

---

## Contract Testing Approach

### 1. Schema Validation
Ensure consumer expectations match producer reality:

```python
# Example contract test
def test_mycel_document_contract():
    """Verify VIA's expectation of MYCEL Document model."""
    from mycel.rag_intelligence.core.models import Document

    # VIA expects these fields
    doc = Document(
        id="test",
        content="Sample content",
        metadata={"source_type": "memo"},
        source="path/to/file.pdf",
    )

    assert hasattr(doc, "id")
    assert hasattr(doc, "content")
    assert hasattr(doc, "metadata")
    assert isinstance(doc.metadata, dict)
    assert doc.created_at  # Must exist
```

### 2. Backward Compatibility Tests
Prevent breaking changes:

```python
def test_chunk_backward_compatibility():
    """Ensure chunk_id property still works (VIA dependency)."""
    from mycel.rag_intelligence.core.models import Chunk

    chunk = Chunk(
        id="chunk_123",
        document_id="doc_456",
        content="Text",
        start_idx=0,
        end_idx=10,
    )

    # VIA uses chunk_id property
    assert chunk.chunk_id == chunk.id
    assert chunk.chunk_id == "chunk_123"
```

### 3. Integration Tests
Test actual cross-module usage:

```python
def test_via_uses_mycel_chunks():
    """Verify VIA can consume MYCEL chunks."""
    from mycel.rag_intelligence.core.models import Chunk
    from via.rag.synthesizer import Synthesizer  # VIA's consumer

    chunks = [
        Chunk(
            id="c1",
            document_id="d1",
            content="Sample claim",
            start_idx=0,
            end_idx=12,
            similarity_score=0.85,
        )
    ]

    synthesizer = Synthesizer()
    # Should not raise type errors
    result = synthesizer.synthesize(chunks, query="test")
    assert result is not None
```

---

## Contract Validator Script

Run `python X:\Projects\_GAIA\runtime\contract_validator.py` to validate all contracts.

**Exit Codes**:
- `0` - All contracts valid
- `1` - Contract validation failed

**Output**:
```
=== GAIA Contract Validator ===

[OK] MYCEL Document model: All required fields present
[OK] MYCEL Chunk model: chunk_id property exists
[FAIL] ARGUS CostEvent: Model not found at expected path
[WARNING] jSeeker ParsedJD: Not yet promoted to MYCEL

Summary: 2 passed, 1 failed, 1 warning
```

---

## Contract Change Protocol

### When to Update a Contract

**SAFE Changes** (non-breaking):
- Add optional fields with defaults
- Add new methods/properties
- Expand enum values (if consumers use `.value` checks)

**BREAKING Changes** (require coordination):
- Remove required fields
- Rename fields
- Change field types
- Remove properties that consumers use

### Change Process

1. **Propose change** in `#gaia-architecture` (if implemented)
2. **Audit consumers** using `contract_validator.py`
3. **Create migration path**:
   - If breaking: Add deprecation warnings, create shim properties
   - Example: Keep `chunk_id` property when renaming `id` to `chunk_id`
4. **Update contract tests** in producer repo
5. **Notify consumer owners** (e.g., VIA owner if MYCEL changes)
6. **Version bump** (semver): Major if breaking, minor if additive

---

## Example: Safe Contract Evolution

**Scenario**: MYCEL needs to add `embedding_version` field to `Chunk`.

**Safe Approach**:
```python
class Chunk(BaseModel):
    # Existing fields
    id: str
    document_id: str
    content: str
    start_idx: int
    end_idx: int

    # New optional field (non-breaking)
    embedding_version: Optional[str] = None  # Default allows old consumers to work
```

**Consumers** (VIA, jSeeker) don't need immediate updates - they ignore the new field.

---

## Example: Breaking Contract Change

**Scenario**: MYCEL wants to rename `similarity_score` to `score` in `Chunk`.

**WRONG Approach**:
```python
# DON'T DO THIS - Breaks VIA/jSeeker immediately
class Chunk(BaseModel):
    score: float  # Renamed from similarity_score
```

**CORRECT Approach** (Deprecation Path):
```python
class Chunk(BaseModel):
    score: float  # New preferred name

    @property
    def similarity_score(self) -> float:
        """Deprecated: Use 'score' instead. Maintained for backward compatibility."""
        import warnings
        warnings.warn(
            "similarity_score is deprecated, use 'score' instead",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.score
```

**Timeline**:
- v0.3.0: Add `score`, keep `similarity_score` as property (deprecation warning)
- v0.4.0: Update all consumers to use `score`
- v0.5.0: Remove `similarity_score` property (major version bump)

---

## Contract Registry

Maintained in `X:\Projects\_GAIA\runtime\contract_validator.py`:

```python
CONTRACTS = {
    "mycel.Document": {
        "producer": "MYCEL",
        "consumers": ["VIA", "jSeeker", "DATA_FORGE"],
        "required_fields": ["id", "content"],
    },
    "mycel.Chunk": {
        "producer": "MYCEL",
        "consumers": ["VIA", "jSeeker"],
        "required_fields": ["id", "document_id", "content", "start_idx", "end_idx"],
        "required_properties": ["chunk_id"],
    },
    "mycel.RetrievalResult": {
        "producer": "MYCEL",
        "consumers": ["VIA", "jSeeker"],
        "required_fields": ["chunk_id", "content", "similarity_score"],
    },
}
```

---

## Future Work

1. **Automated Contract Tests in CI/CD**: Run `contract_validator.py` in pre-commit hooks
2. **Schema Versioning**: Add `__schema_version__ = "1.0"` to models for explicit tracking
3. **Consumer Notification**: WARDEN webhook to alert consumer owners when producer changes models
4. **Contract Documentation Generation**: Auto-generate this doc from Pydantic models

---

## References

- MYCEL Models: `X:\Projects\_GAIA\_MYCEL\rag_intelligence\core\models.py`
- VIA RAG Integration: `X:\Projects\VIA\rag\`
- jSeeker MYCEL Bridge: `X:\Projects\jSeeker\jseeker\integrations\mycel_bridge.py`
- Contract Validator: `X:\Projects\_GAIA\runtime\contract_validator.py`
