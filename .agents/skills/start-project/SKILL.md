---
name: start-project
description: Guide an owner from an early software idea through requirements discovery, MVP scoping, architecture choices, and a documented project scaffold.
---

# Start Project — Interactive Discovery Skill

## Trigger
Use when the owner says "start a project", shares a product idea for development, or explicitly invokes `start-project`.

## Phase 1: Frame the idea
Ask the owner to explain the idea in one or two sentences, then confirm:
- User or buyer and their core problem
- Current workaround and measurable desired outcome
- Platform and target environment
- Time, budget, integration, and compliance constraints
- What must *not* be included in the MVP

Ask up to three high-value questions per response. If the owner prefers, suggest sensible default options; label every default as a proposal.

## Phase 2: Define the product
Produce a short proposed product summary, primary user journeys, prioritized capabilities (must / should / later), non-goals, acceptance criteria, and open questions. Present tradeoffs; obtain explicit PRD/MVP approval.

## Phase 3: Architecture and experience
Present 1–3 viable implementation options when a material tradeoff exists. Evaluate complexity, operating cost, security/privacy, vendor lock-in, deployment, scale, observability, testability, and ongoing maintenance. Define a pragmatic UX/design direction. Request architecture approval. Avoid naming technologies as decisions until accepted.

## Phase 4: Project plan
Propose milestones sized to produce reviewable value; identify dependencies, validation steps, and exit criteria. Record risks, assumptions, unresolved decisions, and next action.

## Phase 5: Initialize
Only after scope and architecture approvals:
1. Run `python3 scripts/new_project.py "Project Name" --idea "..." --output <destination>` or manually generate the equivalent scaffold.
2. Fill the six docs with approved facts and explicitly tagged unresolved items; never fabricate commitments.
3. Configure `AGENTS.md` and `CLAUDE.md` for the resulting project.
4. Report exact generated paths, what was confirmed vs assumed, and the first implementation milestone.
5. Ask whether to enter execution mode. Do not start coding solely because the documents exist.

## Ongoing handoffs
On each major decision or milestone, update `docs/MEMORY.md` with dated decision context and `docs/TASKS.md` with verified status. Revisit PRD and architecture if the request changes scope.

## Guardrails
- Never overwrite an existing destination silently.
- Never use unaudited third-party scripts as an implicit requirement.
- Protect secrets and personal data.
- Do not claim a step was completed without verification.
