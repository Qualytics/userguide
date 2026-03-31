# Datastore Tags API

Tags on datastores are managed through the `PUT /api/datastores/{id}` endpoint. There is no separate endpoint for tag assignment — you update the `tags` field in the datastore update payload, and Qualytics automatically determines which tags to add and which to remove.

!!! tip
    For complete API documentation, including request/response schemas, visit the [API docs](https://demo.qualytics.io/api/docs){:target="_blank"}.

## Assign Tags to a Datastore

To assign tags, send a `PUT` request with the desired tag names in the `tags` array. If a tag doesn't exist yet, it will be **automatically created**.

### Request

```bash
PUT /api/datastores/{datastore_id}
```

```json
{
  "tags": ["production", "critical", "hipaa"]
}
```

### Example

```bash
curl -X PUT "https://your-instance.qualytics.io/api/datastores/42" \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "tags": ["production", "critical", "hipaa"]
  }'
```

### Response

```json
{
  "id": 42,
  "name": "Healthcare Database",
  "store_type": "jdbc",
  "global_tags": [
    {
      "id": 1,
      "name": "production",
      "type": "global",
      "color": "#4CAF50",
      "category": "environment",
      "weight_modifier": 1
    },
    {
      "id": 2,
      "name": "critical",
      "type": "global",
      "color": "#F44336",
      "category": null,
      "weight_modifier": 5
    },
    {
      "id": 3,
      "name": "hipaa",
      "type": "global",
      "color": "#2196F3",
      "category": "compliance",
      "weight_modifier": 1
    }
  ]
}
```

## Unassign Tags from a Datastore

To remove tags, send the same `PUT` request with the updated `tags` array — **excluding the tags you want to remove**. Qualytics compares the desired list with the current tags and removes any that are no longer present.

### Example: Remove a Single Tag

If the datastore currently has tags `["production", "critical", "hipaa"]` and you want to remove `hipaa`:

```bash
curl -X PUT "https://your-instance.qualytics.io/api/datastores/42" \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "tags": ["production", "critical"]
  }'
```

### Example: Remove All Tags

To remove all tags from a datastore, send an empty array:

```bash
curl -X PUT "https://your-instance.qualytics.io/api/datastores/42" \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "tags": []
  }'
```

## Important Notes

!!! warning "Tag Replacement"
    The `tags` field uses a **replacement strategy** — the list you send becomes the new complete set of tags. Any tags not included in the array will be removed from the datastore.

!!! note "Tag Inheritance"
    When tags are updated on a datastore, the changes automatically cascade to all containers, fields, checks, and anomalies within the datastore. Container quality score weights are also recalculated based on tag weight modifiers.

!!! note "Auto-Creation"
    If you include a tag name that doesn't exist yet, Qualytics will automatically create it as a **Global** tag. You need at least the **Editor** role for tag auto-creation to work.

## Request Schema

| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| `tags` | `list[string]` | No | List of tag names to assign. Pass `null` to leave tags unchanged, or `[]` to remove all tags. |

## Response Schema (Tag Object)

| Field | Type | Description |
| :--- | :--- | :--- |
| `id` | `integer` | Unique tag identifier. |
| `name` | `string` | Tag name. |
| `type` | `string` | Tag type: `global`, `external`, `entity`, or `lineage`. |
| `color` | `string` | Hex color code (e.g., `#4CAF50`). |
| `description` | `string` | Optional tag description. |
| `category` | `string` | Optional tag category (e.g., `compliance`, `environment`). |
| `weight_modifier` | `integer` | Weight modifier for quality score calculations (-10 to 10). |

## Bulk Tag Assignment (Multi-Schema Creation)

When creating multiple datastores via the [Multiple-Schema](../add-datastores/multi-schema/overview.md) flow, you can assign tags to **all datastores in the batch** by including the `tags` field in the bulk creation request. All datastores created in the batch will receive the same set of tags.

### Endpoint (Existing Connection)

```bash
POST /api/connections/{connection_id}/datastores/bulk
```

### Endpoint (New Connection)

```bash
POST /api/connections/datastores/bulk
```

### Example

```bash
curl -X POST "https://your-instance.qualytics.io/api/connections/5/datastores/bulk" \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "schemas": ["public", "staging", "analytics"],
    "name_template": "production_{{schema}}",
    "database": "my_database",
    "tags": ["production", "critical"],
    "teams": ["data-engineering"],
    "trigger_catalog": true
  }'
```

This will create 3 datastores (`production_public`, `production_staging`, `production_analytics`) — all tagged with `production` and `critical`.

!!! note "Bulk removal not supported"
    There is no dedicated bulk endpoint for removing tags from multiple existing datastores. To remove tags from existing datastores, use the individual `PUT /api/datastores/{id}` endpoint for each datastore.
