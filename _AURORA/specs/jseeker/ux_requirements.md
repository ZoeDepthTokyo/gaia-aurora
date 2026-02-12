# jSeeker UX Requirements Document
**Version:** 1.0
**Date:** 2026-02-10
**Product:** jSeeker (formerly PROTEUS) - The Shape-Shifting Resume Engine
**Product Version:** v0.2.1
**GAIA Ecosystem Component**

---

## Executive Summary

jSeeker is a specialized AI-powered resume adaptation tool that helps job seekers generate ATS-optimized, platform-aware resumes tailored to specific job descriptions. The system operates on a constitutional constraint: **never invent or hallucinate experience** — it only adapts real content from structured YAML resume blocks. The UX must balance automation (one-click generation) with transparency (cost tracking, ATS scoring, multi-format export) while serving users actively applying to multiple jobs across different markets and platforms.

---

## Target Users

### Primary Persona: "The Active Job Seeker"
- **Context:** Applying to 10-50+ jobs simultaneously across multiple ATS platforms (Greenhouse, Workday, Lever, iCIMS, Ashby, Taleo)
- **Pain Points:**
  - Manually tweaking resumes for each job is time-consuming
  - ATS systems parse resumes differently; hard to know what works
  - Tracking applications across multiple companies is messy
  - Cost anxiety when using AI tools (wants transparency)
  - Need to export in both PDF and DOCX formats depending on platform
- **Goals:**
  - Generate tailored resumes quickly (< 2 minutes per job)
  - Understand ATS compliance before submitting
  - Track application pipeline (resume status, application status, job status)
  - Monitor job postings to know if they close/expire
  - Discover new job opportunities matching their profile
- **Technical Comfort:** Comfortable with web apps; not developers
- **Languages/Markets:** Primarily English (US market), but system supports Spanish and 7 markets (US, MX, CA, UK, ES, DK, FR)

### Secondary Persona: "The Cost-Conscious Power User"
- **Context:** Using jSeeker heavily during job search sprints
- **Pain Points:**
  - AI costs add up quickly ($0.50-$2.00 per resume generation)
  - Need to stay within monthly budget ($50-100/month typical)
  - Want to see exactly where money is going
- **Goals:**
  - Transparent cost tracking (per-resume, per-session, monthly)
  - Budget alerts before exceeding limits
  - Ability to batch-process URLs when budget allows

---

## Core Product Principles (Constitutional Constraints)

1. **Never Hallucinate Experience** — All resume content comes from pre-loaded YAML blocks; AI only rewrites phrasing, never fabricates metrics or achievements
2. **Cost Transparency** — Every LLM call is tracked, logged, and displayed to user in real-time
3. **Platform-Aware ATS Scoring** — Different ATS systems have different parsing rules; scoring must reflect this
4. **User Edits Are Sacred** — System learns from user corrections but never overrides them
5. **Multi-Format Export** — Both PDF (visual) and DOCX (editable) formats must be available; recommendation varies by ATS platform

---

## Feature Inventory & Prioritization

### P0 Features (Core Value Prop — Must Have)

#### F01: One-Click Resume Generation
- **Description:** User pastes job description → system generates tailored resume → exports PDF + DOCX
- **User Flow:**
  1. Navigate to "New Resume" page
  2. Paste full JD text OR provide job URL (system extracts JD)
  3. Click "Generate Resume" button
  4. Wait 30-90 seconds (progress bar shows 5 steps: parse JD → match templates → adapt content → score ATS → render files)
  5. View results: ATS score card, export buttons, detailed analysis
- **UX-Critical Details:**
  - **Budget display** at top: Monthly cost vs. limit, session cost, remaining budget
  - **Budget enforcement:** If monthly limit exceeded, button is disabled with error message
  - **Progress indicator:** 5-stage progress bar with text labels ("Step 1/5: Parsing job description...")
  - **Cost transparency:** After generation, show exact cost of that resume (e.g., "$0.68")
- **Success Criteria:**
  - 90%+ of users can generate first resume without help/docs
  - Generation completes in < 2 minutes for typical JD
  - User understands why ATS score is X/100 (not a black box)

