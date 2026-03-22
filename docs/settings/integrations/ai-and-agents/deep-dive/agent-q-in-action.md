# Agent Q in Action

Qualytics implements the [Model Context Protocol (MCP)](./mcp.md){:target="_blank"} as a server that exposes its entire data quality infrastructure as callable tools. This page covers the endpoint, authentication, available capabilities, and example conversations — everything you need to understand how Agent Q and external MCP clients interact with the Qualytics platform.

!!! info
    Agent Q enforces limits on rate, tokens, timeouts, and query types to ensure fair usage and platform stability. See [Agent Q Limits](./agent-q-limits.md){:target="_blank"} for full details.

## Endpoint

The MCP service is available at your Qualytics instance URL:

```
https://your-qualytics-instance.qualytics.io/mcp
```

## Authentication

The MCP service uses the same authentication mechanism as the Qualytics API. You'll need a Personal API Token (PAT) to authenticate requests. Include it in the `Authorization` header:

```
Authorization: Bearer YOUR_API_TOKEN
```

To generate a token, navigate to **Settings** > **Tokens** and click **Generate Token**. For detailed instructions, see [Tokens](../../../tokens/overview-of-tokens.md){:target="_blank"}.

## Capabilities

This video demonstrates the power of one-shot prompting using the Qualytics MCP server:

<div style="position: relative; padding-bottom: 56.25%; height: 0;"><iframe src="https://www.loom.com/embed/4b204d88eef6467aa3548fb1d9847710" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

### Datastore Exploration

When you connect an AI assistant to Qualytics via MCP, it gains the ability to explore your data landscape and understand the structure of your datastores:

- *"What tables are in our sales database?"*
- *"Show me the schema for the customer_orders table"*
- *"What fields are available in the transactions container?"*

### Data Transformations

Create computed assets through conversation instead of manually configuring them in the UI:

- **Computed Tables (JDBC)** — SQL queries stored and executed in the source database using its native dialect.
- **Computed Files (DFS)** — Spark SQL transformations over file-based sources like S3, ADLS, or GCS.
- **Cross-Datastore Joins** — Join data across completely different systems (Snowflake + PostgreSQL, BigQuery + S3) executed in Spark.
- **Computed Fields** — Add derived or type-cast fields to existing containers using custom expressions.

### Quality Check Management

Create and manage data quality checks through natural conversation:

- *"Make sure the email field in the customers table is never null"*
- *"Add a check that order_total is always between 0 and 1,000,000"*
- *"Verify that ship_date is always after order_date"*

The AI translates your intent into the appropriate rule type and parameters automatically.

### Anomaly Investigation

Investigate quality issues conversationally:

- *"Tell me about the anomalies found in yesterday's scan"*
- *"What's wrong with anomaly 12345?"*
- *"Explain the business impact of the data quality issues in the orders table"*

### Operations, Notifications, and Ticketing

Beyond analysis, Agent Q can take action on your behalf:

- **Run operations** — Trigger catalog, profile, scan, export, or materialize operations and poll for completion.
- **Send notifications** — Post alerts to Slack, Microsoft Teams, Email, Webhook, or PagerDuty.
- **Create tickets** — Open issues in Jira or ServiceNow, optionally linked to a specific anomaly.
- **Manage tags** — Add, remove, or replace tags on datastores, containers, fields, and quality checks.

## Tool Step Labels

When Agent Q processes a request, each action appears as an expandable step in the response. The labels correspond to specific platform actions:

| Step Label | What It Does |
| :--- | :--- |
| Discovery | Searches available tools for your request |
| Search | Queries across datastores, containers, and fields |
| List Quality Checks | Retrieves existing checks on a container |
| List Check Specifications | Fetches available rule types and their schemas |
| Create Quality Check | Creates a new quality check rule |
| Update Quality Check | Modifies an existing quality check |
| Quality Scores | Retrieves 8-dimension quality scores |
| Get Insights | Retrieves daily metrics time series |
| Operation Insights | Retrieves historical operation data |
| Describe Anomaly | Gets full details for a specific anomaly |
| Workflow | Executes a guided multi-step workflow |

## Available Tools

Agent Q and external MCP clients share the same tool set. Agent Q loads a core subset on every session and dynamically discovers additional tools using `discover_tools` as the conversation progresses.

### Exploration

| Tool | Description |
|------|-------------|
| `list_datastores` | List all datastores. Accepts optional `search` (filter by name) and `tags` (filter by tag names). Returns paginated datastore summaries with IDs, names, and types. |
| `list_containers` | List containers within a datastore. Requires `datastore_id`. Accepts optional `search` and `tags` filters. Returns container names, types, and IDs. |
| `list_fields` | List fields within a container. Requires `container_id`. Returns field names, data types, and profile metadata (min, max, null count, distinct count). |
| `global_search` | Search across all datastores, containers, and fields by name. Returns ranked results with entity type and IDs. Use when the user doesn't know exactly where something lives. |
| `preview_query` | Execute a `SELECT` query against a JDBC datastore with an automatic `LIMIT 100`. Returns the result set as a markdown table. Only `SELECT` statements and CTEs are permitted — INSERT/UPDATE/DELETE/DDL are blocked. |

### Quality Checks

| Tool | Description |
|------|-------------|
| `list_quality_check_specs` | List all available quality check rule types and their JSON schemas. Use this before `create_quality_check` to discover valid rule types and required parameters. |
| `list_quality_checks` | List quality checks on a container or field. Accepts `container_id` or `field_id`. Returns rule type, status, filter expression, and field assignments. |
| `create_quality_check` | Create a new quality check rule. Requires `container_id`, `rule_type`, and `field` assignments. Accepts optional `filter` expression and `description`. |
| `update_quality_check` | Update an existing quality check. Requires `check_id`. Accepts any subset of fields to update (rule parameters, description, filter, field assignments). |

