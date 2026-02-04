# PHASE 3 Implementation Status - LOOM + MNEMIS (Visual Editor & Memory)

**Status:** In Design & Planning
**Last Updated:** Feb 4, 2026 23:45 UTC
**Version:** v1.0.0 (Planned)

---

## Executive Summary

Phase 3 (LOOM + MNEMIS) completes the GAIA ecosystem by adding visual workflow editing and cross-project memory. LOOM enables users to visually design and modify agent workflows. MNEMIS enables persistent, hierarchical memory that connects decisions across projects and supports learning propagation.

**Core Mission:** Enable visual orchestration (LOOM) and explicit cross-project learning (MNEMIS) while maintaining governance and transparency.

---

## Component 1: MNEMIS (The Memory System)

### Status: DESIGNED (v0.4.2), IMPLEMENTATION PENDING

**Cross-Project Knowledge Base with Authority Hierarchy**

### 1.1 Memory Architecture

#### Three-Tier Memory Hierarchy

```
┌──────────────────────────────────────────────────────────┐
│ GAIA Tier (Ecosystem)                                    │
├──────────────────────────────────────────────────────────┤
│ Ownership: GAIA Constitution                             │
│ Write Access: GAIA governance decisions (proposal-based) │
│ Read Access: ALL projects (inheritance)                  │
│ Persistence: Permanent (not deletable)                   │
│ Examples:                                                │
│  • Ecosystem decisions (GAIA governance changes)        │
│  • Constitutional amendments                            │
│  • Global pattern library (Mental Models, anti-patterns) │
│  • Cross-project standards                              │
│                                                          │
├──────────────────────────────────────────────────────────┤
│ PROJECT Tier (Persistent)                                │
├──────────────────────────────────────────────────────────┤
│ Ownership: Project Agent                                 │
│ Write Access: Project Agent only (with approval)         │
│ Read Access: Project agents, promoted learnings (GAIA)  │
│ Persistence: Until project archived (can export)         │
│ Examples:                                                │
│  • Project decisions (adapter choice, config, strategy)  │
│  • Project learnings (what worked, what didn't)         │
│  • Project history (evolution, major milestones)         │
│  • Project-specific patterns (learned patterns)          │
│                                                          │
├──────────────────────────────────────────────────────────┤
│ AGENT Tier (Ephemeral)                                   │
├──────────────────────────────────────────────────────────┤
│ Ownership: Execution agents                              │
│ Write Access: Own memory only (proposals to project)     │
│ Read Access: Own memory during execution                 │
│ Persistence: For one execution cycle only                │
│ Examples:                                                │
│  • Execution context (current run state)                 │
│  • Intermediate results (not final)                      │
│  • Hypotheses in formation (not yet confirmed)          │
│  • Agent reasoning (reasoning trail)                     │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

### 1.2 Memory Access Contracts

#### Write Authorization Rules

```python
class MemoryWriteAuth:
    """
    Defines who can write to each memory tier.
    Enforced mechanically (not suggested - required).
    """

    # AGENT tier: Only ephemeral, proposes to project
    def can_agent_write(agent_id, memory_tier):
        return memory_tier == MemoryTier.AGENT  # Never PROJECT or GAIA

    # PROJECT tier: Project Agent approves writes
    def can_project_write(agent_id, memory_tier):
        return (agent_id == current_project.agent_id and
                memory_tier == MemoryTier.PROJECT)

    # GAIA tier: Only through constitutional approval
    def can_gaia_write(agent_id, memory_tier):
        return (agent_id == GAIA_GOVERNOR and
                memory_tier == MemoryTier.GAIA and
                has_constitutional_approval(write_request))

    # Promotion: Agent → Project → GAIA (explicit proposal)
    def propose_promotion(source_tier, target_tier, content):
        """
        Agents can propose to promote learning up tiers.
        Higher tier decides to accept or reject.
        """
        if source_tier == MemoryTier.AGENT:
            project_reviews(content)  # Project agent approves
        elif source_tier == MemoryTier.PROJECT:
            gaia_reviews(content)     # GAIA governance approves