#### F02: ATS Score Card with Actionable Feedback
- **Description:** Platform-specific ATS compliance score with keyword analysis and format recommendation
- **User Flow:**
  1. After resume generation, user sees collapsible "ATS Score Card" section (expanded by default)
  2. View 3 key metrics: Overall Score (0-100), Keyword Match (%), Recommended Format (PDF/DOCX/Both)
  3. See missing keywords (if any) as warning banner
  4. Read format reason (e.g., "Greenhouse prefers DOCX for better parsing")
- **UX-Critical Details:**
  - **Visual hierarchy:** Overall score most prominent (large number with color: red <50, yellow 50-75, green >75)
  - **Platform context:** Display detected ATS platform (e.g., "Detected: Greenhouse")
  - **Keyword transparency:** Show first 10 missing keywords, not full list (avoid overwhelm)
  - **Warnings as badges:** Each warning shown as yellow pill/tag (e.g., "Tables may confuse parser")
- **Success Criteria:**
  - User can explain why their ATS score is low (not "the AI is bad")
  - Format recommendation is followed 80%+ of the time

#### F03: Multi-Format Export (PDF + DOCX)
- **Description:** Download resume in both PDF (for visual consistency) and DOCX (for ATS editability)
- **User Flow:**
  1. After generation, see "Export" section with two download buttons side-by-side
  2. Optionally customize filename (default: "Company_Role_YYYYMMDD")
  3. Click "Download PDF" or "Download DOCX"
- **UX-Critical Details:**
  - **Filename customization:** Single text input, applies to both files (adds `.pdf` or `.docx` extension)
  - **Button styling:** PDF button has document icon, DOCX button has edit icon
  - **Immediate download:** No page refresh, browser download dialog opens
- **Success Criteria:**
  - 100% of users can download at least one format
  - 60%+ download both formats

#### F04: Application Tracker (CRM)
- **Description:** Manage pipeline of job applications with 3 independent status dimensions
- **User Flow:**
  1. Navigate to "Tracker" page
  2. View table of all applications (newest first)
  3. Filter by Application Status, Resume Status, or Job Status (sidebar dropdowns)
  4. Edit any cell inline (click, change value, click away → auto-saves with toast notification)
  5. View clickable job URL, add notes, see ATS score, check creation date
- **UX-Critical Details:**
  - **Three status dimensions:**
    - **Resume Status:** draft → generated → edited → exported → submitted
    - **Application Status:** not_applied → applied → screening → phone_screen → interview → offer → rejected → ghosted → withdrawn
    - **Job Status:** active → closed → expired → reposted
  - **Inline editing:** Use data editor component with dropdowns for status fields, text for notes/location
  - **Column priorities:** Show ID, Company, Role, URL, Relevance %, ATS Score, all 3 statuses, Location, Created, Notes
  - **Filters cumulative:** Can filter by multiple statuses simultaneously (e.g., "exported" resumes that are "not_applied")
- **Success Criteria:**
  - User can find specific application in < 10 seconds
  - Status updates save within 2 seconds with confirmation

### P1 Features (Important — High Value)

#### F05: Dashboard (Overview + Quick Actions)
- **Description:** Landing page showing key metrics, recent applications, and quick action buttons
- **User Flow:**
  1. Launch jSeeker → Dashboard loads as home page
  2. See 5-metric summary row at top
  3. Browse "Recent Applications" list (last 10, collapsible)
  4. Use quick action buttons to navigate: "New Resume", "View Tracker", "Discover Jobs"
  5. Optionally use batch URL intake (paste multiple job URLs → generates resumes for all)
- **UX-Critical Details:**
  - **Metrics row:** 5 equal-width columns: Total Applications | Active Applications | This Week | Avg ATS Score | Monthly Cost
  - **Recent applications:** Each row shows Company - Role, Location, 3 status badges (Resume/App/Job)
  - **Batch intake:** Collapsible expander (default closed), textarea for URLs (one per line), "Generate Resumes For URLs" button
  - **Batch feedback:** Progress bar during generation, summary of successes/skips/failures
- **Success Criteria:**
  - User understands application velocity ("This Week" metric trending up/down)
  - Batch generation saves 5+ minutes when processing 5+ URLs

