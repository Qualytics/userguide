# Datastore Enrichment API

The Enrichment API allows you to link and unlink enrichment datastores to source datastores, and update enrichment settings — all programmatically.

!!! tip
    For complete API documentation, including request/response schemas, visit the [API docs](https://demo.qualytics.io/api/docs){:target="_blank"}.

All endpoints use the base URL of your Qualytics deployment (e.g., `https://your-instance.qualytics.io/api`).

---

## Link an Enrichment Datastore

Link an existing enrichment datastore to a source datastore.

**Endpoint**: `PATCH /api/datastores/{datastore_id}/enrichment/{enrich_store_id}`

**Permission**: Member user role + Editor team permission on the source datastore

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `datastore_id` | `integer` | The source datastore ID. |
| `enrich_store_id` | `integer` | The enrichment datastore ID to link. |

!!! note "Request Details"
    No JSON body is required — the enrichment datastore ID is specified in the URL path. This endpoint only creates the link; to configure enrichment settings (prefix, strategy, limits), send a separate `PUT /api/datastores/{datastore_id}` request.

??? example "Example request and response"

    **Request** (no body required):

    ```bash
    curl -X PATCH "https://your-instance.qualytics.io/api/datastores/42/enrichment/100" \
      -H "Authorization: Bearer YOUR_TOKEN"
    ```

    **Response** (abbreviated — the full response includes all datastore fields):

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

!!! info "Idempotent"
    Calling this endpoint multiple times with the same `enrich_store_id` is safe — the link is re-confirmed. Calling it with a **different** ID will switch the enrichment datastore automatically.

For the UI equivalent, see [Link Enrichment Datastore](../managing-datastores/link-enrichment.md){:target="_blank"}.

---

## Unlink an Enrichment Datastore

Remove the enrichment link from a source datastore. No request body is required.

**Endpoint**: `DELETE /api/datastores/{datastore_id}/enrichment`

**Permission**: Admin user role (no team permission check)

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `datastore_id` | `integer` | The source datastore ID. |

!!! note "Idempotent"
    Calling this endpoint when no enrichment datastore is linked returns `204 No Content` without error — the operation is a no-op.

??? example "Example request and response"

    **Request** (no body required):

    ```bash
    curl -X DELETE "https://your-instance.qualytics.io/api/datastores/42/enrichment" \
      -H "Authorization: Bearer YOUR_TOKEN"
    ```

    **Response**: `204 No Content`

    The enrichment link is removed and the remediation strategy is automatically reset to `None`.

!!! warning
    You cannot unlink an enrichment datastore if the source datastore has active **Export** or **Materialize** operations in flows or scheduled operations.

For the UI equivalent, see [Unlink Enrichment Datastore](../managing-datastores/unlink-enrichment.md){:target="_blank"}.

---

## Update Enrichment Settings

Update the enrichment settings on a source datastore. These settings control how data is written to the enrichment datastore during Scan operations.

**Endpoint**: `PUT /api/datastores/{datastore_id}`

**Permission**: Member user role + Editor team permission on the source datastore

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `datastore_id` | `integer` | The source datastore ID. |

!!! warning "Shared Endpoint"
    This is the **general datastore update endpoint** — it can modify any datastore field, not just enrichment settings. Only include the enrichment fields you want to change. Fields you omit will remain unchanged (partial update semantics despite using PUT).

**Request Body** (enrichment fields):

| Field | Type | Default | Range | Description |
| :--- | :--- | :---: | :---: | :--- |
| `enrichment_prefix` | `string` | Auto-generated | Max 60 chars | Prefix for enrichment table names. Auto-normalized to snake_case with leading underscore. |
| `enrichment_source_record_limit` | `integer` | `10` | 1–1,000,000,000 | Max source records stored per anomaly as examples. |
| `enrichment_remediation_strategy` | `string` | `"none"` | `none`, `append`, `overwrite` | How anomalous source tables are replicated to the enrichment datastore. |
| `high_count_rollup_threshold` | `integer` | `10` | 1–1,000 | Max individual anomalies per check before they are rolled up. |

!!! warning "Remediation Strategy Constraint"
    You cannot run a Scan with `enrichment_remediation_strategy` set to `append` or `overwrite` if no enrichment datastore is linked. Qualytics will return an error.

??? example "Change remediation strategy to Append"

    **Request**:

    ```bash
    curl -X PUT "https://your-instance.qualytics.io/api/datastores/42" \
      -H "Authorization: Bearer YOUR_TOKEN" \
      -H "Content-Type: application/json" \
      -d '{
        "enrichment_remediation_strategy": "append"
      }'
    ```

    **Response** (abbreviated):

    ```json
    {
      "id": 42,
      "name": "Healthcare Database",
      "enrichment_prefix": "_healthcare_database",
      "enrichment_source_record_limit": 10,
      "enrichment_remediation_strategy": "append",
      "high_count_rollup_threshold": 10,
      "enrich_datastore": {
        "id": 100,
        "name": "Healthcare Enrichment"
      }
    }
    ```

??? example "Increase source record limit and change prefix"

    **Request**:

    ```bash
    curl -X PUT "https://your-instance.qualytics.io/api/datastores/42" \
      -H "Authorization: Bearer YOUR_TOKEN" \
      -H "Content-Type: application/json" \
      -d '{
        "enrichment_prefix": "_healthcare_prod",
        "enrichment_source_record_limit": 100
      }'
    ```

    **Response** (abbreviated):

    ```json
    {
      "id": 42,
      "name": "Healthcare Database",
      "enrichment_prefix": "_healthcare_prod",
      "enrichment_source_record_limit": 100,
      "enrichment_remediation_strategy": "append",
      "high_count_rollup_threshold": 10,
      "enrich_datastore": {
        "id": 100,
        "name": "Healthcare Enrichment"
      }
    }
    ```

??? example "Disable remediation and reset rollup threshold"

    **Request**:

    ```bash
    curl -X PUT "https://your-instance.qualytics.io/api/datastores/42" \
      -H "Authorization: Bearer YOUR_TOKEN" \
      -H "Content-Type: application/json" \
      -d '{
        "enrichment_remediation_strategy": "none",
        "high_count_rollup_threshold": 10
      }'
    ```

    **Response** (abbreviated):

    ```json
    {
      "id": 42,
      "name": "Healthcare Database",
      "enrichment_prefix": "_healthcare_prod",
      "enrichment_source_record_limit": 100,
      "enrichment_remediation_strategy": "none",
      "high_count_rollup_threshold": 10,
      "enrich_datastore": {
        "id": 100,
        "name": "Healthcare Enrichment"
      }
    }
    ```

For the UI equivalent, see [Link Enrichment Datastore — Enrichment Settings](../managing-datastores/link-enrichment.md#enrichment-settings){:target="_blank"}.

---

## Get Enrichment Info

Retrieve the current enrichment configuration and linked enrichment datastore for a source datastore.

**Endpoint**: `GET /api/datastores/{datastore_id}`

**Permission**: Member user role + Reporter team permission on the source datastore

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `datastore_id` | `integer` | The source datastore ID. |

!!! note "General Datastore Endpoint"
    This is the **general datastore GET endpoint** — it returns all datastore fields, not just enrichment. The example below shows only the enrichment-related fields for clarity.

??? example "Example request and response"

    **Request**:

    ```bash
    curl -X GET "https://your-instance.qualytics.io/api/datastores/42" \
      -H "Authorization: Bearer YOUR_TOKEN"
    ```

    **Response** (enrichment fields only — the full response includes all datastore fields):

    ```json
    {
      "id": 42,
      "name": "Healthcare Database",
      "enrichment_only": false,
      "enrichment_prefix": "_healthcare_prod",
      "enrichment_source_record_limit": 100,
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

    If no enrichment datastore is linked, `enrich_datastore` will be `null`.

---

## Error Responses

| Status Code | Description |
| :--- | :--- |
| `401 Unauthorized` | Missing or invalid API token. |
| `403 Forbidden` | User does not have the required role or team permission. |
| `404 Not Found` | Source datastore or enrichment datastore with the specified ID does not exist. |
| `409 Conflict` | Cannot link (target is enrichment-only) or cannot unlink (active Export/Materialize operations). |
| `422 Unprocessable Entity` | Invalid request body (e.g., remediation strategy not one of `none`, `append`, `overwrite`). |

??? example "Error response examples"

    **403 Forbidden**:

    ```json
    { "detail": "You must have editor permission in at least one of these teams: ['Data Platform']" }
    ```

    **404 Not Found**:

    ```json
    { "detail": "Datastore id: 999 not found" }
    ```

    **409 Conflict** (linking an enrichment-only datastore as source):

    ```json
    { "detail": "The datastore id: 100 is an enrichment store" }
    ```

    **409 Conflict** (unlinking with active Export/Materialize):

    ```json
    { "detail": "Cannot disconnect enrichment datastore: active export or materialize operations exist" }
    ```

---

## Permission Summary

| Operation | Minimum Permission |
| :--- | :--- |
| Link enrichment datastore | Member user role + Editor team permission |
| Unlink enrichment datastore | Admin user role |
| Update enrichment settings | Member user role + Editor team permission |
| Get enrichment info | Member user role + Reporter team permission |

!!! note "Prefix Normalization"
    The `enrichment_prefix` is automatically normalized to snake_case with a leading underscore. For example, `Analytics Bronze` becomes `_analytics_bronze`. Maximum length is 60 characters.
