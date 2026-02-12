# jSeeker UX Requirements (Draft)

**Status:** DRAFT - Prepared while waiting for Phase 1 completion
**Created:** 2026-02-10
**For:** AURORA Phase 2 (UX/UI Redesign)

---

## Project Context

**jSeeker v0.2.1** - The Shape-Shifting Resume Engine
- Job-seeking platform that adapts resume content to match job descriptions
- ATS scoring, PDF/DOCX rendering, application tracking, job discovery
- Currently built with Streamlit (planned React migration)

---

## Target Users

**Primary:** Job seekers (technical professionals)
- **Literacy:** Medium (can paste text, use forms)
- **Context:** Stressful job search, need speed + quality
- **Device:** Desktop primary, mobile secondary (job hunting happens on phones)
- **Pain Points:**
  - Need to customize resume for each application
  - ATS rejection due to poor keyword matching
  - Tracking multiple applications across companies
  - Time-consuming manual adaptation

---

## Core Features (Priority Order)

### P0: Critical Features
1. **Resume Generation** (Main Flow)
   - Input: Paste JD text OR provide job URL
   - Process: Extract JD → Parse → Adapt resume → Score ATS → Render PDF/DOCX
   - Output: Downloadable resume + ATS score
   - Performance: < 5 seconds target (currently 3-6s)

2. **ATS Scoring**
   - Platform-aware (Greenhouse, Workday, Lever, iCIMS, Ashby, Taleo)
   - Real-time scoring during generation
   - Visual score display (percentage + feedback)

3. **Cost Transparency**
   - Display: Monthly cost, session cost, budget remaining
   - Warning threshold when approaching limit
   - Hard stop when budget exceeded
   - Location: Always visible (sidebar + page headers)

### P1: High Priority
4. **Application Tracker (CRM)**
   - 3 status pipelines:
     - Resume status (draft, final, exported)
     - Application status (not_applied, submitted, interviewing, offer, rejected)
     - Job status (active, closed, withdrawn)
   - Metrics: Total applications, active, this week, avg ATS score
   - Recent activity view (last 10 applications)

5. **Dashboard**
   - 5 metric cards: Total Apps, Active, This Week, Avg ATS Score, Monthly Cost
   - Recent applications list (company, role, 3 status pills, timestamp)
   - Quick actions: New Resume, View Tracker, Discover Jobs
   - Batch URL intake (paste multiple job URLs)

### P2: Nice to Have
6. **Job Discovery**
   - Tag-based search across job boards
   - Market selection (e.g., "software engineer", "data scientist")
   - Source filtering
   - Results with quick-generate action

7. **Resume Library**
   - Browse generated resumes
   - Search by company/role
   - Quick re-export or edit

---

## User Flows

### Main Flow: Paste JD → Generate → Download
```
1. User lands on "New Resume" page
2. User pastes JD text (or provides URL)
3. User clicks "Generate Resume" button
4. System shows 5-step progress:
   - Step 1/5: Fetching/parsing JD
   - Step 2/5: Matching resume template
   - Step 3/5: Adapting content
   - Step 4/5: Scoring ATS compliance
   - Step 5/5: Rendering PDF + DOCX
5. Success: Download buttons + ATS score display
6. System creates application tracker entry
```

### Secondary Flow: Track Applications
```
1. User navigates to "Tracker" page
2. User sees table of all applications
3. User updates status (inline editing or modals)
4. User views metrics (applications per week, success rate)
```

### Tertiary Flow: Discover Jobs → Generate
```
1. User navigates to "Job Discovery" page
2. User selects markets + sources
3. User clicks "Discover Jobs"
4. System shows results with company, role, link
5. User clicks "Generate Resume" on a job
6. System redirects to New Resume with JD pre-filled
```

---

## Success Criteria

**User can successfully:**
- Generate resume from JD in < 5 seconds
- Understand why ATS score is X% (actionable feedback)
- Track 50+ applications without confusion
- Know their monthly spend at all times
- Use on mobile for job discovery

**System metrics:**
- Resume generation success rate > 95%
- Zero silent failures (all errors actionable)
- ATS score accuracy > 80%
- User satisfaction > 4/5 stars

---

## UX-Critical vs Backend-Only

### UX-Critical (Requires React/Design Work)
- Progress indicators (5-step wizard)
- Real-time budget display
- Error messages (actionable, clear)
- ATS score visualization
- Application status updates (inline editing)
- Empty states ("No applications yet")
- Loading states (spinners, skeletons)
- Mobile responsive layouts

### Backend-Only (No UX Impact)
- YAML resume blocks
- LLM prompt optimization
- Cache strategies
- MYCEL integration
- ARGUS telemetry

---

## Current Streamlit UI Pages

1. **Dashboard** (`ui/pages/1_dashboard.py`)
   - Metrics row (5 cards)
   - Recent applications expander
   - Batch URL intake expander

2. **New Resume** (`ui/pages/2_new_resume.py`)
   - Budget display (3 metrics)
   - JD input (text area + URL input)
   - Generate button (one-click)
   - 5-step progress status
   - Download buttons (PDF/DOCX)

3. **Resume Library** (`ui/pages/3_resume_library.py`)
   - Table of generated resumes
   - Search/filter
   - Re-export actions

4. **Tracker** (`ui/pages/4_tracker.py`)
   - Application table (company, role, 3 statuses)
   - Inline status updates
   - Metrics

5. **Job Discovery** (`ui/pages/5_job_discovery.py`)
   - Market + source selection
   - Search button
   - Results table
   - Quick-generate action

---

## Design Constraints

1. **Mobile First** - Job hunting happens on phones
2. **Professional** - LinkedIn/Indeed quality bar
3. **Speed** - Fast generation, no waiting
4. **Transparency** - Always show cost, never hide errors
5. **Accessibility** - WCAG 2.1 AA minimum

---

## Next Steps for AURORA Phase 2

1. **Phase 1: PRD Intake** (Complete this draft)
   - Read all 5 Streamlit pages
   - Extract complete feature list
   - Document all user flows

2. **Phase 2: Inspiration** (Use RAVEN)
   - Research dashboard patterns
   - Research wizard/stepper patterns
   - Research application tracker CRM patterns
   - Research job board UX patterns

3. **Phase 3: UX Spec** (7-Pass Analysis)
   - Mental model alignment
   - Information architecture
   - Affordance & action
   - Progressive disclosure
   - System feedback
   - Interaction patterns
   - Accessibility

4. **Phase 4: Build Order** (Figma Make)
   - 30 numbered prompts for Figma Make
   - Design tokens → Atoms → Molecules → Organisms → Templates → Pages

---

*This is a draft. Will be refined when Phase 2 begins.*
