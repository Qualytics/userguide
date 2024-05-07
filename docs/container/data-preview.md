# Data Preview

The `Data Preview` section in the platform provides users with a streamlined preview of specific container data, offering direct insights into its structure and contents. This feature streamlines workflow processes and empowers users to make confident, data-driven decisions.

`Data preview` is dedicated to displaying a concise yet comprehensive preview of container data, facilitating various tasks such as debugging quality checks and data analysis. It enhances the user experience by offering a grid view that showcases a maximum of 100 rows from the container's source records.

To access the Data Preview section and explore container data within the platform, follow these steps:

1. **Navigate to Your Datastore**

    Begin by navigating to your datastore within the platform.

* **Select a Specific Container**

    From your datastore, select the specific container whose data you want to preview.

* **Ensure Profiling**

    Before accessing the Data Preview tab, ensure that the container has been profiled. If not, run a profile operation on the container. This operation gathers essential information about the table structure, such as column types and field names. Without profiling, the Data Preview section will display no data.

* **Access Data Preview Tab**

    Once the container is profiled, navigate to the Data Preview tab within the specific container.

    ![Screenshot](../assets/container/data-preview/data-preview-tab-light.png#only-light){: style="width:640px"}
    ![Screenshot](../assets/container/data-preview/data-preview-tab-dark.png#only-dark){: style="width:640px"}

## Explore Data Preview Features
In the Data Preview tab, users can access various features to interact with the data:

### Data Display

The primary function of the Data Preview tab is to present users with a preview of container data. This preview includes up to 100 rows from the container's source, providing users with a quick glimpse into the dataset's contents.

![Screenshot](../assets/container/data-preview/data-display-2-light.png#only-light)
![Screenshot](../assets/container/data-preview/data-display-2-dark.png#only-dark)

### UI Caching

Upon initial access, data in the Data Preview section may not be cached, resulting in varying load times depending on the underlying data store technology (e.g., DFS or JDBC) and whether the warehouse is serverless. Subsequent access will display cached data, improving performance and reducing load times.

#### Last Refreshed Information

The Data Preview section displays information about when the data was last refreshed, providing users with transparency regarding the freshness of the displayed data.

![Screenshot](../assets/container/data-preview/last-refreshed-light.png#only-light)
![Screenshot](../assets/container/data-preview/last-refreshed-dark.png#only-dark)

### Filter Input and Refresh

To enable users to focus on specific subsets of data, the Data Preview tab incorporates filter functionality. Users can apply filter clauses to the displayed data, refining the rows based on specific criteria. This feature enhances data analysis capabilities and allows for more targeted insights.

Utilize the filter input to refine the displayed rows based on specific criteria and `Refresh` the data to ensure you are viewing the latest information.

![Screenshot](../assets/container/data-preview/filter-refresh-2-light.png#only-light)
![Screenshot](../assets/container/data-preview/filter-refresh-2-dark.png#only-dark)

#### Profile Operation Changes

After performing a profile operation that adds additional columns to the data table, users must perform a new refresh to view these changes reflected in the Data Preview section. This ensures that users have access to the most up-to-date and comprehensive dataset for analysis.

### Select Specific Fields

Choose specific fields to display, focusing on relevant data for analysis.

![Screenshot](../assets/container/data-preview/fields-to-show-light.png#only-light){: style="width:540px"}
![Screenshot](../assets/container/data-preview/fields-to-show-dark.png#only-dark){: style="width:540px"}

### Download Records

Download the data for further analysis or external use.

![Screenshot](../assets/container/data-preview/download-source-records-light.png#only-light){: style="width:440px"}
![Screenshot](../assets/container/data-preview/download-source-records-dark.png#only-dark){: style="width:440px"}

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
