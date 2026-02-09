# Dashboard-First Approach: GAIA Testing Methodology

**v0.5.0 Implementation Guide - ARGUS Dashboard Architecture**

**Date:** Feb 5, 2026

---

## Table of Contents

1. [Executive Summary](#executive-summary)
2. [Why Dashboard Over CLI SIM](#why-dashboard-over-cli-sim)
3. [Component Graph Architecture](#component-graph-architecture)
4. [Event Bus Design](#event-bus-design)
5. [Scenario Framework](#scenario-framework)
6. [Delta Analysis Approach](#delta-analysis-approach)
7. [Constitutional Compliance](#constitutional-compliance)
8. [Implementation Checklist](#implementation-checklist)

---

## Executive Summary

The ARGUS Dashboard represents a paradigm shift in how we test and validate the GAIA ecosystem. Rather than simulating component interactions through a CLI interface, we've adopted a **dashboard-first approach** that provides:

- **Real-time observability** into all component states and interactions
- **Interactive scenario execution** that lets us observe multi-component workflows
- **Centralized event tracing** across all components
- **Constitutional compliance verification** through visual indicators
- **Delta analysis capabilities** to track changes across component states

This approach aligns with GAIA's transparency principles: if we can't observe it visually, we haven't truly validated it.

---

## Why Dashboard Over CLI SIM

### The CLI SIM Problem

In earlier phases, we considered building a CLI-based SIM (simulator) that would:

1. Accept CLI commands to simulate ecosystem events
2. Generate artificial event sequences
3. Output results to the terminal
4. Require manual log inspection to understand what happened

**Limitations:**

- **Cognitive Load**: Humans are poor at reconstructing system behavior from logs
- **Temporal Blindness**: Sequential events are hard to understand when text-scrolls past
- **State Reconstruction**: Understanding component interactions requires manually cross-referencing multiple logs
- **No Feedback Loop**: Can't interactively explore "what if" scenarios
- **Compliance Blind Spots**: Constitutional violations might hide in event ordering

### The Dashboard-First Advantage

By inverting to dashboard-first, we gain:

1. **Visual Composition**: Component states are visible simultaneously
2. **Event Stream Transparency**: Real-time event visualization shows cause→effect chains
3. **Interactive Exploration**: Click to drill down, filter by component, trace lineage
4. **Scenario Templating**: Pre-built scenarios can be executed and observed step-by-step
5. **Compliance Indicators**: Constitutional violations are visually highlighted

**Core Philosophy:**

"If we can't see it happening in real-time, we haven't validated it."

### Strategic Testing Value

The dashboard approach provides:

- **Observability** (transparency principle): All component interactions are visible
- **Auditability** (inspect principle): Event chains can be replayed and verified
- **Learnability** (pedagogical principle): Users understand what's happening through visual feedback
- **Reproducibility** (scientific principle): Scenarios can be re-run to verify consistency

---

## Component Graph Architecture

### Visual Representation

The ARGUS Dashboard displays components as an interactive graph:

```
┌─────────────────────────────────────────────────────────────┐
│  GAIA Ecosystem Status                        [Refresh]      │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│         ┌─────────────┐           ┌─────────────┐            │
│         │  VULCAN ●   │──────────▶│  MYCEL ●    │            │
│         │ (Project    │           │ (LLM        │            │
│         │  Creator)   │           │  Client)    │            │
│         └─────────────┘           └──────┬──────┘            │
│              ▲                            │                  │
│              │                      ┌─────▼──────┐            │
│              │      ┌─────────────┐ │  MNEMIS ●  │            │
│              │      │  ARGUS ●    │ │ (Memory)   │            │
│              │      │ (Dashboard) │ │            │            │
│              │      │             │ └────────────┘            │
│              │      └──────┬──────┘                           │
│              │             │                                  │
│         ┌────┴──────┐  ┌───▼─────────┐   ┌─────────────┐    │
│         │ ECHO ●    │  │ WARDEN ●    │   │  LOOM ●     │    │
│         │(Chat      │  │(Governance) │   │ (Editor)    │    │
│         │ History)  │  │             │   │             │    │
│         └───────────┘  └─────────────┘   └─────────────┘    │
│                            [Placeholder]  [Placeholder]      │
│         ┌──────────────────────────────────────────────┐     │
│         │  RAVEN ●                                      │     │
│         │  (Research) - Placeholder for v0.5           │     │
│         └──────────────────────────────────────────────┘     │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

### Component Status Indicators

Each component displays:

- **Status**: Green (operational), Yellow (warning), Red (error), Gray (idle)
- **Version**: Current running version
- **Event Count**: Total events processed in this session
- **Last Activity**: Timestamp of last event from this component

### Connection Types

Arrows in the graph represent different types of interactions:

- **→**: Direct API call or method invocation
- **⇄**: Bidirectional communication (request/response)
- **↱**: Async event propagation
- **·····**: Data dependency (without direct call)

### Drill-Down Capability

Clicking a component shows:

- **Properties Panel**: Current state and configuration
- **Event History**: Recent events from this component (last 100)
- **Dependencies**: Components this one depends on
- **Consumers**: Components that depend on this one

---

## Event Bus Design

### Central Architecture

The EventBus is the spine of dashboard-first validation:

```
┌────────────────────────────────────────────────────┐
│              GAIA EventBus                          │
│         (SQLite-backed Event Store)                │
├────────────────────────────────────────────────────┤
│                                                    │
│  Event Table:                                     │
│  ┌─────────────────────────────────────────────┐  │
│  │ id │ timestamp │ source │ type │ payload    │  │
│  │  1 │ 10:00:01  │ VULCAN │CREATE_PROJECT  │  │
│  │  2 │ 10:00:02  │ MYCEL  │LLM_REQUEST     │  │
│  │  3 │ 10:00:03  │ MYCEL  │LLM_RESPONSE    │  │
│  │  4 │ 10:00:04  │ MNEMIS │STORE_CHUNK     │  │
│  │  ... │ ...      │ ...    │ ...             │  │
│  └─────────────────────────────────────────────┘  │
│                                                    │
└────────────────────────────────────────────────────┘
```

### Event Schema

Every event has a standardized structure:

```python
class Event:
    id: str                          # UUID
    timestamp: datetime              # When it occurred
    source: str                      # Component name (VULCAN, MYCEL, etc.)
    event_type: str                  # Type of event (CREATE_PROJECT, LLM_REQUEST)
    payload: dict                    # Event-specific data
    parent_event_id: Optional[str]   # Causality chain
    constitutional_check: str        # PASS, WARN, FAIL (compliance indicator)
    metadata: dict                   # Additional context
```

### Event Types

**VULCAN Events:**
- `PROJECT_CREATION_STARTED` - New project creation initiated
- `QUESTIONNAIRE_STEP` - User completed a step in the 7-step questionnaire
- `PROJECT_VALIDATION` - Project configuration validated
- `PROJECT_REGISTRATION` - Project registered in ecosystem

**MYCEL Events:**
- `LLM_REQUEST` - LLM client makes a call
- `LLM_RESPONSE` - Response received
- `CONFIG_LOADED` - Configuration initialized
- `FALLBACK_TRIGGERED` - Fallover to alternate LLM provider

**MNEMIS Events:**
- `CHUNK_STORED` - Memory chunk saved
- `CHUNK_RETRIEVED` - Memory chunk accessed
- `PROMOTION_PROPOSED` - Chunk promotion request
- `PROMOTION_APPROVED` - Promotion completed

**ARGUS Events:**
- `SCAN_STARTED` - Compliance scan initiated
- `SCAN_COMPLETE` - Scan finished
- `ALERT_TRIGGERED` - Constitutional violation detected
- `PATTERN_DETECTED` - Subconscious pattern recognition

**WARDEN Events:**
- `SECRET_CHECK` - Secret scanning completed
- `DEPENDENCY_AUDIT` - Dependency audit run
- `COMPLIANCE_REPORT` - Report generated

**ECHO Events:**
- `CHAT_INDEXED` - Chat history indexed
- `CONTEXT_EXTRACTED` - Context extracted from history

### Event Bus API

```python
class EventBus:
    def emit(self, event: Event) -> str:
        """Record an event in the store"""

    def get_events(self, filters: EventFilter) -> List[Event]:
        """Query events by source, type, time range, etc."""

    def get_event_chain(self, event_id: str) -> List[Event]:
        """Get causality chain: parent → this → children"""

    def subscribe(self, event_type: str, callback: Callable):
        """Subscribe to real-time event stream"""

    def export_events(self, format: str = 'json') -> bytes:
        """Export all events for delta analysis"""
```

### Real-Time Streaming

The dashboard subscribes to events in real-time:

```javascript
// Browser-side WebSocket subscription
ws = new WebSocket('ws://localhost:8501/events');
ws.onmessage = (event) => {
  const data = JSON.parse(event.data);
  updateComponentGraph(data);
  updateEventTimeline(data);
  checkConstitutionalCompliance(data);
};
```

---

## Scenario Framework

### Two Core Scenarios

GAIA v0.5.0 includes two interactive scenarios that users run through the dashboard:

#### Scenario 1: New Project Creation Wizard

**User Journey:**

1. **Start Screen**: Click "Create New Project"
2. **VULCAN Integration**: Dashboard triggers Scenario Wizard
3. **7-Step Questionnaire**:
   - Step 1: Project name and description
   - Step 2: Project type (Deterministic, Creative, Processor)
   - Step 3: Primary agent (Claude, GPT-4, Gemini)
   - Step 4: Integration points (existing projects, external APIs)
   - Step 5: Template selection (Claude Code, Generic, Domain-specific)
   - Step 6: Validation settings (semantic checks, output constraints)
   - Step 7: Confirmation and registration

4. **Real-Time Event Display**:
   - Each step appears as an event in the timeline
   - Component statuses update (VULCAN: active, MYCEL: waiting, etc.)
   - Event bus records all questionnaire responses

5. **Result**: Project created and registered in registry

**Dashboard Observables:**

```
Timeline View:
├─ VULCAN: PROJECT_CREATION_STARTED (10:00:01)
├─ VULCAN: QUESTIONNAIRE_STEP_1 (10:00:05) - "MyAgent v1"
├─ VULCAN: QUESTIONNAIRE_STEP_2 (10:00:08) - "Creative"
├─ VULCAN: QUESTIONNAIRE_STEP_3 (10:00:12) - "Claude"
├─ VULCAN: QUESTIONNAIRE_STEP_4 (10:00:18) - "2 integrations"
├─ VULCAN: QUESTIONNAIRE_STEP_5 (10:00:22) - "Claude Code template"
├─ VULCAN: QUESTIONNAIRE_STEP_6 (10:00:26) - "Validation enabled"
├─ VULCAN: QUESTIONNAIRE_STEP_7 (10:00:30) - "Confirmation"
├─ VULCAN: PROJECT_VALIDATION (10:00:32) - "PASS"
├─ VULCAN: PROJECT_REGISTRATION (10:00:33) - "Registry updated"
└─ WARDEN: COMPLIANCE_REPORT (10:00:34) - "All checks passed"

Component Graph Updates:
VULCAN: Green ● (4 events)
MYCEL: Gray ○ (waiting)
WARDEN: Green ● (1 event)
Registry: Updated
```

#### Scenario 2: Existing Project Integration Wizard

**User Journey:**

1. **Scan Screen**: Click "Integrate Existing Project"
2. **WARDEN Pre-scan**: Scanner detects project characteristics
3. **Integration Wizard**:
   - Step 1: Project path and discovery
   - Step 2: Dependency analysis
   - Step 3: Secret scanning (WARDEN)
   - Step 4: Configuration extraction
   - Step 5: MYCEL compatibility check
   - Step 6: Registry registration

4. **Real-Time Event Display**:
   - WARDEN events show scanning progress
   - Component compatibility checks
   - Registration confirmation

5. **Result**: Existing project integrated into ecosystem

**Dashboard Observables:**

```
Timeline View:
├─ WARDEN: SECRET_CHECK (10:05:01) - "No secrets detected"
├─ WARDEN: DEPENDENCY_AUDIT (10:05:03) - "23 dependencies"
├─ VULCAN: PROJECT_VALIDATION (10:05:05) - "Deterministic type"
├─ MYCEL: CONFIG_LOADED (10:05:07) - "Config validated"
├─ MNEMIS: STORE_CHUNK (10:05:08) - "Project metadata"
├─ WARDEN: COMPLIANCE_REPORT (10:05:10) - "All checks passed"
└─ VULCAN: PROJECT_REGISTRATION (10:05:11) - "Registry updated"

Component Graph Updates:
WARDEN: Green ● (3 events)
VULCAN: Green ● (2 events)
MYCEL: Green ● (1 event)
MNEMIS: Green ● (1 event)
```

### Scenario Execution Control

The dashboard provides playback controls:

```
Scenario Runner:
┌────────────────────────────────────────┐
│  Scenario: New Project Creation        │
├────────────────────────────────────────┤
│  [▶ Start]  [⏸ Pause]  [⏹ Reset]      │
│  Speed: [○─●───────] (1x)              │
│  Current Step: 4 / 7                   │
│  ▓▓▓▓░░░░░░░░░░░░ (57% complete)     │
└────────────────────────────────────────┘
```

Users can:
- Start/pause/reset scenarios
- Adjust execution speed (0.5x, 1x, 2x, etc.)
- Step through individual events
- Observe all component interactions
- Export event log for analysis

---

## Delta Analysis Approach

### What is Delta Analysis?

Delta analysis examines the **difference in system state** before and after a scenario execution:

```
State Before Scenario:
├─ Projects in registry: 0
├─ MYCEL configurations: 0
├─ Events in store: 0
└─ Constitutional violations: 0

↓ [Execute Scenario 1: New Project Creation]

State After Scenario:
├─ Projects in registry: 1
├─ MYCEL configurations: 1
├─ Events in store: 8
└─ Constitutional violations: 0

Delta (Changes):
├─ +1 project registered
├─ +1 MYCEL config loaded
├─ +8 events recorded
└─ Constitutional compliance: MAINTAINED
```

### Why Delta Analysis Matters

1. **Validation**: We verify that the scenario had the intended effect
2. **Safety**: We check that no unexpected changes occurred
3. **Compliance**: We ensure constitutional principles were maintained
4. **Reproducibility**: We can compare deltas across multiple runs

### Implementation: Delta Capture

The EventBus captures state before and after each scenario:

```python
class DeltaAnalyzer:
    def capture_before(self) -> SystemState:
        """Snapshot system state before scenario"""
        return SystemState(
            project_count=len(registry.projects),
            event_count=eventbus.count(),
            component_status={comp: status for comp, status in components.items()},
            memory_chunks=mnemis.chunk_count(),
            violations=compliance.violation_count()
        )

    def capture_after(self) -> SystemState:
        """Snapshot system state after scenario"""
        return SystemState(...)

    def compute_delta(self, before: SystemState, after: SystemState) -> Delta:
        """Calculate differences"""
        return Delta(
            projects_created=after.project_count - before.project_count,
            events_recorded=after.event_count - before.event_count,
            component_changes=self.diff_components(before, after),
            new_violations=self.find_new_violations(before, after)
        )
```

### Dashboard Delta Visualization

After a scenario completes, the dashboard shows:

```
Delta Analysis Report
═══════════════════════════════════════════════════════

Scenario: New Project Creation
Status: ✓ PASSED
Duration: 33 seconds
Events Recorded: 8

State Changes:
├─ Projects:          0 → 1 (+1)  ✓
├─ Registrations:     0 → 1 (+1)  ✓
├─ Memory Chunks:     0 → 1 (+1)  ✓
├─ Configuration:     0 → 1 (+1)  ✓
└─ Events:            0 → 8 (+8)  ✓

Compliance Changes:
├─ Violations:        0 → 0       ✓
├─ Warnings:          0 → 0       ✓
└─ Trust Score:       100% → 100% ✓

Event Timeline Validation:
├─ All events recorded:          ✓
├─ Causal chains intact:         ✓
├─ No out-of-order events:       ✓
└─ All timestamps sequential:    ✓

Conclusion: Scenario VALIDATED
═══════════════════════════════════════════════════════
```

### Export for Comparison

Users can export deltas in JSON:

```json
{
  "scenario": "New Project Creation",
  "timestamp": "2026-02-05T10:00:00Z",
  "duration_seconds": 33,
  "before_state": {
    "projects": 0,
    "events": 0,
    "violations": 0
  },
  "after_state": {
    "projects": 1,
    "events": 8,
    "violations": 0
  },
  "delta": {
    "projects_created": 1,
    "events_recorded": 8,
    "compliance_maintained": true
  },
  "events": [
    {
      "id": "evt-001",
      "timestamp": "2026-02-05T10:00:01Z",
      "source": "VULCAN",
      "type": "PROJECT_CREATION_STARTED"
    },
    ...
  ]
}
```

---

## Constitutional Compliance

### Compliance Verification

The dashboard continuously monitors the five constitutional principles:

#### 1. GAIA Never Lies

**Check**: All component outputs include explicit uncertainty when present

```python
def check_never_lies(event: Event) -> bool:
    """Verify event includes confidence/uncertainty"""
    payload = event.payload

    # LLM responses must include confidence
    if event.type == 'LLM_RESPONSE':
        return 'confidence' in payload and 'reasoning' in payload

    # Memory retrievals must indicate certainty
    if event.type == 'CHUNK_RETRIEVED':
        return 'relevance_score' in payload

    # Decisions must show alternatives considered
    if event.type == 'DECISION':
        return 'alternatives' in payload and 'reasoning' in payload

    return True
```

**Dashboard Indicator**: Green check if all recent events are transparent

#### 2. GAIA Admits Limits

**Check**: Only authorized components take actions; observers stay read-only

```python
def check_admits_limits(event: Event) -> bool:
    """Verify authority boundaries are respected"""

    # ARGUS (observer) cannot modify state
    if event.source == 'ARGUS':
        return event.event_type in ['SCAN_STARTED', 'PATTERN_DETECTED']

    # WARDEN (governance) can only report, not auto-fix
    if event.source == 'WARDEN':
        return 'ALERT' in event.event_type or 'REPORT' in event.event_type

    # MYCEL cannot persist memory (that's MNEMIS)
    if event.source == 'MYCEL':
        return 'STORE' not in event.event_type

    return True
```

**Dashboard Indicator**: Yellow warning if authority boundary crossed

#### 3. GAIA Degrades Gracefully

**Check**: No silent failures; all errors are logged and observable

```python
def check_degrades_gracefully(event: Event) -> bool:
    """Verify no silent failures"""

    # If an operation failed, must have explicit error event
    if 'FAIL' in event.event_type:
        fallback = event.payload.get('fallback_activated')
        if fallback is None:
            return False  # Silent failure

    # If timeout occurred, must be logged
    if 'TIMEOUT' in event.event_type:
        recovery = event.payload.get('recovery_action')
        if recovery is None:
            return False

    return True
```

**Dashboard Indicator**: Red alert if failure without recovery

#### 4. GAIA Learns Explicitly

**Check**: Learning only happens through proposal mechanism, not auto-updates

```python
def check_learns_explicitly(event: Event) -> bool:
    """Verify learning is proposal-based"""

    if event.event_type == 'PROMOTION_APPROVED':
        # Must have preceding PROMOTION_PROPOSED event
        proposed = event_bus.get_event(event.parent_event_id)
        if proposed is None:
            return False

        # Must have approval trace
        if 'approval_metadata' not in event.payload:
            return False

    if event.event_type == 'PATTERN_DETECTED':
        # Pattern detection is observation only, not action
        if 'recommended_action' in event.payload:
            # Action must be proposal, not execution
            return event.payload.get('action_executed') is False

    return True
```

**Dashboard Indicator**: Green if all learning is proposal-based

#### 5. GAIA Remains Inspectable

**Check**: All decisions have traceable reasoning and provenance

```python
def check_remains_inspectable(event: Event) -> bool:
    """Verify decision trails are complete"""

    if event.event_type == 'DECISION':
        required_fields = [
            'reasoning',           # Why this decision?
            'alternatives',        # What else was considered?
            'confidence',          # How certain?
            'provenance'           # Where did data come from?
        ]

        for field in required_fields:
            if field not in event.payload:
                return False

    return True
```

**Dashboard Indicator**: Green if all decisions are inspectable

### Compliance Dashboard

The dashboard displays a constitution scorecard:

```
Constitutional Compliance Scorecard
═══════════════════════════════════════════════════════

Principle 1: GAIA Never Lies
├─ Transparency: ✓ 100% of recent events explicit
├─ Confidence tracking: ✓ All LLM responses include confidence
└─ Status: ✓ COMPLIANT

Principle 2: GAIA Admits Limits
├─ Authority boundaries: ✓ All respected
├─ Observer isolation: ✓ ARGUS read-only maintained
└─ Status: ✓ COMPLIANT

Principle 3: GAIA Degrades Gracefully
├─ Error handling: ✓ No silent failures detected
├─ Fallback mechanisms: ✓ All deployed
└─ Status: ✓ COMPLIANT

Principle 4: GAIA Learns Explicitly
├─ Proposal-based learning: ✓ All learning is proposational
├─ Approval gates: ✓ All promotions approved
└─ Status: ✓ COMPLIANT

Principle 5: GAIA Remains Inspectable
├─ Decision trails: ✓ All decisions traceable
├─ Provenance tracking: ✓ Complete
└─ Status: ✓ COMPLIANT

Overall Trust Score: 100%
═══════════════════════════════════════════════════════
```

### Violation Detection

When a constitutional violation is detected:

1. **Event is flagged**: `constitutional_check: FAIL`
2. **Alert appears**: Visual warning in dashboard
3. **Context provided**: Explanation of what was violated and why
4. **Remediation suggested**: Recommended corrective action
5. **Logged permanently**: All violations recorded for audit trail

---

## Implementation Checklist

### Core Infrastructure (v0.5.0)

- [ ] **EventBus Implementation**
  - [ ] SQLite event store
  - [ ] Event schema definition
  - [ ] Real-time subscription API
  - [ ] Event filtering and query
  - [ ] Export functionality

- [ ] **Component Integration**
  - [ ] VULCAN emits creation events
  - [ ] MYCEL emits LLM request/response events
  - [ ] MNEMIS emits memory events
  - [ ] WARDEN emits compliance events
  - [ ] ARGUS emits pattern events
  - [ ] ECHO emits indexing events

- [ ] **Component Graph**
  - [ ] Graph data structure
  - [ ] Component status tracking
  - [ ] Connection mapping
  - [ ] Status indicator logic
  - [ ] Real-time updates

### Dashboard UI (v0.5.0)

- [ ] **Streamlit Integration**
  - [ ] Main dashboard layout
  - [ ] Sidebar navigation
  - [ ] Real-time event streaming
  - [ ] Component graph visualization
  - [ ] Event timeline display

- [ ] **Scenario Runner**
  - [ ] Scenario 1: New Project Creation
  - [ ] Scenario 2: Existing Project Integration
  - [ ] Playback controls (play, pause, reset)
  - [ ] Speed adjustment
  - [ ] Step-through navigation
  - [ ] Event log display

- [ ] **Delta Analysis**
  - [ ] State capture (before/after)
  - [ ] Delta computation
  - [ ] Comparison visualization
  - [ ] Export functionality
  - [ ] Result report generation

- [ ] **Compliance Dashboard**
  - [ ] Constitution scorecard
  - [ ] Principle checkers (5 checks)
  - [ ] Violation detection and alerts
  - [ ] Trust score calculation
  - [ ] Audit trail display

### Scenario Execution (v0.5.0)

- [ ] **Scenario 1: New Project Creation**
  - [ ] VULCAN integration
  - [ ] 7-step questionnaire
  - [ ] Event emission at each step
  - [ ] Registry integration
  - [ ] Completion validation

- [ ] **Scenario 2: Existing Project Integration**
  - [ ] WARDEN pre-scan
  - [ ] Dependency analysis
  - [ ] Secret scanning
  - [ ] Configuration extraction
  - [ ] Registry registration

### Testing & Validation (v0.5.0)

- [ ] **Unit Tests**
  - [ ] EventBus functionality
  - [ ] Event schema validation
  - [ ] Component status tracking
  - [ ] Compliance checkers
  - [ ] Delta computation

- [ ] **Integration Tests**
  - [ ] Full scenario 1 execution
  - [ ] Full scenario 2 execution
  - [ ] Event propagation
  - [ ] State consistency
  - [ ] Compliance maintenance

- [ ] **Manual Testing**
  - [ ] Dashboard load and rendering
  - [ ] Real-time event updates
  - [ ] Scenario playback
  - [ ] Delta analysis accuracy
  - [ ] Compliance alerting

### Documentation (v0.5.0)

- [ ] **User Guide**
  - [ ] Dashboard navigation
  - [ ] Scenario execution
  - [ ] Reading the event timeline
  - [ ] Interpreting compliance scores

- [ ] **Developer Guide**
  - [ ] EventBus API reference
  - [ ] Event schema documentation
  - [ ] Component integration guide
  - [ ] Scenario definition format

- [ ] **Architecture Documentation**
  - [ ] Event bus design rationale
  - [ ] Component graph design
  - [ ] Scenario framework
  - [ ] Delta analysis approach

---

## Appendix A: Event Bus SQL Schema

```sql
CREATE TABLE events (
    id TEXT PRIMARY KEY,
    timestamp DATETIME NOT NULL,
    source TEXT NOT NULL,
    event_type TEXT NOT NULL,
    payload TEXT NOT NULL,  -- JSON
    parent_event_id TEXT,   -- For causality
    constitutional_check TEXT,  -- PASS, WARN, FAIL
    metadata TEXT,  -- JSON
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_timestamp ON events(timestamp);
CREATE INDEX idx_source ON events(source);
CREATE INDEX idx_event_type ON events(event_type);
CREATE INDEX idx_parent_event_id ON events(parent_event_id);
CREATE INDEX idx_constitutional_check ON events(constitutional_check);
```

---

## Appendix B: Component Status Codes

```
GREEN (●):   Component operational, recent activity
YELLOW (◐):  Component operational, but warnings present
RED (●):     Component error or critical issue
GRAY (○):    Component idle or awaiting input
BLUE (◆):    Component placeholder (RAVEN, future components)
```

---

## Appendix C: Scenario Definition Format

Scenarios are defined in JSON for easy templating:

```json
{
  "scenario": {
    "name": "New Project Creation",
    "description": "Walk through 7-step VULCAN questionnaire",
    "steps": [
      {
        "id": "vulcan_start",
        "action": "VULCAN.start_creation_wizard",
        "expected_event": "PROJECT_CREATION_STARTED"
      },
      {
        "id": "questionnaire_step_1",
        "action": "VULCAN.submit_questionnaire_step",
        "params": {
          "step": 1,
          "project_name": "MyAgent v1",
          "description": "Test project"
        },
        "expected_event": "QUESTIONNAIRE_STEP_1"
      }
    ]
  }
}
```

---

## Appendix D: Trust Score Calculation

Trust Score = (Compliance Points / Total Possible Points) * 100

**Points Allocation:**

- Never Lies (100 points)
  - All events transparent: +100
  - Partial transparency: +50
  - Silent failures: 0

- Admits Limits (100 points)
  - All authority boundaries respected: +100
  - One violation: +50
  - Multiple violations: 0

- Degrades Gracefully (100 points)
  - All failures logged: +100
  - Most failures logged: +50
  - Silent failures: 0

- Learns Explicitly (100 points)
  - All learning proposal-based: +100
  - Some auto-learning: +50
  - Autonomous learning: 0

- Remains Inspectable (100 points)
  - All decisions traceable: +100
  - Some decisions traceable: +50
  - Black-box decisions: 0

**Total Possible Points**: 500
**Minimum Trust Score**: 0%
**Maximum Trust Score**: 100%

---

## Appendix E: Reading the Event Timeline

The event timeline is the heart of dashboard validation:

```
Timeline Reading Guide:

Event Entry:
┌────────────────────────────────────────────────────┐
│ [10:00:01] VULCAN • PROJECT_CREATION_STARTED       │
│ └─ Payload: {"project_name": "MyAgent v1"}         │
│ └─ Constitutional: ✓ PASS                          │
│ └─ Causality: (root event)                         │
└────────────────────────────────────────────────────┘

Color Coding:
- VULCAN events: Purple
- MYCEL events: Green
- MNEMIS events: Blue
- WARDEN events: Red
- ARGUS events: Orange
- ECHO events: Gray
- RAVEN events: Yellow

Constitutional Indicator:
✓ PASS  - Event complies with all 5 principles
⚠ WARN  - Event has minor compliance issue (warning)
✗ FAIL  - Event violates a principle (critical)
```

---

## Summary

The Dashboard-First Approach represents a fundamental shift in GAIA testing:

1. **Observability First**: All component interactions visible and traceable
2. **Event-Driven Architecture**: Central EventBus captures all system behavior
3. **Interactive Validation**: Users can execute scenarios and observe results
4. **Constitutional Verification**: Continuous compliance checking against 5 principles
5. **Delta Analysis**: Before/after state comparison for rigorous validation

This methodology ensures that GAIA remains transparent, trustworthy, and inspectable as it grows in complexity.

---

**Document Version**: 1.0
**Last Updated**: Feb 5, 2026
**Author**: GAIA Ecosystem Team
