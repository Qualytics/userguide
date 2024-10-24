# Manage Tables & Files

Managing **JDBC “tables”** and **DFS “files”** in a connected **source datastore** allows you to perform actions such as adding validation checks, running scans, monitoring data changes, exporting, or deleting them. For JDBC tables, you can also handle metadata, configure partitions, and manage incremental data for optimized processing. However, for DFS datastores, the default incremental field is the file’s last modified timestamp, and users cannot configure incremental or partition fields manually. 

Let’s get started 🚀

### Navigation

**Step 1:** Log in to your Qualytics account and select the source datastore (JDBC or DFS) from the left menu that you want to manage.

![select-datastore](../assets/container/manage-tables-files/select-light-1.png#only-light)
![select-datastore](../assets/container/manage-tables-files/select-dark-1.png#only-dark)

**Step 2:** Select Tables (if JDBC datastore is connected) or File Patterns (if DFS datastore is connected) from the Navigation tab on the top. 

![select-table](../assets/container/manage-tables-files/table-light-2.png#only-light)
![select-table](../assets/container/manage-tables-files/table-dark-2.png#only-dark)

**Step 3:** You will view the full list of tables or files belonging to the selected source datastore.

![table-list](../assets/container/manage-tables-files/table-light-3.png#only-light)
![table-list](../assets/container/manage-tables-files/table-dark-3.png#only-dark)

## Settings

Settings allow you to edit how data is processed and analyzed for a specific table in your connected source datastore. This includes selecting fields for incremental and partitioning strategies, grouping data, excluding certain fields from scans, and adjusting general behaviors.

**Step 1:** Click on the vertical ellipse next to the table of your choice and select **Settings** from the dropdown list.

![verical-setting](../assets/container/manage-tables-files/setting-light-4.png#only-light)
![vertical-setting](../assets/container/manage-tables-files/setting-dark-4.png#only-dark)

A modal window will appear for **“Table Settings”**.

![table-setting](../assets/container/manage-tables-files/table-settings-light-5.png#only-light)
![table-setting](../assets/container/manage-tables-files/table-settings-dark-5.png#only-dark)

**Step 2:** Modify the table setting based on:

- Identifiers

- Group Criteria

- Excluding

- General

### Identifiers

An **Identifier** is a field that can be used to help load the desired data from a Table in support of analysis. For more details about identifiers, you can refer to the documentation on [Identifiers.](https://userguide.qualytics.io/container/overview-of-identifiers/)

#### Incremental Strategy

This is crucial for tracking changes at the row level within tables. This approach is essential for efficient data processing, as it is specifically used to track which records have already been scanned. This allows for scan operations to focus exclusively on new records that have not been previously scanned, thereby optimizing the scanning process and ensuring that only the most recent and relevant data is analyzed.

!!! note
    If you have connected a DFS datastore, no manual setup is needed for the incremental strategy, the system automatically tracks and processes the latest data changes.

![incremental-strategy](../assets/container/manage-tables-files/incremental-light-6.png#only-light)
![incremental-strategy](../assets/container/manage-tables-files/incremental-dark-6.png#only-dark)

For information about incremental strategy, you can refer to the [Incremental Strategy](https://userguide.qualytics.io/container/overview-of-identifiers/#partition-field) section in the Identifiers documentation.   
                                                                                    
#### Incremental Field

**Incremental Field** lets you select a field that tracks changes in your data. This ensures only new or updated records are scanned, improving efficiency and reducing unnecessary processing.

![incremental-field](../assets/container/manage-tables-files/field-light-7.png#only-light)
![incremental-field](../assets/container/manage-tables-files/field-dark-7.png#only-dark)

#### Partition Field

**Partition Field** is used to divide the data in a table into distinct segments, or dataframes. These partitions allow for parallel analysis, improving efficiency and performance. By splitting the data, each partition can be processed independently. This approach helps optimize large-scale data operations.

![partition-field](../assets/container/manage-tables-files/partition-light-8.png#only-light)
![partition-field](../assets/container/manage-tables-files/partition-dark-8.png#only-dark)

For information about **Partition Field**, you can refer to the [Partition Field](https://userguide.qualytics.io/container/overview-of-identifiers/#partition-field) section in the Identifiers documentation. 

### Group Criteria

**Group Criteria** allow you to organize data into specific groups for more precise analysis. By grouping fields, you can gain better insights and enhance the accuracy of your profiling. 

![group-criteria](../assets/container/manage-tables-files/group-light-9.png#only-light)
![group-criteria](../assets/container/manage-tables-files/group-dark-9.png#only-dark)

For information about **Group Criteria**, you can refer to the documentation on [Grouping.](https://userguide.qualytics.io/container/overview-of-grouping/)

### Excluding

**Excluding** allows you to choose specific fields from a table that you want to exclude from data checks. This helps focus on the fields that matter most for validation while ignoring others that are not relevant to the current analysis.

![excluding-field](../assets/container/manage-tables-files/excluding-light-10.png#only-light)
![excluding-field](../assets/container/manage-tables-files/excluding-dark-10.png#only-dark)

For information about **Excluding**, you can refer to the documentation on [Excluding Settings.](https://userguide.qualytics.io/container/overview-of-infer-data-type/#excluded-fields)

### General

You can control the default behavior of the specific table by checking or unchecking the option to infer the data type for each field. When checked, the system will automatically determine and cast the data types as needed for accurate data processing.

![general-field](../assets/container/manage-tables-files/general-light-11.png#only-light)
![general-field](../assets/container/manage-tables-files/general-dark-11.png#only-dark)

For information about **General**, you can refer to the documentation on [General Settings.](https://userguide.qualytics.io/container/overview-of-infer-data-type/)

**Step 3:** Once you have configured the table settings, click on the **Save** button.

![save-button](../assets/container/manage-tables-files/save-light-12.png#only-light)
![save-button](../assets/container/manage-tables-files/save-dark-12.png#only-dark)

After clicking on the **Save** button, your table is successfully updated and a success flash message will appear stating **"Table has been successfully updated"**.

![flash-message](../assets/container/manage-tables-files/success-light-13.png#only-light)
![flash-message](../assets/container/manage-tables-files/success-dark-13.png#only-dark)

## Add Checks

**Add Check** allows you to create rules to validate the data within a particular table. You can choose the type of rule, link it directly to the selected table, and add descriptions or tags. This ensures that the table's data remains accurate and compliant with the required standards.

**Step 1:** Click on the vertical ellipse next to the table name and select **Add Checks**.

![add-checks](../assets/container/manage-tables-files/check-light-14.png#only-light)
![add-checks](../assets/container/manage-tables-files/check-dark-14.png#only-dark)

A modal window will appear to add checks against the selected table.

![check-window](../assets/container/manage-tables-files/check-light-15.png#only-light)
![check-window](../assets/container/manage-tables-files/check-dark-15.png#only-dark)

To understand how to add checks, you can follow the remaining steps from the documentation [Checks Template.](https://userguide.qualytics.io/checks/checks-template/)

## Run

Execute various operations like profiling or scanning your table or file. It helps validate data quality and ensures that the table meets the defined checks and rules, providing insights into any anomalies or data issues that need attention.

**Step 1:** Click on the vertical ellipse next to the table name and select **Run**.

![run-button](../assets/container/manage-tables-files/run-light-16.png#only-light)
![run-button](../assets/container/manage-tables-files/run-dark-16.png#only-dark)

Under **Run**, choose the type of operation you want to perform:

- **Profile**: To collect metadata and profile the table's contents.

- **Scan**: To validate the data against defined rules and checks.

![run-option](../assets/container/manage-tables-files/run-light-17.png#only-light)
![run-option](../assets/container/manage-tables-files/run-dark-17.png#only-dark)

To understand how a profile operation is performed, you can follow the remaining steps from the documentation [Profile Operation.](https://userguide.qualytics.io/source-datastore/profile/#configuration).

To understand how a scan operation is performed, you can follow the remaining steps from the documentation [Scan Operation.](https://userguide.qualytics.io/source-datastore/scan/#configuration)

## Observability Settings

Observability helps you track and monitor data performance in your connected source datastore’s tables and files. It provides insights into data volume, detects anomalies, and ensures smooth data processing by identifying potential issues early. This makes it easier to manage and maintain data quality over time.

**Step 1:** Select the table in your JDBC datastore that you would like to monitor, then click on **Observability.**  

![observability-setting](../assets/container/manage-tables-files/observability-light-18.png#only-light)
![observability-setting](../assets/container/manage-tables-files/observability-dark-18.png#only-dark)

A modal window **“Observability Settings”** will appear. Here you can view the details of the table and datastore where actions have been applied.

![observability-setting](../assets/container/manage-tables-files/observability-light-19.png#only-light)
![observability-setting](../assets/container/manage-tables-files/observability-dark-19.png#only-dark)

**Step 2:** Check the "**Allow Tracking**" to enable daily volumetric measurement tracking for the data asset.

You can enable or disable volumetric tracking by checking or unchecking the "**Allow Tracking**" option. This feature monitors and records the daily volume of data in the selected table. When enabled, it helps track how much data is being processed and stored over time, providing valuable insights into the data asset's growth and usage.

![allow-tracking](../assets/container/manage-tables-files/tracking-light-20.png#only-light)
![allow-tracking](../assets/container/manage-tables-files/tracking-dark-20.png#only-dark)

**Step 3:** Click on the **Save** button.

![save-button](../assets/container/manage-tables-files/save-light-21.png#only-light)
![save-button](../assets/container/manage-tables-files/save-dark-21.png#only-dark)

After clicking on the Save button, a success flash message will appear stating **"Profile has been successfully updated"**.

![success-msg](../assets/container/manage-tables-files/success-light-22.png#only-light)
![success-msg](../assets/container/manage-tables-files/success-dark-22.png#only-dark)

## Export

**Export feature** lets you capture changes in your tables. You can export metadata for Quality Checks, Field Profiles, and Anomalies from selected tables to an enrichment datastore. This helps you analyze data trends, find issues, and make better decisions based on the table data.

**Step 1:** Select the tables in your JDBC datastore that you would like to export, then click on **Export**.

![export-button](../assets/container/manage-tables-files/export-light-23.png#only-light)
![export-button](../assets/container/manage-tables-files/export-dark-23.png#only-dark)

A modal window will appear with the **Export Metadata** setting.

![observability-window](../assets/container/manage-tables-files/export-light-24.png#only-light)
![observability-window](../assets/container/manage-tables-files/export-dark-24.png#only-dark)

For the next steps, detailed information on the export metadata is available in the [Export Metadata](https://userguide.qualytics.io/container/export-metadata/) section of the documentation.

## Delete

**Delete** allows you to remove a table from the connected source datastore. While the table and its associated data will be deleted, it is not permanent, as the table can be recreated if you run a catalog with the "recreate" option. 

!!! note
    Deleting a table is a reversible action if a catalog with the "recreate" option is run later. 

**Step 1:** Select the tables in your connected source datastore that you would like to delete, then click on **Delete**.

![delete-button](../assets/container/manage-tables-files/delete-light-25.png#only-light)
![delete-button](../assets/container/manage-tables-files/delete-dark-25.png#only-dark)

**Step 2:** A confirmation modal window will appear, click on the Delete button to remove the table from the system.

![delete-window](../assets/container/manage-tables-files/delete-btn-light-26.png#only-light)
![delete-window](../assets/container/manage-tables-files/delete-btn-dark-26.png#only-dark)

**Step 3:** After clicking on the delete button, your table is successfully deleted and a success flash message will appear saying **"Profile has been successfully deleted"**

![success-message](../assets/container/manage-tables-files/success-light-27.png#only-light)
![success-message](../assets/container/manage-tables-files/success-dark-27.png#only-dark)

