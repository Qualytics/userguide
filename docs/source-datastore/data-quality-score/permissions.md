# Datastore Quality Score Permissions

This page covers the roles and permissions required to view and manage data quality score settings on source datastores.

!!! note "Two Permission Systems"
    Qualytics has two separate role systems. **User Roles** (Viewer, Member, Editor, Manager, Admin) control what a user can do across the entire workspace. **Team Permissions** (Reporter, Viewer, Drafter, Author, Editor) control what a user can do on specific datastores they have access to through team membership. The role names overlap (e.g., "Viewer" and "Editor" exist in both) but they are **independent systems** with different scopes.

## User Roles (Workspace-Level)

User Roles determine the type of actions a user can perform across the workspace.

| Action | Viewer | Member | Editor | Manager | Admin |
| :--- | :---: | :---: | :---: | :---: | :---: |
| View quality scores | :material-close-circle-outline:{ title="Not allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } |
| View quality score settings | :material-close-circle-outline:{ title="Not allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } |
| Edit quality score settings | :material-close-circle-outline:{ title="Not allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } |

## Team Permissions (Asset-Level)

Team Permissions determine what a user can do on a specific datastore within their assigned teams. These are checked **in addition** to User Roles.

| Action | Reporter | Viewer | Drafter | Author | Editor |
| :--- | :---: | :---: | :---: | :---: | :---: |
| View quality scores | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } |
| View quality score settings | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } |
| Edit quality score settings | :material-close-circle-outline:{ title="Not allowed" } | :material-close-circle-outline:{ title="Not allowed" } | :material-close-circle-outline:{ title="Not allowed" } | :material-close-circle-outline:{ title="Not allowed" } | :material-check-circle:{ title="Allowed" } |

## How Both Layers Work Together

To **view quality scores**, a user must satisfy both layers:

1. **User Role**: Must be at least **Member** (workspace-level)
2. **Team Permission**: Must have at least **Reporter** permission on the datastore (asset-level)

To **edit quality score settings**, a user must satisfy both layers:

1. **User Role**: Must be at least **Member** (workspace-level)
2. **Team Permission**: Must have **Editor** permission on the datastore (asset-level)

!!! info "Admin Bypass"
    Users with the **Admin** role bypass all team-level permission checks. An Admin can view and edit quality score settings on any datastore regardless of team membership.

## UI Behavior Without Permission

| Scenario | What the User Sees |
| :--- | :--- |
| User has Viewer role (workspace) | Cannot access quality score endpoints — the API returns **403 Forbidden**. |
| User has Member role but Reporter team permission | Can view scores and settings but the **Save** button in the settings modal is **disabled**. |
| User has Member role but no team access | Cannot see the datastore at all — it is not listed. |

## Triggering Recalculations

Quality scores are recalculated automatically after Scan and Profile operations. Running these operations requires the **Editor** team permission. See the [Scan Operation](../operations/scan.md){:target="_blank"} and [Profile Operation](../operations/profile.md){:target="_blank"} pages for details on operation permissions.

!!! info "Full Permissions Reference"
    For the complete permissions and roles matrix across all Qualytics features, see the [Team Permissions](../../settings/security/team-permissions.md){:target="_blank"} page.