```

#### Read Authorization Rules

```python
class MemoryReadAuth:
    """
    Defines who can read from each memory tier.
    Read is permissive; write is restrictive.
    """

    # GAIA tier: Readable by all (ecosystem standards)
    def can_read_gaia(agent_id):
        return True  # Everyone reads ecosystem standards

    # PROJECT tier: Readable by own project, not others
    def can_read_project(agent_id, project_id):
        return get_agent_project(agent_id) == project_id

    # AGENT tier: Readable only by own execution
    def can_read_agent(agent_id, agent_memory_id):
        return agent_id == agent_memory_id
```

#### Promotion Protocol (Agent → Project → GAIA)

```
Step 1: Agent Learns Something
  Agent (Stage 3): "I learned that confidence >0.85 means high confidence"
  Action: Stores in AGENT memory (ephemeral)

Step 2: Agent Proposes Promotion to PROJECT
  Agent: "Should this learning move to project memory?"
  Proposal: Clear rationale, evidence, expected impact

Step 3: Project Agent Reviews
  Project Agent: "Yes, this applies to all HART OS projects"
  Action: Moves to PROJECT memory, stamped with approval date/rationale

Step 4: Project Proposes Promotion to GAIA
  Project Agent: "This threshold (0.85) works across all therapy projects"
  Proposal: Evidence from 12 projects, consistent results

Step 5: GAIA Reviews
  GAIA: "Confirms pattern, approves to GAIA tier"
  Action: Stores in GAIA tier as ecosystem standard
  Impact: All future therapy projects inherit this knowledge

Step 6: Result
  New therapy projects get knowledge WITHOUT re-learning.
  Accelerates onboarding (Day 1 intelligence > Day 0 baseline).
```

### 1.3 Provenance & Audit Trail

#### Every Memory Item Carries Metadata
```json
{
  "id": "memory_87234",
  "content": "Confidence threshold 0.85 optimal for therapy projects",
  "tier": "gaia",
  "created_by": "project_hart_os",
  "created_at": "2026-01-15T14:23:00Z",
  "confidence": 0.92,
  "evidence_count": 12,
  "evidence": [
    {"source": "hart_os", "count": 4, "success_rate": 0.94},
    {"source": "therapy_analyzer", "count": 3, "success_rate": 0.89},
    {"source": "mood_tracker", "count": 5, "success_rate": 0.93}
  ],
  "promotion_path": [
    {
      "tier": "agent",
      "approved_by": "mood_tracker_stage3_agent",
      "reason": "High success rate in local testing",
      "timestamp": "2026-01-14T10:00:00Z"
    },
    {
      "tier": "project",
      "approved_by": "hart_os_project_agent",
      "reason": "Pattern confirmed across 3 projects",
      "timestamp": "2026-01-14T11:00:00Z"
    },
    {
      "tier": "gaia",
      "approved_by": "gaia_governance",
      "reason": "Ecosystem standard, all therapy projects should adopt",
      "timestamp": "2026-01-15T14:23:00Z"
    }
  ],
  "usage_count": 127,
  "feedback": {
    "helpful_count": 124,
    "unhelpful_count": 2,
    "modified_count": 1
  }
}
```

### 1.4 Cross-Project Learning

#### Knowledge Inheritance
```
New Project: "therapy_chatbot"

VULCAN creates project with:
  ✓ Adapter type: Deterministic (from Mental Model Library)
  ✓ LLM: OpenAI gpt-4o (from GAIA tier ecosystem choice)
  ✓ Threshold: 0.85 (from GAIA tier learned from therapy projects)
  ✓ Stages: 5 standard therapy stages (from GAIA tier template)
  ✓ Test framework: 14 tests (ecosystem standard)
  ✓ Failure handling: Graceful degradation (constitutional requirement)

Result: New project starts at "Day 100" intelligence, not "Day 1"
        All previous learning available immediately
```

#### Learning Propagation
```
VIA Project Learns Something:
  "When LLM returns malformed JSON, retry with temperature=0.5"

