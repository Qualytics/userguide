# Datastore FAQ

Answers to frequently asked questions about source datastores in Qualytics.

## General

### What is a source datastore?

A source datastore is a connection to your data infrastructure (database, warehouse, or file storage) that Qualytics monitors for data quality. It represents a specific scope within a system — for example, a database + schema for JDBC or a root path for DFS.

### What is the difference between JDBC and DFS datastores?

| | JDBC | DFS |
| :--- | :--- | :--- |
| **Data sources** | Relational databases and SQL-based warehouses | Cloud object storage and distributed file systems |
| **Data model** | Tables and views | Files and file patterns |
| **Scope** | Database + Schema | Root path |
| **Examples** | PostgreSQL, Snowflake, BigQuery, MySQL, Oracle | Amazon S3, Azure Data Lake Storage, Google Cloud Storage |

### What connectors are supported?

**JDBC** (19 connectors): Athena, BigQuery, Databricks, DB2, Dremio, Fabric, Hive, MariaDB, MySQL, Oracle, PostgreSQL, Presto, Redshift, Snowflake, SQL Server, Synapse, Teradata, TimescaleDB, Trino.

**DFS** (3 connectors): Amazon S3, Azure Data Lake Storage (ABFS), Google Cloud Storage.

**Native** (1 connector): Databricks Unity Catalog.

### Is there a limit on the number of datastores I can create?

There is no programmatic limit on the number of datastores. You can create as many as your deployment supports.

### What file formats does DFS support?

DFS datastores support **Parquet**, **CSV**, **JSON**, **ORC**, and **Avro** file formats. CSV files support configurable options such as header detection, escape characters, and empty-as-null treatment.

---

## Connections

### Can multiple datastores share the same connection?

Yes. A connection stores credentials and endpoint information, while a datastore represents a specific data scope. One Snowflake connection (host, role, warehouse, credentials) can serve multiple datastores — each pointing to a different schema (e.g., `production.public`, `production.sales`, `production.finance`).

### Can I change the connection of an existing datastore?

Yes, but the new connection must be the **same connector type** as the current one. For example, you can switch a PostgreSQL datastore from one PostgreSQL connection to another, but you cannot change it to a Snowflake connection. Changing the connection triggers a re-verification of the datastore.

### What happens if the connection credentials change?

When connection credentials (password, access keys) are updated, all datastores using that connection are re-verified against the dataplane. If the new credentials are valid, all associated datastores continue working normally. If the credentials are invalid, the datastores are marked as disconnected until the issue is resolved.

### Can I use secrets management (HashiCorp Vault) with any connector?

Yes. Secrets management is available for all connector types. You can use `${key}` syntax in any connection property to reference secrets from your vault. Secrets are retrieved dynamically each time the connection is used, so password rotations in your vault are automatically picked up.

---

## Creating Datastores

### What does the "Initiate Sync" checkbox do?

When enabled, a sync operation is automatically triggered after the datastore is created. The sync detects all containers (tables, views, or file patterns) in the datastore. If disabled, you will need to manually trigger a sync operation before profiling or scanning.

### Can I create multiple datastores at once?

