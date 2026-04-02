# Getting Started with Datastore Tags

Tags are flexible labels that help you categorize, organize, and filter your source datastores in Qualytics. By assigning tags to datastores, you can classify them by environment, compliance, team, or any custom category — and those tags automatically cascade to all containers, fields, checks, and anomalies within the datastore.

In this section you will learn how tags work, which roles can manage them, and how to assign or remove tags from your datastores — both through the UI and the API. Any user with the **Editor** role can assign and unassign tags; the **Admin** role is required to create, edit, or delete tags.

<!-- TODO: Update link to tags/overview-of-a-tag.md when the dedicated Tags overview page is created -->
!!! info "Creating, Editing, or Deleting Tags"
    This section covers assigning and unassigning **existing** tags to source datastores. To create new tags, edit tag properties, or delete tags, see the [Tags](../../tags/overview.md){:target="_blank"} section.

<div class="grid cards" markdown>

-   :material-book-open-outline:{ .lg .middle } **Introduction**

    ---

    Understand how tags work with datastores, tag types, inheritance, and how to use tags to filter operations.

    [:octicons-arrow-right-24: Introduction](introduction.md)

-   :material-shield-lock-outline:{ .lg .middle } **Permissions**

    ---

    See which roles can view, assign, create, edit, and delete tags on datastores.

    [:octicons-arrow-right-24: Permissions](permissions.md)

-   :material-tag-plus:{ .lg .middle } **Assign a Tag**

    ---

    Assign an existing tag to a source datastore from the tree view footer panel.

    [:octicons-arrow-right-24: Assign a Tag](assign-tags.md)

-   :material-tag-off-outline:{ .lg .middle } **Unassign a Tag**

    ---

    Remove an existing tag from a source datastore without deleting the tag itself.

    [:octicons-arrow-right-24: Unassign a Tag](unassign-tags.md)

-   :material-api:{ .lg .middle } **API**

    ---

    API endpoints and examples for assigning and unassigning tags on datastores.

    [:octicons-arrow-right-24: API](api.md)

-   :material-help-circle-outline:{ .lg .middle } **FAQ**

    ---

    Common questions about tag inheritance, cascading behavior, filtering operations by tag, and tag limits.

    [:octicons-arrow-right-24: FAQ](faq.md)

</div>
