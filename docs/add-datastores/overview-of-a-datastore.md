# Data Source

Qualytics connects to data sources using "Datastores," a framework that enables organizations to:

* Connect with Apache Spark-compatible data sources.

* Support both traditional databases and modern object storage.

* Profile and monitor structured data across systems.

* Ensure secure and fast access to data.

* Scale data quality operations across platforms.

* Manage data quality centrally across all sources.


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

Qualytics supports a range of datasource, including but not limited to:

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
|      16.  |             [Amazon S3](../add-datastores/amazon-s3.md) |
|      17. |         [Google Cloud Storage](../add-datastores/google-cloud-storage.md) |
|     18. |      [Window Azure Storage Blob](../add-datastores/azure-datalake-storage.md) |
|     19. |        [Azure Blob File System](../add-datastores/azure-blob-storage.md) |
|     20. |      [Qualytics File System (QFS)](../add-datastores/qfs.md) |

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

**1.Catalog Operation**

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
















# Data Sources

The Qualytics platform connects to your enterprise data sources through "Datastores" - our unified connection framework that enables organizations to:
- Connect to any Apache Spark-compatible data source
- Support both traditional databases and modern object storage
- Profile and monitor structured data across your ecosystem
- Maintain secure, performant data access
- Scale data quality operations across diverse data platforms
- Centralize data quality management across sources

These data source integrations ensure comprehensive quality management across your entire data landscape, regardless of where your data resides.

## Understanding Datastores

A Datastore in Qualytics represents any structured data source, including:
- Traditional relational databases (RDBMS)
- Raw files (CSV, XLSX, JSON, Avro, Parquet)
- Cloud storage platforms (AWS S3, Azure Blob Storage, GCP Cloud Storage)

Qualytics integrates with these data sources through a layered architecture:

![Screenshot](../assets/datastores/what-is/qualytics-architecture.png)

## Configuring Data Sources

Start connecting your data sources by adding a new Datastore:

1. Navigate to the Datastores tab in the main menu
2. Click the Add Source Datastore button:

![Screenshot](../assets/datastores/what-is/add-new-datastore-button-light.png#only-light)
![Screenshot](../assets/datastores/what-is/add-new-datastore-button-dark.png#only-dark)

![Screenshot](../assets/datastores/what-is/add-datastore-light.png#only-light){: style="width:450px"}
![Screenshot](../assets/datastores/what-is/add-datastore-dark.png#only-dark){: style="width:450px"}

!!! info
Qualytics supports any Apache Spark-compatible data source:

    1. Traditional RDBMS 
    2. Raw files (CSV, XLSX, JSON, Avro, Parquet) on:
        - AWS S3
        - Azure Blob Storage
        - GCP Cloud Storage

![Screenshot](../assets/datastores/what-is/listing-datastores-light.png#only-light){: style="width:450px"}
![Screenshot](../assets/datastores/what-is/listing-datastores-dark.png#only-dark){: style="width:450px"}

## Connection Management

Each Datastore type requires specific connection credentials. For example, here's a Snowflake connection configuration:

![Screenshot](../assets/datastores/what-is/add-snowflake-datastore-light.png#only-light){: style="width:450px"}
![Screenshot](../assets/datastores/what-is/add-snowflake-datastore-dark.png#only-dark){: style="width:450px"}

Successfully configured Datastores appear on your home screen:

![Screenshot](../assets/datastores/what-is/show-all-created-datastores-light.png#only-light)
![Screenshot](../assets/datastores/what-is/show-all-created-datastores-dark.png#only-dark)

## Datastore Operations

Each Datastore provides access to Qualytics' core capabilities and operations:

Initial Datastore View:
![Screenshot](../assets/datastores/what-is/specific-datastore-light.png#only-light)
![Screenshot](../assets/datastores/what-is/specific-datastore-dark.png#only-dark)

Activity Monitoring:
![Screenshot](../assets/datastores/what-is/data-volume-light.png#only-light)
![Screenshot](../assets/datastores/what-is/data-volume-dark.png#only-dark)

## Getting Started with a New Datastore

When you first configure a Datastore:

1. An automatic Catalog operation initiates to discover your data assets
2. After cataloging completes, run a Profile operation to:
  - Generate comprehensive metadata
  - Infer data quality checks
  - Enable quality monitoring

To start profiling:

![Screenshot](../assets/datastores/what-is/running-profile-menu-light.png#only-light)
![Screenshot](../assets/datastores/what-is/running-profile-menu-dark.png#only-dark)

![Screenshot](../assets/datastores/what-is/running-profile-light.png#only-light){: style="height:auto"}
![Screenshot](../assets/datastores/what-is/running-profile-dark.png#only-dark){: style="height:auto"}
