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
| API/backend | Alabhya | Phase 0 done | PR #1 reviewed | — | Scaffold FastAPI project (Phase 1) |
| Frontend/editor | Pawni | Phase 0 done | PR #1 reviewed | Branch behind dev | Sync branch with dev, then scaffold editor (Phase 1) |
| Execution engine/GitHub | Aditya | Phase 0 done | PR #1 merged, branches created, branch protection set | — | Engine skeleton (Phase 1) |
| AI/integrations | Jayesh | Phase 0 partial | `.env.example` pushed, no PR | Telegram bot not created | Complete Telegram bot setup, push code, open PR |

## 4. Daily log
Append one entry per day; do not delete older entries.

### 22 November 2026
- **Aditya:** Created GitHub repo. Created `main`, `dev`, and 4 feature branches. Pushed 8 baseline docs. Opened and merged PR #1 (`docs/project-baseline` → `dev`). Set up branch protection on `main` and `dev`. Added PR template and `check_docs.py` validation script.
- **Jayesh:** Checked out `feature/jayesh-ai` branch. Pushed `.env.example` with Telegram/Gemini env vars (commit `9124f4c`). Telegram bot NOT yet created. No code written. No PR opened.
- **Alabhya:** Branch `feature/alabhya-api` exists, synced with dev. No code activity yet.
- **Pawni:** Branch `feature/pawni-frontend` exists but is behind `dev` (missing docs commits). Needs to sync. No code activity yet.
- **Status:** Phase 0 exit gate partially met — docs merged but `memory.md` needed updating. Branch protection now configured. `feature/pawni-frontend` needs sync with `dev`.

## 5. Open questions
- Which LLM provider/key quota will the team use for the demo?
- Does the team already have PostgreSQL hosting, or will local Docker be used?
- Is the Telegram bot/token ready? Store it only in environment variables.
- Which deployment target is available to the team?

## 6. How to update this file
At the end of each day, each owner sends Jayesh `Done | Tests/evidence | Blockers | Next`. Jayesh consolidates concise factual updates here. Never put API keys, passwords, private user data or raw secrets in this file.
