# Source Datastores Overview

Source Datastores are the foundation of data quality management in Qualytics. A source datastore represents a connection to your data — whether it's a relational database (JDBC), a distributed file system (DFS), or a cloud storage service. From here, you can connect your data sources, run quality operations, link enrichment datastores, manage data quality scores, and organize your datastores with groups and tags.

## Datastore

Learn the fundamentals of source datastores — supported connectors, connections, multi-schema creation, and how to add, edit, or delete datastores.

<div class="grid cards" markdown>

-   :material-database-outline:{ .lg .middle } **Getting Started**

    ---

    Understand what a datastore is, the architecture behind it, and how to get started.

    [:octicons-arrow-right-24: Getting Started](add-datastores/overview-of-a-datastore.md)

-   :material-view-list:{ .lg .middle } **Available Connectors**

    ---

    Browse the full list of supported JDBC and DFS connectors.

    [:octicons-arrow-right-24: View Connectors](add-datastores/available-datastore-connectors.md)

-   :material-database-marker-outline:{ .lg .middle } **JDBC**

    ---

    Connect relational databases using JDBC connectors like PostgreSQL, Snowflake, Oracle, and more.

    [:octicons-arrow-right-24: Understanding JDBC](add-datastores/overview-of-a-jdbc-datastore.md)

-   :material-file-marker-outline:{ .lg .middle } **DFS**

    ---

    Connect distributed file systems like Amazon S3, Azure Data Lake Storage, and Google Cloud Storage.

    [:octicons-arrow-right-24: Understanding DFS](add-datastores/overview-of-a-dfs-datastore.md)

-   :material-connection:{ .lg .middle } **Connection**

    ---

    Set up new connections or reuse existing credentials to connect your datastores.

    [:octicons-arrow-right-24: Connections Overview](add-datastores/connections/overview-of-a-connection.md)

-   :material-vector-combine:{ .lg .middle } **Multiple-Schema**

    ---

    Discover and onboard multiple schemas from a single connection in one step.

    [:octicons-arrow-right-24: Multiple-Schema](add-datastores/multi-schema/overview.md)

-   :material-cog-outline:{ .lg .middle } **Managing**

    ---

    Add, edit, and delete datastores using new or existing connections.

    [:octicons-arrow-right-24: Managing Datastores](add-datastores/connections/new-connection.md)

</div>

## Operations

Run sync, profile, and scan operations to catalog your data, infer quality checks, and detect anomalies across your datastores.

<div class="grid cards" markdown>

-   :material-database-sync-outline:{ .lg .middle } **Sync**

    ---

    Detect new, changed, or removed containers and fields in the source datastore.

    [:octicons-arrow-right-24: Sync](operations/sync.md)

-   :material-database-eye-outline:{ .lg .middle } **Profile**

    ---

    Analyze records to assess data quality, generate metadata, and infer quality checks.

    [:octicons-arrow-right-24: Profile](operations/profile.md)

-   :material-database-search-outline:{ .lg .middle } **Scan**

    ---

    Enforce data quality checks and identify anomalies at the record and schema levels.

    [:octicons-arrow-right-24: Scan](operations/scan.md)

-   :material-database-alert-outline:{ .lg .middle } **External Scan**

    ---

    Run scan operations using externally provided data files.

    [:octicons-arrow-right-24: External Scan](operations/external-scan.md)

</div>

## Enrichment Datastore

Link an enrichment datastore to persist scan results, anomalies, and remediation data for full data quality visibility.

<div class="grid cards" markdown>

-   :material-database-import-outline:{ .lg .middle } **Getting Started**

    ---

    Get started with enrichment datastores and understand their role in data quality.

    [:octicons-arrow-right-24: Getting Started](enrichment-datastore/getting-started.md)

-   :material-book-open-outline:{ .lg .middle } **Introduction**

    ---

    Learn how to link an enrichment datastore to a source datastore.

    [:octicons-arrow-right-24: Introduction](enrichment-datastore/introduction.md)

-   :material-shield-lock-outline:{ .lg .middle } **Permissions**

    ---

    Understand the roles and permissions required for enrichment datastores.

    [:octicons-arrow-right-24: Permissions](enrichment-datastore/permissions.md)

-   :material-link-variant:{ .lg .middle } **Link**

    ---

    Link a source datastore to an enrichment datastore.

    [:octicons-arrow-right-24: Link](managing-datastores/link-enrichment.md)

-   :material-link-variant-off:{ .lg .middle } **Unlink**

    ---

    Remove the link between a source datastore and its enrichment datastore.

    [:octicons-arrow-right-24: Unlink](managing-datastores/unlink-enrichment.md)

-   :material-api:{ .lg .middle } **API**

    ---

    API endpoints for enrichment datastore operations.

    [:octicons-arrow-right-24: API](enrichment-datastore/api.md)

-   :material-help-circle-outline:{ .lg .middle } **FAQ**

    ---

    Answers to common questions about enrichment datastores.

    [:octicons-arrow-right-24: FAQ](enrichment-datastore/faq.md)

</div>

## Data Quality Score

Configure quality score settings, decay periods, and factor weights to measure and track the health of your data.

<div class="grid cards" markdown>

