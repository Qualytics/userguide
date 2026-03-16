# Model Context Protocol (MCP)

The [Model Context Protocol](https://modelcontextprotocol.io/) (MCP) is an open standard that enables AI assistants to securely connect to external data sources, tools, and services. It defines a common language for how AI models discover and call capabilities exposed by external systems — without hardcoding integrations or writing custom connectors for each tool.

## How MCP Works

MCP follows a client-server architecture:

- **MCP Server** — An application (like Qualytics) exposes a set of tools and resources through the MCP protocol. The server handles authentication, executes the tool logic, and returns structured results.
- **MCP Client** — An AI assistant or agent (like Claude Desktop, ChatGPT, or Agent Q) connects to one or more MCP servers and can call their tools during a conversation.
- **LLM** — The language model decides which tools to call, in what order, and how to interpret the results. The MCP protocol itself is model-agnostic.

When you send a message to an MCP-connected assistant:

1. The LLM receives your message along with a description of available tools.
2. It decides whether to call a tool and which one.
3. The client sends the tool call to the MCP server.
4. The server executes the action and returns a structured result.
5. The LLM receives the result and incorporates it into its response.
6. This loop repeats until the LLM produces a final answer.

This design means the LLM never directly touches your data infrastructure — it only sees the structured results returned by the MCP server, which enforces its own authentication and authorization rules.

## Key Concepts

### Tools

Tools are the primary mechanism through which MCP servers expose functionality. Each tool has:

- A **name** — how the LLM references it (e.g., `list_datastores`)
- A **description** — natural language description the LLM uses to decide when to call it
- An **input schema** — the parameters the tool accepts (JSON Schema)
- An **output** — structured data returned after execution

The LLM reads tool descriptions and schemas to understand what each tool does and how to call it correctly. Well-written tool descriptions are essential — they are what allow the model to select the right tool for a given user request.

### Resources

MCP also defines a resources concept for exposing read-only data (files, database records, documents) that the LLM can reference as context. Qualytics primarily uses tools rather than resources for its MCP integration.

### Prompts

MCP supports server-defined prompt templates — pre-built message structures that guide the LLM through specific workflows. Qualytics uses this for its guided workflow capabilities (analyze trends, investigate anomalies, generate quality checks, etc.).

### Dynamic Tool Discovery

Because LLM context windows are finite, loading every available tool upfront would waste tokens. MCP allows clients to discover tools dynamically — starting with a small core set and loading additional tools on demand. Qualytics implements this through the `discover_tools` meta-tool, which lets Agent Q search and activate tools by capability as the conversation progresses.

## Transport

MCP supports multiple transport mechanisms. Qualytics exposes its MCP server over **HTTP with Server-Sent Events (SSE)**, which is the standard transport for remote MCP servers. This means:

- No special local software is required to connect external clients.
- Authentication is handled via HTTP headers (Bearer token).
- Streaming responses are supported for long-running tool executions.

## Why MCP Matters for Data Quality

Traditional integrations between AI tools and data platforms require custom-built connectors, hardcoded API calls, and constant maintenance as APIs evolve. MCP standardizes this — any MCP-compatible AI client can connect to any MCP server and immediately discover its capabilities.

For data quality workflows, this means:

- **Portability** — The same Qualytics MCP server works with Claude Desktop, ChatGPT, Cursor, and any future MCP-compatible tool, without changes.
- **Security** — The MCP server enforces authentication and RBAC on every tool call. The LLM never has direct database access.
- **Auditability** — Every tool call is a discrete, logged action. You can see exactly what the AI did and why.
- **Composability** — Complex workflows emerge naturally from combining simple tools, driven by the LLM's reasoning rather than hardcoded orchestration logic.

## Qualytics MCP Server

Qualytics implements an MCP server that exposes its entire data quality infrastructure as callable tools. For details on the endpoint, authentication, available tools, limits, and example conversations, see [Agent Q in Action](./agent-q-in-action.md){:target="_blank"}.

## Next Steps

- [Agent Q in Action](./agent-q-in-action.md){:target="_blank"} — How Qualytics implements MCP as a server.
- [Add Integration](../managing/add-agent-q-integration.md#connecting-external-ai-clients){:target="_blank"} — Connect external AI clients (Claude Desktop, ChatGPT, Cursor) to the Qualytics MCP server.
