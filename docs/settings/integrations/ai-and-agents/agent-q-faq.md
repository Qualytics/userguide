# Agent Q FAQ

Frequently asked questions about Agent Q, the AI assistant built into the Qualytics platform.

## General

### What is Agent Q?

Agent Q is the AI-powered assistant integrated into the Qualytics platform. It uses the Model Context Protocol (MCP) and your own LLM provider to interact with your data quality infrastructure through natural language. You can ask it to explore datastores, create quality checks, investigate anomalies, run operations, send notifications, create tickets, and more — without navigating complex interfaces.

### How does Agent Q work?

Agent Q connects to your configured LLM provider and uses a set of MCP tools to interact with the Qualytics platform on your behalf. When you send a message:

1. A lightweight topic classifier checks whether the request is related to data quality or the Qualytics platform.
2. The main agent processes your request using the LLM.
3. Agent Q dynamically discovers and selects the right tools for the task using `discover_tools`.
4. It executes those tools against the Qualytics API — calling them one at a time or in sequence as needed.
5. Results are streamed back to you in real time with per-step progress indicators.

### Is my data sent to the LLM?

Agent Q sends metadata about your data assets — table names, field names, quality check configurations, anomaly details — to the LLM to process your requests. It does **not** send actual row data unless you explicitly request a data preview. The LLM provider you configure handles this data according to their own privacy and data processing policies.

### Will Agent Q act on requests outside of data quality?

No. Agent Q includes an automatic topic guardrail. Before processing a request, a lightweight LLM classifier checks whether it relates to data quality, governance, databases, anomalies, transformations, or the Qualytics platform. Requests outside these topics are declined politely with a message explaining Agent Q's scope.

## Setup

### What LLM providers are supported?

