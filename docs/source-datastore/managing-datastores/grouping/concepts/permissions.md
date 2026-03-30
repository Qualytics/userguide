# Permissions

Datastore Grouping uses two layers of access control in Qualytics: **User Roles** (organization-level) and **Team Permissions** (resource-level).

## User Roles (Organization-Level)

User Roles determine what type of actions a user can perform across the workspace. Group management actions (create, edit, delete) are controlled at this level.

| Action | Admin | Manager | Member |
| :--- | :---: | :---: | :---: |
| **View groups** | ✅ | ✅ | ✅ |
| **Create a group** | ✅ | ✅ | ❌ |
| **Edit a group** | ✅ | ✅ | ❌ |
| **Delete a group** | ✅ | ✅ | ❌ |
| **Manage Groups button** (tree header) | ✅ | ✅ | ❌ |

## Team Permissions (Resource-Level)

Team Permissions determine what a user can do on a specific datastore. Assigning a datastore to a group requires Editor permission on that datastore.

| Action | Reporter | Viewer | Drafter | Author | Editor |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **View groups in tree** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Assign datastore to group** | ❌ | ❌ | ❌ | ❌ | ✅ |
| **Remove datastore from group** | ❌ | ❌ | ❌ | ❌ | ✅ |

## How Both Layers Work Together

To **assign a datastore to a group**, a user must satisfy both layers:

1. **Role**: Must be at least a **Member** (organization-level)
2. **Team Permission**: Must have **Editor** permission on the specific datastore (resource-level)

To **create, edit, or delete a group**, a user only needs:

1. **Role**: Must be a **Manager** or **Admin** (organization-level)

!!! info "Full Permission Matrix"
    For a complete overview of all permissions across all features, see the [Team Permissions](../../../../settings/security/team-permissions.md){:target="_blank"} page.

## Important Notes

- **Group visibility is not restricted**: All users can see all groups, regardless of their role. There is no way to hide a group from specific users.
- **Datastore permissions are independent**: Assigning a datastore to a group does not change who can access or modify that datastore. Existing datastore-level permissions remain unchanged.
- **Favorite status is independent**: Assigning a datastore to a group does not affect its favorite status, and vice versa.
