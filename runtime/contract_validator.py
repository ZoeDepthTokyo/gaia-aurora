"""
GAIA Contract Validator

Validates that Pydantic models serving as cross-module contracts maintain
expected fields and properties. Detects breaking changes before they impact consumers.

Usage:
    python contract_validator.py
    python contract_validator.py --verbose
"""

import importlib
import sys
from dataclasses import dataclass
from typing import Any, Dict, List

# Contract registry: defines expected interfaces
CONTRACTS = {
    "mycel.Document": {
        "producer": "MYCEL",
        "module_path": "rag_intelligence.core.models",
        "class_name": "Document",
        "consumers": ["VIA", "jSeeker", "DATA_FORGE"],
        "required_fields": ["id", "content", "created_at"],
        "optional_fields": ["metadata", "source"],
        "field_types": {
            "id": str,
            "content": str,
            "metadata": (dict, type(None)),
            "source": (str, type(None)),
        },
    },
    "mycel.Chunk": {
        "producer": "MYCEL",
        "module_path": "rag_intelligence.core.models",
        "class_name": "Chunk",
        "consumers": ["VIA", "jSeeker"],
        "required_fields": [
            "id",
            "document_id",
            "content",
            "start_idx",
            "end_idx",
        ],
        "optional_fields": ["metadata", "source", "timestamp", "similarity_score"],
        "required_properties": ["chunk_id"],
        "field_types": {
            "id": str,
            "document_id": str,
            "content": str,
            "start_idx": int,
            "end_idx": int,
        },
    },
    "mycel.RetrievalResult": {
        "producer": "MYCEL",
        "module_path": "rag_intelligence.core.models",
        "class_name": "RetrievalResult",
        "consumers": ["VIA", "jSeeker"],
        "required_fields": ["chunk_id", "content", "similarity_score"],
        "optional_fields": ["source", "metadata"],
        "field_types": {
            "chunk_id": str,
            "content": str,
            "similarity_score": float,
        },
    },
}


@dataclass
class ValidationResult:
    """Result of contract validation."""

    contract_name: str
    passed: bool
    errors: List[str]
    warnings: List[str]

    @property
    def status(self) -> str:
        """Get validation status."""
        if self.errors:
            return "FAIL"
        elif self.warnings:
            return "WARNING"
        return "OK"


