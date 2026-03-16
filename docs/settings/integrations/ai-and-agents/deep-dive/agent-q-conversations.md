# Conversations, Responses & Context

This page covers how Agent Q processes your messages, what happens during a response, how context from your current page is injected automatically, and how long conversations are managed.

## Starting a Conversation

Type your request in the message box at the bottom of the chat and press ++enter++ to send it. Here are some examples of what you can ask:

| Task | Example Prompt |
| :--- | :--- |
| Explore data | *"What tables are in our sales database?"* |
| Create quality checks | *"Add a not-null check on the email field in the customers table"* |
| Investigate anomalies | *"Why did anomaly volume increase last week?"* |
| Build transformations | *"Create a computed table aggregating daily revenue by region"* |
| Validate queries | *"Check if this SQL is valid against our Snowflake warehouse"* |
| Analyze quality | *"Show the quality score trends for the last 30 days"* |
| Run operations | *"Run a profile scan on the orders container"* |
| Manage tags | *"Add the 'production' tag to the sales_db datastore"* |
| Send notifications | *"Send a Slack message summarizing today's anomalies"* |
| Create tickets | *"Open a Jira ticket for the null email anomalies"* |
| Get quality scores | *"What are the quality scores across the 8 dimensions for sales_db?"* |

!!! note
    Agent Q includes an automatic topic guardrail. Requests unrelated to data quality, governance, or the Qualytics platform will be politely declined. Short follow-ups like *"yes"* or *"that one"* are recognized as continuations of an on-topic conversation and pass through automatically. See [Agent Q Best Practices](./agent-q-best-practices.md){:target="_blank"} for more on the guardrail.

## Smart Suggestions

When you open a new conversation, Agent Q generates 3 personalized prompt suggestions based on your data assets. These are not static — they are generated dynamically each time by fetching your **top 5 containers with the highest active anomaly counts** and asking the LLM to produce short, actionable questions that demonstrate different capabilities.

Suggestions are designed around the 5 guided workflow tools: investigating anomalies, analyzing trends, interpreting quality scores, generating quality checks, and transforming datasets. Each suggestion is formatted with explicit container and datastore names so you can send it directly without editing.

Suggestions disappear once the conversation has messages, and reappear when you start a new session.

## Understanding Responses

When Agent Q processes your request, it shows real-time progress in three stages:

1. **Thinking** — Agent Q analyzes your message, decides which tools to call, and builds an execution plan.
2. **Tool Execution** — Each action appears as an expandable step labeled with the operation name (e.g., *Quality Scores*, *List Anomalies*, *Create Quality Check*). Click any step to see the exact input parameters sent and the raw output returned.
3. **Response** — The final answer is rendered in Markdown with tables, code blocks, and formatted text as appropriate.

You can continue the conversation to refine results, ask follow-up questions, or request additional actions.

### Tool Step Labels

The step labels you see during a response correspond to specific platform operations:

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

### Message Actions

Each message includes action buttons:

| Action | Description |
| :--- | :--- |
| **Copy** | Copy the full response content to your clipboard. |
| **Export as PDF** | Download the response as a formatted PDF (assistant messages only, not available while streaming). |
| **Context** | View the injected context that was included with your message (user messages only, when context was present). |

## Context-Aware Conversations

Agent Q automatically detects the page you are on and injects the relevant asset context into the conversation. This means you can ask direct questions without repeating which datastore, container, or anomaly you mean.

| Page You're On | What Agent Q Receives | Example You Can Ask |
| :--- | :--- | :--- |
| **Datastore** | Datastore name + ID | *"What containers are in here?"* |
| **Container** | Container name + ID | *"Create a completeness check on the amount field"* |
| **Field Profile** | Field name + ID | *"What quality checks exist for this field?"* |
| **Quality Check** | Rule type + ID | *"Why is this check failing?"* |
| **Anomaly** | Anomaly ID | *"Explain this anomaly and suggest a fix"* |

The injected context appears as a badge above the input box (icon + asset name) before you send your message. You can always see what context Agent Q is working with.

!!! tip
    Use the floating chat widget when investigating a specific anomaly or container — open it from that page and Agent Q automatically knows which asset you are referring to without you having to name it.

## Long Conversations & Memory

Agent Q automatically manages conversation length to keep the context window efficient without losing important history.

### How Compression Works

1. The last **4 turns** (user + assistant pairs) are always kept verbatim in full detail.
2. Older turns are mechanically summarized to ~3,000 characters.
3. Once a session reaches **10 messages**, the LLM generates a structured summary (~800 tokens) that is stored with the session and used on all subsequent turns.
4. Tool results older than the last 2 user messages are truncated to 300 characters — large outputs like a full container list are not re-sent on every turn.

This means information from early in a long conversation is not lost — it is summarized and remains available to Agent Q throughout the session.

### Background Streaming

If you navigate away from the Agent Q page while a response is being generated, the stream continues in the background. The full response is waiting for you when you return to that session.

For other interface tips like stopping a response or pasting large content, see [Chat Interface Tips](../managing/chat-interface-tips.md){:target="_blank"}.

### Session Persistence

Every conversation is persisted. When you resume a session, Agent Q restores the full message history, the activated tool set, and the conversation summary — so it picks up exactly where you left off, even across days or sessions.

For step-by-step instructions on resuming a session, see [Resume a Conversation](../managing/resume-a-conversation.md){:target="_blank"}.

## Example Conversations

### Investigating a Data Quality Alert

> **You**: We got an alert about anomalies in the transactions table. What's going on?
>
> **Agent Q**: I found 3 anomalies from the last scan. The most significant is a "Not Null" check failure on the `merchant_id` field — 247 records have null values where this field is expected to be populated. This started appearing after the batch that loaded at 2:00 AM. The affected records all have source_system = 'legacy_import'. Would you like me to show you the specific check that's failing or help investigate the source of these null values?

### Setting Up Quality Monitoring for a New Dataset

> **You**: We just connected a new PostgreSQL database called "ecommerce_prod". Can you help me understand what's in there and set up some basic quality checks?
>
> **Agent Q**: I found 12 tables in the ecommerce_prod datastore. The main ones appear to be `customers`, `orders`, `order_items`, `products`, and `inventory`. Would you like me to describe the schema for any of these in detail?
>
> **You**: Yes, tell me about the orders table and suggest some quality checks.
>
> **Agent Q**: The orders table has 15 fields including order_id, customer_id, order_date, ship_date, status, and total_amount. Based on the schema, I'd recommend these quality checks:
>
> - order_id should be unique
> - customer_id should not be null
> - total_amount should be positive
> - ship_date should be after order_date when both are present
> - status should be one of your valid status values
>
> Want me to create these checks?

### Building Cross-System Analytics

> **You**: I need to analyze customer lifetime value but our customer data is in Salesforce (synced to Snowflake) and our transaction data is in our PostgreSQL operational database. Can you help?
>
> **Agent Q**: I can create a computed join that combines data from both sources. I'll join the customer table from your Snowflake datastore with the transactions table from PostgreSQL on customer_id. What fields do you need in the result? At minimum I'd suggest customer details, total transaction count, total spend, and first/last transaction dates.
>
> **You**: That sounds right. Also filter out any test customers.
>
> **Agent Q**: I've created a computed join called "customer_lifetime_value" that combines the data and excludes records where the customer email contains "test" or the customer_type is "internal". The join is now available as a container in Qualytics. Would you like me to set up quality checks on this new dataset or run a profile to understand the data distribution?
