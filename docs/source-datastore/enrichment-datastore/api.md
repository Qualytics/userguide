# Datastore Enrichment API

The Enrichment API allows you to link and unlink enrichment datastores to source datastores, and update enrichment settings — all programmatically.

!!! tip
    For complete API documentation, including request/response schemas, visit the [API docs](https://demo.qualytics.io/api/docs){:target="_blank"}.

## Link an Enrichment Datastore

Link an existing enrichment datastore to a source datastore.

### Request

```bash
PATCH /api/datastores/{datastore_id}/enrichment/{enrich_store_id}
```

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `datastore_id` | `integer` | The source datastore ID. |
| `enrich_store_id` | `integer` | The enrichment datastore ID to link. |

### Example

```bash
curl -X PATCH "https://your-instance.qualytics.io/api/datastores/42/enrichment/100" \
  -H "Authorization: Bearer YOUR_API_TOKEN"
```

### Response

Returns the updated source datastore with the enrichment datastore linked:

```json
{
  "id": 42,
  "name": "Healthcare Database",
  "store_type": "jdbc",
  "enrichment_only": false,
  "enrichment_prefix": "_healthcare_database",
  "enrichment_source_record_limit": 10,
  "enrichment_remediation_strategy": "none",
  "high_count_rollup_threshold": 10,
  "enrich_datastore": {
    "id": 100,
    "name": "Healthcare Enrichment",
    "store_type": "jdbc",
    "type": "postgresql",
    "enrichment_only": true
  }
}
```

## Unlink an Enrichment Datastore

Remove the enrichment link from a source datastore. Requires **Admin** role.

### Request

```bash
DELETE /api/datastores/{datastore_id}/enrichment
```

### Example

```bash
curl -X DELETE "https://your-instance.qualytics.io/api/datastores/42/enrichment" \
  -H "Authorization: Bearer YOUR_API_TOKEN"
```

### Response

Returns `204 No Content` on success. The enrichment link is removed and the remediation strategy is automatically reset to `None`.

!!! warning
    You cannot unlink an enrichment datastore if the source datastore has active **Export** or **Materialize** operations in flows or scheduled operations.

## Update Enrichment Settings

Update the enrichment settings on a source datastore. These settings control how data is written to the enrichment datastore during Scan operations.

### Request

```bash
PUT /api/datastores/{datastore_id}
```

Include only the fields you want to change:

### Request Schema (Enrichment Fields)

| Field | Type | Default | Range | Description |
| :--- | :--- | :---: | :---: | :--- |
| `enrichment_prefix` | `string` | Auto-generated | Max 60 chars | Prefix for enrichment table names. Auto-normalized to snake_case with leading underscore. |
| `enrichment_source_record_limit` | `integer` | `10` | 1–1,000,000,000 | Max source records stored per anomaly as examples. |
| `enrichment_remediation_strategy` | `string` | `"none"` | `none`, `append`, `overwrite` | How anomalous source tables are replicated to the enrichment datastore. |
| `high_count_rollup_threshold` | `integer` | `10` | 1–1,000 | Max individual anomalies per check before they are rolled up. |

### Example: Change Remediation Strategy to Append

```bash
curl -X PUT "https://your-instance.qualytics.io/api/datastores/42" \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "enrichment_remediation_strategy": "append"
  }'
```

### Example: Increase Source Record Limit and Change Prefix

```bash
curl -X PUT "https://your-instance.qualytics.io/api/datastores/42" \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "enrichment_prefix": "_healthcare_prod",
    "enrichment_source_record_limit": 100
  }'
```

### Example: Disable Remediation and Reset Rollup Threshold

```bash
curl -X PUT "https://your-instance.qualytics.io/api/datastores/42" \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "enrichment_remediation_strategy": "none",
    "high_count_rollup_threshold": 10
  }'
```

### Response

Returns the updated source datastore:

```json
{
  "id": 42,
  "name": "Healthcare Database",
  "store_type": "jdbc",
  "enrichment_prefix": "_healthcare_prod",
  "enrichment_source_record_limit": 100,
  "enrichment_remediation_strategy": "append",
  "high_count_rollup_threshold": 10,
  "enrich_datastore": {
    "id": 100,
    "name": "Healthcare Enrichment",
    "store_type": "jdbc",
    "type": "postgresql",
    "enrichment_only": true
  }
}
```

## Get Enrichment Info for a Source Datastore

Retrieve the current enrichment configuration and linked enrichment datastore for a source datastore.

### Request

```bash
GET /api/datastores/{datastore_id}
```

### Example

```bash
curl -X GET "https://your-instance.qualytics.io/api/datastores/42" \
  -H "Authorization: Bearer YOUR_API_TOKEN"
```

### Response (Enrichment Fields)

```json
{
  "id": 42,
  "name": "Healthcare Database",
  "enrichment_only": false,
  "enrichment_prefix": "_healthcare_prod",
  "enrichment_source_record_limit": 100,
  "enrichment_remediation_strategy": "append",
  "high_count_rollup_threshold": 10,
  "enrich_datastore": {
    "id": 100,
    "name": "Healthcare Enrichment",
    "store_type": "jdbc",
    "type": "postgresql",
    "enrichment_only": true
  }
}
```

If no enrichment datastore is linked, `enrich_datastore` will be `null`.

## Important Notes

!!! note "Permissions"
    **Linking** requires at least **Member** role with **Editor** team permission on the source datastore. **Unlinking** requires **Admin** role. **Updating settings** requires **Member** role with **Editor** team permission.

!!! note "Prefix Normalization"
    The `enrichment_prefix` is automatically normalized to snake_case with a leading underscore. For example, `Analytics Bronze` becomes `_analytics_bronze`. Maximum length is 60 characters.

!!! warning "Remediation Strategy Constraint"
    You cannot run a Scan with a remediation strategy other than `none` if no enrichment datastore is linked. Qualytics will return an error.