#### F06: Job Discovery (Tag-Based Search)
- **Description:** Search multiple job boards (Indeed, LinkedIn, Wellfound) using configurable tags across 7 markets
- **User Flow:**
  1. Navigate to "Job Discovery" page
  2. Manage search tags (add, toggle active/inactive)
  3. Select markets (US, MX, CA, UK, ES, DK, FR)
  4. Choose job boards (Indeed, LinkedIn, Wellfound)
  5. Optionally add location filter (e.g., "Remote", "San Francisco")
  6. Click "Search Now" → system searches all tag × board × market combinations
  7. View results grouped by market (collapsible expanders)
  8. Star, dismiss, or import jobs into tracker
- **UX-Critical Details:**
  - **Tag management:** List of tags with Active/Inactive badge + Toggle button; form to add new tag below
  - **Market multiselect:** Default [US, MX]; show full country names ("United States" not "us")
  - **Board multiselect:** Default [Indeed]; show warning if LinkedIn selected (anti-bot protections)
  - **Results grouping:** One expander per market (e.g., "United States (12 jobs)"), sorted by posting date descending
  - **Job actions:** 4-button row per job: Star | Dismiss | Import to Tracker | View Job (external link)
  - **Status filtering:** Dropdown to show All/New/Starred/Dismissed/Imported jobs
- **Success Criteria:**
  - User finds 10+ relevant jobs in < 5 minutes
  - 40%+ of discovered jobs get starred or imported

#### F07: Resume Library (Version Management)
- **Description:** Browse all generated resumes, download files, track base resume references
- **User Flow:**
  1. Navigate to "Resume Library" page
  2. View table of all resumes (ID, Company, Role, Version, ATS Score, Template, Cost, Created)
  3. Select a resume ID from dropdown
  4. Download PDF or DOCX
  5. Optionally delete resume (requires confirmation)
  6. Manage base resume references (A/B/C variants + LinkedIn PDF)
- **UX-Critical Details:**
  - **Base references section:** 4 text inputs for file paths (Base A, Base B, Base C, LinkedIn PDF), "Save" button, validation feedback
  - **Version tracking:** Each resume has version number (increments if same job/company regenerated)
  - **Delete workflow:** Click "Delete Resume" → confirmation prompt → "Confirm Delete" + "Cancel" buttons
  - **File validation:** After saving base references, show checkmark or X icon for each file (exists/missing)
- **Success Criteria:**
  - User can re-download resume from 2 weeks ago in < 30 seconds
  - Base resume references configured correctly 90%+ of time

### P2 Features (Nice-to-Have — Deferred or Experimental)

#### F08: Job Status Monitor (Automated Checking)
- **Description:** Periodically check if active job URLs return 404 or closure language; auto-update job status
- **User Flow:**
  1. Navigate to "Tracker" page → expand "Job Status Monitor" section
  2. See count of active jobs with URLs
  3. Click "Check All Active Job URLs"
  4. Wait for HTTP checks to complete
  5. View summary: X jobs updated, with old → new status changes
- **UX-Critical Details:**
  - **Manual trigger:** User initiates check (not automatic background job)
  - **Spinner feedback:** "Checking job URLs..." during HTTP requests
  - **Change log:** List each status change (Company - Role: active → closed)
- **Success Criteria:**
  - Reduces manual "is this job still open?" checking by 80%

#### F09: Batch URL Intake (Dashboard Feature)
- **Description:** Generate resumes for multiple job URLs in one batch operation
- **User Flow:**
  1. On Dashboard, expand "Batch Generate From Job URLs" section
  2. Paste URLs (one per line) into textarea
  3. Click "Generate Resumes For URLs"
  4. Watch progress bar (processes sequentially)
  5. View summary: X generated, Y skipped (duplicate), Z failed
