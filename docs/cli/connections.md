# Connections

Manage database connections used by datastores. Connections define how Qualytics connects to your databases — credentials, hosts, ports, and connection-specific parameters.

## Create a Connection

```bash
qualytics connections create \
    --type postgresql \
    --name "Production DB" \
    --host ${DB_HOST} \
    --port 5432 \
    --username ${DB_USER} \
    --password ${DB_PASSWORD}
```

### Options

| Option | Type | Default | Required | Description |
|--------|------|---------|----------|-------------|
| `--type`, `-t` | TEXT | — | Yes | Connection type (e.g., `postgresql`, `snowflake`, `mysql`, `bigquery`) |
| `--name`, `-n` | TEXT | — | No | Connection name |
| `--host` | TEXT | — | No | Host (supports `${ENV_VAR}`) |
| `--port` | INTEGER | — | No | Port number |
| `--username` | TEXT | — | No | Username (supports `${ENV_VAR}`) |
| `--password` | TEXT | — | No | Password (supports `${ENV_VAR}`) |
| `--uri` | TEXT | — | No | URI for DFS connections (supports `${ENV_VAR}`) |
| `--access-key` | TEXT | — | No | Access key for DFS connections (supports `${ENV_VAR}`) |
| `--secret-key` | TEXT | — | No | Secret key for DFS connections (supports `${ENV_VAR}`) |
| `--catalog` | TEXT | — | No | Catalog for native connections |
| `--jdbc-fetch-size` | INTEGER | — | No | JDBC fetch size |
| `--max-parallelization` | INTEGER | — | No | Max parallelization level |
| `--parameters` | TEXT | — | No | JSON string for type-specific params |
| `--dry-run` | FLAG | `false` | No | Print payload without making the API call |
| `--format`, `-f` | TEXT | `yaml` | No | Output format: `yaml` or `json` |

### Snowflake Example

```bash
qualytics connections create \
    --type snowflake \
    --name "Snowflake Warehouse" \
    --host ${SNOWFLAKE_ACCOUNT}.snowflakecomputing.com \
    --username ${SNOWFLAKE_USER} \
    --password ${SNOWFLAKE_PASSWORD} \
    --parameters '{"role": "ANALYST", "warehouse": "COMPUTE_WH"}'
```

## Update a Connection

Update specific fields of an existing connection. Only provided fields are changed.

```bash
qualytics connections update \
    --id 1 \
    --password ${NEW_PASSWORD}
```

### Options

| Option | Type | Default | Required | Description |
|--------|------|---------|----------|-------------|
| `--id` | INTEGER | — | Yes | Connection ID to update |
| `--name`, `-n` | TEXT | — | No | New connection name |
| `--host` | TEXT | — | No | New host (supports `${ENV_VAR}`) |
| `--port` | INTEGER | — | No | New port |
| `--username` | TEXT | — | No | New username (supports `${ENV_VAR}`) |
| `--password` | TEXT | — | No | New password (supports `${ENV_VAR}`) |
| `--uri` | TEXT | — | No | New URI (supports `${ENV_VAR}`) |
| `--access-key` | TEXT | — | No | New access key (supports `${ENV_VAR}`) |
| `--secret-key` | TEXT | — | No | New secret key (supports `${ENV_VAR}`) |
| `--parameters` | TEXT | — | No | JSON string for type-specific params |
| `--format`, `-f` | TEXT | `yaml` | No | Output format: `yaml` or `json` |

## Get a Connection

Retrieve connection details by ID or name. Secrets are masked in the response.

```bash
qualytics connections get --id 1
qualytics connections get --name "Production DB"
```

### Options

| Option | Type | Default | Required | Description |
|--------|------|---------|----------|-------------|
| `--id` | INTEGER | — | No | Connection ID |
| `--name` | TEXT | — | No | Connection name |
| `--format`, `-f` | TEXT | `yaml` | No | Output format: `yaml` or `json` |

!!! note
    Specify either `--id` or `--name`, not both.

## List Connections

```bash
qualytics connections list
qualytics connections list --type postgresql,snowflake
qualytics connections list --name "prod" --format json
```

### Options

| Option | Type | Default | Required | Description |
|--------|------|---------|----------|-------------|
| `--name` | TEXT | — | No | Filter by name (search) |
| `--type`, `-t` | TEXT | — | No | Comma-separated connection types |
| `--format`, `-f` | TEXT | `yaml` | No | Output format: `yaml` or `json` |

## Delete a Connection

```bash
qualytics connections delete --id 1
```

| Option | Type | Default | Required | Description |
|--------|------|---------|----------|-------------|
| `--id` | INTEGER | — | Yes | Connection ID to delete |

!!! warning
    Deletion fails with a 409 error if datastores still reference this connection. Remove or reassign those datastores first.

## Test a Connection

Test connectivity with saved or overridden credentials:

```bash
# Test saved connection
qualytics connections test --id 1

# Test with new credentials (without persisting)
qualytics connections test --id 1 --password ${NEW_PASSWORD}
```

### Options

| Option | Type | Default | Required | Description |
|--------|------|---------|----------|-------------|
| `--id` | INTEGER | — | Yes | Connection ID to test |
| `--host` | TEXT | — | No | Override host for testing (supports `${ENV_VAR}`) |
| `--username` | TEXT | — | No | Override username for testing (supports `${ENV_VAR}`) |
| `--password` | TEXT | — | No | Override password for testing (supports `${ENV_VAR}`) |
| `--format`, `-f` | TEXT | `yaml` | No | Output format: `yaml` or `json` |
