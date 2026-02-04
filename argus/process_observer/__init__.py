"""
Process Observer - Non-Intervening Sense-Making Agent.

The Process Observer watches system behavior, detects patterns,
and generates hypotheses WITHOUT intervening in execution.

This is pure reflective cognition - observe, analyze, propose, never execute.

Constitutional constraints:
- Read-only access to all project state
- Cannot execute tools or modify code
- Cannot update memory above AGENT tier
- Produces hypotheses, not actions
- Must explain reasoning transparently

Usage:
    from argus.process_observer import ProcessObserver

    observer = ProcessObserver(memory_path="X:/Projects/_gaia/argus/memory.db")

    # Run observation cycle
    report = observer.observe_ecosystem()

    print(f"Patterns detected: {len(report['patterns'])}")
    print(f"Hypotheses generated: {len(report['hypotheses'])}")
"""

from argus.process_observer.observer import ProcessObserver, ObservationReport
from argus.process_observer.post_mortem import PostMortemAnalyzer, PostMortem

__version__ = "1.0.0"
__all__ = ["ProcessObserver", "ObservationReport", "PostMortemAnalyzer", "PostMortem"]
