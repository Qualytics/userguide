# Supported Connectors

Multi-schema discovery is available for JDBC-based connectors that support schema-level separation. DFS-based datastores (Amazon S3, Azure Datalake Storage, Google Cloud Storage) do not support multi-schema creation because they do not use a catalog/schema hierarchy.

## Connector Reference

The table below shows each supported connector, the field used for catalog selection (if any), and the field used as the schema target for multi-select.

| Connector | Catalog Field | Schema Field |
|-----------|--------------|--------------|
| [Athena](../athena.md) | Catalog | Schema |
| [BigQuery](../bigquery.md) | Project | Dataset |
| [Databricks](../databricks.md) | Catalog | Schema |
| [DB2](../db2.md) | — | Schema |
| [Dremio](../dremio.md) | — | Schema |
| [Fabric Analytics](../fabric-analytics.md) | Database | Schema |
| [Hive](../hive.md) | — | Database |
| [MariaDB](../maria-db.md) | — | Database |
| [Microsoft SQL Server](../microsoft-sql-server.md) | Database | Schema |
| [MySQL](../mysql.md) | — | Database |
| [Oracle](../oracle.md) | — | Schema |
| [PostgreSQL](../postgresql.md) | Database | Schema |
| [Presto](../presto.md) | Catalog | Schema |
| [Redshift](../redshift.md) | Database | Schema |
| [Snowflake](../snowflake.md) | Database | Schema |
| [Synapse](../synapse.md) | Database | Schema |
| [Teradata](../teradata.md) | — | Database |
| [Timescale DB](../timescale-db.md) | — | Schema |
| [Trino](../trino.md) | Catalog | Schema |

## Understanding the Columns

### Catalog Field

The **Catalog Field** is the first-level hierarchy used to group schemas. For connectors that show a "—", no catalog selection is needed — schemas are discovered directly from the connection.

Examples:

- **PostgreSQL**: The catalog is the `Database`. You first select a database, then discover schemas within it.
- **BigQuery**: The catalog is the `Project`. You first select a project, then discover datasets within it.
- **Oracle**: There is no catalog level. Schemas are discovered directly.

### Schema Field

The **Schema Field** is the target for multi-select. This is the level at which individual source datastores are created.

!!! note
    For connectors like **MySQL**, **MariaDB**, **Hive**, and **Teradata**, the "database" field acts as the schema target since these systems do not have a separate schema concept. Each "database" in these systems is treated as a schema for the purpose of multi-schema creation.

## Two-Step vs. Single-Step Discovery

| Flow Type | Connectors | Description |
|-----------|-----------|-------------|
| **Two-step** (Catalog → Schema) | PostgreSQL, Snowflake, BigQuery, SQL Server, Synapse, Databricks, Redshift, Fabric Analytics, Presto, Trino, Athena | First select a catalog, then discover and select schemas within it. |
| **Single-step** (Schema only) | Oracle, DB2, MySQL, MariaDB, Hive, Teradata, Dremio, Timescale DB | Schemas are discovered directly without a catalog selection. |
