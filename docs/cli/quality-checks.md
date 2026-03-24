# Quality Checks

Manage quality checks — create, update, export, import, and organize checks that define your data quality rules.

## Create Checks

Create quality checks from a YAML or JSON file. The file can contain a single check or multiple checks.

```bash
qualytics checks create --datastore-id 1 --file checks.yaml
```

### Options

| Option | Type | Default | Required | Description |
|--------|------|---------|----------|-------------|
| `--datastore-id` | INTEGER | — | Yes | Target datastore ID |
| `--file`, `-f` | TEXT | — | Yes | YAML or JSON file with check definition(s) |

### Check YAML Schema

```yaml
rule_type: isNotNull
container: orders
fields:
  - customer_id
description: "Customer ID must not be null"
coverage: 1.0
filter: null
tags:
  - production
  - orders
properties: {}
status: Active   # or Draft
```

Key fields:

| Field | Required | Description |
|-------|----------|-------------|
| `rule_type` | Yes | Check rule type (e.g., `isNotNull`, `satisfiesExpression`, `isUnique`) |
| `container` | Yes | Container name to apply the check to |
| `fields` | Yes | List of field names |
| `description` | No | Human-readable description |
| `coverage` | No | Expected pass rate (0.0 to 1.0) |
| `filter` | No | SQL WHERE clause to filter rows |
| `tags` | No | List of tag names |
| `properties` | No | Rule-specific properties |
| `status` | No | `Active` or `Draft` |

## Get a Check

```bash
qualytics checks get --id 100
qualytics checks get --id 100 --format json
```

### Options

| Option | Type | Default | Required | Description |
|--------|------|---------|----------|-------------|
| `--id` | INTEGER | — | Yes | Quality check ID |
| `--format` | TEXT | `yaml` | No | Output format: `yaml` or `json` |

## List Checks

```bash
qualytics checks list --datastore-id 1
qualytics checks list --datastore-id 1 --containers "10,20" --status Active
qualytics checks list --datastore-id 1 --tags "production" --format json
```

### Options

| Option | Type | Default | Required | Description |
|--------|------|---------|----------|-------------|
| `--datastore-id` | INTEGER | — | Yes | Datastore ID |
| `--containers` | TEXT | — | No | Comma-separated container IDs |
| `--tags` | TEXT | — | No | Comma-separated tag names |
| `--status` | TEXT | — | No | Filter by status: `Active`, `Draft`, or `Archived` |
| `--format` | TEXT | `yaml` | No | Output format: `yaml` or `json` |

## Update a Check

Update a quality check from a YAML or JSON file:

```bash
qualytics checks update --id 100 --file updated_check.yaml
```

### Options

| Option | Type | Default | Required | Description |
|--------|------|---------|----------|-------------|
| `--id` | INTEGER | — | Yes | Quality check ID to update |
| `--file`, `-f` | TEXT | — | Yes | YAML or JSON file with updated check definition |

## Delete Checks

Delete one or more quality checks:

```bash
# Soft-delete (archive) a single check
qualytics checks delete --id 100

# Hard-delete a single check
qualytics checks delete --id 100 --no-archive

# Bulk soft-delete
qualytics checks delete --ids "100,101,102"
```

### Options

| Option | Type | Default | Required | Description |
|--------|------|---------|----------|-------------|
| `--id` | INTEGER | — | No | Single check ID to delete |
| `--ids` | TEXT | — | No | Comma-separated check IDs for bulk delete |
| `--archive` / `--no-archive` | FLAG | `--archive` | No | Soft-delete (archive) or hard-delete |

## Activate Checks

Re-activate (unarchive) archived checks:

```bash
qualytics checks activate --id 100
qualytics checks activate --ids "100,101,102"
```

### Options

| Option | Type | Default | Required | Description |
|--------|------|---------|----------|-------------|
| `--id` | INTEGER | — | No | Single check ID to activate |
| `--ids` | TEXT | — | No | Comma-separated check IDs for bulk activation |

## Export Checks

Export quality checks to a directory structure organized by container. Each check is saved as a separate YAML file.

```bash
qualytics checks export --datastore-id 1 --output ./checks
qualytics checks export --datastore-id 1 --containers "10,20" --tags "production"
```

### Options

| Option | Type | Default | Required | Description |
|--------|------|---------|----------|-------------|
| `--datastore-id` | INTEGER | — | Yes | Datastore ID to export from |
| `--output`, `-o` | TEXT | `./checks` | No | Output directory |
| `--containers` | TEXT | — | No | Comma-separated container IDs |
| `--tags` | TEXT | — | No | Comma-separated tag names |
| `--status` | TEXT | — | No | Filter by status: `Active`, `Draft`, or `Archived` |

### Export Directory Structure

```text
checks/
  orders/
    isNotNull_customer_id.yaml
    satisfiesExpression_total_positive.yaml
  customers/
    isUnique_email.yaml
```

## Import Checks

Import checks from a directory to one or more datastores. Uses upsert logic — existing checks (matched by `_qualytics_check_uid`) are updated, new checks are created.

```bash
qualytics checks import --datastore-id 1 --input ./checks
qualytics checks import --datastore-id 1 --datastore-id 2 --input ./checks --dry-run
```

### Options

| Option | Type | Default | Required | Description |
|--------|------|---------|----------|-------------|
| `--datastore-id` | INTEGER | — | Yes | Target datastore ID (repeat for multiple) |
| `--input`, `-i` | TEXT | `./checks` | No | Input directory with check files |
| `--dry-run` | FLAG | `false` | No | Preview what would be created or updated |

!!! tip "Idempotent imports"
    Each exported check includes a `_qualytics_check_uid` field that ensures idempotent import. Re-importing the same checks updates them rather than creating duplicates.

## Export Check Templates

Export check templates to an enrichment datastore or a local file:

```bash
# Export to enrichment datastore
qualytics checks export-templates --enrichment_datastore_id 10

# Export to local file
qualytics checks export-templates --output ./templates.yaml

# Filter by rule types and tags
qualytics checks export-templates \
    --output ./templates.yaml \
    --rules "isNotNull,isUnique" \
    --tags "production"
```

### Options

| Option | Type | Default | Required | Description |
|--------|------|---------|----------|-------------|
| `--enrichment_datastore_id` | INTEGER | — | No | Enrichment datastore ID for export |
| `--check_templates` | TEXT | — | No | Comma-separated template IDs |
| `--status` | BOOLEAN | — | No | Template locked status (`true` for locked, `false` for unlocked) |
| `--rules` | TEXT | — | No | Comma-separated rule types |
| `--tags` | TEXT | — | No | Comma-separated tag names |
| `--output` | TEXT | `~/.qualytics/data_checks_template.yaml` | No | Output file path |
| `--format` | TEXT | `yaml` | No | Output format: `yaml` or `json` |

## Import Check Templates

Import check templates from a file. Creates new templates only (no updates to existing).

```bash
qualytics checks import-templates --input ./templates.yaml
```

### Options

| Option | Type | Default | Required | Description |
|--------|------|---------|----------|-------------|
| `--input` | TEXT | `~/.qualytics/data_checks_template.yaml` | No | Input file path |
