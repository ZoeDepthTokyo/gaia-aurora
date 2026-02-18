# Python Testing Patterns for GAIA Autonomous Loops

Reference for `/running-autonomous-loop` when tasks involve test writing or test-driven development.

## GAIA pytest Conventions

### Import Mode
Always use `--import-mode=importlib` when running cross-submodule tests:
```bash
python -m pytest _ARGUS/tests/ _LOOM/tests/ --import-mode=importlib
```

### Coverage Targets
| Component | Minimum | Target |
|-----------|---------|--------|
| MYCEL     | 80%     | 90%    |
| VULCAN    | 60%     | 75%    |
| ARGUS     | 50%     | 80%    |
| LOOM      | 50%     | 70%    |
| MNEMIS    | 50%     | 70%    |
| WARDEN    | 50%     | 70%    |

### Test File Naming
- Unit tests: `tests/test_<module>.py`
- Spec tests: `tests/test_spec_<domain>.py` (GWT scenarios)
- Integration: `tests/test_integration_<feature>.py`
- E2E: `tests/e2e/test_<app>.py`

### GWT (Given-When-Then) Pattern
```python
class TestFeatureName:
    """Spec: changes/<name>/specs/<component>.md"""

    def test_scenario_description(self):
        # GIVEN: setup state
        data = create_test_fixture()

        # WHEN: trigger action
        result = function_under_test(data)

        # THEN: verify outcome
        assert result.status == "expected"
```

### Subprocess Testing (for CLI scripts)
```python
import subprocess
import sys

def run_script(script_path, *args, env=None, cwd=None):
    """Run a Python script and return CompletedProcess."""
    return subprocess.run(
        [sys.executable, str(script_path), *args],
        capture_output=True, text=True,
        env={**os.environ, **(env or {})},
        cwd=str(cwd) if cwd else None
    )
```

### Fixtures for GAIA Root
```python
@pytest.fixture
def gaia_root(tmp_path):
    """Create a minimal GAIA-like directory structure."""
    (tmp_path / "registry.json").write_text('{"projects": []}')
    (tmp_path / ".claude" / "skills").mkdir(parents=True)
    (tmp_path / "changes").mkdir()
    return tmp_path
```

### Windows/Python 3.14 Gotchas
- Always use `python -m pytest` (not bare `pytest`)
- Forward slashes in path strings even on Windows
- Emoji in print statements fail on cp1252 -- use ASCII indicators
- `tmp_path` fixture works correctly on Windows