Yes. The [Multi-Schema Creation](multi-schema/overview.md){:target="_blank"} feature allows you to select multiple schemas from a single connection and create a datastore for each one in a single operation. This is also available via the [Datastore API](api.md#multi-schema-creation){:target="_blank"} for automation.

### What is the Name Template in multi-schema creation?

The Name Template defines the naming pattern for each datastore created in a multi-schema flow. Use `{{schema}}` as a placeholder that gets replaced with the actual schema name. For example, `prod_{{schema}}` produces `prod_public`, `prod_sales`, `prod_finance`.

### Can I duplicate a datastore?

There is no built-in duplication feature. To create a similar datastore, use the same connection and configure the new datastore with the desired properties. For bulk creation, use the [Multi-Schema Creation](multi-schema/overview.md){:target="_blank"} feature or the [Datastore API](api.md#create-a-datastore){:target="_blank"}.

---

## Managing Datastores

### Can I rename a datastore?

Yes. You can rename a datastore through the [Edit Datastore](../../source-datastore/managing-datastores/edit-datastore.md){:target="_blank"} option in the Settings menu or via the [API](api.md#update-a-datastore){:target="_blank"}. Datastore names must be unique within the workspace (max 255 characters).

### Can I move a datastore between teams?

Yes. You can reassign teams through the update endpoint or the Edit Datastore settings. Changing teams requires at least the **Editor** permission on the datastore. Note that updating teams **replaces** the entire team list — include all desired teams in the update.

### What happens when I delete a datastore?

Deletion is **permanent and cascading**:

- All containers (tables, views, file patterns) are deleted.
- All quality checks associated with the datastore are removed.
- All anomalies and scan results are permanently deleted.
- All scheduled operations are cancelled.
- If the datastore has an enrichment link, the link is removed (but the enrichment datastore itself is not deleted).

!!! warning
    Deletion is blocked if the datastore has active flows or if its containers are referenced by computed join containers from other datastores.

### What permissions are needed to manage datastores?

| Action | Minimum Permission |
| :--- | :--- |
| View datastores | Member |
| Create a datastore | Manager |
| Edit a datastore | Editor |
| Delete a datastore | Admin |
| Assign tags | Editor |
| Assign teams | Editor |
| Toggle favorite | Member |
| Link enrichment | Member |
| Unlink enrichment | Admin |

---

## Enrichment

### Can I use a datastore without linking an enrichment datastore?

Yes. Enrichment is optional. Without an enrichment datastore linked, Qualytics still tracks anomalies and checks internally. However, scan results, source record examples, and remediation data will **not** be persisted to your own infrastructure — they will only be available within the Qualytics platform.

### Can I link enrichment after creating the datastore?

Yes. You can link an enrichment datastore at any time through the [Link Enrichment Datastore](../../source-datastore/managing-datastores/link-enrichment.md){:target="_blank"} flow or via the [API](api.md#link-enrichment-datastore){:target="_blank"}.

### What connectors support enrichment?

Not all connectors can be used as enrichment datastores. For the full list of supported enrichment connectors, see the [Supported Enrichment Datastores](../../enrichment-support/supported-enrichment-datastores.md){:target="_blank"} page.

---

## Operations

### What is the correct order of operations?

The recommended order is **Sync → Profile → Scan**:

1. **Sync** detects containers (tables, views, files) in the datastore.
2. **Profile** analyzes the data to generate metadata and infer quality checks.
3. **Scan** executes the quality checks and identifies anomalies.

### What happens if a sync operation fails?

Containers are assigned a status based on the sync result:

| Status | Description |
| :--- | :--- |
| **Available** | Container was found and successfully analyzed. |
| **Changed** | Container fields changed since the last sync — re-profile recommended. |
| **Inaccessible** | Container was not found — it may have been removed or the credentials lack permission. |
| **Unloadable** | Container appears in the listing but could not be analyzed (e.g., corrupt data, unsupported format). |

### Can I run operations on specific tables only?

Yes. When initiating a Profile or Scan operation, you can select **All**, **Specific** tables/file patterns, or filter by **Tag**. This allows you to target specific datasets without scanning the entire datastore.

---

## Troubleshooting

### My datastore shows as "disconnected". What should I do?

A disconnected status means the credentials could not be verified. Common causes:

1. **Credentials expired or rotated** — Update the connection credentials.
2. **Network issue** — Verify that the Qualytics deployment can reach the datastore host.
3. **Permission revoked** — Ensure the database user has the required permissions.
4. **Host changed** — Update the connection host if the database endpoint changed.

Click **Test Connection** in the Edit Datastore modal to diagnose the issue.

### I can't delete my datastore. Why?

Deletion is blocked in the following scenarios:

- The datastore has **active flows** referencing it.
- The datastore's containers are used in **computed join containers** from other datastores.
- If the datastore is an enrichment-only datastore, it may be linked to **export or materialize operations** in active flows.

Resolve the dependencies before attempting to delete.

### My sync operation is not finding all tables. What should I check?

- Verify that the database user has `SELECT` permission on the missing tables.
- For JDBC: Check that the **Database** and **Schema** fields are correctly configured.
- For DFS: Check that the **Root Path** is correct and the access credentials have `LIST` permission on the path.
- Some views or temporary tables may not be included by default — check the sync **Include** settings (Tables, Views).
