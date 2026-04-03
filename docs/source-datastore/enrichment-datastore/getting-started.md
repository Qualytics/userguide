# Getting Started with Datastore Enrichment

An enrichment datastore is a dedicated datastore linked to a source datastore that persists scan results, anomalies, remediation data, and source record examples. It provides full visibility into your data quality by writing findings directly to your own infrastructure — making them queryable, auditable, and available for downstream workflows.

In this section you will learn how enrichment datastores work in the context of source datastores, how to link and configure them, and how to manage enrichment settings. Linking requires the **Member** user role and **Editor** team permission; unlinking requires the **Admin** role.

<div class="grid cards" markdown>

-   :material-book-open-outline:{ .lg .middle } **Introduction**

    ---

    Learn how enrichment datastores work with source datastores, enrichment settings, remediation strategies, and sharing.

    [:octicons-arrow-right-24: Introduction](introduction.md)

-   :material-shield-lock-outline:{ .lg .middle } **Permissions**

    ---

    See which roles can view, link, unlink, and configure enrichment datastores.

    [:octicons-arrow-right-24: Permissions](permissions.md)

-   :material-link-variant:{ .lg .middle } **Link Enrichment Datastore**

    ---

    Link an existing enrichment datastore to a source datastore that has already been created.

    [:octicons-arrow-right-24: Link](../managing-datastores/link-enrichment.md)

-   :material-link-plus:{ .lg .middle } **Link on Datastore Creation**

    ---

    Link an enrichment datastore during the source datastore creation wizard.

    [:octicons-arrow-right-24: Link on Creation](link-during-creation.md)

-   :material-link-variant-off:{ .lg .middle } **Unlink Enrichment Datastore**

    ---

    Remove the enrichment link from a source datastore.

    [:octicons-arrow-right-24: Unlink](../managing-datastores/unlink-enrichment.md)

-   :material-view-list:{ .lg .middle } **Supported Enrichment Datastores**

    ---

    See which connectors support enrichment and their write-back capabilities.

    [:octicons-arrow-right-24: Supported Connectors](../../enrichment-support/supported-enrichment-datastores.md)

-   :material-api:{ .lg .middle } **API**

    ---

    Link, unlink, and update enrichment settings programmatically.

    [:octicons-arrow-right-24: API](api.md)

-   :material-help-circle-outline:{ .lg .middle } **FAQ**

    ---

    Remediation strategies, prefix conflicts, storage impact, Scan behavior, re-linking, and troubleshooting.

    [:octicons-arrow-right-24: FAQ](faq.md)

</div>
