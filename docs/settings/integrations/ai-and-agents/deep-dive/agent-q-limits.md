# Agent Q Limits

Agent Q enforces limits at multiple layers to ensure fair usage, predictable costs, and platform stability. This page documents every constraint with exact values.

## Rate Limits

Rate limiting is applied per authenticated user using a token bucket algorithm.

| Limit | Default |
| :--- | :--- |
| Requests per minute | 10 |
| Concurrent streaming sessions | 2 |

Exceeding either limit returns `HTTP 429 Too Many Requests`. These limits apply equally to the built-in Agent Q chat and to the REST API.

!!! note
    Rate limiting is in-memory and per-pod. In multi-replica deployments, effective limits scale with the number of replicas.

## Tokens and Usage

Every user message can trigger multiple LLM calls as the agent reasons, calls tools, and processes results. Token counts accumulate across all LLM calls within a single execution.

**What consumes tokens in a single execution:**

1. **System prompt** — loaded once per execution (~2,000 tokens)
2. **Tool schemas** — each active tool description (100–400 tokens each)
3. **Conversation history** — all prior messages, subject to compression for long sessions
4. **Tool inputs** — parameters sent to each tool call
5. **Tool outputs** — results from each tool, capped at 8,000 characters per result
6. **LLM response** — text and reasoning generated on each step, capped at 4,000 tokens per individual LLM call

**Per-execution limits:**

| Limit | Value |
| :--- | :--- |
| LLM API requests per execution | 50 |
| Input tokens per execution | 1,000,000 |
| Output tokens per execution | 500,000 |
| Total tokens per execution | 1,500,000 |
| Max tokens per individual LLM call | 4,000 |

These limits apply per user message (or per API call). Exceeding them returns an error indicating which limit was reached.

## Timeouts

Timeouts are layered for defense-in-depth:

| Layer | Timeout | Description |
| :--- | :--- | :--- |
| Individual LLM API request | 120 seconds | Per call to the LLM provider |
| Agent execution | 300 seconds (5 min) | Full `agent.run()` including all tool calls |
| HTTP route handler | 360 seconds (6 min) | Outer safety net on the HTTP request |

If the agent execution timeout is reached, the agent stops and returns whatever it produced up to that point. For long-running tasks, break them into smaller sequential requests.

## Tool Output Truncation

Individual tool results are truncated at **8,000 characters** before being passed to the LLM. This prevents a single large result (e.g., a container with hundreds of fields) from consuming the entire context window.

**Truncation strategy:**

1. The largest list/array fields in the result are trimmed first, iteratively, up to 20 iterations.
2. Each list is reduced to at most 5 items (or half the original length, whichever is smaller).
3. A truncation note is appended to the result so Agent Q knows data was cut off.

**History truncation:**

Tool results from turns older than the last 2 user messages are further truncated to **300 characters** in the conversation history. This prevents large outputs from earlier in the conversation from re-consuming tokens on every subsequent turn.

Tool output metadata stored in the database is also truncated to **500 characters** to keep metadata columns lean.

## Conversation Context and Compression

| Parameter | Value |
| :--- | :--- |
| Recent turns kept verbatim | 4 turns (user + assistant pairs) |
| LLM summary trigger | 10 messages |
| Max summary length | 3,000 characters |
| User message truncation (mechanical summary) | 100 characters |
| Assistant message truncation (mechanical summary) | 150 characters |

Compression works in two stages:

1. **Mechanical compression** — Turns beyond the most recent 4 are summarized mechanically: user messages truncated to 100 chars, assistant messages to 150 chars, tool interactions to 100 chars.
2. **LLM-generated summary** — Once a session reaches 10 messages, the LLM generates a structured summary (up to 3,000 chars) stored with the session and used on all subsequent turns instead of the full history.

Starting a new session resets the context window entirely — the most reliable option for very long or unrelated workflows.

## SQL Constraints

The `preview_query` tool and all computed asset SQL inputs only accept `SELECT` statements and CTEs (`WITH` clauses).

**Blocked statements:**

| Statement | Blocked |
| :--- | :--- |
| `INSERT` | Yes |
| `UPDATE` | Yes |
| `DELETE` | Yes |
| `DROP` | Yes |
| `CREATE` | Yes |
| `ALTER` | Yes |
| `TRUNCATE` | Yes |

These are blocked at the API level regardless of what the LLM generates.

**Non-deterministic function warnings:**

Agent Q generates a warning (but does not block) when SQL contains non-deterministic functions such as `NOW()`, `CURRENT_TIMESTAMP`, `RANDOM()`, and similar. This is because computed assets are expected to produce consistent, reproducible results.

**Query execution timeout:** 30 seconds by default (range: 5–150 seconds).

## Scope Constraints

**Datastore types for computed assets:**

| Asset Type | Supported Datastores |
| :--- | :--- |
| Computed Table | JDBC datastores (PostgreSQL, Snowflake, BigQuery, MySQL, etc.) |
| Computed File | DFS datastores (S3, ADLS, GCS) |
| Computed Join | Any combination of JDBC and/or DFS |

**RBAC enforcement:**

Agent Q operates strictly within your user account's permissions. It cannot access datastores, containers, or fields that your role does not permit, and cannot trigger operations (profile, scan, export) beyond your permission scope.

**Web search (if enabled):**

When web search is enabled for your LLM configuration, Agent Q's search is restricted to the following domains only:

- `userguide.qualytics.io`
- `qualytics.com`
- `qualytics.ai`

**Session ownership:**

Users can only access their own chat sessions. Administrators can access any user's session via the API using an optional `user_id` parameter.

## Discovery and Listing Limits

These are the default limits for tool calls that list platform assets. They can be adjusted within the allowed range per call.

| Tool | Default Limit | Max |
| :--- | :--- | :--- |
| `list_datastores` | 50 | 200 |
| `list_containers` | 100 | 500 |
| `list_fields` | 200 | 500 |
| `discover_tools` results | 8 tools | — |
| Containers fetched for suggestions | 5 | — |

## Input Limits

| Parameter | Value |
| :--- | :--- |
| Paste threshold (triggers attachment mode) | 200 characters |
| Guardrail bypass threshold (very short messages) | 5 characters |

Messages shorter than 5 characters (e.g., *"hi"*, *"yes"*) bypass the topic guardrail classifier entirely for speed. Messages of 200 characters or more pasted into the input are captured as an attachment panel rather than inserted inline.

## Error Reference

| Error | Cause |
| :--- | :--- |
| `HTTP 429 Too Many Requests` | Exceeded 10 requests/min or 2 concurrent sessions |
| `Usage limit exceeded` | Hit 50 LLM requests, 1M input tokens, 500K output tokens, or 1.5M total tokens in a single execution |
| `Agent execution timed out` | Agent ran for more than 5 minutes |
| `SQL not allowed` | Attempted INSERT, UPDATE, DELETE, or DDL in a query |