1. Stored in VIA memory (project tier)
2. VIA proposes to GAIA: "This should be ecosystem standard"
3. GAIA reviews other projects (HART OS, CARE PLANS, DATA FORGE)
4. Pattern confirmed in 3/5 projects
5. GAIA adopts as ecosystem standard
6. All future projects inherit this knowledge

Impact: Cost saving (retries reduce re-runs by 30%)
        Propagates across ecosystem automatically
        Can be overridden per project (user choice)
```

### 1.5 MNEMIS Components

#### Memory Store
- Hierarchical storage (agent → project → gaia)
- Immutable audit trail (append-only log)
- Full-text search (find similar learnings)
- Versioning (history of changes)
- Export capability (users own their memories)

**Implementation:**
- [ ] Database schema (PostgreSQL for production, SQLite for testing)
- [ ] Write authorization layer
- [ ] Read authorization layer
- [ ] Promotion protocol engine
- [ ] Audit trail infrastructure
- [ ] Full-text search indexing

#### Learning Recommendation Engine
- Suggests relevant GAIA tier knowledge to new projects
- Scores relevance (domain, problem type, complexity)
- Shows confidence (learned from how many projects)
- Allows override (user keeps control)

**Implementation:**
- [ ] Relevance scorer (TF-IDF or semantic similarity)
- [ ] Confidence calculator (from evidence count)
- [ ] Recommendation UI (show relevant learnings)
- [ ] Override handler (user can accept/reject/modify)

#### Memory Visualization (LOOM Integration)
- Tree view of GAIA tier learnings
- Project-level memory browser
- Knowledge inheritance tracking
- Usage statistics (which learnings most valuable)

**Implementation:**
- [ ] Tree view component (Streamlit or React)
- [ ] Memory browser UI
- [ ] Inheritance visualization
- [ ] Usage dashboard

### Deliverables

- [ ] Memory hierarchy infrastructure (3-tier system)
- [ ] Authorization layer (write/read contracts enforced)
- [ ] Promotion protocol engine
- [ ] Provenance tracking (full audit trail)
- [ ] Learning recommendation engine
- [ ] Memory visualization (LOOM integration)
- [ ] Search and query interface
- [ ] Export/backup capability
- [ ] Test suite (100+ tests on authorization)

### Metrics

- [ ] Memory query latency (<100ms for common queries)
- [ ] Authorization rule accuracy (100%)
- [ ] Promotion success rate (user accepts recommendations)
- [ ] Learning reuse rate (how often promoted learnings used)
- [ ] Cross-project knowledge propagation time
- [ ] Memory storage efficiency

---

## Component 2: LOOM (The Visual Editor)

### Status: DESIGNED (conceptually), IMPLEMENTATION PENDING

**Visual Workflow Designer for Agent Orchestration**

### 2.1 LOOM Interface Architecture

#### Main View: Workflow Canvas
```
┌─────────────────────────────────────────────────────────┐
│ LOOM - Visual Agent Editor                              │
├─────────────────────────────────────────────────────────┤
│                                                          │
│ Project: HART OS          [Save] [Test] [Deploy]        │
│                                                          │
│ ┌──────────────────────────────────────────────────┐   │
│ │                                                   │   │
│ │  ┌─────────┐       ┌─────────┐       ┌───────┐ │   │
│ │  │  INPUT  │──────→│ STAGE 1 │──────→│ STAGE │ │   │
│ │  │ Extract │       │Classify │      │ 2    │ │   │
│ │  └─────────┘       └─────────┘       └───────┘ │   │
│ │                          ↓                       │   │
│ │  ┌──────────┐      ┌─────────┐      ┌──────┐   │   │
│ │  │ LLM      │←─────┤ Error   │      │Score │   │   │
│ │  │ Client   │      │ Handler │←─────│      │   │   │
│ │  └──────────┘      └─────────┘      └──────┘   │   │
│ │       ↓                                  ↓       │   │
│ │  ┌──────────┐      ┌──────────┐    ┌────────┐  │   │
│ │  │ Cache    │      │ Threshold│    │OUTPUT  │  │   │
│ │  │          │      │          │    │Format  │  │   │
│ │  └──────────┘      └──────────┘    └────────┘  │   │
│ │                                                   │   │
│ └──────────────────────────────────────────────────┘   │
│                                                          │
│ [+Add Stage] [+Add Branch] [+Add Agent] [Delete]      │
│                                                          │
├─────────────────────────────────────────────────────────┤
│ Stage Details                                            │
│ ┌──────────────────────────────────────────────────┐   │
│ │ STAGE 1 - Classify                               │   │
│ │ Input: user_input                                │   │
│ │ LLM: gpt-4o                                      │   │
│ │ Prompt: [Edit]                                   │   │
│ │ Output: classification                           │   │
│ │ Tests: 8/8 passing                               │   │
│ │ [Edit] [Test] [View History]                     │   │
│ └──────────────────────────────────────────────────┘   │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

