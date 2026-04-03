# Datastore Enrichment Permissions

This page covers the roles and permissions required to link, unlink, and manage enrichment datastore settings on source datastores.

!!! note "Two Permission Systems"
    Qualytics has two separate role systems. **User Roles** (Viewer, Member, Editor, Manager, Admin) control what a user can do across the entire workspace. **Team Permissions** (Reporter, Viewer, Drafter, Author, Editor) control what a user can do on specific datastores they have access to through team membership. The role names overlap (e.g., "Viewer" and "Editor" exist in both) but they are **independent systems** with different scopes.

## User Roles (Workspace-Level)

User Roles determine the type of actions a user can perform across the workspace.

| Action | Viewer | Member | Editor | Manager | Admin |
| :--- | :---: | :---: | :---: | :---: | :---: |
| View enrichment datastore | :material-close-circle-outline:{ title="Not allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } |
| Preview enrichment datastore | :material-close-circle-outline:{ title="Not allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } |
| Link enrichment datastore | :material-close-circle-outline:{ title="Not allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } |
| Edit enrichment settings | :material-close-circle-outline:{ title="Not allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } |
| Unlink enrichment datastore | :material-close-circle-outline:{ title="Not allowed" } | :material-close-circle-outline:{ title="Not allowed" } | :material-close-circle-outline:{ title="Not allowed" } | :material-close-circle-outline:{ title="Not allowed" } | :material-check-circle:{ title="Allowed" } |

## Team Permissions (Asset-Level)

Team Permissions determine what a user can do on a specific datastore within their assigned teams. These are checked **in addition** to User Roles.

| Action | Reporter | Viewer | Drafter | Author | Editor |
| :--- | :---: | :---: | :---: | :---: | :---: |
| View enrichment datastore | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } |
| Preview enrichment datastore | :material-close-circle-outline:{ title="Not allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } |
| Link enrichment datastore | :material-close-circle-outline:{ title="Not allowed" } | :material-close-circle-outline:{ title="Not allowed" } | :material-close-circle-outline:{ title="Not allowed" } | :material-close-circle-outline:{ title="Not allowed" } | :material-check-circle:{ title="Allowed" } |
| Edit enrichment settings | :material-close-circle-outline:{ title="Not allowed" } | :material-close-circle-outline:{ title="Not allowed" } | :material-close-circle-outline:{ title="Not allowed" } | :material-close-circle-outline:{ title="Not allowed" } | :material-check-circle:{ title="Allowed" } |
| Unlink enrichment datastore | :material-minus:{ title="Not applicable" } | :material-minus:{ title="Not applicable" } | :material-minus:{ title="Not applicable" } | :material-minus:{ title="Not applicable" } | :material-minus:{ title="Not applicable" } |

!!! note
    **Unlinking** is restricted to **Admin** user role only — no team permission check is performed. The dashes (—) indicate that team permissions are not applicable for this action.

## How Both Layers Work Together

To **link an enrichment datastore** or **edit enrichment settings**, a user must satisfy both layers:

1. **User Role**: Must be at least **Member** (workspace-level)
2. **Team Permission**: Must have **Editor** permission on the source datastore (asset-level)

To **unlink an enrichment datastore**, a user only needs:

1. **User Role**: Must be **Admin** (workspace-level). No team permission is checked.

To **view enrichment datastore** information:

1. **User Role**: Must be at least **Member** (workspace-level)
2. **Team Permission**: Must have at least **Reporter** permission on the source datastore (asset-level)

!!! info "Admin Bypass"
    Users with the **Admin** role bypass all team-level permission checks. An Admin can link, edit, and unlink enrichment datastores on any source datastore regardless of team membership.

## UI Behavior Without Permission

| Scenario | What the User Sees |
| :--- | :--- |
| User has Viewer workspace role | Cannot access enrichment endpoints — the API returns **403 Forbidden**. |
| User has Member role but no Editor team permission | The **Enrichment :material-database-import-outline:** option in the Settings menu is **visible** but attempting to save returns an error. |
| User is not Admin and tries to unlink | The unlink option is **hidden** or returns **403 Forbidden** when called via API. |
| User has no team access to the datastore | The datastore is not listed — the user cannot see it at all. |

## Key Details

- **Viewing** enrichment datastores is available to all users with at least **Member** role and **Reporter** team permission.
- **Previewing** (browsing enrichment tables and source records) requires at least **Viewer** team permission.
- **Linking and editing** enrichment settings requires **Member** role and **Editor** team permission on the source datastore.
- **Unlinking** is restricted to **Admin** only, as it is a destructive operation that stops enrichment data from being written.

!!! info "Enrichment Datastore Management"
    Creating, editing, and deleting enrichment datastores as standalone entities are not specific to the source datastore context. Those permissions will be covered in the [Enrichment Datastores](../../enrichment/overview-of-an-enrichment-datastore.md){:target="_blank"} documentation.

!!! info "Full Permissions Reference"
    For the complete permissions and roles matrix across all Qualytics features, see the [Team Permissions](../../settings/security/team-permissions.md){:target="_blank"} page.
