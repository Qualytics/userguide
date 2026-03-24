# Operations

Trigger and manage data processing workflows — sync (discover containers), profile (infer checks), scan (detect anomalies), materialize (execute computed containers), and export (push results to enrichment).

## Common Options

All trigger commands (`sync`, `profile`, `scan`, `materialize`, `export`) share these options:

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--datastore-id` | TEXT | — | Comma-separated datastore IDs (required) |
| `--background` | FLAG | `false` | Start operation without waiting for completion |
| `--poll-interval` | INTEGER | 30 | Seconds between status checks |
| `--timeout` | INTEGER | 1800 | Maximum wait time in seconds (30 min default) |

## Sync

Discover containers (tables, views, files) in your datastores:

```bash
qualytics operations sync --datastore-id 1
qualytics operations sync --datastore-id 1,2,3 --include "table,view" --prune
```

### Options

| Option | Type | Default | Required | Description |
|--------|------|---------|----------|-------------|
| `--datastore-id` | TEXT | — | Yes | Comma-separated datastore IDs |
| `--include` | TEXT | — | No | Comma-separated include types: `table`, `view` |
| `--prune` | FLAG | `false` | No | Remove containers not found during sync |
| `--recreate` | FLAG | `false` | No | Drop and recreate all containers |
| `--background` | FLAG | `false` | No | Return immediately |
| `--poll-interval` | INTEGER | 30 | No | Seconds between status checks |
| `--timeout` | INTEGER | 1800 | No | Max wait time in seconds |

## Profile

Analyze data and infer quality checks:

```bash
qualytics operations profile --datastore-id 1
qualytics operations profile --datastore-id 1 \
    --container-names "orders,customers" \
    --inference-threshold 3 \
    --infer-as-draft
```

### Options

| Option | Type | Default | Required | Description |
|--------|------|---------|----------|-------------|
| `--datastore-id` | TEXT | — | Yes | Comma-separated datastore IDs |
| `--container-names` | TEXT | — | No | Comma-separated container names |
| `--container-tags` | TEXT | — | No | Comma-separated container tags |
| `--inference-threshold` | INTEGER | — | No | Inference quality checks threshold (0 to 5) |
| `--infer-as-draft` | FLAG | `false` | No | Infer all quality checks as Draft |
| `--max-records-analyzed-per-partition` | INTEGER | — | No | Max records per partition (-1 for unlimited) |
| `--max-count-testing-sample` | INTEGER | — | No | Records for validation of inferred checks (max 100,000) |
| `--percent-testing-threshold` | FLOAT | — | No | Testing threshold percentage |
| `--high-correlation-threshold` | FLOAT | — | No | Correlation threshold |
| `--greater-than-time` | DATETIME | — | No | Incremental: only rows after this time (`YYYY-MM-DDTHH:MM:SS`) |
| `--greater-than-batch` | FLOAT | — | No | Incremental: only rows with value greater than this number |
| `--histogram-max-distinct-values` | INTEGER | — | No | Max distinct values for histogram |
| `--background` | FLAG | `false` | No | Return immediately |
| `--poll-interval` | INTEGER | 30 | No | Seconds between status checks |
| `--timeout` | INTEGER | 1800 | No | Max wait time in seconds |

## Scan

Detect anomalies against quality checks:

```bash
qualytics operations scan --datastore-id 1
qualytics operations scan --datastore-id 1 \
    --container-names "orders" \
    --incremental \
    --remediation append
```

### Options

| Option | Type | Default | Required | Description |
|--------|------|---------|----------|-------------|
| `--datastore-id` | TEXT | — | Yes | Comma-separated datastore IDs |
| `--container-names` | TEXT | — | No | Comma-separated container names |
| `--container-tags` | TEXT | — | No | Comma-separated container tags |
| `--incremental` | FLAG | `false` | No | Process only new or updated records since last scan |
| `--remediation` | TEXT | `none` | No | Replication strategy: `append`, `overwrite`, or `none` |
| `--max-records-analyzed-per-partition` | INTEGER | — | No | Max records per partition (-1 for unlimited) |
| `--enrichment-source-record-limit` | INTEGER | — | No | Enrichment source records limit (min: 1) |
| `--greater-than-time` | DATETIME | — | No | Incremental: only rows after this time (`YYYY-MM-DDTHH:MM:SS`) |
| `--greater-than-batch` | FLOAT | — | No | Incremental: only rows with value greater than this number |
| `--background` | FLAG | `false` | No | Return immediately |
| `--poll-interval` | INTEGER | 30 | No | Seconds between status checks |
| `--timeout` | INTEGER | 1800 | No | Max wait time in seconds |

## Materialize

Execute SQL and persist results for computed containers:

```bash
qualytics operations materialize --datastore-id 1
qualytics operations materialize --datastore-id 1 \
    --container-names "active_customers,order_summary"