#### Sidebar: Components Library
```
┌──────────────────┐
│ Components       │
├──────────────────┤
│                  │
│ INPUT TYPES     │
│  • Text          │
│  • JSON          │
│  • File          │
│  • Stream        │
│                  │
│ PROCESSING      │
│  • LLM Call      │
│  • Data Process  │
│  • Validation    │
│  • Branching     │
│                  │
│ ERROR HANDLING  │
│  • Retry         │
│  • Fallback      │
│  • Escalate      │
│                  │
│ OUTPUT TYPES    │
│  • JSON          │
│  • File          │
│  • Cache         │
│  • Memory        │
│                  │
└──────────────────┘
```

### 2.2 Workflow Design Capabilities

#### 1. Node Types

**Input Nodes**
- User input (text, JSON, file)
- Previous stage output
- Memory/context (from MNEMIS)
- External API call

**Processing Nodes**
- LLM call (with configurable provider, model, temperature)
- Data processing (JSON parsing, validation, transformation)
- Conditional branching (if/else logic)
- Parallel processing (fan-out, fan-in)
- Error handling (retry, fallback, escalate)

**Output Nodes**
- Return to user (formatted response)
- Cache (store in MNEMIS project tier)
- File output (save results)
- API callback (call external service)

**Storage Nodes**
- Save to MNEMIS (with promotion option)
- Update project config
- Log decision (audit trail)

#### 2. Connections & Flow Control

**Sequential Flow**
```
Stage 1 → Stage 2 → Stage 3 → Output
```

**Branching**
```
Input → Decision → Branch A → ...
               └─→ Branch B → ...
                   └─→ Fallback → ...
```

**Parallel Processing**
```
Input → [Process A, Process B, Process C] in parallel → Merge → Output
```

**Error Handling**
```
LLM Call → Success? → Format Output
        └─→ Fail → Retry? → Success → Format Output
                      └─→ Fallback → Handle Gracefully
```

#### 3. Visual Properties

**Per-Node Configuration**
- Input/output types
- LLM settings (model, temperature, max tokens)
- Validation rules
- Error handling strategy
- Test expectations
- Documentation

**Workflow Properties**
- Name and description
- Version control (git integration)
- Test coverage (% of paths tested)
- Performance metrics (latency, cost)
- Deployment status

### 2.3 Development Workflow in LOOM

#### 1. Design Phase
- Create nodes visually
- Connect them logically
- Set configuration
- Add tests for each node
- Save as draft

#### 2. Testing Phase
- Run individual nodes (unit test)
- Run paths (integration test)
- Run full workflow (end-to-end test)
- View execution trace (where did it slow down?)
- Debug failures (inspect intermediate results)

#### 3. Optimization Phase
- Identify bottlenecks (which node is slow?)
- Adjust LLM settings (temperature, model)
- Add caching (reduce redundant calls)
- Parallelize where possible
- Save optimized version

#### 4. Deployment Phase
- Create release notes
- Promote to production
- Monitor performance
- Rollback if issues
- Update MNEMIS with learnings

