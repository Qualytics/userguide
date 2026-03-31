# Datastore Enrichment Permissions

This page covers the roles and permissions required to link, unlink, and manage enrichment datastore settings on source datastores.

Enrichment datastore actions are controlled by two layers: **User Roles** (workspace-level) and **Team Permissions** (asset-level). Both must be satisfied for an action to succeed.

## User Roles (Workspace-Level)

User Roles determine the type of actions a user can perform across the workspace.

| Action | Member | Manager | Admin |
| :--- | :---: | :---: | :---: |
| View enrichment datastore | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } |
| Preview enrichment datastore | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } |
| Link enrichment datastore | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } |
| Edit enrichment settings | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } |
| Unlink enrichment datastore | :material-close-circle-outline:{ title="Not allowed" } | :material-close-circle-outline:{ title="Not allowed" } | :material-check-circle:{ title="Allowed" } |

## Team Permissions (Asset-Level)

Team Permissions determine what a user can do on a specific datastore within their assigned teams. These are checked **in addition** to User Roles.

| Action | Reporter | Viewer | Drafter | Author | Editor |
| :--- | :---: | :---: | :---: | :---: | :---: |
| View enrichment datastore | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } |
| Preview enrichment datastore | :material-close-circle-outline:{ title="Not allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } |
| Link enrichment datastore | :material-close-circle-outline:{ title="Not allowed" } | :material-close-circle-outline:{ title="Not allowed" } | :material-close-circle-outline:{ title="Not allowed" } | :material-close-circle-outline:{ title="Not allowed" } | :material-check-circle:{ title="Allowed" } |
| Edit enrichment settings | :material-close-circle-outline:{ title="Not allowed" } | :material-close-circle-outline:{ title="Not allowed" } | :material-close-circle-outline:{ title="Not allowed" } | :material-close-circle-outline:{ title="Not allowed" } | :material-check-circle:{ title="Allowed" } |
| Unlink enrichment datastore | — | — | — | — | — |

!!! note
    **Unlinking** is restricted to **Admin** only at the User Role level — there is no team permission check. **Admin** users bypass all team permission checks.

## Key Details

- **Viewing** enrichment datastores is available to all users with at least **Member** role and **Reporter** team permission.
- **Previewing** (browsing enrichment tables and source records) requires at least **Viewer** team permission.
- **Linking and editing** enrichment settings requires **Editor** team permission on the source datastore.
- **Unlinking** is restricted to **Admin** only, as it is a destructive operation that stops enrichment data from being written.

!!! info "Enrichment Datastore Management"
    Creating, editing, and deleting enrichment datastores as standalone entities are not specific to the source datastore context. Those permissions will be covered in the [Enrichment Datastores](../../enrichment/overview-of-an-enrichment-datastore.md){:target="_blank"} documentation.

!!! info "Full Permissions Reference"
    For the complete permissions and roles matrix across all Qualytics features, see the [Team Permissions](../../settings/security/team-permissions.md){:target="_blank"} page.