- **UX-Critical Details:**
  - **Deduplication:** Skip URLs already in tracker (don't generate twice)
  - **Progress:** Show "Processing 3/10: [URL]" during generation
  - **Error handling:** Continue batch even if one URL fails; report failures at end
- **Success Criteria:**
  - Successfully processes 5 URLs without user intervention

#### F10: Search Tag Management (Discovery Feature)
- **Description:** Add, toggle, and view search tags for job discovery
- **User Flow:**
  1. On Job Discovery page, expand "Search Tags" section
  2. View list of tags (name + active status + toggle button)
  3. Add new tag via form (text input + submit button)
- **UX-Critical Details:**
  - **Toggle feedback:** Immediately update UI (no page reload)
  - **Duplicate prevention:** Show warning if tag already exists
- **Success Criteria:**
  - User can manage 10+ tags without confusion

---

## Detailed User Flows (Step-by-Step)

### Flow 1: First-Time User Generates Resume
**Goal:** User with no prior jSeeker experience successfully generates their first tailored resume

**Steps:**
1. User launches jSeeker → sees Dashboard landing page
2. User notices sidebar navigation: Dashboard, New Resume, Resume Library, Tracker, Job Discovery
3. User clicks "New Resume" in sidebar (or quick action button on Dashboard)
4. **New Resume page loads:**
   - **Budget display at top:** "Monthly Cost: $0.00 of $50.00" (example), "Session Cost: $0.000", "Budget Remaining: $50.00"
   - **Heading:** "Job Description"
   - **Large textarea:** "Paste the full job description here:" (300px height)
   - **URL input below:** "Job URL (optional - helps detect ATS platform):"
   - **Caption:** "Paste JD text, or provide only a job URL and jSeeker will try to extract the JD."
5. User pastes job description from company careers page (500-2000 words typical)
6. User optionally pastes job URL (e.g., https://boards.greenhouse.io/company/jobs/12345)
7. User clicks **"Generate Resume"** button (primary/blue, full-width, type=primary)
8. **Generation progress:**
   - Status component expands with progress bar
   - Text updates: "Step 1/5: Parsing job description..." → "Step 2/5: Matching resume templates..." → etc.
   - Progress bar fills: 0% → 20% → 40% → 60% → 80% → 95% → 100%
   - Total time: 30-90 seconds depending on JD complexity
9. **Results display:**
   - Status collapses with green checkmark: "Resume generated successfully."
   - Success message: "Resume generated for [Company] - [Role] (Application #123)"
   - **Three collapsible sections appear:**
     - **ATS Score Card** (expanded by default)
     - **Export** (expanded by default)
     - **JD Analysis** (collapsed)
     - **Template Match** (collapsed)
     - **Adaptation Details** (collapsed)
10. User views ATS Score Card:
    - Overall Score: 78/100 (displayed large, green text)
    - Keyword Match: 85%
    - Recommended Format: DOCX
    - Missing keywords: "machine learning, TensorFlow, PyTorch" (yellow warning banner)
    - Format Reason: "Greenhouse prefers DOCX for better parsing of complex layouts"
11. User views Export section:
    - Default filename shown: "Acme_ProductDesigner_20260210"
    - Two buttons side-by-side: "Download PDF" | "Download DOCX"
    - User edits filename to "Acme_Senior_Designer_Final"
    - User clicks "Download DOCX" (based on ATS recommendation)
    - Browser download starts immediately
12. **Cost feedback at bottom:**
    - Caption: "Cost: $0.6800"
    - User sees session cost updated in sidebar: "$0.680"
13. User downloads PDF as well (for personal records)
14. **Success:** User has generated tailored resume, understands ATS compliance, and exported in correct format — all in < 3 minutes

**Edge Cases:**
- **Budget exceeded:** If monthly cost >= limit, button disabled with error: "Monthly budget exceeded ($52.34 / $50.00). Generation disabled."
- **JD extraction fails:** If URL provided but no text extracted, error: "Could not extract job description from URL. Paste the JD text and try again."
- **No template matches:** If JD parser fails to extract keywords, error with diagnostic: "No template matches found. JD Title: [X], Keywords found: [Y]. Try pasting a more complete job description."

---

### Flow 2: Power User Manages Application Pipeline
**Goal:** User with 20+ applications tracks status changes and filters by pipeline stage

**Steps:**
1. User launches jSeeker → clicks "Tracker" in sidebar
2. **Tracker page loads:**
   - Sidebar shows 3 filter dropdowns (default: All)
   - Main area shows inline-editable table with all applications
3. User sees 24 applications in table (newest first)
4. User wants to see only applications with "exported" resumes that haven't been submitted yet
5. User clicks sidebar filter "Resume Status" → selects "exported"
6. User clicks sidebar filter "Application Status" → selects "not_applied"
7. Table updates to show 8 matching applications (caption: "Showing 8 applications")
8. User submitted resume for "Acme Inc - Product Designer" yesterday
9. User clicks Application Status cell for that row → dropdown opens
10. User selects "applied" from dropdown
11. User clicks away → toast notification: "Saved 1 change(s)!"
12. Table updates with new status badge (color changes)
13. User adds note to another application: "Follow up next week"
14. User clicks Notes cell → types note → clicks away → toast: "Saved 1 change(s)!"
15. User wants to see all applications again
16. User resets filters: Resume Status = All, Application Status = All
17. Table shows all 24 applications again
18. **Success:** User has organized pipeline, updated statuses, and added reminders — all without leaving one page

**Edge Cases:**
- **No matching filters:** If filters return 0 results, show: "No applications match your filters."
- **Status transition logic:** System doesn't enforce order (user can jump from "draft" to "submitted" directly — trust user)

---

### Flow 3: User Discovers and Imports Jobs
**Goal:** User configures search tags, runs multi-market search, and imports promising job to tracker

**Steps:**
1. User launches jSeeker → clicks "Job Discovery" in sidebar
2. **Job Discovery page loads:**
   - "Search Tags" section (collapsed)
   - "Markets" section
   - "Search Jobs" section
   - "Discovered Jobs" section (empty on first visit)
3. User expands "Search Tags" section
4. User sees message: "No search tags configured. Add some below."
5. User types "Director of Product Design" in "New search tag" input
6. User clicks "Add Tag" → success: "Added tag: Director of Product Design"
7. Tag appears in list with "Active" badge and "Toggle" button
8. User adds 2 more tags: "Senior UX Designer", "Head of Design"
9. User closes "Search Tags" section
10. **Markets section:**
    - Multiselect shows default [United States, Mexico]
    - User keeps both selected
11. **Search Jobs section:**
    - Location filter: User types "Remote"
    - Job boards: User selects [Indeed, LinkedIn]
    - Warning appears: "LinkedIn may return limited results due to anti-bot protections. Indeed usually returns more consistent results."
12. User clicks "Search Now"
13. **Search executes:**
    - Spinner: "Searching 3 tag(s) across 2 board(s) in 2 market(s)..."
    - System makes 3 × 2 × 2 = 12 search combinations
    - Takes 30-60 seconds (web scraping varies)
14. **Search completes:**
    - Success message: "Found 37 jobs, 34 new (deduplicated)"
    - "Search Details" expander shows diagnostic info
15. **Discovered Jobs section populates:**
    - Two market expanders: "United States (28 jobs)", "Mexico (6 jobs)"
    - United States expander is expanded by default
16. User browses results:
    - Each job shows: Title, Company, Location, Posting Date, Source, Status
    - Action buttons: Star | Dismiss | Import to Tracker | View Job
17. User sees "Director of Product Design - Acme Corp" (remote, posted 2 days ago)
18. User clicks "Star" → job status changes to "starred" (button disappears)
19. User sees another promising job: "Senior Product Designer - Beta Inc"
20. User clicks "Import to Tracker" → success toast: "Imported as application #125"
21. User clicks "View Tracker" button in sidebar
22. **Tracker page loads with new application visible:**
    - Beta Inc - Senior Product Designer (row added)
    - Resume Status: draft (not generated yet)
    - Application Status: not_applied
    - Job Status: active
23. **Success:** User has discovered new opportunities, organized them, and added one to active pipeline — ready to generate resume

**Edge Cases:**
- **No active tags:** If user clicks "Search Now" with no active tags, error: "No active search tags. Add and activate tags first."
- **No markets selected:** If user deselects all markets, error: "Select at least one market to search."
- **Zero results:** If search returns no jobs, info: "No discovered jobs match your current filters. Run a search above."

---

## Success Criteria (Measurable)

### User Onboarding
- **First Resume Generated:** 90% of new users generate their first resume within 10 minutes
- **Error Rate:** < 5% of first-time generations result in errors requiring support

### Core Workflow Efficiency
- **Resume Generation Speed:** 95% of generations complete in < 2 minutes
- **Export Rate:** 80% of generated resumes are downloaded (at least one format)
- **ATS Score Understanding:** User can explain why their score is X/100 (qualitative feedback)

### Cost Transparency
- **Budget Awareness:** 100% of users can see monthly cost at all times (persistent sidebar)
- **Budget Compliance:** < 1% of users exceed monthly limit without warning

### Application Management
- **Tracker Adoption:** 70% of users access Tracker within first 5 resumes generated
- **Status Update Frequency:** Users update application status within 24 hours of real-world status change (70% of cases)

### Job Discovery
- **Discovery Activation:** 40% of users configure search tags within first week
- **Import Rate:** 50% of starred jobs are imported to Tracker

---

## UX-Critical vs Backend-Only Features

### UX-Critical Features (AURORA Must Design)
- F01: One-Click Resume Generation (progress feedback, cost display, error states)
- F02: ATS Score Card (visual hierarchy, color coding, keyword transparency)
- F03: Multi-Format Export (filename customization, button styling)
- F04: Application Tracker (inline editing, filter UI, status badges)
- F05: Dashboard (metrics layout, quick actions, batch intake UI)
- F06: Job Discovery (tag management, market selection, result grouping)
- F07: Resume Library (version browsing, file validation feedback)

### Backend-Only Features (AURORA Can Ignore)
- JD parsing logic (Claude API calls, keyword extraction)
- Resume adaptation algorithm (prompt engineering, content rewriting)
- ATS scoring rules (platform-specific logic)
- PDF/DOCX rendering (Playwright, python-docx)
- SQLite database schema
- Web scraping parsers (Indeed, LinkedIn, Wellfound)

---

## Mobile vs Desktop Considerations

### Current State: Desktop-First
jSeeker is built with Streamlit, which is **desktop-optimized**. Mobile experience is **not prioritized** in v0.2.1.

### Desktop (Primary)
- **Screen width:** Optimized for 1280px+ (standard laptop/desktop)
- **Layout:** Sidebar navigation + main content area
- **Interaction:** Mouse/keyboard (click, hover, type)

### Mobile (Future Consideration)
- **Current experience:** Usable but not optimal (Streamlit responsive but cramped on phone)
- **Pain points:**
  - Sidebar collapses to hamburger menu (extra tap)
  - Long textareas hard to edit on phone
  - Data tables require horizontal scrolling
- **Recommendation for AURORA:** Design for desktop first; ensure minimum 768px tablet support; defer mobile-specific UX to Phase 2

---

## Cost Transparency Requirements (Critical to UX)

### Why It Matters
Users are paying $0.50-$2.00 per resume generation via Claude API. Without transparency, users feel anxious and may abandon tool.

### Required Cost Displays

#### 1. Persistent Sidebar Cost (Always Visible)
- **Location:** Sidebar below "JSEEKER" title
- **Format:** Metric card: "Session Cost: $X.XXX"
- **Updates:** Real-time after each generation

#### 2. Budget Display (New Resume Page)
- **Location:** Top of page, above JD input
- **Format:** 3-metric row:
  - Monthly Cost: $X.XX of $Y.YY
  - Session Cost: $X.XXX
  - Budget Remaining: $X.XX
- **Color coding:**
  - Green: < 80% of budget
  - Yellow: 80-100% of budget (warning)
  - Red: > 100% of budget (generation disabled)

#### 3. Per-Resume Cost (After Generation)
- **Location:** Bottom of results section
- **Format:** Caption: "Cost: $X.XXXX"
- **Explanation:** User understands this specific resume cost them $X

#### 4. Dashboard Monthly Cost Metric
- **Location:** Dashboard metrics row (rightmost metric)
- **Format:** "Monthly Cost: $X.XX"
- **Trend:** Show if approaching limit (yellow/red background)

#### 5. Resume Library Cost Column
- **Location:** Resume table
- **Format:** "Cost ($)" column with 4 decimal places
- **Aggregate:** User can mentally sum costs across resumes

### Budget Enforcement UX
- **Warning threshold:** When monthly cost >= 80% of limit, show yellow banner on New Resume page
- **Hard limit:** When monthly cost >= 100% of limit:
  - Disable "Generate Resume" button
  - Show red error: "Monthly budget exceeded ($X.XX / $Y.YY). Generation disabled."
  - Suggest: "Budget resets on [date] or contact admin to increase limit."
- **Exception:** User can still download/browse existing resumes (no LLM calls)

---

## Platform-Specific Considerations

### ATS Platforms Supported
jSeeker detects and optimizes for 6 ATS platforms:
1. **Greenhouse** (most common) — Prefers DOCX, strict keyword matching
2. **Workday** — Prefers PDF, handles tables well
3. **Lever** — Neutral, both formats work
4. **iCIMS** — Prefers DOCX, struggles with complex formatting
5. **Ashby** (startup-friendly) — Prefers PDF, modern parser
6. **Taleo** (enterprise) — Prefers DOCX, conservative parser

### UX Implications
- **Format recommendation must be visible:** Don't bury in collapsed section
- **Platform name displayed:** User needs to know "this is a Greenhouse job" for context
- **Keyword list prioritized:** If Greenhouse detected, keyword match becomes more critical (show missing keywords prominently)

---

## Internationalization (i18n) Notes

### Languages Supported
- **English (en):** Default, fully supported
- **Spanish (es):** JD parsing, resume generation, UI labels (future)

### Markets Supported
- **us:** United States (default)
- **mx:** Mexico
- **ca:** Canada
- **uk:** United Kingdom
- **es:** Spain
- **dk:** Denmark
- **fr:** France

### UX Implications for AURORA
- **Language detection:** Automatic based on JD text (no user selection needed)
- **Market selection:** User explicitly chooses markets in Job Discovery (multiselect)
- **Resume language:** Matches detected JD language (if JD is Spanish, resume is Spanish)
- **UI labels:** Currently English-only; Spanish translation is Phase 2 roadmap item

---

## Technical Constraints Impacting UX

### 1. Streamlit Framework
- **Single-page app with sidebar navigation:** Cannot use browser back button effectively (design with this in mind)
- **No native mobile components:** Limited gesture support
- **Session state required:** Cross-page data sharing uses `st.session_state` (user cannot refresh without losing context)

### 2. LLM Cost/Latency
- **Generation takes 30-90 seconds:** Must use progress feedback (not instant)
- **Cost per resume:** $0.50-$2.00 depending on JD length → budget transparency is mandatory

### 3. Web Scraping Fragility
- **Job Discovery parsers break:** If Indeed/LinkedIn change markup, results may be empty
- **UX mitigation:** Always show "Search Details" expander with diagnostic info so user knows search ran but found nothing

### 4. File System Dependencies
- **Resume files stored locally:** PDF/DOCX paths are file system paths, not cloud URLs
- **Base resume references:** User must provide correct file paths (validation needed)

---

## Error States & Edge Cases

### Common Error Scenarios AURORA Must Design For

#### 1. Budget Exceeded
- **Trigger:** Monthly cost >= max_monthly_budget_usd
- **UI State:**
  - "Generate Resume" button disabled (grayed out)
  - Red error banner: "Monthly budget exceeded ($X.XX / $Y.YY). Generation disabled."
  - Suggestion: "Budget resets on [date]."
- **Allowed actions:** User can still browse library, tracker, discoveries

#### 2. JD Extraction Failed
- **Trigger:** User provides URL but extraction returns empty string
- **UI State:**
  - Red error message: "Could not extract job description from URL. Paste the JD text and try again."
  - Textarea remains visible (fallback to manual paste)

#### 3. No Template Matches
- **Trigger:** JD parser extracts < 5 keywords (insufficient data)
- **UI State:**
  - Red error with diagnostic:
    ```
    No template matches found.
    JD Title: [X]
    Keywords found: [Y]
    This usually means the JD parser couldn't extract keywords.
    Try pasting a more complete job description.
    ```

#### 4. Zero Search Results (Job Discovery)
- **Trigger:** Search runs but all parsers return empty (site markup changed)
- **UI State:**
  - Success message: "Found 0 jobs, 0 new"
  - Info banner: "No discovered jobs match your current filters. Run a search above."
  - "Search Details" expander shows diagnostic (e.g., "12 search combinations, 0 results")

#### 5. File Not Found (Resume Library)
- **Trigger:** PDF/DOCX path in database points to deleted file
- **UI State:**
  - Download button disabled (grayed out)
  - Caption: "File not found at [path]"

---

## Interaction Design Principles

### 1. Progressive Disclosure
- **Default collapsed:** JD Analysis, Template Match, Adaptation Details (user expands if curious)
- **Default expanded:** ATS Score Card, Export (core actions)

### 2. Inline Editing with Confirmation
- **Pattern:** Click cell → edit → click away → auto-save → toast notification
- **No save buttons:** Reduces friction, faster editing

### 3. Status as Color + Text
- **Resume Status:** draft (gray) → generated (blue) → edited (yellow) → exported (green) → submitted (purple)
- **Application Status:** not_applied (gray) → applied (blue) → screening (yellow) → interview (orange) → offer (green) → rejected (red)
- **Job Status:** active (green) → closed (gray) → expired (red)

### 4. Cost Visibility Without Nagging
- **Always visible but not intrusive:** Sidebar metric is persistent but small
- **Contextual warnings:** Only show budget alert when > 80% used
- **Celebrate low cost:** If resume generates for < $0.50, show green checkmark (positive reinforcement)

---

## Accessibility Considerations

### Minimum Requirements (Future Phase)
- **Color contrast:** All text must meet WCAG AA (4.5:1 ratio)
- **Keyboard navigation:** Tab order logical, all actions keyboard-accessible
- **Screen reader labels:** All buttons/inputs have aria-labels
- **Focus indicators:** Visible outline on focused elements

### Current State (v0.2.1)
- **Streamlit default accessibility:** Basic support but not fully WCAG compliant
- **AURORA recommendation:** Flag accessibility gaps for Phase 2 improvements

---

## Appendix: Data Model Summary (For UX Context)

### Key Entities

#### Application
- **Fields:** id, company_name, role_title, jd_text, jd_url, location, remote_policy, salary_range, relevance_score, resume_status, application_status, job_status, applied_date, notes
- **Relationships:** belongs_to Company, has_many Resumes

#### Resume
- **Fields:** id, application_id, version, template_used, pdf_path, docx_path, ats_score, ats_platform, generation_cost, user_edited, created_at
- **Relationships:** belongs_to Application

#### JobDiscovery
- **Fields:** id, title, company, location, salary_range, url, source, posting_date, market, status (new/starred/dismissed/imported), discovered_at
- **Relationships:** can_be_imported_to Application

#### SearchTag
- **Fields:** id, tag, active, created_at
- **Relationships:** none (simple lookup table)

### Status Enums (3 Independent Dimensions)
1. **ResumeStatus:** draft | generated | edited | exported | submitted
2. **ApplicationStatus:** not_applied | applied | screening | phone_screen | interview | offer | rejected | ghosted | withdrawn
3. **JobStatus:** active | closed | expired | reposted

---

## Summary: What AURORA Needs to Design

### Pages (5)
1. **Dashboard** — Metrics + Recent Apps + Quick Actions + Batch Intake
2. **New Resume** — JD Input + Budget Display + Generate Button + Results (ATS Card + Export + Expanders)
3. **Resume Library** — Base References + Resume Table + Download/Delete
4. **Tracker** — Filters (sidebar) + Inline-Editable Table + Import/Export + Job Monitor
5. **Job Discovery** — Tag Management + Market Selection + Search + Results (grouped by market)

### Components (Reusable)
- **Metric Card** (3-column layout for costs)
- **Status Badge** (color-coded pills for Resume/App/Job status)
- **Progress Bar with Text** (5-stage resume generation)
- **Inline Data Editor** (Tracker + Resume Library tables)
- **Collapsible Expander** (used everywhere for progressive disclosure)
- **Action Button Row** (Star | Dismiss | Import | View — Job Discovery)
- **Cost Display** (sidebar metric + per-resume caption)

### Flows to Prototype
1. **First-time user generates resume** (onboarding critical)
2. **Power user filters and updates tracker** (productivity critical)
3. **User discovers and imports job** (discoverability critical)

---

## Next Steps for AURORA

1. **Wireframe each page** using component library above
2. **Prototype critical flows** (Flow 1, 2, 3) in design tool (Figma, etc.)
3. **Validate cost transparency** — ensure budget displays never hidden/buried
4. **Design error states** for each failure mode (budget exceeded, extraction failed, no results)
5. **Confirm accessibility** — keyboard nav, color contrast, screen reader labels
6. **Document design system** — colors, typography, spacing for Streamlit constraints
7. **Handoff to dev** with annotated mockups + interaction specs

---

**End of Document**
