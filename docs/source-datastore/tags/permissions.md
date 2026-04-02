# Datastore Tags Permissions

This page covers the roles and permissions required to assign and unassign tags on source datastores.

## Permission Matrix

The table below shows which roles can perform tag-related actions on datastores:

| Action | Viewer | Member | Editor | Manager | Admin |
| :--- | :---: | :---: | :---: | :---: | :---: |
| View tags on datastores | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } |
| Assign tags to datastores | :material-close-circle-outline:{ title="Not allowed" } | :material-close-circle-outline:{ title="Not allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } |
| Unassign tags from datastores | :material-close-circle-outline:{ title="Not allowed" } | :material-close-circle-outline:{ title="Not allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } |
| Run operations filtered by tag | :material-close-circle-outline:{ title="Not allowed" } | :material-close-circle-outline:{ title="Not allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } | :material-check-circle:{ title="Allowed" } |

## Key Details

- **Viewing tags** on datastores is available to all roles, including **Viewer**.
- **Assigning and unassigning tags** requires the **Editor** role or above in at least one of the teams the datastore belongs to. This is a team-level permission — the user must be a member of a team that has Editor access to the datastore.
- **Running operations filtered by tag** (scoping Profile/Scan to tagged containers) requires the **Editor** role or above. This is the same permission required to run any operation — the tag filter is part of the operation configuration, not a separate permission.
- **Admin** users bypass all team-level permission checks and can manage tags across all datastores regardless of team membership.

!!! info "Team Context"
    Permissions for assign/unassign are evaluated against the datastore's **team assignments**. A user with the Editor role must be in at least one team that the datastore belongs to. For more details on how teams work, see the [Team Permissions](../../settings/security/team-permissions.md){:target="_blank"} page.

## UI Behavior Without Permission

| Scenario | What the User Sees |
| :--- | :--- |
| User has Viewer or Member role (no Editor team permission) | The **:material-plus:** button next to "Assign tags to this datastore" is **hidden** — the tag selector cannot be opened. Tags are displayed as read-only. |
| User has Editor team permission but Viewer workspace role | The tag selector is visible but the API returns **403 Forbidden** when attempting to save. |
| User has no team access to the datastore | The datastore is not listed — the user cannot see it at all. |

<!-- TODO: Update link to tags/overview-of-a-tag.md when the dedicated Tags overview page is created -->
!!! info "Creating, Editing, or Deleting Tags"
    Creating, editing, and deleting tags are global actions not specific to datastores. These actions require the **Admin** role. For those permissions, see the [Tags](../../tags/overview.md){:target="_blank"} documentation.

!!! info "Full Permissions Reference"
    For the complete permissions and roles matrix across all Qualytics features, see the [Team Permissions](../../settings/security/team-permissions.md){:target="_blank"} page.
