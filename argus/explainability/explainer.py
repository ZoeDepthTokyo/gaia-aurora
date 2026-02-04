"""
Core explainer with 4-level explanation system.

Generates explanations at appropriate complexity levels based on
user's current understanding and growth ladder position.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, Any, Optional, List
from datetime import datetime


class ExplanationLevel(Enum):
    """Levels of explanation complexity."""

    SIMPLE = "simple"  # One sentence, no jargon
    DEFAULT = "default"  # Balanced, key points
    METAPHOR = "metaphor"  # Uses analogies
    ADVANCED = "advanced"  # Technical depth


@dataclass
class Explanation:
    """
    An explanation at a specific level.

    Args:
        topic: What is being explained
        level: Explanation level
        content: Main explanation content
        examples: Concrete examples
        next_steps: What to learn next
        related_topics: Related concepts
        references: Sources or documentation links
        generated_at: When explanation was generated
        metadata: Additional data

    Returns:
        Explanation instance
    """

    topic: str
    level: ExplanationLevel
    content: str
    examples: List[str] = field(default_factory=list)
    next_steps: List[str] = field(default_factory=list)
    related_topics: List[str] = field(default_factory=list)
    references: List[str] = field(default_factory=list)
    generated_at: datetime = field(default_factory=datetime.now)
    metadata: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        """Validate after initialization."""
        if isinstance(self.level, str):
            self.level = ExplanationLevel(self.level)

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return {
            "topic": self.topic,
            "level": self.level.value,
            "content": self.content,
            "examples": self.examples,
            "next_steps": self.next_steps,
            "related_topics": self.related_topics,
            "references": self.references,
            "generated_at": self.generated_at.isoformat(),
            "metadata": self.metadata
        }

    def format_markdown(self) -> str:
        """Format explanation as markdown."""
        lines = [
            f"# {self.topic}",
            "",
            f"**Level:** {self.level.value.title()}",
            "",
            self.content,
            ""
        ]

        if self.examples:
            lines.extend([
                "## Examples",
                ""
            ])
            for example in self.examples:
                lines.append(f"- {example}")
            lines.append("")

        if self.next_steps:
            lines.extend([
                "## Next Steps",
                ""
            ])
            for step in self.next_steps:
                lines.append(f"1. {step}")
            lines.append("")

        if self.related_topics:
            lines.extend([
                "## Related Topics",
                ""
            ])
            for topic in self.related_topics:
                lines.append(f"- {topic}")
            lines.append("")

        if self.references:
            lines.extend([
                "## References",
                ""
            ])
            for ref in self.references:
                lines.append(f"- {ref}")
            lines.append("")

        return "\n".join(lines)


class Explainer:
    """
    Multi-level explainer for GAIA concepts.

    Generates explanations at 4 different levels of complexity,
    adapting to user's current understanding.

    Usage:
        explainer = Explainer()

        # Explain at simple level
        simple = explainer.explain("feedback loops", ExplanationLevel.SIMPLE)
        print(simple.content)

        # Explain at advanced level
        advanced = explainer.explain("feedback loops", ExplanationLevel.ADVANCED)
        print(advanced.content)

        # Auto-select level based on user's growth rung
        explanation = explainer.explain_for_user("feedback loops", growth_rung=3)
    """

    def __init__(self) -> None:
        """Initialize explainer with templates."""
        self.templates = self._load_templates()

    def _load_templates(self) -> Dict[str, Dict[ExplanationLevel, Dict[str, Any]]]:
        """Load explanation templates for common GAIA concepts."""
        return {
            "feedback_loops": {
                ExplanationLevel.SIMPLE: {
                    "content": "A feedback loop is when the output of a process feeds back as input, creating a cycle.",
                    "examples": [
                        "Error causes retry, retry causes error (bad loop)",
                        "Success builds confidence, confidence improves success (good loop)"
                    ],
                    "next_steps": [
                        "Identify feedback loops in your projects",
                        "Determine if loops are reinforcing or balancing"
                    ]
                },
                ExplanationLevel.DEFAULT: {
                    "content": """A feedback loop occurs when a system's output influences its own input, creating a circular relationship.

