# Email Notification API

This page documents the API endpoints related to Email notification operations within Flows.

All endpoints use the base URL of your Qualytics deployment (e.g., `https://your-instance.qualytics.io/api`).

## Get Notification Specifications

Retrieves the specifications for configuring Email notifications in Flow actions.

**Endpoint**: `GET /api/flows/actions/notification/specifications`

**Permission**: Member

??? example "Example response (Email entry)"

    ```json
    {
      "display_name": "Email",
      "type": "Email",
      "properties": [
        {
          "field": "emails",
          "map_to": "parameters",
          "required": true,
          "title": "Email Address",
          "type": "string",
          "placeholder": "user1@example.com, user2@example.com"
        },
        {
          "field": "email_subject",
          "map_to": "parameters",
          "required": false,
          "title": "Email Subject",
          "type": "string",
          "default": "Qualytics Notification",
          "placeholder": "Qualytics Notification"
        }
      ]
    }
    ```

### Configuration Properties

| Property | Type | Required | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `emails` | string | Yes | — | Comma-separated list of email addresses |
| `email_subject` | string | No | `Qualytics Notification` | Subject line of the notification email |

## Get Notification Tokens

Retrieves the available message tokens for each trigger type.

**Endpoint**: `GET /api/flows/actions/notification/tokens`

**Permission**: Member

## Test Notification

Sends a test Email notification to verify the configuration.

**Endpoint**: `POST /api/flows/actions/notifications/test`

**Permission**: Manager

??? example "Example request"

    ```bash
    curl -X POST "https://your-instance.qualytics.io/api/flows/actions/notifications/test" \
      -H "Authorization: Bearer YOUR_TOKEN" \
      -H "Content-Type: application/json" \
      -d '{
        "type": "Email",
        "tokenized_message": "Test notification from {{ flow_name }}",
        "parameters": {
          "emails": "user@example.com",
          "email_subject": "Qualytics Test Alert"
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
