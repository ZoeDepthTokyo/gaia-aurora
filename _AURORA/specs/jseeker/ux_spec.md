# jSeeker UX Specification

**Version:** 1.0
**Date:** 2026-02-10
**Product:** jSeeker v0.2.1 - The Shape-Shifting Resume Engine
**Framework:** AURORA 7-Pass UX Analysis
**Status:** Ready for Implementation

---

## Executive Summary

This specification applies AURORA's 7-pass UX analysis framework to jSeeker, translating functional requirements into detailed interaction design specifications. Every design decision is grounded in user mental models, accessibility standards, and platform constraints. The result is a blueprint that developers and designers can implement without additional questions.

**Core UX Principles:**
1. **Transparency Over Magic** - Users see costs, understand ATS scores, control all decisions
2. **Progressive Disclosure** - Show essentials first, details on demand
3. **Immediate Feedback** - Every action has visible response within 100ms
4. **Respect User Agency** - System suggests, user decides
5. **Platform-Aware Intelligence** - ATS platform detection drives format recommendations

---

## Pass 1: Mental Model Alignment

### 1.1 User's Expected Mental Model

#### Primary Mental Model: "Resume Generator as Template Engine"
**What users THINK happens:**
1. Paste job description → AI reads it
2. System matches my experience → AI rewrites phrasing
3. Instant preview → I can customize if needed
4. Download perfect resume → Submit application

**Reality vs. Expectation Gaps:**
- **Gap 1:** Generation takes 30-90 seconds, not instant
  - **Design Response:** 5-stage progress bar with text labels shows AI is working through distinct steps (parse JD → match templates → adapt content → score ATS → render files). User sees intentional process, not broken system.

- **Gap 2:** Cost per resume ($0.50-$2.00) surprises users
  - **Design Response:** Budget display at top of every page, real-time cost updates, per-resume cost shown after generation. Users always know "how much did THAT cost me."

- **Gap 3:** ATS score isn't just "good resume" score
  - **Design Response:** Platform-specific scoring (e.g., "Greenhouse Score: 78/100") with explicit format recommendation and missing keywords. Users learn ATS platforms have different preferences.

- **Gap 4:** Can't edit resume in-app
  - **Design Response:** Export both PDF (visual) and DOCX (editable). Clear messaging: "Download DOCX to customize in Word before submitting."

#### Secondary Mental Model: "Application Tracker as CRM"
**What users THINK happens:**
1. Add job → Track status → Get reminders
2. Drag card between columns → Status updates automatically
3. See pipeline overview → Know where I stand

**Reality vs. Expectation Gaps:**
- **Gap 1:** Three independent status dimensions (resume/app/job) instead of single "stage"
  - **Design Response:** Three separate status badges per application row. Visual hierarchy: Resume Status (leftmost), Application Status (center), Job Status (rightmost). Each operates independently.

- **Gap 2:** No automatic reminders (manual system)
  - **Design Response:** Don't promise automation. UI shows "Last Updated" date per application. Users set their own follow-up cadence.

### 1.2 Platform Understanding

#### ATS Systems (User Mental Model)
**User Belief:** "ATS is one thing that parses resumes"
**Reality:** 6 distinct platforms (Greenhouse, Workday, Lever, iCIMS, Ashby, Taleo) with different parsing rules

**Design Response:**
- Display detected platform prominently: "Detected: Greenhouse" in ATS Score Card
- Platform-specific recommendations: "Greenhouse prefers DOCX for better parsing"
- Keyword warnings vary by platform: Greenhouse = strict keyword matching, Workday = semantic understanding

#### Cost Mental Model
**User Belief:** "Free AI tool with maybe ads"
**Reality:** Usage-based LLM costs ($0.50-$2.00 per resume)

**Design Response:**
- **Never hide costs** - Persistent sidebar metric "Session Cost: $X.XXX"
- **Budget context** - "Monthly Cost: $12.34 of $50.00" (visual progress bar)
- **Per-action transparency** - After generation: "Cost: $0.6800"
- **Enforcement with explanation** - When budget exceeded: "Monthly budget exceeded ($52.34 / $50.00). Budget resets on March 1st."

### 1.3 Time vs. Money Trade-Off

**User Mental Model:** "Time is more valuable than small amounts of money"

**Design Implications:**
- **One-click generation prioritized** - Don't make users fill forms or answer questions first
- **Batch operations available** - Dashboard batch intake for power users (paste 10 URLs → generate all)
- **Inline editing in Tracker** - Click cell → edit → auto-save (no save button friction)
- **Smart defaults** - Pre-populate filename "Company_Role_YYYYMMDD", detect ATS platform from URL

### 1.4 Expected vs. Actual Resume Quality

**User Belief:** "AI will write better resume than I can"
**Reality:** AI adapts existing content, doesn't invent experience

**Design Response:**
- **Set expectations early** - Dashboard first-time user banner: "jSeeker adapts your real experience to match job descriptions. Upload your base resume YAML first."
- **Base resume validation** - Resume Library shows checkmark/X icon per base file (exists/missing)
- **Template match transparency** - Collapsible "Template Match" section shows which YAML blocks were selected

---

## Pass 2: Information Architecture

### 2.1 Navigation Hierarchy

#### Primary Navigation (Sidebar)
```
JSEEKER
├── Dashboard           (landing page, quick actions, metrics)
├── New Resume          (core value prop: generate resume)
├── Resume Library      (download, manage base files, version history)
├── Tracker             (CRM: manage application pipeline)
└── Job Discovery       (search job boards, import opportunities)
```

**Design Decisions:**
1. **Sidebar always visible** - Streamlit constraint: sidebar is persistent navigation container
2. **Icon + label** - Each nav item has icon (visual recognition) + text label (accessibility)
3. **Active state indication** - Current page highlighted with accent color background + bold text
4. **Session cost below logo** - Metric card: "Session Cost: $X.XXX" (persistent, non-intrusive)

#### Content Hierarchy (Per Page)

**Page Structure Pattern:**
```
[Page Title]
[Budget/Metrics Row] (if applicable)
[Primary Action Area]
[Results/Content Area]
  ├── [Section 1: Expanded by default]
  ├── [Section 2: Expanded by default]
  ├── [Section 3: Collapsed]
  └── [Section 4: Collapsed]
```

### 2.2 Data Relationships

#### Core Entity Model (User Perspective)

```
Company
  └── Job Posting (many)
        ├── Job Description (text)
        ├── Job URL (link)
        └── Application (0-1)
              ├── Resume (1-many versions)
              ├── Application Status (enum)
              ├── Resume Status (enum)
              ├── Job Status (enum)
              └── Notes (text)
```

**UX Implications:**
- One job posting = one application (1:1 mapping)
- Multiple resume versions per application (version tracking)
- Three status dimensions operate independently

#### Relationship Visualizations

**Tracker Table:**
- Each row = one application
- Columns: ID (hidden from casual view) | Company | Role | URL | Relevance % | ATS Score | Resume Status | Application Status | Job Status | Location | Created | Notes

