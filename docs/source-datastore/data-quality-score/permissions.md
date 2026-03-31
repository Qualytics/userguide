# Datastore Quality Score Permissions

This page covers the roles and permissions required to view and manage data quality score settings on source datastores.

Data quality score actions are controlled by two layers: **User Roles** (workspace-level) and **Team Permissions** (asset-level). Both must be satisfied for an action to succeed.

## User Roles (Workspace-Level)

User Roles determine the type of actions a user can perform across the workspace.

| Action | Member | Manager | Admin |
| :--- | :---: | :---: | :---: |
| View quality scores | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } |
| View quality score settings | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } |
| Edit quality score settings | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } |

## Team Permissions (Asset-Level)

Team Permissions determine what a user can do on a specific datastore within their assigned teams. These are checked **in addition** to User Roles.

| Action | Reporter | Viewer | Drafter | Author | Editor |
| :--- | :---: | :---: | :---: | :---: | :---: |
| View quality scores (historical) | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } |
| View quality score settings | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } |
| Edit quality score settings | :material-close-circle-outline:{ title="Not allowed" } | :material-close-circle-outline:{ title="Not allowed" } | :material-close-circle-outline:{ title="Not allowed" } | :material-close-circle-outline:{ title="Not allowed" } | :material-check-circle:{ title="Allowed" } |

## Key Details

- **Viewing quality scores** (the score values displayed on containers and the datastore overview) is available to all users with at least **Reporter** team permission.
- **Viewing quality score settings** (decay period, dimension weights) is available to all **Member** users — no team-level permission check is enforced.
- **Editing quality score settings** (adjusting decay period, enabling/disabling dimensions, changing weights) requires the **Editor** team permission on the datastore.
- **Recalculations are automatic** — quality scores are recalculated after every Scan, Profile, anomaly status change, and check deletion. There is no manual recalculation trigger.
- **Admin** users bypass all team permission checks.

!!! info "Full Permissions Reference"
    For the complete permissions and roles matrix across all Qualytics features, see the [Team Permissions](../../settings/security/team-permissions.md){:target="_blank"} page.
