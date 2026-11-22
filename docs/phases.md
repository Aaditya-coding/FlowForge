# FlowForge — Phased Delivery Plan

**Status:** Baseline schedule  
**Project coordinator:** Aditya  
**Mid-evaluation:** 1 December 2026

## Working assumptions
- Project window: 22 November through 1 December 2026.
- Alabhya and Pawni have reduced availability on 24 and 25 November. Keep their work on those two dates to light review/documentation/unblocking tasks (approximately 1–2 hours each per day); do not schedule critical implementation or integration deliverables for them on those dates.
- Shift their heavier implementation to 22–23 and 26–29 November.
- Aditya and Jayesh carry the heavier independent engineering tasks on 24–25 November.

## Phase 0 — Documentation and contracts (22 November)
**All four collaborate; Aditya coordinates and commits the docs-only PR.**
- Confirm the MVP and acceptance criteria in `prd.md`.
- Confirm stack and service boundaries in `architecture.md`.
- Confirm workflow JSON and execution lifecycle in `flow.md`.
- Pawni adds canvas/screen requirements in `design.md`.
- Alabhya reviews API requirements and endpoint contracts.
- Jayesh reviews AI schema and integration constraints; initializes `memory.md`.
- Aditya verifies all eight docs exist, records decisions, creates branches and merges docs-only PR to `dev`.
**Exit gate:** all eight files exist and are reviewed/merged before feature coding.

## Phase 1 — Foundations and parallel module skeletons (23 November)
- Alabhya: FastAPI project, PostgreSQL connection, Pydantic workflow schema, create/list/get/update API skeletons, Swagger visible.
- Pawni: React app shell, dashboard, React Flow canvas, node palette and shared TypeScript workflow types.
- Aditya: engine module skeleton, graph validation, registry interface, branch protections and PR template.
- Jayesh: LLM service wrapper, prompt/schema design, Pydantic output validation and Telegram bot setup using environment variables.
**Exit gate:** each module runs locally; contracts match `flow.md`.

## Phase 2 — Core implementation (24–25 November)
### Alabhya — reduced workload
- Only 1–2 hours/day: review API contract questions, refine request/response examples, review schema/PR feedback and document any changes.
- No critical new endpoints or major refactors scheduled.
### Pawni — reduced workload
- Only 1–2 hours/day: review canvas UX, finalize node labels/configuration fields, test current UI and document bugs/design refinements.
- No major new page or high-dependency API integration scheduled.
### Aditya — primary implementation
- Complete DAG validation/traversal for supported acyclic workflows.
- Complete node registry and standard handler interface.
- Implement execution context, output passing, condition true/false routing, status tracking and unit tests.
- Provide a small mock/manual handler to prove the engine independently.
### Jayesh — primary implementation
- Complete natural-language workflow generation against the canonical schema.
- Add strict allowlist and validation; create sample prompt fixtures.
- Implement AI summarize/classify handler and Telegram send handler.
- Test handlers independently with mocked inputs; document environment setup.
**Exit gate by 25 Nov evening:** engine can run a simple graph in isolation; AI generator returns validated graph JSON; Telegram handler works in isolation.

## Phase 3 — Integration and end-to-end workflow (26–27 November)
- Alabhya: full availability; finish CRUD and execution APIs, persist executions/node logs, integrate engine service, API tests and error responses.
- Pawni: full availability; finish save/load, connect APIs, build Run flow, node status styling and execution log panel.
- Aditya: integrate engine with Alabhya's service/API, handle branch execution and report results; review/merge PRs.
- Jayesh: wire AI generator route through API, render/test generated workflows with Pawni, connect AI and Telegram node handlers, run complete integration tests.
**Exit gate:** manually created workflow and AI-generated workflow can both be run end to end.

## Phase 4 — Stabilization and evaluation rehearsal (28–29 November)
- All members: bug fixes, negative tests, invalid schema handling and demo workflow verification.
- Alabhya: API ownership checks, persistence and failure response tests.
- Pawni: UX polish, empty/loading/error states, live status refresh and responsive layout.
- Aditya: engine edge cases, skip unselected branch, failure handling, merge/release stability.
- Jayesh: AI prompt robustness, Telegram failure handling, fallback sample workflow and demo data.
**Exit gate:** repeatable end-to-end demo; no known blocker in core path.

## Phase 5 — Feature freeze and presentation (30 November)
- Freeze new features; only critical bug fixes.
- Aditya merges tested `dev` to `main`, tags evaluation build and checks repository.
- Pawni prepares screenshots/UI walkthrough.
- Alabhya prepares API/DB architecture explanation.
- Jayesh prepares AI workflow-generation demo and sample prompts.
- All rehearse the same 3–5 minute end-to-end demo.
**Exit gate:** stable deployed/local demo, slides and responsibilities agreed.

## 1 December — Mid-evaluation
Demonstrate: prompt → generated workflow → user review → manual edit → execution → condition branch → Telegram action → execution history.

## Daily reporting format
Each owner reports: `Done | Tests/evidence | Blockers | Next`. Update relevant document logs daily. Jayesh consolidates `memory.md`; Aditya updates this phase tracker and the decision log.

## Progress log
| Date | Owner | Update | Status |
|---|---|---|---|
| 22 Nov | Aditya | Ten-day phased baseline created; reduced availability on 24–25 accounted for. | Planned |
