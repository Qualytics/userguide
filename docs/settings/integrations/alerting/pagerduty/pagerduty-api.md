# PagerDuty API

This page documents the API endpoints related to PagerDuty integration operations. Use these endpoints to programmatically manage your PagerDuty integration — from creating and validating to editing and removing it.

All endpoints use the base URL of your Qualytics deployment (e.g., `https://your-instance.qualytics.io/api`).

## Add Integration via API

### Get Integration Specifications

Before creating the integration, you can retrieve the specifications to understand the required properties.

**Endpoint**: `GET /api/integrations-specifications`

**Permission**: Manager

??? example "Example request and response"

    **Request**:

    ```bash
    curl -X GET "https://your-instance.qualytics.io/api/integrations-specifications" \
      -H "Authorization: Bearer YOUR_TOKEN"
    ```

    **Response** (PagerDuty entry):

    ```json
    {
      "label": "PagerDuty",
      "type": "pagerduty",
      "implemented": true,
      "category": "alerting",
      "properties": [
        {
          "group": {
            "name": "Connection Properties",
            "outline": true
          },
          "field": "api_access_token",
          "map_to": "api_access_token",
          "required": true,
          "secret": true,
          "type": "string",
          "title": "Routing Key",
          "info_md": "The **Integration Key** (Routing Key) from your PagerDuty Events API v2 integration...",
          "placeholder": "your-routing-key"
        }
      ]
    }
    ```

### Create Integration

Creates a new PagerDuty integration with the provided Routing Key. Qualytics validates the key during creation by sending a Change Event to PagerDuty (which does **not** create an incident).

**Endpoint**: `POST /api/integrations`

**Permission**: Manager

**Request Body**:

| Property | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `type` | string | Yes | Must be `pagerduty` |
| `api_access_token` | string | Yes | The Routing Key (Integration Key) from your PagerDuty Events API v2 integration |

??? example "Example request and response"

    **Request**:

    ```bash
    curl -X POST "https://your-instance.qualytics.io/api/integrations" \
      -H "Authorization: Bearer YOUR_TOKEN" \
      -H "Content-Type: application/json" \
      -d '{
        "type": "pagerduty",
        "api_access_token": "your-pagerduty-routing-key"
      }'
    ```

    **Response**:

    ```json
    {
      "id": 5,
      "type": "pagerduty",
      "created": "2026-03-12T10:00:00Z",
      "updated": "2026-03-12T10:00:00Z"
    }
    ```

!!! note
    If the Routing Key is invalid, the creation will fail with a `400` error. Verify the key in your PagerDuty service under **Integrations > Events API v2**.

---

## Edit Integration via API

### Get Integration

Retrieves the details of a specific integration by ID. Use this to check the current state before editing.

**Endpoint**: `GET /api/integrations/{id}`

**Permission**: Manager

**Path Parameters**:

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `id` | integer | Yes | The integration ID |

??? example "Example request and response"

    **Request**:

    ```bash
    curl -X GET "https://your-instance.qualytics.io/api/integrations/5" \
      -H "Authorization: Bearer YOUR_TOKEN"
    ```

    **Response**:

    ```json
    {
      "id": 5,
      "type": "pagerduty",
      "created": "2026-03-12T10:00:00Z",
      "updated": "2026-03-12T10:00:00Z"
    }
    ```

### Update Integration

Updates an existing PagerDuty integration. Commonly used to rotate the Routing Key or change the target PagerDuty service.

**Endpoint**: `PUT /api/integrations/{id}`

**Permission**: Manager

**Path Parameters**:

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `id` | integer | Yes | The integration ID |

**Request Body**:

| Property | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `api_access_token` | string | No | The new Routing Key |

??? example "Example request and response"

    **Request**:

    ```bash
    curl -X PUT "https://your-instance.qualytics.io/api/integrations/5" \
      -H "Authorization: Bearer YOUR_TOKEN" \
      -H "Content-Type: application/json" \
      -d '{
        "api_access_token": "new-routing-key-value-here"
      }'
    ```

    **Response**:

    ```json
    {
      "id": 5,
      "type": "pagerduty",
      "created": "2026-03-12T10:00:00Z",
      "updated": "2026-03-12T11:30:00Z"
    }
    ```