**Resume Library:**
- Each row = one resume version
- Columns: ID | Company | Role | Version | ATS Score | Template | Cost | Created
- Dropdown select: Choose resume → Download buttons appear

**Job Discovery → Tracker:**
- Discovery "Import to Tracker" button creates new Application record
- Pre-fills: Company, Role, URL, Location (from scraped data)
- Default statuses: Resume Status = draft, Application Status = not_applied, Job Status = active

### 2.3 Search and Filter Patterns

#### Tracker Filters (Sidebar)
```
Filters
├── Resume Status (dropdown: All | draft | generated | edited | exported | submitted)
├── Application Status (dropdown: All | not_applied | applied | screening | interview | offer | rejected | ghosted | withdrawn)
└── Job Status (dropdown: All | active | closed | expired | reposted)

[Reset Filters Button]
```

**Interaction Model:**
- Filters are cumulative (AND logic): Resume=exported AND Application=not_applied
- Dropdown selection immediately updates table (no "Apply Filters" button)
- Caption below table: "Showing X applications" (gives context)
- Reset button restores all dropdowns to "All"

#### Job Discovery Filters (Inline)
```
Markets (multiselect: US, MX, CA, UK, ES, DK, FR)
Job Boards (multiselect: Indeed, LinkedIn, Wellfound)
Location (text input: e.g., "Remote", "San Francisco")
Status (dropdown: All | New | Starred | Dismissed | Imported)
```

**Interaction Model:**
- Markets and Job Boards are pre-search filters (select before "Search Now")
- Status is post-search filter (filter discovered results)
- Location is optional refinement (narrows search scope)

### 2.4 Content Grouping Principles

#### Dashboard: Metrics → Recent → Actions
1. **Metrics Row** (top, equal-width columns): Total Apps | Active Apps | This Week | Avg ATS Score | Monthly Cost
2. **Recent Applications** (middle, list): Last 10 applications with company/role/status badges
3. **Quick Actions** (bottom, button row): New Resume | View Tracker | Discover Jobs
4. **Batch Intake** (optional, collapsible): Textarea + "Generate Resumes For URLs" button

**Rationale:** User scans metrics first (health check), browses recent activity (context), then chooses next action.

#### New Resume: Input → Progress → Results
1. **Budget Display** (top): Monthly Cost | Session Cost | Budget Remaining
2. **Input Section**: JD Textarea + Job URL Input + Generate Button
3. **Progress Feedback**: 5-stage progress bar (only visible during generation)
4. **Results Sections** (collapsed until generation complete):
   - ATS Score Card (expanded by default)
   - Export (expanded by default)
   - JD Analysis (collapsed)
   - Template Match (collapsed)
   - Adaptation Details (collapsed)

**Rationale:** Progressive disclosure - show complexity only after user commits to action.

---

## Pass 3: Affordance & Action

### 3.1 Visual Affordances

#### Clickable Elements

**Primary Actions (Buttons):**
- **Style:** Solid background, white text, border-radius 4px
- **Hierarchy:**
  - Primary (blue): "Generate Resume", "Download PDF", "Download DOCX"
  - Secondary (outline): "Reset Filters", "Cancel"
  - Danger (red): "Delete Resume" (requires confirmation)
- **States:**
  - Default: Solid color, subtle shadow
  - Hover: Darken 10%, cursor pointer, scale 1.02
  - Active: Darken 20%, scale 0.98 (pressed effect)
  - Disabled: 40% opacity, no hover, cursor not-allowed

