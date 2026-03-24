# Tags

Create, list, and delete tags used to organize datastores, containers, checks, and anomalies across your Qualytics instance.

## List Tags

```bash
qualytics tags list
qualytics tags list --type global --category "data-quality"
qualytics tags list --name "prod" --format json
```

### Options

| Option | Type | Default | Required | Description |
|--------|------|---------|----------|-------------|
| `--name` | TEXT | — | No | Filter by tag name (search) |
| `--type` | TEXT | — | No | Filter by tag type: `global` or `external` |
| `--category` | TEXT | — | No | Filter by category |
| `--format` | TEXT | `yaml` | No | Output format: `yaml` or `json` |
| `--page` | INTEGER | 1 | No | Page number for pagination |
| `--size` | INTEGER | 50 | No | Page size for pagination |

## Get a Tag

Retrieve a single tag by name:

```bash
qualytics tags get --name "production"
qualytics tags get --name "production" --format json
```

### Options

| Option | Type | Default | Required | Description |
|--------|------|---------|----------|-------------|
| `--name` | TEXT | — | Yes | Tag name |
| `--format` | TEXT | `yaml` | No | Output format: `yaml` or `json` |

!!! note
    Tags are looked up by name, not by numeric ID.

## Create a Tag

```bash
qualytics tags create --name "production" --color "#FF5733" --description "Production resources"
qualytics tags create --name "high-priority" --weight-modifier 5 --category "priority"
```

### Options

| Option | Type | Default | Required | Description |
|--------|------|---------|----------|-------------|
| `--name` | TEXT | — | Yes | Tag name |
| `--color` | TEXT | — | No | Hex color code (e.g., `#FF5733`) |
| `--description` | TEXT | — | No | Tag description |
| `--category` | TEXT | — | No | Tag category |
| `--weight-modifier` | INTEGER | — | No | Weight modifier for scoring (-10 to 10) |
| `--format` | TEXT | `yaml` | No | Output format: `yaml` or `json` |

## Delete a Tag

Delete a tag by name:

```bash
qualytics tags delete --name "obsolete-tag"
```

### Options

| Option | Type | Default | Required | Description |
|--------|------|---------|----------|-------------|
| `--name` | TEXT | — | Yes | Tag name to delete |

!!! warning
    Deleting a tag removes it from all resources it's attached to.
