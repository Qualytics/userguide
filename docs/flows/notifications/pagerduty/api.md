# PagerDuty Notification API

This page documents the API endpoints related to PagerDuty notification operations within Flows.

All endpoints use the base URL of your Qualytics deployment (e.g., `https://your-instance.qualytics.io/api`).

## Get Notification Specifications

Retrieves the specifications for configuring PagerDuty notifications in Flow actions.

**Endpoint**: `GET /api/flows/actions/notification/specifications`

**Permission**: Member

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

### Configuration Properties

| Property | Type | Required | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `severity` | enum | No | `info` | Severity level: `info`, `warning`, `error`, `critical` |
| `custom_details` | object | No | — | Key-value pairs for additional incident context |
| `routing_key` | string (secret) | No | — | Override the default Routing Key to route to a different PagerDuty service |

## Get Notification Tokens

Retrieves the available message tokens for each trigger type.

**Endpoint**: `GET /api/flows/actions/notification/tokens`

**Permission**: Member

## Test Notification

Sends a test PagerDuty notification to verify the configuration.

**Endpoint**: `POST /api/flows/actions/notifications/test`

**Permission**: Manager

??? example "Example request"

    ```bash
    curl -X POST "https://your-instance.qualytics.io/api/flows/actions/notifications/test" \
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

!!! warning
    Test notifications **will create an incident** in your PagerDuty service (unlike connection validation, which uses Change Events).

## Permission Summary

| Operation | Minimum Permission |
| :--- | :--- |
| View notification specifications | Member |
| View notification tokens | Member |
| Test notification | Manager |
