# Anomalies

View and manage anomalies detected by quality check scans.

## Get an Anomaly

```bash
qualytics anomalies get --id 500
qualytics anomalies get --id 500 --format json
```

### Options

| Option | Type | Default | Required | Description |
|--------|------|---------|----------|-------------|
| `--id` | INTEGER | — | Yes | Anomaly ID |
| `--format` | TEXT | `yaml` | No | Output format: `yaml` or `json` |

## List Anomalies

```bash
qualytics anomalies list --datastore-id 1
qualytics anomalies list --datastore-id 1 --status "Active,Acknowledged" --type record
qualytics anomalies list --datastore-id 1 --start-date 2026-01-01 --end-date 2026-03-23
```

### Options

| Option | Type | Default | Required | Description |
|--------|------|---------|----------|-------------|
| `--datastore-id` | INTEGER | — | Yes | Datastore ID |
| `--container` | INTEGER | — | No | Container ID to filter by |
| `--check-id` | INTEGER | — | No | Quality check ID to filter by |
| `--status` | TEXT | — | No | Comma-separated statuses: `Active`, `Acknowledged`, `Resolved`, `Invalid`, `Duplicate`, `Discarded` |
| `--type` | TEXT | — | No | Anomaly type: `shape` or `record` |
| `--tag` | TEXT | — | No | Tag name to filter by |
| `--start-date` | TEXT | — | No | Start date (`YYYY-MM-DD`) |
| `--end-date` | TEXT | — | No | End date (`YYYY-MM-DD`) |
| `--format` | TEXT | `yaml` | No | Output format: `yaml` or `json` |

## Update Anomalies

Change the status of active anomalies:

```bash
# Update a single anomaly
qualytics anomalies update --id 500 --status Acknowledged

# Bulk update
qualytics anomalies update --ids "500,501,502" --status Acknowledged --description "Under review"
```

### Options

| Option | Type | Default | Required | Description |
|--------|------|---------|----------|-------------|
| `--id` | INTEGER | — | No | Single anomaly ID |
| `--ids` | TEXT | — | No | Comma-separated anomaly IDs for bulk update |
| `--status` | TEXT | — | Yes | New status: `Active` or `Acknowledged` |
| `--description` | TEXT | — | No | Update description |
| `--tags` | TEXT | — | No | Comma-separated tag names |

## Archive Anomalies

Soft-delete anomalies with a resolution status:

```bash
# Archive as resolved
qualytics anomalies archive --id 500 --status Resolved

# Bulk archive as invalid
qualytics anomalies archive --ids "500,501,502" --status Invalid
```

### Options

| Option | Type | Default | Required | Description |
|--------|------|---------|----------|-------------|
| `--id` | INTEGER | — | No | Single anomaly ID |
| `--ids` | TEXT | — | No | Comma-separated anomaly IDs for bulk archive |
| `--status` | TEXT | `Resolved` | No | Archive status: `Resolved`, `Invalid`, `Duplicate`, or `Discarded` |

## Delete Anomalies

Permanently hard-delete anomalies:

```bash
qualytics anomalies delete --id 500
qualytics anomalies delete --ids "500,501,502"
```

### Options

| Option | Type | Default | Required | Description |
|--------|------|---------|----------|-------------|
| `--id` | INTEGER | — | No | Single anomaly ID |
| `--ids` | TEXT | — | No | Comma-separated anomaly IDs for bulk delete |

!!! warning
    Hard-deletes are permanent and cannot be undone. Consider archiving instead.

## Anomaly Statuses

| Status | Type | Description |
|--------|------|-------------|
| `Active` | Open | Newly detected, requires attention |
| `Acknowledged` | Open | Reviewed, under investigation |
| `Resolved` | Archived | Fixed, no longer an issue |
| `Invalid` | Archived | False positive, not a real anomaly |
| `Duplicate` | Archived | Same issue as another anomaly |
| `Discarded` | Archived | Intentionally ignored |
