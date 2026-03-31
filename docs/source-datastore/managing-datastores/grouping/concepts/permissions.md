# Datastore Grouping Permissions

Datastore Grouping uses two layers of access control in Qualytics: **User Roles** (organization-level) and **Team Permissions** (resource-level).

## User Roles (Organization-Level)

User Roles determine what type of actions a user can perform across the workspace. Group management actions (create, edit, delete) are controlled at this level.

| Action | Viewer | Member | Editor | Manager | Admin |
| :--- | :---: | :---: | :---: | :---: | :---: |
| View groups | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } |
| Create a group | :material-close-circle-outline:{ title="Not allowed" } | :material-close-circle-outline:{ title="Not allowed" } | :material-close-circle-outline:{ title="Not allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } |
| Edit a group | :material-close-circle-outline:{ title="Not allowed" } | :material-close-circle-outline:{ title="Not allowed" } | :material-close-circle-outline:{ title="Not allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } |
| Delete a group | :material-close-circle-outline:{ title="Not allowed" } | :material-close-circle-outline:{ title="Not allowed" } | :material-close-circle-outline:{ title="Not allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } |
| Manage Groups button (tree header) | :material-close-circle-outline:{ title="Not allowed" } | :material-close-circle-outline:{ title="Not allowed" } | :material-close-circle-outline:{ title="Not allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } |

## Team Permissions (Resource-Level)

Team Permissions determine what a user can do on a specific datastore. Assigning a datastore to a group requires Editor permission on that datastore.

| Action | Reporter | Viewer | Drafter | Author | Editor |
| :--- | :---: | :---: | :---: | :---: | :---: |
| View groups in tree | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } |
| Assign datastore to group | :material-close-circle-outline:{ title="Not allowed" } | :material-close-circle-outline:{ title="Not allowed" } | :material-close-circle-outline:{ title="Not allowed" } | :material-close-circle-outline:{ title="Not allowed" } | :material-check-circle:{ title="Allowed" } |
| Remove datastore from group | :material-close-circle-outline:{ title="Not allowed" } | :material-close-circle-outline:{ title="Not allowed" } | :material-close-circle-outline:{ title="Not allowed" } | :material-close-circle-outline:{ title="Not allowed" } | :material-check-circle:{ title="Allowed" } |

## How Both Layers Work Together

To **assign a datastore to a group**, a user must satisfy both layers:

1. **Role**: Must be at least a **Member** (organization-level)
2. **Team Permission**: Must have **Editor** permission on the specific datastore (resource-level)

To **create, edit, or delete a group**, a user only needs:

1. **Role**: Must be a **Manager** or **Admin** (organization-level)

## Important Notes

- **Group visibility is not restricted**: All users can see all groups, regardless of their role. There is no way to hide a group from specific users.
- **Datastore permissions are independent**: Assigning a datastore to a group does not change who can access or modify that datastore. Existing datastore-level permissions remain unchanged.
- **Favorite status is independent**: Assigning a datastore to a group does not affect its favorite status, and vice versa.

!!! info "Full Permissions Reference"
    For the complete permissions and roles matrix across all Qualytics features, see the [Team Permissions](../../../../settings/security/team-permissions.md){:target="_blank"} page.
