# Supported Enrichment Datastores

An enrichment datastore is a dedicated datastore linked to a source datastore that persists scan results, anomalies, remediation data, and source record examples. Not all connectors support enrichment — the tables below show which connectors can be used as enrichment datastores.

Enrichment support requires the connector to have **write capabilities** so that Qualytics can create and manage enrichment tables (source records, anomaly records, remediation tables, and metadata tables) in the target datastore.

!!! info "Available Datastore Connectors"
    For the full list of all supported source datastore connectors (including those without enrichment support), see the [Available Datastore Connectors](../source-datastore/add-datastores/available-datastore-connectors.md){:target="_blank"} page.

!!! info "Enrichment Table Types"
    To understand the different table types created in an enrichment datastore (source records, anomaly records, remediation, metadata), see the [Enrichment Table Types](../enrichment/table-types.md){:target="_blank"} documentation.

## JDBC Connectors

JDBC connectors that support enrichment can store scan results and anomaly data directly in the relational database. Out of 19 JDBC connectors, **11 support enrichment**.

<div class="connector-table" markdown>

| No. | Connector | Logo | Enrichment Support |
| :--- | :--- | :---: | :---: |
| 1. | [Athena](../source-datastore/add-datastores/athena.md) | ![Athena](../assets/source-datastores/add-datastores/connector-logos/logo-athena.svg){ width="24" } | :material-close-circle-outline:{ .lg title="Not supported" } |
| 2. | [BigQuery](../source-datastore/add-datastores/bigquery.md#add-enrichment-datastore) | ![BigQuery](../assets/source-datastores/add-datastores/connector-logos/logo-big-query.png){ width="24" } | :material-check-circle:{ .lg title="Supported" } |
| 3. | [Databricks](../source-datastore/add-datastores/databricks.md#add-enrichment-datastore) | ![Databricks](../assets/source-datastores/add-datastores/connector-logos/logo-databricks.png){ width="24" } | :material-check-circle:{ .lg title="Supported" } |
| 4. | [DB2](../source-datastore/add-datastores/db2.md#add-enrichment-datastore) | ![DB2](../assets/source-datastores/add-datastores/connector-logos/logo-ibm-db2.png){ width="24" } | :material-check-circle:{ .lg title="Supported" } |
| 5. | [Dremio](../source-datastore/add-datastores/dremio.md) | ![Dremio](../assets/source-datastores/add-datastores/connector-logos/logo-dremio.svg){ width="24" } | :material-close-circle-outline:{ .lg title="Not supported" } |
| 6. | [Fabric Analytics](../source-datastore/add-datastores/fabric-analytics.md) | ![Fabric](../assets/source-datastores/add-datastores/connector-logos/logo-microsoft-fabric.svg){ width="24" } | :material-close-circle-outline:{ .lg title="Not supported" } |
| 7. | [Hive](../source-datastore/add-datastores/hive.md) | ![Hive](../assets/source-datastores/add-datastores/connector-logos/logo-hive.png){ width="24" } | :material-close-circle-outline:{ .lg title="Not supported" } |
| 8. | [MariaDB](../source-datastore/add-datastores/maria-db.md#add-enrichment-datastore) | ![MariaDB](../assets/source-datastores/add-datastores/connector-logos/logo-mariadb.svg){ width="24" } | :material-check-circle:{ .lg title="Supported" } |
| 9. | [Microsoft SQL Server](../source-datastore/add-datastores/microsoft-sql-server.md#add-enrichment-datastore) | ![SQL Server](../assets/source-datastores/add-datastores/connector-logos/logo-ms-sql.svg){ width="24" } | :material-check-circle:{ .lg title="Supported" } |
| 10. | [MySQL](../source-datastore/add-datastores/mysql.md#add-enrichment-datastore) | ![MySQL](../assets/source-datastores/add-datastores/connector-logos/mysql-icon.svg){ width="24" } | :material-check-circle:{ .lg title="Supported" } |
| 11. | [Oracle](../source-datastore/add-datastores/oracle.md) | ![Oracle](../assets/source-datastores/add-datastores/connector-logos/oracle-icon.svg){ width="24" } | :material-close-circle-outline:{ .lg title="Not supported" } |
| 12. | [PostgreSQL](../source-datastore/add-datastores/postgresql.md#add-enrichment-datastore) | ![PostgreSQL](../assets/source-datastores/add-datastores/connector-logos/logo-postgres.svg){ width="24" } | :material-check-circle:{ .lg title="Supported" } |
| 13. | [Presto](../source-datastore/add-datastores/presto.md) | ![Presto](../assets/source-datastores/add-datastores/connector-logos/presto.png){ width="24" } | :material-close-circle-outline:{ .lg title="Not supported" } |
| 14. | [Redshift](../source-datastore/add-datastores/redshift.md#add-enrichment-datastore) | ![Redshift](../assets/source-datastores/add-datastores/connector-logos/logo-redshift.svg){ width="24" } | :material-check-circle:{ .lg title="Supported" } |
| 15. | [Snowflake](../source-datastore/add-datastores/snowflake.md#add-enrichment-datastore-connection) | ![Snowflake](../assets/source-datastores/add-datastores/connector-logos/snowflake.svg){ width="24" } | :material-check-circle:{ .lg title="Supported" } |
| 16. | [Synapse](../source-datastore/add-datastores/synapse.md#add-enrichment-datastore) | ![Synapse](../assets/source-datastores/add-datastores/connector-logos/logo-synapses.png){ width="24" } | :material-check-circle:{ .lg title="Supported" } |
| 17. | [Teradata](../source-datastore/add-datastores/teradata.md) | ![Teradata](../assets/source-datastores/add-datastores/connector-logos/logo-teradata.png){ width="24" } | :material-close-circle-outline:{ .lg title="Not supported" } |
| 18. | [TimescaleDB](../source-datastore/add-datastores/timescale-db.md) | ![Timescale](../assets/source-datastores/add-datastores/connector-logos/logo-timescaledb.png){ width="24" } | :material-close-circle-outline:{ .lg title="Not supported" } |
| 19. | [Trino](../source-datastore/add-datastores/trino.md) | ![Trino](../assets/source-datastores/add-datastores/connector-logos/trino.svg){ width="24" } | :material-check-circle:{ .lg title="Supported" } |

</div>

## DFS Connectors

DFS connectors that support enrichment store scan results and anomaly data as files (Parquet/JSON) in cloud object storage. **All 3 DFS connectors support enrichment**.

<div class="connector-table" markdown>

| No. | Connector | Logo | Enrichment Support |
| :--- | :--- | :---: | :---: |
| 1. | [Amazon S3](../source-datastore/add-datastores/amazon-s3.md#add-enrichment-datastore) | ![S3](../assets/source-datastores/add-datastores/connector-logos/logo-s3.svg){ width="24" } | :material-check-circle:{ .lg title="Supported" } |
| 2. | [Azure Datalake Storage (ABFS)](../source-datastore/add-datastores/azure-datalake-storage.md#add-enrichment-datastore) | ![ABFS](../assets/source-datastores/add-datastores/connector-logos/logo-abfs.svg){ width="24" } | :material-check-circle:{ .lg title="Supported" } |
| 3. | [Google Cloud Storage (GCS)](../source-datastore/add-datastores/google-cloud-storage.md#add-enrichment-datastore) | ![GCS](../assets/source-datastores/add-datastores/connector-logos/logo-gcs.svg){ width="24" } | :material-check-circle:{ .lg title="Supported" } |

</div>
