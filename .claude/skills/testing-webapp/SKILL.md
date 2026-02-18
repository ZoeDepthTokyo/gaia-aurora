---
name: testing-webapp
description: "[CONTEXT] Playwright E2E testing for Streamlit applications on Python 3.14/Windows. Use when adding E2E test coverage to GAIA Streamlit apps (ARGUS dashboard, GAIA Sim, JobPulse, jSeeker). Triggers on: E2E, end-to-end, UI test, Playwright, Streamlit test, integration test. Why: GAIA has 5 Streamlit apps with zero E2E coverage."
---

# testing-webapp

E2E testing for GAIA's Streamlit apps using Playwright on Python 3.14 / Windows 11.

## GAIA Streamlit Apps
| App | Port | Module |
|-----|------|--------|
| ARGUS Dashboard | 8501 | `_ARGUS/dashboard/app.py` |
| GAIA Simulator | 8503 | `_ARGUS/sim/gaia_sim.py` |
| JobPulse | 8504 | `X:\Projects\JobPulse\app.py` |
| VULCAN | - | `_VULCAN/ui/main.py` |

## Setup
```bash
pip install playwright pytest-playwright
python -m playwright install chromium
```

## Writing Tests
```python
# tests/e2e/test_argus_dashboard.py
import pytest
from playwright.sync_api import Page

def test_dashboard_loads(page: Page):
    page.goto("http://localhost:8501")
    page.wait_for_selector('[data-testid="stApp"]', timeout=10000)
    assert "ARGUS" in page.title() or page.locator("h1").count() > 0
```

## Running Tests
```bash
# Start app first, then in another terminal:
python -m pytest tests/e2e/ -v --headed  # visible browser
python -m pytest tests/e2e/ -v           # headless
```

## Windows/Python 3.14 Notes
- Use `python -m pytest` (not bare pytest)
- Playwright subprocess works fine on Python 3.14
- Use `--timeout 30000` for slow Streamlit startup
- Test IDs: use `data-testid` attributes; Streamlit adds `stApp`, `stSidebar`, etc.

## Streamlit-Specific Patterns
```python
# Wait for Streamlit to finish loading (spinner gone)
page.wait_for_function("!document.querySelector('[data-testid=\"stSpinner\"]')")

# Interact with selectbox
page.locator('[data-testid="stSelectbox"]').first.click()
page.get_by_role("option", name="My Option").click()

# Check metric value
metric = page.locator('[data-testid="stMetric"]').first
assert "42" in metric.inner_text()
```

## Integration with GAIA CI
Add to component `pyproject.toml` or `pytest.ini`:
```ini
[tool.pytest.ini_options]
markers = ["e2e: end-to-end tests requiring running server"]
```

Run E2E separately from unit tests:
```bash
python -m pytest -m "not e2e"  # unit tests only (CI default)
python -m pytest -m e2e        # E2E only (manual/nightly)
```
