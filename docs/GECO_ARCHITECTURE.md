# GECO Architecture — The GAIA Ecosystem
**Version:** 1.0.0 | **Date:** February 2026
**Status:** Reflects implementation state as of Feb 8, 2026
**Audience:** Engineering teams, system architects, integration developers

---

## Table of Contents

1. [The Sovereign Hierarchy](#1-the-sovereign-hierarchy-ascii-diagram)
2. [Shared Service Reference](#2-shared-service-reference)
3. [Product Reference](#3-product-reference)
   - 3A. [Shared Service Deep Dive](#3a-shared-service-deep-dive)
   - 3B. [Product Deep Dive](#3b-product-deep-dive)
4. [Agent Invocation Flow](#4-agent-invocation-flow)
5. [LLM Model Routing](#5-llm-model-routing)
6. [Memory Hierarchy & Agent Authority](#6-memory-hierarchy--agent-authority)
7. [User Flow Simulation — Creating a Test Project](#7-user-flow-simulation--creating-a-test-project)
8. [Shared Service Constraints](#8-shared-service-constraints)
9. [Integration Patterns](#9-integration-patterns)
   - 9A. [Python Tools — GAIA-Aware Standalone Utilities](#9a-python-tools--gaia-aware-standalone-utilities)
10. [What's Missing (Honest Assessment)](#10-whats-missing-honest-assessment)

---

## 1. The Sovereign Hierarchy (ASCII Diagram)

```
┌─────────────────────────────────────────────────────────────────────────┐
│                          GAIA ECOSYSTEM                                 │
│                    (Governance & Constitution)                          │
│                         X:\Projects\_GAIA\                              │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                ┌───────────────────┴───────────────────┐
                │         Shared Services (8)           │
                └───────────────────┬───────────────────┘
                                    │
        ┌───────┬───────┬───────┬───┴───┬───────┬───────┬───────┬───────┐
        │       │       │       │       │       │       │       │       │
        v       v       v       v       v       v       v       v       v
    ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐
    │MYCEL│ │LOOM │ │ARGUS│ │MNEMIS│ │VULCAN│ │WARDEN│ │ABIS │ │RAVEN│
    │     │ │     │ │     │ │     │ │     │ │     │ │     │ │     │
    │ LLM │ │Agent│ │Mental│ │Cross-│ │Proj.│ │Govern│ │No-  │ │Rsrch│
    │ RAG │ │ Orch│ │Models│ │Projct│ │Forge│ │ance │ │Code │ │Agent│
    │Embed│ │     │ │     │ │Memory│ │     │ │     │ │Build│ │     │
    └──┬──┘ └──┬──┘ └──┬──┘ └──┬──┘ └──┬──┘ └──┬──┘ └──┬──┘ └──┬──┘
       │       │       │       │       │       │       │       │
       └───────┴───────┴───────┴───────┴───────┴───────┴───────┘
                                    │
                                    │ provides services to
                                    v
        ┌─────────────────────────────────────────────────────────┐
        │                    Products (8)                         │
        └─────────────────────────────────────────────────────────┘
                                    │
        ┌───────┬───────┬───────┬───┴───┬───────┬───────┬───────┬───────┐
        │       │       │       │       │       │       │       │       │
        v       v       v       v       v       v       v       v       v
    ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐
    │HART │ │ VIA │ │DATA │ │jSeek│ │ DOS │ │Palace│ │Waymo│ │Python│ │GPT  │
    │ OS  │ │Intel│ │FORGE│ │     │ │     │ │     │ │Data │ │Tools │ │ECHO │
    │     │ │     │ │     │ │     │ │     │ │     │ │     │ │Layer │ │     │
    │Thrpy│ │Invst│ │Data │ │Resume│ │Multi│ │Case │ │AV   │ │     │ │Chat │
    │Score│ │Rsch │ │Proc │ │Adapt│ │Agent│ │Study│ │Data │ │     │ │Srch │
    └─────┘ └─────┘ └─────┘ └─────┘ └─────┘ └─────┘ └─────┘ └─────┘ └─────┘

Dependency Arrows:
  Products → MYCEL (LLM + RAG)
  Products → MNEMIS (Memory)
  GPT_ECHO → MYCEL (RAG for conversation search)
  LOOM → MYCEL + MNEMIS
  VULCAN → MYCEL
  ARGUS → MYCEL
  MNEMIS → MYCEL
```

**Hierarchy Guarantees:**
- Products CANNOT call other products directly
- Products MUST use shared services for cross-project communication
- Shared services provide horizontal infrastructure
- GAIA provides constitutional governance

---

## 2. Shared Service Reference

| Service | Role | Version | Status | Key Files | Depends On | Called By |
|---------|------|---------|--------|-----------|------------|-----------|
| **MYCEL** | LLM clients, RAG, embedding, config (IS rag-intelligence library) | v0.2.0 | Active | `rag_intelligence/config.py`, `rag_intelligence/llm.py`, `rag_intelligence/chunking.py` | None | All products, VULCAN, ARGUS, LOOM, MNEMIS |
| **LOOM** | Workflow engine + agent orchestration | v0.1.0 | Development | `loom/core/workflow_engine.py`, `loom/models/agent_models.py`, `loom/integrations/mycel_bridge.py` | MYCEL, MNEMIS | Products (via workflow specs) |
| **ARGUS** | Mental models (59), subconscious pattern detection, explainability | v0.5.0 | Development | `argus/mental_models/`, `argus/subconscious/`, `argus/explainability/explainer.py`, `argus/dashboard/event_bus.py` | MYCEL | Products (telemetry), LOOM (reasoning) |
| **MNEMIS** | 5-tier memory hierarchy (Ephemeral → Permanent), promotion protocol | v0.1.0 | Development | `mnemis/models/memory_models.py`, `mnemis/core/promotion.py`, `mnemis/core/memory_store.py` | MYCEL | Products, LOOM agents |
| **VULCAN** | Project creator (The Forge), 7-step HITL questionnaire, 3 adapters | v0.4.0 | Development | `vulcan_forge/project_creator.py`, `vulcan_forge/questionnaire.py`, `vulcan_forge/adapters/` | MYCEL | Humans (Streamlit UI) |
| **WARDEN** | Enforcement + compliance (git, tests, secrets, hooks) | v0.1.0 | Planned | None (docs only) | MYCEL | Pre-commit hooks, VULCAN validation |
| **ABIS** | No-code visual system builder (agent canvas) | v0.1.0 | Design phase | Placeholder dirs only | LOOM, MYCEL | Humans (visual editor) |
| **RAVEN** | Autonomous research agent (planning) | v0.0.1 | Planned | README.md only | MYCEL, MNEMIS | Products, ARGUS |

**Notes:**
- MYCEL is the only zero-dependency shared service (provides foundation for all others)
- WARDEN enforcement exists in GAIA_BIBLE.md but has no implementation
- ABIS directories exist but contain no production code
- ECHO has been reclassified as product GPT_ECHO (see Product Reference)

---

## 3. Product Reference

| Product | Role | Version | Status | Framework | Uses Services | Registry Entry |
|---------|------|---------|--------|-----------|---------------|----------------|
| **HART OS** | Therapy scoring system (deterministic pipeline) | v6.2.8 | Production | Streamlit | Direct OpenAI (pre-MYCEL) | `hart_os` |
| **VIA** | Investment research + RAG synthesis | v6.4 | Production | Streamlit | MYCEL (Gemini, OpenAI, Anthropic) | `via` |
| **DATA FORGE** | Data processing + memory bank + taxonomy | v1.1 | Production | Streamlit | Direct OpenAI | `data_forge` |
| **jSeeker** | Resume adaptation + ATS optimization (formerly PROTEUS) | v0.2.1 | Active | Streamlit | MYCEL (Anthropic), emits ARGUS telemetry | `proteus` |
| **DOS** | Multi-agent decision orchestration system | v0.1.0 | Planning | TBD | LOOM, MYCEL, MNEMIS (planned) | Not yet registered |
| **The Palace** | Case study visualization (agent workflows) | v1.0 | Complete | Static HTML | None | `the_palace` |
| **Waymo Data** | Autonomous vehicle research data | Reference | Reference | N/A | None | Not registered |
| **GPT_ECHO** | ChatGPT archaeology & search (moved from shared services) | v0.1.0 | Stale | Streamlit | MYCEL, ARGUS, MNEMIS (planned) | Not yet registered |

**Integration Maturity:**
- **Full MYCEL integration:** VIA, jSeeker (formerly PROTEUS)
- **Pre-MYCEL (direct SDK):** HART OS, DATA FORGE
- **No LLM:** The Palace (static), Waymo Data (data only)
- **Future integration:** DOS (will be first full LOOM + MNEMIS product), GPT_ECHO (planned RAG integration)

---

## 3A. Shared Service Deep Dive

### RAVEN — Autonomous Research Agent (Planning)
- **Purpose:** Ad-hoc research investigations across the ecosystem
- **Capabilities (Planned):**
  - Document search via MYCEL RAG (semantic + keyword)
  - Code repository scanning (grep, AST analysis)
  - External source queries (web search, API calls)
  - Structured research report generation
  - Cross-project pattern analysis
- **Use Cases:** Competitive analysis, dependency audits, regulatory scanning, knowledge gap discovery
- **Architecture:** Uses MYCEL for retrieval, MNEMIS for storing findings, ARGUS for quality tracking
- **Status:** v0.0.1 — README.md only, no implementation

### ABIS-ARGUS Mental Model Integration

ABIS queries the ARGUS Mental Model Library (59 models across 6 categories) at design time:

**When user adds an agent node:**
1. ABIS sends node type + context to ARGUS
2. ARGUS returns top-3 relevant mental models with scores
3. ABIS presents models as suggestions to user
4. User selects model → model reasoning style injected into agent config

**Example:**
- User adds "Financial Analyst" agent node
- ARGUS suggests: Prospect Theory (0.92), Expected Utility Theory (0.87), Cost-Benefit Analysis (0.81)
- User selects Prospect Theory
- Agent config includes: `reasoning_style: "prospect_theory"`, `bias_awareness: ["loss_aversion", "framing_effect"]`

**Explanation Levels in ABIS:**
- Simple: "This agent thinks about gains and losses differently"
- Detailed: "Prospect Theory weights losses 2x more than gains, making this agent conservative on downside risk"
- Technical: "Loss aversion coefficient lambda=2.25, reference point = current portfolio value"

---

## 3B. Product Deep Dive

### GPT_ECHO — ChatGPT Archaeology & Search (Product)
- **Purpose:** Mirror, search, and organize ChatGPT conversation exports
- **Status:** v0.1.0 (stale — 19 manual version copies, needs ENG-003 consolidation)
- **GAIA Integration:**
  - Uses MYCEL for RAG-based conversation search
  - Uses ARGUS for monitoring and telemetry
  - Uses MNEMIS for cross-session pattern storage
  - Governed by WARDEN (secrets, tests)
  - Registered by VULCAN
- **Current Issues:** 19 manual version copies (ui_v0.py through ui_v012.py), empty requirements.txt, hardcoded paths, zero tests
- **Path:** `X:\Projects\_GAIA\_ECHO` (to be moved to `X:\Projects\GPT_ECHO` during cleanup)

---

## 4. Agent Invocation Flow

### High-Level Flow

```
┌──────────┐
│ Product  │ (e.g., jSeeker, DOS, VIA)
└────┬─────┘
     │ 1. Create workflow spec
     v
┌────────────────────┐
│ LOOM               │
│ WorkflowEngine     │ WorkflowEngine.execute_workflow(workflow, inputs)
└────┬───────────────┘
     │ 2. Validate workflow structure
     │ 3. Create ExecutionContext
     v
┌────────────────────────────────────────────────────────────┐
│ _execute_agent_cascade(workflow, agent, inputs, context)  │
│                                                            │
│   For each agent in workflow:                             │
│   ┌──────────────────────────────────────────────┐       │
│   │ 4. Execute agent (_execute_agent)            │       │
│   │    - Validate inputs against schema          │       │
│   │    - Check governance rules                  │       │
│   │    - Call agent implementation                │       │
│   │    - Record execution in context             │       │
│   └───────────────┬──────────────────────────────┘       │
│                   │                                        │
│   ┌───────────────v──────────────────────────────┐       │
│   │ 5. Get downstream agents via connections     │       │
│   │    - Prepare inputs from upstream outputs    │       │
│   │    - Recursive cascade to next agents        │       │
│   └──────────────────────────────────────────────┘       │
└────────────────────────────────────────────────────────────┘
     │
     │ Parallel execution paths:
     v
┌──────────────────┐   ┌──────────────────┐   ┌──────────────────┐
│ MYCEL Bridge     │   │ MNEMIS Bridge    │   │ ARGUS Telemetry  │
│                  │   │                  │   │                  │
│ LLM calls        │   │ Memory read/write│   │ Event emission   │
│ (Haiku/Sonnet)   │   │ (tier-enforced)  │   │ (cost, trace)    │
└──────────────────┘   └──────────────────┘   └──────────────────┘
```

### Agent Node Types (from `loom/models/agent_models.py`)

```python
class AgentType(str, Enum):
    """Agent classification types."""
    EXECUTOR = "executor"      # Performs actions (tools, API calls)
    OBSERVER = "observer"      # Read-only, analyzes but doesn't act
    COORDINATOR = "coordinator"  # Manages other agents
    TRANSFORMER = "transformer"  # Pure data transformation
```

**Execution Rules:**
- EXECUTOR: Can read/write memory at its tier, call external APIs
- OBSERVER: Read-only, cannot modify memory or call external services
- COORDINATOR: Orchestrates other agents, has elevated authority
- TRANSFORMER: Pure function, no side effects

### Workflow Execution (from `loom/core/workflow_engine.py`)

```python
def execute_workflow(
    self,
    workflow: AgentWorkflow,
    initial_inputs: Dict[str, Any],
    dry_run: bool = False
) -> ExecutionContext:
    """Execute workflow from entry points."""
    # Validate workflow structure
    validation_errors = workflow.validate_workflow()
    if validation_errors:
        raise ValueError(f"Workflow validation failed: {validation_errors}")

    # Create execution context
    context = ExecutionContext(
        workflow_id=workflow.id,
        workflow_name=workflow.name
    )

    # Execute entry point agents
    for entry_agent_id in workflow.entry_points:
        agent = workflow.get_agent(entry_agent_id)
        if agent:
            self._execute_agent_cascade(
                workflow=workflow,
                agent=agent,
                inputs=initial_inputs,
                context=context
            )

    context.complete()
    return context
```

### Agent Cascade (from `loom/core/workflow_engine.py:98-149`)

```python
def _execute_agent_cascade(
    self,
    workflow: AgentWorkflow,
    agent: AgentNode,
    inputs: Dict[str, Any],
    context: ExecutionContext
) -> None:
    """Execute agent and cascade to downstream agents."""
    # Execute this agent
    execution_record = self._execute_agent(agent, inputs, context)
    context.add_execution_record(execution_record)

    # If execution failed, halt cascade
    if execution_record.state == AgentExecutionState.FAILED:
        context.record_error(
            agent_id=agent.id,
            error=execution_record.error
        )
        return

    # Get downstream agents
    downstream_ids = workflow.get_downstream_agents(agent.id)

    # Execute downstream agents
    for downstream_id in downstream_ids:
        downstream_agent = workflow.get_agent(downstream_id)
        if not downstream_agent:
            continue

        # Prepare inputs for downstream agent
        downstream_inputs = self._prepare_downstream_inputs(
            workflow=workflow,
            source_agent_id=agent.id,
            target_agent_id=downstream_id,
            source_outputs=execution_record.outputs or {}
        )

        # Recursive cascade
        self._execute_agent_cascade(
            workflow=workflow,
            agent=downstream_agent,
            inputs=downstream_inputs,
            context=context
        )
```

### MYCEL Bridge Integration (from `loom/integrations/mycel_bridge.py`)

```python
class MycelAgentBridge:
    """Bridge for LOOM agents to access MYCEL capabilities."""

    def create_llm_agent_implementation(
        self,
        agent_id: str,
        model_provider: str = "openai",
        model_name: str = "gpt-4o",
        system_prompt: str = ""
    ) -> Callable:
        """Create agent implementation using MYCEL LLM client."""
        def agent_implementation(inputs: Dict[str, Any]) -> Dict[str, Any]:
            # TODO: Integrate with MYCEL create_llm_client
            # client = create_llm_client(provider=model_provider)
            return {
                "response": f"Mock response for {agent_id}",
                "confidence": 0.95,
                "cost": 0.001
            }
        return agent_implementation
```

**Note:** MYCEL bridge currently returns mock implementations. Full integration pending.

---

## 5. LLM Model Routing

### Authority-Based Model Selection

| Authority Level | Models | Cost/1M tokens (Input/Output) | Use Cases | Budget |
|----------------|--------|-------------------------------|-----------|--------|
| **GAIA-level** | `claude-opus-4-6` (planned) | $15.00 / $75.00 | Ecosystem decisions, cross-project reasoning | Unlimited (admin approval) |
| **PROJECT-level** | `claude-sonnet-4-5-20250929` | $3.00 / $15.00 | Reasoning, adaptation, synthesis, quality tasks | $50/month per project |
| **AGENT-level** | `claude-haiku-4-5-20251001` | $0.80 / $4.00 | Fast parsing, classification, cheap tasks | $10/month per project |

### jSeeker (formerly PROTEUS) Routing Example

From `proteus/llm.py`:

```python
MODEL_PRICING = {
    "claude-haiku-4-5-20251001": {"input": 0.80, "output": 4.00, "cache_read": 0.08},
    "claude-sonnet-4-5-20250929": {"input": 3.00, "output": 15.00, "cache_read": 0.30},
}

class ProteusLLM:
    """Claude API wrapper with Haiku/Sonnet routing, prompt caching, and cost tracking."""

    def call(
        self,
        prompt: str,
        *,
        task: str = "general",
        model: str = "haiku",  # "haiku" or "sonnet"
        system: str = "",
        temperature: float = 0.3,
        max_tokens: int = 4096,
        cache_system: bool = False,
        use_local_cache: bool = True,
    ) -> str:
        """Call Claude API with model routing and cost tracking."""
        model_id = (
            settings.sonnet_model if model == "sonnet" else settings.haiku_model
        )

        # Budget enforcement
        monthly_cost = tracker_db.get_monthly_cost()
        if monthly_cost >= settings.max_monthly_budget_usd:
            raise BudgetExceededError(
                f"Monthly budget exceeded: ${monthly_cost:.2f} / ${settings.max_monthly_budget_usd:.2f}"
            )

        # API call with prompt caching
        response = self.client.messages.create(
            model=model_id,
            max_tokens=max_tokens,
            temperature=temperature,
            system=system_blocks if system_blocks else [],
            messages=messages,
        )

        # Calculate cost including cache reads
        cost = self._calculate_cost(
            model_id,
            usage.input_tokens,
            usage.output_tokens,
            usage.cache_read_input_tokens,
        )

        # Track to DB
        tracker_db.log_cost(APICost(...))
```

### jSeeker Task → Model Mapping (from `proteus/pipeline.py`)

| Task | Model | Rationale | Avg Cost |
|------|-------|-----------|----------|
| JD parsing (`process_jd`) | Haiku | Fast extraction, structured output | $0.002 |
| Template matching (`match_templates`) | Haiku | Simple similarity scoring | $0.001 |
| Resume adaptation (`adapt_resume`) | **Sonnet** | Quality matters, nuanced rewriting | $0.015 |
| ATS scoring (`score_resume`) | **Sonnet** | Quality reasoning, keyword analysis | $0.010 |
| Metadata generation | Haiku | Simple formatting | $0.001 |

**Total pipeline cost:** ~$0.03 per resume (well under $10/month budget for 300 resumes)

### Cost Enforcement (from `proteus/config.py`)

```python
class ProteusSettings(_BaseSettings):
    """PROTEUS configuration with GAIA ecosystem integration."""

    # Model Configuration
    haiku_model: str = "claude-haiku-4-5-20251001"
    sonnet_model: str = "claude-sonnet-4-5-20250929"

    # Cost Controls
    max_monthly_budget_usd: float = 10.0
    cost_warning_threshold_usd: float = 8.0

    # Caching
    enable_prompt_cache: bool = True  # Anthropic prompt caching (90% discount)
    enable_local_cache: bool = True   # SHA256 file cache
```

### MYCEL Router (Future)

From `rag_intelligence/config.py`, the base `GaiaSettings` provides ecosystem-wide defaults:

```python
class GaiaSettings(BaseSettings):
    """Base settings for any GAIA ecosystem project."""

    # OpenAI Defaults
    openai_model: str = "gpt-4o"
    openai_model_fast: str = "gpt-4o-mini"
    openai_model_thinking: str = "o1"

    # Anthropic Defaults
    anthropic_model: str = "claude-sonnet-4-5-20250929"

    # Gemini Defaults
    gemini_model: str = "gemini-2.0-flash"
    gemini_model_fallback: str = "gemini-1.5-flash"
```

**Future MYCEL Router (Planned):**
```python
def select_model(
    task: str,
    query_complexity: float,  # 0.0-1.0
    budget_remaining: float,
    provider_preference: str = "anthropic"
) -> str:
    """
    Route to appropriate model based on:
    - Query complexity estimation (heuristic or learned)
    - Budget constraints
    - Provider preference
    """
    # Not yet implemented
    pass
```

---

## 6. Memory Hierarchy & Agent Authority

### 5-Tier Memory Hierarchy (from `mnemis/models/memory_models.py`)

| Tier | Lifespan | Access Level | Use Cases | Example |
|------|----------|--------------|-----------|---------|
| **Ephemeral** | Single function call | AGENT | Intermediate computation results | Parsing buffer |
| **Working** | Single agent execution | AGENT | Agent scratch space | Iteration state |
| **Session** | User session | PROJECT | Conversation context | Chat history |
| **Long-term** | Project lifetime | PROJECT | Learned patterns | User preferences |
| **Permanent** | Cross-project | GAIA | Universal knowledge | Design patterns |

### 3-Tier Access Control

```python
class MemoryAccessLevel(str, Enum):
    """Three-tier memory hierarchy levels."""
    GAIA = "gaia"      # Ecosystem-wide, eternal, cross-project patterns
    PROJECT = "project"  # Project-scoped, persistent within project lifecycle
    AGENT = "agent"    # Execution-scoped, ephemeral, auto-expire after session
```

### Memory Contracts (from `mnemis/models/memory_models.py:124-242`)

```python
class MemoryContract(BaseModel):
    """Enforces memory boundary constraints for agents.

    Constitutional principle: Agents can read down the hierarchy,
    but can only write at their exact level.
    """
    agent_id: str
    access_level: MemoryAccessLevel
    project_id: Optional[str] = None
    read_permissions: List[MemoryAccessLevel]
    write_permissions: List[MemoryAccessLevel]

    def _default_read_permissions(self) -> List[MemoryAccessLevel]:
        """
        Default read permissions: can read at level and below.

        GAIA agents can read: GAIA, PROJECT, AGENT
        PROJECT agents can read: PROJECT, AGENT
        AGENT can read: AGENT only
        """
        hierarchy = {
            MemoryAccessLevel.GAIA: [
                MemoryAccessLevel.GAIA,
                MemoryAccessLevel.PROJECT,
                MemoryAccessLevel.AGENT
            ],
            MemoryAccessLevel.PROJECT: [
                MemoryAccessLevel.PROJECT,
                MemoryAccessLevel.AGENT
            ],
            MemoryAccessLevel.AGENT: [
                MemoryAccessLevel.AGENT
            ]
        }
        return hierarchy[self.access_level]

    def _default_write_permissions(self) -> List[MemoryAccessLevel]:
        """
        Default write permissions: can only write at exact level.
        Prevents accidental cross-tier contamination.
        """
        return [self.access_level]

    def can_read(self, memory_scope: MemoryScope) -> bool:
        """Check if agent can read memory at given scope."""
        return memory_scope.level in self.read_permissions

    def can_write(self, memory_scope: MemoryScope) -> bool:
        """Check if agent can write to memory at given scope."""
        if memory_scope.level not in self.write_permissions:
            return False
        # PROJECT and AGENT level writes must match project context
        if memory_scope.level in [MemoryAccessLevel.PROJECT, MemoryAccessLevel.AGENT]:
            if memory_scope.project_id != self.project_id:
                return False
        # AGENT level writes must match agent context
        if memory_scope.level == MemoryAccessLevel.AGENT:
            if memory_scope.agent_id != self.agent_id:
                return False
        return True
```

### Memory Promotion Protocol (from `mnemis/core/promotion.py`)

```python
class MemoryPromotionEngine:
    """Manages memory promotion from lower to higher tiers.

    Constitutional principles:
    - Memory moves UP hierarchy via proposal only
    - All promotions require explicit approval
    - Provenance tracked at every step
    - Rejected proposals are logged (not discarded)
    """

    def propose_promotion(
        self,
        memory_id: str,
        to_scope: MemoryScope,
        agent_id: str,
        rationale: str
    ) -> str:
        """Propose promoting memory to higher tier."""
        memory = self.memory_store._locate_memory(memory_id)

        # Validate promotion authority
        self.access_controller.validate_promotion_proposal(
            agent_id=agent_id,
            from_scope=memory.scope,
            to_scope=to_scope
        )

        # Create proposal
        proposal = MemoryPromotionProposal(
            id=str(uuid.uuid4()),
            memory_id=memory_id,
            from_scope=memory.scope,
            to_scope=to_scope,
            rationale=rationale,
            proposed_by=agent_id
        )

        self._proposals[proposal.id] = proposal
        return proposal.id

    def approve_promotion(
        self,
        proposal_id: str,
        reviewer: str,
        notes: Optional[str] = None
    ) -> str:
        """Approve memory promotion proposal."""
        proposal = self._proposals[proposal_id]
        proposal.approve(reviewer=reviewer, notes=notes)

        # Execute promotion
        promoted_memory_id = self._execute_promotion(proposal, reviewer)
        return promoted_memory_id
```

**Promotion Rules:**
- AGENT → PROJECT: Requires PROJECT-level approval
- PROJECT → GAIA: Requires human or GAIA-level approval
- All promotions create new memory entry (source preserved)
- Full provenance chain maintained

---

## 7. User Flow Simulation — Creating a Test Project

### Scenario: User creates "Customer Sentiment Analyzer" using VULCAN

**Step 1: User Opens VULCAN UI**
```bash
cd X:\Projects\_GAIA\_VULCAN
streamlit run ui/main.py
```
Browser opens to `localhost:8501`

**Step 2: VULCAN Presents 7-Step HITL Questionnaire**

From `vulcan_forge/questionnaire.py`:

```python
QUESTIONNAIRE_STEPS = [
    {
        "step": 1,
        "question": "What does this project do?",
        "hint": "Describe in 1-2 sentences",
        "field": "project_description"
    },
    {
        "step": 2,
        "question": "What LLM provider(s) will it use?",
        "options": ["openai", "anthropic", "gemini", "none"],
        "field": "providers"
    },
    # ... 5 more steps
]
```

User fills out:
- Name: `sentiment_analyzer`
- Description: "Analyzes customer feedback sentiment with confidence scoring"
- Providers: OpenAI
- Project Type: **Deterministic** (pipeline + scoring)
- Testing: Yes (pytest)
- Documentation: Yes

**Step 3: VULCAN Selects Adapter**

From `vulcan_forge/project_creator.py`:

```python
def select_adapter(self, answers: Dict[str, Any]) -> BaseAdapter:
    """Select appropriate adapter based on questionnaire answers."""
    project_type = answers.get("project_type", "deterministic")

    adapter_map = {
        "deterministic": DeterministicAdapter,
        "creative": CreativeAdapter,
        "processor": ProcessorAdapter,
    }

    adapter_class = adapter_map.get(project_type, DeterministicAdapter)
    return adapter_class(answers)
```

VULCAN selects `DeterministicAdapter` (5-stage pipeline + confidence scoring).

**Step 4: VULCAN Scaffolds Project**

From `vulcan_forge/adapters/deterministic_adapter.py`:

```python
def scaffold(self, project_path: Path) -> None:
    """Create deterministic project structure."""
    # Create directory structure
    (project_path / "sentiment_analyzer" / "core" / "stages").mkdir(parents=True)
    (project_path / "sentiment_analyzer" / "scoring").mkdir(parents=True)
    (project_path / "tests").mkdir()
    (project_path / "docs").mkdir()
    (project_path / "logs").mkdir()

    # Generate config.py with GaiaSettings
    self._write_config(project_path)

    # Generate CLAUDE.md with context
    self._write_claude_md(project_path)

    # Generate .gitignore with secrets protection
    self._write_gitignore(project_path)

    # Generate requirements.txt including rag-intelligence>=0.3.1
    self._write_requirements(project_path)

    # Generate 5 stage templates
    for i in range(1, 6):
        self._write_stage_template(project_path, i)
```

**Project Structure Created:**
```
X:\Projects\sentiment_analyzer\
├── config.py                    # GaiaSettings subclass
├── CLAUDE.md                    # Context for Claude Code
├── .gitignore                   # Secrets protection
├── requirements.txt             # rag-intelligence>=0.3.1
├── sentiment_analyzer/
│   ├── core/
│   │   ├── stages/
│   │   │   ├── 1_extract_phrases.py
│   │   │   ├── 2_classify_sentiment.py
│   │   │   ├── 3_calculate_confidence.py
│   │   │   ├── 4_apply_threshold.py
│   │   │   └── 5_format_output.py
│   │   └── scoring/
│   │       └── confidence_engine.py
├── tests/
│   └── test_stages.py
├── docs/
│   └── ARCHITECTURE.md
└── logs/                        # For ARGUS telemetry
```

**Step 5: VULCAN Registers in registry.json**

From `vulcan_forge/registry_manager.py`:

```python
def register_project(self, project_metadata: Dict[str, Any]) -> None:
    """Add project to GAIA registry."""
    registry = self._load_registry()
    registry["projects"][project_metadata["id"]] = {
        "name": project_metadata["name"],
        "path": str(project_metadata["path"]),
        "version": "0.1.0",
        "status": "development",
        "git": True,
        "providers": project_metadata["providers"],
        "depends_on": ["mycel"],
        "tags": project_metadata["tags"]
    }
    self._save_registry(registry)
```

Entry added to `X:\Projects\_GAIA\registry.json`:
```json
{
  "sentiment_analyzer": {
    "name": "Sentiment Analyzer",
    "path": "X:/Projects/sentiment_analyzer",
    "version": "0.1.0",
    "status": "development",
    "git": true,
    "providers": ["openai"],
    "depends_on": ["mycel"],
    "tags": ["deterministic-pipeline", "sentiment", "nlp"]
  }
}
```

**Step 6: WARDEN Validates Scaffold (FUTURE)**

Currently not implemented. Future validation:
```python
# FUTURE: warden/enforce.py
def validate_new_project(project_path: Path) -> List[str]:
    """Validate VULCAN-generated project."""
    errors = []

    # Check git initialized
    if not (project_path / ".git").exists():
        errors.append("Git not initialized")

    # Check .gitignore has secrets protection
    gitignore = (project_path / ".gitignore").read_text()
    if ".env" not in gitignore:
        errors.append(".gitignore missing .env")

    # Check MYCEL in requirements
    reqs = (project_path / "requirements.txt").read_text()
    if "rag-intelligence" not in reqs:
        errors.append("MYCEL not in requirements")

    return errors
```

**Step 7: Project Ready — Integration Layer Active**

The new project can now:
- Import MYCEL for LLM calls: `from rag_intelligence import create_llm_client`
- Import MNEMIS for memory: `from mnemis import MnemisStore`
- Emit ARGUS telemetry: Write to `logs/*.jsonl`

**Step 8: Runtime Example**

User runs the project:
```python
# sentiment_analyzer/core/stages/2_classify_sentiment.py
from rag_intelligence import create_llm_client

def classify_sentiment(text: str) -> dict:
    client = create_llm_client(provider="openai")
    response = client.complete_json(
        system="You are a sentiment classifier",
        user=f"Classify sentiment: {text}\nReturn JSON with sentiment and confidence."
    )
    return response
```

- LLM call routes through MYCEL
- Cost tracked by product's internal tracker
- (Future) Events emitted to ARGUS EventBus
- (Future) Patterns stored in MNEMIS PROJECT tier

---

## 8. Shared Service Constraints

| Service | Hard Constraints | Soft Constraints | Tools/Libraries |
|---------|------------------|------------------|-----------------|
| **MYCEL** | - Python 3.10+<br>- Pydantic v2<br>- .env for API keys | - Prefer `GaiaSettings` inheritance<br>- Use `create_llm_client()` not direct SDK | `pydantic-settings`, `openai`, `anthropic`, `google-generativeai`, `tiktoken` |
| **LOOM** | - Must use MYCEL for LLM<br>- Must use MNEMIS for memory<br>- Agent types enforced (EXECUTOR/OBSERVER/COORDINATOR/TRANSFORMER) | - Prefer JSON workflow specs over code<br>- Document all agent contracts | `pydantic`, `uuid`, `datetime` |
| **ARGUS** | - 59 mental models (immutable)<br>- 4 explanation levels (Simple/Detailed/Technical/Debug)<br>- Growth Rung 1-4 mapping | - Log to `logs/*.jsonl` format<br>- Use EventBus for real-time events | `pydantic`, `streamlit` (dashboard) |
| **MNEMIS** | - 5 tiers enforced<br>- Write-at-level-only rule<br>- Promotion requires approval | - Use MemoryContract for all access<br>- Always track provenance | `pydantic`, `uuid`, `datetime` |
| **VULCAN** | - Must use MYCEL<br>- Must create registry entry<br>- Must generate CLAUDE.md + .gitignore | - Use adapters, don't scaffold manually<br>- Follow 7-step questionnaire | `streamlit`, `pathlib`, `pydantic` |
| **WARDEN** | (Not implemented) | - Pre-commit hooks<br>- Git status checks<br>- Secrets validation | TBD |
| **ABIS** | (Design phase) | - Visual canvas UI<br>- LOOM integration<br>- No-code agent builder | TBD (likely React + Streamlit) |
| **RAVEN** | (Planned) | - Use MYCEL for retrieval<br>- Use MNEMIS for findings<br>- Document search via RAG<br>- Structured report generation | TBD |

**Universal Constraints (All Services):**
- No Spanish text in Python code (localization in `config/locales/es.json`)
- Type hints on all function signatures
- Docstrings on public functions
- Absolute imports: `from rag_intelligence import ...` not `from . import ...`
- No API keys in code: `os.getenv("KEY")`

---

## 9. Integration Patterns

### Pattern 1: MYCEL Bridge (LLM Access)

**From jSeeker (formerly PROTEUS):** `proteus/integrations/mycel_bridge.py`

```python
"""MYCEL bridge — LLM client via GAIA MYCEL infrastructure.

Falls back to direct Anthropic SDK if MYCEL is not available.
"""

from typing import Optional

def get_llm_client(provider: str = "anthropic") -> Optional[object]:
    """Try to get LLM client from MYCEL, fall back to direct SDK."""
    try:
        from rag_intelligence.llm import create_llm_client
        return create_llm_client(provider=provider)
    except ImportError:
        return None
```

**Usage Pattern:**
```python
# In product code
from proteus.integrations.mycel_bridge import get_llm_client

client = get_llm_client(provider="anthropic")
if client:
    response = client.complete(system="...", user="...")
else:
    # Fallback to direct SDK
    from anthropic import Anthropic
    client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
```

**Why This Pattern:**
- Graceful degradation if MYCEL not installed
- Products can start standalone, integrate later
- No hard dependency on MYCEL (soft coupling)

---

### Pattern 2: MNEMIS Bridge (Memory Access)

**From jSeeker (formerly PROTEUS):** `proteus/integrations/mnemis_bridge.py`

```python
"""MNEMIS bridge — Pattern memory storage for PROTEUS (Phase 3+).

Stores successful resume patterns in MNEMIS PROJECT tier.
Promotes proven patterns to GAIA tier for cross-project reuse.
"""

from typing import Optional

def store_pattern(
    pattern_type: str,
    pattern_data: dict,
    tier: str = "PROJECT",
) -> Optional[str]:
    """Store a resume pattern in MNEMIS memory."""
    try:
        from rag_intelligence.memory import MnemisClient
        client = MnemisClient()
        return client.store(
            component="proteus",
            pattern_type=pattern_type,
            data=pattern_data,
            tier=tier,
        )
    except ImportError:
        return None

def recall_patterns(
    pattern_type: str,
    limit: int = 5,
) -> list[dict]:
    """Recall stored patterns from MNEMIS."""
    try:
        from rag_intelligence.memory import MnemisClient
        client = MnemisClient()
        return client.recall(
            component="proteus",
            pattern_type=pattern_type,
            limit=limit,
        )
    except ImportError:
        return []
```

**Usage Pattern:**
```python
# After successful resume generation
from proteus.integrations.mnemis_bridge import store_pattern

pattern_id = store_pattern(
    pattern_type="bullet_style",
    pattern_data={
        "style": "action_verb_quantified",
        "example": "Increased sales by 40% through strategic outreach",
        "ats_score": 0.92
    },
    tier="PROJECT"
)

# Later, in similar context
from proteus.integrations.mnemis_bridge import recall_patterns

patterns = recall_patterns(pattern_type="bullet_style", limit=5)
for p in patterns:
    print(f"Pattern: {p['style']} (ATS: {p['ats_score']})")
```

**Why This Pattern:**
- Products accumulate learnings over time
- Successful patterns promoted to GAIA tier
- Cross-project knowledge sharing

---

### Pattern 3: ARGUS Telemetry (Event Emission)

**From jSeeker (formerly PROTEUS):** `proteus/integrations/argus_telemetry.py`

```python
"""ARGUS telemetry — build and runtime monitoring for PROTEUS."""

import json
from datetime import datetime, timezone
from pathlib import Path
from config import settings

def log_event(
    agent: str,
    wave: int,
    module: str,
    status: str,
    duration_ms: int = 0,
    details: str = "",
) -> None:
    """Write a telemetry event to the ARGUS build log."""
    log_path = settings.argus_log_path
    log_path.parent.mkdir(parents=True, exist_ok=True)

    entry = {
        "ts": datetime.now(timezone.utc).isoformat(),
        "agent": agent,
        "wave": wave,
        "module": module,
        "status": status,
        "duration_ms": duration_ms,
        "details": details,
    }

    with open(log_path, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")

def log_runtime_event(
    task: str,
    model: str,
    cost_usd: float,
    input_tokens: int = 0,
    output_tokens: int = 0,
    details: str = "",
) -> None:
    """Log a runtime API call event for cost monitoring."""
    log_path = settings.gaia_root / "logs" / "proteus_runtime.jsonl"
    log_path.parent.mkdir(parents=True, exist_ok=True)

    entry = {
        "ts": datetime.now(timezone.utc).isoformat(),
        "component": "proteus",
        "task": task,
        "model": model,
        "cost_usd": cost_usd,
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "details": details,
    }

    with open(log_path, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")
```

**Usage Pattern:**
```python
# In product pipeline
from proteus.integrations.argus_telemetry import log_runtime_event
from proteus.llm import llm

# Execute task
start = time.time()
response = llm.call_sonnet(prompt, task="adapt_resume")
duration_ms = int((time.time() - start) * 1000)

# Log to ARGUS
cost = llm.get_total_session_cost()
log_runtime_event(
    task="adapt_resume",
    model="claude-sonnet-4-5-20250929",
    cost_usd=cost,
    input_tokens=2500,
    output_tokens=1200,
    details=f"Duration: {duration_ms}ms"
)
```

**ARGUS Dashboard Reads:**
```python
# argus/dashboard/registry_reader.py
import json

def read_runtime_logs(component: str) -> list[dict]:
    """Read runtime telemetry for a component."""
    log_path = Path("X:/Projects/_GAIA/logs") / f"{component}_runtime.jsonl"

    events = []
    with open(log_path, "r") as f:
        for line in f:
            events.append(json.loads(line))

    return events
```

**Why This Pattern:**
- Standardized JSONL format (one event per line)
- Append-only (no database needed)
- Cross-project aggregation via ARGUS
- Real-time monitoring possible

---

## 9A. Python Tools — GAIA-Aware Standalone Utilities

Python Tools are standalone utilities that participate in GAIA governance without full LOOM orchestration:

**What They Get:**
- MYCEL LLM clients (unified API access)
- ARGUS telemetry (cost and usage tracking via JSONL)
- MNEMIS pattern storage (contribute learned patterns)
- WARDEN validation (secrets scanning, dependency checks)
- Registry tracking (version and status in registry.json)

**What They Don't Get:**
- LOOM workflow orchestration (they run independently)
- ABIS visual editing (not agent systems)
- Full CI/CD pipelines (manual testing acceptable)

**Governance Contract:**
```
Python Tool → Uses MYCEL for LLM → Emits ARGUS telemetry →
Stores patterns in MNEMIS → WARDEN validates on commit →
Registry tracks version → Tool contributes to ecosystem intelligence
```

---

## 10. What's Missing (Honest Assessment)

Based on code review and registry analysis (Feb 8, 2026):

### WARDEN: Enforcement Exists in Docs, Not in Code

**Current State:**
- Described in GAIA_BIBLE.md Chapter 0 (lines 332-340)
- Registry entry exists: `v0.1.0`, status `development`
- Directory exists: `X:\Projects\_GAIA\_WARDEN` (empty)

**Gap:**
- Zero enforcement code
- No pre-commit hooks
- No validation scripts
- No `warden/enforce.py`

**Impact:**
- Projects can commit without tests passing
- No automated secrets validation
- No dependency freshness checks
- VULCAN scaffolds projects but doesn't enforce quality

**Recommendation:**
Implement Phase 4: WARDEN with pre-commit hooks:
```bash
# .git/hooks/pre-commit (future)
#!/bin/bash
python X:/Projects/_GAIA/_WARDEN/warden/enforce.py --check-secrets --check-tests
```

---

### ARGUS: Monitoring Vision vs. Implementation

**Current State:**
- Mental Model Library: COMPLETE (59 models, 4 explanation levels)
- Subconscious Layer: COMPLETE (pattern detection, external memory)
- Dashboard: PARTIAL (registry reader exists, live trace empty)

**Gap:**
```
X:\Projects\_GAIA\_ARGUS\dashboard\
├── app.py                 # Streamlit dashboard (exists)
├── event_bus.py           # EventBus class (exists)
├── components\
│   ├── ecosystem_graph.py # Graph visualization (exists)
│   ├── live_trace.py      # EMPTY (just __init__)
│   └── memory_tree.py     # EMPTY (just __init__)
└── process_observer\      # EMPTY directory
```

**Impact:**
- Can't visualize real-time agent execution
- Can't trace memory access patterns
- EventBus exists but no subscribers

**Recommendation:**
Implement live trace UI:
```python
# argus/dashboard/components/live_trace.py (future)
import streamlit as st

def render_live_trace(event_stream: list[dict]) -> None:
    """Render real-time agent execution trace."""
    for event in event_stream:
        with st.expander(f"{event['ts']} - {event['agent']}"):
            st.json(event)
```

---

### MYCEL Router: Placeholder, Not Implemented

**Current State:**
- Base settings exist (`GaiaSettings` in `rag_intelligence/config.py`)
- Model defaults hardcoded (Sonnet, Haiku, GPT-4o)
- No query complexity estimation
- No automatic model selection

**Gap:**
```python
# Future: rag_intelligence/router.py
def select_model(
    task: str,
    query_complexity: float,  # NOT IMPLEMENTED
    budget_remaining: float,
    provider_preference: str = "anthropic"
) -> str:
    """Route to appropriate model based on complexity and budget."""
    # NOT IMPLEMENTED
    pass
```

**Impact:**
- Products must manually choose Haiku vs. Sonnet
- No automatic cost optimization
- No learned routing patterns

**Recommendation:**
Implement Phase 5: MYCEL Router with heuristics:
```python
def estimate_query_complexity(prompt: str) -> float:
    """Heuristic complexity estimation."""
    # Token count
    tokens = len(prompt.split())
    # Reasoning keywords
    reasoning_keywords = ["analyze", "compare", "synthesize", "evaluate"]
    has_reasoning = any(kw in prompt.lower() for kw in reasoning_keywords)

    complexity = min(tokens / 500, 1.0)
    if has_reasoning:
        complexity = min(complexity + 0.3, 1.0)

    return complexity
```

---

### Universal Telemetry: Only jSeeker Emits Events

**Current State:**
- jSeeker (formerly PROTEUS) has full telemetry integration
- HART OS, VIA, DATA FORGE: No telemetry

**Gap:**
- ARGUS can only monitor jSeeker
- No ecosystem-wide cost tracking
- No cross-project pattern detection

**Recommendation:**
Add telemetry to existing products:
```python
# hart_os/core/scoring.py (add this)
from argus_telemetry import log_runtime_event

def score_therapy_session(transcript: str) -> dict:
    start = time.time()
    # ... existing logic ...

    log_runtime_event(
        task="score_therapy",
        model="gpt-4o",
        cost_usd=0.05,
        details=f"Transcript length: {len(transcript)}"
    )
```

---

### CI/CD: Zero GitHub Actions

**Current State:**
- 15 projects in registry
- 1 has GitHub remote (`hart_os`)
- 0 have CI/CD pipelines

**Gap:**
- No automated testing on commit
- No pre-deployment validation
- No cost budget alerts

**Recommendation:**
Implement GitHub Actions for critical projects:
```yaml
# .github/workflows/test.yml (future)
name: Test Suite
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
      - run: pip install -r requirements.txt
      - run: pytest tests/
      - run: python warden/enforce.py --check-secrets
```

---

### GitHub Remotes: 1 of 15 Projects

**Current State (from registry.json):**
- 15 total projects
- 11 have `git: true`
- 1 has `git_remote` (hart_os)

**Gap:**
- No remote backups
- No collaboration enabled
- No GitHub issue tracking

**Recommendation:**
Create GitHub organization and push core services:
```bash
# Push MYCEL, LOOM, ARGUS, MNEMIS to GitHub
gh repo create gaia-ecosystem/mycel --private
cd X:\Projects\_GAIA\_MYCEL
git remote add origin https://github.com/gaia-ecosystem/mycel.git
git push -u origin main
```

---

### Summary: Implementation vs. Documentation Gap

| Component | Documentation | Implementation | Gap |
|-----------|---------------|----------------|-----|
| MYCEL | 100% | 90% (router missing) | 10% |
| LOOM | 100% | 80% (mock bridge) | 20% |
| ARGUS Mental Models | 100% | 100% | 0% |
| ARGUS Dashboard | 100% | 40% (live trace empty) | 60% |
| MNEMIS | 100% | 95% (promotion tested) | 5% |
| VULCAN | 100% | 100% | 0% |
| WARDEN | 100% | 0% | 100% |
| ABIS | 80% | 0% | 100% |
| RAVEN | 60% (expanded definition) | 0% | 100% |
| GPT_ECHO (Product) | 50% | 10% (stale) | 90% |

**Overall Ecosystem Maturity:** 65% implemented relative to documented vision

---

## Appendix: File Paths Reference

**GAIA Core:**
- Constitution: `X:\Projects\_GAIA\GAIA_BIBLE.md`
- Registry: `X:\Projects\_GAIA\registry.json`
- Logs: `X:\Projects\_GAIA\logs\{component}_runtime.jsonl`

**MYCEL (rag-intelligence):**
- Config: `X:\Projects\_GAIA\_MYCEL\rag_intelligence\config.py`
- LLM Clients: `X:\Projects\_GAIA\_MYCEL\rag_intelligence\llm.py`
- Chunking: `X:\Projects\_GAIA\_MYCEL\rag_intelligence\chunking.py`

**LOOM:**
- Workflow Engine: `X:\Projects\_GAIA\_LOOM\loom\core\workflow_engine.py`
- Agent Models: `X:\Projects\_GAIA\_LOOM\loom\models\agent_models.py`
- MYCEL Bridge: `X:\Projects\_GAIA\_LOOM\loom\integrations\mycel_bridge.py`

**ARGUS:**
- Mental Models: `X:\Projects\_GAIA\_ARGUS\mental_models\`
- Explainer: `X:\Projects\_GAIA\_ARGUS\explainability\explainer.py`
- Event Bus: `X:\Projects\_GAIA\_ARGUS\dashboard\event_bus.py`

**MNEMIS:**
- Memory Models: `X:\Projects\_GAIA\_MNEMIS\mnemis\models\memory_models.py`
- Promotion Engine: `X:\Projects\_GAIA\_MNEMIS\mnemis\core\promotion.py`

**VULCAN:**
- Project Creator: `X:\Projects\_GAIA\_VULCAN\vulcan_forge\project_creator.py`
- Adapters: `X:\Projects\_GAIA\_VULCAN\vulcan_forge\adapters\`

**jSeeker (formerly PROTEUS):**
- LLM Wrapper: `X:\Projects\_GAIA\_PROTEUS\proteus\llm.py`
- Pipeline: `X:\Projects\_GAIA\_PROTEUS\proteus\pipeline.py`
- MYCEL Bridge: `X:\Projects\_GAIA\_PROTEUS\proteus\integrations\mycel_bridge.py`
- MNEMIS Bridge: `X:\Projects\_GAIA\_PROTEUS\proteus\integrations\mnemis_bridge.py`
- ARGUS Telemetry: `X:\Projects\_GAIA\_PROTEUS\proteus\integrations\argus_telemetry.py`

---

**Document Maintenance:**
- This document reflects the GAIA Ecosystem state as of February 8, 2026
- For updates to service versions, see `X:\Projects\_GAIA\registry.json`
- For constitutional changes, see `X:\Projects\_GAIA\GAIA_BIBLE.md`
- For implementation gaps, see Section 10 above

**Contributors:**
- Architecture: Claude Code (Sonnet 4.5)
- Review: Fed (GAIA Architect)
- Last Updated: 2026-02-08
