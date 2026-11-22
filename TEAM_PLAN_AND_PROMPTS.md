# FlowForge — Team Plan, Phases and Individual Coding Prompts

**Team:** Alabhya, Pawni, Aditya, Jayesh  
**Planning window:** 22 November–1 December 2026  
**Mid-evaluation:** 1 December 2026

## Critical instruction: documentation first, coding second
The eight shared documents in `/docs` must exist and be reviewed before any feature implementation starts:

- `docs/prd.md`
- `docs/architecture.md`
- `docs/rules.md`
- `docs/phases.md`
- `docs/design.md`
- `docs/memory.md`
- `docs/decisions.md`
- `docs/flow.md`

The ZIP pack provides a baseline for these files. Aditya must place them in the GitHub repository and open a documentation-only PR to `dev`. All members review their relevant sections. Merge this PR before feature coding. If the team changes anything during review, update the docs before starting code.

## Team ownership
| Member | Primary ownership | Supporting work | Branch |
|---|---|---|---|
| Alabhya | FastAPI, API contracts, PostgreSQL, CRUD/execution APIs | API documentation and integration tests | `feature/alabhya-api` |
| Pawni | React, React Flow, dashboard, node UI | Frontend/API integration and UX testing | `feature/pawni-frontend` |
| Aditya | Workflow execution engine, graph validation, branching | GitHub administration, PR/release integration | `feature/aditya-engine` |
| Jayesh | AI workflow generator, AI node, Telegram integration | Daily memory consolidation and end-to-end fixtures | `feature/jayesh-ai` |

## Workload adjustment for 24 and 25 November
Alabhya and Pawni are intentionally assigned only light work on these two dates (about 1–2 hours/day). Do not place critical implementation deadlines or integration dependencies on them then.

- Alabhya: answer API-contract questions, review schema/PR feedback, refine examples and update API documentation.
- Pawni: review current canvas UX, finalize node labels/config fields, test existing UI and record design bugs.
- Aditya: carry the main execution-engine implementation and tests.
- Jayesh: carry the main AI generator, schema validation and Telegram handler implementation.

Their heavier implementation is scheduled for 22–23 and 26–29 November.

## Phases and exit gates
| Dates | Phase | Main outcome |
|---|---|---|
| 22 Nov | Phase 0: Docs and contracts | All eight docs reviewed and docs-only PR merged before coding |
| 23 Nov | Phase 1: Foundations | Each module runs locally; shared workflow schema adopted |
| 24–25 Nov | Phase 2: Core implementation | Engine and AI/integration modules work independently; Alabhya/Pawni light workload |
| 26–27 Nov | Phase 3: Integration | Manual and AI-generated workflows run end to end |
| 28–29 Nov | Phase 4: Stabilization | Core path tested, errors fixed, demo repeatable |
| 30 Nov | Phase 5: Freeze and rehearsal | Stable `main`, presentation and rehearsed demo |
| 1 Dec | Mid-evaluation | Demonstrate end-to-end FlowForge MVP |

## GitHub rules
- Aditya creates and maintains `main`, `dev` and the four feature branches.
- Each person commits only to their own feature branch.
- No direct pushes to `main` or `dev`.
- All work enters `dev` through a PR with test evidence and relevant documentation updates.
- Aditya reviews/coordinates merges but each author must test their own work.
- Stable, tested `dev` is merged to `main` before evaluation.

## Daily progress documentation rule
At the beginning of a work session, read `phases.md`, `memory.md` and the docs for your module. At the end of each day, report `Done | Tests/evidence | Blockers | Next`.

Update the relevant document(s) every day:
- Alabhya: `prd.md` for requirement changes; `flow.md` for API/schema changes; append progress in both when relevant.
- Pawni: `design.md`; update `flow.md` if the visual graph contract changes.
- Aditya: `architecture.md`, `rules.md`, `phases.md`, `decisions.md` as relevant.
- Jayesh: `memory.md`; update `flow.md` for AI node/handler contract changes and `decisions.md` through proposals.
- Every code PR must update relevant docs or explicitly state why no doc change is required.
- Append dated entries; do not delete previous progress history. Never add secrets to docs.

---

# Copy-paste prompts for each teammate

## Common instructions — include at the top of every teammate prompt
You are joining an existing four-person hackathon team building FlowForge. Before writing any implementation code, inspect the repository and verify that all eight shared files exist under `/docs`: `prd.md`, `architecture.md`, `rules.md`, `phases.md`, `design.md`, `memory.md`, `decisions.md`, `flow.md`.

Read all eight files, especially the sections relevant to your role. These are the project's source of truth. If any file is missing, incomplete or inconsistent, do not start feature coding. Create/fix the missing documentation first, open a docs-only PR, and wait for Aditya/team approval and merge into `dev`. Do not create conflicting personal copies of shared documents.

After docs are approved, start your assigned implementation only on your own branch. Before/with every implementation PR, update the relevant shared docs with current status, progress, tests, blockers and decisions. At the end of each workday, append a dated update to the relevant document progress log and send `Done | Tests/evidence | Blockers | Next`. Never claim a feature works unless you ran it or provide a clear test limitation. Do not commit secrets. Follow `rules.md` and the canonical schema in `flow.md`.

## 1. Alabhya — API and backend
You are the backend/API owner for FlowForge. Work only on `feature/alabhya-api`.

Use Python FastAPI, Pydantic, SQLAlchemy and PostgreSQL, following `architecture.md` and `flow.md`.

