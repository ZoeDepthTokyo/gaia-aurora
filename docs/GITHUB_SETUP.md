# GAIA GitHub Organization Setup Guide

**Version:** 1.0.0
**Date:** February 8, 2026
**Status:** Reference Documentation

---

## Organization Structure

### Recommended Organization Name
`gaia-ecosystem` (or your preferred GitHub org name)

### Repository Naming Convention

| Type | Prefix | Example |
|------|--------|---------|
| Shared Service | `gaia-` | `gaia-mycel`, `gaia-argus`, `gaia-warden` |
| Product | (none) | `jseeker`, `hart-os`, `data-forge` |
| Governance | `gaia-` | `gaia-core` |
| Tools | `gaia-` | `gaia-python-tools` |

### Full Repository List

**Shared Services (8 repos):**
| Repository | Description | Status |
|------------|-------------|--------|
| `gaia-argus` | Monitoring, mental models, telemetry | Active |
| `gaia-loom` | Workflow engine, agent orchestration | Active |
| `gaia-mnemis` | Cross-project memory, pattern storage | Active |
| `gaia-mycel` | Unified LLM intelligence, RAG | Active |
| `gaia-raven` | Autonomous research agent | Planning |
| `gaia-vulcan` | Project creator, The Forge | Active |
| `gaia-warden` | Governance, compliance, validation | Active |
| `gaia-abis` | Visual system builder, node editor | Planning |

**Products (8 repos):**
| Repository | Description | Status |
|------------|-------------|--------|
| `hart-os` | Therapy scoring system | Complete |
| `via-intel` | Investment research | Paused |
| `data-forge` | Data processing pipeline | Blocked |
| `jseeker` | Resume adaptation engine | Active |
| `dos` | Decision orchestration system | Planning |
| `gpt-echo` | ChatGPT archaeology and search | Stale |
| `the-palace` | Case study (archived) | Archived |
| `waymo-data` | AV data analysis (archived) | Archived |

**Governance (1 repo):**
| Repository | Description | Status |
|------------|-------------|--------|
| `gaia-core` | Bible, PRD, registry, architecture docs | Active |

---

## Setup Steps

### Step 1: Create GitHub Organization

1. Go to https://github.com/organizations/plan
2. Choose Free plan (sufficient for solo developer)
3. Organization name: `gaia-ecosystem`
4. Contact email: your email
5. This organization belongs to: My personal account

### Step 2: Create Repositories