Agent Q supports over 20 LLM providers including OpenAI, Anthropic, Google Gemini, Amazon Bedrock, Groq, Mistral, DeepSeek, Cohere, Ollama, OpenRouter, Perplexity, and more. See the full list with example models in the [Add Integration](managing/add-agent-q-integration.md#supported-llm-providers){:target="_blank"} guide.

### Do I need my own LLM API key?

Yes. Agent Q uses your own LLM API key to make calls to the language model. You choose the provider, select the model, and pay your own API costs. Qualytics does not supply LLM API keys.

### Is my API key validated when I save it?

Yes. When you create or update the LLM configuration, Qualytics makes a minimal test call to verify the API key and confirms connectivity to the provider before saving. You will see an error if the key is invalid or the provider is unreachable.

### What is the Base URL field for?

The **Base URL** is an optional custom endpoint for OpenAI-compatible providers that self-host or proxy models. Use it for providers like Ollama (local), OpenRouter, LiteLLM proxy, or any other provider that exposes an OpenAI-compatible API at a custom URL.

### Can Agent Q search the web?

If your configured LLM provider supports web search (e.g., certain OpenAI or Anthropic configurations), Agent Q can optionally use it to search the Qualytics documentation (userguide.qualytics.io) and related resources to answer questions about platform capabilities and best practices. This is detected automatically when you configure the integration.

### Can multiple users configure different LLM providers?

Yes. Each Qualytics user configures their own LLM provider independently. One user can use OpenAI while another uses Anthropic — both can use Agent Q simultaneously with their own configurations, API keys, and associated costs.

### What happens if I change my LLM provider?

Your conversation history is preserved when you switch providers — sessions are stored independently of the LLM configuration. The new provider takes effect immediately on the next message you send. Note that different models may behave differently for the same prompts, so results may vary after switching.

### What happens if I don't configure an LLM?

Without an LLM configured, Agent Q displays a "No LLM Integration Configured" message with a **Configure LLM** button. The platform is fully functional otherwise — only Agent Q's chat capabilities are unavailable. Follow the [Add Integration](managing/add-agent-q-integration.md){:target="_blank"} guide to get started.

## Usage

### How do I open Agent Q?

Two ways:

- Click **Agent Q** in the left sidebar for the full-page chat interface.
- Use the floating action button in the bottom-right corner of any page. Press the ++q++ key to toggle it from anywhere.

### What are the smart suggestions?

When you start a new conversation, Agent Q generates 3 personalized prompt suggestions using the LLM, based on your actual containers and active anomalies. These highlight common workflows like investigating anomalies, creating quality checks, and analyzing trends. Click any suggestion to use it as your opening message.

Suggestions are hidden when you open Agent Q from a page where context is already injected (e.g., from an anomaly page).

### How does context injection work?

When you open Agent Q from a page that has relevant data (a datastore, container, field, quality check, or anomaly), Agent Q automatically receives that asset's identity as context. This context appears as a badge above the input box (icon + asset name). You can then ask questions like *"Explain this anomaly"* or *"What checks exist here?"* without specifying which asset you mean.

The context is embedded in your first message using invisible Unicode markers and is visible to you via the **Context** action button on the message after it's sent.

### Can I have multiple conversations?

Yes. Agent Q supports full session management. You can start new conversations at any time, switch between sessions from the history sidebar or the floating chat dropdown, search sessions by title, and rename, archive, restore, or delete sessions.

### Does Agent Q remember previous conversations?

Yes. Each session maintains its full message history. For long sessions, Agent Q compresses context automatically:

- **Mechanical compression**: Recent messages (last 4 turns) are kept verbatim. Older messages are truncated to short summaries.
- **LLM-generated summary**: Once a session reaches 10 messages, the same LLM generates a structured summary capturing key topics, decisions, and context. This is stored with the session and used when resuming.

If you notice Agent Q losing context in a very long conversation, starting a new session for a fresh context window is the most reliable approach.

### What happens if I navigate away while Agent Q is generating?

The response continues streaming in the background. When you return to that session, the completed (or in-progress) response is waiting for you. You can see which sessions are still generating from the loading indicators in the session list.

### Can Agent Q make changes to my platform configuration?

Yes. Agent Q can create and update quality checks, create computed assets (tables, files, joins, fields), trigger operations (catalog, profile, scan, export, materialize), manage tags, send notifications, and create tickets. All changes are tracked in the audit trail and marked with **Agent Q co-authorship** alongside your user identity.

### Can I export Agent Q responses?

Yes. Click the **Export as PDF** button below any assistant message to download a formatted PDF. You can also copy any response to your clipboard.

### Are there usage limits?

Yes. To ensure fair usage and predictable costs:

| Limit | Default |
|-------|---------|
| Requests per minute | 10 per user |
| Concurrent streaming responses | 2 per user |
| LLM requests per execution | 100 |
| Input tokens per execution | 1,000,000 |
| Output tokens per execution | 500,000 |
| Total tokens per execution | 1,500,000 |

If you hit the rate limit, wait a moment and try again. If you consistently exceed token limits on a single request, try breaking it into smaller focused steps.

### What happens if Agent Q makes a mistake?

Ask it to fix the result in the same conversation. For example: *"That check is wrong — the field should be not-null, not unique. Please update it."* Agent Q will correct the action and update the platform accordingly.

If the change was already applied to the platform and you want to revert it, you can ask Agent Q to undo it (e.g., *"Delete the check you just created"*) or manually reverse it in the platform interface.

### How much does it cost to use Agent Q?

Agent Q uses your own LLM API key — you pay your LLM provider directly based on your usage. Qualytics does not charge separately for Agent Q. Costs depend on the model you choose and how many tool calls your requests generate.

To reduce costs, use specific, focused prompts and scope requests to a particular datastore or container rather than platform-wide queries. See [Best Practices](deep-dive/agent-q-best-practices.md){:target="_blank"} for detailed guidance.

### Can I share a conversation with another user?

Not directly — conversations are private to your user account. To share findings, use the **Export as PDF** button below any assistant message to download a formatted PDF you can share externally.

### How long are conversations stored?

Conversations persist indefinitely until you delete them. Archived conversations are also kept until explicitly deleted. See [Delete a Conversation](managing/delete-a-conversation.md){:target="_blank"} for instructions on permanent removal.

### What languages does Agent Q support?

Agent Q can understand and respond in any language your configured LLM model supports. The platform interface is in English, but you can write prompts in your preferred language and Agent Q will respond in kind.

## MCP Integration

### What is MCP?

The [Model Context Protocol](https://modelcontextprotocol.io/) is an open standard that enables AI assistants to securely connect to external data sources and tools. Qualytics implements an MCP server that exposes its data quality functionality to any compatible client.

### Can I connect external AI clients to Qualytics?

Yes. Beyond the built-in Agent Q, you can connect ChatGPT, Claude Desktop, Cursor, and any MCP-compatible client directly to the Qualytics MCP server using your Personal API Token. See the [Add Integration](managing/add-agent-q-integration.md#connecting-external-ai-clients){:target="_blank"} guide for step-by-step instructions for each client.

### What is the difference between Agent Q, the MCP server, and the Agentic API?

| Component | Purpose |
|-----------|---------|
| **Agent Q** | The built-in chat UI inside Qualytics. Full session management, context injection, streaming, PDF export. |
| **MCP Server** | An open-protocol endpoint. External clients (Claude Desktop, ChatGPT, Cursor) connect to it directly with your API token. |
| **Agentic API** | REST endpoints for integrating Agent Q capabilities into custom applications, scripts, and automation pipelines. |

All three use the same underlying MCP tools and capabilities — they differ only in how you access them.

### What tools are available?

Agent Q loads a core set of tools on every session and dynamically discovers additional tools using `discover_tools` as the conversation progresses. This keeps the token budget lean while making all capabilities available on demand.

| Category | Tools |
|----------|-------|
| **Exploration** | `list_datastores`, `list_containers`, `list_fields`, `global_search`, `preview_query` |
| **Transformations** | `create_computed_table`, `create_computed_file`, `create_computed_join`, `create_computed_field` |
| **Quality Checks** | `list_quality_check_specs`, `create_quality_check`, `update_quality_check`, `list_quality_checks` |
| **Anomalies** | `list_anomalies`, `anomaly_describe` |
| **Insights & Scores** | `quality_scores`, `get_insights`, `operation_insights` |
| **Operations** | `run_operation`, `get_operation_status` |
| **Integrations** | `send_notification`, `create_ticket`, `list_integrations`, `manage_tags` |
| **Workflows** | `workflow_analyze_trends`, `workflow_investigate_anomaly`, `workflow_interpret_quality_scores`, `workflow_generate_quality_check`, `workflow_transform_dataset` |
| **Meta** | `discover_tools` (dynamically discover and activate tools by capability) |

## Security

### Is Agent Q safe to use in production?

Yes. Agent Q includes multiple safety layers:

- **Topic guardrail**: A lightweight classifier rejects off-topic requests before they reach the main agent.
- **SQL injection protection**: Computed asset queries are validated — only `SELECT` statements and CTEs are permitted. INSERT/UPDATE/DELETE/DDL are blocked.
- **Prompt injection defense**: Tool output is sanitized to strip control characters before being passed to the LLM.
- **Token budget limits**: Tool results are truncated if they exceed 8,000 characters to prevent context flooding.
- **Co-authorship tracking**: All platform changes are audited with Agent Q attribution.
- **Rate limiting**: Per-user limits prevent runaway usage.
- **RBAC enforcement**: Agent Q respects the same permission model as the rest of the platform. It can only access what your user account is authorized to use.

## Troubleshooting

### Agent Q is not responding

- Verify your LLM configuration is active in **Settings** > **Integrations**.
- Check that your API key is valid and has sufficient credits with your provider.
- You may have hit the rate limit (10 requests/minute). Wait briefly and try again.
- If you exceeded a token limit, try breaking the request into smaller steps.

### I'm getting unexpected results

- Be specific about datastore and table names in your requests.
- Use the context injection feature — open Agent Q from the relevant page so it automatically knows which asset you mean.
- If Agent Q creates something incorrect, ask it to fix or update the result in the same conversation.
- For complex multi-step tasks, break them into sequential steps.

### Tool calls are failing

- Some operations require specific permissions. Verify your Qualytics user has the necessary access rights.
- If a datastore operation fails, confirm the Qualytics service account has access to that datastore.
- Click the tool step in the response to expand it and read the specific error in the **Output** section.

### The response was cut off mid-way

You may have hit a timeout (5-minute agent execution limit) or token limit for a single request. Try:

- Breaking the request into smaller, more focused prompts.
- Starting a fresh session and asking the same question with more specific context.
- Using a more capable model (e.g., GPT-4o or Claude Sonnet) if you're using a smaller model.

### Computed table/file/join quality checks fail immediately after creation

Computed assets require a profiling operation to complete before quality checks can be created on them. Agent Q handles this automatically by triggering a profile operation and polling until it finishes. If you're creating checks programmatically via the API, wait for the profile operation to reach `completed` status before creating checks.

### Smart suggestions are empty or not showing

Suggestions are generated based on your top 5 containers with active anomalies. If no anomalies exist in your datastores, suggestions may be generic or not appear. Run a scan on your datastores to generate anomalies, or simply type your request directly.

### My request was declined as off-topic

Agent Q's topic guardrail occasionally misclassifies edge-case requests. If your request is genuinely related to data quality or the Qualytics platform, try rephrasing it with more explicit context — for example, mention a specific datastore, container, or quality check in your message.
