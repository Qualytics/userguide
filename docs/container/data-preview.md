# Data Preview

Data Preview in Qualytics makes it easy for users to view and understand their container data. It provides a clear snapshot of the data's structure and contents, showing up to 100 rows from the source. With options to filter specific data, refresh for the latest updates, and download records, it helps users focus on the most relevant information, troubleshoot issues, and analyze data effectively. The simple grid view ensures a smooth and efficient way to explore and work with your data.

Let’s get started 🚀

## Navigation

**Step 1:** Log in to your Qualytics account and select the source datastore (JDBC or DFS) from the left menu that contains the data you want to preview.

![select](../assets/container/data-preview/select-light.png#only-light)
![select](../assets/container/data-preview/select-dark.png#only-dark)

**Step 2:** Select Tables (if JDBC datastore is connected) or File Patterns (if DFS datastore is connected) from the Navigation tab on the top.

!!! note 
    Before accessing the Data Preview tab, ensure the container is profiled. If not, run a profile operation on the container. Profiling collects important information about the table structure, like column types and field names. Without profiling, no data will be shown in the Data Preview section. 

![table](../assets/container/data-preview/table-light.png#only-light)
![table](../assets/container/data-preview/table-dark.png#only-dark)

**Step 3:** You will view the full list of tables or files belonging to the selected source datastore. Select the specific table or file whose data you want to preview.

![list](../assets/container/data-preview/list-light.png#only-light)
![list](../assets/container/data-preview/list-dark.png#only-dark)

Alternatively, you can access the tables or files by clicking the drop-down arrow on the selected datasource. This will display the full list of tables or files associated with the selected source datastore. From there, select the specific table or file whose data you want to preview.

![alter](../assets/container/data-preview/alter-light.png#only-light)
![alter](../assets/container/data-preview/alter-dark.png#only-dark)

**Step 4:** After selecting the specific table or file, click on the Data Preview tab.

![preview](../assets/container/data-preview/preview-light.png#only-light)
![preview](../assets/container/data-preview/preview-dark.png#only-dark)

You will see a tabular view of the data, displaying the field names (columns) and their corresponding data values, allowing you to review the data's structure, types, and sample records.

![tabular](../assets/container/data-preview/tabular-light.png#only-light)
![tabular](../assets/container/data-preview/tabular-dark.png#only-dark)

## UI Caching

Upon initial access, data in the Data Preview section, the data may not be stored (cached) yet, which can cause longer loading times. How long it takes to load depends on the type of data store being used (like DFS or JDBC) and if the data warehouse is serverless. However, the next time you access the same data, it will load faster because it will be cached, meaning the data is stored temporarily for quicker access.

## Filter Clause and Refresh

**Data Preview** tab includes a filter functionality that enables users to focus on a specific field by applying filter clauses. This refines the displayed rows based on specific criteria, enhancing data analysis and providing more targeted insights and a **Refresh** button to update the data view with the latest data. 

### Filter Clause

Use the Filter Clause to narrow down the displayed rows by applying specific filter clauses, allowing for focused and precise data analysis.

![filter](../assets/container/data-preview/filter-light.png#only-light)
![filter](../assets/container/data-preview/filter-dark.png#only-dark)

### Refresh

Click **Refresh** button to update the data view with the latest information, ensuring accuracy and relevance.

![refresh](../assets/container/data-preview/refresh-light.png#only-light)
![refresh](../assets/container/data-preview/refresh-dark.png#only-dark)

## Select Specific Fields

Select specific fields to display, allowing you to focus on the most relevant data for analysis.To focus on relevant data for analysis, click on the **Select Fields to Show** dropdown. Choose specific fields you want to review by checking or unchecking options.

![field](../assets/container/data-preview/field-light.png#only-light)
![field](../assets/container/data-preview/field-dark.png#only-dark)

## Download Records

**Download Records** feature in Qualytics allows users to easily export all source records from the selected enrichment dataset. This functionality is essential for performing deeper analysis outside the platform or for sharing data with external tools and teams.

![download](../assets/container/data-preview/download-light.png#only-light)
![download](../assets/container/data-preview/download-dark.png#only-dark)

## Use Cases

### Debugging Checks

One of the primary use cases of the Data Preview tab is for debugging checks. Users can efficiently inspect the first 100 rows of container data to identify any anomalies, inconsistencies, or errors, facilitating the debugging process and improving data quality.

### Data Analysis

The Data Preview tab also serves as a valuable tool for data analysis tasks. Users can explore the dataset, apply filters to focus on specific subsets of data, and gain insights into patterns, trends, and correlations within the container data.

## Examples

### Example 1: Debugging Data Import

Suppose a user encounters issues with importing data into a container. By utilizing the Data Preview tab, the user can quickly examine the first 100 rows of imported data, identify any formatting errors or missing values, and troubleshoot the data import process effectively.

### Example 2: Filtering Data by Date Range

In another scenario, a user needs to analyze sales data within a specific date range. The user can leverage the filter support feature of the Data Preview tab to apply date range filters, displaying only the sales records that fall within the specified timeframe. This allows for targeted analysis and informed decision-making.