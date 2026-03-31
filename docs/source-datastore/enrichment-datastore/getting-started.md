# Getting Started with Datastore Enrichment

An enrichment datastore is a dedicated datastore linked to a source datastore that persists scan results, anomalies, remediation data, and source record examples. It provides full visibility into your data quality by writing findings directly to your own infrastructure — making them queryable, auditable, and available for downstream workflows.

In this section you will find everything about managing enrichment datastores in the context of source datastores — from understanding how they work, to linking and unlinking, permissions, API reference, and frequently asked questions.

## Deep Dive

Understand how enrichment datastores work when linked to a source datastore, and the permissions required to manage them.

<div class="grid cards" markdown>

-   :material-book-open-outline:{ .lg .middle } **Introduction**

    ---

    Learn how enrichment datastores work with source datastores, enrichment settings, remediation strategies, and sharing.

    [:octicons-arrow-right-24: Introduction](introduction.md)

-   :material-shield-lock-outline:{ .lg .middle } **Permissions**

    ---

    See which roles can view, link, unlink, create, edit, and delete enrichment datastores.

    [:octicons-arrow-right-24: Permissions](permissions.md)

</div>

## Managing

Link, unlink, or configure enrichment datastores on your source datastores.

<div class="grid cards" markdown>

-   :material-link-variant:{ .lg .middle } **Link Enrichment Datastore**

    ---

    Link an existing enrichment datastore to a source datastore that has already been created.

    [:octicons-arrow-right-24: Link](../managing-datastores/link-enrichment.md)

-   :material-link-variant-off:{ .lg .middle } **Unlink Enrichment Datastore**

    ---

    Remove the enrichment link from a source datastore.

    [:octicons-arrow-right-24: Unlink](../managing-datastores/unlink-enrichment.md)

-   :material-database-import-outline:{ .lg .middle } **Link on Datastore Creation**

    ---

    Link an enrichment datastore during the source datastore creation wizard.

    [:octicons-arrow-right-24: Link on Creation](link-during-creation.md)

</div>

## Resources

<div class="grid cards" markdown>

-   :material-api:{ .lg .middle } **API**

    ---

    API endpoints for enrichment datastore operations.

    [:octicons-arrow-right-24: API](api.md)

-   :material-help-circle-outline:{ .lg .middle } **FAQ**

    ---

    Answers to common questions about enrichment datastores.

    [:octicons-arrow-right-24: FAQ](faq.md)

</div>
