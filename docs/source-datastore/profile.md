# Profile Operation

The Profile Operation is a comprehensive analysis conducted on every record within all available containers in a datastore. This process is aimed at understanding and improving data quality by generating metadata for each field within the collections of data (like tables or files).

By gathering detailed statistical data and interacting with the Qualytics Inference Engine, the operation not only identifies and evaluates data quality but also suggests and refines checks to ensure ongoing data integrity. Executing Profile Operations periodically helps maintain up-to-date and accurate data quality checks based on the latest data.

This guide explains how to configure the profile operation with available functionalities such as tables, tags, and schedule options.

Let's get started 🚀

## How Profiling Works

### Fields Identification

The initial step involves recognizing and identifying all the fields within each data container. This step is crucial as it lays the foundation for subsequent analysis and profiling.

### Statistical Data Gathering

After identifying the fields, the Profile Operation collects statistical data for each field based on its declared or inferred data type. This data includes essential metrics such as minimum and maximum values, mean, standard deviation, and other relevant statistics. These metrics provide valuable insights into the characteristics and distribution of the data, helping to understand its quality and consistency.

### Metadata Generation

The gathered statistical data is then submitted to the Qualytics Inference Engine. The engine utilizes this data to generate metadata that forms the basis for creating appropriate data quality checks. This metadata is essential for setting up robust quality control mechanisms within the data management system.

### Data Quality Checks

The inferred data quality checks are rigorously tested against the actual source data. This testing phase is critical to fine-tuning the checks to the desired sensitivity levels, ensuring they are neither too strict (causing false positives) nor too lenient (missing errors). By calibrating these checks accurately, the system can maintain high data integrity and reliability.

## Navigation to Profile Operation

**Step 1**: Select a source datastore from the side menu on which you would like to perform the profile operation.

