# Multi-Schema Creation FAQ

## General

### What is multi-schema source datastore creation?

It is a feature that allows you to discover and select multiple schemas from a single connection and create all corresponding source datastores in one step, instead of adding each schema individually.

### Which connectors support multi-schema creation?

All JDBC-based connectors support multi-schema creation. DFS-based datastores (Amazon S3, Azure Datalake Storage, Google Cloud Storage) do not support it because they do not use a catalog/schema hierarchy. See the full list in [Supported Connectors](supported-connectors.md).

### Can I use multi-schema creation with an existing connection?

Yes. You can either create a new connection or reuse an existing one. When using an existing connection, you can only configure the datastore-specific properties (catalog, schemas, name template, teams, group, and initiate sync).

### Is there a limit on how many schemas I can select at once?

There is no hard limit on the number of schemas you can select for creation. However, the validation endpoint accepts a maximum of **50 schemas per request**. If you have more than 50 schemas, validate them in batches. The creation endpoint itself has no such limit.

### Can I edit the datastores created in bulk after creation?

Yes. Each datastore created through the multi-schema flow is a regular source datastore. You can edit, delete, or reconfigure them individually through the [Datastore Settings](../../../managing-datastores/settings-overview.md) just like any other datastore.

### Can I delete all datastores created in bulk at once?

No. There is no bulk delete option tied to the multi-schema creation. Each datastore must be deleted individually through the [Delete Datastore](../../../managing-datastores/delete-datastore.md) settings.

### Can I use multi-schema creation for enrichment datastores?

Yes. You can set `enrichment_only: true` in the bulk creation request to create enrichment datastores instead of source datastores. This is useful when you need to set up enrichment across multiple schemas from the same connection.

### A new schema was added to my database. How do I add it to Qualytics?

Run the multi-schema flow again using the same connection. The schema discovery will show all available schemas, including the new one. Schemas that already have a datastore will display a warning icon, so you can easily identify and select only the new schema.

Alternatively, you can use the [API](multi-schema-api.md) to discover and create the datastore for the new schema programmatically.

### How do I know which datastores were created by multi-schema vs. individually?

There is no visual indicator that distinguishes them. Once created, a datastore from multi-schema is identical to one created individually. If you need to track this, use a consistent naming convention through the name template (e.g., `batch_{{schema}}`) or apply a specific tag during creation.

## Permissions

### Who can use multi-schema creation?

Users with the **Manager** or **Admin** role can use multi-schema creation. This is the same permission required to create a single datastore.

### Are there different permissions for discovery, validation, and creation?

No. All operations in the multi-schema flow — catalog discovery, schema discovery, validation, and bulk creation — require the same **Manager** role.

!!! info "Full Permission Matrix"
    For a complete overview of all permissions across all features, see the [Team Permissions](../../../../settings/security/team-permissions.md) page.

### Can I assign different teams to different schemas?

No. In the multi-schema flow, all source datastores created in the batch are assigned to the same teams. If you need different team assignments, you can change them individually after creation through the [Edit Datastore](../../../managing-datastores/edit-datastore.md) settings.

## Schema Discovery

### How are schemas discovered?

When you provide connection credentials and select a catalog (if applicable), Qualytics queries the database's information schema to retrieve the list of available schemas. This happens in real-time during the creation flow.

### What does the warning icon next to a schema mean?

The warning icon indicates that the schema already has one or more existing datastores in Qualytics. A tooltip shows which datastores are associated. You can still select it, but this will create a duplicate datastore for that schema.

### Can I refresh the list of available schemas?

Yes. Click the **refresh** button next to the catalog or schema dropdown to re-query the connection and reload the available options.

### Why are some schemas missing from the list?

The schema discovery relies on the permissions of the database user configured in the connection. If a schema does not appear, the user may not have the necessary privileges (e.g., `USAGE` on the schema) to see it. Verify your database user's permissions with your DBA.

### Does discovery show system schemas (e.g., information_schema, pg_catalog)?

Yes — discovery returns all schemas visible to the database user, including system schemas. You can simply skip selecting them. Only the schemas you explicitly select will have datastores created.

## Name Templates

### What is a name template?

A name template is a naming pattern that uses the `{{schema}}` placeholder. When datastores are created, `{{schema}}` is replaced with the actual schema name. For example, `production_{{schema}}` with schema `public` becomes `production_public`.

### Is `{{schema}}` the only placeholder available?

Yes. Currently, `{{schema}}` is the only supported placeholder in the name template.

### Can I use the name template without the `{{schema}}` placeholder?

No. The `{{schema}}` placeholder is required to ensure each datastore gets a unique name. Without it, all datastores would have the same name.

### Can I preview the generated names before creating?

Yes. A preview is displayed below the name template field showing how the first few datastores will be named based on your selected schemas.

### What happens if the generated name conflicts with an existing datastore?

The creation will proceed and a new datastore with that name will be created. Qualytics does not enforce unique datastore names, but using distinct name templates helps avoid confusion.

### Can I rename a datastore after it was created by multi-schema?

