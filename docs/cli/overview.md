# Qualytics CLI

The Qualytics CLI is a command-line tool for managing your Qualytics data quality platform. It provides full control over connections, datastores, quality checks, operations, anomalies, and configuration — all from the terminal.

## Installation

### Prerequisites

- **Python 3.10** or higher

!!! tip "Need Python?"
    See our [Python Installation Guide](python-installation.md) for step-by-step instructions on Windows.

### Install via pip

```bash
pip install qualytics-cli
```

### Install via uv (recommended)

```bash
uv pip install qualytics-cli
```

### Upgrade

```bash
pip install qualytics-cli --upgrade
```

## Quick Start

**1. Authenticate** — Open a browser login (recommended):

```bash
qualytics auth login --url https://your-instance.qualytics.io
```

Or configure with a token directly:

```bash
qualytics auth init --url https://your-instance.qualytics.io --token YOUR_TOKEN
```

**2. Verify setup** — Run diagnostics:

```bash
qualytics doctor
```

**3. Start working** — List your datastores:

```bash
qualytics datastores list
```

**4. Run an operation** — Sync, profile, and scan:

```bash
qualytics operations sync --datastore-id 1
qualytics operations profile --datastore-id 1
qualytics operations scan --datastore-id 1
```

## Command Groups

The CLI organizes its functionality into these command groups:

| Group | Description | Commands |
|-------|-------------|----------|
| [`auth`](authentication.md) | Authentication and configuration | `login`, `init`, `status` |
| [`connections`](connections.md) | Database connection management | `create`, `update`, `get`, `list`, `delete`, `test` |
| [`datastores`](datastores.md) | Datastore management | `create`, `update`, `get`, `list`, `delete`, `verify`, `enrichment` |
| [`containers`](containers.md) | Computed containers (tables, files, joins) | `create`, `update`, `get`, `list`, `delete`, `validate`, `import`, `preview` |
| [`checks`](quality-checks.md) | Quality check management | `create`, `get`, `list`, `update`, `delete`, `activate`, `export`, `import`, `export-templates`, `import-templates` |
| [`anomalies`](anomalies.md) | Anomaly management | `get`, `list`, `update`, `archive`, `delete` |
| [`operations`](operations.md) | Data processing workflows | `sync`, `profile`, `scan`, `materialize`, `export`, `get`, `list`, `abort` |
| [`users`](users.md) | User account listing | `list`, `get` |
| [`teams`](teams.md) | Team listing | `list`, `get` |
| [`tags`](tags.md) | Tag management | `list`, `get`, `create`, `delete` |
| [`config`](config-as-code.md) | Configuration as code | `export`, `import` |
| [`schedule`](automation.md) | Scheduled exports | `export-metadata` |
| [`mcp`](mcp-server.md) | AI assistant integration | `serve` |
| `doctor` | Health diagnostics | _(see below)_ |

## Doctor

Run `qualytics doctor` to verify your CLI setup. It performs 7 diagnostic checks:

```bash
qualytics doctor
```

```text
  ✓ CLI version      Qualytics CLI v1.0.0
  ✓ Python version   3.12.0
  ✓ Configuration    ~/.qualytics/config.yaml
  ✓ Auth token       Token present
  ✓ Token expiry     Expires 2026-04-15
  ✓ API connectivity https://your-instance.qualytics.io — OK
  ✓ SSL certificate  Valid

  7 passed, 0 failed
```

| Check | What it validates |
|-------|-------------------|
| CLI version | Current installed version |
| Python version | Python 3.10+ is available |
| Configuration | `~/.qualytics/config.yaml` exists |
| Auth token | A token is configured |
| Token expiry | Token is not expired |
| API connectivity | Can reach the Qualytics API |
| SSL certificate | SSL certificate is valid |

## Global Options

### Output Format

Most `get` and `list` commands support `--format`:

```bash
qualytics connections list --format json
qualytics datastores get --id 1 --format yaml
```

Supported formats: `yaml` (default), `json`.

### Help

View available commands and usage:

```bash
qualytics --help
qualytics connections --help
qualytics connections create --help
```

## Environment Variables

| Variable | Description |
|----------|-------------|
| `QUALYTICS_URL` | Qualytics instance URL (overrides config file) |
| `QUALYTICS_TOKEN` | Auth token (overrides config file) |
| `QUALYTICS_NO_BANNER` | Set to suppress the startup banner |
| `CI` | When `true`, suppresses the banner (auto-set in CI environments) |

## Configuration File

The CLI stores its configuration at `~/.qualytics/config.yaml`:

```yaml
url: https://your-instance.qualytics.io
token: eyJhbGciOiJSUzI1NiIs...
verify_ssl: true
```

- File permissions are set to `0600` (owner read/write only)
- Environment variables (`QUALYTICS_URL`, `QUALYTICS_TOKEN`) take precedence over the config file
- Legacy `config.json` files are automatically migrated to `config.yaml`

## Secrets Management

Sensitive fields in connection definitions support `${ENV_VAR}` syntax:

```yaml
host: ${DB_HOST}
username: ${DB_USER}
password: ${DB_PASSWORD}
```

These placeholders are resolved from environment variables (or a `.env` file in the working directory) at import time. Secrets are never stored in plaintext in exported files.
