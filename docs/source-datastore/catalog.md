# Catalog Operation

A Catalog Operation imports named data collections like tables, views, and files into a Source Datastore. It identifies incremental fields for incremental scans, and offers options to recreate or delete these containers, streamlining data management and enhancing data discovery.

Let's get started 🚀

## Key Components

### Incremental Identifier

An [incremental identifier](https://userguide.qualytics.io/glossary/#incremental-identifier) is essential for supporting incremental scan operations, as it allows the system to detect changes since the last operation.

### Partition Identifier

For large data containers or partitions, a [partition identifier](https://userguide.qualytics.io/glossary/#partition-identifier) is necessary to process data efficiently. In DFS datastores, the default fields for both incremental and partition identifiers are set by the last-modified timestamp. If a partition identifier is missing, the system uses repeatable ordering candidates (order-by fields) to process containers, although this method is less efficient for handling large datasets with many rows.

!!! info
    Attribute Overrides: After the profile operation, the qualytics engine might automatically update the containers to have partition fields and incremental fields. Those "attributes" can be manually overridden.

!!! note
    Advanced users should be able to override these auto-detected selections and overwritten options should persist through subsequent Catalog Operations.

## Initialization & Operation Options

### Automatic Catalog Operation

While adding the datastore, tick the Initiate Cataloging checkbox to automatically perform catalog operation on the configured source datastore.

![test-connection](../assets/catalog-operations/test-connection-light.png#only-light)
![test-connection](../assets/catalog-operations/test-connection-dark.png#only-dark)

With the automatic cataloging option turned on, you will be redirected to the datastore details page once the datastore (whether JDBC or DFS) is successfully added. You will observe the cataloging operation running automatically with the following default options:

-   Prune: Disabled ❌  

-   Recreate: Disabled ❌  

-   Include: Tables and views ✔️

![catalog](../assets/catalog-operations/catalog-light.png#only-light)
![catalog](../assets/catalog-operations/catalog-dark.png#only-dark)

### Manual Catalog Operation

If automatic cataloging is disabled while adding the datastore, users can initiate the catalog operation manually by selecting preferred options. Manual catalog operation offers the users the flexibility to set up custom catalog configurations like syncing only tables or views.

**Step 1**: Select a source datastore from the side menu on which you would like to perform the catalog operation.

![add-source-datadtore](../assets/catalog-operations/add-source-datastore-light.png#only-light)
![add-source-datadtore](../assets/catalog-operations/add-source-datastore-dark.png#only-dark)

**Step 2**: Clicking on your preferred datastore will navigate you to the datastore details page. Within the overview tab (default view), click on the **Run** button under **Catalog** to initiate the catalog operation.

![run-catalog](../assets/catalog-operations/run-catalog-light.png#only-light)
![run-catalog](../assets/catalog-operations/run-catalog-dark.png#only-dark)

A modal window will display **Operation Triggered** and you will be notified once the catalog operation is completed.  

!!! note
    You will receive a notification when the catalog operation is completed.

![opertaion-triggered](../assets/catalog-operations/operation-triggred-light.png#only-light)
![opertaion-triggered](../assets/catalog-operations/operation-triggred-dark.png#only-dark)

**Step 3**: Close the **Success** modal window and you will observe in the UI that the Catalog operation has been completed and it has gathered the data structures, file patterns, and corresponding metadata from your configured datastore.  
  
![file-pattern](../assets/catalog-operations/file-pattern-light.png#only-light)
![file-pattern](../assets/catalog-operations/file-pattern-dark.png#only-dark)

Users might encounter a warning error if the schema of the datastore is empty or if the specified user for logging does not have the necessary permissions to read the objects. This ensures that proper access controls are in place and that the data structure is correctly defined.

![catalog-aborted](../assets/catalog-operations/catalog-aborted-light.png#only-light)
![catalog-aborted](../assets/catalog-operations/catalog-aborted-dark.png#only-dark)

#### Custom Catalog Configuration

The catalog operation can be custom-configured with the following options:  

-   **Prune**: Remove any existing named collections that no longer appear in the datastore

-   **Recreate**: Restore any previously removed named collection that does currently appear in the database

-   **Include**: Include Tables and Views

**Step 1**: Click on the **Run** button from the datastore details page (top-right corner) and select **Catalog** from the dropdown list.

![run-dropdown](../assets/catalog-operations/run-dropdown-light.png#only-light)
![run-dropdown](../assets/catalog-operations/run-dropdown-dark.png#only-dark)

**Step 2:** When configuring the catalog operation settings, you have two options to tune: 

- **Prune:** This option allows the removal of any named collections (tables, views, files, etc.) that no longer exist in the datastore. This ensures that outdated or obsolete collections are not included in future operations, keeping the datastore clean and relevant.

- **Recreate**: This option enables the recreation of any named collections that have been previously deleted in Qualytics. It is useful for restoring collections that may have been removed accidentally or need to be brought back for analysis.

![options](../assets/catalog-operations/options-light.png#only-light)
![options](../assets/catalog-operations/options-dark.png#only-dark)

**Step 3:** The user can choose whether to include only tables, only views, or both in the catalog operation. This flexibility allows for more targeted metadata analysis based on the specific needs of the data management task.

![include](../assets/catalog-operations/include-light.png#only-light)
![include](../assets/catalog-operations/include-dark.png#only-dark)

### Run Instantly

Click on the “**Run Now**” button, and perform the catalog operation immediately. 

![run](../assets/catalog-operations/run-light.png#only-light)
![run](../assets/catalog-operations/run-dark.png#only-dark)

After clicking **Run Now**, a confirmation message appears stating **"Operation Triggered"**.

![operation-triggered](../assets/catalog-operations/operation-triggered-light.png#only-light)
![operation-triggered](../assets/catalog-operations/operation-triggered-dark.png#only-dark)

### Schedule

**Step 1:** Click on the **“Schedule”** button to configure the available schedule options in the catalog operation.

![schedule-catalog](../assets/catalog-operations/schedule-catalog-light.png#only-light)
![schedule-catalog](../assets/catalog-operations/schedule-catalog-dark.png#only-dark)

**Step 2:** Set the scheduling preferences for the catalog operation. 

**1. Hourly:** This option allows you to schedule the catalog operation to run every hour at a specified minute. You can define the frequency in hours and the exact minute within the hour the cataloging should start. Example: If set to "Every 1 hour(s) on minute 0," the catalog operation will run every hour at the top of the hour (e.g., 1:00, 2:00, 3:00). 

![hourly](../assets/catalog-operations/hourly-light.png#only-light)
![hourly](../assets/catalog-operations/hourly-dark.png#only-dark)

**2. Daily:** This option schedules the catalog operation to run once every day at a specific time. You specify the number of days between scans and the exact time of day in UTC. Example: If set to "Every 1 day(s) at 00:00 UTC," the scan will run every day at midnight UTC. 

![daily](../assets/catalog-operations/daily-light.png#only-light)
![daily](../assets/catalog-operations/daily-dark.png#only-dark)

**3. Weekly:** This option schedules the catalog operation to run on specific days of the week at a set time. You select the days of the week and the exact time of day in UTC for the catalog operation to run. Example: If configured to run on "Sunday" and "Friday" at 00:00 UTC, the scan will execute at midnight UTC on these days. 

![weekly](../assets/catalog-operations/weekly-light.png#only-light)
![weekly](../assets/catalog-operations/weekly-dark.png#only-dark)

**4. Monthly:** This option schedules the catalog operation to run once a month on a specific day at a set time. You specify the day of the month and the time of day in UTC. If set to "On the 1st day of every 1 month(s), at 00:00 UTC," the catalog operation will run on the first day of each month at midnight UTC. 

![monthly](../assets/catalog-operations/monthly-light.png#only-light)
![monthly](../assets/catalog-operations/monthly-dark.png#only-dark)

**5. Advanced:** The advanced section for scheduling operations allows users to set up more complex and custom scheduling using Cron expressions. This option is particularly useful for defining specific times and intervals for catalog operations with precision. 

Cron expressions are a powerful and flexible way to schedule tasks. They use a syntax that specifies the exact timing of the task based on five fields:

* Minute (0 - 59)  
* Hour (0 - 23)  
* Day of the month (1 - 31)  
* Month (1 - 12)  
* Day of the week (0 - 6) (Sunday to Saturday)

Each field can be defined using specific values, ranges, or special characters to create the desired schedule.

**Example:** For instance, the Cron expression `0 0 * * *`** schedules the catalog operation to run at midnight (00:00) every day. Here’s a breakdown of this expression:

* 0 (Minute) - The task will run at the 0th minute.  
* 0 (Hour) - The task will run at the 0th hour (midnight).  
* *(Day of the month) - The task will run every day of the month.  
* *(Month) - The task will run every month.  
* *(Day of the week) - The task will run every day of the week.

Users can define other specific schedules by adjusting the Cron expression. For example:

* 0 12 * * 1-5 - Runs at 12:00 PM from Monday to Friday.  
* 30 14 1 * * - Runs at 2:30 PM on the first day of every month.  
* 0 22 * * 6 - Runs at 10:00 PM every Saturday.

To define a custom schedule, enter the appropriate Cron expression in the **"Custom Cron Schedule (UTC)"** field before specifying the schedule name. This will allow for precise control over the timing of the catalog operation, ensuring it runs exactly when needed according to your specific requirements.

![advanced](../assets/catalog-operations/advanced-light.png#only-light)
![advanced](../assets/catalog-operations/advanced-dark.png#only-dark)

**Step 3**: Define the **“Schedule Name”** to identify the scheduled operation at the running time.

![schedule-name](../assets/catalog-operations/schedule-name-light.png#only-light)
![schedule-name](../assets/catalog-operations/schedule-name-dark.png#only-dark)

**Step 4:** Click on the **“Schedule”** button to activate your catalog operation schedule. 

![schedule](../assets/catalog-operations/schedule-light.png#only-light)
![schedule](../assets/catalog-operations/schedule-dark.png#only-dark)

After clicking **Schedule**, a confirmation message appears stating **"Operation Scheduled"**.

![operation-scheduled](../assets/catalog-operations/operation-scheduled-light.png#only-light)
![operation-scheduled](../assets/catalog-operations/operation-scheduled-dark.png#only-dark)

Once the catalog operation is triggered, your view will be automatically switched to the Activity tab, allowing you to explore post-operation details on your ongoing/completed catalog operation.

![completed-catalog](../assets/catalog-operations/completed-catalog-light.png#only-light)
![completed-catalog](../assets/catalog-operations/completed-catalog-dark.png#only-dark)

## Operations Insights

When the catalog operation is completed, you will receive the notification and can navigate to the **Activity tab** for the datastore on which you triggered the Catalog Operation and learn about the operation results.

### Top Panel

**1. Runs (Default View)**: Provides insights into the operations that have been performed.

**2. Search**: Search any operation (including catalog) by entering the operation ID

**3. Sort by**: Organize the list of operations based on the **Created Date** or the **Duration**.

**4. Filter**: Narrow down the list of operations based on:

-   Operation Type

-   Operation Status

-   Table

![activity](../assets/catalog-operations/activity-light.png#only-light)
![activity](../assets/catalog-operations/activity-dark.png#only-dark)

### Activity Heatmap

The activity heatmap shown in the snippet below represents activity levels over a period, with each square indicating a day and the color intensity representing the number of operations or activities on that day. It is useful in tracking the number of operations performed on each day within a specific timeframe.  

!!! tip
    You can click on any of the squares from the Activity Heatmap to filter operations

![activity-calender](../assets/catalog-operations/activity-calender-light.png#only-light)
![activity-calender](../assets/catalog-operations/activity-calender-dark.png#only-dark)

### Operation Detail

#### Running

This status indicates that the catalog operation is still running at the moment and is yet to be completed. A catalog operation having a **running** status reflects the following details and actions:

| Parameter      | Interpretation |
|----------------|---------------------------------------------------------------|
| Operation ID   | Unique identifier |
| Operation Type | Type of operation performed (catalog, profile, or scan) |
| Timestamp      | Timestamp when the operation was started |
| Progress Bar   | The progress of the operation |
| Triggered By   | The author who triggered the operation |
| Schedule       | Whether the operation was scheduled or not |
| Prune          | Indicates whether Prune was enabled or disabled in the operation |
| Recreate       | Indicates whether Recreate was enabled or disabled in the operation |
| Table          | Indicates whether the **Table** was included in the operation or not |
| Views          | Indicates whether the **Views** was included in the operation or not |
| Abort          | Click on the **Abort** button to stop the catalog operation |

![running-catalog](../assets/catalog-operations/running-catalog-light.png#only-light)
![running-catalog](../assets/catalog-operations/running-catalog-dark.png#only-dark)

#### Aborted

This status indicates that the catalog operation was manually stopped before it could be completed. A catalog operation having an **aborted** status reflects the following details and actions:

| Parameter      | Interpretation |
|----------------|---------------------------------------------------------------------|
| Operation ID   | Unique identifier |
| Operation Type | Type of operation performed (catalog, profile, or scan) |
| Timestamp      | Timestamp when the operation was started |
| Progress Bar   | The progress of the  operation |
| Triggered By   | The author who triggered the operation |
| Schedule       | Whether the operation was scheduled or not |
| Prune          | Indicates whether Prune was enabled or disabled in the operation |
| Recreate       | Indicates whether Recreate was enabled or disabled in the operation |
| Table          | Indicates whether the **Table** was included in the operation or not |
| Views          | Indicates whether the **Views** was included in the operation or not |
| Resume         | Click on the **Resume** button to continue a previously aborted catalog operation from where it left off |
| Rerun          | Click on the **Rerun** button to initiate the catalog operation from the beginning, ignoring any previous attempts |
| Delete         | Click on the **Delete** button to remove the record of the catalog operation from the list |

![aborted](../assets/catalog-operations/aborted-light.png#only-light)
![aborted](../assets/catalog-operations/aborted-dark.png#only-dark)

#### Warning

This status signals that the catalog operation encountered some issues and displays the logs that facilitate improved tracking of the blockers and issue resolution. A catalog operation having a **warning** status reflects the following details and actions:

| Parameter      | Interpretatio  |
|----------------|-------------------------------------------------------------------------|
| Operation ID   | Unique identifier |
| Operation Type | Type of operation performed (catalog, profile, or scan) |
| Timestamp      | Timestamp when the operation was started |
| Progress Bar   | The progress of the operation |
| Triggered By   | The author who triggered the operation |
| Schedule       | Whether the operation was scheduled or not |
| Prune          | Indicates whether Prune was enabled or disabled in the operation |
| Recreate       | Indicates whether Recreate was enabled or disabled in the operation |
| Table          | Indicates whether the **Table** was included in the operation or not |
| Views          | Indicates whether the **Views** was included in the operation or not |
| Rerun          | Click on the **Rerun** button to initiate the catalog operation from the beginning, ignoring any previous attempts |
| Delete         | Click on the **Delete** button to remove the record of the catalog operation from the list |
| Logs           | Logs include error messages, warnings, and other pertinent information that occurred during the execution of the Catalog Operation |

![warning-catalog](../assets/catalog-operations/warning-catalog-light.png#only-light)
![warning-catalog](../assets/catalog-operations/warning-catalog-dark.png#only-dark)

### Success

This status confirms that the catalog operation was completed successfully without any issues. A catalog operation having a **success** status reflects the following details and actions:

| Parameter      | Interpretation |
|----------------|-----------------------------------------------------------------------|
| Operation ID   | Unique identifier |
| Operation Type | Type of operation performed (catalog, profile, or scan) |
| Timestamp      | Timestamp when the operation was started |
| Progress Bar   | The progress of the operation |
| Triggered By   | The author who triggered the operation |
| Schedule       | Whether the operation was scheduled or not |
| Prune          | Indicates whether Prune was enabled or disabled in the operation |
| Recreate       | Indicates whether Recreate was enabled or disabled in the operation |
| Table          | Indicates whether the **Table** was included in the operation or not |
| Views          | Indicates whether the **Views** was included in the operation or not |
| Rerun          | Click on the **Rerun** button to initiate the catalog operation from the beginning, ignoring any previous attempts |
| Delete         | Click on the **Delete** button to remove the record of the catalog operation from the list |

![success-catalog](../assets/catalog-operations/success-catalog-light.png#only-light)
![success-catalog](../assets/catalog-operations/success-catalog-dark.png#only-dark)

## Post-Operation Details

### For JDBC Source Datastores

After the catalog operation is completed on a JDBC source datastore, users can view the following information:

**Container Names**: These are the names of the data collections (e.g., tables, views) identified during the catalog operation.

![container-names](../assets/catalog-operations/container-names-light.png#only-light)
![container-names](../assets/catalog-operations/container-names-dark.png#only-dark)

**Fields for Each Container**: Each container will display its fields or columns, which were detected during the catalog operation.

![connector-field](../assets/catalog-operations/connector-field-light.png#only-light)
![connector-field](../assets/catalog-operations/connector-field-dark.png#only-dark)

**Incremental Identifiers and Partition Fields**: These settings are automatically configured based on the catalog operation. Incremental identifiers help in recognizing changes since the last scan, and partition fields aid in efficient data processing.

**Tree view > Container node > Gear icon > Settings option**

![table-settings](../assets/catalog-operations/table-settings-light.png#only-light)
![table-settings](../assets/catalog-operations/table-settings-dark.png#only-dark)

### For DFS Source Datastores

After the catalog operation is completed on a DFS source datastore, users can view the following information:

-   **Container Names**: Similar to JDBC, these are the data collections identified during the catalog operation.

-   **Fields for Each Container**: Each container will list its fields or metadata detected during the catalog operation.

-   **Directory Tree Traversal**: The catalog operation traverses the directory tree, treating each file with a supported extension as a single-partition container. It reveals metadata such as the relative path, filename, and extension.

-  **Incremental Identifier and Partition Field**: By default, both the incremental identifier and partition field are set to the last-modified timestamp. This ensures efficient incremental scans and data partitioning.

-   **"Globbed" Containers**: Files in the same folder with the same extensions and similar naming formats are grouped into a single container, where each file is treated as a partition. This helps in managing and querying large datasets effectively.

## API Payload Examples

This section provides API payload examples for initiating and checking the running status of a catalog operation. Replace the placeholder values with data specific to your setup.

### Running a Catalog operation

To run a catalog operation, use the API payload example below and replace the placeholder values with your specific values:

**Endpoint (Post)**:  ```/api/operations/run (post)```

```json
{
  "type": "catalog",
  "datastore_id": "datastore-id",
  "prune": false,
  "recreate": false,
  "include": [
    "table",
    "view"
  ]
}
```
### Retrieving Catalog Operation Status

To retrieve the catalog operation status, use the API payload example below and replace the placeholder values with your specific values:

**Endpoint (Get)**:  ```/api/operations/{id} (get)```

```json
{
  "items": [
    {
      "id": 12345,
      "created": "YYYY-MM-DDTHH:MM:SS.ssssssZ",
      "type": "catalog",
      "start_time": "YYYY-MM-DDTHH:MM:SS.ssssssZ",
      "end_time": "YYYY-MM-DDTHH:MM:SS.ssssssZ",
      "result": "success",
      "message": null,
      "triggered_by": "user@example.com",
      "datastore": {
        "id": 54321,
        "name": "Datastore-Sample",
        "store_type": "jdbc",
        "type": "db_type",
        "enrich_only": false,
        "enrich_container_prefix": "_data_prefix",
        "favorite": false
      },
      "schedule": null,
      "include": [
        "table",
        "view"
      ],
      "prune": false,
      "recreate": false
    }
  ],
  "total": 1,
  "page": 1,
  "size": 50,
  "pages": 1
}
```