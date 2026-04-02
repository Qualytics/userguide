# Datastore Grouping Permissions

Datastore Grouping uses two independent layers of access control in Qualytics: **User Roles** (organization-level) and **Team Permissions** (resource-level). A user may need to satisfy both layers to perform certain actions.

!!! note "Two Permission Systems"
    Qualytics has two separate role systems. **User Roles** (Viewer, Member, Editor, Manager, Admin) control what a user can do across the entire workspace. **Team Permissions** (Reporter, Viewer, Drafter, Author, Editor) control what a user can do on specific datastores they have access to through team membership. The role names overlap (e.g., "Viewer" and "Editor" exist in both) but they are **independent systems** with different scopes.

## User Roles (Organization-Level)

User Roles determine what type of actions a user can perform across the workspace. Group management actions (create, edit, delete) are controlled at this level.

| Action | Viewer | Member | Editor | Manager | Admin |
| :--- | :---: | :---: | :---: | :---: | :---: |
| View groups | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } |
| Create a group | :material-close-circle-outline:{ title="Not allowed" } | :material-close-circle-outline:{ title="Not allowed" } | :material-close-circle-outline:{ title="Not allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } |
| Edit a group | :material-close-circle-outline:{ title="Not allowed" } | :material-close-circle-outline:{ title="Not allowed" } | :material-close-circle-outline:{ title="Not allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } |
| Delete a group | :material-close-circle-outline:{ title="Not allowed" } | :material-close-circle-outline:{ title="Not allowed" } | :material-close-circle-outline:{ title="Not allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } |
| Add/remove datastore from group | :material-close-circle-outline:{ title="Not allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } |

!!! note "Manage Groups Button"
    The **Manage groups :material-bookmark-box-outline:** button in the tree view header is only visible to users with the **Manager** role or above. Users with lower roles can still see groups and their contents, but cannot access the group management panel.

## Team Permissions (Resource-Level)

Team Permissions determine what a user can do on a specific datastore. Adding or removing a datastore from a group requires Editor permission on that datastore's team.

| Action | Reporter | Viewer | Drafter | Author | Editor |
| :--- | :---: | :---: | :---: | :---: | :---: |
| View groups in tree | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } |
| Add datastore to group | :material-close-circle-outline:{ title="Not allowed" } | :material-close-circle-outline:{ title="Not allowed" } | :material-close-circle-outline:{ title="Not allowed" } | :material-close-circle-outline:{ title="Not allowed" } | :material-check-circle:{ title="Allowed" } |
| Remove datastore from group | :material-close-circle-outline:{ title="Not allowed" } | :material-close-circle-outline:{ title="Not allowed" } | :material-close-circle-outline:{ title="Not allowed" } | :material-close-circle-outline:{ title="Not allowed" } | :material-check-circle:{ title="Allowed" } |

## How Both Layers Work Together

To **add or remove a datastore from a group**, a user must satisfy both layers:

1. **User Role**: Must be at least **Member** (organization-level)
2. **Team Permission**: Must have **Editor** permission on the specific datastore (resource-level)

To **create, edit, or delete a group**, a user only needs:

1. **User Role**: Must be **Manager** or **Admin** (organization-level). No team permission is required since groups are workspace-wide resources.

!!! info "Admin Bypass"
    Users with the **Admin** role bypass all team-level permission checks. An Admin can add or remove any datastore from any group regardless of team membership.

## UI Behavior Without Permission

| Scenario | What the User Sees |
| :--- | :--- |
| User is below Manager role | The **Manage groups :material-bookmark-box-outline:** button is **hidden** — the user cannot access the group management panel. |
| User is below Editor team permission | The **Assign to group :material-bookmark-box-outline:** button on datastore hover is **hidden** — the user cannot add or remove the datastore from a group. |
| User has Editor but is below Member role | The API returns **403 Forbidden** — the user role check fails before the team permission is evaluated. |

## Important Notes

- **Group visibility is not restricted**: All users can see all groups and their contents, regardless of role. There is no way to hide a group from specific users.
- **Datastore permissions are independent**: Adding a datastore to a group does not change who can access or modify that datastore. Existing team permissions remain unchanged.
- **Favorite status is independent**: Adding a datastore to a group does not affect its favorite status, and vice versa.

!!! info "Full Permissions Reference"
    For the complete permissions and roles matrix across all Qualytics features, see the [Team Permissions](../../../../settings/security/team-permissions.md){:target="_blank"} page.