![adding-source-datastore](../assets/profile-operations/adding-source-datastore-light.png#only-light)
![adding-source-datastore](../assets/profile-operations/adding-source-datastore-dark.png#only-dark)
  
**Step 2**: Clicking on your preferred datastore will navigate you to the datastore details page. Within the overview tab (default view), click on the Run button under Profile to initiate the catalog operation.

![profile](../assets/profile-operations/profile-light.png#only-light)
![profile](../assets/profile-operations/profile-dark.png#only-dark)

## Configuration

**Step 1**: Click on the **Run** button to initiate the profile operation.

![run-profile](../assets/profile-operations/run-profile-light.png#only-light)
![run-profile](../assets/profile-operations/run-profile-dark.png#only-dark)
  
!!! note
    You can run Profile Operation anytime to update the inferred data quality checks, automatically based on new data in the Datastore. It is recommended to schedule the profile operations periodically to update inferred rules. More details are discussed in the **Schedule** section below.

**Step 2**: Select tables (in your JDBC datastore) or file patterns (in your DFS datastore) and tags you would like to be profiled.

**1. All Tables/File Patterns**

This option includes all tables or files currently available in the datastore for profiling. Selecting this will profile every table within the source datastore without the need for further selection.

![profile-operation-all](../assets/profile-operations/profile-operation-all-light.png#only-light)
![profile-operation-all](../assets/profile-operations/profile-operation-all-dark.png#only-dark)

**2. Specific**

This option allows users to manually select individual tables or files for profiling. It provides the flexibility to focus on particular tables of interest, which can be useful if the user is only interested in a subset of the available data.

![profile-operation-specific](../assets/profile-operations/profile-operation-specific-light.png#only-light)
![profile-operation-specific](../assets/profile-operations/profile-operation-specific-dark.png#only-dark)

**3. Tag**

This option automatically profiles tables associated with selected tags. Tags are used to categorize tables, and by selecting a specific tag, all tables associated with that tag will be profiled. This option helps in managing and profiling grouped data efficiently.

![profile-operation-tag](../assets/profile-operations/profile-operation-tag-light.png#only-light)
![profile-operation-tag](../assets/profile-operations/profile-operation-tag-dark.png#only-dark)
  
**Step 3**: After making the relevant selections, click on the **Next** button to configure the **Operation Settings**.

![profile-operation-next](../assets/profile-operations/profile-operation-next-light.png#only-light)
![profile-operation-next](../assets/profile-operations/profile-operation-next-dark.png#only-dark)
  
**Step 4**: Configure the following three operations settings:

**1. Infer data quality checks**: When enabled, this option allows Qualytics to automatically generate and update data quality checks based on the profile results. This feature leverages the Qualytics Inference Engine to create appropriate checks that ensure data integrity and quality.  
  
![inference-engine](../assets/profile-operations/inference-engine-light.png#only-light)
![inference-engine](../assets/profile-operations/inference-engine-dark.png#only-dark)
  
**2. Starting Threshold**: This setting allows users to specify a minimum incremental identifier value to set a starting point for the profile operation. It helps in filtering data from a specific point in time or a particular batch value.  

- Greater Than Time: Users can select a timestamp in UTC to start profiling data from a specific time onwards. This is useful for focusing on recent data or data changes since a particular time.  

- Greater Than Batch: Users can enter a batch value to start profiling from a specific batch. This option is helpful for scenarios where data is processed in batches, allowing the user to profile data from a specific batch number onwards.

!!! note 
    The starting threshold i.e. **Greater Than Time** and **Greater Than Batch** are applicable only to the tables or files with an incremental timestamp strategy.

![starting-threshold](../assets/profile-operations/starting-threshold-light.png#only-light)
![starting-threshold](../assets/profile-operations/starting-threshold-dark.png#only-dark)

**3. Record Limit**: Define the maximum number of records to be profiled: This slider allows users to set a limit on the number of records to be profiled per table. The range can be adjusted from 1 million to all available records. This setting helps in controlling the scope of the profiling operation, particularly for large datasets, by capping the number of records to analyze.

![record-limit](../assets/profile-operations/record-limit-light.png#only-light)
![record-limit](../assets/profile-operations/record-limit-dark.png#only-dark)
  
## Run Instantly

Click on the **Run Now** button, and perform the profile operation immediately.

![run-now](../assets/profile-operations/run-now-light.png#only-light)
![run-now](../assets/profile-operations/run-now-dark.png#only-dark)
  
### Schedule

**Step 1**: Click on the **Schedule** button to configure the available schedule options in the profile operation.

![schedule](../assets/profile-operations/schedule-light.png#only-light)
![schedule](../assets/profile-operations/schedule-dark.png#only-dark)
  
**Step 2**: Set the scheduling preferences for the profile operation.

**1. Hourly**: This option allows you to schedule the profile operation to run every hour at a specified minute. You can define the frequency in hours and the exact minute within the hour the profiling should start. Example: If set to "Every 1 hour(s) on minute 0," the profile operation will run every hour at the top of the hour (e.g., 1:00, 2:00, 3:00).

![hourly](../assets/profile-operations/hourly-light.png#only-light)
![hourly](../assets/profile-operations/hourly-dark.png#only-dark)
  
**2. Daily**: This option schedules the profile operation to run once every day at a specific time. You specify the number of days between scans and the exact time of day in UTC. Example: If set to "Every 1 day(s) at 00:00 UTC," the scan will run every day at midnight UTC.

![daily](../assets/profile-operations/daily-light.png#only-light)
![daily](../assets/profile-operations/daily-dark.png#only-dark)
  
**3. Weekly**: This option schedules the profile operation to run on specific days of the week at a set time. You select the days of the week and the exact time of day in UTC for the profile operation to run. Example: If configured to run on "Sunday" and "Friday" at 00:00 UTC, the scan will execute at midnight UTC on these days.

![weekly](../assets/profile-operations/weekly-light.png#only-light)
![weekly](../assets/profile-operations/weekly-dark.png#only-dark)
  
**4. Monthly**: This option schedules the profile operation to run once a month on a specific day at a set time. You specify the day of the month and the time of day in UTC. If set to "On the 1st day of every 1 month(s), at 00:00 UTC," the profile operation will run on the first day of each month at midnight UTC.

![monthly](../assets/profile-operations/monthly-light.png#only-light)
![monthly](../assets/profile-operations/monthly-dark.png#only-dark)
  
**5. Advanced**: The advanced section for scheduling operations allows users to set up more complex and custom scheduling using Cron expressions. This option is particularly useful for defining specific times and intervals for profile operations with precision.

Cron expressions are a powerful and flexible way to schedule tasks. They use a syntax that specifies the exact timing of the task based on five fields:

-   Minute (0 - 59)
-   Hour (0 - 23)
-   Day of the month (1 - 31)
-   Month (1 - 12)
-   Day of the week (0 - 6) (Sunday to Saturday)

Each field can be defined using specific values, ranges, or special characters to create the desired schedule.

**Example**: For instance, the Cron expression `0 0 * * *` schedules the profile operation to run at midnight (00:00) every day. Here’s a breakdown of this expression:

-   0 (Minute) - The task will run at the 0th minute.
-   0 (Hour) - The task will run at the 0th hour (midnight).
-   *(Day of the month) - The task will run every day of the month.
-   *(Month) - The task will run every month.
-   *(Day of the week) - The task will run every day of the week.  

Users can define other specific schedules by adjusting the Cron expression. For example:

-   0 12 * * 1-5 - Runs at 12:00 PM from Monday to Friday.
-   30 14 1 * * - Runs at 2:30 PM on the first day of every month.
-   0 22 * * 6 - Runs at 10:00 PM every Saturday.
    
To define a custom schedule, enter the appropriate Cron expression in the **Custom Cron Schedule (UTC)** field before specifying the schedule name. This will allow for precise control over the timing of the profile operation, ensuring it runs exactly when needed according to your specific requirements.

![advanced](../assets/profile-operations/advanced-light.png#only-light)
![advanced](../assets/profile-operations/advanced-dark.png#only-dark)
  
**Step 3**: Define the **Schedule Name** to identify the scheduled operation at the running time.

![schedule-name](../assets/profile-operations/schedule-name-light.png#only-light)
![schedule-name](../assets/profile-operations/schedule-name-dark.png#only-dark)

**Step 4**: Click on the **Schedule** button to activate your profile operation schedule.

![profile-operation-schedule](../assets/profile-operations/profile-operation-schedule-light.png#only-light)
![profile-operation-schedule](../assets/profile-operations/profile-operation-schedule-dark.png#only-dark)
  
!!! note 
    You will receive a notification when the profile operation is completed.

## Operation Insights

When the profile operation is completed, you will receive the notification and can navigate to the Activity tab for the datastore on which you triggered the Profile Operation and learn about the operation results.

### Top Panel

1. **Runs (Default View)**: Provides insights into the operations that have been performed

2. **Schedule**: Provides insights into the scheduled operations.

3. **Search**: Search any operation (including catalog) by entering the operation ID

4. **Sort by**: Organize the list of operations based on the **Created Date** or the **Duration**.

5. **Filter**: Narrow down the list of operations based on:

-   Operation Type
-   Operation Status
-   Table

![activity-fields](../assets/profile-operations/activity-fields-light.png#only-light)
![activity-fields](../assets/profile-operations/activity-fields-dark.png#only-dark)
  
### Activity Heatmap

The activity heatmap shown in the snippet below represents activity levels over a period, with each square indicating a day and the color intensity representing the number of operations or activities on that day. It is useful in tracking the number of operations performed on each day within a specific timeframe.

!!! tip
    You can click on any of the squares from the Activity Heatmap to filter operations

![activity-table](../assets/profile-operations/activity-table-light.png#only-light)
![activity-table](../assets/profile-operations/activity-table-dark.png#only-dark)

### Operation Detail

#### Running

This status indicates that the profile operation is still running at the moment and is yet to be completed. A profile operation having a **running** status reflects the following details and actions:

| Parameter                  | Interpretation |
|----------------------------|-------------------------------------------------------------------------|
| Operation ID               | Unique identifier |
| Operation Type             | Type of operation performed (catalog, profile, or scan) |
| Timestamp                  | Timestamp when the operation was started |
| Progress Bar               | The progress of the operation |
| Triggered By               | The author who triggered the operation |
| Schedule                   | Whether the operation was scheduled or not |
| Infer Constraints          | Indicates whether Infer Constraints was enabled or disabled in the operation |
| Checks Synchronized        | Indicates the count of Checks Synchronized in the operation |
| Results                    | This provides immediate insights into the profile operation conducted |
| Abort                      | The "Abort" button enables you to stop the ongoing profile operation |
| Summary                    | The "Summary" section provides a real-time overview of the profile operation's progress. It includes key metrics such as: <br><ul><li> **Tables Requested**: The total number of tables that were requested for profiling. Click on the adjacent magnifying glass icon to view the tables requested.</li><li> **Tables Profiled**: The number of tables that have been profiled so far. Click on the adjacent magnifying glass icon to view the tables profiled. </li><li> **Records Profiled**:  This represents the total number of records that were included in the profiling process. </li><li> **Field Profiles Updates**:  This number shows how many field profiles were updated as a result of the profiling operation. </li><li> **Inferred Checks Synchronized**:  This indicates the number of inferred checks that were synchronized based on the profile operation. </li></ul> |

![profile-running](../assets/profile-operations/profile-running-light.png#only-light)
![profile-running](../assets/profile-operations/profile-running-dark.png#only-dark)
  
#### Aborted

This status indicates that the profile operation was manually stopped before it could be completed. A profile operation having an **aborted** status reflects the following details and actions:

| Parameters           | Interpretation |
|----------------------|-----------------------------------------------------------------------------|
| Operation ID         | Unique identifier |
| Operation Type       | Type of operation performed (catalog, profile, or scan) |
| Timestamp            | Timestamp when the operation was started |
| Progress Bar         | The progress of the operation |
| Triggered By         | The author who triggered the operation |
| Schedule             | Whether the operation was scheduled or not |
| Infer Constraints    | Indicates whether Infer Constraints was enabled or disabled in the operation |
| Checks Synchronized  | Indicates the count of Checks Synchronized in the operation |
| Results              | This provides immediate insights into the profile operation conducted |
| Resume               | Provides an option to continue the profile operation from where it left off. This can be useful if the operation is interrupted and you wish to complete it without starting over from the beginning. |
| Rerun                | The "Rerun" button allows you to start a new profile operation using the same settings as the aborted scan. This is helpful if you want to restart the profile operation from scratch due to errors or issues encountered in the previous attempt. |
| Delete               | Removes the record of the aborted profile operation from the system. This permanently deletes all profile results generated by the operation. This action cannot be undone. |
| Summary              | The "Summary" section provides a real-time overview of the profile operation's progress. It includes key metrics such as: <br><ul><li> **Tables Requested**: The total number of tables that were requested for profiling. Click on the adjacent magnifying glass icon to view the tables requested.</li><li> **Tables Profiled**: The number of tables that were profiled before the operation was aborted. Click on the adjacent magnifying glass icon to view the tables profiled. </li><li> **Records Profiled**: This represents the total number of records that were included before the profiling process was aborted. </li><li> **Field Profiles Updates**: This number shows how many field profiles were updated as a result of the profiling operation. </li><li> **Inferred Checks Synchronized**: This indicates the number of inferred checks that were synchronized based on the profile operation. </li></ul> |

![profile-aborted](../assets/profile-operations/profile-aborted-light.png#only-light)
![profile-aborted](../assets/profile-operations/profile-aborted-dark.png#only-dark)
  
#### Warning

This status signals that the profile operation encountered some issues and displays the logs that facilitate improved tracking of the blockers and issue resolution. A profile operation having a **warning** status reflects the following details and actions:

| Parameter               | Interpretation  |
|-------------------------|--------------------------------------------------------------------------|
| Operation ID            | Unique identifier |
| Operation Type          | Type of operation performed (catalog, profile, or scan) |
| Timestamp               | Timestamp when the operation was started |
| Progress Bar            | The progress of the operation |
| Triggered By            | The author who triggered the operation |
| Schedule                | Whether the operation was scheduled or not |
| Infer Constraints       | Indicates whether Infer Constraints was enabled or disabled in the operation  |
| Checks Synchronized     | Indicates the count of Checks Synchronized in the operation |
| Rerun                   | The "Rerun" button allows you to start a new profile operation using the same settings as the warning scan. This is helpful if you want to restart the profile operation from scratch due to errors or issues encountered in the previous attempt. |
| Delete                  | Removes the record of the profile operation from the system. This permanently deletes all profile results generated by the operation. This action cannot be undone. |
| Summary                 | The "Summary" section provides a real-time overview of the profile operation's progress. It includes key metrics such as: <br><ul><li> **Tables Requested**: The total number of tables that were requested for profiling. Click on the adjacent magnifying glass icon to view the tables requested.</li><li> **Tables Profiled**: The number of tables that were profiled before the operation was aborted. Click on the adjacent magnifying glass icon to view the tables profiled. </li><li> **Records Profiled**: This represents the total number of records that were included before the profiling process was aborted. </li><li> **Field Profiles Updates**: This number shows how many field profiles were updated as a result of the profiling operation.</li><li>  **Inferred Checks Synchronized**: This indicates the number of inferred checks that were synchronized based on the profile operation. </li></ul> |
| Logs                    | Logs include error messages, warnings, and other pertinent information that occurred during the execution of the Profile Operation. |

![profile-warning](../assets/profile-operations/profile-warning-light.png#only-light)
![profile-warning](../assets/profile-operations/profile-warning-dark.png#only-dark)
  
#### Success

This status confirms that the profile operation was completed successfully without any issues. A profile operation having a **success** status reflects the following details and actions:

| Parameter               | Interpretation            |
|-------------------------|----------------------------------------------------------------------------|
| Operation ID            | Unique identifier |
| Operation Type          | Type of operation performed (catalog, profile, or scan) |
| Timestamp               | Timestamp when the operation was started |
| Progress Bar            | The progress of the operation |
| Triggered By            | The author who triggered the operation |
| Schedule                | Whether the operation was scheduled or not |
| Infer Constraints       | Indicates whether Infer Constraints was enabled or disabled in the operation |
| Checks Synchronized     | Indicates the count of Checks Synchronized in the operation |
| Rerun                   | The "Rerun" button allows you to start a new profile operation using the same settings as the warning scan. This is helpful if you want to restart the profile operation from scratch due to errors or issues encountered in the previous attempt. |
| Delete                  | Removes the record of the profile operation from the system. This permanently deletes all profile results generated by the operation. This action cannot be undone. |
| Summary                 | The "Summary" section provides a real-time overview of the profile operation's progress. It includes key metrics such as: <br><ul><li> **Tables Requested**: The total number of tables that were requested for profiling. Click on the adjacent magnifying glass icon to view the tables requested. </li><li> **Tables Profiled**: The number of tables that were profiled before the operation was aborted. Click on the adjacent magnifying glass icon to view the tables profiled. </li><li> **Records Profiled**: This represents the total number of records that were included before the profiling process was aborted. </li><li> **Field Profiles Updates**: This number shows how many field profiles were updated as a result of the profiling operation. </li><li> **Inferred Checks Synchronized**: This indicates the number of inferred checks that were synchronized based on the profile operation. </li></ul> |

![profile-success](../assets/profile-operations/profile-success-light.png#only-light)
![profile-success](../assets/profile-operations/profile-success-dark.png#only-dark)
  
## Post Operation Details

**Step 1**: Click on any of the successful **Scan Operations** from the list and hit the Results button.

![profile-result](../assets/profile-operations/profile-result-light.png#only-light)
![profile-result](../assets/profile-operations/profile-result-dark.png#only-dark)
  
**Step 2**: The **Profile Results** modal demonstrates the list of all the containers profiled. This opens the following two analysis options for you:

-   Details for a Specific Container (Container's Profile)
-   Details for a Specific Field of a Container (Field Profile)

Unwrap any of the containers from the **Profile Results** modal and click on the arrow icon.

![view-table](../assets/profile-operations/view-table-light.png#only-light)
![view-table](../assets/profile-operations/view-table-dark.png#only-dark)
  
### Details for a Specific Container (Container's Profile)

Based on your selection of container from the profile operation results, you will be automatically redirected to the container details on the source datastore details page.

![sandbox-tpch](../assets/profile-operations/sandbox-tpch-light.png#only-light)
![sandbox-tpch](../assets/profile-operations/sandbox-tpch-dark.png#only-dark)
  
The following details (metrics) will be visible for analyzing the specific container you selected:

-   Quality Score:  
-   Sampling:
-   Completeness:  
-   Records:  
-   Fields:  
-   Checks:  
-   Data Volume Overtime:

![total-anomalies](../assets/profile-operations/total-anomalies-light.png#only-light)
![total-anomalies](../assets/profile-operations/total-anomalies-dark.png#only-dark)

### Details for a Specific Field of a Container (Field Profile)

Unwrap the container to view the underlying fields. The following details (metrics) will be visible for analyzing a specific field of the container:

1. Sampling, completeness, checks

2. Type inferred (Whether type is declared by the source or inferred)

3. Distinct values (Count of distinct values)

4. Min (Shortest length of the observed values)/Max Length (Greatest length of the observed values) (for strings) or Min (lowest value)/Max (greatest value) (for numerics and datetime)

5. Entropy (Measure of how many bits are required to identify a value)

6. Unique/distinct (The ratio of values that appear once to number of different values observed)

7. Unique Values (Count of values that appear once)

8. For numeric values, it shows:  
  
    a. Mean (Mathematical average)

    b. Median (The median of the observed values)

    c. Std. Deviation (Measure of the amount of variation in observed values)

    d. Kurtosis (Measure of the 'tailedness' of the distribution of values)

    e. Skewness (Measure of the asymmetry of the distribution around its mean)

    f. Q1 (The central point between the min and the median)

    g. Q3 (The central point between the median and the max)

    h. Sum (Sum of all observed values)

    ![total-profile](../assets/profile-operations/totals-profile-light.png#only-light)
    ![total-profile](../assets/profile-operations/totals-profile-dark.png#only-dark)

9. Histogram

![histogram](../assets/profile-operations/histogram-light.png#only-light)
![histogram](../assets/profile-operations/histogram-dark.png#only-dark)
  
## API Payload Examples

This section provides payload examples for initiating and checking the running status of a profile operation. Replace the placeholder values with data specific to your setup.

### Running a Catalog operation

To run a profile operation, use the API payload example below and replace the placeholder values with your specific values:

**Endpoint (Post)**:  ```/api/operations/run (post)```

#### Option I: Running a profile operation of all containers

-   **container_names: [ ]**: This setting indicates that profiling will encompass all containers.

-   **max_records_analyzed_per_partition: null**: This setting implies that all records within all containers will be profiled.

-   **infer_constraints: false**: This setting indicates that the engine will not automatically infer quality checks for you.
    
```json
{  
    "type":"profile",  
    "datastore_id": datastore-id,  
    "container_names":[],  
    "max_records_analyzed_per_partition":null,  
    "infer_constraints":true  
}
```
  
#### Option II: Running a profile operation of specific containers

-   **container_names**: ["table_name_1", "table_name_2"]: This setting indicates that profiling will only cover the tables named table_name_1 and table_name_2.

-   **max_records_analyzed_per_partition: 1000000:** This setting means that up to 1 million rows per container will be profiled.

-   **infer_constraints: false:** This setting indicates that the engine will not automatically infer quality checks.

```json
{  
    "type":"profile",  
    "datastore_id":datastore-id,  
    "container_names":[  
        "table_name_1",  
        "table_name_2"  
    ],  
    "max_records_analyzed_per_partition":1000000,  
    "infer_constraints":false  
}
```

### Scheduling a Profile operation

Below is a sample payload for scheduling a profile operation. Please substitute the placeholder values with the appropriate data relevant to your setup.

**Endpoint (Post)**: ```/api/operations/schedule (post)```

**INFO**: This payload is to run a scheduled profile operation every day at 00:00

#### Scheduling profile operation of all containers

```json
{  
    "type":"profile",  
    "name":"My scheduled Profile operation",  
    "datastore_id":"datastore-id",  
    "container_names":[],  
    "max_records_analyzed_per_partition":null,  
    "infer_constraints":true,  
    "crontab":"00 00 */1 * *"  
}
```

### Retrieving Profile Operation Status

To retrieve the profile operation status, use the API payload example below and replace the placeholder values with your specific values:

**Endpoint (Get)**: ```/api/operations/{id} (get)```

```json
{
    "items": [
        {
            "id": 12345,
            "created": "YYYY-MM-DDTHH:MM:SS.ssssssZ",
            "type": "profile",
            "start_time": "YYYY-MM-DDTHH:MM:SS.ssssssZ",
            "end_time": "YYYY-MM-DDTHH:MM:SS.ssssssZ",
            "result": "success",
            "message": null,
            "triggered_by": "user@example.com",
            "datastore": {
                "id": 101,
                "name": "Sample-Store",
                "store_type": "jdbc",
                "type": "db_type",
                "enrich_only": false,
                "enrich_container_prefix": "data_prefix",
                "favorite": false
            },
            "schedule": null,
            "infer_constraints": true,
            "max_records_analyzed_per_partition": -1,
            "max_count_testing_sample": 100000,
            "histogram_max_distinct_values": 100,
            "greater_than_time": null,
            "greater_than_batch": null,
            "percent_testing_threshold": 0.4,
            "high_correlation_threshold": 0.5,
            "status": {
                "total_containers": 2,
                "containers_analyzed": 2,
                "partitions_analyzed": 2,
                "records_processed": 1126,
                "fields_profiled": 9,
                "checks_synchronized": 26
            },
            "containers": [
                {
                    "id": 123,
                    "name": "Container1",
                    "container_type": "table",
                    "table_type": "table"
                },
                {
                    "id": 456,
                    "name": "Container2",
                    "container_type": "table",
                    "table_type": "table"
                }
            ],
            "container_profiles": [
                {
                    "id": 789,
                    "created": "YYYY-MM-DDTHH:MM:SS.ssssssZ",
                    "parent_profile_id": null,
                    "container": {
                        "id": 456,
                        "name": "Container2",
                        "container_type": "table",
                        "table_type": "table"
                    },
                    "records_count": 550,
                    "records_processed": 550,
                    "checks_synchronized": 11,
                    "field_profiles_count": 4,
                    "result": "success",
                    "message": null
                },
                {
                    "id": 790,
                    "created": "YYYY-MM-DDTHH:MM:SS.ssssssZ",
                    "parent_profile_id": null,
                    "container": {
                        "id": 123,
                        "name": "Container1",
                        "container_type": "table",
                        "table_type": "table"
                    },
                    "records_count": 576,
                    "records_processed": 576,
                    "checks_synchronized": 15,
                    "field_profiles_count": 5,
                    "result": "success",
                    "message": null
                }
            ],
            "tags": []
        }
    ],
    "total": 1,
    "page": 1,
    "size": 50,
    "pages": 1
}
``` 