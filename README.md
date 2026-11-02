# AI Project Starter Agent

A repeatable, approval-driven discovery workflow for turning a new software idea into an actionable, documented project.

## Start here

Open this repository in Codex or Claude Code and say:

> Start a project: An AI-powered inventory management SaaS.

The agent follows `.agents/skills/start-project/SKILL.md`, interviews you in small batches, identifies unknowns, proposes a scoped MVP, and prepares the project documents. **No application code until you approve the plan.**

## Contents
- `AGENTS.md`: shared agent operating rules
- `CLAUDE.md`: Claude Code entrypoint
- `.agents/skills/start-project/SKILL.md`: discovery and initialization workflow
- `docs/`: six reusable templates
- `scripts/new_project.py`: standard new-project scaffold generator

## Local scaffold
```bash
python3 scripts/new_project.py "Inventory AI" --idea "Inventory management for small companies" --output ~/Projects
```

The scaffold is a draft, not a substitute for product discovery. The generator will not overwrite existing projects. Review and approve all architectural and scope decisions before implementation.

## Use in another repository
Copy `AGENTS.md`, `CLAUDE.md`, `docs/` and `.agents/skills/start-project/` to the project repository; alternatively ask your agent to reference this starter repository. Note that agents do **not** automatically load remote GitHub instructions—provide them access to a checked-out copy or explicitly include the skill.

## Principles
Requirements before code. Ask about uncertainties rather than invent facts. Preserve decisions and context in versioned Markdown. Keep human approval gates at architecture, MVP, and build stages. Protect credentials and user data.
