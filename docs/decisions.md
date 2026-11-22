# FlowForge — Architecture and Product Decisions

**Decision owner:** Aditya  
**Rule:** Record significant decisions here; do not silently change shared contracts.  
**Last updated:** 22 November 2026

## Decision log

### DEC-001 — Use React Flow for the visual editor
- **Date:** 22 Nov 2026
- **Status:** Accepted baseline
- **Decision:** Use React + TypeScript + React Flow for workflow canvas and node interactions.
- **Reason:** Avoid building a graph editor from scratch and focus hackathon time on execution and product behavior.
- **Owner:** Pawni

### DEC-002 — Use FastAPI and PostgreSQL for backend/persistence
- **Date:** 22 Nov 2026
- **Status:** Accepted baseline
- **Decision:** Use Python FastAPI, Pydantic, SQLAlchemy and PostgreSQL.
- **Reason:** Clear API contracts, schema validation and persistent workflow/execution data.
- **Owner:** Alabhya

### DEC-003 — Start with an acyclic execution graph
- **Date:** 22 Nov 2026
- **Status:** Accepted for MVP
- **Decision:** Support DAG workflows with conditional branch selection; reject cycles for mid-evaluation.
- **Reason:** A bounded execution model can be implemented and tested reliably in the available time.
- **Owner:** Aditya

### DEC-004 — AI returns constrained workflow JSON, never executable code
- **Date:** 22 Nov 2026
- **Status:** Accepted for MVP
- **Decision:** LLM outputs only supported node types and graph schema defined in `flow.md`; backend validates before persistence/execution.
- **Reason:** Predictability, safety and compatibility with the visual editor.
- **Owner:** Jayesh

### DEC-005 — Prioritize one real external integration
- **Date:** 22 Nov 2026
- **Status:** Accepted for MVP
- **Decision:** Telegram notification is the first external action; generic HTTP can be added if time allows.
- **Reason:** Demonstrates an actual external side effect without spending the sprint on multiple OAuth integrations.
- **Owner:** Jayesh

## Change proposal template
For each new decision, append:
- ID and date
- Status: proposed / accepted / rejected / superseded
- Context/problem
- Options considered
- Decision and rationale
- Impacted files/interfaces
- Owner and reviewer

## Progress log
| Date | Owner | Update | Status |
|---|---|---|---|
| 22 Nov | Aditya | Five baseline decisions recorded; revisit only through an explicit team decision. | Active |
