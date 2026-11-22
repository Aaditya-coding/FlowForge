# FlowForge — Living Project Memory

**Purpose:** Current shared project state, key context, blockers and next actions.  
**Steward:** Jayesh (daily consolidation)  
**Last updated:** 22 November 2026

## 1. Product snapshot
FlowForge is a visual workflow automation platform using React Flow, FastAPI, PostgreSQL, a Python execution engine, an LLM API and Telegram integration.

## 2. Current agreed facts
- Mid-evaluation: 1 December 2026.
- Team: Alabhya (API/backend), Pawni (frontend/editor), Aditya (execution engine + GitHub), Jayesh (AI + integrations).
- Alabhya and Pawni have reduced availability on 24–25 November; assign light review/docs only on those dates.
- The eight shared docs must be present and merged before feature coding starts.
- `flow.md` is the canonical workflow payload and execution contract.
- `decisions.md` records changes to agreed technology, scope and interfaces.

## 3. Current status
| Workstream | Owner | Status | Evidence / PR | Blocker | Next action |
|---|---|---|---|---|---|
| API/backend | Alabhya | Not started | — | — | Review API contract and scaffold service |
| Frontend/editor | Pawni | Not started | — | — | Review design and scaffold editor |
| Execution engine/GitHub | Aditya | Not started | — | — | Create repo, branches and docs-only PR |
| AI/integrations | Jayesh | Not started | — | — | Review schema and set up provider wrapper |

## 4. Daily log
Append one entry per day; do not delete older entries.

### 22 November 2026
- Baseline documentation pack prepared for team review.
- Next: confirm docs, create repo/branches and merge docs-only PR before implementation.

## 5. Open questions
- Which LLM provider/key quota will the team use for the demo?
- Does the team already have PostgreSQL hosting, or will local Docker be used?
- Is the Telegram bot/token ready? Store it only in environment variables.
- Which deployment target is available to the team?

## 6. How to update this file
At the end of each day, each owner sends Jayesh `Done | Tests/evidence | Blockers | Next`. Jayesh consolidates concise factual updates here. Never put API keys, passwords, private user data or raw secrets in this file.
