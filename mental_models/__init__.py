"""
Mental Models Library for GAIA Ecosystem.

Provides 59 mental models across 7 categories for structured analysis:
- Systems Thinking
- Decision Making
- Cognitive Biases
- Learning & Pedagogy
- Quality & Reliability
- Communication
- Temporal

Usage:
    from mental_models import MentalModelSelector, get_model

    selector = MentalModelSelector()
    models = selector.select_for_context("performance degradation detected")

    model = get_model("feedback_loops")
    analysis = model.analyze(data)
"""

from mental_models.models import MentalModel, ModelCategory
from mental_models.selector import MentalModelSelector, get_model

__version__ = "1.0.0"
__all__ = ["MentalModelSelector", "get_model", "MentalModel", "ModelCategory"]