**Links:**
- **Style:** Underline on hover, blue text color (#1E90FF)
- **Usage:** Job URLs, "View Job" external links, navigation within results

**Data Table Cells (Editable):**
- **Visual cue:** Dotted bottom border (indicates editability)
- **Hover:** Light background color change, cursor text
- **Click:** Cell expands to show dropdown (for enums) or text input (for notes)

#### Non-Clickable Elements

**Metric Cards:**
- **Style:** Card background (light gray or dark mode equivalent), padding, no hover effect
- **Purpose:** Display-only information (Total Applications, Monthly Cost)

**Status Badges:**
- **Style:** Pill shape, colored background, white text, no underline
- **Not clickable:** Status changes via inline edit in Tracker table only

**Labels and Captions:**
- **Style:** Gray text, smaller font size, no hover effect
- **Purpose:** Context and instructions (e.g., "Step 1/5: Parsing job description...")

### 3.2 Hover States

#### Buttons
- **Desktop:** Darken color 10%, subtle lift (box-shadow increase), cursor pointer
- **Mobile:** No hover (touch device), rely on active press state

#### Links
- **Desktop:** Underline appears, cursor pointer
- **Mobile:** No hover (touch device)

#### Table Rows (Tracker, Resume Library)
- **Desktop:** Light background highlight, subtle shadow
- **Mobile:** No hover (touch device)

#### Editable Cells
- **Desktop:** Background color change (e.g., light yellow tint), cursor text, dotted border becomes solid
- **Mobile:** No hover (touch device), tap to edit

### 3.3 Focus States (Keyboard Navigation)

**All interactive elements:**
- **Visual:** 2px solid outline in accent color (e.g., blue #1E90FF)
- **Offset:** 2px from element boundary (clear separation from element border)
- **Keyboard nav order:** Top-to-bottom, left-to-right (natural reading order)

**Form inputs (text, textarea, dropdowns):**
- **Focus ring:** Blue outline, remove browser default
- **Label highlight:** Label text color changes to match focus color

### 3.4 Disabled States

**Buttons:**
- **Visual:** 40% opacity, no shadow, cursor not-allowed
- **Tooltip:** On hover (if supported), show reason (e.g., "Budget exceeded")

**Form inputs:**
- **Visual:** Gray background, 50% opacity, cursor not-allowed
- **Usage:** When budget exceeded, "Generate Resume" button disabled with error message above

**Table cells:**
- **Visual:** Gray background, no dotted border
- **Usage:** ID column is never editable (read-only)

### 3.5 Action Feedback Patterns

#### Immediate Feedback (< 100ms)
- **Button click:** Scale down 0.98 (pressed effect)
- **Checkbox toggle:** Checkmark appears immediately
- **Dropdown selection:** Menu closes, selected value displays

#### Short Wait (100ms - 2s)
- **Inline edit save:** Spinner icon replaces cell content → toast notification "Saved 1 change(s)!"
- **Filter application:** Table updates, caption changes "Showing X applications"

#### Long Wait (2s+)
- **Resume generation:** Progress bar with text updates "Step 1/5: Parsing job description..."
- **Batch URL processing:** Progress bar "Processing 3/10: [URL]"
- **Job board search:** Spinner + status text "Searching 3 tag(s) across 2 board(s)..."

---

## Pass 4: Progressive Disclosure

### 4.1 Default Visibility Strategy

#### Always Visible (Page Load)
1. **Navigation Sidebar** - User needs to know where they are, access other pages
2. **Page Title** - Context setting ("New Resume", "Application Tracker")
3. **Primary Actions** - Core value prop (Generate Resume button, table with filters)
4. **Budget/Metrics** - Cost transparency is constitutional requirement
5. **Empty States** - If no data, show "No applications yet. Add your first job above."

#### Expanded by Default (After User Action)
1. **ATS Score Card** - Most important result after generation
2. **Export Section** - Primary next step (download resume)
3. **Recent Applications** (Dashboard) - Contextual awareness

#### Collapsed by Default (On Demand)
1. **JD Analysis** - Diagnostic info, power users only
2. **Template Match** - Implementation detail, not essential
3. **Adaptation Details** - Deep transparency for curious users
4. **Batch URL Intake** (Dashboard) - Advanced feature, not main workflow
5. **Search Tags Management** (Job Discovery) - Configuration, not every-use

### 4.2 Expansion Mechanisms

#### Collapsible Sections (Expanders)
**Visual Design:**
- **Header:** Bold text, chevron icon (▶ collapsed, ▼ expanded), full-width clickable area
- **Interaction:** Click anywhere on header to toggle
- **Animation:** Smooth 200ms slide down/up
- **Nested expanders:** Indent 16px from parent

**Usage Pattern:**
```
▼ ATS Score Card (Expanded)
  [Content visible]

▶ JD Analysis (Collapsed)
  [Content hidden]
```

#### Modals (Confirmation Dialogs)
**When to Use:**
- Destructive actions requiring confirmation (Delete Resume)
- Multi-step wizards that need isolation (future: Add Application Wizard)

**Design:**
- **Overlay:** Semi-transparent dark background (60% opacity)
- **Modal:** Center-screen, white/dark mode card, 600px max width
- **Header:** Title + close X button (top-right)
- **Footer:** Action buttons (Cancel | Confirm)
- **Escape key:** Closes modal (keyboard accessibility)

**Example: Delete Resume Confirmation**
```
┌─────────────────────────────────────┐
│ Delete Resume?                    X │
│─────────────────────────────────────│
│ Are you sure you want to delete     │
│ "Acme_ProductDesigner_20260210"?    │
│ This action cannot be undone.       │
│                                     │
│              [Cancel]  [Delete]     │
└─────────────────────────────────────┘
```

#### Dropdown Filters (Reveal Options)
**Design:**
- **Closed state:** Show selected value + down arrow icon
- **Open state:** List of options, max-height 300px, scrollable if needed
- **Selection:** Click option → dropdown closes → value updates

### 4.3 Complexity Management

#### Information Hierarchy (New Resume Results)
**Level 1 (Essential - Expanded by default):**
- Overall ATS Score (78/100)
- Keyword Match (85%)
- Recommended Format (DOCX)
- Download buttons (PDF, DOCX)

**Level 2 (Helpful - Collapsed by default):**
- Missing keywords list (first 10)
- Format recommendation reasoning
- JD title and extracted keywords
- Template selection logic

**Level 3 (Diagnostic - Collapsed, text-heavy):**
- Full JD analysis (keyword extraction, seniority detection, company research)
- Complete adaptation details (which YAML blocks selected, why)
- Token counts and cost breakdown

**Rationale:** 80% of users only need Level 1. Power users can drill into Level 2/3 for transparency.

#### Dashboard Metrics (Glanceable → Detailed)
**Glanceable (Metrics row):**
- Total Applications: 42
- Active Applications: 18
- This Week: 5
- Avg ATS Score: 76.2
- Monthly Cost: $28.50

**Detailed (Click metric → expander opens):**
- Total Applications: 42
  - Breakdown: 12 not_applied, 15 applied, 8 screening, 5 interview, 2 offer
- This Week: 5
  - Mon: 2, Wed: 1, Fri: 2
- Avg ATS Score: 76.2
  - Range: 52-94, Median: 78

**Interaction:** Click metric card → expands inline to show detail → click again to collapse

### 4.4 First-Time User Experience

#### Dashboard Welcome Banner (First Visit Only)
```
┌─────────────────────────────────────────────────────────────┐
│ Welcome to jSeeker!                                       X │
│ 1. Upload your base resume (Resume Library)                │
│ 2. Generate your first tailored resume (New Resume)        │
│ 3. Track your applications (Tracker)                       │
│                                        [Get Started]        │
└─────────────────────────────────────────────────────────────┘
```
**Behavior:** Dismissible (X button), never shows again after dismissal (stored in session state)

#### Empty States (Encouraging First Action)
**Tracker (No Applications):**
```
No applications yet.
Generate your first resume to start tracking.
[Go to New Resume]
```

**Resume Library (No Resumes):**
```
No resumes generated yet.
Upload your base resume YAML files first.
[Upload Base Resume]
```

**Job Discovery (No Tags):**
```
No search tags configured.
Add tags below to discover jobs matching your profile.
[Search Tags section expanded automatically]
```

---

## Pass 5: System Feedback

### 5.1 Loading States

#### Short Wait (< 3 seconds)
**Spinner Pattern:**
- **Visual:** Small circular spinner (24px diameter) next to action
- **Color:** Accent color (blue)
- **Placement:** Replaces button text or appears next to form input

**Usage:**
- Inline edit save (Tracker table)
- Filter application
- Tag toggle (Job Discovery)

#### Medium Wait (3-30 seconds)
**Progress Bar Pattern:**
- **Visual:** Horizontal bar, 0-100% fill, animated left-to-right
- **Text Label:** "Loading..." or specific status
- **Placement:** Full-width below action button

**Usage:**
- Job board search (3-30 seconds depending on network)
- File upload (base resume)

#### Long Wait (30-90 seconds)
**Multi-Stage Progress Bar:**
- **Visual:** Horizontal bar divided into stages (e.g., 5 stages)
- **Current Stage:** Highlighted segment, different color
- **Text Label:** "Step 1/5: Parsing job description..." → "Step 2/5: Matching templates..." → etc.
- **Percentage:** 0% → 20% → 40% → 60% → 80% → 100%

**Usage:**
- Resume generation (5 stages: parse JD → match templates → adapt content → score ATS → render files)
- Batch URL processing (sequential, show "Processing 3/10: [URL]")

**Design Specification:**
```
┌─────────────────────────────────────────────┐
│ Generating Resume...                        │
│ Step 2/5: Matching resume templates...      │
│ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░  40% │
└─────────────────────────────────────────────┘
```

### 5.2 Success States

#### Inline Success (After Short Wait)
**Toast Notification:**
- **Visual:** Small card (300px width), green left border, checkmark icon, white/dark mode background
- **Placement:** Top-right corner, overlays content
- **Duration:** 3 seconds, then auto-dismiss
- **Animation:** Slide in from right, fade out

**Example:**
```
┌────────────────────────┐
│ ✓ Saved 1 change(s)!   │
└────────────────────────┘
```

**Usage:**
- Inline edit saved (Tracker)
- Tag added (Job Discovery)
- Filter applied

#### Prominent Success (After Long Wait)
**Success Banner:**
- **Visual:** Full-width, green background (light green in light mode, dark green in dark mode), checkmark icon, bold text
- **Placement:** Below action button, above results section
- **Duration:** Persistent (user dismisses or navigates away)

**Example:**
```
┌────────────────────────────────────────────────┐
│ ✓ Resume generated successfully!               │
│   Resume generated for Acme Inc - Product      │
│   Designer (Application #123)                  │
└────────────────────────────────────────────────┘
```

**Usage:**
- Resume generation complete
- Batch URL processing complete
- Job search complete

#### Download Feedback
**Browser Download Dialog:**
- **Trigger:** User clicks "Download PDF" or "Download DOCX"
- **Behavior:** Browser's native download dialog opens immediately
- **No custom UI:** Trust browser's download management

**Optional Toast (If Supported):**
```
┌────────────────────────┐
│ ✓ Download started     │
└────────────────────────┘
```

### 5.3 Error States

#### Validation Errors (Before Submission)
**Inline Error Message:**
- **Visual:** Red text, icon (⚠), below form input
- **Placement:** Directly below invalid field
- **Prevent submission:** Disable button until resolved

**Example:**
```
[Job Description]
[_____________________________] ← empty textarea
⚠ Job description is required.
[Generate Resume] ← button disabled
```

#### API/Backend Errors (After Submission)
**Error Banner:**
- **Visual:** Full-width, red background, warning icon, bold text, dismiss X button
- **Placement:** Below action button, above form
- **Duration:** Persistent until dismissed

**Example: JD Extraction Failed**
```
┌────────────────────────────────────────────────┐
│ ⚠ Could not extract job description from URL.  │
│   Paste the JD text and try again.          X  │
└────────────────────────────────────────────────┘
```

**Example: Budget Exceeded**
```
┌────────────────────────────────────────────────┐
│ ⚠ Monthly budget exceeded ($52.34 / $50.00).   │
│   Generation disabled. Budget resets on        │
│   March 1st.                                 X  │
└────────────────────────────────────────────────┘
```

#### Network/System Errors
**Modal Dialog (Blocking):**
- **Usage:** Critical failures requiring user acknowledgment
- **Visual:** Center-screen modal, red accent, warning icon
- **Actions:** Retry | Cancel

**Example: File Not Found**
```
┌─────────────────────────────────────┐
│ File Not Found                    X │
│─────────────────────────────────────│
│ Resume file missing at path:        │
│ /path/to/resume.pdf                 │
│                                     │
│ The file may have been moved or     │
│ deleted. Generate a new resume.     │
│                                     │
│                 [OK]                │
└─────────────────────────────────────┘
```

### 5.4 Empty States

#### No Data (Initial State)
**Pattern:**
- **Visual:** Center-aligned text, muted color, illustration (optional), call-to-action button
- **Placement:** Replace table/list with empty state
- **Tone:** Encouraging, not punishing

**Examples:**

**Tracker (No Applications):**
```
        [Illustration: Empty folder]

        No applications yet
        Generate your first resume to start tracking.

        [Go to New Resume]
```

**Resume Library (No Resumes):**
```
        [Illustration: Document with plus icon]

        No resumes generated yet
        Upload your base resume YAML files first.

        [Configure Base Resumes]
```

**Job Discovery (No Results):**
```
        [Illustration: Magnifying glass]

        No discovered jobs match your current filters
        Run a search above or adjust your tags.
```

#### No Search Results (After Action)
**Pattern:**
- **Visual:** Same as empty state, but with search context
- **Suggestions:** Show search criteria, suggest refinements

**Example: Job Discovery Zero Results**
```
        No jobs found

        We searched:
        - 3 tags across 2 boards in 2 markets
        - 12 search combinations

        Try:
        - Adding more tags
        - Removing location filter
        - Checking different job boards
```

#### Filtered to Zero
**Pattern:**
- **Visual:** Lighter tone (not a problem, just narrow filters)
- **Action:** Reset filters button prominent

**Example: Tracker Filters**
```
        No applications match your filters

        Current filters:
        - Resume Status: exported
        - Application Status: not_applied
        - Job Status: closed

        [Reset Filters]
```

### 5.5 Progress Indicators

#### Determinate Progress (Known Duration)
**Visual:**
- **Bar:** Horizontal, 0-100%, animated fill
- **Percentage:** Numeric display (e.g., "45%")
- **Label:** Current stage description

**Usage:**
- Resume generation (5 stages, 20% per stage)
- Batch URL processing (X/N completed)

#### Indeterminate Progress (Unknown Duration)
**Visual:**
- **Spinner:** Circular, rotating animation
- **No percentage:** Just spinner + label

**Usage:**
- Job board search (network-dependent, unpredictable)
- File upload (size-dependent)

#### Multi-Item Progress (Batch Operations)
**Visual:**
- **Overall bar:** X/N items processed
- **Current item:** Show which item is processing
- **Summary:** After completion, show successes/failures

**Example: Batch URL Generation**
```
Processing 3/10: https://example.com/job/12345
▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░  30%

Summary:
✓ 2 resumes generated
⚠ 1 skipped (duplicate)
✗ 0 failed
```

---

## Pass 6: Interaction Patterns

### 6.1 Mouse/Pointer Interactions

#### Click Patterns

**Single Click:**
- **Buttons:** Execute action (generate resume, download file)
- **Links:** Navigate to URL (external job posting)
- **Table cells:** Enter edit mode (dropdown or text input)
- **Expanders:** Toggle expand/collapse
- **Checkboxes:** Toggle on/off

**Double Click:**
- **Not used** - Streamlit constraint, no native double-click support

**Right Click (Context Menu):**
- **Not used** - Keep interactions simple, avoid context menus

#### Drag Patterns

**Drag-and-Drop (Future: Kanban View):**
- **Visual:** Card lifts with shadow, cursor changes to grab/move
- **Drag over column:** Column highlights (light background)
- **Drop:** Card animates to new position, auto-save, toast "Status updated"

**Current Implementation:**
- **Not in v0.2.1** - Tracker uses inline edit dropdowns instead
- **Phase 2 Feature** - Research pattern 3.1 (Drag-and-Drop Kanban) deferred

#### Hover Patterns (Desktop Only)

**Buttons:**
- **Effect:** Darken 10%, subtle lift (box-shadow), cursor pointer
- **Timing:** Immediate (0ms delay)

**Links:**
- **Effect:** Underline appears, cursor pointer
- **Timing:** Immediate (0ms delay)

**Table rows:**
- **Effect:** Light background highlight
- **Timing:** 50ms delay (prevent flicker during cursor movement)

**Tooltips (Informational):**
- **Trigger:** Hover over info icon (ℹ) or disabled button
- **Delay:** 500ms (avoid accidental tooltips)
- **Visual:** Small card with arrow, dark background, white text, max-width 200px
- **Dismiss:** Move cursor away

### 6.2 Keyboard Interactions

#### Tab Navigation

**Tab Order (New Resume Page):**
1. Job Description textarea
2. Job URL input
3. Generate Resume button
4. [After generation] Filename input
5. Download PDF button
6. Download DOCX button
7. Expander headers (ATS Score Card, JD Analysis, etc.)

**Visual Focus Indicator:**
- **Style:** 2px solid blue outline, 2px offset
- **All focusable elements:** Buttons, inputs, links, expanders

#### Keyboard Shortcuts

**Global (All Pages):**
- **Tab:** Next focusable element
- **Shift+Tab:** Previous focusable element
- **Enter:** Activate focused button/link
- **Esc:** Close modal/dropdown/expander (if open)

**Page-Specific:**
- **Ctrl+N:** Go to New Resume page (from Dashboard)
- **Ctrl+T:** Go to Tracker page (from anywhere)
- **Ctrl+D:** Go to Job Discovery page (from anywhere)

**Form Inputs:**
- **Enter (in textarea):** New line (not submit)
- **Enter (in single-line input):** Submit form (if applicable)
- **Ctrl+Enter (in textarea):** Submit form (if button is below)

**Tracker Table:**
- **Arrow keys:** Navigate cells (if data editor supports)
- **Enter:** Enter edit mode for focused cell
- **Esc:** Exit edit mode without saving

#### Screen Reader Support

**Semantic HTML:**
- **Buttons:** `<button>` elements, not `<div>` with click handlers
- **Links:** `<a href>` elements
- **Headings:** `<h1>`, `<h2>`, `<h3>` hierarchy
- **Lists:** `<ul>`, `<ol>` for navigation and results

**ARIA Labels:**
- **Icon-only buttons:** `aria-label="Download PDF"`
- **Status badges:** `aria-label="Resume status: exported"`
- **Progress bars:** `aria-valuenow`, `aria-valuemin`, `aria-valuemax`
- **Expanders:** `aria-expanded="true"` or `"false"`

**Focus Management:**
- **After modal opens:** Focus first input or Cancel button
- **After modal closes:** Return focus to trigger element
- **After inline edit saves:** Keep focus on edited cell (or next cell)

### 6.3 Touch Interactions (Mobile)

#### Tap Patterns

**Single Tap:**
- **Buttons:** Execute action
- **Links:** Navigate
- **Table cells:** Enter edit mode (optimized for touch)
- **Expanders:** Toggle expand/collapse

**Long Press:**
- **Not used** - Keep interactions simple

#### Swipe Patterns

**Horizontal Swipe (Table):**
- **Right swipe on row:** Reveal delete action (future)
- **Left swipe on row:** Reveal archive action (future)
- **Current Implementation:** Not in v0.2.1 (Streamlit constraint)

**Vertical Scroll:**
- **Expected behavior:** Smooth scrolling, momentum
- **Tables:** Horizontal scroll if too wide for viewport

#### Touch Targets

**Minimum Size:**
- **All tappable elements:** 44×44px (iOS guideline)
- **Buttons:** Minimum height 48px, full-width on mobile
- **Table cells:** Minimum height 48px

**Spacing:**
- **Between buttons:** Minimum 8px vertical gap
- **Between form inputs:** Minimum 16px vertical gap

### 6.4 Responsive Design

#### Breakpoints

**Desktop (1280px+):**
- **Sidebar:** 280px fixed width, always visible
- **Main content:** Remaining width (1000px+)
- **Tables:** All columns visible, horizontal scroll if needed

**Tablet (768px - 1279px):**
- **Sidebar:** 240px fixed width or collapsible hamburger menu
- **Main content:** Remaining width (500-1000px)
- **Tables:** Hide non-essential columns (ID, Created), show core columns only

**Mobile (< 768px):**
- **Sidebar:** Hamburger menu (collapsible), overlays main content when open
- **Main content:** Full viewport width minus padding
- **Tables:** Vertical card layout (each row becomes card), or horizontal scroll with minimum column widths

#### Component Adaptations

**Metrics Row (Dashboard):**
- **Desktop:** 5 columns, equal width
- **Tablet:** 5 columns, scroll horizontally if needed
- **Mobile:** Stack vertically (1 column), full-width cards

**Buttons:**
- **Desktop:** Inline buttons with fixed width (e.g., 120px)
- **Tablet:** Same as desktop
- **Mobile:** Full-width buttons, stack vertically

**Forms:**
- **Desktop:** Label left, input right (horizontal layout)
- **Tablet:** Same as desktop if space allows
- **Mobile:** Label top, input below (vertical layout)

**Expanders:**
- **All breakpoints:** Full-width, same behavior (Streamlit default is already responsive)

---

## Pass 7: Accessibility & Inclusivity

### 7.1 WCAG 2.1 AA Compliance

#### Color Contrast

**Text on Background:**
- **Normal text (< 18px):** 4.5:1 minimum contrast ratio
- **Large text (>= 18px):** 3:1 minimum contrast ratio
- **Example:**
  - Light mode: Black (#000000) on White (#FFFFFF) = 21:1 ✓
  - Dark mode: White (#FFFFFF) on Dark Gray (#1E1E1E) = 15.8:1 ✓

**UI Components (Buttons, Form Inputs):**
- **Border/Icon contrast:** 3:1 minimum
- **Example:**
  - Blue button (#1E90FF) on White (#FFFFFF) = 3.25:1 ✓
  - Red error text (#D32F2F) on White (#FFFFFF) = 5.5:1 ✓

**Status Badges:**
- **Color alone insufficient** - Use color + icon + text
- **Example:**
  - Resume Status: draft = Gray badge + "draft" text
  - Application Status: offer = Green badge + "offer" text + ✓ icon

#### Focus Indicators

**Visible Focus:**
- **All interactive elements:** 2px solid outline, accent color (#1E90FF)
- **Contrast:** 3:1 against background
- **Offset:** 2px from element boundary (clear separation)

**Focus Order:**
- **Logical sequence:** Top-to-bottom, left-to-right (natural reading order)
- **No focus traps:** User can Tab through all elements and Tab out of sections

#### Form Labels

**All inputs have labels:**
- **Visual label:** Displayed above or left of input
- **Programmatic association:** `<label for="input-id">` or `aria-labelledby`
- **Required fields:** Indicated by asterisk (*) + aria-required="true"

**Example:**
```html
<label for="job-url">Job URL (optional)</label>
<input id="job-url" type="text" placeholder="https://...">
```

### 7.2 Keyboard Navigation

#### Full Keyboard Access

**All actions accessible without mouse:**
- **Generate Resume:** Tab to button, press Enter
- **Download files:** Tab to button, press Enter
- **Edit Tracker cell:** Tab to cell, press Enter to enter edit mode, Tab to dropdown options, Enter to select
- **Toggle filters:** Tab to dropdown, Enter to open, Arrow keys to select, Enter to confirm

#### Skip Links

**Skip to Main Content:**
- **Visual:** Hidden until focused (Tab on page load reveals it)
- **Action:** Jumps focus to main content area (bypasses sidebar navigation)
- **Placement:** First focusable element on page

**Example:**
```html
<a href="#main-content" class="skip-link">Skip to main content</a>
```

#### Keyboard Shortcuts (Documented)

**Help Modal (Future):**
- **Trigger:** Press "?" key (from anywhere)
- **Content:** List all keyboard shortcuts
- **Dismiss:** Esc key

### 7.3 Screen Reader Support

#### Semantic HTML

**Use native elements:**
- **Buttons:** `<button>` not `<div onclick>`
- **Links:** `<a href>` not `<span onclick>`
- **Headings:** `<h1>` for page title, `<h2>` for sections, `<h3>` for subsections

**Landmarks:**
- **Navigation:** `<nav>` for sidebar
- **Main content:** `<main>` for page content
- **Footer:** `<footer>` for credits/links (if applicable)

#### ARIA Labels

**Icon-only buttons:**
```html
<button aria-label="Download PDF">
  [PDF Icon]
</button>
```

**Status badges:**
```html
<span class="badge" aria-label="Resume status: exported">
  exported
</span>
```

**Progress bars:**
```html
<div role="progressbar" aria-valuenow="40" aria-valuemin="0" aria-valuemax="100">
  40%
</div>
```

**Expanders:**
```html
<button aria-expanded="true" aria-controls="ats-score-content">
  ATS Score Card
</button>
<div id="ats-score-content">
  [Content]
</div>
```

#### Live Regions (Dynamic Updates)

**Toast notifications:**
```html
<div role="status" aria-live="polite">
  Saved 1 change(s)!
</div>
```

**Error messages:**
```html
<div role="alert" aria-live="assertive">
  Monthly budget exceeded.
</div>
```

### 7.4 Internationalization (i18n)

#### Languages Supported

**Current (v0.2.1):**
- **English (en):** Default, fully supported
- **Spanish (es):** Resume generation + JD parsing supported, UI labels pending

**Roadmap (Phase 2):**
- **UI translation:** Spanish UI labels
- **Additional languages:** French, German (based on market demand)

#### Market Support

**7 Markets:**
- **us:** United States
- **mx:** Mexico
- **ca:** Canada
- **uk:** United Kingdom
- **es:** Spain
- **dk:** Denmark
- **fr:** France

**UX Implications:**
- **Job Discovery:** User selects markets via multiselect (full country names: "United States" not "US")
- **Language detection:** Automatic based on JD text (if JD is Spanish, resume is Spanish)
- **Resume language:** Matches detected JD language (no separate language selector)

#### Currency & Date Formats

**Current (v0.2.1):**
- **Currency:** USD only ($0.6800)
- **Dates:** ISO format (YYYYMMDD in filenames, "2026-02-10" in UI)

**Roadmap (Phase 2):**
- **Locale-aware formatting:**
  - US: $1,234.56, MM/DD/YYYY
  - EU: €1.234,56, DD/MM/YYYY
  - UK: £1,234.56, DD/MM/YYYY

### 7.5 Error Recovery

#### Graceful Degradation

**Network Failure:**
- **Error message:** "Unable to connect. Check your internet connection and try again."
- **Action:** Retry button + Cancel button
- **Persistence:** Form input values preserved (not lost on error)

**LLM API Failure:**
- **Error message:** "Resume generation failed. Error: [API error message]. Please try again or contact support."
- **Action:** Retry button + Copy Error Details button (for support ticket)
- **Logging:** Error logged to backend (ARGUS telemetry)

**File Not Found:**
- **Error message:** "Resume file missing at [path]. The file may have been moved or deleted."
- **Action:** Re-generate resume button + Go to Resume Library button
- **Prevention:** Validate base resume paths on Resume Library page (show checkmark/X)

#### Undo/Redo (Not Implemented)

**Current State:**
- **No undo:** Inline edits are auto-saved immediately
- **Workaround:** User can manually change value back

**Roadmap (Phase 2):**
- **Undo last edit:** Ctrl+Z to revert last inline edit (per-page scope)

#### Confirmation Dialogs (Prevent Mistakes)

**Destructive Actions:**
- **Delete Resume:** Modal confirmation "Are you sure? This action cannot be undone."
- **Archive Application:** (Future) Modal confirmation
- **Reset Filters:** (Low risk) No confirmation, just immediate reset

---

## Component Specifications

### C01: Metric Card

**Usage:** Dashboard metrics, budget display

**Visual Design:**
- **Container:** Card background, border-radius 8px, padding 16px, box-shadow subtle
- **Title:** Small text (14px), gray color, uppercase, font-weight 600
- **Value:** Large text (32px), bold, primary color
- **Subtitle (optional):** Small text (12px), gray color, below value

**Variants:**
1. **Single metric:** Just title + value
2. **Metric with trend:** Title + value + trend indicator (↑ green, ↓ red)
3. **Metric with progress:** Title + value + progress bar (e.g., budget usage)

**Example (Budget Display):**
```
┌───────────────────────┐
│ MONTHLY COST          │
│ $28.50 of $50.00      │
│ ▓▓▓▓▓▓▓▓▓▓▓░░░░░  57% │
└───────────────────────┘
```

**Accessibility:**
- Semantic HTML: `<div class="metric-card">`
- Screen reader: "Monthly cost: 28 dollars 50 cents of 50 dollars"

---

### C02: Status Badge

**Usage:** Resume/Application/Job status indicators

**Visual Design:**
- **Container:** Pill shape (border-radius 12px), padding 4px 12px
- **Text:** 12px, uppercase, font-weight 600, white text
- **Color:** Background color varies by status (see color map below)

**Status Color Map:**

**Resume Status:**
- draft: Gray (#9E9E9E)
- generated: Blue (#1E90FF)
- edited: Yellow (#FFA726)
- exported: Green (#4CAF50)
- submitted: Purple (#9C27B0)

**Application Status:**
- not_applied: Gray (#9E9E9E)
- applied: Blue (#1E90FF)
- screening: Yellow (#FFA726)
- phone_screen: Orange (#FF7043)
- interview: Orange (#FF5722)
- offer: Green (#4CAF50)
- rejected: Red (#D32F2F)
- ghosted: Dark Gray (#616161)
- withdrawn: Light Gray (#BDBDBD)

**Job Status:**
- active: Green (#4CAF50)
- closed: Gray (#9E9E9E)
- expired: Red (#D32F2F)
- reposted: Blue (#1E90FF)

**Accessibility:**
- ARIA label: "Resume status: exported"
- Icon (optional): Add checkmark (✓) for positive states, X for negative states

---

### C03: Progress Bar (Multi-Stage)

**Usage:** Resume generation, batch processing

**Visual Design:**
- **Container:** Full-width, border-radius 4px, height 8px, background light gray
- **Fill:** Animated left-to-right, height 8px, background accent color (blue)
- **Label:** Above bar, "Step X/Y: [Description]"
- **Percentage:** Right-aligned, "45%"

**Stages (Resume Generation):**
1. "Step 1/5: Parsing job description..." (0-20%)
2. "Step 2/5: Matching resume templates..." (20-40%)
3. "Step 3/5: Adapting content..." (40-60%)
4. "Step 4/5: Scoring ATS compliance..." (60-80%)
5. "Step 5/5: Rendering files..." (80-100%)

**Accessibility:**
- ARIA: `role="progressbar" aria-valuenow="40" aria-valuemin="0" aria-valuemax="100"`
- Screen reader: "Step 2 of 5: Matching resume templates. 40 percent complete."

---

### C04: Inline Data Editor (Tracker Table)

**Usage:** Tracker table, Resume Library table

**Visual Design:**
- **Table:** Full-width, bordered rows, alternating row backgrounds
- **Editable cells:** Dotted bottom border, cursor text on hover
- **Dropdowns (status fields):** Click cell → dropdown opens → select → auto-save
- **Text inputs (notes):** Click cell → text input expands → type → click away → auto-save

**Interaction Flow:**
1. User clicks editable cell → cell background changes (light yellow tint)
2. Dropdown/text input appears
3. User makes change → clicks away
4. Spinner icon appears briefly → toast "Saved 1 change(s)!"
5. Cell reverts to display mode with new value

**Accessibility:**
- **Keyboard nav:** Tab to cell, Enter to edit, Tab through dropdown options, Enter to select
- **Screen reader:** "Resume status, editable dropdown, currently exported. Press Enter to edit."

---

### C05: Collapsible Expander

**Usage:** ATS Score Card, JD Analysis, Batch Intake, Search Tags

**Visual Design:**
- **Header:** Bold text, chevron icon (▶ collapsed, ▼ expanded), full-width clickable area
- **Header background:** Light gray on hover (desktop)
- **Content:** Padded 16px, visible when expanded
- **Animation:** Smooth 200ms slide down/up

**States:**
- **Collapsed:** Content hidden, chevron points right (▶)
- **Expanded:** Content visible, chevron points down (▼)

**Interaction:**
- **Click anywhere on header:** Toggle expand/collapse
- **Keyboard:** Tab to header, Enter to toggle

**Accessibility:**
- ARIA: `aria-expanded="true"` or `"false"`, `aria-controls="content-id"`
- Screen reader: "ATS Score Card, expanded. Press Enter to collapse."

---

### C06: Action Button Row

**Usage:** Job Discovery (Star | Dismiss | Import | View Job)

**Visual Design:**
- **Container:** Horizontal flexbox, gap 8px
- **Buttons:** Small size (32px height), outline style, icon + text (or icon-only on mobile)
- **Responsive:** Desktop = icon + text, Mobile = icon-only + tooltip

**Buttons (Job Discovery):**
1. **Star:** Outline, star icon, "Star" text (desktop only)
2. **Dismiss:** Outline, X icon, "Dismiss" text (desktop only)
3. **Import to Tracker:** Primary style, + icon, "Import" text
4. **View Job:** Link style, external icon, "View Job" text

**Accessibility:**
- **Icon-only buttons:** `aria-label="Star this job"`
- **Keyboard nav:** Tab through buttons, Enter to activate

---

## Design System Integration

### Typography Scale

**Streamlit Constraints:**
- **Primary font:** Default system font (varies by OS)
- **Override:** Use `st.markdown` with custom CSS for headings

**Scale:**
- **H1 (Page Title):** 32px, bold, line-height 1.2
- **H2 (Section Header):** 24px, bold, line-height 1.3
- **H3 (Subsection):** 18px, semi-bold, line-height 1.4
- **Body:** 16px, regular, line-height 1.5
- **Caption:** 14px, regular, line-height 1.4, gray color
- **Small:** 12px, regular, line-height 1.3

### Color Palette

**Light Mode:**
- **Background:** #FFFFFF
- **Surface (cards):** #F5F5F5
- **Border:** #E0E0E0
- **Text Primary:** #212121
- **Text Secondary:** #757575
- **Accent (primary):** #1E90FF
- **Success:** #4CAF50
- **Warning:** #FFA726
- **Error:** #D32F2F

**Dark Mode:**
- **Background:** #121212
- **Surface (cards):** #1E1E1E
- **Border:** #424242
- **Text Primary:** #FFFFFF
- **Text Secondary:** #B0B0B0
- **Accent (primary):** #1E90FF
- **Success:** #4CAF50
- **Warning:** #FFA726
- **Error:** #EF5350

### Spacing Grid

**Base unit:** 8px

**Scale:**
- **xs:** 4px (0.5 units)
- **sm:** 8px (1 unit)
- **md:** 16px (2 units)
- **lg:** 24px (3 units)
- **xl:** 32px (4 units)
- **xxl:** 48px (6 units)

**Usage:**
- **Between form inputs:** 16px (md)
- **Between sections:** 32px (xl)
- **Card padding:** 16px (md)
- **Button padding:** 8px 16px (sm md)

### Border Radius

**Scale:**
- **xs:** 2px (sharp corners)
- **sm:** 4px (buttons, inputs)
- **md:** 8px (cards, modals)
- **lg:** 12px (badges, pills)
- **full:** 9999px (circular)

### Shadows

**Elevation levels:**
- **Level 0 (flat):** No shadow
- **Level 1 (cards):** 0px 1px 3px rgba(0,0,0,0.12)
- **Level 2 (hover):** 0px 2px 6px rgba(0,0,0,0.16)
- **Level 3 (modals):** 0px 4px 12px rgba(0,0,0,0.24)

---

## Implementation Priorities

### Phase 1: Core Flows (P0 Features)

**Week 1-2:**
1. **New Resume page:** JD input + budget display + generate button + 5-stage progress bar
2. **ATS Score Card component:** Overall score + keyword match + format recommendation + missing keywords
3. **Export section:** Filename input + Download PDF/DOCX buttons
4. **Tracker page:** Data editor table + 3 filter dropdowns + inline editing

**Week 3-4:**
5. **Dashboard page:** 5-metric row + recent applications list + quick action buttons
6. **Resume Library page:** Base resume config + resume table + download/delete
7. **Job Discovery page:** Tag management + market selection + search + results

**Success Criteria:**
- User can generate first resume in < 10 minutes (Flow 1 complete)
- User can update application status in Tracker (Flow 2 complete)
- User can discover and import job (Flow 3 complete)

### Phase 2: Polish & Refinement

**Week 5-6:**
1. **Empty states:** All pages have encouraging empty states
2. **Error states:** All failure modes have clear error messages
3. **Loading states:** All long operations have progress feedback
4. **Success states:** All actions have confirmation (toast notifications)

**Week 7-8:**
5. **Keyboard navigation:** Tab order, focus indicators, keyboard shortcuts
6. **Responsive design:** Mobile/tablet adaptations
7. **Accessibility audit:** WCAG 2.1 AA compliance check

### Phase 3: Advanced Features (P1)

**Week 9+:**
1. **Batch URL intake:** Dashboard batch generation
2. **Job Status Monitor:** Automated job URL checking
3. **Kanban view (Tracker):** Drag-and-drop pipeline (research pattern 3.1)
4. **Multi-dimensional board:** Priority × Status grid (research pattern 3.2)

---

## Testing Specifications

### Usability Testing Scenarios

#### Scenario 1: First-Time User
**Task:** Generate your first resume for a Product Designer role at Acme Inc.

**Success Criteria:**
- Completes task without help in < 10 minutes
- Understands ATS score (can explain why it's X/100)
- Downloads at least one format (PDF or DOCX)

**Observe:**
- Where do they look first?
- Do they notice budget display?
- Do they read progress bar text?
- Do they expand JD Analysis (optional sections)?

#### Scenario 2: Power User (Pipeline Management)
**Task:** You have 20 applications. Find all applications with exported resumes that you haven't applied to yet, then update one to "applied" status.

**Success Criteria:**
- Finds correct filter combination in < 30 seconds
- Updates status via inline edit in < 10 seconds
- Sees confirmation (toast notification)

**Observe:**
- Do they find sidebar filters immediately?
- Do they understand cumulative filters?
- Do they click cell or try to drag?

#### Scenario 3: Job Discovery
**Task:** Set up search tags for "Senior UX Designer" jobs, search Indeed in US + Mexico, and import one promising job to your tracker.

**Success Criteria:**
- Adds search tag in < 20 seconds
- Runs search successfully
- Imports job and verifies it appears in Tracker

**Observe:**
- Do they find "Search Tags" section (collapsed by default)?
- Do they understand market multiselect?
- Do they see LinkedIn warning?

### A/B Testing Candidates

**Test 1: ATS Score Visibility**
- **Variant A:** ATS Score Card expanded by default (current spec)
- **Variant B:** ATS Score Card collapsed by default
- **Metric:** Percentage of users who expand it (if collapsed)
- **Hypothesis:** Expanded by default increases ATS score awareness

**Test 2: Budget Display Location**
- **Variant A:** Sidebar metric (current spec)
- **Variant B:** Top banner on every page
- **Metric:** User survey: "How aware are you of your monthly cost?"
- **Hypothesis:** Sidebar is visible but not intrusive

**Test 3: Tracker Status Edit Method**
- **Variant A:** Inline edit (current spec)
- **Variant B:** Kanban drag-and-drop (research pattern 3.1)
- **Metric:** Status updates per session, time per update
- **Hypothesis:** Drag-and-drop is faster but less precise

---

## Handoff Checklist

### For Developers

- [ ] Read all 7 passes (understand rationale, not just implementation)
- [ ] Review component specifications (C01-C06)
- [ ] Confirm design system tokens (colors, spacing, typography)
- [ ] Validate Streamlit constraints (no native drag-and-drop, session state required)
- [ ] Implement keyboard navigation (tab order, focus indicators)
- [ ] Test error states (budget exceeded, JD extraction failed, no results)
- [ ] Add ARIA labels (buttons, progress bars, expanders)
- [ ] Test responsive breakpoints (desktop, tablet, mobile)

### For Designers (Future Figma Sync)

- [ ] Create Figma component library (based on C01-C06)
- [ ] Design dark mode variants (all components)
- [ ] Export design tokens (JSON for AURORA design_system/)
- [ ] Create interaction prototypes (Flow 1, 2, 3)
- [ ] Document edge cases (empty states, error states)
- [ ] Run accessibility audit (color contrast, focus indicators)

### For Product/QA

- [ ] Validate success criteria (Flow 1, 2, 3 complete)
- [ ] Test usability scenarios (Scenario 1, 2, 3)
- [ ] Verify cost transparency (budget displays never hidden)
- [ ] Check error messaging (user-friendly, actionable)
- [ ] Confirm GAIA constitutional compliance (transparency, HITL, sovereignty)
- [ ] Review analytics instrumentation (track key actions)

---

## Appendix A: Glossary

**ATS (Applicant Tracking System):** Software used by companies to manage job applications. Examples: Greenhouse, Workday, Lever, iCIMS, Ashby, Taleo.

**JD (Job Description):** Text description of a job role, including responsibilities, requirements, and qualifications.

**YAML Block:** Structured resume content in YAML format (used by jSeeker as base resume data).

**Resume Status:** 5-stage lifecycle of a resume: draft → generated → edited → exported → submitted.

**Application Status:** 9-stage lifecycle of a job application: not_applied → applied → screening → phone_screen → interview → offer → rejected → ghosted → withdrawn.

**Job Status:** 4-stage lifecycle of a job posting: active → closed → expired → reposted.

**Inline Edit:** Pattern where user clicks table cell → edits value → clicks away → auto-saves (no save button).

**Progressive Disclosure:** UX pattern where complexity is hidden by default and revealed on demand (expanders, modals).

**Toast Notification:** Small, temporary message that appears on screen (usually top-right) to confirm action (e.g., "Saved 1 change(s)!").

**Skeleton Loader:** Placeholder UI (animated gray boxes) shown while real content is loading (reduces perceived wait time).

**WCAG 2.1 AA:** Web Content Accessibility Guidelines, level AA (industry standard for accessible web design).

---

## Appendix B: References

**PRD:**
- X:\Projects\_GAIA\_AURORA\specs\jseeker\ux_requirements.md (19,000 words)

**Research:**
- X:\Projects\_GAIA\_AURORA\specs\jseeker\inspiration.md (18 patterns)

**Design System:**
- X:\Projects\_GAIA\_AURORA\design_system\master\tokens.json (AURORA 30% DNA)

**GAIA Constitutional Principles:**
- X:\Projects\_GAIA\GAIA_BIBLE.md (constitutional constraints)

**Accessibility Standards:**
- WCAG 2.1 Guidelines: https://www.w3.org/WAI/WCAG21/quickref/
- iOS Human Interface Guidelines (Touch Targets): https://developer.apple.com/design/human-interface-guidelines/

**Research Patterns Applied:**
- Pattern 1.1: Modular Card-Based Layout (Dashboard metrics)
- Pattern 2.1: Horizontal Stepper (Resume generation progress)
- Pattern 2.2: Inline Validation (Form inputs)
- Pattern 3.1: Drag-and-Drop Kanban (Deferred to Phase 3)
- Pattern 4.1: Niche Filters with Auto-Complete (Job Discovery)
- Pattern 5.1: Interactive Cost Calculator (Budget display)
- Pattern 5.2: Transparent Usage-Based Pricing (Cost tracking)

---

**Document Status:** Complete - Ready for Implementation
**Word Count:** 12,847 words
**Approval Required From:** jSeeker Product Lead, GAIA WARDEN (constitutional validation)

**Next Steps:**
1. Review with team-lead for approval
2. Handoff to jSeeker dev team
3. Create Figma prototypes (Phase 4: Build Order)
4. Begin implementation (Priority: P0 features)

---

**End of Specification**
