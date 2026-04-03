# Microsoft Teams Notification API

This page documents the API endpoints related to Microsoft Teams notification operations within Flows.

All endpoints use the base URL of your Qualytics deployment (e.g., `https://your-instance.qualytics.io/api`).

## Get Notification Specifications

Retrieves the specifications for configuring Microsoft Teams notifications in Flow actions.

**Endpoint**: `GET /api/flows/actions/notification/specifications`

**Permission**: Member

??? example "Example response (Microsoft Teams entry)"

    ```json
    {
      "display_name": "Microsoft Teams",
      "type": "MSFT_Teams",
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
| `channel` | enum | Yes | The Microsoft Teams channel where notifications will be sent. The available channels are retrieved from your connected Teams workspace. |

## Get Notification Tokens

Retrieves the available message tokens for each trigger type.

**Endpoint**: `GET /api/flows/actions/notification/tokens`

**Permission**: Member

## Test Notification

Sends a test Microsoft Teams notification to verify the configuration.

**Endpoint**: `POST /api/flows/actions/notifications/test`

**Permission**: Manager

??? example "Example request"

    ```bash
    curl -X POST "https://your-instance.qualytics.io/api/flows/actions/notifications/test" \
      -H "Authorization: Bearer YOUR_TOKEN" \
      -H "Content-Type: application/json" \
      -d '{
        "type": "MSFT_Teams",
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
