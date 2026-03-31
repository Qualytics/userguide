# Available Datastore Connectors

Qualytics provides **22 verified connectors** to integrate with your data platforms — 19 JDBC connectors for relational databases and 3 DFS connectors for distributed file systems and cloud object storage.

Each connector page contains step-by-step instructions for adding a source datastore, configuring connection properties, and linking an enrichment datastore.

!!! info "Enrichment Support"
    Want to check which connectors can be used as enrichment datastores? See the [Supported Enrichment Datastores](../../enrichment-support/supported-enrichment-datastores.md){:target="_blank"} page.

## JDBC Connectors

JDBC (Java Database Connectivity) connectors allow Qualytics to connect to relational databases. Data is organized as **Tables in a Schema** and accessed using standard SQL.

<div class="connector-table" markdown>

| No. | Connector | Logo | Multi-Schema Discovery |
| :--- | :--- | :---: | :---: |
| 1. | [Amazon Redshift](redshift.md) | ![Redshift](../../assets/shared/connector-logos/logo-redshift.svg){ width="24" } | :material-check-circle:{ .lg title="Supported" } |
| 2. | [Athena](athena.md) | ![Athena](../../assets/shared/connector-logos/logo-athena.svg){ width="24" } | :material-check-circle:{ .lg title="Supported" } |
| 3. | [BigQuery](bigquery.md) | ![BigQuery](../../assets/shared/connector-logos/logo-big-query.png){ width="24" } | :material-check-circle:{ .lg title="Supported" } |
| 4. | [Databricks](databricks.md) | ![Databricks](../../assets/shared/connector-logos/logo-databricks.png){ width="24" } | :material-check-circle:{ .lg title="Supported" } |
| 5. | [DB2](db2.md) | ![DB2](../../assets/shared/connector-logos/logo-ibm-db2.png){ width="24" } | :material-check-circle:{ .lg title="Supported" } |
| 6. | [Dremio](dremio.md) | ![Dremio](../../assets/shared/connector-logos/logo-dremio.svg){ width="24" } | :material-check-circle:{ .lg title="Supported" } |
| 7. | [Fabric Analytics](fabric-analytics.md) | ![Fabric](../../assets/shared/connector-logos/logo-microsoft-fabric.svg){ width="24" } | :material-close-circle-outline:{ .lg title="Not supported" } |
| 8. | [Hive](hive.md) | ![Hive](../../assets/shared/connector-logos/logo-hive.png){ width="24" } | :material-check-circle:{ .lg title="Supported" } |
| 9. | [MariaDB](maria-db.md) | ![MariaDB](../../assets/shared/connector-logos/logo-mariadb.svg){ width="24" } | :material-check-circle:{ .lg title="Supported" } |
| 10. | [Microsoft SQL Server](microsoft-sql-server.md) | ![SQL Server](../../assets/shared/connector-logos/logo-ms-sql.svg){ width="24" } | :material-check-circle:{ .lg title="Supported" } |
| 11. | [MySQL](mysql.md) | ![MySQL](../../assets/shared/connector-logos/mysql-icon.svg){ width="24" } | :material-check-circle:{ .lg title="Supported" } |
| 12. | [Oracle](oracle.md) | ![Oracle](../../assets/shared/connector-logos/oracle-icon.svg){ width="24" } | :material-check-circle:{ .lg title="Supported" } |
| 13. | [PostgreSQL](postgresql.md) | ![PostgreSQL](../../assets/shared/connector-logos/logo-postgres.svg){ width="24" } | :material-check-circle:{ .lg title="Supported" } |
| 14. | [Presto](presto.md) | ![Presto](../../assets/shared/connector-logos/presto.png){ width="24" } | :material-close-circle-outline:{ .lg title="Not supported" } |
| 15. | [Snowflake](snowflake.md) | ![Snowflake](../../assets/shared/connector-logos/snowflake.svg){ width="24" } | :material-check-circle:{ .lg title="Supported" } |
| 16. | [Synapse](synapse.md) | ![Synapse](../../assets/shared/connector-logos/logo-synapses.png){ width="24" } | :material-check-circle:{ .lg title="Supported" } |
| 17. | [Teradata](teradata.md) | ![Teradata](../../assets/shared/connector-logos/logo-teradata.png){ width="24" } | :material-close-circle-outline:{ .lg title="Not supported" } |
| 18. | [Timescale DB](timescale-db.md) | ![Timescale](../../assets/shared/connector-logos/logo-timescaledb.png){ width="24" } | :material-check-circle:{ .lg title="Supported" } |
| 19. | [Trino](trino.md) | ![Trino](../../assets/shared/connector-logos/trino.svg){ width="24" } | :material-check-circle:{ .lg title="Supported" } |

</div>

## DFS Connectors

DFS (Distributed File System) connectors allow Qualytics to connect to cloud object storage and distributed file systems. Data is organized as **Files in a Folder** and supports formats like AVRO, Parquet, CSV, and JSON.

<div class="connector-table" markdown>

| No. | Connector | Logo | Multi-Schema Discovery |
| :--- | :--- | :---: | :---: |
| 1. | [Amazon S3](amazon-s3.md) | ![S3](../../assets/shared/connector-logos/logo-s3.svg){ width="24" } | :material-close-circle-outline:{ .lg title="Not supported" } |
| 2. | [Azure Datalake Storage (ABFS)](azure-datalake-storage.md) | ![ABFS](../../assets/shared/connector-logos/logo-abfs.svg){ width="24" } | :material-close-circle-outline:{ .lg title="Not supported" } |
| 3. | [Google Cloud Storage](google-cloud-storage.md) | ![GCS](../../assets/shared/connector-logos/logo-gcs.svg){ width="24" } | :material-close-circle-outline:{ .lg title="Not supported" } |

</div>