!!! note
    Qualytics validates the new Routing Key before saving. If the key is invalid, the update will fail.

---

## Remove Integration via API

### Delete Integration

Deletes the PagerDuty integration. Any Flows using PagerDuty notifications will no longer be able to deliver alerts until a new integration is created.

**Endpoint**: `DELETE /api/integrations/{id}`

**Permission**: Manager

**Path Parameters**:

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `id` | integer | Yes | The integration ID |

??? example "Example request"

    ```bash
    curl -X DELETE "https://your-instance.qualytics.io/api/integrations/5" \
      -H "Authorization: Bearer YOUR_TOKEN"
    ```

    **Response**: `204 No Content`

!!! warning
    Deleting the integration does not delete Flow actions that reference PagerDuty. Those actions will fail to deliver notifications until the integration is re-created.

---

## Additional Endpoints

### List Channels

Returns the list of available channels for an alerting integration.

**Endpoint**: `GET /api/alerting/{type}/list-channels`

**Permission**: Manager

!!! note
    PagerDuty does not use channels — events are routed via Routing Keys, not channel selection. This endpoint returns an empty list for PagerDuty integrations.

??? example "Example request and response"

    **Request**:

    ```bash
    curl -X GET "https://your-instance.qualytics.io/api/alerting/pagerduty/list-channels" \
      -H "Authorization: Bearer YOUR_TOKEN"
    ```

    **Response**:

    ```json
    []
    ```

### Get Action Notification Specifications

Returns the specifications for configuring PagerDuty notifications in Flow actions, including severity levels, custom details, and routing key override.

**Endpoint**: `GET /api/action-notification-specifications`

**Permission**: Manager

??? example "Example response (PagerDuty entry)"

    ```json
    {
      "display_name": "PagerDuty",
      "type": "PagerDuty",
      "properties": [
        {
          "field": "severity",
          "map_to": "parameters",
          "required": false,
          "title": "Severity",
          "type": "enum",
          "values": [
            { "label": "Info", "value": "info" },
            { "label": "Warning", "value": "warning" },
            { "label": "Error", "value": "error" },
            { "label": "Critical", "value": "critical" }
          ],
          "default": "info"
        },
        {
          "field": "custom_details",
          "map_to": "parameters",
          "required": false,
          "title": "Additional Details",
          "type": "object",
          "info": "Enhance the PagerDuty alert by setting additional details"
        },
        {
          "field": "routing_key",
          "map_to": "parameters",
          "required": false,
          "title": "Routing Key Override",
          "info": "Override the default routing key from the PagerDuty integration to route events to a different PagerDuty service",
          "type": "string",
          "secret": true
        }
      ]
    }
    ```

### Test Notification

Sends a test PagerDuty notification to verify the configuration.

**Endpoint**: `POST /api/flows/actions/test-notification`

**Permission**: Manager

??? example "Example request"

    ```bash
    curl -X POST "https://your-instance.qualytics.io/api/flows/actions/test-notification" \
      -H "Authorization: Bearer YOUR_TOKEN" \
      -H "Content-Type: application/json" \
      -d '{
        "type": "PagerDuty",
        "tokenized_message": "Test notification from {{ flow_name }}",
        "parameters": {
          "severity": "info"
        }
      }'
    ```

    **Response**: `200 OK` with a success confirmation.

!!! tip
    Use the test notification endpoint to verify that your Routing Key and Flow action configuration are working correctly before publishing the Flow.

---

## Permission Summary

| Operation | Minimum Permission |
| :--- | :--- |
| View integration specifications | Manager |
| Create, update, or delete integration | Manager |
| List channels | Manager |
| Test notification | Manager |
| Configure Flow action notifications | Manager |
