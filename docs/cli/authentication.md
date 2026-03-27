# Authentication

The Qualytics CLI supports three authentication methods: browser-based login (recommended), manual token configuration, and environment variables for CI/CD.

## Browser Login

The recommended way to authenticate. Opens your browser, you log in, and the CLI receives a token automatically.

```bash
qualytics auth login --url https://your-instance.qualytics.io
```

The CLI starts a local callback server, opens your browser to the Qualytics login page, and waits for the authentication callback. Once you log in, the token is saved automatically.

### Options

| Option | Type | Default | Required | Description |
|--------|------|---------|----------|-------------|
| `--url`, `-u` | TEXT | — | Yes | Qualytics deployment URL |
| `--timeout` | INTEGER | 120 | No | Seconds to wait for browser callback |
| `--no-verify-ssl` | FLAG | `false` | No | Disable SSL certificate verification |

### How It Works

1. The CLI starts a temporary HTTP server on an ephemeral port (`127.0.0.1`)
2. Your browser opens the Qualytics login page
3. After login, Qualytics redirects back to the local server with a token
4. The token is saved to `~/.qualytics/config.yaml`

!!! tip
    If the browser doesn't open automatically, copy the URL printed in the terminal and open it manually.

## Manual Token Setup

For environments where a browser isn't available, or when you already have a token:

```bash
qualytics auth init \
    --url https://your-instance.qualytics.io \
    --token YOUR_TOKEN
```

### Options

| Option | Type | Default | Required | Description |
|--------|------|---------|----------|-------------|
| `--url` | TEXT | — | Yes | Qualytics instance URL |
| `--token` | TEXT | — | Yes | Personal access token |
| `--no-verify-ssl` | FLAG | `false` | No | Disable SSL certificate verification |

!!! info "Self-signed certificates"
    Use `--no-verify-ssl` when connecting to instances with self-signed SSL certificates.

## Check Auth Status

View your current authentication configuration:

```bash
qualytics auth status
```

```text
  URL:        https://your-instance.qualytics.io
  Token:      eyJh...****
  Expires:    2026-04-15T12:00:00Z
  SSL Verify: true
  Config:     ~/.qualytics/config.yaml
```

## CI/CD Authentication

For automated pipelines, use environment variables instead of interactive login:

```bash
export QUALYTICS_URL=https://your-instance.qualytics.io
export QUALYTICS_TOKEN=your-service-token
```

Environment variables take precedence over the config file. Combined with `QUALYTICS_NO_BANNER=1` or `CI=true`, the CLI runs fully non-interactively.

### GitHub Actions Example

{% raw %}
```yaml
jobs:
  quality-scan:
    runs-on: ubuntu-latest
    steps:
      - name: Install CLI
        run: pip install qualytics-cli

      - name: Run scan
        env:
          QUALYTICS_URL: ${{ secrets.QUALYTICS_URL }}
          QUALYTICS_TOKEN: ${{ secrets.QUALYTICS_TOKEN }}
        run: |
          qualytics operations scan --datastore-id 1 --background
```
{% endraw %}
