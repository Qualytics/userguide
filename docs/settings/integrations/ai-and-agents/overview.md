# AI & Agents Overview

The AI & Agents section of Qualytics brings artificial intelligence directly into your data quality workflows. Whether you prefer interacting through natural language inside the platform, connecting your favorite AI tools via the Model Context Protocol, or integrating AI capabilities into your own pipelines through REST APIs, Qualytics provides flexible options to accelerate every aspect of data quality management.

## Agent Q

Agent Q is the AI assistant built into the Qualytics platform. Powered by the Model Context Protocol (MCP) and your choice of LLM provider, Agent Q turns natural language into action — exploring datastores, building transformations, creating quality checks, investigating anomalies, and more.

### How You Can Interact

| Method | Description |
| :--- | :--- |
| **Full-Page Chat** | Click **Agent Q** in the left sidebar to open the dedicated full-page chat interface. This view includes a collapsible chat history sidebar on the left and the main chat area on the right. |
| **Floating Chat** | A persistent widget in the bottom-right corner of every page. Click it or press ++q++ to toggle it. Agent Q automatically knows what page you're on and injects that context into the conversation. To minimize without closing, hover over the button for 2 seconds — a shrink badge appears. |
| **REST API** | Programmatic access to all Agent Q capabilities through standard REST endpoints for custom integrations and automation. |
| **External MCP Clients** | Connect tools like Claude Desktop, ChatGPT, and Cursor directly to the Qualytics MCP server. |

### Key Capabilities

| Capability | Description |
| :--- | :--- |
| **Datastore Exploration** | Discover and understand your data assets — list datastores, containers, fields, and preview data through conversation. |
| **Data Transformations** | Create computed tables (SQL), computed files (Spark SQL), cross-datastore joins, and computed fields using natural language. |
| **Quality Check Management** | Create, update, and manage data quality checks by describing business rules in plain language. |
| **Anomaly Investigation** | Investigate data quality issues with AI-assisted analysis, impact assessment, and remediation suggestions. |
| **Trend Analysis** | Analyze data quality trends, quality scores, and patterns over time. |
| **Operations** | Trigger catalog, profile, scan, export, and materialize operations directly from chat. |
| **Notifications & Ticketing** | Send alerts via Slack, Teams, Email, Webhook, or PagerDuty. Create tickets in Jira or ServiceNow. |
| **Tag Management** | Add, remove, and manage tags on datastores, containers, fields, and quality checks. |

### Built-In Intelligence

- **Smart Suggestions** — When you start a new conversation, Agent Q generates personalized prompt suggestions based on your data assets and common workflows.
- **Context Awareness** — Agent Q automatically detects the page you're on and injects relevant context (datastore, container, field, check, or anomaly) into the conversation.
- **Co-Authorship Tracking** — All changes made through Agent Q are stamped with a co-author record in the audit trail, so you always know which actions were AI-assisted.
- **Conversation Memory** — Long conversations are automatically managed through context compression, keeping recent messages in full detail while summarizing older context. See [Conversations, Responses & Context](deep-dive/agent-q-conversations.md) for details.
- **Background Streaming** — If you navigate away while Agent Q is generating, the stream continues in the background. The response is waiting when you return to that session.
- **PDF Export** — Export any Agent Q response as a PDF for sharing and reporting.

## Deep Dive

| Section | Description |
| :--- | :--- |
| [MCP](deep-dive/mcp.md) | What is the Model Context Protocol — how it works, key concepts, and why it matters. |
| [Agent Q in Action](deep-dive/agent-q-in-action.md) | How Qualytics implements MCP — endpoint, tools, and tool step labels. |
| [Conversations, Responses & Context](deep-dive/agent-q-conversations.md) | How to write prompts, understand Agent Q responses, and use context-aware conversations. |
| [Best Practices](deep-dive/agent-q-best-practices.md) | Prompt design, cost management, guardrail behavior, rate limits, and async operation patterns. |
| [Agent Q Limits](deep-dive/agent-q-limits.md) | Rate limits, token usage, timeouts, SQL constraints, and scope constraints. |
| [Agentic API](deep-dive/agentic.md) | Building custom applications with the Agentic API — integration patterns, best practices, and code examples. |

## Managing

| Task | Description |
| :--- | :--- |
| [Connecting External AI Clients](managing/connecting-external-ai-clients.md) | Connect ChatGPT, Claude Desktop, Claude Code, Cursor, VS Code, Windsurf, or Amazon Q Developer to the Qualytics MCP server. |
| [Add Integration](managing/add-agent-q-integration.md) | Configure your LLM provider to power Agent Q's built-in chat. |
| [Update Agent Q Integration](managing/update-agent-q-integration.md) | Change your LLM provider, model, or API key. |
| [Remove Agent Q Integration](managing/remove-agent-q-integration.md) | Disconnect your LLM provider from Agent Q. |
| [Start a New Conversation](managing/start-a-new-conversation.md) | Create a fresh chat session from the sidebar, chat header, or floating chat. |
| [Resume a Conversation](managing/resume-a-conversation.md) | Return to a previous session and continue from where you left off. |
| [Rename a Conversation](managing/rename-a-conversation.md) | Give a session a descriptive title for easier navigation. |
| [Archive a Conversation](managing/archive-a-conversation.md) | Move a session out of the active list into the archived section. |
| [Restore a Conversation](managing/restore-a-conversation.md) | Bring an archived session back to the active list. |
| [Delete a Conversation](managing/delete-a-conversation.md) | Permanently remove an archived session. |
| [Search Conversations](managing/search-conversations.md) | Filter active sessions by title or message content to find a specific conversation. |
| [Chat Interface Tips](managing/chat-interface-tips.md) | Refresh the chat list, collapse or expand the sidebar, expand the floating chat, stop a response, paste large content, and use prompt suggestions. |

## Reference

| Section | Description |
| :--- | :--- |
| [API](agent-q-api.md) | REST API reference for Agent Q — chat, sessions, specialized endpoints, and LLM configuration management. |
| [FAQ](agent-q-faq.md) | Answers to frequently asked questions about Agent Q, security, usage limits, and troubleshooting. |
