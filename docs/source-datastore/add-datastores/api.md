# Datastore API

You can manage source datastores programmatically using the Qualytics API. This page covers all endpoints related to creating, reading, updating, and deleting datastores, as well as multi-schema bulk creation.

!!! tip "Complete API Reference"
    For the full interactive API documentation with all request/response schemas, visit the [API docs](https://demo.qualytics.io/api/docs){:target="_blank"}.

All endpoints use the base URL of your Qualytics deployment (e.g., `https://your-instance.qualytics.io/api`).

---

## Create a Datastore

Creates a single source datastore with either a new or existing connection.

**Endpoint**: `POST /api/datastores`

**Permission**: Manager

=== "New Connection (JDBC)"

    ??? example "Example request and response"

        **Request**:

        ```bash
        curl -X POST "https://your-instance.qualytics.io/api/datastores" \
          -H "Authorization: Bearer YOUR_TOKEN" \
          -H "Content-Type: application/json" \
          -d '{
            "name": "Production Sales",
            "connection": {
              "name": "postgres_production",
              "type": "postgresql",
              "host": "db.acme-corp.com",
              "port": 5432,
              "username": "qualytics_reader",
              "password": "s3cur3_p4ssw0rd",
              "parameters": {}
            },
            "database": "production",
            "schema": "sales",
            "teams": ["Data Platform", "Analytics"],
            "tags": ["production", "postgresql"],
            "trigger_catalog": true
          }'
        ```

        **Response** (201 Created):

        ```json
        {
          "id": 42,
          "name": "Production Sales",
          "type": "postgresql",
          "store_type": "jdbc",
          "database": "production",
          "schema": "sales",
          "connected": true,
          "favorite": false,
          "enrichment_only": false,
          "created": "2026-03-31T14:30:00.000000Z",
          "teams": [
            { "name": "Data Platform" },
            { "name": "Analytics" }
          ],
          "global_tags": [
            { "name": "production" },
            { "name": "postgresql" }
          ]
        }
        ```

=== "Existing Connection (JDBC)"

    ??? example "Example request and response"

        **Request**:

        ```bash
        curl -X POST "https://your-instance.qualytics.io/api/datastores" \
          -H "Authorization: Bearer YOUR_TOKEN" \
          -H "Content-Type: application/json" \
          -d '{
            "name": "Production Finance",
            "connection_id": 7,
            "database": "production",
            "schema": "finance",
            "teams": ["Finance Team"],
            "trigger_catalog": true
          }'
        ```

        **Response** (201 Created):

        ```json
        {
          "id": 43,
          "name": "Production Finance",
          "type": "postgresql",
          "store_type": "jdbc",
          "database": "production",
          "schema": "finance",
          "connected": true
        }
        ```

=== "Existing Connection (DFS)"

    ??? example "Example request and response"

        **Request**:

        ```bash
        curl -X POST "https://your-instance.qualytics.io/api/datastores" \
          -H "Authorization: Bearer YOUR_TOKEN" \
          -H "Content-Type: application/json" \
          -d '{
            "name": "Processed Events S3",
            "connection_id": 12,
            "root_path": "/processed/events/2026/",
            "teams": ["Data Engineering"],
            "trigger_catalog": true
          }'
        ```

        **Response** (201 Created):

        ```json
        {
          "id": 45,
          "name": "Processed Events S3",
          "type": "s3",
          "store_type": "dfs",
          "root_path": "/processed/events/2026/",
          "connected": true
        }
        ```

=== "New Connection (DFS)"

    ??? example "Example request and response"

        **Request**:

        ```bash
        curl -X POST "https://your-instance.qualytics.io/api/datastores" \
          -H "Authorization: Bearer YOUR_TOKEN" \
          -H "Content-Type: application/json" \
          -d '{
            "name": "Raw Events S3",
            "connection": {
              "name": "s3_data_lake",
              "type": "s3",
              "uri": "s3://acme-data-lake",
              "access_key": "AKIAIOSFODNN7EXAMPLE",
              "secret_key": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLE"
            },
            "root_path": "/raw/events/2026/",
            "teams": ["Data Engineering"],
            "trigger_catalog": true
          }'
        ```

        **Response** (201 Created):

        ```json
        {
          "id": 44,
          "name": "Raw Events S3",
          "type": "s3",
          "store_type": "dfs",
          "root_path": "/raw/events/2026/",
          "connected": true
        }
        ```

### Create Request Fields

| Property | Type | Required | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `name` | string | Yes | — | Display name for the datastore (max 255 characters). |
| `connection` | object | Conditional | — | Connection details for a new connection. Required if `connection_id` is not provided. |
| `connection_id` | integer | Conditional | — | ID of an existing connection. Required if `connection` is not provided. |
| `database` | string | No | `null` | Database name (JDBC only). |
| `schema` | string | No | `null` | Schema name (JDBC and Native only). |
| `root_path` | string | Conditional | — | Base directory path (DFS only, required for DFS). |
| `description` | string | No | `null` | Description for the datastore (max 255 characters). |
| `teams` | list[string] | No | `null` | Team names to assign. |
| `tags` | list[string] | No | `null` | Tag names to assign. |
| `group_id` | integer | No | `null` | Existing datastore group ID to assign. |
| `group` | object | No | `null` | Inline group to create and assign (mutually exclusive with `group_id`). |
| `trigger_catalog` | boolean | No | `null` | Whether to trigger a sync operation after creation. |
| `enrichment_datastore_id` | integer | No | `null` | Enrichment datastore ID to link. |
| `enrichment_prefix` | string | No | Auto-generated | Prefix for enrichment tables (max 60 characters). |
| `enrichment_source_record_limit` | integer | No | `10` | Max source records per anomaly (1–1,000,000,000). |
| `enrichment_remediation_strategy` | string | No | `"none"` | Replication strategy: `"none"`, `"append"`, or `"overwrite"`. |
| `high_count_rollup_threshold` | integer | No | `10` | Max anomalies per check before rolling up (1–1,000). |

---

## Get a Datastore

Retrieves a single datastore by its ID.

**Endpoint**: `GET /api/datastores/{id}`

**Permission**: Member

??? example "Example request and response"

    **Request**:

    ```bash
    curl -X GET "https://your-instance.qualytics.io/api/datastores/42" \
      -H "Authorization: Bearer YOUR_TOKEN"
    ```

    **Response**:

    ```json
    {
      "id": 42,
      "name": "Production Sales",
      "type": "postgresql",
      "store_type": "jdbc",
      "database": "production",
      "schema": "sales",
      "connected": true,
      "favorite": false,
      "enrichment_only": false,
      "description": null,
      "created": "2026-03-31T14:30:00.000000Z",
      "updated": "2026-03-31T14:30:00.000000Z",
      "connection": {
        "id": 7,
        "name": "postgres_production",
        "type": "postgresql"
      },
      "teams": [
        { "name": "Data Platform" },
        { "name": "Analytics" }
      ],
      "global_tags": [
        { "name": "production" },
        { "name": "postgresql" }
      ],
      "metrics": {
        "containers": 12,
        "records": 1850000,
        "fields_profiled": 87,
        "active_checks": 145,
        "active_anomalies": 3
      }
    }
    ```

---

## List Datastores

Retrieves a paginated list of datastores with optional filtering and sorting.

**Endpoint**: `GET /api/datastores`

**Permission**: Member

??? example "Example request and response"

    **Request**:

    ```bash
    curl -X GET "https://your-instance.qualytics.io/api/datastores?tag=production&sort_name=asc&limit=10" \
      -H "Authorization: Bearer YOUR_TOKEN"
    ```

    **Response**:

    ```json
    {
      "items": [
        {
          "id": 42,
          "name": "Production Finance",
          "type": "postgresql",
          "store_type": "jdbc",
          "connected": true
        },
        {
          "id": 43,
          "name": "Production Sales",
          "type": "postgresql",
          "store_type": "jdbc",
          "connected": true
        }
      ],
      "total": 2,
      "page": 1,
      "size": 10,
      "pages": 1
    }
    ```

### Query Parameters

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `id` | list[int] | Filter by datastore ID(s). |
| `name` | string | Filter by exact name. |
| `search` | string | Search by name or ID (partial match). |
| `datastore_type` | list[string] | Filter by connection type (e.g., `postgresql`, `snowflake`, `s3`). |
| `tag` | list[string] | Filter by tag names. |
| `group` | list[int] | Filter by datastore group ID(s). |
| `enrichment_only` | boolean | Filter enrichment-only (`true`) vs source (`false`) datastores. Default: `false`. |
| `sort_name` | string | Sort by name (`asc` or `desc`). |
| `sort_created` | string | Sort by created date (`asc` or `desc`). |
| `sort_favorite` | string | Sort by favorite flag (`asc` or `desc`). Default: `desc`. |
| `sort_containers` | string | Sort by container count (`asc` or `desc`). |
| `sort_active_anomalies` | string | Sort by active anomalies count (`asc` or `desc`). |

---

## Update a Datastore

Updates an existing datastore's properties, tags, or teams.

**Endpoint**: `PUT /api/datastores/{id}`

**Permission**: Editor

??? example "Example request and response"

    **Request**:

    ```bash
    curl -X PUT "https://your-instance.qualytics.io/api/datastores/42" \
      -H "Authorization: Bearer YOUR_TOKEN" \
      -H "Content-Type: application/json" \
      -d '{
        "name": "Production Sales (Updated)",
        "description": "Core sales data from the production PostgreSQL database",
        "connection_id": 7,
        "database": "production",
        "schema": "sales",
        "enrichment_only": false,
        "enrichment_prefix": "_production_sales",
        "tags": ["production", "postgresql", "sales"],
        "teams": ["Data Platform", "Analytics", "Sales Ops"]
      }'
    ```

    **Response**:

    ```json
    {
      "id": 42,
      "name": "Production Sales (Updated)",
      "description": "Core sales data from the production PostgreSQL database",
      "type": "postgresql",
      "store_type": "jdbc",
      "database": "production",
      "schema": "sales",
      "global_tags": [
        { "name": "production" },
        { "name": "postgresql" },
        { "name": "sales" }
      ],
      "teams": [
        { "name": "Data Platform" },
        { "name": "Analytics" },
        { "name": "Sales Ops" }
      ]
    }
    ```

!!! note
    Updating `tags` or `teams` **replaces** the entire list. To add a tag without removing existing ones, include all current tags plus the new one.

---

## Delete a Datastore

Permanently deletes a datastore and all its associated containers, checks, and anomalies.

**Endpoint**: `DELETE /api/datastores/{id}`

**Permission**: Admin

??? example "Example request"

    ```bash
    curl -X DELETE "https://your-instance.qualytics.io/api/datastores/42" \
      -H "Authorization: Bearer YOUR_TOKEN"
    ```

    **Response**: `204 No Content`

!!! warning
    Deletion is permanent and cascading. All containers, checks, anomalies, and enrichment data associated with this datastore will be removed.

---

## Toggle Favorite

Marks or unmarks a datastore as a favorite.

**Endpoint**: `PATCH /api/datastores/{id}/favorite`

**Permission**: Member

??? example "Example request and response"

    **Request**:

    ```bash
    curl -X PATCH "https://your-instance.qualytics.io/api/datastores/42/favorite" \
      -H "Authorization: Bearer YOUR_TOKEN" \
      -H "Content-Type: application/json" \
      -d '{ "favorite": true }'
    ```

    **Response**: Returns the updated datastore object with `"favorite": true`.

---

## Assign Group

Assigns a datastore to a datastore group.

**Endpoint**: `PATCH /api/datastores/{id}/assign-group`

**Permission**: Editor

??? example "Example request and response"

    **Request**:

    ```bash
    curl -X PATCH "https://your-instance.qualytics.io/api/datastores/42/assign-group" \
      -H "Authorization: Bearer YOUR_TOKEN" \
      -H "Content-Type: application/json" \
      -d '{ "group_id": 5 }'
    ```

    **Response**: Returns the updated datastore object with the group assigned.

To unassign, pass `null`:

```bash
curl -X PATCH "https://your-instance.qualytics.io/api/datastores/42/assign-group" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{ "group_id": null }'
```

---

## Link Enrichment Datastore

Links an enrichment datastore to a source datastore to persist scan results and anomalies.

**Endpoint**: `PATCH /api/datastores/{datastore_id}/enrichment/{enrichment_id}`

**Permission**: Member

??? example "Example request"

    Link enrichment datastore ID 42 to source datastore ID 110:

    ```bash
    curl -X PATCH "https://your-instance.qualytics.io/api/datastores/110/enrichment/42" \
      -H "Authorization: Bearer YOUR_TOKEN"
    ```

    **Response**: Returns the updated datastore object with enrichment linked.

---

## Unlink Enrichment Datastore

Removes the enrichment link from a source datastore.

**Endpoint**: `DELETE /api/datastores/{datastore_id}/enrichment`

**Permission**: Admin

??? example "Example request"

    ```bash
    curl -X DELETE "https://your-instance.qualytics.io/api/datastores/110/enrichment" \
      -H "Authorization: Bearer YOUR_TOKEN"
    ```

    **Response**: `204 No Content`

!!! warning
    Unlinking enrichment requires the **Admin** role, which is a higher permission than linking.

---

## Test Connection

Validates connectivity for a datastore without persisting any data.

**Endpoint**: `POST /api/datastores/connection`

**Permission**: Manager

??? example "Example request and response"

    **Request**:

    ```bash
    curl -X POST "https://your-instance.qualytics.io/api/datastores/connection" \
      -H "Authorization: Bearer YOUR_TOKEN" \
      -H "Content-Type: application/json" \
      -d '{
        "name": "Test PostgreSQL",
        "connection": {
          "name": "pg_test",
          "type": "postgresql",
          "host": "db.acme-corp.com",
          "port": 5432,
          "username": "qualytics_reader",
          "password": "s3cur3_p4ssw0rd"
        },
        "database": "production",
        "schema": "public"
      }'
    ```

    **Response** (204 No Content): Connection verified successfully.

    **Error Response** (400 Bad Request):

    ```json
    {
      "message": "Connection refused: could not connect to server at db.acme-corp.com:5432"
    }
    ```

---

## Multi-Schema Creation

Use these endpoints to programmatically discover catalogs and schemas, validate connectivity, and bulk-create multiple datastores from a single connection.

### Discover Catalogs

Retrieves the list of available catalogs (databases/projects) from a connection.

=== "New Connection"
    **Endpoint**: `POST /api/connections/catalogs`

    **Permission**: Manager

    Send the full connection details in the request body.

    **Response**: `list[string]` — a list of catalog names.

    ??? example "Example request and response"

        **Request**:

        ```bash
        curl -X POST "https://your-instance.qualytics.io/api/connections/catalogs" \
          -H "Authorization: Bearer YOUR_TOKEN" \
          -H "Content-Type: application/json" \
          -d '{
            "name": "snowflake_production",
            "type": "snowflake",
            "host": "acme.snowflakecomputing.com",
            "username": "qualytics_user",
            "password": "your_password",
            "parameters": {
              "role": "qualytics_read_role",
              "warehouse": "qualytics_wh"
            }
          }'
        ```

        **Response**:

        ```json
        ["production_db", "staging_db", "analytics_db"]
        ```

=== "Existing Connection"
    **Endpoint**: `GET /api/connections/{connection_id}/catalogs`

    **Permission**: Manager

    **Response**: `list[DiscoveredCatalog]` — catalogs annotated with existing datastores.

    ??? example "Example request and response"

        **Request**:

        ```bash
        curl -X GET "https://your-instance.qualytics.io/api/connections/7/catalogs" \
          -H "Authorization: Bearer YOUR_TOKEN"
        ```

        **Response**:

        ```json
        [
          {
            "name": "production_db",
            "existing_datastores": [
              { "id": 50, "name": "prod_public" }
            ]
          },
          {
            "name": "staging_db",
            "existing_datastores": []
          }
        ]
        ```

!!! note
    Only JDBC and Native connectors support catalog discovery. Calling this endpoint for a DFS connection returns `409 Conflict`.

---

### Discover Schemas

Retrieves the list of available schemas within a catalog.

**Query Parameters**:

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `catalog` | string | No | Catalog/database name to filter schemas by |

=== "New Connection"
    **Endpoint**: `POST /api/connections/schemas`

    **Permission**: Manager

    Send the full connection details in the request body.

    **Response**: `list[string]` — a list of schema names.

    ??? example "Example request and response"

        **Request**:

        ```bash
        curl -X POST "https://your-instance.qualytics.io/api/connections/schemas?catalog=production_db" \
          -H "Authorization: Bearer YOUR_TOKEN" \
          -H "Content-Type: application/json" \
          -d '{
            "name": "snowflake_production",
            "type": "snowflake",
            "host": "acme.snowflakecomputing.com",
            "username": "qualytics_user",
            "password": "your_password",
            "parameters": {
              "role": "qualytics_read_role",
              "warehouse": "qualytics_wh"
            }
          }'
        ```

        **Response**:

        ```json
        ["public", "sales", "finance", "hr", "marketing"]
        ```

=== "Existing Connection"
    **Endpoint**: `GET /api/connections/{connection_id}/schemas`

    **Permission**: Manager

    **Response**: `list[DiscoveredSchema]` — schemas annotated with existing datastores.

    ??? example "Example request and response"

        **Request**:

        ```bash
        curl -X GET "https://your-instance.qualytics.io/api/connections/7/schemas?catalog=production_db" \
          -H "Authorization: Bearer YOUR_TOKEN"
        ```

        **Response**:

        ```json
        [
          {
            "name": "public",
            "existing_datastores": []
          },
          {
            "name": "sales",
            "existing_datastores": [
              { "id": 60, "name": "prod_sales" }
            ]
          },
          {
            "name": "finance",
            "existing_datastores": []
          }
        ]
        ```

!!! note
    Only JDBC and Native connectors support schema discovery. Calling this endpoint for a DFS connection returns `409 Conflict`.

---

### Validate Schemas

Validates connectivity for one or more schemas before creating datastores.

=== "New Connection"
    **Endpoint**: `POST /api/connections/datastores/validate`

    **Permission**: Manager

    ??? example "Example request and response"

        **Request**:

        ```bash
        curl -X POST "https://your-instance.qualytics.io/api/connections/datastores/validate" \
          -H "Authorization: Bearer YOUR_TOKEN" \
          -H "Content-Type: application/json" \
          -d '{
            "connection": {
              "name": "snowflake_production",
              "type": "snowflake",
              "host": "acme.snowflakecomputing.com",
              "username": "qualytics_user",
              "password": "your_password",
              "parameters": {
                "role": "qualytics_read_role",
                "warehouse": "qualytics_wh"
              }
            },
            "database": "production_db",
            "schemas": ["public", "sales", "finance"]
          }'
        ```

        **Response**:

        ```json
        {
          "results": [
            { "schema_name": "public", "status": "success" },
            { "schema_name": "sales", "status": "success" },
            { "schema_name": "finance", "status": "failure", "message": "Permission denied for schema finance" }
          ]
        }
        ```

=== "Existing Connection"
    **Endpoint**: `POST /api/connections/{connection_id}/datastores/validate`

    **Permission**: Manager

    ??? example "Example request and response"

        **Request**:

        ```bash
        curl -X POST "https://your-instance.qualytics.io/api/connections/7/datastores/validate" \
          -H "Authorization: Bearer YOUR_TOKEN" \
          -H "Content-Type: application/json" \
          -d '{
            "database": "production_db",
            "schemas": ["public", "sales", "finance"]
          }'
        ```

        **Response**:

        ```json
        {
          "results": [
            { "schema_name": "public", "status": "success" },
            { "schema_name": "sales", "status": "success" },
            { "schema_name": "finance", "status": "failure", "message": "Permission denied for schema finance" }
          ]
        }
        ```

---

### Bulk Create Datastores

Creates multiple source datastores from selected schemas in a single operation.

=== "New Connection"
    **Endpoint**: `POST /api/connections/datastores/bulk`

    **Permission**: Manager

    ??? example "Example request and response"

        **Request**:

        ```bash
        curl -X POST "https://your-instance.qualytics.io/api/connections/datastores/bulk" \
          -H "Authorization: Bearer YOUR_TOKEN" \
          -H "Content-Type: application/json" \
          -d '{
            "connection": {
              "name": "snowflake_production",
              "type": "snowflake",
              "host": "acme.snowflakecomputing.com",
              "username": "qualytics_user",
              "password": "your_password",
              "parameters": {
                "role": "qualytics_read_role",
                "warehouse": "qualytics_wh"
              }
            },
            "database": "production_db",
            "schemas": ["public", "sales", "finance"],
            "name_template": "prod_{{schema}}",
            "description": "Production Snowflake datastores",
            "teams": ["Data Platform"],
            "trigger_catalog": true,
            "enrichment_datastore_id": 42,
            "enrichment_source_record_limit": 100,
            "enrichment_remediation_strategy": "append",
            "high_count_rollup_threshold": 10,
            "group_id": 5,
            "tags": ["production", "snowflake"]
          }'
        ```

        **Response**:

        ```json
        {
          "created": [101, 102, 103],
          "errors": []
        }
        ```

=== "Existing Connection"
    **Endpoint**: `POST /api/connections/{connection_id}/datastores/bulk`

    **Permission**: Manager

    ??? example "Example request and response"

        **Request**:

        ```bash
        curl -X POST "https://your-instance.qualytics.io/api/connections/7/datastores/bulk" \
          -H "Authorization: Bearer YOUR_TOKEN" \
          -H "Content-Type: application/json" \
          -d '{
            "database": "production_db",
            "schemas": ["public", "sales"],
            "name_template": "prod_{{schema}}",
            "teams": ["Data Platform", "Analytics"],
            "trigger_catalog": true
          }'
        ```

        **Response**:

        ```json
        {
          "created": [110, 111],
          "errors": []
        }
        ```

??? example "Example response with errors"

    When some schemas fail, the response includes both successes and errors:

    ```json
    {
      "created": [101, 102],
      "errors": [
        {
          "schema_name": "finance",
          "error": "Permission denied for schema finance"
        }
      ]
    }
    ```

!!! note
    The bulk creation is non-atomic. Schemas that succeed are created even if other schemas fail. The response includes both the list of created datastore IDs and any errors encountered.

### Bulk Create Request Fields

| Property | Type | Required | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `connection` | object | Yes (new only) | — | Connection details to create before bulk creation. |
| `schemas` | list[string] | Yes | — | List of schema names to create datastores for. |
| `database` | string | No | `null` | Database/catalog name (for connectors with catalog hierarchy). |
| `name_template` | string | No | `{connection_name}_{{schema}}` | Naming pattern with `{{schema}}` placeholder. |
| `description` | string | No | `null` | Description applied to all created datastores. |
| `enrichment_datastore_id` | integer | No | `null` | Existing enrichment datastore ID to link. |
| `enrichment_prefix` | string | No | `null` | Enrichment container prefix name. |
| `enrichment_source_record_limit` | integer | No | `10` | Max source records per anomaly (1–1,000,000,000). |
| `enrichment_remediation_strategy` | string | No | `"none"` | Replication strategy: `"none"`, `"append"`, or `"overwrite"`. |
| `high_count_rollup_threshold` | integer | No | `10` | Max anomalies per check before rolling up (1–1,000). |
| `group_id` | integer | No | `null` | Existing datastore group ID to assign. |
| `group` | object | No | `null` | Inline group to create and assign (mutually exclusive with `group_id`). |
| `tags` | list[string] | No | `null` | Tags to apply to all created datastores. |
| `teams` | list[string] | No | `null` | Teams to assign to all created datastores. |
| `trigger_catalog` | boolean | No | `null` | Whether to trigger a sync operation after each creation. |

!!! warning
    `group_id` and `group` are mutually exclusive — provide only one.

---

## Practical Guides

### End-to-End: Onboard All Schemas from a Snowflake Database

??? example "Complete workflow — Snowflake with new connection"

    **1. Discover what databases are available:**

    ```bash
    curl -X POST "https://your-instance.qualytics.io/api/connections/catalogs" \
      -H "Authorization: Bearer YOUR_TOKEN" \
      -H "Content-Type: application/json" \
      -d '{
        "name": "snowflake_prod",
        "type": "snowflake",
        "host": "acme.snowflakecomputing.com",
        "username": "qualytics_user",
        "password": "your_password",
        "parameters": {
          "role": "qualytics_read_role",
          "warehouse": "qualytics_wh"
        }
      }'
    ```

    Response: `["production_db", "staging_db", "analytics_db"]`

    **2. Discover schemas in your target database:**

    ```bash
    curl -X POST "https://your-instance.qualytics.io/api/connections/schemas?catalog=production_db" \
      -H "Authorization: Bearer YOUR_TOKEN" \
      -H "Content-Type: application/json" \
      -d '{ ... same connection payload ... }'
    ```

    Response: `["public", "sales", "finance", "hr", "marketing"]`

    **3. Validate the schemas you want to onboard:**

    ```bash
    curl -X POST "https://your-instance.qualytics.io/api/connections/datastores/validate" \
      -H "Authorization: Bearer YOUR_TOKEN" \
      -H "Content-Type: application/json" \
      -d '{
        "connection": { ... same connection payload ... },
        "database": "production_db",
        "schemas": ["public", "sales", "finance", "hr", "marketing"]
      }'
    ```

    **4. Bulk create all datastores:**

    ```bash
    curl -X POST "https://your-instance.qualytics.io/api/connections/datastores/bulk" \
      -H "Authorization: Bearer YOUR_TOKEN" \
      -H "Content-Type: application/json" \
      -d '{
        "connection": { ... same connection payload ... },
        "database": "production_db",
        "schemas": ["public", "sales", "finance", "hr", "marketing"],
        "name_template": "prod_snowflake_{{schema}}",
        "teams": ["Data Platform"],
        "trigger_catalog": true,
        "enrichment_datastore_id": 42,
        "enrichment_source_record_limit": 100,
        "enrichment_remediation_strategy": "append",
        "tags": ["production", "snowflake"]
      }'
    ```

    Response: `{ "created": [101, 102, 103, 104, 105], "errors": [] }`

---

### End-to-End: Onboard PostgreSQL Schemas Using an Existing Connection

??? example "Complete workflow — PostgreSQL with existing connection"

    **1. Discover schemas:**

    ```bash
    curl -X GET "https://your-instance.qualytics.io/api/connections/7/schemas?catalog=analytics_db" \
      -H "Authorization: Bearer YOUR_TOKEN"
    ```

    **2. Bulk create:**

    ```bash
    curl -X POST "https://your-instance.qualytics.io/api/connections/7/datastores/bulk" \
      -H "Authorization: Bearer YOUR_TOKEN" \
      -H "Content-Type: application/json" \
      -d '{
        "database": "analytics_db",
        "schemas": ["raw", "staging", "curated"],
        "name_template": "analytics_{{schema}}",
        "teams": ["Analytics"],
        "trigger_catalog": true
      }'
    ```

    **3. Link enrichment after creation:**

    ```bash
    for ID in 201 202 203; do
      curl -X PATCH "https://your-instance.qualytics.io/api/datastores/$ID/enrichment/42" \
        -H "Authorization: Bearer YOUR_TOKEN"
    done
    ```

---

### Automation Script

??? example "Python automation script"

    ```python
    import requests

    BASE_URL = "https://your-instance.qualytics.io/api"
    TOKEN = "YOUR_TOKEN"
    HEADERS = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json",
    }

    CONNECTION_ID = 7
    DATABASE = "production_db"
    NAME_TEMPLATE = "prod_{{schema}}"
    TEAMS = ["Data Platform"]
    ENRICHMENT_ID = 42

    # Step 1: Discover available schemas
    resp = requests.get(
        f"{BASE_URL}/connections/{CONNECTION_ID}/schemas",
        headers=HEADERS,
        params={"catalog": DATABASE},
    )
    resp.raise_for_status()
    discovered = resp.json()

    # Filter out schemas that already have datastores
    new_schemas = [
        s["name"] for s in discovered
        if len(s["existing_datastores"]) == 0
    ]
    print(f"Found {len(new_schemas)} new schemas: {new_schemas}")

    if not new_schemas:
        print("No new schemas to onboard.")
        exit()

    # Step 2: Validate connectivity
    resp = requests.post(
        f"{BASE_URL}/connections/{CONNECTION_ID}/datastores/validate",
        headers=HEADERS,
        json={
            "database": DATABASE,
            "schemas": new_schemas,
        },
    )
    resp.raise_for_status()
    validation = resp.json()

    failed = [r for r in validation["results"] if r["status"] == "failure"]
    if failed:
        print(f"Warning: {len(failed)} schemas failed validation:")
        for f in failed:
            print(f"  - {f['schema_name']}: {f.get('message', 'Unknown error')}")

    valid_schemas = [
        r["schema_name"] for r in validation["results"]
        if r["status"] == "success"
    ]
    print(f"Proceeding with {len(valid_schemas)} valid schemas.")

    # Step 3: Bulk create datastores
    resp = requests.post(
        f"{BASE_URL}/connections/{CONNECTION_ID}/datastores/bulk",
        headers=HEADERS,
        json={
            "database": DATABASE,
            "schemas": valid_schemas,
            "name_template": NAME_TEMPLATE,
            "teams": TEAMS,
            "trigger_catalog": True,
            "enrichment_datastore_id": ENRICHMENT_ID,
        },
    )
    resp.raise_for_status()
    result = resp.json()

    print(f"Created {len(result['created'])} datastores: {result['created']}")
    if result["errors"]:
        print(f"Errors: {result['errors']}")
    ```

---

## Permission Summary

| Operation | Minimum Permission |
| :--- | :--- |
| Create a datastore | Manager |
| Get / List datastores | Member |
| Update a datastore | Editor |
| Delete a datastore | Admin |
| Toggle favorite | Member |
| Assign group | Editor |
| Link enrichment | Member |
| Unlink enrichment | Admin |
| Test connection | Manager |
| Discover catalogs / schemas | Manager |
| Validate schemas | Manager |
| Bulk create datastores | Manager |
