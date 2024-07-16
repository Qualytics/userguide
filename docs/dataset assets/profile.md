# Profile Operation

A Profile Operation will analyze every available record in all available Containers in a datastore. Full Profiles provide the benefit of generating metadata with 100% fidelity at the cost of maximum compute time.

The Profile Operation is executed on a Datastore to analyze the named collections of data (tables, files, etc.) within it. The operation will:

* Identify the fields within the collection
* Gather statistical data about each field according to its declared or inferred type
* Submit that metadata to the Qualytics Inference Engine to produce appropriate data quality checks
* Test the inferred data quality checks against actual source data to tune with desired sensitivities


!!! note
    Profile Operations can be run at any time to update the inferred data quality checks automatically based on new data in the Datastore. It's recommended to run Profile operations periodically to update inferred rules.

## Configuration

![Screenshot](../assets/operations/operation-profile-light.png#only-light)
![Screenshot](../assets/operations/operation-profile-dark.png#only-dark)

A Profile Operation can be configured with the following options:

* **Record limit**: Profile only a subset of the available data
* **Disable Check Inference**: Update field metadata without adjusting or infering data quality checks
* **Target selection**
    - All tables/files
    - Subset of available named collections (tables, files, etc.)
    - Selection of collections based on tags

    ![Screenshot](../assets/operations/operation-profile-specific-tables-light.png#only-light)
    ![Screenshot](../assets/operations/operation-profile-specific-tables-dark.png#only-dark)

* **Schedule Options**: There's also an option to schedule the operation by:
    - **Hourly**
    - **Daily**
    - **Weekly**
    - **Monthly**
    - **Advanced**
        - Cron job expression

![Screenshot](../assets/operations/scheduling-a-profile-light.png#only-light)
![Screenshot](../assets/operations/scheduling-a-profile-dark.png#only-dark)

## API Payload Examples

### Running a Profile operation

This section provides a sample payload for running a profile operation. Replace the placeholder values with actual data relevant to your setup.

#### Endpoint (Post)

`/api/operations/run` _(post)_

=== "Running a profile operation of all containers"
    * **container_names**: `[]` means that it’s going to profile all containers
    * **max_records_analyzed_per_partition**: `null` means that it’s going to profile all records of all containers
    * **infer_constraints**: `false` means that the engine is going to infer quality checks for you

    ```json
        {
            "type":"profile",
            "datastore_id": datastore-id,
            "container_names":[],
            "max_records_analyzed_per_partition":null,
            "infer_constraints":true
        }
    ```
=== "Running a profile operation of specific containers"
    * **container_names**: `["table_name_1", "table_name_2"]` means that it’s going to profile only the tables table_name_1 and table_name_2
    * **max_records_analyzed_per_partition**: `1000000` means that it's going to profile at maximum 1 million rowsof the containers
    * **infer_constraints**: `false` means that the engine is not going to infer quality checks

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

This section provides a sample payload for scheduling a profile operation. Replace the placeholder values with actual data relevant to your setup.

#### Endpoint (Post)

`/api/operations/schedule` _(post)_

This payload is to run a scheduled profile operation every day at 00:00

=== "Scheduling profile operation of all containers"
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

#### Endpoint (Get)

`/api/operations/{id}` _(get)_

### Retrieving Profile Operation Information

#### Endpoint (Get)

`/api/operations/{id}` _(get)_

=== "Example result response"
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
