# Source Datastore

Qualytics connects to Source Datastore using "Datastores," a framework that enables organizations to:

* Connect with Apache Spark-compatible source datastore.  
* Support both traditional databases and modern object storage.  
* Profile and monitor structured data across systems.  
* Ensure secure and fast access to data.  
* Scale data quality operations across platforms.  
* Manage data quality centrally across all sources.

These source datastore integrations ensure comprehensive quality management across your entire data landscape, regardless of where your data resides.

## **Understanding Datastores**

A Datastore in Qualytics represents any structured source datastore, such as:

* Relational databases (RDBMS)  
* Raw files like CSV, XLSX, JSON, Avro, or Parquet  
* Cloud storage platforms like AWS S3, Azure Blob Storage, or GCP Cloud Storage

Qualytics integrates with these source datastores through a layered architecture:

![datastore](../assets/datastores/what-is/datastore.png#only-light)
![datastore](../assets/datastores/what-is/datastore.png#only-dark)

## Available Datastores Connector

Qualytics supports a range of source datastores, including but not limited to:

| No. | Source Datastores | Enrichment Support |
| :---- | :---- | :---- |
| 1. | [Amazon Redshift](../add-datastores/redshift.md) | Yes |
| 2. | [Amazon S3](../add-datastores/amazon-s3.md) | Yes |
| 3. | [Athena](../add-datastores/athena.md) | No |
| 4. | [Azure Datalake Storage (ABFS)](../add-datastores/azure-datalake-storage.md) | Yes |
| 5. | [Big Query](../add-datastores/bigquery.md) | Yes |
| 6. | [Databricks](../add-datastores/databricks.md) | Yes |
| 7. | [DB2](../add-datastores/db2.md) | Yes |
| 8. | [Dremio](../add-datastores/dremio.md) | No |
| 9. | [Google Cloud Storage](../add-datastores/google-cloud-storage.md) | Yes |
| 10. | [Hive](../add-datastores/hive.md) | No |
| 11. | [MariaDB](../add-datastores/maria-db.md) | Yes |
| 12. | [Microsoft SQL Server](../add-datastores/microsoft-sql-server.md) | Yes |
| 13. | [MySQL](../add-datastores/mysql.md) | Yes |
| 14. | [Oracle](../add-datastores/oracle.md) | No |
| 15. | [PostgreSQL](../add-datastores/postgresql.md) | Yes |
| 16. | [Presto](../add-datastores/presto.md) | No |
| 17. | [Snowflake](../add-datastores/snowflake.md) | Yes |
| 18. | [Synapse](../add-datastores/synapse.md) | Yes |
| 19. | [Teradata](../add-datastores/teradata.md) | No |
| 20. | [Timescale DB](../add-datastores/timescale-db.md) | No |
| 21. | [Trino](../add-datastores/trino.md) | Yes |