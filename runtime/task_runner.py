"""
GAIA Background Task Runner

Provides scheduled task execution for ecosystem maintenance:
- WARDEN compliance scans (daily)
- ARGUS health checks (hourly)
- MNEMIS memory promotion evaluation (daily)
- Stale process detection (every 15 minutes)

Uses APScheduler for scheduling. Can run standalone or embedded.

Usage:
    python -m runtime.task_runner          # Run all scheduled tasks
    python -m runtime.task_runner --once   # Run all tasks once and exit
    python -m runtime.task_runner --list   # List registered tasks
"""
import argparse
import logging
import signal
import sys
from datetime import datetime
from pathlib import Path
from typing import Callable, Dict, List, Optional

logger = logging.getLogger("gaia.runtime")

# Task registry
REGISTERED_TASKS: Dict[str, dict] = {}


def register_task(name: str, func: Callable, schedule: str, description: str = ""):
    """Register a background task.

    Args:
        name: Unique task identifier
        func: Callable to execute
        schedule: Cron-like schedule string ("hourly", "daily", "every_15m")
        description: Human-readable description
    """
    REGISTERED_TASKS[name] = {
        "func": func,
        "schedule": schedule,
        "description": description,
        "last_run": None,
        "last_status": None,
    }


# --- Built-in tasks ---

def task_warden_scan():
    """Run WARDEN compliance scan across all registered projects."""
    from pathlib import Path
    import json

    registry_path = Path("X:/Projects/_GAIA/registry.json")
    if not registry_path.exists():
        logger.warning("Registry not found, skipping WARDEN scan")
        return

    registry = json.loads(registry_path.read_text())
    projects = registry.get("projects", {})

    results = {}
    for key, project in projects.items():
        project_path = Path(project.get("path", ""))
        if project_path.exists():
            try:
                # Import WARDEN scanner
                sys.path.insert(0, str(Path("X:/Projects/_GAIA/_WARDEN")))
                from scanner import ComplianceScanner
                scanner = ComplianceScanner()
                result = scanner.scan(project_path)
                results[key] = {
                    "passed": result.passed,
                    "issues": len(result.issues),
                    "scanned_files": result.scanned_files,
                }
                logger.info(f"WARDEN scan {key}: {'PASS' if result.passed else 'FAIL'} ({len(result.issues)} issues)")
            except Exception as e:
                logger.error(f"WARDEN scan failed for {key}: {e}")
                results[key] = {"error": str(e)}

    return results


def task_health_check():
    """Check ecosystem health: git status, file existence, process status."""
    import json

    registry_path = Path("X:/Projects/_GAIA/registry.json")
    if not registry_path.exists():
        return {"error": "Registry not found"}

    registry = json.loads(registry_path.read_text())
    health = {}

    for key, project in registry.get("projects", {}).items():
        path = Path(project.get("path", ""))
        health[key] = {
            "exists": path.exists(),
            "has_git": (path / ".git").exists() if path.exists() else False,
            "has_tests": bool(list(path.glob("tests/test_*.py"))) if path.exists() else False,
            "has_claude_md": (path / "CLAUDE.md").exists() if path.exists() else False,
        }

    return health


def task_stale_cache_cleanup():
    """Detect and warn about stale __pycache__ directories."""
    import json

    registry_path = Path("X:/Projects/_GAIA/registry.json")
    if not registry_path.exists():
        return

    registry = json.loads(registry_path.read_text())
    stale = []

    for key, project in registry.get("projects", {}).items():
        path = Path(project.get("path", ""))
        if path.exists():
            for cache_dir in path.rglob("__pycache__"):
                stale.append(str(cache_dir))

    if stale:
        logger.info(f"Found {len(stale)} __pycache__ directories across ecosystem")

    return {"cache_dirs": len(stale), "paths": stale[:10]}


# Register built-in tasks
register_task("warden_scan", task_warden_scan, "daily", "WARDEN compliance scan across all projects")
register_task("health_check", task_health_check, "hourly", "Ecosystem health check")
register_task("stale_cache", task_stale_cache_cleanup, "every_15m", "Detect stale __pycache__ directories")


def run_all_once():
    """Run all registered tasks once."""
    results = {}
    for name, task in REGISTERED_TASKS.items():
        logger.info(f"Running task: {name}")
        try:
            result = task["func"]()
            task["last_run"] = datetime.now().isoformat()
            task["last_status"] = "success"
            results[name] = result
        except Exception as e:
            task["last_status"] = f"error: {e}"
            logger.error(f"Task {name} failed: {e}")
            results[name] = {"error": str(e)}
    return results


def list_tasks():
    """Print all registered tasks."""
    print(f"{'Name':<20} {'Schedule':<12} {'Last Run':<25} {'Description'}")
    print("-" * 80)
    for name, task in REGISTERED_TASKS.items():
        print(f"{name:<20} {task['schedule']:<12} {task['last_run'] or 'never':<25} {task['description']}")


def main():
    parser = argparse.ArgumentParser(description="GAIA Background Task Runner")
    parser.add_argument("--once", action="store_true", help="Run all tasks once and exit")
    parser.add_argument("--list", action="store_true", help="List registered tasks")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(name)s] %(levelname)s: %(message)s")

    if args.list:
        list_tasks()
        return

    if args.once:
        results = run_all_once()
        import json
        print(json.dumps(results, indent=2, default=str))
        return

    # Full scheduler mode (requires APScheduler)
    try:
        from apscheduler.schedulers.blocking import BlockingScheduler
        scheduler = BlockingScheduler()

        schedule_map = {
            "hourly": {"hours": 1},
            "daily": {"days": 1},
            "every_15m": {"minutes": 15},
        }

        for name, task in REGISTERED_TASKS.items():
            interval = schedule_map.get(task["schedule"], {"hours": 1})
            scheduler.add_job(task["func"], "interval", **interval, id=name)
            logger.info(f"Scheduled: {name} ({task['schedule']})")

        def shutdown(signum, frame):
            scheduler.shutdown()

        signal.signal(signal.SIGINT, shutdown)
        signal.signal(signal.SIGTERM, shutdown)

        logger.info("GAIA Task Runner started. Press Ctrl+C to stop.")
        scheduler.start()

    except ImportError:
        logger.error("APScheduler not installed. Run: pip install apscheduler")
        logger.info("Falling back to --once mode")
        run_all_once()


if __name__ == "__main__":
    main()
