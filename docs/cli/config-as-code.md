# Config as Code

Export your entire Qualytics configuration to a hierarchical YAML folder structure, version-control it with Git, and import it into other environments. This enables infrastructure-as-code workflows for data quality.

## Export Configuration

```bash
qualytics config export --datastore-id 1 --output ./qualytics-export
```

Export multiple datastores:

```bash
qualytics config export --datastore-id 1 --datastore-id 2 --datastore-id 3
```

Export only specific resource types:

```bash
qualytics config export --datastore-id 1 --include connections,datastores,checks
```

### Options

| Option | Type | Default | Required | Description |
|--------|------|---------|----------|-------------|
| `--datastore-id` | INTEGER | — | Yes | Datastore ID to export (repeat for multiple) |
| `--output`, `-o` | TEXT | `./qualytics-export` | No | Root output directory |
| `--include` | TEXT | — | No | Comma-separated resource types: `connections`, `datastores`, `containers`, `computed_fields`, `checks` |

### Export Directory Structure

```text
qualytics-export/
├── connections/
│   └── production-db.yaml
├── datastores/
│   └── orders-production/
│       ├── _datastore.yaml
│       ├── containers/
│       │   └── orders/
│       │       ├── _container.yaml
│       │       └── computed_fields/
│       │           └── full_name.yaml
│       └── checks/
│           └── orders/
│               ├── isNotNull_customer_id.yaml
│               └── satisfiesExpression_total_positive.yaml
```

### What Gets Exported

- **Connections** — Credentials are replaced with `${ENV_VAR}` placeholders (never stored in plaintext)
- **Datastores** — Configuration, enrichment settings, references connection by name
- **Containers** — Computed container definitions (computed tables, files, joins)
- **Computed Fields** — User-defined field transformations
- **Quality Checks** — Full check definitions with `_qualytics_check_uid` for idempotent import

!!! tip "Git-friendly output"
    Re-running export on the same directory produces zero git diff when nothing has changed. The output is designed for clean version control.

## Import Configuration

```bash
qualytics config import --input ./qualytics-export
```

Preview what would change without making any API calls:

```bash
qualytics config import --input ./qualytics-export --dry-run
```

Import only specific resource types:

```bash
qualytics config import --input ./qualytics-export --include connections,datastores
```

### Options

| Option | Type | Default | Required | Description |
|--------|------|---------|----------|-------------|
| `--input`, `-i` | TEXT | `./qualytics-export` | No | Root input directory |
| `--dry-run` | FLAG | `false` | No | Preview changes without making API calls |
| `--include` | TEXT | — | No | Comma-separated resource types: `connections`, `datastores`, `containers`, `computed_fields`, `checks` |

### Import Order

Resources are imported in dependency order to ensure references resolve correctly:

1. **Connections** — Matched by name
2. **Datastores** — Matched by name, connection resolved by name
3. **Computed containers** — Matched by name within datastore
4. **Computed fields** — Matched by name within container
5. **Quality checks** — Matched by `_qualytics_check_uid`

### Secret Resolution

Connection files use `${ENV_VAR}` placeholders for sensitive values:

```yaml
# connections/production-db.yaml
name: production-db
type: postgresql
host: ${DB_HOST}
port: 5432
username: ${DB_USER}
password: ${DB_PASSWORD}
```

At import time, these are resolved from:

1. Environment variables
2. A `.env` file in the working directory

## Dev-to-Prod Workflow

A typical promotion workflow using config-as-code:

### 1. Export from Dev

```bash
export QUALYTICS_URL=https://dev.qualytics.io
export QUALYTICS_TOKEN=$DEV_TOKEN

qualytics config export --datastore-id 1 --output ./qualytics-config
```

### 2. Version Control

```bash
cd qualytics-config
git add .
git commit -m "Export quality checks from dev"
git push
```

### 3. Import to Production

```bash
export QUALYTICS_URL=https://prod.qualytics.io
export QUALYTICS_TOKEN=$PROD_TOKEN
export DB_HOST=prod-db.example.com
export DB_USER=qualytics_reader
export DB_PASSWORD=$PROD_DB_PASSWORD

# Preview first
qualytics config import --input ./qualytics-config --dry-run

# Apply
qualytics config import --input ./qualytics-config
```

### GitHub Actions Example

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

      - name: Dry-run import
        env:
          QUALYTICS_URL: ${{ secrets.PROD_QUALYTICS_URL }}
          QUALYTICS_TOKEN: ${{ secrets.PROD_QUALYTICS_TOKEN }}
          DB_HOST: ${{ secrets.PROD_DB_HOST }}
          DB_USER: ${{ secrets.PROD_DB_USER }}
          DB_PASSWORD: ${{ secrets.PROD_DB_PASSWORD }}
        run: qualytics config import --input ./qualytics-config --dry-run

      - name: Import to production
        env:
          QUALYTICS_URL: ${{ secrets.PROD_QUALYTICS_URL }}
          QUALYTICS_TOKEN: ${{ secrets.PROD_QUALYTICS_TOKEN }}
          DB_HOST: ${{ secrets.PROD_DB_HOST }}
          DB_USER: ${{ secrets.PROD_DB_USER }}
          DB_PASSWORD: ${{ secrets.PROD_DB_PASSWORD }}
        run: qualytics config import --input ./qualytics-config
```
{% endraw %}
