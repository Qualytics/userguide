# Overview of infer data type

The "infer data type" option in containers allows the system to automatically determine the appropriate data types (e.g., fractional, integer, date) for columns within your data containers.  This setting is configurable for both JDBC and DFS containers.

## Behavior in JDBC Datastores

* **Default:** Disabled
* **Reason:** JDBC datastores provide inherent schema information from the database tables. Qualytics leverages this existing schema for accurate data typing. 
* **Override:** You can optionally enable this setting if encountering issues with automatic type detection from the source database.

## Behavior in DFS Datastores

* **Default:** 
    * Enabled for CSV files 
    * Disabled for other file formats (Parquet, Delta, Avro, ORC, etc.)
* **Reason:** 
    * CSV files lack a defined schema. Data type inference helps ensure correct data interpretation.
    * File formats like Parquet, Delta, Avro, and ORC have embedded schemas, making inference unnecessary.
* **Override:** You can adjust the default behavior based on your specific data sources and requirements.

## Rule for the "Infer Data Type" 

### Schema-Based Data Sources

If the data source has a defined schema (JDBC, Delta, Parquet, Avro, ORC), the flag is set to "False".

### Schema-less Data Sources

If the data source lacks a defined schema (CSV), the flag is set to "True".
