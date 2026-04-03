# Source Datastores Overview

Source Datastores are the foundation of data quality management in Qualytics. A source datastore represents a connection to your data — whether it's a relational database (JDBC), a distributed file system (DFS), or a cloud storage service.

In this section you will find:

- **Datastore** — Learn the fundamentals (JDBC and DFS), set up connections, browse supported connectors, use multi-schema creation, and add, edit, or delete datastores.
- **Operations** — Run Sync, Profile, Scan, and External Scan operations to catalog your data, infer quality checks, and detect anomalies.
- **Enrichment Datastore** — Link an enrichment datastore to persist scan results, anomalies, source record examples, and remediation data to your own infrastructure.
- **Data Quality Score** — Configure scoring weights, decay periods, and thresholds to measure and track the health of your data over time.
- **Grouping** — Organize datastores into custom groups by environment, team, domain, or priority for easier navigation in the tree view.
- **Tags** — Assign tags to datastores to categorize, filter operations by tag, and influence quality score weighting.
- **Tips & Tricks** — Discover right-click options and keyboard shortcuts to navigate and manage datastores faster.

---

## Datastore

### Understanding

<div class="grid cards" markdown>

-   :material-database-outline:{ .lg .middle } **Getting Started**

    ---

    Understand what a datastore is, the architecture behind it, and how to get started.

    [:octicons-arrow-right-24: Getting Started](add-datastores/overview-of-a-datastore.md)

-   :material-table:{ .lg .middle } **JDBC**

    ---

    Connect relational databases using JDBC connectors like PostgreSQL, Snowflake, Oracle, and more.

    [:octicons-arrow-right-24: Understanding JDBC](add-datastores/overview-of-a-jdbc-datastore.md)

-   :material-file-outline:{ .lg .middle } **DFS**

    ---

    Connect distributed file systems like Amazon S3, Azure Data Lake Storage, and Google Cloud Storage.

    [:octicons-arrow-right-24: Understanding DFS](add-datastores/overview-of-a-dfs-datastore.md)

</div>

### Connections

<div class="grid cards" markdown>

-   :material-connection:{ .lg .middle } **Connection Introduction**

    ---

    Learn what connections are, their role in datastore setup, and key concepts.

    [:octicons-arrow-right-24: Introduction](add-datastores/connections/introduction.md)

-   :material-cog-transfer-outline:{ .lg .middle } **How Connections Work**

    ---

    Connection lifecycle, authentication methods, secrets management, and network requirements.

    [:octicons-arrow-right-24: How It Works](add-datastores/connections/how-it-works.md)

-   :material-format-list-checks:{ .lg .middle } **Available Connectors**

    ---

    Browse the full list of supported JDBC and DFS connectors.

    [:octicons-arrow-right-24: View Connectors](add-datastores/available-datastore-connectors.md)

</div>

### Multiple-Schema

<div class="grid cards" markdown>

-   :material-layers-outline:{ .lg .middle } **Multiple-Schema Introduction**

    ---

    Discover and onboard multiple schemas from a single connection in one step.

    [:octicons-arrow-right-24: Introduction](add-datastores/multi-schema/overview.md)

-   :material-sitemap-outline:{ .lg .middle } **How Multi-Schema Works**

    ---

    Schema discovery flow, name templates, catalog/schema hierarchy, and validation.

    [:octicons-arrow-right-24: How It Works](add-datastores/multi-schema/how-it-works.md)

-   :material-database-check-outline:{ .lg .middle } **Supported Connectors (Multi-Schema)**

    ---

    Which connectors support multi-schema discovery and their catalog/schema mappings.

    [:octicons-arrow-right-24: Supported Connectors](add-datastores/multi-schema/supported-connectors.md)

-   :material-shield-lock-outline:{ .lg .middle } **Multi-Schema Permissions**

    ---

    Roles and team permissions required for multi-schema creation and validation.

    [:octicons-arrow-right-24: Permissions](add-datastores/multi-schema/permissions.md)

-   :material-help-circle-outline:{ .lg .middle } **Multi-Schema FAQ**

    ---

    Connectors, enrichment linking, naming, batch limits, and troubleshooting.

    [:octicons-arrow-right-24: FAQ](add-datastores/multi-schema/faq.md)

</div>

### Managing

<div class="grid cards" markdown>

-   :material-plus-circle:{ .lg .middle } **Add with New Connection**

    ---

    Create a new source datastore by setting up a new connection from scratch.

    [:octicons-arrow-right-24: New Connection](add-datastores/connections/new-connection.md)

-   :material-link-variant:{ .lg .middle } **Add with Existing Connection**

    ---

    Create a new source datastore by reusing credentials from an existing connection.

    [:octicons-arrow-right-24: Existing Connection](add-datastores/connections/existing-connection.md)

-   :material-pencil-outline:{ .lg .middle } **Edit Datastore**

    ---

    Modify your datastore's connection scope, teams, or other properties.

    [:octicons-arrow-right-24: Edit](managing-datastores/edit-datastore.md)