Feedback loops can be:
- **Reinforcing**: Amplify change (positive feedback)
- **Balancing**: Stabilize system (negative feedback)

In GAIA, feedback loops appear in:
- Error patterns (errors causing more errors)
- Cost spirals (inefficiency causing resource constraints)
- Learning cycles (success enabling more success)""",
                    "examples": [
                        "Hallucination loop: LLM generates false info → system accepts it → uses it in next prompt → more hallucinations",
                        "Cost spiral: High token usage → budget concerns → rushed optimization → bugs → more debugging → more token usage",
                        "Trust building: Transparent errors → user understands → accepts system limits → provides better input → fewer errors"
                    ],
                    "next_steps": [
                        "Map feedback loops in your system",
                        "Identify which are reinforcing vs balancing",
                        "Design interventions to break bad loops"
                    ],
                    "related_topics": [
                        "Systems thinking",
                        "Second-order effects",
                        "Emergence"
                    ]
                },
                ExplanationLevel.METAPHOR: {
                    "content": """Think of feedback loops like a thermostat and furnace:

**Balancing loop (thermostat):**
- Room gets cold → thermostat triggers heat → room warms → thermostat stops heat → room cools
- System maintains stable temperature

**Reinforcing loop (microphone feedback):**
- Sound from speaker → picked up by mic → amplified by speaker → picked up by mic (louder) → amplified (even louder)
- System spirals out of control

In GAIA, you want:
- **Balancing loops** for stability (error correction, cost management)
- **Reinforcing loops** for growth (learning, trust building)