class ContractValidator:
    """Validates cross-module Pydantic contracts."""

    def __init__(self, verbose: bool = False):
        """
        Initialize validator.

        Args:
            verbose: Print detailed validation info
        """
        self.verbose = verbose
        self.results: List[ValidationResult] = []

    def validate_all(self) -> bool:
        """
        Validate all registered contracts.

        Returns:
            True if all contracts valid, False otherwise
        """
        print("=== GAIA Contract Validator ===\n")

        for contract_name, contract_spec in CONTRACTS.items():
            result = self.validate_contract(contract_name, contract_spec)
            self.results.append(result)
            self._print_result(result)

        return self._print_summary()

    def validate_contract(self, contract_name: str, spec: Dict[str, Any]) -> ValidationResult:
        """
        Validate a single contract.

        Args:
            contract_name: Name of contract (e.g., "mycel.Document")
            spec: Contract specification dictionary

        Returns:
            ValidationResult with errors/warnings
        """
        errors = []
        warnings = []

        # Try to import the model
        try:
            model_class = self._import_model(spec)
        except ImportError as e:
            errors.append(f"Failed to import: {e}")
            return ValidationResult(contract_name, False, errors, warnings)

        # Validate required fields
        model_fields = self._get_model_fields(model_class)
        for field in spec.get("required_fields", []):
            if field not in model_fields:
                errors.append(f"Missing required field: {field}")
            elif self.verbose:
                print(f"  ✓ Field '{field}' present")

        # Validate field types
        for field, expected_type in spec.get("field_types", {}).items():
            if field in model_fields:
                actual_type = model_fields[field].annotation
                if not self._check_type_compatibility(actual_type, expected_type):
                    errors.append(
                        f"Field '{field}' type mismatch: expected {expected_type}, got {actual_type}"
                    )

        # Validate required properties
        for prop in spec.get("required_properties", []):
            if not hasattr(model_class, prop):
                errors.append(f"Missing required property: {prop}")
            elif not isinstance(getattr(model_class, prop), property):
                warnings.append(f"'{prop}' exists but is not a property")
            elif self.verbose:
                print(f"  ✓ Property '{prop}' present")

        # Check for deprecated fields (warnings only)
        optional_fields = spec.get("optional_fields", [])
        for field in optional_fields:
            if field not in model_fields:
                warnings.append(f"Optional field '{field}' not found (may be deprecated)")

        passed = len(errors) == 0
        return ValidationResult(contract_name, passed, errors, warnings)

    def _import_model(self, spec: Dict[str, Any]) -> type:
        """
        Import model class from specification.

        Args:
            spec: Contract specification

        Returns:
            Model class

        Raises:
            ImportError: If model cannot be imported
        """
        module_path = spec["module_path"]
        class_name = spec["class_name"]

        # Try to import (will fail if MYCEL not in path)
        try:
            module = importlib.import_module(module_path)
            return getattr(module, class_name)
        except (ImportError, AttributeError) as e:
            raise ImportError(f"Cannot import {module_path}.{class_name}: {e}")

    def _get_model_fields(self, model_class: type) -> Dict[str, Any]:
        """
        Get Pydantic model fields.

        Args:
            model_class: Pydantic model class

        Returns:
            Dictionary of field name to FieldInfo
        """
        if hasattr(model_class, "model_fields"):
            # Pydantic v2
            return model_class.model_fields
        elif hasattr(model_class, "__fields__"):
            # Pydantic v1
            return model_class.__fields__
        return {}

    def _check_type_compatibility(self, actual: Any, expected: Any) -> bool:
        """
        Check if actual type is compatible with expected type.

        Args:
            actual: Actual type annotation
            expected: Expected type (may be tuple for union types)

        Returns:
            True if compatible
        """
        # Simple check - could be expanded for complex generics
        if isinstance(expected, tuple):
            # Union type (e.g., str | None)
            return any(self._type_matches(actual, exp_type) for exp_type in expected)
        return self._type_matches(actual, expected)

    def _type_matches(self, actual: Any, expected: type) -> bool:
        """Check if types match (handles Optional, etc.)."""
        # Convert string annotations to actual types
        actual_str = str(actual)

        if expected is str:
            return "str" in actual_str
        elif expected is int:
            return "int" in actual_str
        elif expected is float:
            return "float" in actual_str
        elif expected is dict:
            return "dict" in actual_str
        elif expected is type(None):
            return "None" in actual_str or "Optional" in actual_str

        return False

    def _print_result(self, result: ValidationResult):
        """Print validation result."""
        status_color = {
            "OK": "\033[92m",  # Green
            "WARNING": "\033[93m",  # Yellow
            "FAIL": "\033[91m",  # Red
        }
        reset = "\033[0m"

        status = result.status
        color = status_color.get(status, "")
        print(f"{color}[{status}]{reset} {result.contract_name}")

        if result.errors:
            for error in result.errors:
                print(f"  ERROR: {error}")

        if result.warnings and self.verbose:
            for warning in result.warnings:
                print(f"  WARNING: {warning}")

        if self.verbose and result.passed and not result.warnings:
            consumers = CONTRACTS[result.contract_name].get("consumers", [])
            print(f"  Consumers: {', '.join(consumers)}")

        print()

    def _print_summary(self) -> bool:
        """Print summary and return overall pass/fail."""
        passed = sum(1 for r in self.results if r.passed)
        failed = sum(1 for r in self.results if not r.passed)
        warned = sum(1 for r in self.results if r.warnings and r.passed)

        print("=" * 50)
        print(f"Summary: {passed} passed, {failed} failed, {warned} warnings")
        print("=" * 50)

        return failed == 0


def main():
    """Main entry point."""
    verbose = "--verbose" in sys.argv or "-v" in sys.argv

    validator = ContractValidator(verbose=verbose)
    success = validator.validate_all()

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
