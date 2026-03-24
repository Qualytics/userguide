# Teams

View teams in your Qualytics instance. Teams are managed through the Qualytics web application — the CLI provides read-only access for listing and inspecting team details.

## List Teams

```bash
qualytics teams list
qualytics teams list --name "Data Engineering"
qualytics teams list --format json --page 1 --size 10
```

### Options

| Option | Type | Default | Required | Description |
|--------|------|---------|----------|-------------|
| `--name` | TEXT | — | No | Filter by team name (search) |
| `--format` | TEXT | `yaml` | No | Output format: `yaml` or `json` |
| `--page` | INTEGER | 1 | No | Page number for pagination |
| `--size` | INTEGER | 50 | No | Page size for pagination |

## Get a Team

Retrieve details for a single team by ID:

```bash
qualytics teams get --id 5
qualytics teams get --id 5 --format json
```

### Options

| Option | Type | Default | Required | Description |
|--------|------|---------|----------|-------------|
| `--id` | INTEGER | — | Yes | Team ID |
| `--format` | TEXT | `yaml` | No | Output format: `yaml` or `json` |
