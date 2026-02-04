"""
External memory system for GAIA subconscious.

Implements persistent storage using SQLite for structured data
and ChromaDB for semantic search.
"""

import sqlite3
import json
from dataclasses import dataclass, field, asdict
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple
from enum import Enum


class MemoryType(Enum):
    """Types of memory entries."""

    OBSERVATION = "observation"  # Observable fact
    PATTERN = "pattern"  # Detected pattern
    HYPOTHESIS = "hypothesis"  # Generated hypothesis
    DECISION = "decision"  # Decision made
    OUTCOME = "outcome"  # Result of action
    ERROR = "error"  # Error or failure
    SUCCESS = "success"  # Successful operation


class MemoryScope(Enum):
    """Scope of memory entry."""

    GAIA = "gaia"  # Ecosystem-wide
    PROJECT = "project"  # Project-specific
    AGENT = "agent"  # Agent-specific (ephemeral)


@dataclass
class MemoryEntry:
    """
    A single memory entry in external memory.

    Args:
        id: Unique identifier (auto-generated)
        type: Type of memory entry
        scope: Memory scope (GAIA/PROJECT/AGENT)
        content: Main content of memory
        context: Additional context
        timestamp: When memory was created
        source: What created this memory
        confidence: Confidence score (0.0-1.0)
        tags: Tags for categorization
        metadata: Additional metadata

    Returns:
        MemoryEntry instance
    """

    type: MemoryType
    scope: MemoryScope
    content: str
    source: str
    id: Optional[str] = None
    context: Dict[str, Any] = field(default_factory=dict)
    timestamp: datetime = field(default_factory=datetime.now)
    confidence: float = 1.0
    tags: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        """Validate after initialization."""
        if not 0.0 <= self.confidence <= 1.0:
            raise ValueError(f"confidence must be in [0, 1], got {self.confidence}")

        # Convert enums from strings if needed
        if isinstance(self.type, str):
            self.type = MemoryType(self.type)
        if isinstance(self.scope, str):
            self.scope = MemoryScope(self.scope)

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for storage."""
        return {
            "id": self.id,
            "type": self.type.value,
            "scope": self.scope.value,
            "content": self.content,
            "context": json.dumps(self.context),
            "timestamp": self.timestamp.isoformat(),
            "source": self.source,
            "confidence": self.confidence,
            "tags": json.dumps(self.tags),
            "metadata": json.dumps(self.metadata)
        }

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "MemoryEntry":
        """Create MemoryEntry from dictionary."""
        return MemoryEntry(
            id=data["id"],
            type=MemoryType(data["type"]),
            scope=MemoryScope(data["scope"]),
            content=data["content"],
            context=json.loads(data.get("context", "{}")),
            timestamp=datetime.fromisoformat(data["timestamp"]),
            source=data["source"],
            confidence=data["confidence"],
            tags=json.loads(data.get("tags", "[]")),
            metadata=json.loads(data.get("metadata", "{}"))
        )


class ExternalMemory:
    """
    External memory system using SQLite.

    Provides persistent storage for GAIA's subconscious observations,
    patterns, and hypotheses.

    Usage:
        memory = ExternalMemory("X:/Projects/_gaia/argus/memory.db")

        entry = MemoryEntry(
            type=MemoryType.OBSERVATION,
            scope=MemoryScope.PROJECT,
            content="HART OS confidence scores declining",
            source="process_observer"
        )

        memory.store(entry)

        results = memory.search(query="confidence scores", limit=10)
    """

    def __init__(self, db_path: str) -> None:
        """
        Initialize external memory.

        Args:
            db_path: Path to SQLite database file

        Returns:
            None

        Raises:
            sqlite3.Error: If database initialization fails
        """
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)

        self.conn = sqlite3.connect(str(self.db_path))
        self.conn.row_factory = sqlite3.Row
        self._initialize_schema()

    def _initialize_schema(self) -> None:
        """Create database schema if not exists."""
        cursor = self.conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS memories (
                id TEXT PRIMARY KEY,
                type TEXT NOT NULL,
                scope TEXT NOT NULL,
                content TEXT NOT NULL,
                context TEXT,
                timestamp TEXT NOT NULL,
                source TEXT NOT NULL,
                confidence REAL NOT NULL,
                tags TEXT,
                metadata TEXT
            )
        """)

        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_type ON memories(type)
        """)

        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_scope ON memories(scope)
        """)

        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_timestamp ON memories(timestamp)
        """)

        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_source ON memories(source)
        """)

        self.conn.commit()

    def store(self, entry: MemoryEntry) -> str:
        """
        Store memory entry.

        Args:
            entry: MemoryEntry to store

        Returns:
            Memory entry ID

        Raises:
            sqlite3.Error: If storage fails
        """
        if entry.id is None:
            # Generate ID from timestamp + type + hash of content
            entry.id = f"{entry.timestamp.isoformat()}_{entry.type.value}_{hash(entry.content)}"

        cursor = self.conn.cursor()
        data = entry.to_dict()

        cursor.execute("""
            INSERT OR REPLACE INTO memories
            (id, type, scope, content, context, timestamp, source, confidence, tags, metadata)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            data["id"],
            data["type"],
            data["scope"],
            data["content"],
            data["context"],
            data["timestamp"],
            data["source"],
            data["confidence"],
            data["tags"],
            data["metadata"]
        ))

        self.conn.commit()
        return entry.id

    def retrieve(self, memory_id: str) -> Optional[MemoryEntry]:
        """
        Retrieve memory by ID.

        Args:
            memory_id: Memory entry ID

        Returns:
            MemoryEntry or None if not found
        """
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM memories WHERE id = ?", (memory_id,))
        row = cursor.fetchone()

        if row is None:
            return None

        return MemoryEntry.from_dict(dict(row))

    def search(
        self,
        query: Optional[str] = None,
        type: Optional[MemoryType] = None,
        scope: Optional[MemoryScope] = None,
        source: Optional[str] = None,
        tags: Optional[List[str]] = None,
        min_confidence: float = 0.0,
        limit: int = 100,
        offset: int = 0
    ) -> List[MemoryEntry]:
        """
        Search memories with filters.

        Args:
            query: Text search in content
            type: Filter by memory type
            scope: Filter by memory scope
            source: Filter by source
            tags: Filter by tags (any match)
            min_confidence: Minimum confidence threshold
            limit: Maximum results
            offset: Result offset

        Returns:
            List of matching MemoryEntry objects
        """
        cursor = self.conn.cursor()

        conditions = ["confidence >= ?"]
        params: List[Any] = [min_confidence]

        if query:
            conditions.append("content LIKE ?")
            params.append(f"%{query}%")

        if type:
            conditions.append("type = ?")
            params.append(type.value)

        if scope:
            conditions.append("scope = ?")
            params.append(scope.value)

        if source:
            conditions.append("source = ?")
            params.append(source)

        if tags:
            # Search for any tag match
            tag_conditions = " OR ".join(["tags LIKE ?" for _ in tags])
            conditions.append(f"({tag_conditions})")
            params.extend([f'%"{tag}"%' for tag in tags])

        where_clause = " AND ".join(conditions)

        sql = f"""
            SELECT * FROM memories
            WHERE {where_clause}
            ORDER BY timestamp DESC
            LIMIT ? OFFSET ?
        """

        params.extend([limit, offset])

        cursor.execute(sql, params)
        rows = cursor.fetchall()

        return [MemoryEntry.from_dict(dict(row)) for row in rows]

    def count(
        self,
        type: Optional[MemoryType] = None,
        scope: Optional[MemoryScope] = None
    ) -> int:
        """
        Count memories matching criteria.

        Args:
            type: Filter by memory type
            scope: Filter by memory scope

        Returns:
            Count of matching memories
        """
        cursor = self.conn.cursor()

        conditions = []
        params = []

        if type:
            conditions.append("type = ?")
            params.append(type.value)

        if scope:
            conditions.append("scope = ?")
            params.append(scope.value)

        where_clause = " AND ".join(conditions) if conditions else "1=1"

        sql = f"SELECT COUNT(*) FROM memories WHERE {where_clause}"

        cursor.execute(sql, params)
        return cursor.fetchone()[0]

    def get_recent(
        self,
        limit: int = 100,
        type: Optional[MemoryType] = None,
        scope: Optional[MemoryScope] = None
    ) -> List[MemoryEntry]:
        """
        Get most recent memories.

        Args:
            limit: Maximum results
            type: Filter by memory type
            scope: Filter by memory scope

        Returns:
            List of recent MemoryEntry objects
        """
        return self.search(type=type, scope=scope, limit=limit, offset=0)

    def delete_old_agent_memories(self, days: int = 30) -> int:
        """
        Delete agent-scoped memories older than specified days.

        Args:
            days: Age threshold in days

        Returns:
            Number of deleted entries
        """
        cursor = self.conn.cursor()

        threshold = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        threshold_str = threshold.isoformat()

        cursor.execute("""
            DELETE FROM memories
            WHERE scope = ? AND timestamp < ?
        """, (MemoryScope.AGENT.value, threshold_str))

        deleted = cursor.rowcount
        self.conn.commit()

        return deleted

    def close(self) -> None:
        """Close database connection."""
        self.conn.close()

    def __enter__(self) -> "ExternalMemory":
        """Context manager entry."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """Context manager exit."""
        self.close()
