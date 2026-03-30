# Datastore Grouping API

You can manage datastore groups programmatically using the Qualytics API. This page documents the available endpoints.

!!! tip
    For complete API documentation, including request/response schemas, visit the [API docs](https://demo.qualytics.io/api/docs).

## Endpoints

### List All Groups

Retrieves all datastore groups, ordered by name.

```
GET /api/datastore-groups
```

**Required Role**: Member

**Response Example**:

```json
[
  {
    "id": 1,
    "name": "Production",
    "icon": "gold",
    "created": "2026-02-23T17:00:00Z"
  },
  {
    "id": 2,
    "name": "Staging",
    "icon": "silver",
    "created": "2026-02-23T17:05:00Z"
  }
]
```

---

### Create a Group

Creates a new datastore group.

```
POST /api/datastore-groups
```

**Required Role**: Manager

**Request Body**:

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `name` | string | Yes | Group name (1-100 characters, must be unique) |
| `icon` | string | No | Icon identifier (e.g., `bookmark`, `folder`, `gold`) |

**Request Example**:

```json
{
  "name": "Production",
  "icon": "gold"
}
```

!!! warning
    Returns `409 Conflict` if a group with the same name already exists (case-insensitive).

---

### Update a Group

Updates an existing datastore group's name and/or icon.

```
PUT /api/datastore-groups/{id}
```

**Required Role**: Manager

**Request Body**:

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `name` | string | No | New group name (1-100 characters, must be unique) |
| `icon` | string | No | New icon identifier |

---

### Delete a Group

Deletes a datastore group. All datastores in the group become ungrouped.

```
DELETE /api/datastore-groups/{id}
```

**Required Role**: Manager

!!! note
    Deleting a group does **not** delete the datastores within it. They simply become ungrouped.

---

### Assign a Datastore to a Group

Assigns a datastore to a group, or removes it from its current group.

```
PUT /api/datastores/{id}/assign-group
```

**Required Role**: Editor (on the datastore)

**Request Body**:

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `group_id` | integer or null | Yes | The group ID to assign, or `null` to remove from the current group |

**Request Example** (assign to group):

```json
{
  "group_id": 1
}
```

**Request Example** (remove from group):

```json
{
  "group_id": null
}
```