The key is recognizing which loop you're in and whether it serves your goals.""",
                    "examples": [
                        "Like compound interest: Small improvements reinforce over time (good)",
                        "Like a snowball rolling downhill: Small problems accumulate mass (bad)",
                        "Like cruise control: System self-corrects to maintain speed (good)"
                    ],
                    "next_steps": [
                        "Draw your system as a loop diagram",
                        "Identify the 'thermostat' (balancing mechanisms)",
                        "Find the 'microphone' (runaway amplifiers)"
                    ]
                },
                ExplanationLevel.ADVANCED: {
                    "content": """Feedback loops in control systems theory are characterized by:

**Transfer Function**: H(s) = G(s) / (1 + G(s)H(s))

Where G(s) is forward path gain and H(s) is feedback path gain.

**Loop Dynamics:**
- **Positive feedback** (G·H > 1): System becomes unstable, oscillates or diverges
- **Negative feedback** (G·H < 1): System stabilizes around setpoint

**In GAIA Architecture:**

```python
# Balancing loop: Process Observer
observation → pattern_detection → hypothesis → user_review → memory_update → refined_pattern_detection

# Reinforcing loop: Trust building
transparency → user_understanding → better_input → better_output → more_transparency

# Dangerous loop: Hallucination cascade
false_memory → retrieval → prompt_contamination → LLM_hallucination → stored_as_memory
```

**Breaking Bad Loops:**
1. **Insert human gate**: User approval breaks automation
2. **Add confidence threshold**: Low confidence blocks propagation
3. **Implement circuit breaker**: Detect loop, halt process
4. **Expire ephemeral memory**: Agent memory doesn't persist

**Design Pattern:**
```python
class FeedbackLoopGuard:
    def __init__(self, max_iterations: int = 3):
        self.iteration_count = 0
        self.max_iterations = max_iterations

    def check_loop(self, state: Any) -> bool:
        self.iteration_count += 1
        if self.iteration_count > self.max_iterations:
            raise CircuitBreakerException("Feedback loop detected")
        return True
```
""",
                    "examples": [
                        "Retrieval-augmented generation with contaminated context",
                        "Distributed system cascading failures",
                        "Neural network gradient explosion"
                    ],
                    "next_steps": [
                        "Implement loop detection in critical paths",
                        "Add telemetry for iteration counts",
                        "Design circuit breakers for known loop patterns"
                    ],
                    "references": [
                        "Meadows, D. (2008). Thinking in Systems",
                        "GAIA_BIBLE.md: Authority Graph",
                        "SR_COUNCIL_ANALYSIS.md: Reflective vs Executive Cognition"
                    ]
                }
            },
            "mental_models": {
                ExplanationLevel.SIMPLE: {
                    "content": "Mental models are frameworks for understanding and analyzing problems.",
                    "examples": [
                        "First principles: Break down to fundamentals",
                        "Feedback loops: Circular cause and effect",
                        "Margin of safety: Build in buffers"
                    ]
                },
                ExplanationLevel.DEFAULT: {
                    "content": """Mental models are structured ways of thinking about problems.

GAIA provides 59 mental models across 7 categories:
- Systems Thinking (8 models)
- Decision Making (8 models)
- Cognitive Biases (7 models)
- Learning & Pedagogy (8 models)
- Quality & Reliability (8 models)
- Communication (6 models)
- Temporal (6 models)

**Why mental models matter:**
- Provide consistent analytical frameworks
- Reduce ad-hoc reasoning
- Make thinking explicit and auditable
- Enable knowledge transfer""",
                    "examples": [
                        "Use 'First Principles' for architectural decisions",
                        "Apply 'Confirmation Bias' check when detecting patterns",
                        "Invoke 'Graceful Degradation' for error handling"
                    ],
                    "related_topics": [
                        "Pattern detection",
                        "Hypothesis generation",
                        "Process Observer"
                    ]
                }
            }
        }

    def explain(
        self,
        topic: str,
        level: ExplanationLevel = ExplanationLevel.DEFAULT
    ) -> Optional[Explanation]:
        """
        Generate explanation for topic at specified level.

        Args:
            topic: Topic to explain
            level: Explanation level

        Returns:
            Explanation or None if topic not found
        """
        topic_key = topic.lower().replace(" ", "_")

        if topic_key not in self.templates:
            return None

        template = self.templates[topic_key].get(level)
        if not template:
            # Fall back to default level
            template = self.templates[topic_key].get(ExplanationLevel.DEFAULT)
            if not template:
                return None

        return Explanation(
            topic=topic,
            level=level,
            content=template["content"],
            examples=template.get("examples", []),
            next_steps=template.get("next_steps", []),
            related_topics=template.get("related_topics", []),
            references=template.get("references", [])
        )

    def explain_for_user(
        self,
        topic: str,
        growth_rung: int = 1
    ) -> Optional[Explanation]:
        """
        Generate explanation at appropriate level for user's growth rung.

        Args:
            topic: Topic to explain
            growth_rung: User's current growth ladder rung (1-5)

        Returns:
            Explanation at appropriate level
        """
        # Map growth rung to explanation level
        level_map = {
            1: ExplanationLevel.SIMPLE,     # Creator: Just started
            2: ExplanationLevel.METAPHOR,   # Explorer: Learning patterns
            3: ExplanationLevel.DEFAULT,    # Adapter: Understanding architecture
            4: ExplanationLevel.ADVANCED,   # Architect: Deep technical
            5: ExplanationLevel.ADVANCED    # Mentor: Teaching others
        }

        level = level_map.get(growth_rung, ExplanationLevel.DEFAULT)
        return self.explain(topic, level)

    def add_custom_explanation(
        self,
        topic: str,
        level: ExplanationLevel,
        content: str,
        examples: Optional[List[str]] = None,
        next_steps: Optional[List[str]] = None
    ) -> None:
        """
        Add custom explanation template.

        Args:
            topic: Topic identifier
            level: Explanation level
            content: Explanation content
            examples: Optional examples
            next_steps: Optional next steps

        Returns:
            None
        """
        topic_key = topic.lower().replace(" ", "_")

        if topic_key not in self.templates:
            self.templates[topic_key] = {}

        self.templates[topic_key][level] = {
            "content": content,
            "examples": examples or [],
            "next_steps": next_steps or []
        }

    def list_topics(self) -> List[str]:
        """
        List all available topics.

        Returns:
            List of topic identifiers
        """
        return list(self.templates.keys())
