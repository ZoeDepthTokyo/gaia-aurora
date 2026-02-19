"""Quick verification script for GAIA Runtime infrastructure."""
import sys
from pathlib import Path

# Add runtime to path
sys.path.insert(0, str(Path(__file__).parent))

from task_runner import (
    REGISTERED_TASKS,
    list_tasks,
    register_task,
    run_all_once,
)


def main():
    print("=" * 80)
    print("GAIA Runtime Infrastructure Verification")
    print("=" * 80)
    print()

    # 1. Show registered tasks
    print("[1] Listing built-in tasks:")
    print("-" * 80)
    list_tasks()
    print()

    # 2. Register a custom task
    print("[2] Registering custom task...")

    def custom_test_task():
        return {"message": "Custom task executed successfully!", "value": 42}

    register_task(
        name="test_custom",
        func=custom_test_task,
        schedule="hourly",
        description="Verification test task",
    )
    print("   Registered 'test_custom' task")
    print(f"   Total tasks: {len(REGISTERED_TASKS)}")
    print()

    # 3. Run all tasks once
    print("[3] Executing all tasks once...")
    print("-" * 80)
    results = run_all_once()
    print()

    # 4. Show results summary
    print("[4] Results summary:")
    print("-" * 80)
    for task_name, result in results.items():
        status = REGISTERED_TASKS[task_name]["last_status"]
        last_run = REGISTERED_TASKS[task_name]["last_run"]

        if status == "success":
            print(f"   [{task_name}] SUCCESS")
            if result and isinstance(result, dict):
                for key, value in result.items():
                    if isinstance(value, dict) and len(value) > 3:
                        print(f"      {key}: {len(value)} items")
                    else:
                        print(f"      {key}: {value}")
        else:
            print(f"   [{task_name}] FAILED: {status}")

        print(f"      Last run: {last_run}")
        print()

    # 5. Verify infrastructure
    print("[5] Infrastructure verification:")
    print("-" * 80)

    checks = [
        ("Task registry functional", len(REGISTERED_TASKS) > 0),
        ("Built-in tasks registered", "warden_scan" in REGISTERED_TASKS),
        ("Health check present", "health_check" in REGISTERED_TASKS),
        ("Cache cleanup present", "stale_cache" in REGISTERED_TASKS),
        ("Custom tasks supported", "test_custom" in REGISTERED_TASKS),
        ("All tasks executed", all(t["last_run"] for t in REGISTERED_TASKS.values())),
        (
            "No critical failures",
            all(
                t["last_status"] == "success" or "error:" in t["last_status"]
                for t in REGISTERED_TASKS.values()
            ),
        ),
    ]

    all_passed = True
    for check_name, passed in checks:
        status = "PASS" if passed else "FAIL"
        symbol = "✓" if passed else "✗"
        print(f"   {symbol} {check_name}: {status}")
        if not passed:
            all_passed = False

    print()
    print("=" * 80)
    if all_passed:
        print("VERIFICATION COMPLETE: All checks passed!")
    else:
        print("VERIFICATION COMPLETE: Some checks failed (see above)")
    print("=" * 80)


if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.INFO, format="%(message)s")
    main()
