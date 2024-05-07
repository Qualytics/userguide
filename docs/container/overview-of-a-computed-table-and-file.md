# Computed Tables and Files Overview

Computed tables and computed files are powerful virtual tables within the Qualytics platform.

## Key Concepts

### Computed Tables

A container created from SQL queries on JDBC datastores, allowing advanced data manipulation (joins, where clauses, etc.).

### Computed Files

A container derived from Spark SQL transformations on DFS datastores.

## When to Use Computed Tables

* **Data Preparation and Transformation**: Clean, shape, and restructure raw data from JDBC datastores.
* **Complex Calculations and Aggregations**: Perform calculations not easily supported by standard containers.
* **Data Subsetting**: Extract specific data subsets based on filters using SQL's WHERE clause.
* **Joining Data Across Datastores**: Combine data from multiple JDBC datastores using SQL joins.

## When to Use Computed Files

* **Data Preparation and Transformation**: Clean and restructure data from raw files stored in a DFS.
* **Column-Level Transformations**: Apply Spark SQL functions to individual columns for data manipulation and cleaning.
* **Filtering Data**: Create subsets of data within a DFS container using Spark SQL's WHERE clause.
* **Important Note**: Computed files currently do not support joins or union operations. If these operations are required, consider using a computed table or alternative data transformation techniques.
 

## Key Differences

| Feature                | Computed Table (JDBC) | Computed File (DFS) |
|------------------------|-----------------------|---------------------| 
| Source Data            | JDBC Datastores       | DFS Datastores      |
| Query Language         | SQL (database-specific functions)  | Spark SQL           |
| Supported Operations   | Joins, where clauses, database functions | Column transforms, where clauses (no joins), SparkSQL functions|


## Important Notes

* Computed tables/files behave like normal tables. You can profile them, create checks, and detect anomalies.
* Updating a computed table's query triggers a profiling operation.
* Updating a computed file's select clause or where clause triggers a profiling operation.
* Upon creation, a basic profile (max 1000 records) is automatically generated.
