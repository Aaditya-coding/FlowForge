# FlowForge — Product Requirements Document

**Status:** Baseline for team review  
**Document owner:** Alabhya (API/product requirements)  
**Last updated:** 22 November 2026  
**Mid-evaluation:** 1 December 2026

## 1. Product summary
FlowForge is a visual workflow automation platform. Users assemble trigger, AI, logic, and action nodes on a canvas, save workflows, run them, and inspect execution results. A user can also describe an automation in plain language and have AI generate a draft workflow for review.

## 2. Target user and problem
The target user wants to automate repeatable tasks without writing a full application. The product should make the workflow understandable visually and make execution results observable.

## 3. Mid-evaluation MVP
### Must work end to end
- Dashboard with create/open workflow entry points.
- React Flow canvas: add, connect, configure, delete and save nodes.
- Workflow CRUD APIs and persistent storage.
- Manual trigger and a small set of working node handlers.
- AI processing node (summarize or classify).
- If/Else condition with true/false branch selection.
- One external action integration: Telegram notification.
- Run workflow and display per-node status and execution history.
- Natural-language workflow generation that returns the agreed JSON schema and renders on the canvas.

### Stretch goals only after MVP is stable
- Webhook trigger, scheduled execution, OAuth-based Gmail/Google Sheets, retries, workflow templates, agent memory, marketplace, analytics and complex loops.

## 4. Core user journeys
1. User creates a workflow, adds nodes, connects them, configures them and saves.
2. User runs a saved workflow; the engine executes reachable nodes and the UI shows node statuses and logs.
3. User enters a natural-language request; AI returns a validated workflow draft; user reviews/edits it before running.
4. User opens an execution record and inspects success/failure and node outputs.

## 5. Functional requirements
- FR-01: Create, list, retrieve, update and delete owned workflows.
- FR-02: Persist workflow name, nodes, edges and version.
- FR-03: Validate node types, configuration and edge references before saving/running.
- FR-04: Support manual trigger, AI processing, condition and Telegram action nodes.
- FR-05: Pass node output to downstream nodes through a consistent execution context.
- FR-06: Condition nodes select only the matching true or false edge.
- FR-07: Record execution and node-execution status, input/output summary, errors and timing.
- FR-08: Generate workflows from natural language using only supported node types.
- FR-09: Display workflow and execution state in the frontend.

## 6. Non-functional requirements
- Keep modules separated and interfaces documented.
- Never execute arbitrary code returned by an LLM.
- Keep API keys and bot tokens in environment variables; never commit secrets.
- Validate ownership on workflow and execution endpoints.
- Provide useful errors and basic automated tests for core paths.
- A working, reliable MVP is more important than a large feature count.

## 7. Out of scope for the mid-evaluation
Arbitrary Python execution, unrestricted agent tool access, loops/cycles, complex parallel orchestration, broad third-party connector catalogue, production-grade multi-tenant billing and marketplace.

## 8. Acceptance criteria for 1 December
- Team can demonstrate a workflow created manually and saved.
- Workflow can execute through at least trigger → AI → condition → Telegram (true branch) and visibly skip the false branch.
- User can ask AI to generate a supported workflow, review it on canvas and execute it.
- Execution history shows each node's result and errors where applicable.
- Demo is repeatable on the team's demo environment.

## 9. Progress log
| Date | Owner | Update | Status |
|---|---|---|---|
| 22 Nov | Team | Baseline PRD created; review requirements and adjust only through a recorded decision. | Draft |
