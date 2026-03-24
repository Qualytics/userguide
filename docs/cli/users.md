# Users

View user accounts in your Qualytics instance. Users are managed through the Qualytics web application — the CLI provides read-only access for listing and inspecting user details.

## List Users

```bash
qualytics users list
qualytics users list --role Admin --type Human
qualytics users list --team "Data Engineering" --format json
```

### Options

| Option | Type | Default | Required | Description |
|--------|------|---------|----------|-------------|
| `--name` | TEXT | — | No | Filter by user name (search) |
| `--role` | TEXT | — | No | Filter by role: `Admin`, `Manager`, `Editor`, or `Member` |
| `--type` | TEXT | — | No | Filter by user type: `Human` or `Service` |
| `--team` | TEXT | — | No | Filter by team name |
| `--include-deleted` | FLAG | `false` | No | Include deleted users in the results |
| `--format` | TEXT | `yaml` | No | Output format: `yaml` or `json` |
| `--page` | INTEGER | 1 | No | Page number for pagination |
| `--size` | INTEGER | 50 | No | Page size for pagination |

## Get a User

Retrieve details for a single user by ID:

```bash
qualytics users get --id 42
qualytics users get --id 42 --format json
```

### Options

| Option | Type | Default | Required | Description |
|--------|------|---------|----------|-------------|
| `--id` | INTEGER | — | Yes | User ID |
| `--format` | TEXT | `yaml` | No | Output format: `yaml` or `json` |
