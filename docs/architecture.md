# FlowForge — Architecture

**Status:** Baseline architecture  
**Document owner:** Aditya  
**Last updated:** 22 November 2026

## 1. Architecture overview
FlowForge uses a React frontend, a FastAPI backend, PostgreSQL persistence, a Python workflow execution engine, and an LLM API for workflow generation and AI node execution.

```text
User
  ↓
React + TypeScript + React Flow
  ↓ REST / WebSocket or polling
FastAPI  ─────────────── LLM API
  ↓                       ↑
Workflow service      AI workflow generator
  ↓                       ↓
PostgreSQL  ← validated workflow JSON
  ↓
Execution service
  ↓
Node registry → trigger / AI / condition / Telegram / HTTP
  ↓
Execution records → frontend status and logs
```

## 2. Agreed technology choices
- Frontend: React, TypeScript, React Flow, Tailwind CSS; use the team's existing UI library if already configured.
- Backend: Python FastAPI, Pydantic, SQLAlchemy.
- Database: PostgreSQL. Store graph definition as JSON/JSONB initially; use relational tables for workflow metadata and execution records.
- AI: one agreed provider API (Gemini or another provider selected by the team); wrap provider access behind a small service interface.
- Integrations: Telegram Bot API and generic HTTP request. Do not build multiple OAuth connectors for the mid-evaluation.
- Background execution: start with a simple background task/process model for the MVP. Add Redis/Celery only if required and time permits; do not let infrastructure block the first end-to-end run.

## 3. Service boundaries and owners
- Frontend/editor — Pawni: canvas, node UI, dashboard, save/load and status visualization.
- API/persistence — Alabhya: REST endpoints, database models, validation, auth baseline and API documentation.
- Execution engine/GitHub integration — Aditya: graph validation, registry, scheduler/traversal, branching, execution results and repository management.
- AI/integrations — Jayesh: natural-language generator, AI node, Telegram node handler and integration tests.

## 4. API contract
The canonical graph format is defined in `flow.md`. API handlers must validate this format rather than inventing a separate payload shape.

Minimum routes:
- `POST /workflows`
- `GET /workflows`
- `GET /workflows/{workflow_id}`
- `PUT /workflows/{workflow_id}`
- `DELETE /workflows/{workflow_id}`
- `POST /workflows/{workflow_id}/execute`
- `GET /executions/{execution_id}`
- `POST /ai/generate-workflow`

Execution route should call the engine through a stable Python service interface; it should not duplicate graph execution logic in the API route.

## 5. Execution model
- Validate unique node IDs, supported node types, edge endpoints and configuration.
- Reject cycles for the MVP.
- Find the supported start trigger, execute nodes and store outputs in an execution context keyed by node ID.
- For condition nodes, choose the `true` or `false` outgoing edge and do not execute the unselected branch.
- Record each node's status: `pending`, `running`, `success`, `failed`, or `skipped`.
- Save execution and node logs in PostgreSQL.

## 6. Data model (initial)
- `users`: identity and authentication fields.
- `workflows`: owner, name, status, current graph JSON and timestamps.
- `executions`: workflow/version, trigger source, overall status, started/finished timestamps.
- `node_executions`: execution ID, node ID, status, input/output JSON, error and duration.
- `credentials`: only if needed for user-specific integrations; encrypt secrets at rest and never return them to clients.

## 7. Security and reliability
- Treat LLM output as untrusted data. Validate against a strict schema and allowlist of node/action types.
- Never use `eval`, dynamic imports or arbitrary execution for AI-generated content.
- Keep secrets in `.env` locally and environment variables in deployment; commit `.env.example` only.
- Apply workflow ownership checks to reads, writes and executions.
- Set timeouts for external API calls and avoid logging secrets or full sensitive payloads.

## 8. Progress log
| Date | Owner | Update | Status |
|---|---|---|---|
| 22 Nov | Aditya | Initial boundaries and stack documented. Confirm exact framework versions and API response envelopes with owners. | Draft |
