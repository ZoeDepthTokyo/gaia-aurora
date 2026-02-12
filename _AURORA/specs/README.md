# AURORA Specs

UX specifications for all GAIA projects, organized by project.

## Directory Structure

```
specs/
├── {project_name}/
│   ├── ux_requirements.md       # Phase 1: Intake output
│   ├── creative_direction.md    # Phase 2: Mood board + style direction
│   ├── inspiration.md           # Phase 2: Curated references
│   ├── ux_spec.md              # Phase 3: 7-pass UX analysis
│   ├── build_order.md          # Phase 4: Numbered implementation prompts
│   └── learnings.md            # Phase 6: Post-deployment learnings
```

## Workflow

1. **Phase 1: Intake** → `ux_requirements.md`
2. **Phase 2: Inspire** → `creative_direction.md` + `inspiration.md`
3. **Phase 3: Spec** → `ux_spec.md`
4. **Phase 4: Build** → `build_order.md`
5. **Phase 5: Refine** → (working prototype)
6. **Phase 6: Deploy** → `learnings.md`

## Projects

Specs are created per-project. Each project gets its own directory.

Example projects:
- `jseeker/` — jSeeker UX specs
- `abis/` — ABIS Visual Builder UX specs
- `argus/` — ARGUS Dashboard UX specs
- `hart-os/` — HART OS UX specs

## Usage

```bash
# Start new project spec
/aurora-intake <project_name>

# Generate creative direction
/aurora-mood <project_name>

# Create UX specification
/aurora-spec <project_name>

# Generate build order
/aurora-build <project_name>
```

## Cross-Project Patterns

When AURORA discovers reusable patterns during specification:
- Pattern documented in `X:\Projects\_GAIA\_AURORA\patterns\`
- Pattern referenced in future specs
- Pattern promoted to design system if widely applicable
