# MCP Server

The Qualytics CLI includes a built-in [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) server that lets AI assistants like Claude Code, Cursor, and Windsurf interact with your Qualytics instance directly.

## Start the Server

```bash
qualytics mcp serve
```

### Options

| Option | Type | Default | Required | Description |
|--------|------|---------|----------|-------------|
| `--transport`, `-t` | TEXT | `stdio` | No | Transport protocol: `stdio` or `streamable-http` |
| `--host` | TEXT | `127.0.0.1` | No | Host for `streamable-http` transport |
| `--port`, `-p` | INTEGER | 8000 | No | Port for `streamable-http` transport |

## Setup for Claude Code

Add the Qualytics MCP server to your Claude Code configuration at `~/.claude.json`:

```json
{
  "mcpServers": {
    "qualytics": {
      "command": "qualytics",
      "args": ["mcp", "serve"]
    }
  }
}
```

Claude Code uses the default `stdio` transport.

## Setup for Cursor

Add to your Cursor MCP configuration (`.cursor/mcp.json` in your project or global settings):

```json
{
  "mcpServers": {
    "qualytics": {
      "command": "qualytics",
      "args": ["mcp", "serve"]
    }
  }
}
```

## Setup with HTTP Transport

For network-accessible deployments or tools that require HTTP:

```bash
qualytics mcp serve --transport streamable-http --host 0.0.0.0 --port 8000
```

Then configure your tool to connect to `http://localhost:8000`.

## Available Tools

The MCP server exposes 35 tools across 8 domains:

| Domain | Tools |
|--------|-------|
| **Auth** | Check authentication status |
| **Datastores** | List, get, create, update, delete, verify datastores |
| **Containers** | List, get, create, update, delete containers |
| **Connections** | List, get, create, update, delete, test connections |
| **Quality Checks** | List, get, create, update, delete, export, import checks |
| **Anomalies** | List, get, update, archive, delete anomalies |
| **Operations** | Trigger sync/profile/scan/materialize/export, list, get, abort operations |
| **Config** | Export and import configuration as code |

!!! info "Prerequisites"
    The MCP server uses your existing CLI authentication. Run `qualytics auth login` or `qualytics auth init` before starting the MCP server.