```

### Options

| Option | Type | Default | Required | Description |
|--------|------|---------|----------|-------------|
| `--datastore-id` | TEXT | — | Yes | Comma-separated datastore IDs |
| `--container-names` | TEXT | — | No | Comma-separated container names |
| `--container-tags` | TEXT | — | No | Comma-separated container tags |
| `--max-records-per-partition` | INTEGER | — | No | Max records per partition (-1 for unlimited) |
| `--background` | FLAG | `false` | No | Return immediately |
| `--poll-interval` | INTEGER | 30 | No | Seconds between status checks |
| `--timeout` | INTEGER | 1800 | No | Max wait time in seconds |

## Export

Export assets (anomalies, checks, or profiles) to the enrichment datastore:

```bash
qualytics operations export --datastore-id 1 --asset-type anomalies
qualytics operations export --datastore-id 1 \
    --asset-type checks \
    --container-ids "10,20" \
    --include-deleted
```

### Options

| Option | Type | Default | Required | Description |
|--------|------|---------|----------|-------------|
| `--datastore-id` | TEXT | — | Yes | Comma-separated datastore IDs |
| `--asset-type` | TEXT | — | Yes | Asset type: `anomalies`, `checks`, or `profiles` |
| `--container-ids` | TEXT | — | No | Comma-separated container IDs |
| `--container-tags` | TEXT | — | No | Comma-separated container tags |
| `--include-deleted` | FLAG | `false` | No | Include deleted items in export |
| `--background` | FLAG | `false` | No | Return immediately |
| `--poll-interval` | INTEGER | 30 | No | Seconds between status checks |
| `--timeout` | INTEGER | 1800 | No | Max wait time in seconds |

## Get Operation Details

```bash
qualytics operations get --id 1234
qualytics operations get --id 1234 --format json
```

### Options

| Option | Type | Default | Required | Description |
|--------|------|---------|----------|-------------|
| `--id` | INTEGER | — | Yes | Operation ID |
| `--format` | TEXT | `yaml` | No | Output format: `yaml` or `json` |

## List Operations

```bash
qualytics operations list
qualytics operations list --datastore-id "1,2" --type scan --status success
qualytics operations list --start-date 2026-01-01 --end-date 2026-03-23
```

### Options

| Option | Type | Default | Required | Description |
|--------|------|---------|----------|-------------|
| `--datastore-id` | TEXT | — | No | Comma-separated datastore IDs |
| `--type` | TEXT | — | No | Operation type: `sync`, `profile`, `scan`, `materialize`, `export` |
| `--status` | TEXT | — | No | Comma-separated statuses: `running`, `success`, `failure`, `aborted` |
| `--start-date` | TEXT | — | No | Start date filter (`YYYY-MM-DD`) |
| `--end-date` | TEXT | — | No | End date filter (`YYYY-MM-DD`) |
| `--format` | TEXT | `yaml` | No | Output format: `yaml` or `json` |

## Abort an Operation

Cancel a running operation (best-effort):

```bash
qualytics operations abort --id 1234
```

| Option | Type | Default | Required | Description |
|--------|------|---------|----------|-------------|
| `--id` | INTEGER | — | Yes | Operation ID to abort |

## Workflow Example

A typical data quality workflow runs these operations in sequence:

```bash
# 1. Discover containers
qualytics operations sync --datastore-id 1

# 2. Profile data and infer checks
qualytics operations profile --datastore-id 1 --inference-threshold 3

# 3. Scan for anomalies
qualytics operations scan --datastore-id 1

# 4. Export results to enrichment
qualytics operations export --datastore-id 1 --asset-type anomalies
```

!!! tip "Background mode"
    Add `--background` to any trigger command to start the operation and return immediately. Use `qualytics operations list --status running` to check progress.
