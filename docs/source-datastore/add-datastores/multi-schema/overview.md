# Getting Started with Multiple-Schema

Multi-Schema Creation allows you to discover and select multiple schemas from a single connection and create all corresponding source datastores in one step. Instead of adding each schema individually, you can onboard multiple schemas at once, streamlining the setup process for organizations with many schemas across their data platforms.

## Why Multi-Schema Creation Matters

As organizations scale their data infrastructure, databases often contain dozens or even hundreds of schemas. Onboarding each schema individually is time-consuming and error-prone. Multi-Schema Creation solves this by letting you:

- **Batch onboarding**: Create multiple source datastores from a single connection in one operation.
- **Schema discovery**: Automatically discover available catalogs and schemas from your connection.
- **Optional enrichment linking**: Link all newly created source datastores to a single enrichment datastore during the same flow.
- **Name templates**: Use a naming pattern with a `{{schema}}` placeholder to generate consistent datastore names.

!!! note "Permissions"
    Multi-schema creation requires the **Manager** or **Admin** role. This is the same permission required to create a single datastore. For more details, see the [Team Permissions](../../../settings/security/team-permissions.md) page.

## Getting Started

To create multi-schema datastores, use the **Add Source Datastore** flow. The multi-schema options will appear automatically when you select a supported JDBC connector.

<div class="grid cards" markdown>

-   :material-plus-circle:{ .lg .middle } **Add Datastore with a New Connection**

    ---

    Create multiple source datastores by setting up a new connection from scratch.

    [:octicons-arrow-right-24: Setup a Connection](../connections/new-connection.md)

-   :material-link-variant:{ .lg .middle } **Add Datastore with an Existing Connection**

    ---

    Create multiple source datastores by reusing credentials from a connection that already exists.

    [:octicons-arrow-right-24: Reuse a Connection](../connections/existing-connection.md)

</div>

## Deep Dive

<div class="grid cards" markdown>

-   :material-cog-outline:{ .lg .middle } **How It Works**

    ---

    Understand the multi-schema creation flow, schema discovery, and name templates.

    [:octicons-arrow-right-24: How It Works](concepts/how-it-works.md)

-   :material-database-outline:{ .lg .middle } **Supported Connectors**

    ---

    See which connectors support multi-schema discovery and their catalog/schema mappings.

    [:octicons-arrow-right-24: Supported Connectors](concepts/supported-connectors.md)

</div>

## Resources

<div class="grid cards" markdown>

-   :material-help-circle-outline:{ .lg .middle } **FAQ**

    ---

    Answers to common questions about multi-schema source datastore creation.

    [:octicons-arrow-right-24: FAQ](concepts/multi-schema-faq.md)

</div>
