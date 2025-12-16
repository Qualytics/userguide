# Computed Table vs Computed File

Computed Tables and Computed Files both allow you to generate transformed datasets within Qualytics, but they differ in how the output is stored, processed, and consumed. **Computed Tables** produce table-like results inside JDBC datastores and support SQL-based relational operations such as joins. **Computed Files**, on the other hand, generate file-based outputs stored in DFS datastores and support Spark SQL operations suited for large-scale file processing. This comparison helps you choose the right option for your transformation needs.

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