Yes. You can rename any datastore through the [Edit Datastore](../../../managing-datastores/edit-datastore.md) settings, regardless of how it was created.

## Enrichment

### Is linking an enrichment datastore required?

No. The enrichment linking step is optional. You can click **Finish** after the source datastore configuration to skip it. However, linking an enrichment datastore is recommended for full data quality visibility.

### Can I link different enrichment datastores to different schemas?

No. In the multi-schema flow, all source datastores created in the batch are linked to the same enrichment datastore. If you need different enrichment datastores for different schemas, you can change the enrichment linking individually after creation through the [Link Enrichment](../../../managing-datastores/link-enrichment.md) settings.

### Can I change the enrichment datastore after creation?

Yes. You can unlink and relink a different enrichment datastore for any individual source datastore through the [Link Enrichment](../../../managing-datastores/link-enrichment.md) and [Unlink Enrichment](../../../managing-datastores/unlink-enrichment.md) settings.

### What is the enrichment prefix?

The prefix is a string prepended to table names when Qualytics writes metadata to the enrichment datastore. It helps uniquely identify which source datastore the enrichment data belongs to. It is auto-generated from the name template but can be customized.

### Is the enrichment prefix the same for all datastores created in the batch?

The prefix is auto-generated based on each datastore's name, so each datastore in the batch will have its own unique prefix derived from the name template and the schema name.

## Integration with Other Features

### Can I use multi-schema creation together with datastore grouping?

Yes. You can assign all newly created datastores to a [datastore group](../../../managing-datastores/grouping/overview.md) during the creation flow by selecting a group in the form. All datastores in the batch will be assigned to the same group.

### Can I add tags during multi-schema creation?

Yes, through the API. The bulk creation request accepts a `tags` field that applies the specified tags to all created datastores. The UI form does not currently include a tags field during creation, but you can add tags to individual datastores after creation.

### Do the created datastores automatically appear in my team's view?

Yes. The datastores are assigned to the teams you select during creation and will be visible to all users in those teams according to their permission level.

### Does multi-schema creation work with Secrets Management (HashiCorp Vault)?

Yes. If your connection uses Secrets Management, you can use `${key}` references in connection properties. The secrets are resolved dynamically each time the connection is used, including during schema discovery and datastore creation.

## Operations

### What happens when I enable "Initiate Sync"?

When enabled, a sync operation is automatically triggered on each newly created source datastore after creation. The sync operations run independently and detect containers and fields within each schema.

### Do all sync operations run at the same time?

The sync operations are triggered sequentially as each datastore is created, but they run independently and may execute in parallel depending on system capacity.

### Can I schedule operations in bulk for the datastores created?

There is no bulk scheduling option tied to multi-schema creation. Operations (sync, profile, scan) must be scheduled individually for each datastore. However, you can use the [API](multi-schema-api.md) to automate scheduling across multiple datastores programmatically.

## Performance

### Does multi-schema creation take longer with many schemas?

Yes. Each schema is validated and created individually within the bulk operation. More schemas means more validation and creation steps. For very large numbers of schemas (50+), consider breaking the operation into smaller batches.

### Is there a validation limit?

Yes. The validation endpoint accepts a maximum of **50 schemas per request**. If you need to validate more, split them into multiple validation requests. The creation endpoint itself has no such limit.

### Can I run multi-schema creation while other operations are running?

Yes. Multi-schema creation does not block other operations. However, if you enable "Initiate Sync", the sync operations that start after creation will compete for system resources with any other running operations.

## Errors and Troubleshooting

### What happens if some schemas fail validation?

The validation runs per-schema and reports individual results. You can review which schemas failed, fix the underlying issues (e.g., permissions), and retry. Only schemas that pass validation will be created.

### What happens if some schemas fail during creation?

The bulk creation operation is non-atomic — schemas that succeed are created, and schemas that fail are reported with error messages. You can retry the failed schemas individually or through a new multi-schema creation.

### How do I retry only the schemas that failed?

Run the multi-schema flow again (or use the API) with only the failed schema names. The previously created datastores will not be affected. See the [Handling Errors](multi-schema-api.md#handling-errors-and-retrying-failed-schemas) section in the API documentation for a practical example.

### I don't see the catalog/schema dropdowns. Why?

Make sure you have:

1. Selected a JDBC connector (DFS connectors do not support multi-schema).
2. Provided valid connection credentials.
3. Clicked **Test Connection** or waited for the catalog/schema discovery to complete.

If the connection credentials are invalid, the catalog and schema discovery will fail silently.

### The schema list is empty even though my database has schemas. What should I do?

This usually indicates a permissions issue. Verify that:

1. The database user has `USAGE` or equivalent privileges on the schemas.
2. The catalog (database) was correctly selected (for two-step connectors).
3. The connection credentials are valid — try clicking the **refresh** button to retry discovery.

### What happens to the datastores if the connection is deleted?

Deleting a connection does not delete the datastores that were created from it. The datastores will lose their connection reference and you will need to reconfigure a connection for them to remain operational.
