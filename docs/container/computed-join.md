# Computed Joined

A Computed Joined is a virtual table in Qualytics that allows you to combine data from two different containers, which can belong to either JDBC or DFS source datastores. It supports multiple join types and enables you to bring together data from different sources, making it easier to analyze related information and generate more unified insights.

Let's get started 🚀

Use Computed Joins when you want to combine data from multiple containers, including those across different source datastores:

* Cross-Datastore Data Analysis: Join data between containers from different datastores to support advanced analytical use cases.

* Multiple Join Types: Choose from Inner Join, Left Join, Right Join, and Full Outer Join to meet various data combination requirements.

* Field Mapping and Prefixing: Define joins using intuitive left and right container selections, configure field mappings, and optionally apply prefixes to avoid naming conflicts.

* Custom Query Enhancements: Add custom SELECT expressions and WHERE clauses to refine and filter the joined dataset.

## Add Computed Joined

**Step 1:** Log in to your Qualytics account and select the source datastore from the side menu that contains the container you want to include in the computed join.

![select-datastore](../assets/container/computed-join/select-datastore-light.png#only-light)
![select-datastore](../assets/container/computed-join/select-datastore-dark.png#only-dark)

**Step 2:** After selecting your preferred source datastore, you will be taken to the source datastore's store operation page. From this page, click on the **Add** button and select the **Computed Joined** option from the drop-down menu.

![select-computed-join](../assets/container/computed-join/select-computed-join-light.png#only-light)
![select-computed-join](../assets/container/computed-join/select-computed-join-dark.png#only-dark)

**Step 3:** A modal window will appear prompting you to enter the name for your computed join, select the join type, configure left and right references (datastore, container, fields), define the SELECT expression, and optionally add a filter clause.

| REF. | FIELDS  | ACTION  |
|------|----------------------------|---------------------------------------|
| 1.   | Name (Required) | Enter a name for your computed join. The name should be descriptive and meaningful for easier identification (e.g., Customer_Currency_Join). |
| 2.   | Join Type (Required) | Choose the type of join from the dropdown (e.g., Inner Join). Determines how rows from the two containers are combined. |
| 3.   | Left Reference (Required)  | Configure the left side of the join: the datastore is pre-selected based on your earlier selection. Choose the container and field to be used as the join key. Optionally, add a prefix.|
| 4.   | Right Reference (Required)   | Configure the right side of the join: select the datastore, container, and field to be used as a join key. Optionally, add a prefix. |
| 5.   | Select Expression (Required)   | Define the output fields using a valid SQL SELECT expression. Use this to control which columns appear in the computed join result. |
| 6.   | Filter Clause (Optional)   | Add a WHERE clause to filter the joined data based on specific conditions. |

![computed-join](../assets/container/computed-join/computed-join-light.png#only-light)
![computed-join](../assets/container/computed-join/computed-join-dark.png#only-dark)

**Step 4:** Click on the **Add** button to create the computed join using the configured join settings and selected source containers.

![add-join](../assets/container/computed-join/add-join-light.png#only-light)
![add-join](../assets/container/computed-join/add-join-dark.png#only-dark)

After clicking the **Add** button, a success notification appears on the screen showing the action was completed successfully.
