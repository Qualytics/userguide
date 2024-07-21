# Scan Operation

The Scan Operation in Qualytics is performed on a datastore to enforce data quality checks for various data collections such as tables, views, and files. This operation has several key functions:

-   **Record Anomalies:** Identifies a single record (row) as anomalous and provides specific details regarding why it is considered anomalous. The simplest form of a record anomaly is a row that lacks an expected value for a field.  

-   **Shape Anomalies:** Identifies structural issues within a dataset at the column or schema level. It highlights broader patterns or distributions that deviate from expected norms. If a dataset is expected to have certain fields and one or more fields are missing or contain inconsistent patterns, this would be flagged as a shape anomaly.  

-   **Anomaly Data Recording:** All identified anomalies, along with related analytical data, are recorded in the associated Enrichment Datastore for further examination. Additionally, the Scan Operation offers flexible options, including the ability to:

-   Perform checks on incremental loads versus full loads.
-   Limit the number of records scanned.
-   Run scans on a selected list of tables or files.
-   Schedule scans for future execution.

Let's get started! 🚀

# Navigation to Scan Operation

**Step 1:** Select a source datastore from the side menu on which you would like to perform the scan operation.

![side-menu](../assets/datastores/scan/side-menu-light.png#only-light)
![side-menu](../assets/datastores/scan/side-menu-dark.png#only-dark)

**Step 2:** Clicking on your preferred datastore will navigate you to the datastore details page. Within the overview tab (default view), click on the Run button under Scan to initiate the catalog operation.

![details-page](../assets/datastores/scan/details-page-light.png#only-light)
![details-page](../assets/datastores/scan/details-page-dark.png#only-dark)

!!! note
    Scanning operation can be commenced once the catalog operation and profile operation is completed.

# Configuration

**Step 1:** Click on the **Run** button to initiate the scan operation.

![run](../assets/datastore/scan/run-light.png#only-light)
![run](../assets/datastores/scan/run-dark.png#only-dark)

**Step 2:** Select tables (in your JDBC datastore) or file patterns (in your DFS datastore) and tags you would like to be scanned.

**1. All Tables/File Patterns**

This option includes all tables or file patterns currently available for scanning in the datastore. It means that every table or file pattern recognized in your datastore will be subjected to the defined data quality checks. Use this when you want to perform a comprehensive scan covering all the available data without any exclusions.

![tablefile](../assets/datastores/scan/tablefile-light.png#only-light)
![tablefile](../assets/datastores/scan/tablefile-dark.png#only-dark)

**2. Specific Tables/File Patterns**

This option allows you to manually select the individual table(s) or file pattern(s) in your datastore to scan. Upon selecting this option, all the tables or file patterns associated with your datastore will be automatically populated allowing you to select the datasets you want to scan.

You can also search the tables/file patterns you want to scan directly using the search bar. Use this option when you need to target particular datasets or when you want to exclude certain files from the scan for focused analysis or testing purpoaes

![specific-patterns](../assets/datastores/scan/specific-patterns.png#only-light)
![specific-pattrens](../assets/datastores/scan/specific-patterns.png#only-dark)

**Tag**
This option enables you to automatically scan file patterns associated with the selected tags. Tags can be predefined or created to categorize and manage file patterns effectively.

![tag](../assets/datastores/scan/tag-light.png#only-light)
![tag](../assets/datastores/scan/tag-dark.png#only-dark)

**Step 3:** After making the relevant selections, click on the **Next** button.

![next](../assets/datastores/scan/next-light.png#only-light)
![next](../assets/datastores/scan/next-dark.png#only-dark)

**Step 4:** Configure Read Settings, Starting Threshold (Optional), and the Record Limit.

![read-setting](../assets/datastores/scan/read-setting-light.png#only-light)
![read-setting](../assets/datastores/scan/read-setting-dark.png#only-dark)

**1.Select the Read Strategy for your scan operation**.

- **Incremental:** This strategy is used to scan only the new or updated records since the last scan operation. On the initial run, a full scan is conducted unless a specific starting threshold is set. For subsequent scans, only the records that have changed since the last scan are processed. If tables or views do not have a defined incremental key, a full scan will be performed. Ideal for regular scans where only changes need to be tracked, saving time and computational resources.  

- **Full:** This strategy performs a comprehensive scan of all records within the specified data collections, regardless of any previous changes or scans. Every scan operation will include all records, ensuring a complete check each time. Suitable for periodic comprehensive checks or when incremental scanning is not feasible due to the nature of the data.

![incremental](../assets/datastores/scan/incremental-light.png#only-light)
![incremental](../assets/datastores/scan/incremental-dark.png#only-dark)

**2. Define the Starting Threshold (Optional) i.e.** - specify a minimum incremental identifier value to set a starting point for the scan.

- **Greater Than Time:** This option applies only to tables with an incremental timestamp strategy. Users can specify a timestamp to scan records that were modified after this time.

- **Greater Than Batch:** This option applies to tables with an incremental batch strategy. Users can set a batch value, ensuring that only records with a batch identifier greater than the specified value are scanned.

**3. Define the record limit**- the maximum number of records to be scanned per table after any initial filtering.

![record-limit](../assets/datastores/scan/record-limit-light.png#only-light)
![record-limit](../assets/datastores/scan/record-limit-dark.png#only-dark)

**Step 5:** Click on the **Next** button to Configure the **Enrichment Settings**.

![enrichment](../assets/datastores/scan/enrichment-light.png#only-light)
![enrichment](../assets/datastores/scan/enrichment-dark.png#only-dark)

**Step 6:** Configure the **Enrichment Settings**.  

1. **Remediation Strategy:** This strategy dictates how your source tables are replicated in your enrichment datastore:

-   **None:** This option does not replicate source tables. It only writes anomalies and associated source data to the enrichment datastore. This is useful when the primary goal is to track anomalies without duplicating the entire dataset.  

-   **Append:** This option replicates source tables using an append-first strategy. It adds new records to the enrichment datastore, maintaining a history of all data changes over time. This approach is beneficial for auditing and historical analysis.

-   **Overwrite:** This option replicates source tables using an overwrite strategy, replacing existing data in the enrichment datastore with the latest data from the source. This method ensures the enrichment datastore always contains the most current data, which is useful for real-time analysis and reporting.

![overwrite](../assets/datastores/scan/overwrite-light.png#only-light)
![overwrite](../assets/datastores/scan/overwrite-dark.png#only-dark)

**2. Source Record Limit:** Sets a maximum limit on the number of records written to the enrichment datastore for each detected anomaly. This helps manage storage and processing requirements effectively.

![recordlimit](../assets/datastores/scan/record-limit-light.png#only-light)
![recordlimit](../assets/datastores/scan/record-limit-dark.png#only-dark)

## Run Instantly

Click on the **Run Now** button to perform the scan operation immediately.

![run-now](../assets/datastores/scan/run-now-light.png#only-light)
![run-now](../assets/datastores/scan/run-now-dark.png#only-dark)

## Schedule

**Step 1:** Click on the **Schedule** button to configure the available schedule options for your scan operation.

![schedule-button](../assets/datastores/scan/schedule-button-light.png#only-light)
![schedule-button](../assets/datastores/scan/schedule-button-dark.png#only-dark)

**Step 2:** Set the scheduling preferences for the profile operation.

**1. Hourly:** This option allows you to schedule the scan to run every hour at a specified minute. You can define the frequency in hours and the exact minute within the hour the scan should start. Example: If set to **Every 1 hour(s) on minute 0,** the scan will run every hour at the top of the hour (e.g., 1:00, 2:00, 3:00).

![hourly](../assets/datastores/scan/hourly-light.png#only-light)
![hourly](../assets/datastores/scan/hourly-dark.png#only-dark)

**2. Daily:** This option schedules the scan to run once every day at a specific time. You specify the number of days between scans and the exact time of day in UTC. Example: If set to **Every 1 day(s) at 00:00 UTC,** the scan will run every day at midnight UTC.

![daily](../assets/datastores/scan/daily-light.png#only-light)
![daily](../assets/datastores/scan/daily-dark.png#only-dark)

**3. Weekly:** This option schedules the scan to run on specific days of the week at a set time. You select the days of the week and the exact time of day in UTC for the scan to run. Example: If configured to run on "Sunday" and "Friday" at 00:00 UTC, the scan will execute at midnight UTC on these days.

![weekly](../assets/datastores/scan/weekly-light.png#only-light)
![weekly](../assets/datastores/scan/weekly-dark.png#only-dark)

**4. Monthly:** This option schedules the scan to run once a month on a specific day at a set time. You specify the day of the month and the time of day in UTC. If set to "On the 1st day of every 1 month(s), at 00:00 UTC," the scan will run on the first day of each month at midnight UTC.

![monthly](../assets/datastores/scan/monthly-light.png#only-light)
![monthly](../assets/datastores/scan/monthly-dark.png#only-dark)

**5. Advanced:** This option allows for more complex and custom scheduling using Cron expressions. Enter a cron expression to define the exact times and intervals for the scan operation. Cron expressions are a powerful way to schedule tasks using a syntax that specifies the exact timing of the task. For example, a cron expression like 0 0 * * * would schedule the scan to run at midnight (00:00) every day.

![advanced](../assets/datastores/scan/advanced-light.png#only-light)
![advanced](../assets/datastores/scan/advanced-dark.png#only-dark)

**Step 3:** Define the **Schedule Name** to identify the scheduled operation at the running time.

![schedule-name](../assets/datastores/scan/schedule-name-light.png#only-light)
![schedule-name](../assets/datastores/scan/schedule-name-dark.png#only-dark)

**Step 4:** Click on the **Schedule** button to schedule your scan operation.

![schedule](../assets/datastores/scan/schedule-light.png#only-light)
![schedule](../assets/datastores/scan/schedule-dark.png#only-dark)

!!! note
    You will receive a notification when the profile operation is completed. 

## Runtime Variable Assignment

It is possible to reference a variable in a check definition (declared in double curly braces) and then assign that variable a value when a Scan operation is initiated. Variables are supported within any Spark SQL expression and are most commonly used in a check filter.

If a Scan is meant to assert a check with a variable, a value for that variable must be supplied as part of the Scan operation's check_variables property.

For example, a check might include a filter.- transaction_date == {{ checked_date }} which will be asserted against any records where transaction_date is equal to the value supplied when the Scan operation is initiated. In this case that value would be assigned by passing the following payload when calling ```/api/operations/run```

```json
        {
          "type": "scan",
          "datastore_id": 42,
          "container_names": [
            "my_container"
            ],
          "incremental": true,
          "remediation": "none",
          "max_records_analyzed_per_partition": 0,
          "check_variables": {
          "checked_date": "2023-10-15"
      },
          "high_count_rollup_threshold": 10
      }
```
### Operations Insights

When the scan operation is completed, you will receive the notification and can navigate to the Activity tab for the datastore on which you triggered the Scan Operation and learn about the scan results.
## Top Panel

**1. Runs (Default View):** Provides insights into the operations that have been performed

**2. Schedule:** Provides insights into the [scheduled operations](https://userguide.qualytics.io/operation-automation/automated-tasks-with-cron/).

**3. Search:** Search any operation (including scan) by entering the operation ID

**4. Sort by:** Organize the list of operations based on the **Created Date** or the **Duration**.

**5. Filter:** Narrow down the list of operations based on:

-   Operation Type
-   Oeration Status   
-   Table

![operations](../assets/datastores/scan/operations-light.png#only-light)
![operations](../assets/datastores/scan/operations-dark.png#only-dark)

## Activity Heatmap

The activity heatmap shown in the snippet below represents activity levels over a period, with each square indicating a day and the color intensity representing the number of operations or activities on that day. It is useful in tracking the number of operations performed on each day within a specific timeframe.

!!! tip 
    You can click on any of the squares from the Activity Heatmap to filter operations.

![activity](../assets/datastores/scan/activity-light.png#only-light)
![activity](../assets/datastores/scan/activity-dark.png#only-dark)


## Operation Detail

### Running

This status indicates that the scan operation is still running at the moment and is yet to be completed. A scan operation having a “running” status reflects the following details and actions:

![running](../assets/datastores/scan/running-page-light.png#only-light)
![running](../assets/datastores/scan/running-page-dark.png#only-dark)

| Parameter         | Interpretation |
|-------------------|-----------------------------------------------------|
| Operation ID | Unique identifier  |
| Operation Type | Type of operation performed (catalog, profile, or scan) |
| Timestamp | Timestamp when the operation was started  |
| Progress Bar | The progress of the operation |
| Triggered By | The author who triggered the operation |
| Schedule | Whether the operation was scheduled or not |
| Incremental Field | Indicates whether Incremental was enabled or disabled in the operation  |
| Remediation | Indicates whether Remediation was enabled or disabled in the operation |
| Results | Provides immediate insights into any anomalies identified so far during the scan process |
| Abort | The "Abort" button enables you to stop the ongoing scan operation |
| Summary | The "Summary" section provides a real-time overview of the scan operation's progress. It includes key metrics such as: |
|                   | - **Tables Requested**: The total number of tables that were scheduled for scanning. Click on the adjacent magnifying glass icon to view the tables requested. |
|                   | - **Tables Scanned**: The number of tables that have been scanned so far. Click on the adjacent magnifying glass icon to view the tables scanned. |
|                   | - **Partitions Scanned**: The number of partitions scanned. |
|                   | - **Records Scanned**: The total number of records that have been scanned.|
|                   | - **Anomalies Identified**: The number of anomalies detected during the scan. |

### Aborted

This status indicates that the scan operation was manually stopped before it could be completed. A scan operation having an “aborted” status reflects the following details and actions:

![aborted](../assets/datastores/scan/aborted-light.png#only-light)
![aborted](../assets/datastores/scan/aborted-dark.png#only-dark)

| Parameter | Interpretation |
|----------------------|-------------------------------------|
| Operation ID | Unique identifier |
| Operation Type | Type of operation performed (catalog, profile, or scan) |
| Timestamp | Timestamp when the operation was started |
| Progress Bar | The progress of the operation |
| Triggered By | The author who triggered the operation |
| Schedule | Whether the operation was scheduled or not |
| Incremental Field | Indicates whether Incremental was enabled or disabled in the operation |
| Remediation | Indicates whether Remediation was enabled or disabled in the operation |
| Anomalies Identified | Provides a count on the number of anomalies detected before the operation was aborted |
| Results | View the details of the scan operation that was aborted. This includes information on which tables were scanned, the anomalies identified (if any), and other related data collected up to the point when the scan was aborted. |
| Resume  | Provides an option to continue the scan operation from where it left off. This can be useful if the scan was interrupted and you wish to complete it without starting over from the beginning. |
| Rerun | The "Rerun" button allows you to start a new scan operation using the same settings as the aborted scan. This is helpful if you want to restart the scan from scratch due to errors or issues encountered in the previous attempt. |
| Delete | Removes the record of the aborted scan operation from the system. This permanently deletes all scan results and anomalies generated by the operation. This action cannot be undone. |
| Summary | The summary section provides an overview of the scan operation up to the point it was aborted. It includes: |
|                      | - **Tables Requested**: The total number of tables that were scheduled for scanning. Click on the adjacent magnifying glass icon to view the tables requested. |
|                      | - **Tables Scanned**: The number of tables that have been scanned so far. Click on the adjacent magnifying glass icon to view the tables scanned. |
|                      | - **Partitions Scanned**: The number of partitions scanned before the operation was aborted.|
|                      | - **Records Scanned**: The total number of records processed before the scan was stopped. |
|                      | - **Anomalies Identified**: The number of anomalies detected during the partial scan. |

### Warning

This status signals that the scan operation encountered some issues and displays the logs that facilitate improved tracking of the blockers and issue resolution. A scan operation having a “warning” status reflects the following details and actions:

![warning](../assets/datastores/scan/warning-light.png#only-light)
![warning](../assets/datastores/scan/warning-page-dark.png#only-dark)

| Parameter            | Interpretation |
|----------------------|-------------------------------------------|
| Operation ID         | Unique identifier |
| Operation Type       | Type of operation performed (catalog, profile, or scan)|
| Timestamp            | Timestamp when the operation was started |
| Progress Bar         | The progress of the operation |
| Triggered By         | The author who triggered the operation |
| Schedule             | Whether the operation was scheduled or not |
| Incremental Field    | Indicates whether Incremental was enabled or disabled in the operation |
| Remediation          | Indicates whether Remediation was enabled or disabled in the operation |
| Anomalies Identified | Provides a count on the number of anomalies detected before the operation was aborted |
| Results              | View the details of the scan operation that was aborted. This includes information on which tables were scanned, the anomalies identified (if any), and other related data collected up to the point when the scan was aborted. |
| Resume               | Provides an option to continue the scan operation from where it left off. This can be useful if the scan was interrupted and you wish to complete it without starting over from the beginning. |
| Rerun                | The "Rerun" button allows you to start a new scan operation using the same settings as the aborted scan. This is helpful if you want to restart the scan from scratch due to errors or issues encountered in the previous attempt. |
| Delete               | Removes the record of the aborted scan operation from the system. This permanently deletes all scan results and anomalies generated by the operation. This action cannot be undone. |
| Summary              | The summary section provides an overview of the scan operation up to the point it was aborted. It includes: |
|                      | - **Tables Requested**: The total number of tables that were scheduled for scanning. Click on the adjacent magnifying glass icon to view the tables requested. |
|                      | - **Tables Scanned**: The number of tables that have been scanned so far. Click on the adjacent magnifying glass icon to view the tables scanned. |
|                      | - **Partitions Scanned**: The number of partitions scanned before the operation was aborted.|
|                      | - **Records Scanned**: The total number of records processed before the scan was stopped.  |
|                      | - **Anomalies Identified**: The number of anomalies detected during the partial scan. |

# Post Operation Details

**Step 1:** Click on any of the successful **Scan Operations** from the list and hit the Results button.

![operations](../assets/datastores/scan/operations-light.png#only-light)
![operations](../assets/datastores/scan/operations-dark.png#only-dark)

**Step 2:** The **Scan Results** modal demonstrates the highlighted anomalies (if any) identified in your datastore with the following properties:

| Ref. | Scan Properties | Description |
|------|-----------------|------------------------|
| 1.   | Table/File | The table or file where the anomaly is found.|
| 2.   | Field | The field(s) where the anomaly is present. Field(s) of the anomaly. |
| 3.   | Location | Fully qualified location of the anomaly.|
| 4.   | Rule | Inferred and authored checks that failed assertions. |
| 5.   | Description | Human-readable, auto-generated description of the anomaly.|
| 6.   | Status | The status of the anomaly. Active, Acknowledged, Resolved, or Invalid |
| 7.   | Type | The type of anomaly (e.g., Record or Shape) |
| 8.   | Tag | Tags or labels associated with an anomaly. |
| 9.   | Date time | The date and time when the anomaly was found. |

# API Payload Examples

This section provides payload examples for running, scheduling, and checking the status of scan operations. Replace the placeholder values with data specific to your setup.

## Running a Scan operation

To run a scan operation, use the API payload example below and replace the placeholder values with your specific values.

Endpoint (Post): ```/api/operations/run (post)```

### Option I: Running a scan operation of all containers

-   **container_names:** [] means that it will scan all containers.
-   **max_records_analyzed_per_partition:** null means that it will scan all records of all containers.   
-   **Remediation:** append replicates source containers using an append-first strategy.
```json
        {
          "type":"scan",
          "name":null,
          "datastore_id": datastore-id,
          "container_names":[],
          "remediation":"append",
          "incremental":false,
          "max_records_analyzed_per_partition":null,
          "enrichment_source_record_limit":10
        }
```

### Option II: Running a scan operation of specific containers

-   **container_names:** ["table_name_1", "table_name_2"] means that it will scan only the tables table_name_1 and table_name_2.
-   **max_records_analyzed_per_partition:** 1000000 means that it will scan a maximum of 1 million records per partition.  
-   **Remediation:** overwrite replicates source containers using an overwrite strategy.

```json
    {
        "name": "your_datastore_name",
        "teams": ["Public"],
        "database": "databricks_database",
        "schema": "databricks_catalog",
        "enrich_only": false,
        "trigger_catalog": true,
        "connection_id": connection-id
    }
```
## Scheduling scan operation of all containers

To schedule a scan operation, use the API payload example below and replace the placeholder values with your specific values.

**Endpoint (Post):** ```/api/operations/schedule (post)```

```json  
    {
      "items": [
        {
              "id": 12345,
              "created": "YYYY-MM-DDTHH:MM:SS.ssssssZ",
              "type": "scan",
            "start_time": "YYYY-MM-DDTHH:MM:SS.ssssssZ",
              "end_time": "YYYY-MM-DDTHH:MM:SS.ssssssZ",
              "result": "success",
              "message": null,
              "triggered_by": "user@example.com",
            "datastore": {
                          "id": 101,
                          "name": "Datastore-Sample",
                          "store_type": "jdbc",
                          "type": "db_type",
                          "enrich_only": false,
                          "enrich_container_prefix": "data_prefix",
                        "favorite": false
                          },
                              "schedule": null,
                              "incremental": false,
                              "remediation": "none",
                              "max_records_analyzed_per_partition": -1,
                              "greater_than_time": null,
                              "greater_than_batch": null,
                              "high_count_rollup_threshold": 10,
                              "enrichment_source_record_limit": 10,
                              "status": {
                                        "total_containers": 2,
                                        "containers_analyzed": 2,
                                        "partitions_scanned": 2,
                                        "records_processed": 28,
                                        "anomalies_identified": 2
                                        },
                                      "containers": [
                                        {
                                          "id": 234,
                                          "name": "Container1",
                                          "container_type": "table",
                                            "table_type": "table"
                                        },
                                        {
                                          "id": 235,
                                          "name": "Container2",
                                          "container_type": "table",
                                          "table_type": "table"
                                        }
                                  ],
                                          "container_scans": [
                                      {
                                        "id": 456,
                                        "created": "YYYY-MM-DDTHH:MM:SS.ssssssZ",
                                        "container": {
                                                      "id": 235,
                                                      "name": "Container2",
                                                      "container_type": "table",
                                                      "table_type": "table"
                                                      },
                                        "start_time": "YYYY-MM-DDTHH:MM:SS.ssssssZ",
                                        "end_time": "YYYY-MM-DDTHH:MM:SS.ssssssZ",
                                        "records_processed": 8,
                                        "anomaly_count": 1,
                                        "result": "success",
                                          "message": null
                                          },
                                          {
                                          "id": 457,
                                          "created": "YYYY-MM-DDTHH:MM:SS.ssssssZ",
                                          "container": {
                                          "id": 234,
                                          "name": "Container1",
                                          "container_type": "table",
                                            "table_type": "table"
                                            },
                                          "start_time": "YYYY-MM-DDTHH:MM:SS.ssssssZ",
                                          "end_time": "YYYY-MM-DDTHH:MM:SS.ssssssZ",
                                          "records_processed": 20,
                                          "anomaly_count": 1,
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
This payload is to run a scheduled scan operation every day at 00:00