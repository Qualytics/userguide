# Datastore Tags API

Tags on datastores are managed through the `PUT /api/datastores/{id}` endpoint. There is no separate endpoint for tag assignment — you update the `tags` field in the datastore update payload, and Qualytics automatically determines which tags to add and which to remove.

!!! tip
    For complete API documentation, including request/response schemas, visit the [API docs](https://demo.qualytics.io/api/docs){:target="_blank"}.

## Get Current Tags

Before updating tags, retrieve the current tags on a datastore to avoid accidentally removing existing ones (the `tags` field uses a replacement strategy).

**Endpoint**: `GET /api/datastores/{datastore_id}`

**Permission**: Member or above

??? example "Example request and response"

    **Request**:

    ```bash
    curl -X GET "https://your-instance.qualytics.io/api/datastores/42" \
      -H "Authorization: Bearer YOUR_API_TOKEN"
    ```

    **Response** (abbreviated — the full response includes all datastore fields):

    ```json
    {
      "id": 42,
      "name": "Healthcare Database",
      "description": "Patient and clinical data warehouse",
      "store_type": "jdbc",
      "global_tags": [
        {
          "id": 1,
          "name": "production",
          "type": "global",
          "color": "#4CAF50",
          "description": "Production environment",
          "category": "environment",
          "weight_modifier": 1
        }
      ]
    }
    ```

!!! info "tags vs global_tags"
    In **requests**, you send `tags` as a list of **tag name strings** (e.g., `["production", "critical"]`). In **responses**, the datastore returns `global_tags` as a list of **tag objects** with full details (id, name, type, color, category, weight_modifier, description). Other tag types (external, entity, lineage) may appear in separate fields if applicable.

---

## Assign Tags to a Datastore

To assign tags, send a `PUT` request with the desired tag names in the `tags` array.

**Endpoint**: `PUT /api/datastores/{datastore_id}`

**Permission**: Editor or above

??? example "Example request and response"

    **Request**:

    ```bash
    curl -X PUT "https://your-instance.qualytics.io/api/datastores/42" \
      -H "Authorization: Bearer YOUR_API_TOKEN" \
      -H "Content-Type: application/json" \
      -d '{
        "tags": ["production", "critical", "hipaa"]
      }'
    ```

    **Response** (abbreviated — the full response includes all datastore fields):

    ```json
    {
      "id": 42,
      "name": "Healthcare Database",
      "description": "Patient and clinical data warehouse",
      "store_type": "jdbc",
      "global_tags": [
        {
          "id": 1,
          "name": "production",
          "type": "global",
          "color": "#4CAF50",
          "description": "Production environment",
          "category": "environment",
          "weight_modifier": 1
        },
        {
          "id": 2,
          "name": "critical",
          "type": "global",
          "color": "#F44336",
          "description": null,
          "category": null,
          "weight_modifier": 5
        },
        {
          "id": 3,
          "name": "hipaa",
          "type": "global",
          "color": "#2196F3",
          "description": "HIPAA compliance scope",
          "category": "compliance",
          "weight_modifier": 1
        }
      ]
    }
    ```

---

## Unassign Tags from a Datastore

To remove tags, send the same `PUT` request with the updated `tags` array — **excluding the tags you want to remove**. Qualytics compares the desired list with the current tags and removes any that are no longer present.

??? example "Remove a single tag"

    If the datastore currently has tags `["production", "critical", "hipaa"]` and you want to remove `hipaa`:

    ```bash
    curl -X PUT "https://your-instance.qualytics.io/api/datastores/42" \
      -H "Authorization: Bearer YOUR_API_TOKEN" \
      -H "Content-Type: application/json" \
      -d '{
        "tags": ["production", "critical"]
      }'
    ```

??? example "Remove all tags"

    To remove all tags from a datastore, send an empty array:

    ```bash
    curl -X PUT "https://your-instance.qualytics.io/api/datastores/42" \
      -H "Authorization: Bearer YOUR_API_TOKEN" \
      -H "Content-Type: application/json" \
      -d '{
        "tags": []
      }'
    ```

---

## Important Notes

!!! warning "Tag Replacement"
    The `tags` field uses a **replacement strategy** — the list you send becomes the new complete set of tags. Any tags not included in the array will be removed from the datastore. Always retrieve the current tags first with `GET /api/datastores/{id}` before updating.

!!! note "Tag Inheritance"
    When tags are updated on a datastore, the changes automatically cascade to all containers, fields, checks, and anomalies within the datastore. Container quality score weights are also recalculated based on tag weight modifiers.

!!! note "Auto-Creation"
    If you include a tag name that doesn't exist yet, Qualytics will automatically create it as a **Global** tag. This works for any user with the **Editor** role or above — no separate Admin permission is needed for auto-creation via the API.

---

## Error Responses

| Status Code | Description |
| :--- | :--- |
| `401 Unauthorized` | Missing or invalid API token. |
| `403 Forbidden` | User does not have Editor permission on the datastore's teams. |
| `404 Not Found` | Datastore with the specified ID does not exist. |
| `422 Unprocessable Entity` | Invalid request body (e.g., `tags` is not a list of strings). |

??? example "Error response examples"

    **401 Unauthorized**:

    ```json
    { "detail": "Not authenticated" }
    ```

    **403 Forbidden**:

    ```json
    { "detail": "You must have editor permission in at least one of these teams: ['Data Platform']" }
    ```

    **404 Not Found**:

    ```json
    { "detail": "Datastore with id 999 not found" }
    ```

    **422 Unprocessable Entity**:

    ```json
    { "detail": [{ "loc": ["body", "tags", 0], "msg": "str type expected", "type": "type_error.str" }] }
    ```

---

## Request Schema

| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| `tags` | `list[string]` | No | List of tag names to assign. Pass `null` to leave tags unchanged, or `[]` to remove all tags. |

## Response Schema (Tag Object)

Each tag in the `global_tags` array has the following structure:

| Field | Type | Description |
| :--- | :--- | :--- |
| `id` | `integer` | Unique tag identifier. |
| `name` | `string` | Tag name. |
| `type` | `string` | Tag type: `global`, `external`, `entity`, or `lineage`. |
| `color` | `string` | Hex color code (e.g., `#4CAF50`). |
| `description` | `string` | Optional tag description. |
| `category` | `string` | Optional tag category (e.g., `compliance`, `environment`). |
| `weight_modifier` | `integer` | Weight modifier for quality score calculations (-10 to 10). |

---

## Bulk Tag Assignment (Multi-Schema Creation)

When creating multiple datastores via the [Multiple-Schema](../add-datastores/multi-schema/overview.md){:target="_blank"} flow, you can assign tags to **all datastores in the batch** by including the `tags` field in the bulk creation request.

??? example "Bulk create with tags"

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

    This creates 3 datastores (`production_public`, `production_staging`, `production_analytics`) — all tagged with `production` and `critical`.

!!! note "Bulk removal not supported"
    There is no dedicated bulk endpoint for removing tags from multiple existing datastores. To remove tags from existing datastores, use the individual `PUT /api/datastores/{id}` endpoint for each datastore.