-   :material-bullseye:{ .lg .middle } **Getting Started**

    ---

    Get started with data quality scores and understand how they are calculated.

    [:octicons-arrow-right-24: Getting Started](data-quality-score/getting-started.md)

-   :material-book-open-outline:{ .lg .middle } **Introduction**

    ---

    Understand the concepts behind data quality scoring in Qualytics.

    [:octicons-arrow-right-24: Introduction](data-quality-score/introduction.md)

-   :material-shield-lock-outline:{ .lg .middle } **Permissions**

    ---

    Understand the roles and permissions required for quality score settings.

    [:octicons-arrow-right-24: Permissions](data-quality-score/permissions.md)

-   :material-cog-outline:{ .lg .middle } **Settings**

    ---

    Configure decay periods, factor weights, and scoring thresholds.

    [:octicons-arrow-right-24: Settings](managing-datastores/quality-score-settings.md)

-   :material-api:{ .lg .middle } **API**

    ---

    API endpoints for data quality score operations.

    [:octicons-arrow-right-24: API](data-quality-score/api.md)

-   :material-help-circle-outline:{ .lg .middle } **FAQ**

    ---

    Answers to common questions about data quality scores.

    [:octicons-arrow-right-24: FAQ](data-quality-score/faq.md)

</div>

## Grouping

Organize your datastores into custom groups by environment, team, domain, or priority for easier navigation and management.

<div class="grid cards" markdown>

-   :material-bookmark-box-outline:{ .lg .middle } **Getting Started**

    ---

    Get started with datastore grouping and understand how groups work.

    [:octicons-arrow-right-24: Getting Started](managing-datastores/grouping/overview.md)

-   :material-book-open-outline:{ .lg .middle } **Introduction**

    ---

    Understand the concepts behind datastore grouping in Qualytics.

    [:octicons-arrow-right-24: Introduction](managing-datastores/grouping/concepts/understanding-grouping.md)

-   :material-shield-lock-outline:{ .lg .middle } **Permissions**

    ---

    Understand the roles and permissions required for group management.

    [:octicons-arrow-right-24: Permissions](managing-datastores/grouping/concepts/permissions.md)

-   :material-bookmark-plus-outline:{ .lg .middle } **Create a Group**

    ---

    Create a new datastore group.

    [:octicons-arrow-right-24: Create](managing-datastores/grouping/managing-groups/create-a-group.md)

-   :material-pencil-outline:{ .lg .middle } **Edit a Group**

    ---

    Modify an existing datastore group.

    [:octicons-arrow-right-24: Edit](managing-datastores/grouping/managing-groups/edit-a-group.md)

-   :material-trash-can-outline:{ .lg .middle } **Delete a Group**

    ---

    Remove a datastore group.

    [:octicons-arrow-right-24: Delete](managing-datastores/grouping/managing-groups/delete-a-group.md)

-   :material-bookmark-check-outline:{ .lg .middle } **Assign a Group**

    ---

    Assign a datastore to a group.

    [:octicons-arrow-right-24: Assign](managing-datastores/grouping/managing-groups/assign-a-datastore.md)

-   :material-bookmark-remove-outline:{ .lg .middle } **Unassign a Group**

    ---

    Remove a datastore from a group.

    [:octicons-arrow-right-24: Unassign](managing-datastores/grouping/managing-groups/remove-a-datastore.md)

-   :material-api:{ .lg .middle } **API**

    ---

    API endpoints for datastore grouping operations.

    [:octicons-arrow-right-24: API](managing-datastores/grouping/concepts/grouping-api.md)

-   :material-help-circle-outline:{ .lg .middle } **FAQ**

    ---

    Answers to common questions about datastore grouping.

    [:octicons-arrow-right-24: FAQ](managing-datastores/grouping/concepts/grouping-faq.md)

</div>

## Tags

Assign tags to datastores and use them to filter operations, organize resources, and streamline workflows.

<div class="grid cards" markdown>

-   :material-tag-outline:{ .lg .middle } **Getting Started**

    ---

    Get started with tags and understand how they work in Qualytics.

    [:octicons-arrow-right-24: Getting Started](tags/getting-started.md)

-   :material-book-open-outline:{ .lg .middle } **Introduction**

    ---

    Understand the concepts behind tagging in Qualytics.

    [:octicons-arrow-right-24: Introduction](tags/introduction.md)

-   :material-shield-lock-outline:{ .lg .middle } **Permissions**

    ---

    Understand the roles and permissions required for tag management.

    [:octicons-arrow-right-24: Permissions](tags/permissions.md)

-   :material-tag-plus:{ .lg .middle } **Assign a Tag**

    ---

    Assign a tag to a datastore.

    [:octicons-arrow-right-24: Assign](tags/assign-tags.md)

-   :material-tag-off-outline:{ .lg .middle } **Unassign a Tag**

    ---

    Remove a tag from a datastore.

    [:octicons-arrow-right-24: Unassign](tags/unassign-tags.md)

-   :material-api:{ .lg .middle } **API**

    ---

    API endpoints for tag operations.

    [:octicons-arrow-right-24: API](tags/api.md)

-   :material-help-circle-outline:{ .lg .middle } **FAQ**

    ---

    Answers to common questions about tags.

    [:octicons-arrow-right-24: FAQ](tags/faq.md)

</div>