Deliver:
1. FastAPI project scaffold and environment configuration (`.env.example`, never real secrets).
2. Database models/migrations or documented schema for users, workflows, executions and node executions.
3. Workflow CRUD endpoints: create, list, retrieve, update and delete, with ownership checks where authentication is implemented.
4. Pydantic models that validate the exact graph structure in `flow.md`.
5. `POST /workflows/{workflow_id}/execute` that calls Aditya's engine through an agreed service interface, rather than duplicating engine logic.
6. `GET /executions/{execution_id}` and persistence of execution/node logs.
7. Swagger docs and API tests (CRUD, invalid graph, missing workflow and execution results).

Coordinate the route request/response envelope and handler call with Aditya; coordinate workflow types with Pawni; coordinate `/ai/generate-workflow` payload/response with Jayesh. Do not invent a second JSON schema.

Schedule: do the main scaffold/schema/CRUD work on 22–23 Nov; keep 24–25 Nov to approximately 1–2 hours/day for contract review, documentation and answering integration questions; complete execution API and persistence integration on 26–27 Nov; test/fix on 28–29 Nov. Update `prd.md`, `flow.md` and relevant `architecture.md` sections as implementation evolves.

Work module by module. Give complete code, commands and tests. Do not build unrelated advanced infrastructure before the core backend works.

## 2. Pawni — Frontend and visual workflow editor
You are the frontend/UI owner for FlowForge. Work only on `feature/pawni-frontend`.

Use React, TypeScript, React Flow and the styling setup already agreed in `architecture.md` and `design.md`.

Deliver:
1. Dashboard and workflow editor shell.
2. React Flow canvas with palette, connections, pan/zoom and custom Trigger, AI, Condition and Action nodes.
3. Node configuration panel with required-field validation.
4. Typed frontend model that matches `flow.md` exactly.
5. Save/load integration with Alabhya's workflow APIs.
6. Run action and visible per-node states: pending, running, success, failed and skipped.
7. Execution log/history panel.
8. AI-generated workflow preview that loads as an editable draft; never auto-run generated content.

Coordinate exact request/response shapes with Alabhya. Coordinate node action names and edge handles with Aditya. Do not implement backend execution logic.

Schedule: build the React shell and canvas on 22–23 Nov; keep 24–25 Nov to approximately 1–2 hours/day for UX review, node-label/config review and testing existing UI only; complete save/load and status integration on 26–27 Nov; polish and test on 28–29 Nov. Update `design.md` daily and update `flow.md` if UI exposes a schema mismatch.

Prioritize a clear, usable editor over decorative effects. Give complete components, setup steps and tests.

## 3. Aditya — Execution engine and GitHub maintainer
You are the workflow-engine owner and GitHub maintainer for FlowForge. Your coding branch is `feature/aditya-engine`.

Before feature coding, create the repo branches and ensure the eight docs are committed through a docs-only PR to `dev`. You manage `main`, `dev`, PR review, integration, merge-conflict resolution and stable release. Do not do all teammates' coding for them; authors test their own PRs.

Build the Python execution engine according to `architecture.md` and `flow.md`:
1. Graph validation: unique node IDs, valid edge endpoints, supported node/action allowlist and cycle rejection.
2. Node registry with a shared handler interface such as `async def execute(config, input_data, context) -> dict`.
3. DAG traversal for supported acyclic graphs.
4. Input/output passing and execution context.
5. If/Else routing using the `true`/`false` source handles; execute only the selected branch and represent the unselected path as skipped where practical.
6. Per-node and overall execution statuses, durations and structured error handling.
7. Unit tests for valid graph, invalid graph, true branch, false branch, missing handler and handler failure.
8. A documented engine service interface that Alabhya can call from FastAPI.

Schedule: set up docs/repo on 22 Nov; engine skeleton on 23 Nov; prioritize engine traversal, branching and tests on 24–25 Nov; integrate with Alabhya/Jayesh on 26–27 Nov; stabilize, merge and tag the evaluation version on 28–30 Nov. Keep `architecture.md`, `rules.md`, `phases.md` and `decisions.md` current. Coordinate any schema change before coding it.

## 4. Jayesh — AI workflow generation and integrations
You are the AI/integration owner for FlowForge. Work only on `feature/jayesh-ai`.

Use the agreed LLM provider API, Python/Pydantic and Telegram Bot API. Follow `architecture.md`, `prd.md` and `flow.md`.

Deliver:
1. LLM service wrapper configured via environment variables.
2. `POST /ai/generate-workflow` integration contract with Alabhya (you own generator logic; Alabhya owns API route unless team agrees otherwise).
3. Natural-language prompt to structured graph JSON using only allowlisted node/action types in `flow.md`.
4. Strict schema validation and helpful error/fallback behavior; never generate or execute arbitrary Python/JavaScript code.
5. AI summarize/classify node handler following Aditya's handler interface.
6. Telegram send handler with token/chat ID from environment variables and no secrets in logs.
7. Prompt fixtures and tests for valid request, malformed LLM output, unsupported node type and Telegram success/failure (mock external calls in tests).
8. A sample AI-generated workflow for the evaluation demo.

Coordinate handler interface with Aditya, API route and response with Alabhya, and generated graph rendering with Pawni. Update `memory.md` daily and `flow.md`/`decisions.md` when interfaces or decisions change.

Schedule: schema and provider setup on 22–23 Nov; main generation, validation, AI node and Telegram handler work on 24–25 Nov; connect generator and handlers end to end on 26–27 Nov; robustness and demo fixtures on 28–29 Nov.

## Final instruction for all four members
A feature is not complete just because code was generated. Run it, test it, record evidence, update the docs, push your feature branch and open a PR. The target for 1 December is one reliable end-to-end product, not four disconnected modules.
