# Containers

Manage computed containers — computed tables, computed files, and computed joins. These are virtual containers whose data is derived from SQL queries or joins over existing containers.

## Create a Container

Create a computed container by specifying its type and definition.

### Computed Table

A computed table runs a SQL query against the datastore's database:

```bash
qualytics containers create \
    --type computed_table \
    --name "active_customers" \
    --datastore-id 1 \
    --query "SELECT * FROM customers WHERE status = 'active'" \
    --tags "production,customers"
```

### Computed File

A computed file applies a Spark SQL transformation on a file-based container:

```bash
qualytics containers create \
    --type computed_file \
    --name "filtered_events" \
    --datastore-id 1 \
    --source-container-id 10 \
    --select-clause "event_type, timestamp, user_id" \
    --where-clause "event_type = 'purchase'"
```

### Computed Join

A computed join combines two containers:

```bash
qualytics containers create \
    --type computed_join \
    --name "orders_with_customers" \
    --left-container-id 10 \
    --right-container-id 20 \
    --left-key-field "customer_id" \
    --right-key-field "id" \
    --join-type inner \
    --select-clause "l.order_id, r.customer_name, l.total"
```

### Options

| Option | Type | Default | Required | Description |
|--------|------|---------|----------|-------------|
| `--type`, `-t` | TEXT | — | Yes | Container type: `computed_table`, `computed_file`, or `computed_join` |
| `--name`, `-n` | TEXT | — | Yes | Container name |
| `--datastore-id` | INTEGER | — | Yes | Datastore ID (for `computed_table` and `computed_file`) |
| `--query`, `-q` | TEXT | — | No | SQL query (required for `computed_table`) |
| `--source-container-id` | INTEGER | — | No | Source container ID (for `computed_file`) |
| `--select-clause` | TEXT | — | No | Select clause (for `computed_file` and `computed_join`) |
| `--where-clause` | TEXT | — | No | Where clause (optional filter) |
| `--group-by-clause` | TEXT | — | No | Group by clause |
| `--left-container-id` | INTEGER | — | No | Left container ID (for `computed_join`) |
| `--right-container-id` | INTEGER | — | No | Right container ID (for `computed_join`) |
| `--left-key-field` | TEXT | — | No | Left join key field (for `computed_join`) |
| `--right-key-field` | TEXT | — | No | Right join key field (for `computed_join`) |
| `--left-prefix` | TEXT | — | No | Prefix for left container fields in join |
| `--right-prefix` | TEXT | — | No | Prefix for right container fields in join |
| `--join-type` | TEXT | — | No | Join type: `inner`, `left`, `right`, or `full` |
| `--description`, `-d` | TEXT | — | No | Container description |
| `--tags` | TEXT | — | No | Comma-separated tags |
| `--dry-run` | FLAG | `false` | No | Print payload without making the API call |
| `--format`, `-f` | TEXT | `yaml` | No | Output format: `yaml` or `json` |

## Update a Container

Update specific fields of an existing container (GET-merge-PUT):

```bash
qualytics containers update \
    --id 5 \
    --query "SELECT * FROM customers WHERE status = 'active' AND region = 'US'"
```

### Options

| Option | Type | Default | Required | Description |
|--------|------|---------|----------|-------------|
| `--id` | INTEGER | — | Yes | Container ID to update |
| `--name`, `-n` | TEXT | — | No | New container name |
| `--query`, `-q` | TEXT | — | No | New SQL query (for `computed_table`) |
| `--select-clause` | TEXT | — | No | New select clause |
| `--where-clause` | TEXT | — | No | New where clause |
| `--group-by-clause` | TEXT | — | No | New group by clause |
| `--description`, `-d` | TEXT | — | No | New description |
| `--tags` | TEXT | — | No | Comma-separated tags |
| `--force-drop-fields` | FLAG | `false` | No | Allow dropping fields that have associated checks or anomalies |
| `--format`, `-f` | TEXT | `yaml` | No | Output format: `yaml` or `json` |

!!! warning
    Changing a query may drop fields. Use `--force-drop-fields` to allow this when fields have associated checks or anomalies.

## Get a Container

```bash
qualytics containers get --id 5
qualytics containers get --id 5 --profiles
```

### Options

| Option | Type | Default | Required | Description |
|--------|------|---------|----------|-------------|
| `--id` | INTEGER | — | Yes | Container ID |
| `--profiles` | FLAG | `false` | No | Also fetch field profiles |
| `--format`, `-f` | TEXT | `yaml` | No | Output format: `yaml` or `json` |

## List Containers

```bash
qualytics containers list --datastore-id 1
qualytics containers list --datastore-id 1 --type computed_table,computed_join
qualytics containers list --datastore-id 1 --tag production --format json
```

### Options

