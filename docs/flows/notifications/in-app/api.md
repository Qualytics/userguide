# In App Notification API

This page documents the API endpoints related to In App notification operations within Flows.

All endpoints use the base URL of your Qualytics deployment (e.g., `https://your-instance.qualytics.io/api`).

!!! note
    In App notifications do not have specific configuration properties beyond the message. They are automatically delivered to all Qualytics users when triggered.

## Get Notification Tokens

Retrieves the available message tokens for each trigger type.

**Endpoint**: `GET /api/flows/actions/notification/tokens`

**Permission**: Member

??? example "Example request and response"

    **Request**:

    ```bash
    curl -X GET "https://your-instance.qualytics.io/api/flows/actions/notification/tokens" \
      -H "Authorization: Bearer YOUR_TOKEN"
    ```

    **Response** (abbreviated):

    ```json
    [
      {
        "trigger_type": "anomaly",
        "valid_message_tokens": ["{{flow_name}}", "{{datastore_name}}", "{{container_name}}", "{{anomaly_message}}", "{{anomaly_type}}"],
        "default_message": "..."
      },
      {
        "trigger_type": "operation",
        "valid_message_tokens": ["{{flow_name}}", "{{datastore_name}}", "{{operation_type}}", "{{operation_result}}"],
        "default_message": "..."
      }
    ]
    ```

## Test Notification

Sends a test In App notification to verify the configuration.

**Endpoint**: `POST /api/flows/actions/notifications/test`

**Permission**: Manager

??? example "Example request"

    ```bash
    curl -X POST "https://your-instance.qualytics.io/api/flows/actions/notifications/test" \
      -H "Authorization: Bearer YOUR_TOKEN" \
      -H "Content-Type: application/json" \
      -d '{
        "type": "InApp",
        "tokenized_message": "Test notification from {{ flow_name }}"
      }'
    ```

    **Response**: `200 OK` with a success confirmation.