-   :material-trash-can-outline:{ .lg .middle } **Delete Datastore**

    ---

    Permanently remove a datastore and all its associated data.

    [:octicons-arrow-right-24: Delete](managing-datastores/delete-datastore.md)

-   :material-api:{ .lg .middle } **Datastore API**

    ---

    Create, update, delete, bulk create, link enrichment, and manage datastores programmatically.

    [:octicons-arrow-right-24: API](add-datastores/api.md)

-   :material-help-circle-outline:{ .lg .middle } **Datastore FAQ**

    ---

    Connections, creating, managing, enrichment, operations, and troubleshooting.

    [:octicons-arrow-right-24: FAQ](add-datastores/faq.md)

</div>

---

## Operations

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

---

## Enrichment Datastore

<div class="grid cards" markdown>

-   :material-database-import-outline:{ .lg .middle } **Getting Started**

    ---

    Overview of enrichment datastores, supported connectors, and all managing pages.

    [:octicons-arrow-right-24: Getting Started](enrichment-datastore/getting-started.md)

-   :material-book-open-outline:{ .lg .middle } **Introduction**

    ---

    How enrichment works, settings, remediation strategies, side effects, and sharing.

    [:octicons-arrow-right-24: Introduction](enrichment-datastore/introduction.md)

-   :material-shield-lock-outline:{ .lg .middle } **Permissions**

    ---

    Roles and team permissions for linking, unlinking, and configuring enrichment.

    [:octicons-arrow-right-24: Permissions](enrichment-datastore/permissions.md)

-   :material-link-variant:{ .lg .middle } **Link Enrichment Datastore**

    ---

    Link a source datastore to an enrichment datastore through the Settings menu or tree footer.

    [:octicons-arrow-right-24: Link](managing-datastores/link-enrichment.md)

-   :material-link-plus:{ .lg .middle } **Link on Datastore Creation**

    ---

    Link an enrichment datastore during the datastore creation wizard.

    [:octicons-arrow-right-24: Link on Creation](enrichment-datastore/link-during-creation.md)

-   :material-link-variant-off:{ .lg .middle } **Unlink Enrichment Datastore**

    ---

    Remove the enrichment link from a source datastore.

    [:octicons-arrow-right-24: Unlink](managing-datastores/unlink-enrichment.md)

-   :material-view-list:{ .lg .middle } **Supported Enrichment Datastores**

    ---

    Which connectors support enrichment and their write-back capabilities.

    [:octicons-arrow-right-24: Supported Connectors](enrichment-support/supported-enrichment-datastores.md)

-   :material-api:{ .lg .middle } **Enrichment API**

    ---

    Link, unlink, and update enrichment settings programmatically.

    [:octicons-arrow-right-24: API](enrichment-datastore/api.md)

-   :material-help-circle-outline:{ .lg .middle } **Enrichment FAQ**

    ---

    Remediation strategies, prefix conflicts, storage, re-linking, and troubleshooting.

    [:octicons-arrow-right-24: FAQ](enrichment-datastore/faq.md)

</div>

---

## Data Quality Score

<div class="grid cards" markdown>

-   :material-bullseye:{ .lg .middle } **Getting Started**

    ---

    Overview of quality scores, dimensions, settings, weighting, and all managing pages.

    [:octicons-arrow-right-24: Getting Started](data-quality-score/getting-started.md)

-   :material-book-open-outline:{ .lg .middle } **Introduction**

    ---

    Score hierarchy, the 8 dimensions, decay period, weights, independent settings, and recalculations.

    [:octicons-arrow-right-24: Introduction](data-quality-score/introduction.md)

-   :material-shield-lock-outline:{ .lg .middle } **Permissions**

    ---

    Roles and team permissions for viewing scores and editing settings.

    [:octicons-arrow-right-24: Permissions](data-quality-score/permissions.md)

-   :material-tune:{ .lg .middle } **Settings**

    ---

    Configure decay period and dimension weights for your datastore.

    [:octicons-arrow-right-24: Settings](managing-datastores/quality-score-settings.md)

-   :material-api:{ .lg .middle } **Quality Score API**

    ---

    Retrieve and update score settings and access historical score snapshots.

    [:octicons-arrow-right-24: API](data-quality-score/api.md)

-   :material-help-circle-outline:{ .lg .middle } **Quality Score FAQ**

    ---

    Baseline, dimensions, decay, independent settings, troubleshooting, and more.

    [:octicons-arrow-right-24: FAQ](data-quality-score/faq.md)

</div>

---

## Grouping

<div class="grid cards" markdown>

-   :material-bookmark-box-outline:{ .lg .middle } **Getting Started**

    ---

    Overview of datastore grouping, permissions, and all managing pages.

    [:octicons-arrow-right-24: Getting Started](managing-datastores/grouping/overview.md)