| Option | Type | Default | Required | Description |
|--------|------|---------|----------|-------------|
| `--datastore-id` | INTEGER | — | Yes | Datastore ID |
| `--type`, `-t` | TEXT | — | No | Comma-separated types: `table`, `view`, `file`, `computed_table`, `computed_file`, `computed_join` |
| `--name` | TEXT | — | No | Filter by name |
| `--tag` | TEXT | — | No | Tag name to filter by |
| `--search` | TEXT | — | No | Search string across container fields |
| `--archived` | TEXT | — | No | Archive filter: `only` for archived, `include` for all |
| `--format`, `-f` | TEXT | `yaml` | No | Output format: `yaml` or `json` |

## Delete a Container

```bash
qualytics containers delete --id 5
```

| Option | Type | Default | Required | Description |
|--------|------|---------|----------|-------------|
| `--id` | INTEGER | — | Yes | Container ID to delete |

!!! warning
    Deletion cascades to all fields, quality checks, and anomalies associated with the container.

## Validate a Container

Dry-run validation of a computed container definition without creating it:

```bash
qualytics containers validate \
    --type computed_table \
    --datastore-id 1 \
    --query "SELECT * FROM customers WHERE status = 'active'"
```

### Options

| Option | Type | Default | Required | Description |
|--------|------|---------|----------|-------------|
| `--type`, `-t` | TEXT | — | Yes | Container type: `computed_table`, `computed_file`, or `computed_join` |
| `--name`, `-n` | TEXT | `validation_test` | No | Container name for validation |
| `--datastore-id` | INTEGER | — | No | Datastore ID (for `computed_table` and `computed_file`) |
| `--query`, `-q` | TEXT | — | No | SQL query (for `computed_table`) |
| `--source-container-id` | INTEGER | — | No | Source container ID (for `computed_file`) |
| `--select-clause` | TEXT | — | No | Select clause |
| `--where-clause` | TEXT | — | No | Where clause |
| `--group-by-clause` | TEXT | — | No | Group by clause |
| `--left-container-id` | INTEGER | — | No | Left container ID (for `computed_join`) |
| `--right-container-id` | INTEGER | — | No | Right container ID (for `computed_join`) |
| `--left-key-field` | TEXT | — | No | Left join key field |
| `--right-key-field` | TEXT | — | No | Right join key field |
| `--join-type` | TEXT | — | No | Join type: `inner`, `left`, `right`, or `full` |
| `--timeout` | INTEGER | 60 | No | Validation timeout in seconds |

## Bulk Import Computed Tables

Import computed tables from an Excel, CSV, or TXT file:

```bash
qualytics containers import \
    --datastore 1 \
    --input computed_tables.xlsx \
    --prefix "ct_" \
    --tags "imported,production"
```

The input file must have 3 columns:

| Column | Required | Description |
|--------|----------|-------------|
| 1 - Name | Yes | Computed table name |
| 2 - Description | No | Description (can be empty) |
| 3 - Query | Yes | SQL query |

### Options

| Option | Type | Default | Required | Description |
|--------|------|---------|----------|-------------|
| `--datastore` | INTEGER | — | Yes | Datastore ID |
| `--input` | TEXT | — | Yes | Input file path (`.xlsx`, `.csv`, or `.txt`) |
| `--delimiter` | TEXT | `,` or `\t` | No | Delimiter for CSV/TXT files |
| `--prefix` | TEXT | `ct_` | No | Prefix for computed table names |
| `--as-draft` / `--as-active` | FLAG | `--as-draft` | No | Create checks as Draft or Active |
| `--skip-checks` | FLAG | `false` | No | Skip creating quality checks (only create computed tables) |
| `--skip-profile-wait` | FLAG | `false` | No | Skip waiting for profile operation |
| `--tags` | TEXT | — | No | Tags for checks (comma-separated) |
| `--dry-run` | FLAG | `false` | No | Preview without making changes |
| `--debug` | FLAG | `false` | No | Enable debug mode, write logs to `~/.qualytics/logs/` |

!!! warning
    Using `--skip-profile-wait` means checks may fail if the profile hasn't completed. Use with caution.

## Preview Computed Tables

Preview computed table definitions from a file without importing:

```bash
qualytics containers preview --input computed_tables.xlsx --limit 10
```

### Options

| Option | Type | Default | Required | Description |
|--------|------|---------|----------|-------------|
| `--input` | TEXT | — | Yes | Input file path (`.xlsx`, `.csv`, or `.txt`) |
| `--delimiter` | TEXT | `,` or `\t` | No | Delimiter for CSV/TXT files |
| `--limit` | INTEGER | 5 | No | Number of records to preview |
| `--prefix` | TEXT | `ct_` | No | Prefix to show for computed table names |