Using `gh` CLI (install: https://cli.github.com/):

```bash
# Authenticate
gh auth login

# Create shared service repos
gh repo create gaia-ecosystem/gaia-argus --public --description "ARGUS - Monitoring, mental models, and telemetry for GAIA ecosystem"
gh repo create gaia-ecosystem/gaia-loom --public --description "LOOM - Workflow engine and agent orchestration"
gh repo create gaia-ecosystem/gaia-mnemis --public --description "MNEMIS - Cross-project memory and pattern storage"
gh repo create gaia-ecosystem/gaia-mycel --public --description "MYCEL - Unified LLM intelligence layer with RAG"
gh repo create gaia-ecosystem/gaia-raven --public --description "RAVEN - Autonomous research agent"
gh repo create gaia-ecosystem/gaia-vulcan --public --description "VULCAN - Project creator and The Forge"
gh repo create gaia-ecosystem/gaia-warden --public --description "WARDEN - Governance and compliance validation"
gh repo create gaia-ecosystem/gaia-abis --public --description "ABIS - Visual system builder and node editor"

# Create product repos
gh repo create gaia-ecosystem/hart-os --public --description "HART OS - Therapy scoring system"
gh repo create gaia-ecosystem/via-intel --public --description "VIA - Investment research intelligence"
gh repo create gaia-ecosystem/data-forge --public --description "DATA FORGE - Data processing pipeline"
gh repo create gaia-ecosystem/jseeker --public --description "jSeeker - Resume adaptation engine"
gh repo create gaia-ecosystem/dos --public --description "DOS - Decision orchestration system"
gh repo create gaia-ecosystem/gpt-echo --public --description "GPT_ECHO - ChatGPT archaeology and search"

# Create governance repo
gh repo create gaia-ecosystem/gaia-core --public --description "GAIA Core - Ecosystem governance, bible, PRD, registry"
```

### Step 3: Configure Git Remotes Locally

```bash
# For each project, add the GitHub remote:

# Shared Services
cd X:\Projects\_GAIA\_ARGUS && git remote add origin https://github.com/gaia-ecosystem/gaia-argus.git
cd X:\Projects\_GAIA\_LOOM && git remote add origin https://github.com/gaia-ecosystem/gaia-loom.git
cd X:\Projects\_GAIA\_MNEMIS && git remote add origin https://github.com/gaia-ecosystem/gaia-mnemis.git
cd X:\Projects\_GAIA\_MYCEL && git remote add origin https://github.com/gaia-ecosystem/gaia-mycel.git
cd X:\Projects\_GAIA\_RAVEN && git remote add origin https://github.com/gaia-ecosystem/gaia-raven.git
cd X:\Projects\_GAIA\_VULCAN && git remote add origin https://github.com/gaia-ecosystem/gaia-vulcan.git
cd X:\Projects\_GAIA\_WARDEN && git remote add origin https://github.com/gaia-ecosystem/gaia-warden.git
cd X:\Projects\_GAIA\_ABIS && git remote add origin https://github.com/gaia-ecosystem/gaia-abis.git

# Products
cd X:\Projects\hart_os_v6 && git remote add origin https://github.com/gaia-ecosystem/hart-os.git
cd X:\Projects\jSeeker && git remote add origin https://github.com/gaia-ecosystem/jseeker.git
cd X:\Projects\DOS && git remote add origin https://github.com/gaia-ecosystem/dos.git
cd X:\Projects\GPT_ECHO && git remote add origin https://github.com/gaia-ecosystem/gpt-echo.git

# Governance
cd X:\Projects\_GAIA && git remote add origin https://github.com/gaia-ecosystem/gaia-core.git
```

### Step 4: Configure Branch Protection

Apply to `main` branch on all active repos:

```bash
# For each repo:
gh api repos/gaia-ecosystem/REPO_NAME/branches/main/protection \
  --method PUT \
  --input - << 'EOF'
{
  "required_status_checks": {
    "strict": true,
    "contexts": ["test", "warden"]
  },
  "enforce_admins": false,
  "required_pull_request_reviews": null,
  "restrictions": null
}
EOF
```

### Step 5: Add Repository Secrets

```bash
# Add API keys as repository secrets (for CI/CD)
gh secret set OPENAI_API_KEY --repo gaia-ecosystem/gaia-mycel
gh secret set ANTHROPIC_API_KEY --repo gaia-ecosystem/gaia-mycel

# Repeat for other repos that need API keys
```

---

## Branch Protection Rules

| Rule | Setting | Reason |
|------|---------|--------|
| Require pull request | No (solo dev) | Too much friction for one person |
| Require status checks | Yes | Ensures CI/CD passes |
| Required checks | `test`, `warden` | Tests + governance validation |
| Enforce admins | No | Solo dev can bypass when needed |
| Allow force pushes | No | Prevent accidental history rewrite |
| Allow deletions | No | Prevent accidental branch deletion |

---

## Automation Scripts

### setup_remotes.py

A script to configure git remotes for all GAIA projects is available at:
`X:\Projects\_GAIA\setup_remotes.py`

Run with:
```bash
python X:\Projects\_GAIA\setup_remotes.py --org gaia-ecosystem
python X:\Projects\_GAIA\setup_remotes.py --org gaia-ecosystem --dry-run
python X:\Projects\_GAIA\setup_remotes.py --org gaia-ecosystem --project mycel
```

---

## Initial Push Workflow

For each project, the first push follows this pattern:

```bash
cd X:\Projects\jSeeker

# Initialize git (if not already)
git init

# Add remote
git remote add origin https://github.com/gaia-ecosystem/jseeker.git

# Create .gitignore
# (should already exist from WARDEN setup)

# Initial commit
git add .
git commit -m "Initial commit: jSeeker v0.2.1"

# Push to main
git push -u origin main
```

---

## Maintenance

### Adding New Projects
1. Register in `registry.json` via VULCAN
2. Create GitHub repo: `gh repo create gaia-ecosystem/project-name`
3. Add remote: `git remote add origin https://github.com/gaia-ecosystem/project-name.git`
4. Copy `.pre-commit-config.yaml` template
5. Push initial commit

### Archiving Projects
1. Update `registry.json` status to `"archived"`
2. Archive GitHub repo: `gh repo archive gaia-ecosystem/project-name`
