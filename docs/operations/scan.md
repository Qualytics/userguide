# Scan Operation


The Scan Operation is executed on a Datastore to assert the data quality checks defined for the named collections of data (e.g. tables, views, files, topics) within it. The operation will:



* produce a record anomaly for any record where anomalous values are detected
* produce a shape anomaly for anomalous values that span multiple records
* record the anomaly data along with related analysis in the associated Enrichment Datastore

Scan operation enables the user to assert the checks in incremental vs full loads, with options to limit the number of records, run a scan on a select list of tables / files, and to set schedules for future scans.

!!! info
    To assert data quality checks to find anomalies, a user needs to perform a Scan operation.

## Configuration

![Screenshot](../assets/operations/operation-scan-light.png#only-light)
![Screenshot](../assets/operations/operation-scan-dark.png#only-dark)

A Scan Operation can be configured with the following options:

* **Full**: To process all records ignoring the previous scan.

* **Incremental**: To scan only new data updated since the previous scan.

!!! info

    When running an Incremental Scan for the first time, Qualytics automatically performs a full scan, saving the incremental field for subsequent runs. 

    - This ensures that the system establishes a baseline and captures all relevant data. 

    - Once the initial full scan is completed, the system intelligently uses the saved incremental field to execute future Incremental Scans efficiently, focusing only on the new or updated data since the last scan. 

    - This approach optimizes the scanning process while maintaining data quality and consistency.

* **Record limit**: To limit the total number of records scanned.

* **Target selection**
    - All tables/files
    - Subset of available named collections (tables, files, etc.)
    - Selection of collections based on tags

* **Starting Thresholds**

	* **Greater Than Time**
		* Applicable only to profiles with an incremental timestamp strategy. 
		* Users can define a starting point based on incremental timestamps, allowing the analysis to focus on data beyond a specified time threshold.

	* **Greater Than Batch**
		* Applicable only to profiles with an incremental batch strategy.
		* Users can set a beginning point by specifying a batch threshold. This ensures that the analysis concentrates on data beyond a defined batch number.

![Screenshot](../assets/operations/operation-scan-specific-tables-light.png#only-light)
![Screenshot](../assets/operations/operation-scan-specific-tables-dark.png#only-dark)

* **Remediation strategy**: To specify how enrichment tables should be migrated to reflect changes in source tables.

* **Source Record Limit**: Set a maximum limit on the number of records written to the enrichment for each detected anomaly.

![Screenshot](../assets/operations/remediation-strategy-light.png#only-light)
![Screenshot](../assets/operations/remediation-strategy-dark.png#only-dark)

* **Schedule Options**: There's also an option to schedule the operation by:
    - **Hourly**
    - **Daily**
    - **Weekly**
    - **Monthly**
    - **Advanced**
        - Cron job expression

![Screenshot](../assets/operations/scheduling-a-scan-light.png#only-light)
![Screenshot](../assets/operations/scheduling-a-scan-dark.png#only-dark)

## Advanced Options

The advanced use cases described below require options that are not yet exposed in our user interface but possible through interation with our API.

### Runtime Variable Assignment

It is possible to reference a variable in a check definition (declared in double curly braces) and then assign that variable a value when a Scan operation is initiated. 

Variables are supported within any Spark SQL expression and most commonly used in a check's filter. 

If a Scan is meant to assert a check with a variable, a value for that variable must be supplied as part of the Scan operation's `check_variables` property.

For example, a check might include a filter such as `transaction_date == {{checked_date}}` which will be asserted against any records where transaction_date is equal to the value supplied when the Scan operation is initiated. In this case that value would be assigned by passing the following payload when calling `/api/operations/run`

```
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

## Scan Results

When a Scan is run, Qualytics will highlight anomalies with the following information:

![Screenshot](../assets/anomalies/anomalies-fields-light.png#only-light)
![Screenshot](../assets/anomalies/anomalies-fields-dark.png#only-dark)

* **Table**/**File**: the **Table** or **File** of the anomaly
* **Field**: the field(s) of the anomaly
* **Location**: fully qualified location of the anomaly
* **Rule**: **Infered** and **Authored** checks that failed assertions
* **Description**: human-readable, auto-generated description of the anomaly
* **Status**: The status of the anomaly. If it's **Active**, **Acknowledged**, **Resolved** or **Invalid**
* **Type**: **Record** or **Shape**
* **Tag**: tag(s) / label(s) associated with an anomaly
* **Date time**: date/time when the anomaly was found

## API Payload Examples

### Running a Scan operation

This section provides a sample payload for running a scan operation. Replace the placeholder values with actual data relevant to your setup.

#### Endpoint (Post)

`/api/operations/run` _(post)_

=== "Running a scan operation of all containers"
    * **container_names**: `[]` means that it’s going to scan all containers
    * **max_records_analyzed_per_partition**: `null` means that it’s going to scan all records of all containers
    * **Remediation**: `append` Replicate source containers using an append-first strategy 

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
=== "Running a scan operation of specific containers"
    * **container_names**: `["table_name_1", "table_name_2"]` means that it’s going to scan only the tables table_name_1 and table_name_2
    * **max_records_analyzed_per_partition**: `1000000` means that it’s going to scan at maximum 1 million of the containers
    * **Remediation**: `overwrite` Replicate source containers using an overwrite strategy

    ```json
        {
            "type":"profile",
            "name":null,
            "datastore_id":datastore-id,
            "container_names":[
              "table_name_1",
              "table_name_2"
            ],
            "max_records_analyzed_per_partition":1000000,
            "enrichment_source_record_limit":10
        }
    ```

### Scheduling a Scan operation

This section provides a sample payload for scheduling a scan operation. Replace the placeholder values with actual data relevant to your setup.

#### Endpoint (Post)

`/api/operations/schedule` _(post)_

This payload is to run a scheduled scan operation every day at 00:00

=== "Scheduling scan operation of all containers"
    ```json
        {
            "type":"scan",
            "name":"My scheduled Scan operation",
            "datastore_id":"datastore-id",
            "container_names":[],
            "remediation": "overwrite"
            "incremental": false,
            "max_records_analyzed_per_partition":null,
            "enrichment_source_record_limit":10,
            "crontab":"00 00 */2 * *"
        }
    ```

### Retrieving Scan Operation Information

#### Endpoint (Get)

`/api/operations/{id}` _(get)_

=== "Example result response"
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
