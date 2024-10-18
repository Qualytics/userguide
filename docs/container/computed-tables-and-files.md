# Computed Tables & Files

Computed Tables and Computed Files are powerful virtual tables within the Qualytics platform, each serving distinct purposes in data manipulation. Computed Tables are created using SQL queries on JDBC source datastores, enabling advanced operations like joins and where clauses. Computed Files, derived from Spark SQL transformations on DFS source datastores, allow for efficient data manipulation and transformation directly within the DFS environment.

This guide explains how to add Computed Tables and Computed Files and discusses the differences between them.

Let's get started 🚀

## Computed Tables

Use Computed Tables when you want to perform the following operation on your selected source datastore:

-   Data Preparation and Transformation: Clean, shape, and restructure raw data from JDBC source datastores.           
-   Complex Calculations and Aggregations: Perform calculations not easily supported by standard containers.      
-   Data Subsetting: Extract specific data subsets based on filters using SQL's WHERE clause.     
-   Joining Data Across source datastores: Combine data from multiple JDBC source datastores using SQL joins.

## Add Computed Tables

**Step 1:** Sign in to your Qualytics account and select a JDBC-type source datastore from the side menu on which you would like to add computed table.

![select-datastore](../assets/datastores/add-computed-tables-files/select-datastore-light.png#only-light)
![select-datastore](../assets/datastores/add-computed-tables-files/select-datastore-dark.png#only-dark)

**Step 2:** After selecting your preferred source datastore, you will be redirected to the source datastore's store operation page. From this page, click on the **Add** button and select the **Computed Table** option from the dropdown menu.

![computed-table](../assets/datastores/add-computed-tables-files/select-computed-table-light.png#only-light)
![computed-table](../assets/datastores/add-computed-tables-files/select-computed-table-dark.png#only-dark)

**Step 3:** A modal window will appear prompting you to enter the name for your computed table and a valid SQL query that supports your selected source datastore.

| REF. | FIELDS | ACTIONS |
|------|--------|---------|
| 1.   | Name   | Enter a name for your compute table. The name should be descriptive and meaningful to help you easily identify the table later (e.g., add a meaningful name like `Customer_Order_Statistics`). |
| 2.   | Query  | Write the valid SQL queries that support your selected source datastore. The query helps to perform joins and aggregations on your selected source datastore. |

![add-computed-table](../assets/datastores/add-computed-tables-files/add-computed-table-light.png#only-light)
![add-computed-table](../assets/datastores/add-computed-tables-files/add-computed-table-dark.png#only-dark)

**Step 4:** Click on the **Add** button to add the computed file table with your selected source datastore.

![click-add](../assets/datastores/add-computed-tables-files/click-add-light.png#only-light)
![click-add](../assets/datastores/add-computed-tables-files/click-add-dark.png#only-dark)

## Computed Files

Use Computed Files when you want to perform the following operation on your selected source datastore:

-  Data Preparation and Transformation: Efficiently clean and restructure raw data stored in a DFS.
-  Column-Level Transformations: Utilize Spark SQL functions to manipulate and clean individual columns.
-  Filtering Data: Extract specific data subsets within a DFS container using Spark SQL's WHERE clause.

## Add Computed Files

**Step 1:** Sign in to your Qualytics account and select a DFS-type source datastore from the side menu on which you would like to add computed file.

![select-datastore](../assets/datastores/add-computed-tables-files/select-datastore-light.png#only-light)
![select-datastore](../assets/datastores/add-computed-tables-files/select-datastore-dark.png#only-dark)

**Step 2:** After clicking on your preferred source datastore, it will navigate you to the source datastore's store operation page. From this page, click on the **Add** button and select the **Computed files** option from the dropdown menu.

![select-computed-file](../assets/datastores/add-computed-tables-files/select-computed-file-light.png#only-light)
![select-computed-file](../assets/datastores/add-computed-tables-files/select-computed-file-dark.png#only-dark)

**Step 3:** A modal window will appear prompting you to enter the name for your computed file, select a source file pattern, select the expression, and define the filter clause (optional).

| REF. | FIELDS  | ACTION  |
|------|----------------------------|---------------------------------------|
| 1.   | Name (Required) | Enter a name for your computed table. The name should be descriptive and meaningful to help you easily identify the table later (e.g., add a meaningful name like Customer_Order_Statistics). |
| 2.   | Source File Pattern (Required) | Select a source file pattern from the dropdown menu to match files that have a similar naming convention. |
| 3.   | Select Expression (Required)  | Select the expression to define the data you want to include in the computed file.|
| 4.   | Filter Clause (Optional)   | Add a WHERE clause to filter the data that meets certain conditions. |
After configuring the **computed file** details, it will look like this:

![add-compute-file](../assets/datastores/add-computed-tables-files/add-compute-file-light.png#only-light)
![add-compute-file](../assets/datastores/add-computed-tables-files/add-compute-file-dark.png#only-dark)

**Step 4:** Click on the **Add** button to add the computed file with your selected source datastore.

![click-add-file](../assets/datastores/add-computed-tables-files/click-add-file-light.png#only-light)
![click-add-file](../assets/datastores/add-computed-tables-files/click-add-file-dark.png#only-dark)

After clicking on the **Add** button, a flash message for successful operation will display

![created-file](../assets/datastores/add-computed-tables-files/created-file-light.png#only-light)
![created-file](../assets/datastores/add-computed-tables-files/created-file-dark.png#only-dark)

## Computed Table Vs. Computed Files

| Feature             | Computed Table (JDBC)                 | Computed File (DFS)                        |
|---------------------|---------------------------------------|--------------------------------------------|
| Source Data         | JDBC source datastores                | DFS source datastores                      |
| Query Language      | SQL (database-specific functions)     | Spark SQL                                  |
| Supported Operations| Joins, where clauses, and database functions | Column transforms, where clauses (no joins), Spark SQL functions |

!!! note   
    Computed tables and files function like regular tables. You can profile them, create checks, and detect anomalies.   

    - Updating a computed table's query will trigger a profiling operation.      
    - Updating a computed file's select or where clause will trigger a profiling operation.  
    - When you create a computed table or file, a basic profile of up to 1000 records is automatically generated.