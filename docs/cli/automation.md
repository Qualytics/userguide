# Automation & CI/CD

Automate data quality workflows with scheduled operations, CI/CD pipelines, and environment-based configuration.

## Scheduled Metadata Exports

Schedule recurring exports of metadata (anomalies, checks, or field profiles) using cron expressions:

```bash
qualytics schedule export-metadata \
    --crontab "0 6 * * *" \
    --datastore 1 \
    --options anomalies,checks
```

### Options

| Option | Type | Default | Required | Description |
|--------|------|---------|----------|-------------|
| `--crontab` | TEXT | — | Yes | Cron expression in quotes (e.g., `'0 * * * *'`) |
| `--datastore` | TEXT | — | Yes | Datastore ID |
| `--containers` | TEXT | — | No | Comma-separated container IDs |
| `--options` | TEXT | — | Yes | What to export: `anomalies`, `checks`, `field-profiles`, or `all` |

### Platform Behavior

- **Linux/macOS** — Creates crontab entries and installs them via `crontab`
- **Windows** — Generates a PowerShell script for Task Scheduler

## CI/CD Integration

The CLI is designed for automated pipelines with these features:

### Environment Variables

Use environment variables instead of config files in CI:

```bash
export QUALYTICS_URL=https://your-instance.qualytics.io
export QUALYTICS_TOKEN=your-service-token
```

### Silent Mode

Suppress the startup banner for clean CI logs:

```bash
export QUALYTICS_NO_BANNER=1
# or
export CI=true
```

### Dry-Run Mode

Preview changes before applying in production:

```bash
qualytics config import --input ./config --dry-run
qualytics checks import --datastore-id 1 --input ./checks --dry-run
```

### Background Operations

Start operations without blocking your pipeline:

```bash
qualytics operations scan --datastore-id 1 --background
```

## GitHub Actions Examples

### Quality Scan on Schedule

{% raw %}
```yaml
name: Nightly Quality Scan
on:
  schedule:
    - cron: '0 6 * * *'

jobs:
  scan:
    runs-on: ubuntu-latest
    steps:
      - name: Install CLI
        run: pip install qualytics-cli

      - name: Run scan
        env:
          QUALYTICS_URL: ${{ secrets.QUALYTICS_URL }}
          QUALYTICS_TOKEN: ${{ secrets.QUALYTICS_TOKEN }}
        run: |
          qualytics operations sync --datastore-id ${{ vars.DATASTORE_ID }}
          qualytics operations profile --datastore-id ${{ vars.DATASTORE_ID }}
          qualytics operations scan --datastore-id ${{ vars.DATASTORE_ID }}
```
{% endraw %}

### Config Promotion (Dev to Prod)

{% raw %}
```yaml
name: Promote Quality Config
on:
  push:
    branches: [main]
    paths: ['qualytics-config/**']

jobs:
  promote:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Install CLI
        run: pip install qualytics-cli

      - name: Import to production
        env:
          QUALYTICS_URL: ${{ secrets.PROD_QUALYTICS_URL }}
          QUALYTICS_TOKEN: ${{ secrets.PROD_QUALYTICS_TOKEN }}
          DB_HOST: ${{ secrets.PROD_DB_HOST }}
          DB_USER: ${{ secrets.PROD_DB_USER }}
          DB_PASSWORD: ${{ secrets.PROD_DB_PASSWORD }}
        run: |
          qualytics config import --input ./qualytics-config --dry-run
          qualytics config import --input ./qualytics-config
```
{% endraw %}

### Check Export and Import Across Environments

{% raw %}
```yaml
name: Sync Checks Dev → Staging
on:
  workflow_dispatch:

jobs:
  export:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Install CLI
        run: pip install qualytics-cli

      - name: Export checks from dev
        env:
          QUALYTICS_URL: ${{ secrets.DEV_QUALYTICS_URL }}
          QUALYTICS_TOKEN: ${{ secrets.DEV_QUALYTICS_TOKEN }}
        run: qualytics checks export --datastore-id ${{ vars.DEV_DATASTORE_ID }} --output ./checks

      - name: Import checks to staging
        env:
          QUALYTICS_URL: ${{ secrets.STAGING_QUALYTICS_URL }}
          QUALYTICS_TOKEN: ${{ secrets.STAGING_QUALYTICS_TOKEN }}
        run: qualytics checks import --datastore-id ${{ vars.STAGING_DATASTORE_ID }} --input ./checks
```
{% endraw %}

## Secrets Management

The CLI supports `${ENV_VAR}` syntax for sensitive fields in connection and config files. This ensures secrets are never committed to version control.

### Supported Fields

These fields accept `${ENV_VAR}` placeholders:

- `host`
- `username`
- `password`
- `access_key`
- `secret_key`
- `uri`
- `token`

### Resolution Order

1. System environment variables
2. `.env` file in the current working directory

### Example `.env` File

```bash
DB_HOST=production-db.example.com
DB_USER=qualytics_reader
DB_PASSWORD=s3cur3p@ss
SNOWFLAKE_ACCOUNT=xy12345
SNOWFLAKE_PASSWORD=another_secret
```
