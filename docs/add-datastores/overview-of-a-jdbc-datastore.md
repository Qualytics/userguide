# JDBC Datastore Overview

JDBC Datastore in Qualytics allows you to easily integrate and manage data from relational databases. Using the Java Database Connectivity (JDBC) API, you can securely connect to databases, analyze data, and perform data profiling. This feature supports a wide range of relational databases, providing you with a flexible solution for data discovery and quality checks.

## Adding JDBC Datastore

Log in to your Qualytics account and click on the **Add Source Datastore** button located at the top-right corner of the interface.

![add-datastore](../assets/datastores/jdbc-datastores/add-datastore-light.png#only-light)
![add-datastore](../assets/datastores/jdbc-datastores/add-datastore-dark.png#only-dark)

For detailed steps on adding a JDBC Datastore, refer to the [**Add the Source Datastore**](../add-datastores/athena.md#add-the-source-datastore) section of the documentation.

## Supported JDBC Databases

Qualytics supports a range of relational databases, including but not limited to:

* [Athena](../add-datastores/athena.md)  
* [Databricks](../add-datastores/databricks.md)  
* [DB2](../add-datastores/db2.md)  
* [Hive](../add-datastores/hive.md)  
* [MariaDB](../add-datastores/maria-db.md)  
* [Microsoft SQL Server](../add-datastores/microsoft-sql-server.md)  
* [MySQL](../add-datastores/mysql.md)  
* [Oracle](../add-datastores/oracle.md)  
* [PostgreSQL](../add-datastores/postgresql.md)  
* [Presto](../add-datastores/presto.md)  
* [Amazon Redshift](../add-datastores/redshift.md)  
* [Snowflake](../add-datastores/snowflake.md)  
* [Synapse](../add-datastores/synapse.md)  
* [Timescale DB](../add-datastores/timescale-db.md)  
* [Trino](../add-datastores/trino.md)

## Connection Details

To connect to a JDBC datastore, users must provide the required connection details, such as Host/Port or URI. These fields may vary depending on the datastore and are essential for establishing a secure and reliable connection to the target database.

For more information about connections, refer to the [**Connection Overview**](../connections/overview-of-a-connection.md) documentation.

## Catalog Operation  

After adding a JDBC Datastore, you can initiate a **Catalog operation** to extract key metadata from the database. This operation provides:

* A list of containers (schemas, tables, or views).  
* Field names within each container.  
* Record counts for data analysis and profiling.

![catalog](../assets/datastores/jdbc-datastores/catalog-light.png#only-light)
![catalog](../assets/datastores/jdbc-datastores/catalog-dark.png#only-dark)

For more information about how to run catalog operation, refer to the [**Catalog Operation**](../source-datastore/catalog.md) documentation.

## Field Types Inference

Qualytics employs weighted histogram analysis during the Catalog operation to infer field types automatically. This advanced method ensures accurate detection of data types within the JDBC Datastore, enhancing the precision of data profiling.

## Containers Overview  

Containers are fundamental entities representing structured data sets. These containers could manifest as tables in JDBC datastores or as files within DFS datastores. They play a pivotal role in data organization, profiling, and quality checks within the Qualytics application.  For a more detailed understanding of how Qualytics manages and interacts with containers in JDBC Datastores, please refer to the [**Containers overview**](../container/container.md) documentation.