### 2.4 Integration with MNEMIS

#### Knowledge Integration in Workflow Design
```
User designing new workflow in LOOM:

1. LOOM suggests: "You usually use gpt-4o for therapy tasks"
   Source: GAIA tier learning (from MNEMIS)
   Evidence: 8 therapy projects, 0 failures with gpt-4o
   Confidence: 92%
   Action: User can accept or override

2. LOOM suggests: "Stage 3 usually has threshold 0.85"
   Source: Project tier learning (HART OS history)
   Evidence: Last 5 stages in HART OS use 0.85
   Confidence: 80%
   Action: User can accept or modify

3. After testing, user finds: "Retry with temperature=0.5 works best"
   LOOM: "Should I save this learning to project memory?"
   User confirms: Learning saved to PROJECT tier
   LOOM: "Promote to GAIA tier for all therapy projects?"
   User confirms: Learning promoted to GAIA tier
```

#### Visual Memory Browser
```
┌──────────────────────────────────────┐
│ GAIA Learnings (Therapy Domain)      │
├──────────────────────────────────────┤
│                                       │
│ ✓ LLM Model Preference                │
│   └─ gpt-4o for therapy               │
│      Evidence: 8 projects             │
│      Success Rate: 94%                │
│      [Use] [Override] [Remove]        │
│                                       │
│ ✓ Threshold Standard                  │
│   └─ 0.85 for high confidence        │
│      Evidence: 12 projects            │
│      Success Rate: 91%                │
│      [Use] [Override] [Remove]        │
│                                       │
│ ✓ Error Handling Pattern              │
│   └─ Retry with temperature 0.5       │
│      Evidence: 5 projects             │
│      Recovery Rate: 87%               │
│      [Use] [Override] [Remove]        │
│                                       │
└──────────────────────────────────────┘
```

### 2.5 Version Control & Collaboration

#### Git Integration
```
Every LOOM workflow changes:
  1. Auto-commits to git
  2. Creates clear message: "LOOM: Stage 3 temperature changed 0.7→0.5"
  3. Links to test results: "Tests: 8/8 passing"
  4. Creates commit hash: reproducible version
```

#### Collaboration Features
- Multi-user viewing (read-only for others)
- Merge conflicts (if two users modify same workflow)
- History browser (see all changes)
- Rollback capability (revert to previous version)
- Comments and annotations (on specific nodes)

#### Deployment Workflow
```
Development (draft) → Testing (validation) → Staging (pre-prod) → Production

Each stage:
  • Requires passing tests (100%)
  • Can be reviewed by team
  • Creates audit trail
  • Links to MNEMIS learnings
```

### Deliverables

- [ ] LOOM web UI (React or Streamlit-based)
- [ ] Node components library (input, processing, output, storage)
- [ ] Workflow canvas (drag-drop design)
- [ ] Visual debugger (trace execution)
- [ ] Workflow editor (configuration panel)
- [ ] Version control integration (git)
- [ ] Test runner (unit, integration, e2e)
- [ ] Deployment manager
- [ ] MNEMIS integration (suggestions, learnings)
- [ ] Documentation generator (auto-doc from workflow)

### Metrics

- [ ] Workflow creation time (faster than hand-coding)
- [ ] Design accuracy (workflows match intent)
- [ ] Test coverage (% of paths tested before deployment)
- [ ] Deployment success rate (% of deployments without rollback)
- [ ] User satisfaction (survey: easier than text-based design)

---

## Component 3: Integration Architecture

### Status: DESIGNED (conceptually), IMPLEMENTATION PENDING

**How LOOM, MNEMIS, and Phases 1-2 Connect**

### 3.1 Complete Workflow Pipeline