### Data Transformation

| Tool | Description |
|------|-------------|
| `create_computed_table` | Create a computed table in a JDBC datastore. Requires `datastore_id`, `name`, and `sql` (a `SELECT` statement in the datastore's native SQL dialect). The SQL is validated before creation. |
| `create_computed_file` | Create a computed file in a DFS datastore. Requires `datastore_id`, `name`, and `sql` (Spark SQL). The result is written as a file container that can be profiled and scanned. |
| `create_computed_join` | Create a cross-datastore join. Requires `name`, `left_datastore_id`, `left_container_id`, `right_datastore_id`, `right_container_id`, `join_type` (`inner`, `left`, `right`, `full`), and `join_condition` (SQL expression). Executes in Spark. |
| `create_computed_field` | Add a computed field to an existing container. Requires `container_id`, `field_name`, `expression` (SQL expression), and `data_type`. Accepts optional `description`. |

### Anomalies

| Tool | Description |
|------|-------------|
| `list_anomalies` | List anomalies with flexible filtering. Accepts `datastore_id`, `container_id`, `status` (`active`, `acknowledged`, `resolved`), `check_id`, and pagination parameters. |
| `anomaly_describe` | Get full details for a single anomaly. Requires `anomaly_id` (numeric ID or UUID). Returns the failed check configuration, affected field, record count, sample values, and AI-generated description. |

### Insights & Scores

| Tool | Description |
|------|-------------|
| `quality_scores` | Retrieve quality scores across the 8 dimensions (completeness, coverage, conformity, consistency, precision, timeliness, volumetrics, accuracy). Accepts optional `datastore_id` or `container_id` to scope the query. Returns current scores and trend direction. |
| `get_insights` | Retrieve daily time-series metrics for an asset. Accepts `datastore_id` or `container_id` and a `timeframe` (`week`, `month`, `quarter`, `year`). Returns anomaly counts, quality score changes, and scan coverage over time. |
| `operation_insights` | Retrieve historical operation data for an asset. Returns operation types, durations, record counts, and completion statuses over time. |

### Operations & Integrations

| Tool | Description |
|------|-------------|
| `run_operation` | Trigger an operation on a datastore or container. Requires `datastore_id` and `operation_type` (`catalog`, `profile`, `scan`, `export`, `materialize`). Accepts optional `container_ids` to scope to specific containers. Returns the operation ID. |
| `get_operation_status` | Poll the status of a running operation. Requires `operation_id`. Returns `running`, `completed`, `failed`, or `cancelled` along with progress details. Agent Q uses this to wait for profile completion before creating quality checks on new computed assets. |
| `send_notification` | Send an alert via a configured notification channel. Requires `integration_id` and `message`. Supports Slack, Microsoft Teams, Email, Webhook, and PagerDuty channels. |
| `create_ticket` | Create a ticket in a configured ticketing integration. Requires `integration_id`, `title`, and `description`. Accepts optional `anomaly_id` to link the ticket to a specific anomaly. Supports Jira and ServiceNow. |
| `list_integrations` | List all configured notification and ticketing integrations. Returns integration IDs, names, and types. Use this before `send_notification` or `create_ticket` to discover available channels. |
| `manage_tags` | Add, remove, or replace tags on an asset. Requires `entity_type` (`datastore`, `container`, `field`, `quality_check`), `entity_id`, `action` (`add`, `remove`, `replace`), and `tags` (array of tag names). |

### Guided Workflows

Workflow tools execute multi-step guided processes for complex tasks. Each returns a structured `AgentResponse` with step-by-step results.

| Tool | Description |
|------|-------------|
| `workflow_analyze_trends` | Analyze quality score trends and anomaly volume patterns over time. Accepts `datastore_name`, optional `container_name` and `field_name`, and `timeframe`. Combines `get_insights` and `quality_scores` into a coherent trend report. |
| `workflow_investigate_anomaly` | Perform a full AI-assisted investigation of an anomaly. Accepts `anomaly_identifier` (ID or UUID). Returns root cause context, business impact assessment, and remediation suggestions. |
| `workflow_interpret_quality_scores` | Interpret 8-dimension quality scores in business terms. Accepts `datastore_name` and optional `container_name`. Explains what each score means and highlights areas for improvement. |
| `workflow_generate_quality_check` | Generate and create a quality check from a natural language description. Accepts `datastore_name`, `container_name`, and `description` (the business rule). Selects the appropriate rule type and parameters automatically. |
| `workflow_transform_dataset` | Create a computed asset from a natural language description. Accepts `asset_name`, `container_name`, `datastore_name`, and `description`. Agent Q determines whether to create a computed table, file, or join based on the datastore types involved. |

### Meta

| Tool | Description |
|------|-------------|
| `discover_tools` | Dynamically discover and activate tools by capability keyword. Accepts a `query` string (e.g., `"notifications"`, `"ticket"`, `"tag"`). Returns matching tool names and descriptions, and activates them for use in the current session. Agent Q calls this automatically when it needs a capability not yet loaded. |

## Connecting External Clients

For step-by-step instructions on connecting ChatGPT, Claude Desktop, Cursor, and other MCP-compatible clients to the Qualytics MCP server, see [Connecting External AI Clients](../managing/connecting-external-ai-clients.md){:target="_blank"}.

For example conversations showing Agent Q in use, see [Conversations, Responses & Context](./agent-q-conversations.md#example-conversations){:target="_blank"}.
