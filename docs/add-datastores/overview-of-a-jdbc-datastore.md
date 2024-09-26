# JDBC Datastore Overview

The JDBC Datastore in Qualytics facilitates seamless integration with relational databases using the Java Database Connectivity (JDBC) API. 
This allows users to connect, analyze, and profile data stored in various relational databases. 

## Supported Databases

Qualytics supports a range of relational databases, including but not limited to:

- [**BigQuery**](../add-datastores/bigquery.md)
- [**Databricks**](../add-datastores/databricks.md)
- [**DB2**](../add-datastores/db2.md)
- [**Hive**](../add-datastores/hive.md)
- [**MariaDB**](../add-datastores/maria-db.md)
- [**Microsoft SQL Server**](../add-datastores/microsoft-sql-server.md)
- [**MySQL**](../add-datastores/mysql.md)
- [**Oracle**](../add-datastores/oracle.md)
- [**PostgreSQL**](../add-datastores/postgresql.md)
- [**Presto**](../add-datastores/presto.md)
- [**Amazon Redshift**](../add-datastores/redshift.md)
- [**Snowflake**](../add-datastores/snowflake.md)
- [**Synapse**](../add-datastores/synapse.md)
- [**Timescale DB**](../add-datastores/timescale-db.md)
- [**Trino**](../add-datastores/trino.md)
- [**Athena**](../add-datastores/athena.md)


##  Connection Details

Users are required to provide specific connection details such as Host/Port or URI for the JDBC Datastore.

The connection details are used to establish a secure and reliable connection to the target database.


## Catalog Operation

Upon successful verification, a Catalog operation can be initiated, providing metadata about the JDBC Datastore, including containers, field names, and record counts.

## Field Types Inference

During the Catalog operation, Qualytics infers field types by weighted histogram analysis.
This allows for automatic detection of data types within the JDBC Datastore, facilitating more accurate data profiling.

## Containers Overview

For a more detailed understanding of how Qualytics manages and interacts with containers in JDBC Datastores, please refer to the [Containers](/userguide/container/container) section in our comprehensive user guide. 

This section covers topics such as container deletion, field deletion, and the initial profile of a Datastore's containers.

