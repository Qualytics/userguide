# Datastores

Manage datastores that define which database, schema, and connection Qualytics monitors for data quality.

## Create a Datastore

```bash
qualytics datastores create \
    --name "Orders Production" \
    --connection-name "Production DB" \
    --database analytics \
    --schema public
```

### Options

| Option | Type | Default | Required | Description |
|--------|------|---------|----------|-------------|
| `--name`, `-n` | TEXT | — | Yes | Datastore name |
| `--connection-name`, `-cn` | TEXT | — | No | Connection name (required if `--connection-id` not set) |
| `--connection-id` | INTEGER | — | No | Connection ID (required if `--connection-name` not set) |
| `--database`, `-db` | TEXT | — | Yes | Database name |
| `--schema`, `-sc` | TEXT | — | Yes | Schema name |
| `--tags` | TEXT | — | No | Comma-separated tags |
| `--teams` | TEXT | — | No | Comma-separated team names |
| `--enrichment-only` / `--no-enrichment-only` | FLAG | `false` | No | Set as enrichment-only datastore |
| `--enrichment-prefix` | TEXT | — | No | Prefix for enrichment artifacts |
| `--enrichment-source-record-limit` | INTEGER | — | No | Source record limit for enrichment (min: 1) |
| `--enrichment-remediation-strategy` | TEXT | `none` | No | Remediation strategy |
| `--high-count-rollup-threshold` | INTEGER | — | No | High count rollup threshold (min: 1) |
| `--trigger-sync` / `--no-trigger-sync` | FLAG | `true` | No | Whether to trigger sync after creation |
| `--dry-run` | FLAG | `false` | No | Print payload without making the API call |
| `--format`, `-f` | TEXT | `yaml` | No | Output format: `yaml` or `json` |

### With Enrichment Configuration

```bash
qualytics datastores create \
    --name "Orders Production" \
    --connection-id 1 \
    --database analytics \
    --schema public \
    --enrichment-prefix "_qualytics" \
    --enrichment-remediation-strategy append \
    --tags "production,orders"
```

## Update a Datastore

Update specific fields of an existing datastore. Only provided fields are changed.

```bash
qualytics datastores update --id 1 --name "Orders v2" --tags "production,v2"
```

### Options

| Option | Type | Default | Required | Description |
|--------|------|---------|----------|-------------|
| `--id` | INTEGER | — | Yes | Datastore ID to update |
| `--name`, `-n` | TEXT | — | No | New datastore name |
| `--connection-id` | INTEGER | — | No | New connection ID |
| `--database`, `-db` | TEXT | — | No | New database |
| `--schema`, `-sc` | TEXT | — | No | New schema |
| `--tags` | TEXT | — | No | Comma-separated tags |
| `--teams` | TEXT | — | No | Comma-separated team names |
| `--enrichment-only` / `--no-enrichment-only` | FLAG | — | No | Enrichment-only flag |
| `--enrichment-prefix` | TEXT | — | No | Prefix for enrichment artifacts |
| `--enrichment-source-record-limit` | INTEGER | — | No | Source record limit (min: 1) |
| `--enrichment-remediation-strategy` | TEXT | — | No | Remediation strategy |
| `--high-count-rollup-threshold` | INTEGER | — | No | High count rollup threshold (min: 1) |
| `--format`, `-f` | TEXT | `yaml` | No | Output format: `yaml` or `json` |

## Get a Datastore

```bash
qualytics datastores get --id 1
qualytics datastores get --name "Orders Production"
```

### Options

| Option | Type | Default | Required | Description |
|--------|------|---------|----------|-------------|
| `--id` | INTEGER | — | No | Datastore ID |
| `--name` | TEXT | — | No | Datastore name |
| `--format`, `-f` | TEXT | `yaml` | No | Output format: `yaml` or `json` |

!!! note
    Specify either `--id` or `--name`, not both.

## List Datastores

```bash
qualytics datastores list
qualytics datastores list --type postgresql,snowflake --tag production
qualytics datastores list --enrichment-only --format json
```

### Options

| Option | Type | Default | Required | Description |
|--------|------|---------|----------|-------------|
| `--name` | TEXT | — | No | Filter by name (search) |
| `--type` | TEXT | — | No | Comma-separated connection types |
| `--tag` | TEXT | — | No | Tag name to filter by |
| `--enrichment-only` / `--no-enrichment-only` | FLAG | — | No | Filter enrichment-only datastores |
| `--format`, `-f` | TEXT | `yaml` | No | Output format: `yaml` or `json` |

## Delete a Datastore

```bash
qualytics datastores delete --id 1
```

| Option | Type | Default | Required | Description |
|--------|------|---------|----------|-------------|
| `--id` | INTEGER | — | Yes | Datastore ID to delete |

!!! warning
    This permanently deletes the datastore and all associated containers, checks, and anomalies.

## Verify a Datastore

Test the database connection for an existing datastore:

```bash
qualytics datastores verify --id 1
```

| Option | Type | Default | Required | Description |
|--------|------|---------|----------|-------------|
| `--id` | INTEGER | — | Yes | Datastore ID to verify |
| `--format`, `-f` | TEXT | `yaml` | No | Output format: `yaml` or `json` |

## Enrichment Linking

Link or unlink an enrichment datastore to a source datastore:

```bash
# Link enrichment datastore
qualytics datastores enrichment --id 1 --link 2

# Unlink enrichment datastore
qualytics datastores enrichment --id 1 --unlink
```

### Options

| Option | Type | Default | Required | Description |
|--------|------|---------|----------|-------------|
| `--id` | INTEGER | — | Yes | Source datastore ID |
| `--link` | INTEGER | — | No | Enrichment datastore ID to link |
| `--unlink` | FLAG | `false` | No | Unlink the enrichment datastore |

!!! note
    Specify either `--link` or `--unlink`, not both.
