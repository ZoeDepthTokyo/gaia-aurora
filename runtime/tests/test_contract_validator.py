"""
Tests for contract validator.
"""

from unittest.mock import MagicMock, patch

import pytest

from runtime.contract_validator import CONTRACTS, ContractValidator, ValidationResult


class TestContractValidator:
    """Test suite for ContractValidator."""

    def test_validation_result_status(self):
        """Test ValidationResult status property."""
        # OK status
        result = ValidationResult("test", True, [], [])
        assert result.status == "OK"

        # WARNING status
        result = ValidationResult("test", True, [], ["warning"])
        assert result.status == "WARNING"

        # FAIL status
        result = ValidationResult("test", False, ["error"], [])
        assert result.status == "FAIL"

    def test_validator_initialization(self):
        """Test validator can be initialized."""
        validator = ContractValidator(verbose=False)
        assert validator.verbose is False
        assert validator.results == []

        validator_verbose = ContractValidator(verbose=True)
        assert validator_verbose.verbose is True

    def test_contract_registry_structure(self):
        """Test CONTRACTS registry has expected structure."""
        assert "mycel.Document" in CONTRACTS
        assert "mycel.Chunk" in CONTRACTS
        assert "mycel.RetrievalResult" in CONTRACTS

        # Check Document contract
        doc_contract = CONTRACTS["mycel.Document"]
        assert doc_contract["producer"] == "MYCEL"
        assert "required_fields" in doc_contract
        assert "id" in doc_contract["required_fields"]
        assert "content" in doc_contract["required_fields"]

    def test_get_model_fields_pydantic_v2(self):
        """Test _get_model_fields with Pydantic v2."""
        validator = ContractValidator()

        # Mock Pydantic v2 model
        mock_model = MagicMock()
        mock_model.model_fields = {"field1": "info1", "field2": "info2"}

        fields = validator._get_model_fields(mock_model)
        assert fields == {"field1": "info1", "field2": "info2"}

    def test_get_model_fields_pydantic_v1(self):
        """Test _get_model_fields with Pydantic v1."""
        validator = ContractValidator()

        # Mock Pydantic v1 model
        mock_model = MagicMock()
        del mock_model.model_fields  # Remove v2 attribute
        mock_model.__fields__ = {"field1": "info1"}

        fields = validator._get_model_fields(mock_model)
        assert fields == {"field1": "info1"}

    def test_type_matches_string(self):
        """Test _type_matches for string types."""
        validator = ContractValidator()

        assert validator._type_matches("str", str) is True
        assert validator._type_matches("int", str) is False
        assert validator._type_matches("Optional[str]", str) is True

    def test_type_matches_int(self):
        """Test _type_matches for int types."""
        validator = ContractValidator()

        assert validator._type_matches("int", int) is True
        assert validator._type_matches("str", int) is False

    def test_type_matches_optional(self):
        """Test _type_matches for Optional types."""
        validator = ContractValidator()

        assert validator._type_matches("Optional[str]", type(None)) is True
        assert validator._type_matches("str | None", type(None)) is True

    def test_check_type_compatibility_simple(self):
        """Test _check_type_compatibility with simple types."""
        validator = ContractValidator()

        assert validator._check_type_compatibility("str", str) is True
        assert validator._check_type_compatibility("int", int) is True
        assert validator._check_type_compatibility("str", int) is False

    def test_check_type_compatibility_union(self):
        """Test _check_type_compatibility with union types."""
        validator = ContractValidator()

        # Union type (str | None)
        assert validator._check_type_compatibility("Optional[str]", (str, type(None))) is True
        assert validator._check_type_compatibility("str | None", (str, type(None))) is True

    def test_import_model_failure(self):
        """Test _import_model with non-existent module."""
        validator = ContractValidator()

        spec = {
            "module_path": "nonexistent.module",
            "class_name": "NonExistent",
        }

        with pytest.raises(ImportError):
            validator._import_model(spec)

    def test_validate_contract_import_failure(self):
        """Test validate_contract with import failure."""
        validator = ContractValidator()

        spec = {
            "module_path": "nonexistent.module",
            "class_name": "NonExistent",
            "required_fields": ["id"],
        }

        result = validator.validate_contract("test.Contract", spec)

        assert result.passed is False
        assert len(result.errors) > 0
        assert "Failed to import" in result.errors[0]

    @patch("runtime.contract_validator.importlib.import_module")
    def test_validate_contract_missing_field(self, mock_import):
        """Test validate_contract detects missing required field."""
        validator = ContractValidator()

        # Mock model with incomplete fields
        mock_model = MagicMock()
        mock_model.model_fields = {"id": MagicMock()}  # Missing 'content' field

        mock_module = MagicMock()
        mock_module.MockModel = mock_model
        mock_import.return_value = mock_module

        spec = {
            "module_path": "test.module",
            "class_name": "MockModel",
            "required_fields": ["id", "content"],
        }

        result = validator.validate_contract("test.Contract", spec)

        assert result.passed is False
        assert any("Missing required field: content" in err for err in result.errors)

    @patch("runtime.contract_validator.importlib.import_module")
    def test_validate_contract_missing_property(self, mock_import):
        """Test validate_contract detects missing required property."""
        validator = ContractValidator()

        # Mock model without required property
        mock_model = MagicMock()
        mock_model.model_fields = {"id": MagicMock()}
        del mock_model.chunk_id  # Remove property

        mock_module = MagicMock()
        mock_module.MockModel = mock_model
        mock_import.return_value = mock_module

        spec = {
            "module_path": "test.module",
            "class_name": "MockModel",
            "required_fields": ["id"],
            "required_properties": ["chunk_id"],
        }

        result = validator.validate_contract("test.Contract", spec)

        assert result.passed is False
        assert any("Missing required property: chunk_id" in err for err in result.errors)

    def test_validate_all_structure(self):
        """Test validate_all returns bool and populates results."""
        validator = ContractValidator()

        # Mock validate_contract to return passing results
        with patch.object(validator, "validate_contract") as mock_validate:
            mock_validate.return_value = ValidationResult("test", True, [], [])

            result = validator.validate_all()

            # Should have validated all contracts
            assert len(validator.results) == len(CONTRACTS)
            assert isinstance(result, bool)
