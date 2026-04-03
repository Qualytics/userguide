# Getting Started with Datastore Grouping

Datastore Grouping allows you to organize your datastores into custom groups within the tree view. Instead of browsing a flat list, you can create meaningful categories — such as by environment, team, domain, or priority — making it easier to locate and manage your data sources.

Each datastore can belong to **one group at a time**. Ungrouped datastores appear in the default "Ungrouped" section of the tree view. The **Manager** role is required to create, edit, and delete groups; adding or removing datastores from groups requires the **Member** user role and **Editor** team permission — see the [Permissions](concepts/permissions.md){:target="_blank"} page for details.

You can also filter datastores by group on the Source Datastores listing page, making it easy to narrow down results when working with many datastores.

In this section you will learn how grouping works, which roles can manage groups, and how to create, assign, and organize your datastores into groups.

!!! info "Groups vs. Tags"
    Groups and tags serve different purposes. A **group** organizes datastores visually in the tree view — each datastore can belong to only one group. A **tag** is a flexible label for categorization, filtering operations, and quality score weighting — a datastore can have multiple tags. Use groups for navigation structure and tags for classification.

<div class="grid cards" markdown>

-   :material-book-open-outline:{ .lg .middle } **Introduction**

    ---

    Understand what groups are, how they appear in the tree view, and best practices for organizing datastores.

    [:octicons-arrow-right-24: Introduction](concepts/understanding-grouping.md)

-   :material-shield-lock-outline:{ .lg .middle } **Permissions**

    ---

    See which roles can create, edit, delete groups and add or remove datastores from groups.

    [:octicons-arrow-right-24: Permissions](concepts/permissions.md)

-   :material-plus-circle:{ .lg .middle } **Create a Group**

    ---

    Create a new datastore group with a custom name and icon.

    [:octicons-arrow-right-24: Create](managing-groups/create-a-group.md)

-   :material-pencil-outline:{ .lg .middle } **Edit a Group**

    ---

    Rename a group or change its icon.

    [:octicons-arrow-right-24: Edit](managing-groups/edit-a-group.md)

-   :material-trash-can-outline:{ .lg .middle } **Delete a Group**

    ---

    Remove a group — datastores in the group become ungrouped.

    [:octicons-arrow-right-24: Delete](managing-groups/delete-a-group.md)

-   :material-bookmark-check-outline:{ .lg .middle } **Assign a Datastore to a Group**

    ---

    Add an existing datastore to a group from the tree view.

    [:octicons-arrow-right-24: Assign to Group](managing-groups/assign-a-datastore.md)

-   :material-bookmark-remove-outline:{ .lg .middle } **Unassign a Datastore from a Group**

    ---

    Unassign a datastore from its current group. The datastore moves to Ungrouped.

    [:octicons-arrow-right-24: Unassign from Group](managing-groups/unassign-a-datastore.md)

-   :material-filter-outline:{ .lg .middle } **Filter by Group**

    ---

    Filter the Source Datastores listing page to show only datastores in specific groups.

    [:octicons-arrow-right-24: Filter by Group](managing-groups/filter-by-group.md)

-   :material-api:{ .lg .middle } **API**

    ---

    API endpoints for managing datastore groups programmatically.

    [:octicons-arrow-right-24: API](concepts/grouping-api.md)

-   :material-help-circle-outline:{ .lg .middle } **FAQ**

    ---

    Answers to common questions about datastore grouping.

    [:octicons-arrow-right-24: FAQ](concepts/grouping-faq.md)

</div>
