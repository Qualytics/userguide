# Slack Notification API

This page documents the API endpoints related to Slack notification operations within Flows.

All endpoints use the base URL of your Qualytics deployment (e.g., `https://your-instance.qualytics.io/api`).

## Get Notification Specifications

Retrieves the specifications for configuring Slack notifications in Flow actions.

**Endpoint**: `GET /api/flows/actions/notification/specifications`

**Permission**: Member

??? example "Example response (Slack entry)"

    ```json
    {
      "display_name": "Slack",
      "type": "Slack",
      "properties": [
        {
          "field": "channel",
          "map_to": "parameters",
          "required": true,
          "title": "Channel",
          "type": "enum",
          "placeholder": "general"
        }
      ]
    }
    ```

### Configuration Properties

| Property | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `channel` | enum | Yes | The Slack channel where notifications will be sent. The available channels are retrieved from your connected Slack workspace. |

## Get Notification Tokens

Retrieves the available message tokens for each trigger type.

**Endpoint**: `GET /api/flows/actions/notification/tokens`

**Permission**: Member

## Test Notification

Sends a test Slack notification to verify the configuration.

**Endpoint**: `POST /api/flows/actions/notifications/test`

**Permission**: Manager

??? example "Example request"

    ```bash
    curl -X POST "https://your-instance.qualytics.io/api/flows/actions/notifications/test" \
      -H "Authorization: Bearer YOUR_TOKEN" \
      -H "Content-Type: application/json" \
      -d '{
        "type": "Slack",
        "tokenized_message": "Test notification from {{ flow_name }}",
        "parameters": {
          "channel": "general"
        }
      }'
    ```

    **Response**: `200 OK` with a success confirmation.

## Permission Summary

| Operation | Minimum Permission |
| :--- | :--- |
| View notification specifications | Member |
| View notification tokens | Member |
| Test notification | Manager |
