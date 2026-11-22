# FlowForge — Canonical Workflow Format and Execution Flow

**Contract owner:** Alabhya (API schema) + Aditya (execution semantics)  
**Consumers:** Pawni (frontend), Jayesh (AI generator and handlers)  
**Last updated:** 22 November 2026

## 1. Canonical workflow JSON
The frontend, backend, execution engine and AI generator must use this format. Do not create parallel shapes.

```json
{
  "id": "workflow-1",
  "name": "Urgent Message Alert",
  "nodes": [
    {
      "id": "trigger-1",
      "type": "trigger",
      "position": { "x": 100, "y": 100 },
      "data": {
        "action": "manual_trigger",
        "label": "Manual Trigger",
        "config": {}
      }
    },
    {
      "id": "ai-1",
      "type": "ai",
      "position": { "x": 350, "y": 100 },
      "data": {
        "action": "classify_message",
        "label": "Classify Message",
        "config": { "prompt": "Classify urgency as high or normal" }
      }
    },
    {
      "id": "condition-1",
      "type": "condition",
      "position": { "x": 600, "y": 100 },
      "data": {
        "action": "if_else",
        "label": "Urgent?",
        "config": { "field": "urgency", "operator": "equals", "value": "high" }
      }
    },
    {
      "id": "telegram-1",
      "type": "action",
      "position": { "x": 850, "y": 50 },
      "data": {
        "action": "telegram_send",
        "label": "Send Telegram Alert",
        "config": { "message_template": "Urgent message: {{input.text}}" }
      }
    }
  ],
  "edges": [
    { "id": "e1", "source": "trigger-1", "target": "ai-1" },
    { "id": "e2", "source": "ai-1", "target": "condition-1" },
    { "id": "e3", "source": "condition-1", "target": "telegram-1", "sourceHandle": "true" }
  ]
}
```

## 2. Required fields and rules
- `id`: unique workflow ID when persisted; drafts may use a client-generated ID.
- `name`: human-readable workflow name.
- `nodes`: array of nodes with unique `id`, supported `type`, canvas `position` and `data`.
- `data.action`: allowlisted handler key; this selects a registered node implementation.
- `data.config`: node-specific configuration only; validate by action type.
- `edges`: directed connections. `source` and `target` must refer to existing node IDs.
- Conditional edge `sourceHandle` is `true` or `false`; use the same literal in React Flow handles and engine routing.
- Reject unsupported node/action types, duplicate IDs, invalid references and cycles for the MVP.

## 3. Initial supported node actions
| Node type | Action | Purpose |
|---|---|---|
| trigger | `manual_trigger` | Starts a manual run and provides initial input |
| ai | `summarize_text` | Summarizes input text |
| ai | `classify_message` | Classifies input/urgency |
| condition | `if_else` | Evaluates configured field/operator/value |
| action | `telegram_send` | Sends a Telegram message |
| action | `http_request` | Optional generic HTTP request |

## 4. Node handler contract
All handlers should follow one agreed interface (sync or async may be wrapped consistently):

```python
async def execute(config: dict, input_data: dict, context: dict) -> dict:
    """Execute one node and return JSON-serializable output."""
```

- `config`: node's `data.config`.
- `input_data`: output selected from the upstream node(s), according to the agreed input-passing rule.
- `context`: execution ID, workflow ID and safe runtime metadata; never expose secrets to the UI.
- Return a JSON-serializable dictionary.
- Raise a structured exception on failure; engine records the failure and stops downstream execution unless an explicit future error branch is implemented.

## 5. Execution lifecycle
1. API loads workflow version and validates the graph.
2. Create an execution record with status `running`.
3. Initialize trigger input and locate the start trigger.
4. Execute node handler from registry; record input/output/status/timing.
5. Route to downstream edges. For `if_else`, select only the true or false edge based on result.
6. Mark nodes in the unselected branch `skipped` if they are part of the recorded run view.
7. Mark execution `success` or `failed`; persist final result.
8. Frontend fetches or receives execution status updates.

## 6. Execution response example
```json
{
  "execution_id": "exec-123",
  "workflow_id": "workflow-1",
  "status": "success",
  "nodes": [
    { "node_id": "trigger-1", "status": "success", "output": { "text": "..." } },
    { "node_id": "ai-1", "status": "success", "output": { "urgency": "high" } },
    { "node_id": "condition-1", "status": "success", "output": { "result": true } },
    { "node_id": "telegram-1", "status": "success", "output": { "message_id": 42 } }
  ]
}
```

## 7. Progress log
| Date | Owner | Update | Status |
|---|---|---|---|
| 22 Nov | Alabhya + Aditya | Initial graph schema, supported actions and execution lifecycle defined. All other modules must conform. | Draft — team approval required |
