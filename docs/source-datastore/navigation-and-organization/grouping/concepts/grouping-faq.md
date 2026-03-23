# Datastore Grouping FAQ

## General

### Can a datastore belong to multiple groups?

No. A datastore can belong to **zero or one** group at a time. If you assign a datastore to a new group, it is automatically removed from the previous group.

### Are groups visible to all users?

Yes. Groups are **workspace-wide** — all users in the workspace see the same groups and the same datastore assignments.

### What happens to datastores when I delete a group?

The datastores are **not deleted**. They simply become ungrouped and appear in the "Ungrouped" section of the tree view.

### Can I reorder groups in the tree view?

Groups are displayed in **alphabetical order** by name. To change the order, rename the groups (e.g., prefix with numbers like "01 - Production", "02 - Staging").

## Permissions

### Who can create groups?

Only users with the **Manager** role can create, edit, or delete groups.

### Who can assign datastores to groups?

Users with **Editor** permission on a datastore can assign it to or remove it from a group. You do not need Manager role to assign datastores.

### Does assigning a datastore to a group change its permissions?

No. Group membership is purely organizational. It does not affect who can access, edit, or manage the datastore.

!!! info "Full Permission Matrix"
    For a complete overview of all permissions across all features, see the [Team Permissions](../../../../settings/security/team-permissions.md){:target="_blank"} page.

## Icons

### What icons are available?

The following icons are available for groups: **Bookmark**, **Folder**, **Shape**, **Chart**, **Flask**, **Star**, **Texture**, **Bronze**, **Silver**, and **Gold**.

### Can I use custom icons?

No. Icons are limited to the predefined set listed above.

### Is an icon required when creating a group?

No. The icon is optional. If not set, the group displays with a default icon.
