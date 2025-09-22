# Supported Enrichment Datastores

Qualytics offers a variety of connectors, some of which support enrichment capabilities while others do not. These connectors are grouped into two main categories: JDBC (Java Database Connectivity) and DFS (Distributed File System) datastores.

## JDBC Connectors in Qualytics

JDBC datastores in Qualytics make it easy to connect and manage data from relational databases. Using the JDBC API, you can establish secure connections, analyze data, and perform data profiling. This flexible feature supports a wide range of relational databases, making data discovery and quality checks seamless.

| No. | JDBC Connector | Enrichment Support |
| :---- | :---- | :---- |
| 01. | [Athena](../add-datastores/athena.md#add-enrichment-datastore) | No |
| 02. | [Big Query](../add-datastores/bigquery.md#add-enrichment-datastore) | Yes |
| 03. | [Databricks](../add-datastores/databricks.md#add-enrichment-datastore) | Yes |
| 04. | [DB2](../add-datastores/db2.md#add-enrichment-datastore) | No |
| 05. | [Dremio](../add-datastores/dremio.md#add-enrichment-datastore) | No |
| 06. | [Hive](../add-datastores/hive.md#add-enrichment-datastore) | No |
| 07. | [MariaDB](../add-datastores/maria-db.md#add-enrichment-datastore) | Yes |
| 08. | [Microsoft SQL](../add-datastores/microsoft-sql-server.md#add-enrichment-datastore) | Yes |
| 09. | [MySQL](../add-datastores/mysql.md#add-enrichment-datastore) | Yes |
| 10. | [Oracle](../add-datastores/oracle.md#add-enrichment-datastore) | No |
| 11. | [PostgreSQL](../add-datastores/postgresql.md#add-enrichment-datastore) | Yes |
| 12. | [Presto](../add-datastores/presto.md#add-enrichment-datastore) | No |
| 13. | [Redshift](../add-datastores/redshift.md#add-enrichment-datastore) | Yes |
| 14. | [Snowflake](../add-datastores/snowflake.md#add-enrichment-datastore-connection) | No |
| 15. | [Synapse](../add-datastores/synapse.md#add-enrichment-datastore) | Yes |
| 16. | [Teradata](../add-datastores/teradata.md#add-enrichment-datastore) | No |
| 17. | [TimescaleDB](../add-datastores/timescale-db.md#add-enrichment-datastore) | No |
| 18. | [Trino](../add-datastores/trino.md#add-enrichment-datastore) | Yes |

## DFS Connectors in Qualytics

DFS datastores in Qualytics handle data stored in distributed file systems. These systems include Hadoop Distributed File System (HDFS) and similar large-scale storage solutions. With DFS connectors, you can easily access and enrich data from distributed environments.

| No. |  DFS Connector | Enrichment Support |
| :---- | :---- | :---- |
| 1. | [Amazon S3](../add-datastores/amazon-s3.md#add-enrichment-datastore) | Yes |
| 2. |  [Azure Datalake Storage (ABFS)](../add-datastores/azure-datalake-storage.md#add-enrichment-datastore) | Yes |
| 3. | [Google Cloud Storage](../add-datastores/google-cloud-storage.md#add-enrichment-datastore) | Yes |
