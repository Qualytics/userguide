# Computed Table vs Computed File

| **Feature** | **Computed Table (JDBC)** | **Computed File (DFS)** |
|--------------|----------------------------|---------------------------|
| Source Data | JDBC source datastores | DFS source datastores |
| Query Language | SQL (database-specific functions) | Spark SQL |
| Supported Operations | Joins, where clauses, and database functions | Column transforms, where clauses (no joins), Spark SQL functions |

!!! note
    Computed tables and files function like regular tables. You can profile them, create checks, and detect anomalies.

    - Updating a computed table’s query will trigger a profiling operation.  
    - Updating a computed file’s select or where clause will trigger a profiling operation.  
    - When you create a computed table or file, a basic profile of up to 1000 records is automatically generated.