-   :material-book-open-outline:{ .lg .middle } **Introduction**

    ---

    How groups work, key characteristics, favorites interaction, and best practices.

    [:octicons-arrow-right-24: Introduction](managing-datastores/grouping/concepts/understanding-grouping.md)

-   :material-shield-lock-outline:{ .lg .middle } **Permissions**

    ---

    Two permission layers for group management and datastore assignment.

    [:octicons-arrow-right-24: Permissions](managing-datastores/grouping/concepts/permissions.md)

-   :material-plus-circle:{ .lg .middle } **Create a Group**

    ---

    Create a new datastore group with a custom name and icon.

    [:octicons-arrow-right-24: Create](managing-datastores/grouping/managing-groups/create-a-group.md)

-   :material-pencil-outline:{ .lg .middle } **Edit a Group**

    ---

    Rename a group or change its icon.

    [:octicons-arrow-right-24: Edit](managing-datastores/grouping/managing-groups/edit-a-group.md)

-   :material-trash-can-outline:{ .lg .middle } **Delete a Group**

    ---

    Remove a group — datastores in the group become ungrouped.

    [:octicons-arrow-right-24: Delete](managing-datastores/grouping/managing-groups/delete-a-group.md)

-   :material-bookmark-check-outline:{ .lg .middle } **Assign a Datastore to a Group**

    ---

    Assign a datastore to an existing group from the tree view.

    [:octicons-arrow-right-24: Assign to Group](managing-datastores/grouping/managing-groups/assign-a-datastore.md)

-   :material-bookmark-remove-outline:{ .lg .middle } **Unassign a Datastore from a Group**

    ---

    Unassign a datastore from its current group. The datastore moves to Ungrouped.

    [:octicons-arrow-right-24: Unassign](managing-datastores/grouping/managing-groups/unassign-a-datastore.md)

-   :material-filter-outline:{ .lg .middle } **Filter by Group**

    ---

    Filter the Source Datastores listing page to show only datastores in specific groups.

    [:octicons-arrow-right-24: Filter by Group](managing-datastores/grouping/managing-groups/filter-by-group.md)

-   :material-api:{ .lg .middle } **Grouping API**

    ---

    Create, update, delete groups and assign/unassign datastores programmatically.

    [:octicons-arrow-right-24: API](managing-datastores/grouping/concepts/grouping-api.md)

-   :material-help-circle-outline:{ .lg .middle } **Grouping FAQ**

    ---

    Groups vs tags, favorites, permissions, limits, filter behavior, and more.

    [:octicons-arrow-right-24: FAQ](managing-datastores/grouping/concepts/grouping-faq.md)

</div>

---

## Tags

<div class="grid cards" markdown>

-   :material-tag-outline:{ .lg .middle } **Getting Started**

    ---

    Overview of datastore tags, permissions, and all managing pages.

    [:octicons-arrow-right-24: Getting Started](tags/getting-started.md)

-   :material-book-open-outline:{ .lg .middle } **Introduction**

    ---

    Tag inheritance, operation filtering, quality score impact, and weight modifiers.

    [:octicons-arrow-right-24: Introduction](tags/introduction.md)

-   :material-shield-lock-outline:{ .lg .middle } **Permissions**

    ---

    Roles and team permissions for viewing, assigning, and unassigning tags.

    [:octicons-arrow-right-24: Permissions](tags/permissions.md)

-   :material-tag-plus:{ .lg .middle } **Assign a Tag**

    ---

    Assign an existing tag to a source datastore from the tree view footer.

    [:octicons-arrow-right-24: Assign](tags/assign-tags.md)

-   :material-tag-off-outline:{ .lg .middle } **Unassign a Tag**

    ---

    Remove a tag from a source datastore without deleting the tag itself.

    [:octicons-arrow-right-24: Unassign](tags/unassign-tags.md)

-   :material-api:{ .lg .middle } **Tags API**

    ---

    Assign, unassign, and query tags on datastores via the datastore update endpoint.

    [:octicons-arrow-right-24: API](tags/api.md)

-   :material-help-circle-outline:{ .lg .middle } **Tags FAQ**

    ---

    Inheritance, permissions, weight modifiers, storage, re-linking, and troubleshooting.

    [:octicons-arrow-right-24: FAQ](tags/faq.md)

</div>

---

## Tips & Tricks

<div class="grid cards" markdown>

-   :material-mouse:{ .lg .middle } **Right Click Options**

    ---

    Quick actions available via right-click on datastores in the tree view, listing, and breadcrumb.

    [:octicons-arrow-right-24: Right Click Options](tips-and-tricks/right-click-options.md)

-   :material-keyboard:{ .lg .middle } **Keyboard Shortcuts**

    ---

    Speed up common datastore actions with keyboard shortcuts and the Command Bar.

    [:octicons-arrow-right-24: Keyboard Shortcuts](tips-and-tricks/keyboard-shortcuts.md)

</div>
