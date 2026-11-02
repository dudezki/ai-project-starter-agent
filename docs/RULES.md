# Engineering Rules

Status: BASELINE — customize and approve before development.

1. No implementation before MVP and architecture approvals.
2. No keys, passwords, tokens, customer data or private credentials in source control, logs or prompts.
3. Implement the smallest validated milestone; do not silently expand scope.
4. Keep architecture and PRD synchronized when accepted changes alter requirements.
5. Define tests and acceptance criteria before declaring work complete.
6. Use dependency pinning, review new dependencies, and document licenses and security exposure.
7. Validate inputs, enforce authorization server-side and apply least privilege.
8. Favor simple, readable, observable and maintainable solutions.
9. Never claim tests were executed or deployments succeeded without evidence.
10. Update TASKS.md and MEMORY.md at meaningful milestones, without recording secrets.

## Project-specific conventions
TBD: coding style, repo layout, branching, environments, CI, releases.

## Quality gates
TBD: tests, static checks, security checks, review, rollback plan.

## Exceptions
Document and obtain approval for material deviations.