```
┌─────────────────────────────────────────────────────────────┐
│                                                              │
│ 1. VULCAN Creates Project                                   │
│    ├─ Asks 7 questions (HITL questionnaire)                 │
│    ├─ Creates project structure                             │
│    ├─ Inherits MNEMIS learnings (GAIA tier)                │
│    └─ Project ready (Day 1 intelligence from Day 100)       │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│ 2. LOOM Edits Workflow                                      │
│    ├─ Opens generated workflow visually                     │
│    ├─ Modifies stages, connections, config                 │
│    ├─ Tests incrementally (node, path, full)               │
│    ├─ Gets MNEMIS suggestions for each decision             │
│    └─ Saves version, commits to git                         │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│ 3. ARGUS Monitors Execution                                 │
│    ├─ Observes workflow runs                                │
│    ├─ Detects patterns (what's working, what's not)         │
│    ├─ Flags anti-patterns (duplication, regressions)        │
│    ├─ Suggests growth opportunities                         │
│    └─ Updates Trust Dashboard                               │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│ 4. MNEMIS Learns & Shares                                   │
│    ├─ Agent proposes learnings (project tier)               │
│    ├─ Project approves (project tier)                       │
│    ├─ GAIA promotes if ecosystem-wide (GAIA tier)           │
│    ├─ New projects inherit knowledge immediately            │
│    └─ Knowledge accessible in LOOM suggestions              │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│ 5. Back to LOOM                                             │
│    └─ User leverages MNEMIS learnings in next workflow      │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### 3.2 Data Flow

```
VULCAN                    LOOM                  ARGUS
  │                        │                      │
  ├─→ Creates project ────→ Edits workflow ─────→ Monitors
  │                        │                      │
  │   Inherits learnings   │ Suggests learnings   │ Detects patterns
  │   (MNEMIS GAIA tier)   │ (MNEMIS)             │ (Process Observer)
  │                        │                      │
  ↓                        ↓                      ↓
Project created        Workflow optimized    Insights generated
(Day 1 of Day 100)     (tested, refined)     (patterns, suggestions)
                                                  │
                                                  ↓
                                            MNEMIS ←──┐
                                            (learns)  │
                                                  │   │
                                                  └───┘
