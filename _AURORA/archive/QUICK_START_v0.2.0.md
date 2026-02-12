# AURORA v0.2.0 — Quick Start Guide

**3 new ways to work with AURORA**

---

## 1. Extract Style from Successful Site (5 minutes)

**When**: You see a website with great UX and want to learn from it

**Command**:
```bash
/aurora-extract-style https://linear.app
```

**What happens:**
1. AURORA analyzes the site using WebFetch
2. Extracts design tokens (colors, typography, spacing, borders, shadows)
3. Documents interaction patterns (navigation, buttons, forms, feedback)
4. Saves analysis to `creative_direction/extracted_styles/linear/`

**Output files:**
- `analysis.md` — Full visual + interaction analysis
- `tokens.json` — Design tokens ready for import
- `observations.md` — Creative insights (why it works, what to borrow)

**Next step:** Use extracted tokens in mood board or brand kit

---

## 2. Generate Mood Board for Project (15 minutes)

**When**: Starting UX work on a project and need creative direction

**Command**:
```bash
/aurora-mood jseeker
```

**What happens:**
1. AURORA reads PRD and project context
2. Generates creative brief (personality, audience, constraints, success criteria)
3. **Checkpoint 1**: You approve creative brief
4. AURORA proposes 5-7 visual references with patterns to borrow
5. **Checkpoint 2**: You approve references (or suggest alternatives)
6. AURORA generates mood board with style direction + design tokens
7. **Checkpoint 3**: You approve mood board

**Output files:**
- `creative_direction/mood_boards/{project}/creative_brief.md`
- `creative_direction/mood_boards/{project}/mood_board.md`
- `creative_direction/mood_boards/{project}/references.json`

**Next step:** `/aurora-spec {project}` (UX Specification informed by mood board)

---

## 3. Quick Design Task (< 5 minutes)

**When**: Need a single component or quick UI fix

**Command**:
```bash
/aurora-quick "Design a loading spinner for ARGUS dashboard"
```

**What happens:**
1. AURORA checks ARGUS brand kit for tokens
2. Checks existing patterns for similar components
3. Designs component following AURORA principles
4. Provides copy-paste ready code (HTML/CSS/Streamlit/React)
5. Documents rationale + accessibility notes

**Output:** Instant response with code + rationale (no files created)

**When to use:**
- ✅ Single component (button, card, empty state, loading state)
- ✅ Quick fix (spacing, color, alignment)
- ✅ Small enhancement (add icon, improve copy)

**When NOT to use:**
- ❌ New feature (use full 6-phase workflow)
- ❌ Multiple components (use full workflow)
- ❌ System-wide change (use `/aurora-mood` + full workflow)

---

## Full Workflow with Creative Direction

```
/aurora-intake project-name
    ↓
/aurora-mood project-name        ← NEW: Creative brief + mood board
    ↓
/aurora-spec project-name        ← Informed by mood board
    ↓
/aurora-build project-name
    ↓
/aurora-refine project-name
    ↓
Deploy
```

---

## Example Session: jSeeker

```bash
# Step 1: Extract reference styles (build library)
/aurora-extract-style https://linear.app
/aurora-extract-style https://notion.so
/aurora-extract-style https://stripe.com/docs

# Step 2: Generate mood board
/aurora-mood jseeker
# → AURORA generates creative brief
# → User approves: "Professional, fast, transparent, data-driven, trustworthy"
# → AURORA proposes 5 references (Linear, Notion, Stripe, Vercel, Airtable)
# → User approves
# → AURORA generates mood board with tokens
# → User approves

# Step 3: Create UX spec (informed by mood board)
/aurora-spec jseeker

# Step 4: Quick task during development
/aurora-quick "Design empty state for job results table"
# → AURORA uses jSeeker brand tokens
# → Provides code + rationale
# → < 5 minutes
```

---

## Tips

### Building a Style Library
Extract 5-10 sites in your product category:
```bash
/aurora-extract-style https://linear.app        # Developer tools
/aurora-extract-style https://notion.so         # Productivity
/aurora-extract-style https://stripe.com/docs   # SaaS
/aurora-extract-style https://vercel.com        # Modern web
/aurora-extract-style https://ui.shadcn.com     # Components
```

### Creative Brief Shortcuts
If PRD is unclear, manually provide:
- 5 adjectives for brand personality
- Target audience description
- Technical constraints (framework, performance, devices)
- Success criteria (3 measurable outcomes)

### Quick Task Examples
```bash
/aurora-quick "Design a success toast notification"
/aurora-quick "Create loading skeleton for data table"
/aurora-quick "Fix spacing in sidebar navigation"
/aurora-quick "Design empty state for search results"
/aurora-quick "Create error message for form validation"
```

---

## Troubleshooting

### "No PRD found"
→ Provide path: `/aurora-mood jseeker --prd="X:\path\to\PRD.md"`

### "Mood board too generic"
→ Provide specific references: "Use Linear, Notion, and Stripe Docs as references"

### "Quick task escalated to full workflow"
→ Task is too complex for quick workflow, follow AURORA's recommendation

### "Extracted style is incomplete"
→ Site might have dynamic content, try homepage or docs page instead

---

## What Changed from v0.1.0?

| v0.1.0 | v0.2.0 |
|--------|--------|
| Generic "find inspiration" | Systematic creative brief + mood board |
| No style extraction | `/aurora-extract-style` analyzes sites |
| Full workflow for all tasks | `/aurora-quick` for simple tasks |
| Implicit creative direction | Explicit creative rationale documented |

---

## Next Steps

1. **Extract 3-5 reference styles** in your product category
2. **Generate mood board** for current project
3. **Try quick task** for immediate need

---

**Questions?** Check `AURORA_v0.2.0_SUMMARY.md` for full details.
