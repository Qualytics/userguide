# Field Status API

This page documents the API endpoints related to field status operations. Use these endpoints to programmatically manage field statuses, retrieve field profiles, and access masking audit logs.

All endpoints use the base URL of your Qualytics deployment (e.g., `https://your-instance.qualytics.io/api`).

## Field Status Operations

### List Fields

Retrieves a paginated list of fields with optional filters.

**Endpoint**: `GET /api/fields`

**Query Parameters**:

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `container_id` | integer | No | Filter by container ID |
| `datastore` | list[integer] | No | Filter by datastore IDs |
| `container` | list[integer] | No | Filter by container IDs |
| `name` | string | No | Filter by field name |
| `type` | list[string] | No | Filter by field types |
| `tag` | list[string] | No | Filter by tags |
| `status` | list[string] | No | Filter by status: `active`, `masked`, `missing`, `excluded`. When omitted, returns `active` and `missing` fields |

**Response**: Paginated list of field objects.

??? example "Example request and response"

    **Request**:

    ```bash
    curl -X GET "https://your-instance.qualytics.io/api/fields?container_id=42&status=active&status=masked" \
      -H "Authorization: Bearer YOUR_TOKEN"
    ```

    **Response** (abbreviated):

    ```json
    {
      "total": 2,
      "items": [
        {
          "id": 101,
          "name": "customer_email",
          "display_name": null,
          "type": "String",
          "status": "active",
          "completeness": 0.98,
          "nullable": true,
          "quality_score": {
            "total": 95.2
          }
        },
        {
          "id": 102,
          "name": "social_security_number",
          "display_name": "SSN",
          "type": "String",
          "status": "masked",
          "completeness": 1.0,
          "nullable": false,
          "quality_score": {
            "total": 99.1
          }
        }
      ]
    }
    ```

### Get a Single Field

Retrieves a single field by its ID.

**Endpoint**: `GET /api/fields/{id}`

**Path Parameters**:

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `id` | integer | Yes | The field ID |

??? example "Example request and response"

    **Request**:

    ```bash
    curl -X GET "https://your-instance.qualytics.io/api/fields/101" \
      -H "Authorization: Bearer YOUR_TOKEN"
    ```

    **Response**:

    ```json
    {
      "id": 101,
      "name": "customer_email",
      "display_name": null,
      "description": null,
      "type": "String",
      "status": "active",
      "completeness": 0.98,
      "nullable": true,
      "native_type": "varchar",
      "column_size": 255,
      "additional_metadata": {},
      "global_tags": [],
      "latest_profile_id": 5001,
      "quality_score": {
        "total": 95.2
      },
      "computed_field": null
    }
    ```

---

## Mask a Field

Masks a field by updating its status to `masked`. The field remains fully operational (profiled, scanned, quality-checked), but its actual values are hidden across the platform.

**Endpoint**: `PUT /api/fields/{id}`

**Permission**: Editor

??? example "Example request and response"

    **Request**:

    ```bash
    curl -X PUT "https://your-instance.qualytics.io/api/fields/101" \
      -H "Authorization: Bearer YOUR_TOKEN" \
      -H "Content-Type: application/json" \
      -d '{
        "status": "masked"
      }'
    ```

    **Response**:

    ```json
    {
      "id": 101,
      "name": "customer_email",
      "type": "String",
      "status": "masked",
      "completeness": 0.98
    }
    ```

## Unmask a Field

Restores a masked field back to `active` status, making its values visible again.

**Endpoint**: `PUT /api/fields/{id}`

**Permission**: Editor

??? example "Example request and response"

    **Request**:

    ```bash
    curl -X PUT "https://your-instance.qualytics.io/api/fields/102" \
      -H "Authorization: Bearer YOUR_TOKEN" \
      -H "Content-Type: application/json" \
      -d '{
        "status": "active"
      }'
    ```

    **Response**:

    ```json
    {
      "id": 102,
      "name": "social_security_number",
      "type": "String",
      "status": "active",
      "completeness": 1.0
    }
    ```

## Exclude a Field

Excludes a field from quality monitoring. Associated quality checks are archived (except [Expected Schema](/checks/expected-schema-check.md) checks, which are updated to remove the field).

**Endpoint**: `DELETE /api/fields/{id}?archive=true`

**Permission**: Editor

**Query Parameters**:

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `archive` | boolean | `true` | Set to `true` to exclude (archive) the field |

??? example "Example request"

    ```bash
    curl -X DELETE "https://your-instance.qualytics.io/api/fields/101?archive=true" \
      -H "Authorization: Bearer YOUR_TOKEN"
    ```

    **Response**: `204 No Content`

## Restore a Field

Restores an excluded field back to `active` status. Archived quality checks are **not** automatically restored.