```

### 3.3 Constitutional Boundaries in Integration

#### User Agency Preserved
- LOOM: User designs workflow (GAIA suggests, doesn't auto-complete)
- ARGUS: GAIA detects patterns (user investigates, user decides)
- MNEMIS: User approves promotions (knowledge doesn't auto-propagate)

#### Transparency Maintained
- LOOM: User sees suggestions and sources (why this suggestion?)
- ARGUS: Dashboard shows all metrics and trends
- MNEMIS: Every learning has provenance trail (who approved, when, why)

#### Graceful Degradation
- LOOM: If MNEMIS unavailable, user designs without suggestions
- ARGUS: If detection fails, fallback to basic metrics
- MNEMIS: If promotion stuck, user can override or escalate

---

## Success Criteria

### Technical
- [ ] LOOM designs are executable (no syntax errors after visual design)
- [ ] LOOM workflows run 20%+ faster than equivalent hand-coded
- [ ] MNEMIS authorization rules 100% accurate (no unauthorized access)
- [ ] Memory promotion latency <2 seconds (users don't wait)
- [ ] Cross-project learning latency <1 second (recommendations instant)
- [ ] LOOM saves/loads <500ms (responsive UX)

### User Experience
- [ ] Workflow design 50% faster in LOOM vs. hand-coding
- [ ] MNEMIS suggestions helpful in >70% of cases
- [ ] Users understand memory hierarchy (survey: >80% comprehension)
- [ ] Users promote learnings (>50% of projects)
- [ ] Workflow reuse increases (>40% of new workflows reuse components)

### Adoption
- [ ] All Phase 1 (VULCAN) workflows editable in LOOM
- [ ] 100% of users have LOOM access
- [ ] 80% of users create/edit at least one workflow in LOOM
- [ ] MNEMIS growing >50 learnings per week
- [ ] 60% of new projects inherit from GAIA tier learnings

---

## Timeline & Milestones

### Phase 2 (Parallel with ARGUS): Foundation
- [ ] MNEMIS infrastructure (storage, authorization, audit trail)
- [ ] Process Observer feeds patterns to MNEMIS
- [ ] Growth Tracker publishes learnings to MNEMIS

### Phase 3 Sprint 1 (Weeks 1-2): MNEMIS Complete
- [ ] Memory hierarchy operational (3-tier system)
- [ ] Promotion protocol tested
- [ ] LOOM prototype starts (UI mockups)

### Phase 3 Sprint 2 (Weeks 3-4): LOOM MVP
- [ ] Basic canvas (add/edit nodes)
- [ ] Node library (essential node types)
- [ ] Save/load (persists designs)
- [ ] Test runner (basic execution)

### Phase 3 Sprint 3 (Weeks 5-6): LOOM Integration
- [ ] MNEMIS suggestions in LOOM
- [ ] Visual debugger
- [ ] Git integration
- [ ] Deployment workflow

### Phase 3 Sprint 4 (Weeks 7-8): Polish & Release
- [ ] Performance optimization
- [ ] UI refinement
- [ ] Documentation
- [ ] v1.0.0 release

---

## Estimated Effort

- **Design:** 60% COMPLETE (MNEMIS architecture solid, LOOM conceptual)
- **Implementation:** 0% (STARTING after Phase 2)
- **Testing:** 0% (PLANNED)
- **Refinement:** 0% (PLANNED)

**Estimated Duration:** 8-12 weeks
**Team Size:** 2-4 developers
**Risk Level:** Medium-High (visual editor is complex, but design is clear)

---

## Known Dependencies

- ✅ MYCEL (Phase 0.5) - COMPLETE
- ✅ VULCAN (Phase 1) - COMPLETE
- ⏳ ARGUS (Phase 2) - Feeds patterns to MNEMIS
- ⏳ Process Observer (Phase 2) - Feeds patterns to MNEMIS
- ⏳ Growth Tracker (Phase 2) - Publishes learnings to MNEMIS

---

## Key Design Decisions

### 1. MNEMIS Tier Hierarchy
**Decision:** 3-tier system (AGENT → PROJECT → GAIA)
**Rationale:**
- Prevents ephemeral agent memory from contaminating project tier
- Ensures explicit promotion (governance point)
- Enables clear promotion criteria (ecosystem-wide benefit)
- Preserves user agency (approvals at each level)

### 2. Read Permissive, Write Restrictive
**Decision:** Reads inherit from higher tiers, writes require authority
**Rationale:**
- GAIA tier standards shared with all (inheritance)
- Project tier private (doesn't leak to other projects)
- Agent tier ephemeral (never persists without approval)
- Authorization simple and enforced mechanically

### 3. LOOM as Workflow, Not Agent Editor
**Decision:** LOOM designs execution flows, not autonomous agents
**Rationale:**
- Matches constitutional requirement (humans in loop)
- Workflow is still governed by Project Agent
- User remains architect (GAIA suggests, doesn't auto-complete)
- Cleaner scope (visual editor for coordination, not autonomy)

### 4. Promotion as Deliberate Act
**Decision:** Learning doesn't auto-propagate (requires approval at each tier)
**Rationale:**
- Prevents false learnings from spreading
- Builds confidence (only proven patterns propagate)
- User maintains control (approves what becomes ecosystem standard)
- Transparency (history shows why pattern was/wasn't promoted)

---

## References

- `X:\Projects\_gaia\VERSION_LOG.md` - v0.4.3 strategic refinements
- `X:\Projects\_gaia\GAIA_BIBLE.md` - Chapter 2: Authority graph, memory contracts
- `X:\Projects\_gaia\SR_COUNCIL_ANALYSIS.md` - Constitutional framework
- `X:\Projects\_gaia\PREDICTIVE_GAIA_SPEC.md` - Safe proactive behavior
- `X:\Projects\_gaia\PHASE_2_IMPLEMENTATION_STATUS.md` - ARGUS planning

---

**Maintained by:** GAIA Phase 3 Team
**Status:** Ready for detailed design review
**Next Review:** After Phase 2 ARGUS mid-point check
