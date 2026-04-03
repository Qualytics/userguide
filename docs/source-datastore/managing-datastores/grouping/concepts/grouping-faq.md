# Datastore Grouping FAQ

## General

### What's the difference between groups and tags?

Groups and tags serve different purposes. A **group** organizes datastores visually in the tree view — each datastore can belong to only one group. A **tag** is a flexible label for categorization, filtering operations, and quality score weighting — a datastore can have multiple tags. Use groups for navigation structure and tags for classification.

### Can a datastore belong to multiple groups?

No. A datastore can belong to **zero or one** group at a time. If you assign a datastore to a new group, it is automatically removed from the previous group.

### Is there a maximum number of groups?

No. There is no programmatic limit on the number of groups you can create.

### Are groups visible to all users?

Yes. Groups are **workspace-wide** — all users in the workspace see the same groups and the same datastore assignments.

### If I create or modify a group, does it affect all users?

Yes. Groups are shared across the entire workspace. When you create a group, assign a datastore to a group, rename a group, or delete a group, **every user** in the workspace sees the change immediately. There are no personal or private groups — all grouping is organization-wide.

### What happens to datastores when I delete a group?

The datastores are **not deleted**. They simply become ungrouped and appear in the "Ungrouped" section of the tree view. If you had an active filter by that group on the listing page, the filter will no longer match any datastores — clear the filter to see all datastores again.

### What happens if a datastore is both favorited and grouped?

The datastore appears in **both sections** of the tree view. In the **Favorites** section at the top, it is shown under a sub-section with the group's name and icon. In the **regular groups** section below, it appears alongside non-favorited datastores in the same group. Favorites are personal (per user), while groups are shared across the workspace.

### Can I reorder groups in the tree view?

Groups are displayed in **alphabetical order** by name. To change the order, rename the groups (e.g., prefix with numbers like "01 - Production", "02 - Staging").

## Permissions

### Who can create groups?

Only users with the **Manager** role can create, edit, or delete groups. See the [Permissions](permissions.md){:target="_blank"} page for details.

### Who can assign datastores to groups?

Users with the **Member** user role and **Editor** team permission on the datastore can assign it to or remove it from a group. Admin users bypass team-level checks. See the [Permissions](permissions.md){:target="_blank"} page for details.

### Does assigning a datastore to a group change its permissions?

No. Group membership is purely organizational. It does not affect who can access, edit, or manage the datastore.

## Icons

### What icons are available?

There are 10 predefined icons: Bookmark (default), Folder, Shape, Chart, Flask, Star, Texture, Bronze, Silver, and Gold. For the full list with visual previews, see the [Create a Group](../managing-groups/create-a-group.md#available-icons){:target="_blank"} page.

### Can I use custom icons?

No. Icons are limited to the predefined set.

### Is an icon required when creating a group?

No. The icon is optional. If not set, the group displays with the default **Bookmark** :material-bookmark-box-outline: icon.

## API

### Can I manage groups via the API?

Yes. You can create, update, delete groups and assign/unassign datastores from groups via the API. See the [Grouping API](grouping-api.md){:target="_blank"} page for endpoints, examples, and valid icon values.
