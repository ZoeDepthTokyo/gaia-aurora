# AURORA 7-Pass UX Analysis Framework

## Pass 1: Mental Model Alignment
**Question**: What does the user THINK should happen?

**Checks**:
- Does UI match user's conceptual model?
- Are actions where users expect them?
- Does terminology align with domain language?
- Are outcomes predictable?

**Output**: Mental model gaps and misalignments

## Pass 2: Information Architecture
**Question**: How are concepts organized?

**Checks**:
- Is navigation intuitive?
- Are groupings logical?
- Is hierarchy clear (primary vs secondary actions)?
- Can users find what they need in <3 clicks?

**Output**: IA issues, navigation bottlenecks

## Pass 3: Affordance & Action
**Question**: How do we signal interactivity?

**Checks**:
- Are clickable elements obvious?
- Do buttons look like buttons?
- Is hover state clear?
- Are disabled states distinguishable?

**Output**: Affordance violations, unclear interactions

## Pass 4: Progressive Disclosure
**Question**: What shows immediately vs on-demand?

**Checks**:
- Is complexity hidden until needed?
- Are advanced features accessible but not overwhelming?
- Does primary path stay clear?
- Are details available on hover/expand?

**Output**: Information overload, buried features

## Pass 5: System Feedback
**Question**: How does the system communicate state?

**Checks**:
- Empty states: Are they helpful?
- Loading states: Is progress clear?
- Error states: Are errors actionable?
- Success states: Is completion confirmed?

**Output**: Missing feedback, unhelpful error messages

## Pass 6: Interaction Patterns
**Question**: How do mouse, keyboard, touch, and responsive work?

**Checks**:
- Keyboard navigation: Can user tab through all actions?
- Touch targets: Are they ≥44x44px?
- Responsive: Does it work on mobile/tablet/desktop?
- Shortcuts: Are power-user shortcuts available?

**Output**: Interaction gaps, poor responsive behavior

## Pass 7: Accessibility (WCAG 2.1 AA)
**Question**: Can everyone use this?

**Checks**:
- Color contrast: Text readable for low vision?
- Screen reader: Semantic HTML, ARIA labels?
- Keyboard-only: Can user complete all tasks?
- Focus indicators: Are they visible?

**Output**: WCAG violations, accessibility blockers