**Endpoint**: `POST /api/fields/{id}/restore`

**Permission**: Editor

??? example "Example request and response"

    **Request**:

    ```bash
    curl -X POST "https://your-instance.qualytics.io/api/fields/101/restore" \
      -H "Authorization: Bearer YOUR_TOKEN"
    ```

    **Response**:

    ```json
    {
      "id": 101,
      "name": "customer_email",
      "type": "String",
      "status": "active",
      "completeness": 0.98
    }
    ```

## Permanently Delete a Field

Permanently removes a field from the platform. Only allowed for **missing** fields that have never been referenced by any quality check.

**Endpoint**: `DELETE /api/fields/{id}?archive=false`

**Permission**: Editor

**Query Parameters**:

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `archive` | boolean | `true` | Set to `false` to permanently delete the field |

??? example "Example request"

    ```bash
    curl -X DELETE "https://your-instance.qualytics.io/api/fields/103?archive=false" \
      -H "Authorization: Bearer YOUR_TOKEN"
    ```

    **Response**: `204 No Content`

!!! warning
    This action is irreversible. The field and all its associated data are permanently removed.

---

## Bulk Operations

### Bulk Update Fields

Updates multiple fields at once. You can change status and tags in a single request.

**Endpoint**: `PATCH /api/fields`

**Permission**: Editor

**Request Body**: Array of field update objects.

| Property | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `id` | integer | Yes | The field ID |
| `status` | string | No | New status: `active`, `masked`, or `excluded` |
| `tags` | list[string] | No | Updated tags for the field |

??? example "Example: Mask multiple fields"

    **Request**:

    ```bash
    curl -X PATCH "https://your-instance.qualytics.io/api/fields" \
      -H "Authorization: Bearer YOUR_TOKEN" \
      -H "Content-Type: application/json" \
      -d '[
        { "id": 101, "status": "masked" },
        { "id": 102, "status": "masked" }
      ]'
    ```

    **Response**: Array of updated field objects.

    ```json
    [
      {
        "id": 101,
        "name": "customer_email",
        "status": "masked"
      },
      {
        "id": 102,
        "name": "social_security_number",
        "status": "masked"
      }
    ]
    ```

### Bulk Exclude Fields

Excludes multiple fields at once.

**Endpoint**: `DELETE /api/fields`

**Permission**: Editor

**Request Body**: Array of delete objects.

| Property | Type | Required | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `id` | integer | Yes | — | The field ID |
| `archive` | boolean | No | `true` | `true` to exclude, `false` to permanently delete |

??? example "Example: Exclude multiple fields"

    **Request**:

    ```bash
    curl -X DELETE "https://your-instance.qualytics.io/api/fields" \
      -H "Authorization: Bearer YOUR_TOKEN" \
      -H "Content-Type: application/json" \
      -d '[
        { "id": 101, "archive": true },
        { "id": 102, "archive": true }
      ]'
    ```

    **Response**: `204 No Content`

### Bulk Restore Fields

Restores multiple excluded fields back to `active` status.

**Endpoint**: `PATCH /api/fields/restore`

**Permission**: Editor

**Request Body**: Array of restore objects.

| Property | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `id` | integer | Yes | The field ID |

??? example "Example: Restore multiple fields"

    **Request**:

    ```bash
    curl -X PATCH "https://your-instance.qualytics.io/api/fields/restore" \
      -H "Authorization: Bearer YOUR_TOKEN" \
      -H "Content-Type: application/json" \
      -d '[
        { "id": 101 },
        { "id": 102 }
      ]'
    ```

    **Response**: Array of restored field objects.

    ```json
    [
      {
        "id": 101,
        "name": "customer_email",
        "status": "active"
      },
      {
        "id": 102,
        "name": "social_security_number",
        "status": "active"
      }
    ]
    ```

---

## Merge Fields

Merges two fields on the same container. The source field keeps its ID and all associated data (quality checks, anomalies, profiles) but adopts the target field's name. The target field is removed after the merge.

This is useful when a column is renamed in the source data — instead of losing history on the old field and starting fresh on the new one, you can merge them to preserve continuity.

**Endpoint**: `POST /api/fields/merge`

**Permission**: Editor

**Query Parameters**:

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `source_field_id` | integer | Yes | The field whose history and assets to keep |
| `target_field_id` | integer | Yes | The field whose name to adopt (this field is removed) |

??? example "Example request and response"

    **Request**:

    ```bash
    curl -X POST "https://your-instance.qualytics.io/api/fields/merge?source_field_id=101&target_field_id=105" \
      -H "Authorization: Bearer YOUR_TOKEN"
    ```

    **Response**:

    ```json
    {
      "id": 101,
      "name": "new_customer_email",
      "type": "String",
      "status": "active",
      "completeness": 0.98
    }
    ```

