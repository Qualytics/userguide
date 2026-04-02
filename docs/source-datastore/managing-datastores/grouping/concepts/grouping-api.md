# Datastore Grouping API

You can manage datastore groups programmatically using the Qualytics API.

!!! tip
    For complete API documentation, including request/response schemas, visit the [API docs](https://demo.qualytics.io/api/docs){:target="_blank"}.

All endpoints use the base URL of your Qualytics deployment (e.g., `https://your-instance.qualytics.io/api`).

---

## List All Groups

Retrieves all datastore groups, ordered by name.

**Endpoint**: `GET /api/datastore-groups`

**Permission**: Member

??? example "Example request and response"

    **Request**:

    ```bash
    curl -X GET "https://your-instance.qualytics.io/api/datastore-groups" \
      -H "Authorization: Bearer YOUR_TOKEN"
    ```

    **Response**:

    ```json
    [
      {
        "id": 1,
        "name": "Mission Critical",
        "icon": "mdi-star-outline",
        "created": "2026-03-31T14:00:00.000000Z"
      },
      {
        "id": 2,
        "name": "Analytics",
        "icon": "mdi-chart-box-outline",
        "created": "2026-03-31T14:05:00.000000Z"
      }
    ]
    ```

---

## Create a Group

Creates a new datastore group.

**Endpoint**: `POST /api/datastore-groups`

**Permission**: Manager

??? example "Example request and response"

    **Request**:

    ```bash
    curl -X POST "https://your-instance.qualytics.io/api/datastore-groups" \
      -H "Authorization: Bearer YOUR_TOKEN" \
      -H "Content-Type: application/json" \
      -d '{
        "name": "Production",
        "icon": "mdi-podium-gold"
      }'
    ```

    **Response** (200):

    ```json
    {
      "id": 3,
      "name": "Production",
      "icon": "mdi-podium-gold",
      "created": "2026-04-01T10:00:00.000000Z"
    }
    ```

**Request Body**:

| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| `name` | string | Yes | Group name (1–100 characters, must be unique, case-insensitive). |
| `icon` | string | No | Icon identifier. See [Valid Icon Values](#valid-icon-values) below. Defaults to `mdi-bookmark-box-outline`. |

For the UI equivalent, see [Create a Group](../managing-groups/create-a-group.md){:target="_blank"}.

---

## Update a Group

Updates an existing datastore group's name and/or icon.

**Endpoint**: `PUT /api/datastore-groups/{id}`

**Permission**: Manager

??? example "Example request and response"

    **Request**:

    ```bash
    curl -X PUT "https://your-instance.qualytics.io/api/datastore-groups/3" \
      -H "Authorization: Bearer YOUR_TOKEN" \
      -H "Content-Type: application/json" \
      -d '{
        "name": "Prod Critical",
        "icon": "mdi-star-outline"
      }'
    ```

    **Response** (200):

    ```json
    {
      "id": 3,
      "name": "Prod Critical",
      "icon": "mdi-star-outline",
      "created": "2026-04-01T10:00:00.000000Z"
    }
    ```

**Request Body**:

| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| `name` | string | No | New group name (1–100 characters, must be unique, case-insensitive). |
| `icon` | string | No | New icon identifier. See [Valid Icon Values](#valid-icon-values) below. |

For the UI equivalent, see [Edit a Group](../managing-groups/edit-a-group.md){:target="_blank"}.

---

## Delete a Group

Deletes a datastore group. All datastores in the group become ungrouped.

**Endpoint**: `DELETE /api/datastore-groups/{id}`

**Permission**: Manager

??? example "Example request and response"

    **Request**:

    ```bash
    curl -X DELETE "https://your-instance.qualytics.io/api/datastore-groups/3" \
      -H "Authorization: Bearer YOUR_TOKEN"
    ```

    **Response** (200): Returns the deleted group object.

    ```json
    {
      "id": 3,
      "name": "Prod Critical",
      "icon": "mdi-star-outline",
      "created": "2026-04-01T10:00:00.000000Z"
    }
    ```

!!! note
    Deleting a group does **not** delete the datastores within it — they simply become ungrouped.

For the UI equivalent, see [Delete a Group](../managing-groups/delete-a-group.md){:target="_blank"}.

---

## Assign a Datastore to a Group

Assigns a datastore to a group, or removes it from its current group. If the datastore already belongs to a different group, it is **automatically moved** to the new group.

**Endpoint**: `PATCH /api/datastores/{id}/assign-group`

**Permission**: Member user role + Editor team permission on the datastore. Admin users bypass team-level checks.

??? example "Assign to a group"

    **Request**:

    ```bash
    curl -X PATCH "https://your-instance.qualytics.io/api/datastores/42/assign-group" \
      -H "Authorization: Bearer YOUR_TOKEN" \
      -H "Content-Type: application/json" \
      -d '{
        "group_id": 1
      }'
    ```

    **Response** (200): Returns the updated datastore object (abbreviated).

    ```json
    {
      "id": 42,
      "name": "Healthcare Analytics",
      "group": {
        "id": 1,
        "name": "Mission Critical",
        "icon": "mdi-star-outline"
      }
    }
    ```

??? example "Remove from a group (unassign)"

    **Request**:

    ```bash
    curl -X PATCH "https://your-instance.qualytics.io/api/datastores/42/assign-group" \
      -H "Authorization: Bearer YOUR_TOKEN" \
      -H "Content-Type: application/json" \
      -d '{
        "group_id": null
      }'
    ```

    **Response** (200): Returns the updated datastore object with `"group": null`.

    ```json
    {
      "id": 42,
      "name": "Healthcare Analytics",
      "group": null
    }
    ```

**Request Body**:

| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| `group_id` | integer or null | Yes | The group ID to assign, or `null` to remove from the current group. |

For the UI equivalents, see [Assign a Datastore to a Group](../managing-groups/assign-a-datastore.md){:target="_blank"} and [Unassign a Datastore from a Group](../managing-groups/unassign-a-datastore.md){:target="_blank"}.

---

## Valid Icon Values

The `icon` field accepts the following MDI (Material Design Icons) identifiers:

<div class="icon-table" markdown>

| No. | Value | Label |
| :--- | :--- | :--- |
| 1. | `mdi-bookmark-box-outline` | Bookmark (default) |
| 2. | `mdi-folder-outline` | Folder |
| 3. | `mdi-shape-outline` | Shape |
| 4. | `mdi-chart-box-outline` | Chart |
| 5. | `mdi-flask-outline` | Flask |
| 6. | `mdi-star-outline` | Star |
| 7. | `mdi-texture-box` | Texture |
| 8. | `mdi-podium-bronze` | Bronze |
| 9. | `mdi-podium-silver` | Silver |
| 10. | `mdi-podium-gold` | Gold |

</div>

---

## Error Responses

| Status Code | Description |
| :--- | :--- |
| `401 Unauthorized` | Missing or invalid API token. |
| `403 Forbidden` | User does not have the required role or team permission. |
| `404 Not Found` | Group or datastore with the specified ID does not exist. |
| `409 Conflict` | Group name already exists (case-insensitive). |
| `422 Unprocessable Entity` | Invalid request body (e.g., name exceeds 100 characters). |

??? example "Error response examples"

    **403 Forbidden**:

    ```json
    { "detail": "You must have editor permission in at least one of these teams: ['Data Platform']" }
    ```

    **404 Not Found**:

    ```json
    { "detail": "Datastore group id: 999 not found" }
    ```

    **409 Conflict**:

    ```json
    { "detail": "Datastore group name: 'Production' already exists" }
    ```

---

## Permission Summary

| Operation | Minimum Permission |
| :--- | :--- |
| List all groups | Member |
| Create a group | Manager |
| Update a group | Manager |
| Delete a group | Manager |
| Assign a datastore to a group | Member user role + Editor team permission |
| Remove a datastore from a group | Member user role + Editor team permission |
