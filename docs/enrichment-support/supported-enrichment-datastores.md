# Supported Enrichment Datastores

Qualytics supports enrichment datastore connectors that help enhance data discovery, profiling, and quality checks. Some connectors include enrichment capabilities, while others provide only standard connectivity.

In this guide, we will cover:

- **[JDBC Connectors with Enrichment Support](#jdbc-connectors-with-enrichment-support)**
- **[JDBC Connectors without Enrichment Support](#jdbc-connector-without-enrichment-support)**
- **[DFS Connectors with Enrichment Support](#dfs-connector-with-enrichment-support)**
- **[DFS Connectors without Enrichment Support](#dfs-connector-without-enrichment-support)**

Let’s get started 🚀.

## JDBC Connectors with Enrichment Support

The table below lists JDBC connectors with enrichment support for enhanced data profiling and quality checks:

| No. | Enrichment Support |
| :---- | :---- |
| 01. | [Big Query](../add-datastores/bigquery.md#add-enrichment-datastore) | 
| 02. | [Databricks](../add-datastores/databricks.md#add-enrichment-datastore) |
| 03. | [DB2](../add-datastores/db2.md#add-enrichment-datastore) | 
| 04. | [MariaDB](../add-datastores/maria-db.md#add-enrichment-datastore) | 
| 05. | [Microsoft SQL Server](../add-datastores/microsoft-sql-server.md#add-enrichment-datastore) | 
| 06. | [MySQL](../add-datastores/mysql.md#add-enrichment-datastore) | 
| 07. | [PostgreSQL](../add-datastores/postgresql.md#add-enrichment-datastore)| 
| 08. | [Redshift](../add-datastores/redshift.md#add-enrichment-datastore)|
| 09. | [Snowflake](../add-datastores/snowflake.md#add-enrichment-datastore-connection) | 
| 10. | [Synapse](../add-datastores/synapse.md#add-enrichment-datastore) | 
| 11. | [Trino](../add-datastores/trino.md#add-enrichment-datastore) | 

## JDBC Connectors without Enrichment Support

The table below shows the JDBC connectors that do not support enrichment capabilities but still provide basic connectivity for data integration:

| No. | Enrichment Not Support |
| :---- | :---- |
| 1. | [Athena](../add-datastores/athena.md) |
| 2. | [Dremio](../add-datastores/dremio.md) |
| 3. | [Hive](../add-datastores/hive.md) | 
| 4. | [Oracle](../add-datastores/oracle.md) | 
| 5. | [Presto](../add-datastores/presto.md) | 
| 6. | [Teradata](../add-datastores/teradata.md) |
| 7. | [TimescaleDB](../add-datastores/timescale-db.md) | 

## DFS Connectors with Enrichment Support

The table below lists DFS connectors with enrichment support for enhanced data profiling and discovery:

| No. | Enrichment Support |
| :---- | :---- |
| 01. | [Amazon S3](../add-datastores/amazon-s3.md#add-enrichment-datastore) |
| 02. | [Azure Datalake Storage (ABFS)](../add-datastores/azure-datalake-storage.md#add-enrichment-datastore) |
| 03. | [Google Cloud Storage (GCS)](../add-datastores/google-cloud-storage.md#add-enrichment-datastore) |

## DFS Connectors without Enrichment Support

Currently in Qualytics, all available DFS datastores support enrichment. There are no DFS datastores without enrichment support.