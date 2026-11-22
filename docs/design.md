# FlowForge — Product and UI Design Notes

**Status:** Initial UX baseline  
**Document owner:** Pawni  
**Last updated:** 22 November 2026

## 1. UX objective
Make workflow creation understandable: users should see the flow, add/connect nodes, configure the selected node, run the workflow and understand what succeeded or failed.

## 2. Main screens
1. Dashboard: create workflow, recent workflows, recent execution summary.
2. Workflow editor: top toolbar, node library, central canvas, configuration panel and execution panel.
3. AI Builder: plain-language prompt, generate action, preview/validation message and open-on-canvas action.
4. Execution history: run status, time, per-node input/output summary and error details.

## 3. Editor layout
- Top toolbar: workflow name, save status, Run button.
- Left panel: node categories — Triggers, AI, Logic, Actions.
- Center: React Flow canvas with zoom/pan, minimap if time permits, connectable handles.
- Right panel: selected node's configuration fields.
- Bottom or collapsible panel: execution log and node result details.

## 4. MVP node catalogue
- Trigger: Manual Trigger.
- AI: Summarize/Classify.
- Logic: If/Else condition.
- Action: Telegram Send; optional HTTP Request.
Use clear labels, short descriptions and visible input/output handles.

## 5. Visual states
- Pending: neutral.
- Running: animated or highlighted state, not color alone.
- Success: green indicator and label.
- Failed: red indicator, error detail available.
- Skipped: muted indicator for unselected conditional branch.
- Saved/unsaved: explicit status near workflow title.

## 6. Interaction requirements
- Drag node from palette to canvas.
- Connect source/target handles.
- Select node to configure; validate required fields.
- Save workflow and reload the same graph.
- Run workflow and reflect execution status without page refresh where practical.
- AI-generated workflow opens as an editable draft; it must not auto-run.
- Show clear empty, loading, validation and failure states.

## 7. Design priorities
Prioritize usability and a coherent editor over decorative animation. Keep a consistent spacing/type/color system; ensure status is communicated through text/icons as well as color. Use responsive layout, but desktop editor is the primary mid-evaluation target.

## 8. Progress log
| Date | Owner | Update | Status |
|---|---|---|---|
| 22 Nov | Pawni | Initial editor layout and interaction requirements documented. | Draft |
