# JDBC Datastore Overview

The JDBC Datastore in Qualytics facilitates seamless integration with relational databases using the Java Database Connectivity (JDBC) API. 
This allows users to connect, analyze, and profile data stored in various relational databases. 

## Supported Databases

Qualytics supports a range of relational databases, including but not limited to:

- [**BigQuery**](../datastores/bigquery.md)
- [**Databricks**](../datastores/databricks.md)
- [**DB2**](../datastores/db2.md)
- [**Hive**](../datastores/hive.md)
- [**MariaDB**](../datastores/maria-db.md)
- [**Microsoft SQL Server**](../datastores/microsoft-sql-server.md)
- [**MySQL**](../datastores/mysql.md)
- [**Oracle**](../datastores/oracle.md)
- [**PostgreSQL**](../datastores/postgresql.md)
- [**Presto**](../datastores/presto.md)
- [**Amazon Redshift**](../datastores/redshift.md)
- [**Snowflake**](../datastores/snowflake.md)
- [**Synapse**](../datastores/synapse.md)
- [**Timescale DB**](../datastores/timescale-db.md)
- [**Trino**](../datastores/trino.md)
- **Athena**


##  Connection Details

Users are required to provide specific connection details such as Host/Port or URI for the JDBC Datastore.

The connection details are used to establish a secure and reliable connection to the target database.


## Catalog Operation

Upon successful verification, a Catalog operation can be initiated, providing metadata about the JDBC Datastore, including containers, field names, and record counts.

## Field Types Inference

During the Catalog operation, Qualytics infers field types by weighted histogram analysis.
This allows for automatic detection of data types within the JDBC Datastore, facilitating more accurate data profiling.

## Containers Overview

For a more detailed understanding of how Qualytics manages and interacts with containers in JDBC Datastores, please refer to the [Containers](/userguide/container/what-is-container) section in our comprehensive user guide. 

This section covers topics such as container deletion, field deletion, and the initial profile of a Datastore's containers.

