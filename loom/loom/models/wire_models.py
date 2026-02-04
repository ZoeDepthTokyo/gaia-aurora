"""
Wire and connection models for LOOM.

Represents data flow connections between agents with type validation.
"""

from typing import Any, Optional, Dict
from enum import Enum
from pydantic import BaseModel, Field


class WireType(str, Enum):
    """Types of wires connecting agents."""
    DATA = "data"  # Standard data flow
    CONTROL = "control"  # Control flow (triggers)
    MEMORY = "memory"  # Memory access
    FEEDBACK = "feedback"  # Feedback loops


class WireValidationError(Exception):
    """Raised when wire connection is invalid."""
    pass


class Wire(BaseModel):
    """
    Wire connecting two agent nodes.

    Constitutional principle: All data flow is explicit and traceable.

    Attributes:
        id: Unique wire identifier
        wire_type: Type of wire
        source_node_id: Source agent ID
        source_port: Source output port name
        target_node_id: Target agent ID
        target_port: Target input port name
        transformation: Optional transformation function
        validation_schema: Optional validation rules
        metadata: Additional wire metadata
    """
    id: str
    wire_type: WireType
    source_node_id: str
    source_port: str
    target_node_id: str
    target_port: str
    transformation: Optional[str] = None
    validation_schema: Optional[Dict[str, Any]] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)

    def validate_connection(
        self,
        source_type: str,
        target_type: str
    ) -> None:
        """
        Validate that source and target types are compatible.

        Args:
            source_type: Source output type
            target_type: Target input type

        Raises:
            WireValidationError: If types incompatible
        """
        # Type compatibility matrix
        compatible_types = {
            "str": ["str", "Any"],
            "int": ["int", "float", "str", "Any"],
            "float": ["float", "str", "Any"],
            "bool": ["bool", "str", "Any"],
            "dict": ["dict", "Any"],
            "list": ["list", "Any"],
            "Any": ["Any"],
        }

        if source_type not in compatible_types:
            raise WireValidationError(f"Unknown source type: {source_type}")

        if target_type not in compatible_types[source_type]:
            raise WireValidationError(
                f"Incompatible types: {source_type} -> {target_type}"
            )

    def to_serializable(self) -> Dict[str, Any]:
        """
        Convert to JSON-serializable format.

        Returns:
            Dictionary representation
        """
        return self.model_dump(mode='json')


class WireBundle(BaseModel):
    """
    Bundle of related wires (for visual grouping).

    Attributes:
        id: Bundle identifier
        name: Bundle name
        wires: Wire IDs in bundle
        color: Visual color (for UI)
        description: What this bundle represents
    """
    id: str
    name: str
    wires: list[str]
    color: Optional[str] = None
    description: str = ""
