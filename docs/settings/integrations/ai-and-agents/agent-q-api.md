# Agent Q API

The Agent Q API provides programmatic access to Agent Q's chat capabilities, session management, specialized workflows, and LLM configuration. Use these endpoints to integrate Agent Q into your own applications, automate interactions, or build custom interfaces.

## Authentication

All Agent Q API endpoints require a Qualytics Personal API Token (PAT) and a **Member** role or higher.

Include the token in the `Authorization` header:

```
Authorization: Bearer YOUR_QUALYTICS_API_TOKEN
```

For instructions on generating a token, see [Tokens](../../tokens/overview-of-tokens.md){:target="_blank"}.

## Chat

### Send a Message

Start or continue a conversation with Agent Q. Responses are streamed via Server-Sent Events (SSE) using the Vercel AI Data Stream Protocol.

```bash
curl -X POST "https://your-qualytics.qualytics.io/api/agent/chat" \
  -H "Authorization: Bearer YOUR_QUALYTICS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      {"role": "user", "content": "What tables are in our sales_db datastore?"}
    ],
    "data": {}
  }'
```

The request body follows the Vercel AI format:

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `messages` | array | Yes | Array of `{role, content}` objects representing the conversation history. |
| `data.session_id` | integer | No | Existing session ID to continue a conversation. If omitted, a new session is created automatically. |

The response streams SSE events:

| Event Type | Description |
|------------|-------------|
| `text-delta` | Incremental text chunk from Agent Q. |
| `tool-call` | A tool invocation has started. |
| `tool-input-available` | Input parameters for a tool call are ready. |
| `tool-output-available` | A tool execution has completed and returned results. |
| `error` | An error occurred during processing. |
| `done` | The response stream is complete. Messages are persisted to the session. |

!!! note
    The chat endpoint is rate-limited to **10 requests per minute** per user, with a maximum of **2 simultaneous streaming responses**. Exceeding these limits returns `HTTP 429 Too Many Requests`.

**Timeouts:**

| Layer | Timeout |
|-------|---------|
| Individual LLM API request | 120 seconds |
| Overall agent execution | 300 seconds |
| HTTP route handler | 360 seconds |

### Execute a Prompt

Execute a named MCP prompt directly for single-turn interactions without session context:

```bash
curl -X POST "https://your-qualytics.qualytics.io/api/agent/prompt" \
  -H "Authorization: Bearer YOUR_QUALYTICS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt_name": "list_containers",
    "arguments": {"datastore_name": "analytics_warehouse"}
  }'
```

Returns a JSON `AgentResponse`:

```json
{
  "success": true,
  "message": "...",
  "data": {},
  "error": null
}
```

### Get Suggestions

Retrieve 3 LLM-generated contextual prompt suggestions based on your data assets and active anomalies. These are the same suggestions shown in the Agent Q empty state in the UI.

```bash
curl -X GET "https://your-qualytics.qualytics.io/api/agent/suggestions" \
  -H "Authorization: Bearer YOUR_QUALYTICS_TOKEN"
```

Returns:

```json
{
  "suggestions": [
    "Investigate the recent spike in null values on the customers table",
    "Create a not-null check on the order_id field in transactions",
    "Show quality score trends for sales_db over the last 30 days"
  ]
}
```

## Chat Sessions

Agent Q organizes conversations into persistent sessions. Each session stores its message history, activated tools, and a generated summary for context resumption.

### Create a Session

```bash
curl -X POST "https://your-qualytics.qualytics.io/api/chat-sessions" \
  -H "Authorization: Bearer YOUR_QUALYTICS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"title": "Sales Data Investigation"}'
```

### List Sessions

```bash
curl -X GET "https://your-qualytics.qualytics.io/api/chat-sessions?page=1&size=20" \
  -H "Authorization: Bearer YOUR_QUALYTICS_TOKEN"
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `page` | integer | Page number (default: 1). |
| `size` | integer | Sessions per page (default: 20). |
| `search` | string | Filter by session title. |
| `archived` | string | `include` — return both active and archived. `only` — return archived only. |

### Get Active Generating Sessions

Returns the IDs of sessions that are currently streaming a response. Useful for showing loading indicators when the user navigates away.

```bash
curl -X GET "https://your-qualytics.qualytics.io/api/chat-sessions/generating" \
  -H "Authorization: Bearer YOUR_QUALYTICS_TOKEN"
```

Returns: `[123, 456]`

### Get a Session

```bash
curl -X GET "https://your-qualytics.qualytics.io/api/chat-sessions/{session_id}" \
  -H "Authorization: Bearer YOUR_QUALYTICS_TOKEN"
```

Returns the session with its full message array (`GetChatSessionDetail`).

### Get Session Messages

Retrieve paginated messages for a session (default: 10 per page, newest first).

```bash
curl -X GET "https://your-qualytics.qualytics.io/api/chat-sessions/{session_id}/messages?page=1&size=10" \
  -H "Authorization: Bearer YOUR_QUALYTICS_TOKEN"
```

### Update a Session

Rename or update session metadata:

```bash
curl -X PUT "https://your-qualytics.qualytics.io/api/chat-sessions/{session_id}" \
  -H "Authorization: Bearer YOUR_QUALYTICS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"title": "Updated Title"}'
```

### Archive a Session

Soft-deletes a session. Archived sessions are read-only and can be restored.

```bash
curl -X DELETE "https://your-qualytics.qualytics.io/api/chat-sessions/{session_id}" \
  -H "Authorization: Bearer YOUR_QUALYTICS_TOKEN"
