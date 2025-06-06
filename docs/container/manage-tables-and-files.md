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

## Settings For JDBC Table

Settings allow you to edit how data is processed and analyzed for a specific table in your connected source datastore. This includes selecting fields for incremental and partitioning strategies, grouping data, excluding certain fields from scans, and adjusting general behaviors.

**Step 1:** Click on the vertical ellipse next to the table of your choice and select **Settings** from the dropdown list.

![vertical-setting](../assets/container/manage-tables-files/setting-light-4.png#only-light)
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

## Settings For DFS Files Pattern

Settings allow you to edit how data is processed and analyzed for a specific file patterns in your connected source datastore. This includes selecting fields for incremental and partitioning strategies, grouping data, excluding certain fields from scans, and adjusting general behaviors.

**Step 1:** Click on the vertical ellipse next to the file pattern of your choice and select **Settings** from the dropdown list.

![vertical-setting](../assets/container/manage-tables-files/setting-light-44.png#only-light)
![vertical-setting](../assets/container/manage-tables-files/setting-dark-44.png#only-dark)

A modal window will appear for **“File Pattern Settings”**.

![table-setting](../assets/container/manage-tables-files/table-settings-light-55.png#only-light)
![table-setting](../assets/container/manage-tables-files/table-settings-dark-55.png#only-dark)

**Step 2:** Modify the table setting based on:

- Group Criteria

- Excluding

- General

### Group Criteria

**Group Criteria** allow you to organize data into specific groups for more precise analysis. By grouping fields, you can gain better insights and enhance the accuracy of your profiling. 

![group-criteria](../assets/container/manage-tables-files/group-light-99.png#only-light)
![group-criteria](../assets/container/manage-tables-files/group-dark-99.png#only-dark)

For information about **Group Criteria**, you can refer to the documentation on [Grouping.](../container/overview-of-grouping.md)

### Excluding

**Excluding** allows you to choose specific fields from a file pattern that you want to exclude from data checks. This helps focus on the fields that matter most for validation while ignoring others that are not relevant to the current analysis.

![excluding-field](../assets/container/manage-tables-files/excluding-light-100.png#only-light)
![excluding-field](../assets/container/manage-tables-files/excluding-dark-100.png#only-dark)

For information about **Excluding**, you can refer to the documentation on [Excluding Settings.](../container/overview-of-infer-data-type.md#excluding-fields)

### General

You can control how file patterns behave by checking or unchecking options to make data processing easier and more consistent. These settings help the system automatically adjust file structures for better integration and analysis.

![general-field](../assets/container/manage-tables-files/general-light-111.png#only-light)
![general-field](../assets/container/manage-tables-files/general-dark-111.png#only-dark)

* **Inferring Data Types:** When enabled, the system figures out the correct data type for each field and applies it automatically. This keeps data consistent and reduces errors, saving you time on manual fixes.

![general-field](../assets/container/manage-tables-files/general-light-112.png#only-light)
![general-field](../assets/container/manage-tables-files/general-dark-112.png#only-dark)

* **First Row as Field Names:** Turning this on uses the first row of a file as headers, making it simple to map and organize data in the right format.

![general-field](../assets/container/manage-tables-files/general-light-113.png#only-light)
![general-field](../assets/container/manage-tables-files/general-dark-113.png#only-dark)

* **Treating Empty Values as Nulls:** The Treat empty values as null setting controls how empty fields in files like Excel and CSV are handled. If enabled (true), empty fields are treated as NULL (missing data). If disabled (false), they are stored as empty strings (""), meaning the field exists but is blank. This affects reporting, calculations, and data processing, as NULL values are ignored while empty strings may still be counted.

![general-field](../assets/container/manage-tables-files/general-light-114.png#only-light)
![general-field](../assets/container/manage-tables-files/general-dark-114.png#only-dark)

**Step 3:** Once you have configured the file pattern settings, click on the **Save** button.

![save-button](../assets/container/manage-tables-files/save-light-122.png#only-light)
![save-button](../assets/container/manage-tables-files/save-dark-12.png#only-dark)

After clicking on the **Save** button, your table is successfully updated and a success flash message will appear stating **"File Pattern has been successfully updated"**.

![flash-message](../assets/container/manage-tables-files/success-light-133.png#only-light)
![flash-message](../assets/container/manage-tables-files/success-dark-133.png#only-dark)

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

**Step 2:** Check the "**Volume Tracking**" to enable trend analysis and anomaly detection in data volumes over time and check the "**Freshness Tracking**" to ensure data timeliness and to identify pipeline delays.

**Volume Tracking** monitors and records daily volume metrics for this data asset. This feature enables trend analysis and anomaly detection in data volumes over time. **Freshness Tracking** measures and records the last time data was added or updated in the data asset. This feature helps ensure data timeliness and identifies pipeline delays.

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

A modal window will appear with the **Export Operation** setting.

![observability-window](../assets/container/manage-tables-files/export-light-24.png#only-light)
![observability-window](../assets/container/manage-tables-files/export-dark-24.png#only-dark)

For the next steps, detailed information on the export operation is available in the [Export Operation](https://userguide.qualytics.io/container/export-operation/) section of the documentation.

## Materialize

**Materialize Operation** captures snapshots of selected containers from a source datastore and exports them to an enrichment datastore for seamless data loading. Users can run it instantly or schedule it at set intervals, ensuring structured data is readily available for analysis and integration.

**Step 1:** Select the tables in your JDBC datastore that you would like to capture and export containers for the Materialize Operation, then click on **Materialize**.

![materialize-button](../assets/container/manage-tables-files/materialize-light-24.png#only-light)
![materialize-button](../assets/container/manage-tables-files/materialize-dark-24.png#only-dark)

A modal window will appear with the **Materialize Operation** setting.

![observability-materialize](../assets/container/manage-tables-files/materialize-light-30.png#only-light)
![observability-materialize](../assets/container/manage-tables-files/materialize-dark-30.png#only-dark)

For the next steps, detailed information on the materialize operation is available in the [Materialize Operation](https://userguide.qualytics.io/container/materialize-operation/) section of the documentation.

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

## Mark Tables & Files as Favorite

Marking a tables and files as a favorite allows you to quickly access important items. This feature helps you prioritize and manage the tables and files you use frequently, making data management more efficient.

**Step 1**: Locate the table and file you want to mark as a favorite and click on the bookmark icon to mark the table and file as a favorite.

![mark-fav](../assets/container/manage-tables-files/mark-fav-light-28.png#only-light)
![mark-fav](../assets/container/manage-tables-files/mark-fav-dark-28.png#only-dark)

After Clicking on the bookmark icon your table and file is successfully marked as a favorite and a success flash message will appear stating “The Table has been favorited”.

![fav-msg](../assets/container/manage-tables-files/fav-msg-light-29.png#only-light)
![fav-msg](../assets/container/manage-tables-files/fav-msg-dark-29.png#only-dark)

**Step 2**: To unmark a tables and files, simply click on the bookmark icon of the marked tables and files. This will remove it from your favorites.

![unmark-fav](../assets/container/manage-tables-files/unmark-fav-light-30.png#only-light)
![unmark-fav](../assets/container/manage-tables-files/unmark-fav-dark-30.png#only-dark)