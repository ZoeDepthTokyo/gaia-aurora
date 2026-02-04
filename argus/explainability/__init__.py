"""
Layered Explainability System for GAIA.

Provides 4 levels of explanation:
- Simple: One-sentence answer (for beginners)
- Default: Balanced explanation with key points
- Metaphor: Uses analogies and comparisons
- Advanced: Deep technical details with references

Usage:
    from argus.explainability import Explainer, ExplanationLevel

    explainer = Explainer()

    # Get explanation at different levels
    simple = explainer.explain(topic, level=ExplanationLevel.SIMPLE)
    advanced = explainer.explain(topic, level=ExplanationLevel.ADVANCED)
"""

from argus.explainability.explainer import Explainer, ExplanationLevel, Explanation
from argus.explainability.template_manager import TemplateManager

__version__ = "1.0.0"
__all__ = ["Explainer", "ExplanationLevel", "Explanation", "TemplateManager"]