```

### Hard-Delete a Session

Permanently deletes a session. This cannot be undone.

```bash
curl -X DELETE "https://your-qualytics.qualytics.io/api/chat-sessions/{session_id}?archive=false" \
  -H "Authorization: Bearer YOUR_QUALYTICS_TOKEN"
```

The `archive` query parameter defaults to `true` (soft-delete). Pass `archive=false` for a permanent hard delete.

### Restore an Archived Session

```bash
curl -X PATCH "https://your-qualytics.qualytics.io/api/chat-sessions/{session_id}/restore" \
  -H "Authorization: Bearer YOUR_QUALYTICS_TOKEN"
```

## Specialized Workflow Endpoints

These endpoints execute guided multi-step AI workflows for specific data quality tasks. Each one calls the underlying workflow tool and returns an `AgentResponse` with step-by-step guidance.

### Transform Dataset

Create computed tables, files, or cross-datastore joins through natural language. Agent Q determines the correct asset type from the description.

```bash
curl -X POST "https://your-qualytics.qualytics.io/api/agent/transform-dataset" \
  -H "Authorization: Bearer YOUR_QUALYTICS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "asset_name": "daily_revenue_by_region",
    "container_name": "transactions",
    "datastore_name": "sales_db",
    "description": "Aggregate daily revenue by region from the transactions table, include only completed orders"
  }'
```

### Generate Quality Check

Create a data quality check by describing the business rule or validation expectation.

```bash
curl -X POST "https://your-qualytics.qualytics.io/api/agent/generate-quality-check" \
  -H "Authorization: Bearer YOUR_QUALYTICS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "datastore_name": "sales_db",
    "container_name": "customers",
    "description": "Ensure the email field is never null and matches a valid email format"
  }'
```

### Investigate Anomaly

Get AI-powered analysis of a specific data quality anomaly, including root cause context, business impact, and suggested remediation steps.

```bash
curl -X POST "https://your-qualytics.qualytics.io/api/agent/investigate-anomaly" \
  -H "Authorization: Bearer YOUR_QUALYTICS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"anomaly_identifier": 12345}'
```

`anomaly_identifier` accepts either a numeric ID or a UUID string.

### Analyze Trends

Analyze data quality trends, score patterns, and anomaly volume changes over time.

```bash
curl -X POST "https://your-qualytics.qualytics.io/api/agent/analyze-trends" \
  -H "Authorization: Bearer YOUR_QUALYTICS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "datastore_name": "sales_db",
    "container_name": "transactions",
    "timeframe": "month"
  }'
```

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `datastore_name` | string | Yes | Target datastore. |
| `container_name` | string | No | Scope to a specific container. |
| `field_name` | string | No | Scope to a specific field. |
| `timeframe` | string | No | `week`, `month`, `quarter`, or `year` (default: `month`). |

## LLM Configuration

### Get Configuration Status

Check whether an LLM provider is configured. Returns model name and web search enablement.

```bash
curl -X GET "https://your-qualytics.qualytics.io/api/agent/llm-config/status" \
  -H "Authorization: Bearer YOUR_QUALYTICS_TOKEN"
```

```json
{
  "is_configured": true,
  "model_name": "gpt-4o",
  "web_search_enabled": false
}
```

### Get Supported Models

Discover all available LLM providers and their supported models. This endpoint is the authoritative source for provider/model combinations.

```bash
curl -X GET "https://your-qualytics.qualytics.io/api/agent/supported-models" \
  -H "Authorization: Bearer YOUR_QUALYTICS_TOKEN"
```

```json
{
  "providers": [
    {
      "id": "openai",
      "name": "OpenAI",
      "example_models": ["gpt-4o", "gpt-4-turbo", "o1", "o3-mini"],
      "accepts_any_model": true,
      "requires_base_url": false
    }
  ]
}
```

### Get LLM Configuration

Retrieve the current LLM configuration. The API key is **never** returned.

```bash
curl -X GET "https://your-qualytics.qualytics.io/api/agent/llm-config" \
  -H "Authorization: Bearer YOUR_QUALYTICS_TOKEN"
```

### Create LLM Configuration

The API key is validated and the connection is tested before the configuration is stored.

```bash
curl -X POST "https://your-qualytics.qualytics.io/api/agent/llm-config" \
  -H "Authorization: Bearer YOUR_QUALYTICS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "model_name": "anthropic:claude-sonnet-4-20250514",
    "api_key": "YOUR_LLM_API_KEY"
  }'
```

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `model_name` | string | Yes | Provider and model in `provider:model` format (e.g., `openai:gpt-4o`, `anthropic:claude-sonnet-4-20250514`). |
| `api_key` | string | Yes | Your API key for the LLM provider. Stored encrypted. |
| `base_url` | string | No | Custom endpoint URL for OpenAI-compatible providers (Ollama, OpenRouter, LiteLLM). |

### Update LLM Configuration

Update any combination of fields. Omit `api_key` to keep the current key.

```bash
curl -X PATCH "https://your-qualytics.qualytics.io/api/agent/llm-config" \
  -H "Authorization: Bearer YOUR_QUALYTICS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"model_name": "openai:gpt-4o"}'
```

### Delete LLM Configuration

Removes the configuration and disables Agent Q until a new provider is configured.

```bash
curl -X DELETE "https://your-qualytics.qualytics.io/api/agent/llm-config" \
  -H "Authorization: Bearer YOUR_QUALYTICS_TOKEN"
```

## Rate Limits

For the complete limits reference — rate limits, token budgets, timeouts, and SQL constraints — see [Agent Q Limits](deep-dive/agent-q-limits.md){:target="_blank"}.

Exceeding the per-minute or concurrent limits returns `HTTP 429 Too Many Requests`. Token and request limits return an error message indicating the cost control was reached.
