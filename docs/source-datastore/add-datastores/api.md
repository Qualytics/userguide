# Datastore API

You can manage datastores programmatically using the Qualytics API.

!!! tip
    For complete API documentation, including request/response schemas, visit the [API docs](https://demo.qualytics.io/api/docs){:target="_blank"}.

## Multi-Schema Creation

This section documents the API endpoints related to multi-schema source datastore creation. Use these endpoints to programmatically discover catalogs and schemas, validate connectivity, and bulk-create datastores.

All endpoints use the base URL of your Qualytics deployment (e.g., `https://your-instance.qualytics.io/api`).

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

Validates connectivity for one or more schemas before creating datastores. The validation runs per-schema and reports individual results.

=== "New Connection"
    **Endpoint**: `POST /api/connections/datastores/validate`

    **Permission**: Manager

    Send the full connection details along with the schemas to validate.

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

**Request Body**:

| Property | Type | Required | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `schemas` | list[string] | Yes | — | List of schema names to validate (max 50) |
| `database` | string | No | `null` | Database/catalog name |
| `enrichment_only` | boolean | No | `false` | When `true`, validates write permissions (DDL) in addition to read |

---

### Bulk Create Datastores

Creates multiple source datastores from selected schemas in a single operation.

=== "New Connection"
    **Endpoint**: `POST /api/connections/datastores/bulk`

    **Permission**: Manager

    Creates the connection and bulk-creates datastores in a single request.

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
            "enrichment_prefix": "_prod",
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

---

### Link Enrichment Datastore

If you did not include `enrichment_datastore_id` during bulk creation, you can link an enrichment datastore to each source datastore individually after creation.

#### Link Enrichment to a Source Datastore

**Endpoint**: `PATCH /api/datastores/{datastore_id}/enrichment/{enrichment_id}`

**Permission**: Member

??? example "Example request"

    Link enrichment datastore ID 42 to source datastore ID 110:

    **Request**:

    ```bash
    curl -X PATCH "https://your-instance.qualytics.io/api/datastores/110/enrichment/42" \
      -H "Authorization: Bearer YOUR_TOKEN"
    ```

    **Response**: Returns the updated datastore object with enrichment linked.

!!! tip
    To automate enrichment linking across multiple datastores created in bulk, loop through the `created` IDs from the bulk creation response:

    ```bash
    for DATASTORE_ID in 110 111 112; do
      curl -X PATCH "https://your-instance.qualytics.io/api/datastores/$DATASTORE_ID/enrichment/42" \
        -H "Authorization: Bearer YOUR_TOKEN"
    done
    ```

#### Unlink Enrichment from a Source Datastore

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

### Request Fields Reference

#### Bulk Create Request

| Property | Type | Required | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `connection` | object | Yes (new only) | — | Connection details to create before bulk creation |
| `schemas` | list[string] | Yes | — | List of schema names to create datastores for |
| `database` | string | No | `null` | Database/catalog name (for connectors with catalog hierarchy) |
| `name_template` | string | No | `{connection_name}_{{schema}}` | Naming pattern with `{{schema}}` placeholder |
| `description` | string | No | `null` | Description applied to all created datastores |
| `enrichment_only` | boolean | No | `false` | Whether created datastores are enrichment-only |
| `enrichment_datastore_id` | integer | No | `null` | Existing enrichment datastore ID to link to each created datastore |
| `enrichment_prefix` | string | No | `null` | Enrichment container prefix name |
| `enrichment_source_record_limit` | integer | No | `10` | Max source records written to enrichment per anomaly (1–1,000,000,000) |
| `enrichment_remediation_strategy` | string | No | `"none"` | Replication strategy: `"none"`, `"append"`, or `"overwrite"` |
| `high_count_rollup_threshold` | integer | No | `10` | Max anomalies per check before rolling up (1–1,000) |
| `group_id` | integer | No | `null` | Existing datastore group ID to assign to all datastores |
| `group` | object | No | `null` | Inline group to create and assign (mutually exclusive with `group_id`) |
| `tags` | list[string] | No | `null` | Tags to apply to all created datastores |
| `teams` | list[string] | No | `null` | Teams to assign to all created datastores |
| `trigger_catalog` | boolean | No | `null` | Whether to trigger a sync operation after each datastore creation |

!!! warning
    `group_id` and `group` are mutually exclusive — provide only one.

#### Validate Request

| Property | Type | Required | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `schemas` | list[string] | Yes | — | List of schema names to validate (max 50) |
| `database` | string | No | `null` | Database/catalog name |
| `enrichment_only` | boolean | No | `false` | When `true`, validates write permissions (DDL) in addition to read |

---

### Practical Guides

#### End-to-End: Onboard All Schemas from a Snowflake Database

A common scenario for data engineers: you have a Snowflake database with multiple schemas and want to onboard them all into Qualytics with enrichment and auto-sync.

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

    Response — check that all schemas passed:

    ```json
    {
      "results": [
        { "schema_name": "public", "status": "success" },
        { "schema_name": "sales", "status": "success" },
        { "schema_name": "finance", "status": "success" },
        { "schema_name": "hr", "status": "success" },
        { "schema_name": "marketing", "status": "success" }
      ]
    }
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
        "description": "Snowflake production schemas",
        "teams": ["Data Platform"],
        "trigger_catalog": true,
        "enrichment_datastore_id": 42,
        "enrichment_source_record_limit": 100,
        "enrichment_remediation_strategy": "append",
        "tags": ["production", "snowflake"]
      }'
    ```

    Response:

    ```json
    {
      "created": [101, 102, 103, 104, 105],
      "errors": []
    }
    ```

    Done — 5 datastores created, all linked to enrichment, sync running on each.

---

#### End-to-End: Onboard PostgreSQL Schemas Using an Existing Connection

A common scenario for analysts: your DBA already configured a connection in Qualytics and you want to add new schemas from it.

??? example "Complete workflow — PostgreSQL with existing connection"

    **1. Find available databases (catalogs):**

    ```bash
    curl -X GET "https://your-instance.qualytics.io/api/connections/7/catalogs" \
      -H "Authorization: Bearer YOUR_TOKEN"
    ```

    Response — shows which databases already have datastores:

    ```json
    [
      {
        "name": "app_db",
        "existing_datastores": [
          { "id": 50, "name": "app_db_public" }
        ]
      },
      {
        "name": "analytics_db",
        "existing_datastores": []
      }
    ]
    ```

    **2. Discover schemas in the `analytics_db` database:**

    ```bash
    curl -X GET "https://your-instance.qualytics.io/api/connections/7/schemas?catalog=analytics_db" \
      -H "Authorization: Bearer YOUR_TOKEN"
    ```

    Response — `existing_datastores` helps you avoid duplicates:

    ```json
    [
      { "name": "raw", "existing_datastores": [] },
      { "name": "staging", "existing_datastores": [] },
      { "name": "curated", "existing_datastores": [] }
    ]
    ```

    **3. Validate and create:**

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

    Response:

    ```json
    {
      "created": [201, 202, 203],
      "errors": []
    }
    ```

    **4. Link enrichment after creation:**

    ```bash
    for ID in 201 202 203; do
      curl -X PATCH "https://your-instance.qualytics.io/api/datastores/$ID/enrichment/42" \
        -H "Authorization: Bearer YOUR_TOKEN"
    done
    ```

---

#### End-to-End: Onboard BigQuery Datasets

BigQuery uses "project" as catalog and "dataset" as schema. The flow is the same but the terminology differs.

??? example "Complete workflow — BigQuery with new connection"

    **1. Discover available projects:**

    ```bash
    curl -X POST "https://your-instance.qualytics.io/api/connections/catalogs" \
      -H "Authorization: Bearer YOUR_TOKEN" \
      -H "Content-Type: application/json" \
      -d '{
        "name": "bigquery_prod",
        "type": "bigquery",
        "host": "https://www.googleapis.com/bigquery/v2",
        "username": "project-id",
        "password": "service-account-key-json",
        "parameters": {}
      }'
    ```

    Response: `["my-project-prod", "my-project-staging"]`

    **2. Discover datasets in your project:**

    ```bash
    curl -X POST "https://your-instance.qualytics.io/api/connections/schemas?catalog=my-project-prod" \
      -H "Authorization: Bearer YOUR_TOKEN" \
      -H "Content-Type: application/json" \
      -d '{ ... same connection payload ... }'
    ```

    Response: `["raw_events", "user_analytics", "financial_data"]`

    **3. Bulk create:**

    ```bash
    curl -X POST "https://your-instance.qualytics.io/api/connections/datastores/bulk" \
      -H "Authorization: Bearer YOUR_TOKEN" \
      -H "Content-Type: application/json" \
      -d '{
        "connection": { ... same connection payload ... },
        "database": "my-project-prod",
        "schemas": ["raw_events", "user_analytics", "financial_data"],
        "name_template": "bq_{{schema}}",
        "teams": ["Data Engineering"],
        "trigger_catalog": true
      }'
    ```

    Response:

    ```json
    {
      "created": [301, 302, 303],
      "errors": []
    }
    ```

---

#### Handling Errors and Retrying Failed Schemas

When bulk creation partially fails, some datastores are created and some are not. Here is how to handle this.

??? example "Handling partial failures"

    **Scenario**: You tried to create 5 datastores but 2 failed due to permission issues.

    **Response from bulk create:**

    ```json
    {
      "created": [101, 102, 103],
      "errors": [
        { "schema_name": "restricted_schema", "error": "Permission denied" },
        { "schema_name": "locked_schema", "error": "Schema is locked for maintenance" }
      ]
    }
    ```

    **What to do:**

    1. The 3 successful datastores (`101`, `102`, `103`) are fully operational — no action needed.
    2. Fix the underlying issues for the failed schemas (e.g., grant `USAGE` permission, wait for maintenance to complete).
    3. Retry only the failed schemas:

    ```bash
    curl -X POST "https://your-instance.qualytics.io/api/connections/7/datastores/bulk" \
      -H "Authorization: Bearer YOUR_TOKEN" \
      -H "Content-Type: application/json" \
      -d '{
        "database": "production_db",
        "schemas": ["restricted_schema", "locked_schema"],
        "name_template": "prod_{{schema}}",
        "teams": ["Data Platform"],
        "trigger_catalog": true,
        "enrichment_datastore_id": 42
      }'
    ```

---

#### Automation Script

A ready-to-use Python script that automates the full multi-schema onboarding flow: discover schemas, validate, create, and link enrichment.

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

### Permission Summary

| Operation | Minimum Permission |
| :--- | :--- |
| Discover catalogs | Manager |
| Discover schemas | Manager |
| Validate schemas | Manager |
| Bulk create datastores | Manager |
| Link enrichment to source datastore | Member |
| Unlink enrichment from source datastore | Admin |
