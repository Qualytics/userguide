# Datastore Tags Permissions

This page covers the roles and permissions required to assign and unassign tags on source datastores.

## Permission Matrix

The table below shows which roles can perform tag-related actions on datastores:

| Action | Viewer | Member | Editor | Manager | Admin |
| :--- | :---: | :---: | :---: | :---: | :---: |
| View tags on datastores | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } |
| Assign tags to datastores | :material-close-circle-outline:{ title="Not allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } |
| Unassign tags from datastores | :material-close-circle-outline:{ title="Not allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } |
| Use tags to filter operations | :material-close-circle-outline:{ title="Not allowed" } | :material-close-circle-outline:{ title="Not allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } |

## Key Details

- **Viewing tags** on datastores is available to all roles, including **Viewer**.
- **Assigning and unassigning tags** to datastores requires at least the **Member** role in one of the teams the datastore is assigned to.
- **Using tags to filter operations** (scoping Profile/Scan to tagged containers) requires the **Editor** role or above.
- **Admin** users bypass all permission checks and can manage tags across all datastores regardless of team membership.

!!! info "Tag Management Permissions"
    Creating, editing, and deleting tags are global actions not specific to datastores. For those permissions, see the [Tags](../../tags/overview.md){:target="_blank"} documentation.

!!! info "Full Permissions Reference"
    For the complete permissions and roles matrix across all Qualytics features, see the [Team Permissions](../../settings/security/team-permissions.md){:target="_blank"} page.
