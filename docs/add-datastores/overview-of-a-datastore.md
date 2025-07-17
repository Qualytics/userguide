# Source Datastore

Qualytics connects to data sources using "Datastores," a framework that enables organizations to:

* Connect with Apache Spark-compatible data sources.

* Support both traditional databases and modern object storage.

* Profile and monitor structured data across systems.

* Ensure secure and fast access to data.

* Scale data quality operations across platforms.

* Manage data quality centrally across all sources.

These data source integrations ensure comprehensive quality management across your entire data landscape, regardless of where your data resides.

## Understanding Datastores

A Datastore in Qualytics represents any structured data source, such as:

* Relational databases (RDBMS)

* Raw files like CSV, XLSX, JSON, Avro, or Parquet

* Cloud storage platforms like AWS S3, Azure Blob Storage, or GCP Cloud Storage

Qualytics integrates with these data sources through a layered architecture:

![datastore](../assets/datastores/what-is/datastore.png#only-light)
![datastore](../assets/datastores/what-is/datastore.png#only-dark)

## Configuring Data Source

Configure your data sources in Qualytics by connecting them through a new datastore.

**Step 1**: Log in to your Qualytics account and click on the **Add Source Datastore** button located at the top-right corner of the interface.

![add](../assets/datastores/what-is/add-light-1.png#only-light)
![add](../assets/datastores/what-is/add-dark-1.png#only-dark)

**Step 2**: A modal window- **Add Datastore** will appear, providing you with the options to connect a datastore.

![connector](../assets/datastores/what-is/connector-light-2.png#only-light)
![connector](../assets/datastores/what-is/connector-dark-2.png#only-dark)

| REF. | FIELDS | ACTIONS |
| :---- | :---- | :---- |
| 1. | Name | Specify the name of the datastore (e.g., The specified name will appear on the datastore cards) |
| 2. | Toggle Button | Toggle **ON** to create a new source datastore from scratch, or toggle **OFF** to reuse credentials from an existing connection |
| 3. | Connector | Select **Any Data source** from the dropdown list. |

## Available Datastores Connector

Qualytics supports a range of datasources, including but not limited to:

|          No. |                       Datasource |
| :---- | :---- |
|         1. |                         [Athena](../add-datastores/athena.md) |
|         2. |                      [Databricks](../add-datastores/databricks.md) |
|         3. |                          [DB2](../add-datastores/db2.md) |
|         4. |                         [Hive](../add-datastores/hive.md) |
|        5. |                      [MariaDB](../add-datastores/maria-db.md) |
|        6. |              [Microsoft SQL Server](../add-datastores/microsoft-sql-server.md) |
|        7. |                     [MySQL](../add-datastores/mysql.md) |
|        8. |                     [Oracle](../add-datastores/oracle.md) |
|        9.  |               [PostgreSQL](../add-datastores/postgresql.md) |
|      10. |                   [Presto](../add-datastores/presto.md) |
|      11. |            [Amazon Redshift](../add-datastores/redshift.md) |
|      12. |               [Snowflake](../add-datastores/snowflake.md) |
|      13. |                 [Synapse](../add-datastores/synapse.md) |
|      14. |            [Timescale DB](../add-datastores/timescale-db.md) |
|      15. |                  [Trino](../add-datastores/trino.md) |
|      16.  |             [Dremio](../add-datastores/dremio.md) |
|      17.  |             [Amazon S3](../add-datastores/amazon-s3.md) |
|      18. |         [Google Cloud Storage](../add-datastores/google-cloud-storage.md) |
|     19. |      [Windows Azure Storage Blob](../add-datastores/azure-datalake-storage.md) |
|     20. |        [Azure Blob File System](../add-datastores/azure-blob-storage.md) |

## Connection Management

To connect to a datastore, users must provide the required connection details, such as Host/Port or URI. These fields may vary depending on the datastore and are essential for establishing a secure and reliable connection to the target database.

For demonstration purposes, we have selected the **Snowflake** connector.

### Option I: Create a Datastore with a new Connection

If the toggle for **Add New connection** is turned on, then this will prompt you to add and configure the source datastore from scratch without using existing connection details.

**Step 1**: Select any connector as we are selecting **Snowflake** connector from the dropdown list and add connection properties such as Secrets Management, host, port, username, and password, along with datastore properties like catalog, database, etc.

![detail](../assets/datastores/what-is/detail-light-3.png#only-light)
![detail](../assets/datastores/what-is/detail-dark-3.png#only-dark)

For the next steps, refer to the "[**Add Source** **Datastore**](../add-datastores/snowflake.md#add-a-source-datastore)" section in the **Snowflake** Datastore documentation.

Once a datastore is verified and created, it appears in your source datastores.

![home](../assets/datastores/what-is/home-light-4.png#only-light)
![home](../assets/datastores/what-is/home-dark-4.png#only-dark)

## Datastore Operations

Once a datastore is added in Qualytics, you can perform three key operations to manage and ensure data quality effectively:

**1. Catalog Operation**

   This operation imports named data collections such as tables, views, and files into the source datastore. It identifies incremental fields for scans and allows you to recreate or delete containers, streamlining data organization and enhancing discovery.  

   For more details about the catalog operation, refer to the "[**Catalog Operation**](../source-datastore/catalog.md)" document.

**2. Profile Operation**

   After cataloging, the Profile Operation analyzes each record within the collections to assess and improve data quality. By generating detailed metadata and interacting with the Qualytics Inference Engine, it identifies quality issues and refines checks for maintaining data integrity.

   For more details about the profile operation, refer to the "[**Profile Operation**](../source-datastore/profile.md)" document.

**3. Scan Operation**

   Finally, the Scan Operation enforces data quality checks on the collections. It identifies anomalies at the record and schema levels, highlights structural issues, and records all findings for further analysis. Flexible options allow for incremental scans, specific table/file scans, and scheduling future scans.

   For more details about the scan operation, refer to the "[**Scan Operation**](../source-datastore/scan.md)" document.

By performing these operations sequentially, you can efficiently manage and ensure the quality of your data in Qualytics.

## View Operation

Once the datastores are connected, you can run operations on the selected datastore. To track the progress, simply navigate to the **Activity** tab, where you can view the running operation.

**Step 1:** Simply click to open the datastore on which you ran the operation.

![home](../assets/datastores/what-is/home-light-5.png#only-light)
![home](../assets/datastores/what-is/home-dark-5.png#only-dark)

**Step 2:** After click on datastore, select the "Activity" tab to view the ongoing operation.

![activity](../assets/datastores/what-is/activity-light-6.png#only-light)
![activity](../assets/datastores/what-is/activity-dark-6.png#only-dark)
