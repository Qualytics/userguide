# Agent Q Best Practices

This page covers how to get the most out of Agent Q — writing effective prompts, managing costs, understanding guardrails, and structuring complex workflows.

## Prompt Design

### Be Specific About Assets

Agent Q resolves asset references by name. The more specific you are, the faster it locates the right datastore, container, or field — and the fewer tool calls it needs to make.

| Instead of... | Use... |
| :--- | :--- |
| *"Check my main table"* | *"Check the `orders` table in the `ecommerce_prod` datastore"* |
| *"Fix the data quality issues"* | *"Create a not-null check on the `customer_id` field in the `orders` container"* |
| *"Show me anomalies"* | *"List active anomalies in the `transactions` container in `sales_db`"* |

When a container or datastore name is ambiguous, Agent Q calls `list_datastores` then `list_containers` to resolve it. Providing the full path up front skips those steps entirely.

### Describe Business Intent, Not Just Operations

Agent Q works best when you describe *what you want to achieve*, not just the technical operation. It translates intent into the appropriate rule type and parameters automatically.

- **Good**: *"Make sure order totals are always positive and under 1,000,000"*
- **Verbose and unnecessary**: *"Create a `between` rule on the `total_amount` field with min 0 and max 1000000"*

### Use Context Injection

Open Agent Q from the relevant page — a datastore, container, field profile, quality check, or anomaly — and it automatically injects that asset's context into the conversation. You can then ask direct questions without repeating the asset name.

The injected context appears as a badge above the input box so you always know what Agent Q is working with.

### Break Down Complex Tasks

Each conversation has a limit of **50 LLM tool-call requests**. For complex, multi-step workflows, split them into sequential messages rather than one large request.

- **Good**: *"First, show me quality scores for `sales_db`. [wait for response] Now create checks for any container scoring below 80."*
- **Risky**: *"Analyze all 12 containers in `sales_db`, create quality checks for each, run scans, then send a Slack summary."*

### Use Workflow Tools for Complex Tasks

Agent Q has 5 guided workflow tools that handle multi-step operations reliably. These are preferred over ad-hoc combinations of raw tools:

| Workflow | Best For |
| :--- | :--- |
| `workflow_generate_quality_check` | Creating checks from a natural language business rule |
| `workflow_transform_dataset` | Creating computed assets (auto-routes to table, file, or join) |
| `workflow_investigate_anomaly` | Deep-dive root cause analysis on a specific anomaly |
| `workflow_analyze_trends` | Quality score and anomaly volume trend analysis |
| `workflow_interpret_quality_scores` | Understanding 8-dimension scores in business terms |

Just describe what you want — Agent Q selects the right workflow automatically.

## Cost Management

Agent Q uses your own LLM API key, so every request has a real cost. Here is how to keep usage efficient.

### Understand What Drives Token Usage

Each conversation accumulates tokens from:

- **System prompt** — always present (~2,000 tokens)
- **Tool schemas** — each active tool description (~100–400 tokens each)
- **Conversation history** — compressed automatically after 4 turns
- **Tool results** — each response from a tool call (capped at ~8,000 chars)

### How Compression Works

Agent Q automatically manages long conversations to minimize token usage:

1. The last **4 turns** (user + assistant pairs) are kept verbatim.
2. Older turns are mechanically summarized to ~3,000 characters.
3. Once a session reaches **10 messages**, an LLM-generated structured summary (~800 tokens) is stored and used on all subsequent turns.
4. Tool results older than the last 2 user messages are truncated to 300 characters — so large outputs (e.g., 100 containers × 50 fields) are not re-sent on every turn.

This reduces cumulative token usage significantly on long conversations without losing important context.

### Tips to Reduce Unnecessary Tool Calls

- **Use `global_search`** with specific keywords instead of chaining `list_datastores` → `list_containers` → `list_fields` — it's faster and cheaper.
- **Provide explicit filters**: ask to list specific containers by name rather than listing all of them.
- **Avoid requesting entire tables**: tool results are capped at ~8,000 characters anyway; asking for 10,000 rows just triggers truncation.
- **Use `preview_query` before creating computed assets** to validate your SQL, rather than creating and deleting repeatedly.

### Dynamic Tool Loading

Agent Q starts each session with only a small set of core tools loaded. As the conversation progresses, it calls `discover_tools` to activate additional tools based on what you're asking for. This keeps the initial context window small and startup fast.

Tools stay activated for the rest of the session. New sessions reset to core tools only.

## Topic Guardrail

Agent Q includes an automatic guardrail that declines requests unrelated to data quality, governance, or the Qualytics platform.

### What Is Allowed

Any request related to:

- Data quality, governance, management, or engineering
- Databases, datastores, tables, fields, schemas, or profiling
- Anomalies, quality checks, validation, or observability
- Transformations, ETL, computed datasets, or SQL
- Trends, metrics, insights, or quality scores
- Qualytics platform features and operations
- General greetings or help requests about Agent Q itself

### What Gets Blocked

Requests clearly outside the data quality domain — for example, asking Agent Q to write creative content, answer general knowledge questions, or perform tasks unrelated to your data infrastructure.

### How Follow-Ups Are Handled

The guardrail includes up to 2,000 characters of prior conversation context when evaluating a new message. This means short follow-ups like *"yes"*, *"that one"*, or *"the second datastore"* are automatically recognized as continuations of an on-topic conversation and pass through without being blocked.

## Rate Limits & Concurrency

| Limit | Value |
| :--- | :--- |
| Requests per minute (per user) | 10 |
| Concurrent requests (per user) | 2 |
| Max tool calls per request | 50 |
| Agent execution timeout | 5 minutes |

If you receive a `429 Too Many Requests` error, you have exceeded the per-minute rate limit. Wait a moment and retry.

If you hit a "Usage limit exceeded" error mid-conversation, you have reached the 50 tool-call limit for a single request. Break the remaining work into a new message.

Avoid opening more than 2 Agent Q chat windows simultaneously — only 2 concurrent requests are allowed per user.

For the full list of all limits and constraints, see [Agent Q Limits](./agent-q-limits.md){:target="_blank"}.

## Async Operations

When Agent Q triggers an operation (profile, scan, catalog, etc.), it runs asynchronously. Agent Q automatically polls `get_operation_status` until the operation reaches a terminal state (completed, failed, or cancelled) before proceeding with dependent steps.

This means you can ask Agent Q to **create and validate** in a single message:

> *"Create a computed table joining `customers` and `orders` on `customer_id`, then profile it and create quality checks for the key fields."*

Agent Q will: create the computed table → trigger a profile operation → poll until complete → create quality checks on the profiled fields. You do not need to wait or send follow-up messages.