---

## Viewing Masked Values

When a field is masked, its actual values are hidden across the platform. Authorized users (Editor permission or above) can request to view unmasked values through specific endpoints. Every reveal action is recorded in the [masking audit log](#masking-audit-log).

### Field Profile with Unmasked Histogram

Retrieves a field profile with the option to include unmasked histogram values for masked fields.

**Endpoint**: `GET /api/field-profiles/{id}`

**Permission**: Editor (when `include_masked=true`)

**Query Parameters**:

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `include_masked` | boolean | `false` | When `true`, returns actual histogram values for masked fields. Creates an audit log entry |

??? example "Example request and response"

    **Request**:

    ```bash
    curl -X GET "https://your-instance.qualytics.io/api/field-profiles/5001?include_masked=true" \
      -H "Authorization: Bearer YOUR_TOKEN"
    ```

    **Response** (abbreviated):

    ```json
    {
      "id": 5001,
      "field_id": 102,
      "completeness": 1.0,
      "histogram": {
        "labels": ["john@example.com", "jane@example.com", "..."],
        "data": [150, 120, "..."]
      }
    }
    ```

### Container Source Records with Unmasked Values

Retrieves source records from a container with the option to include unmasked values for masked fields.

**Endpoint**: `GET /api/containers/{id}/source-records`

**Permission**: Editor (when `include_masked=true`)

**Query Parameters**:

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `filter` | string | — | A Spark SQL where clause to filter records |
| `sort_columns` | list[string] | — | Field names to order by |
| `include_masked` | boolean | `false` | When `true`, returns actual values for masked fields. Creates an audit log entry |

### Anomaly Source Records with Unmasked Values

Retrieves source records for a specific anomaly with the option to include unmasked values.

**Endpoint**: `GET /api/anomalies/{id}/source-record`

**Permission**: Editor (when `include_masked=true`)

**Query Parameters**:

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `limit` | integer | `10` | Maximum number of source records to return |
| `include_masked` | boolean | `false` | When `true`, returns actual values for masked fields. Creates an audit log entry |
| `include_deleted` | boolean | `true` | Include records that have been deleted from the source |

A CSV export variant is also available at `GET /api/anomalies/{id}/source-record/csv` with the same parameters.

---

## Masking Audit Log

The masking audit log records every instance where an authorized user accessed unmasked values for masked fields. This endpoint is available to **Admin** users only.

**Endpoint**: `GET /api/audit-logs/masking`

**Permission**: Admin

**Query Parameters**:

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `user_id` | integer | No | Filter by user ID |
| `action` | string | No | Filter by action (e.g., `unmask_field_values`) |
| `resource_type` | string | No | Filter by resource type: `container`, `anomaly`, or `field_profile` |
| `resource_id` | integer | No | Filter by resource ID |
| `start_date` | datetime | No | Filter logs created on or after this date |
| `end_date` | datetime | No | Filter logs created on or before this date |

??? example "Example request and response"

    **Request**:

    ```bash
    curl -X GET "https://your-instance.qualytics.io/api/audit-logs/masking?start_date=2026-03-01T00:00:00Z" \
      -H "Authorization: Bearer YOUR_TOKEN"
    ```

    **Response** (abbreviated):

    ```json
    {
      "total": 1,
      "items": [
        {
          "id": 501,
          "user_id": 10,
          "action": "unmask_field_values",
          "resource_type": "container",
          "resource_id": 42,
          "masked_field_names": ["social_security_number", "credit_card"],
          "endpoint": "GET /api/containers/42/source-records",
          "ip_address": "192.168.1.100",
          "created": "2026-03-05T14:30:00Z",
          "user": {
            "id": 10,
            "name": "Jane Doe",
            "email": "jane@example.com"
          }
        }
      ]
    }
    ```

---

## Status Values Reference

The `status` field in API responses uses the following values:

| Status | Description | Set By |
| :--- | :--- | :--- |
| `active` | Field is fully operational — profiled, scanned, and quality-checked | System (default) or User (unmask/restore) |
| `masked` | Field is operational but actual values are hidden across the platform | User |
| `missing` | Field was not found in the latest profile results | System (automatic) |
| `excluded` | Field is removed from quality monitoring; quality checks are archived | User |

## Permission Summary

| Operation | Minimum Permission |
| :--- | :--- |
| List and view fields | Member |
| Update field status (mask, unmask, exclude) | Editor |
| Restore a field | Editor |
| Delete a field | Editor |
| Merge fields | Editor |
| View unmasked values (`include_masked=true`) | Editor |
| View masking audit logs | Admin |
