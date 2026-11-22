# FlowForge — Team, Git and Engineering Rules

**Status:** Active from repository kickoff  
**Document owner:** Aditya (repository maintainer)  
**Last updated:** 22 November 2026

## 1. Work must not start before the documentation baseline exists
Before feature coding begins, all eight shared documents must be present in `/docs`:
`prd.md`, `architecture.md`, `rules.md`, `phases.md`, `design.md`, `memory.md`, `decisions.md`, `flow.md`.

The team reviews the baseline and merges a documentation-only PR to `dev`. If any file is missing or materially incomplete, create/fix the documentation first. Do not begin feature implementation until the docs-only PR is merged.

## 2. Branch policy
- `main`: evaluation-ready stable code; protected.
- `dev`: team integration branch; protected from direct pushes.
- `feature/alabhya-api`: Alabhya.
- `feature/pawni-frontend`: Pawni.
- `feature/aditya-engine`: Aditya.
- `feature/jayesh-ai`: Jayesh.
- Each member commits only to their feature branch.
- All feature work enters `dev` through a Pull Request.
- Aditya maintains branch protections, reviews PRs, resolves merge conflicts and coordinates merges. Each author remains responsible for testing their changes.

## 3. Commit and PR standards
- Use descriptive commits, e.g. `feat(api): add workflow create endpoint` or `fix(engine): skip unselected branch`.
- Keep PRs small and focused; include purpose, files changed, test evidence and screenshots/API examples where relevant.
- Do not merge code that breaks the shared app or changes the canonical JSON schema without an approved decision.
- Pull latest `dev` into the feature branch regularly; avoid force-pushing shared branches.

## 4. Coding standards
- Prefer small modules and explicit interfaces.
- TypeScript: use typed props and shared types for workflow JSON.
- Python: use type hints, Pydantic validation, clear exceptions and async only where it helps.
- Keep API handlers thin; business logic belongs in services.
- No hardcoded API keys, bot tokens, passwords or private user data.
- Do not commit `.env`, generated build folders, virtual environments or secrets.
- Add tests for schema validation, execution branches and API CRUD where practical.

## 5. Shared contract rule
The schema in `flow.md` is the source of truth. If a change is necessary, propose it in `decisions.md`, get agreement from affected owners, then update `flow.md`, API models, frontend types, tests and examples together.

## 6. Documentation update rule (mandatory)
These eight files are living project documents, not one-time setup files.
- Before coding: create and review all eight files, then merge a docs-only PR.
- At the start of each work session: read `phases.md`, `memory.md` and the relevant design/architecture/flow section.
- When implementation starts: update the relevant file's status and progress log before or with the first implementation PR.
- At the end of each day: every owner updates the relevant document(s) with completed work, tests, blockers and next step. Jayesh consolidates the daily summary in `memory.md`; Aditya updates `phases.md` and `decisions.md` when status or decisions change.
- Update `architecture.md` when component boundaries, data storage or integration change; `design.md` when screens/interactions change; `flow.md` when graph schema or execution behavior changes; `prd.md` when requirements or acceptance criteria change; `rules.md` when team conventions change.
- Every code PR must include relevant documentation changes or explicitly state “No documentation change required” with a reason.
- Never rewrite history or delete earlier progress entries; append dated entries.

## 7. Definition of done
A task is done only when: implementation is committed to its feature branch; tests/manual verification are recorded; relevant docs are updated; PR is opened; and the feature is integrated and smoke-tested on `dev`.

## 8. Progress log
| Date | Owner | Update | Status |
|---|---|---|---|
| 22 Nov | Aditya | Branch, PR, documentation-first and daily update rules drafted. | Active |
