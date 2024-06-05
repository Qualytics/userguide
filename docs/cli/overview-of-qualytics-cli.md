# Qualytics CLI

Qualytics CLI is a command-line tool designed to interact with the Qualytics API. With this tool, users can manage configurations, export and import checks, run operations and more.

You can check more the latest version in [Qualytics CLI](https://pypi.org/project/qualytics-cli/)

## Installation and Upgrading

You can install `Qualytics CLI` via pip:
```bash
pip install qualytics-cli
```

You can upgrade the `Qualytics CLI` via pip:

```bash
pip install qualytics-cli --upgrade
```

## Usage

### Help

To view available commands and their usage:

```bash
qualytics --help
```    

### Initializing Configuration

To set up your Qualytics URL and token:
=== "Bash Example"
    ```bash
        qualytics init 
            --url "https://your-qualytics.qualytics.io/" 
            --token "YOUR_TOKEN_HERE"
    ```
=== "Python Example"
    ```python
        import qualytics.qualytics as qualytics
        CLI_TOKEN = "<your-token>"
        AUDIENCE = "https://your-qualytics.qualytics.io/"

        qualytics.init(AUDIENCE, CLI_TOKEN)
    ```
    ```bash
        Configuration saved! 
    ```
Options:

| Option         | Type            | Description      | Default                          | Required |
|----------------|-----------------|------------------|----------------------------------|----------|
| `--url`  | TEXT         | The URL of your Qualytics instance    | None                 | Yes      |
| `--token`  | TEXT         | The personal access token for accessing Qualytics   | None | Yes      |


### Display Configuration

To view the currently saved configuration:

=== "Bash Example"
    ```bash
    qualytics show-config
    ```
=== "Python Example"
    ```python
        import qualytics.qualytics as qualytics
        
        qualytics.show_config()
    ```
    ```bash
        Config file located in: /home/user/.qualytics/config.json
        URL: (https://your-qualytics.qualytics.io/)
        Token: <your-token>
    ```

### Export Checks

To export checks to a file:

=== "Bash Example"
    ```bash
        qualytics checks export 
            --datastore DATASTORE_ID [--containers CONTAINER_IDS] 
            [--tags TAG_NAMES] 
            [--output LOCATION_TO_BE_EXPORTED]
    ```
=== "Python Example"
    ```python
        import qualytics.qualytics as qualytics
        
        DATASTORE_ID = 844
        CONTAINERS = "7504, 6657"
        qualytics.checks_export(
            datastore=DATASTORE_ID, 
            containers=CONTAINERS, 
            tags=None, 
            output="/home/user/.qualytics/data_checks.json"
        )
    ```
    ```bash
        Exporting quality checks... -------------------------------------- 100% 0:00:00
        Total of Quality Checks = 27 
        Total pages = 1 
        Data exported to /home/user/.qualytics/data_checks.json
    ```
Options:

| Option         | Type            | Description      | Default                            | Required |
|----------------|-----------------|------------------|------------------------------------|---------|
| `--datastore`  | INTEGER         | Datastore ID     | None                               | Yes     |
| `--containers` | List of INTEGER | Containers IDs   | None                               | No      |
| `--tags`       | List of TEXT    | Tag names        | None                               | No      |
| `--output`     | TEXT            | Output file path | `$HOME/.qualytics/data_checks.json`      | No      |


### Export Check Templates

To export check templates:

=== "Bash Example"
    ```bash
    qualytics checks export-templates 
        --enrichment_datastore_id 123 
        [--check_templates "1, 2, 3" or "[1,2,3]"]
        [--status `true` or `false`]
        [--rules "afterDateTime, aggregationComparison" or "[afterDateTime, aggregationComparison]"]
        [--tags "tag1, tag2, tag3" or "[tag1, tag2, tag3]"]
        [--output "/home/user/.qualytics/data_checks_template.json"]
    ```
=== "Python Example to enrichment"
    ```python
        import qualytics.qualytics as qualytics
        
        ENRICH_DATASTORE_ID = 597
        CHECK_TEMPLATES = "182716, 179514"
        qualytics.check_templates_export(
            enrich_datastore_id=ENRICH_DATASTORE_ID,
            check_templates=CHECK_TEMPLATES,
            status=None,
            rules=None,
            tags=None
        )
    ```
    ```bash
        The check templates were exported to the table `_export_check_templates` to enrichment id: 597.
    ```
=== "Python Example to local (output destination)"
    ```python
        import qualytics.qualytics as qualytics
        
        ENRICH_DATASTORE_ID = 597
        CHECK_TEMPLATES = "182716, 179514"
        qualytics.check_templates_export(
            enrich_datastore_id=None,
            check_templates=CHECK_TEMPLATES,
            status=None,
            rules=None,
            tags=None,
            output="/home/user/.qualytics/data_checks_template.json"
        )
    ```
    ```bash
        Exporting quality checks... -------------------------------------- 100% 0:00:01
        Total of Check Templates = 123 
        Total pages = 2 
        Data exported to /home/user/.qualytics/data_checks_template.json
    ```
Options:

| Option        | Type     | Description                                                                | Default                            | Required |
|---------------|----------|----------------------------------------------------------------------------|------------------------------------|----------|
| `--enrichment_datastore_id` | INTEGER  | The ID of the enrichment datastore where check templates will be exported.| Yes      |
| `--check_templates`    | TEXT     | IDs of specific check templates to export (comma-separated or array-like). | No       |
| `--status`    | BOOL     | Check Template status send `true` if it's locked or `false` to unlocked.| No       | No       |
| `--rules`    | TEXT     | Comma-separated list of check templates rule types or array-like format. Example: "afterDateTime, aggregationComparison" or "[afterDateTime, aggregationComparison]".| No       | No       |
| `--tags`    | TEXT     | Comma-separated list of Tag names or array-like format. Example: "tag1, tag2, tag3" or "[tag1, tag2, tag3]".| No       | No       |
| `--output`    | TEXT     |  Output file path [example: `/home/user/.qualytics/data_checks_template.json`].| No       | No       |



### Import Checks

To import checks from a file:
=== "Bash Example"
    ```bash
    qualytics checks import 
        --datastore DATASTORE_ID_LIST 
        [--input LOCATION_FROM_THE_EXPORT]
    ```
=== "Python Example"
    ```python
        import qualytics.qualytics as qualytics
        
        TARGET_DATASTORE_ID = 1172
        qualytics.checks_import(
            datastore=TARGET_DATASTORE_ID, 
            input_file="/home/user/.qualytics/data_checks.json"
        )
    ```
    ```bash
        Quality check id: 195646 for container: CUSTOMER created successfully
        Quality check id: 195647 for container: CUSTOMER created successfully
        Quality check id: 195648 for container: CUSTOMER created successfully
        Quality check id: 195649 for container: CUSTOMER created successfully
        Quality check id: 195650 for container: CUSTOMER created successfully
        Quality check id: 195651 for container: CUSTOMER created successfully
        Quality check id: 195652 for container: CUSTOMER created successfully
        Quality check id: 195653 for container: CUSTOMER created successfully
        Quality check id: 195654 for container: CUSTOMER created successfully
    ```

Options:

| Option       | Type | Description                                                          | Default                       | Required |
|--------------|------|----------------------------------------------------------------------|-------------------------------|----------|
| `--datastore`| TEXT | Datastore IDs to import checks into (comma-separated or array-like). | None                          | Yes      |
| `--input`    | TEXT | Input file path                                                     | HOME/.qualytics/data_checks.json | No       |


_Note_: Errors during import will be logged in `$HOME/.qualytics/errors.log`.

### Run a Catalog Operation on a Datastore

Allows you to trigger a catalog operation on any current datastore (datastore permission required by admin)

<!-- ![Screenshot](../assets/cli/qualytics-run-catalog.gif) -->
=== "Bash Example"
    ```bash
        qualytics run catalog 
            --datastore "DATSTORE_ID_LIST" 
            --include "INCLUDE_LIST" 
            --prune 
            --recreate 
            --background
    ```
=== "Python Example"
    ```python
        import qualytics.qualytics as qualytics
        
        DATASTORE_ID = "1172"
        qualytics.catalog_operation(
            datastores=DATASTORE_ID, 
            include=None,
            prune=None ,
            recreate=None,
            background=False
        )
    ```
    ```bash
        Started Catalog operation 29464 for datastore: 1172 
        Waiting for operation to finish
        Waiting for operation to finish
        Waiting for operation to finish
        Successfully Finished Catalog operation 29464for datastore: 1172 
        Processing... ---------------------------------------- 100% 0:00:29
    ```
Options:

| Option              | Type     | Description                                                                                                               | Required |
|---------------------|----------|---------------------------------------------------------------------------------------------------------------------------|----------|
| `--datastore`      | TEXT     | Comma-separated list of Datastore IDs or array-like format. Example: 1,2,3,4,5 or "[1,2,3,4,5]"                           | Yes      |
| `--include`        | TEXT     | Comma-separated list of include types or array-like format. Example: "table,view" or "[table,view]"                       | No       |
| `--prune`           | BOOL     | Prune the operation. Do not include if you want prune == false                                                           | No       |
| `--recreate`        | BOOL     | Recreate the operation. Do not include if you want recreate == false                                                     | No       |
| `--background`      | BOOL     | Starts the catalog but does not wait for the operation to finish                                                         | No       |


### Run a Profile Operation on a Datastore

Allows you to trigger a profile operation on any current datastore (datastore permission required by admin)
=== "Bash Example"
    ```bash
    qualytics run profile 
        --datastore "DATSTORE_ID_LIST" 
        --container_names "CONTAINER_NAMES_LIST" 
        --container_tags "CONTAINER_TAGS_LIST"
        --infer_constraints 
        --max_records_analyzed_per_partition "MAX_RECORDS_ANALYZED_PER_PARTITION" 
        --max_count_testing_sample "MAX_COUNT_TESTING_SAMPLE"
        --percent_testing_threshold "PERCENT_TESTING_THRESHOLD" 
        --high_correlation_threshold "HIGH_CORRELATION_THRESHOLD" 
        --greater_then_date "GREATER_THAN_TIME"
        --greater_than_batch "GREATER_THAN_BATCH" 
        --histogram_max_distinct_values "HISTOGRAM_MAX_DISTINCT_VALUES" 
        --background
    ```
=== "Python Example"
    ```python
        import qualytics.qualytics as qualytics
        
        DATASTORE_ID = "844"
        CONTAINER_NAMES = "CUSTOMER, NATION"
        qualytics.profile_operation(
            datastores=DATASTORE_ID,
            container_names=CONTAINER_NAMES,
            container_tags=None,
            infer_constraints=True,
            max_records_analyzed_per_partition=None,
            max_count_testing_sample=None,
            percent_testing_threshold=None,
            high_correlation_threshold=None,
            greater_than_time=None,
            greater_than_batch=None,
            histogram_max_distinct_values=None,
            background=False
        )
    ```
    ```bash
        Successfully Started Profile 29466 for datastore: 844 
        Waiting for operation to finish
        Waiting for operation to finish
        Waiting for operation to finish
        Waiting for operation to finish
        Waiting for operation to finish
        Waiting for operation to finish
        Successfully Finished Profile operation 29466 for datastore: 844 
        Processing... ---------------------------------------- 100% 0:00:46
    ```
Options:

| Option                                 | Type     | Description                                                                                                                                      | Required |
|----------------------------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------|----------|
| `--datastore`                          | TEXT     | Comma-separated list of Datastore IDs or array-like format. Example: 1,2,3,4,5 or "[1,2,3,4,5]"                                                  | Yes      |
| `--container_names`                    | TEXT     | Comma-separated list of include types or array-like format. Example: "container1,container2" or "[container1,container2]"                        | No       |
| `--container_tags`                     | TEXT     | Comma-separated list of include types or array-like format. Example: "tag1,tag2" or "[tag1,tag2]"                                                | No       |
| `--infer_constraints`                  | BOOL     | Infer quality checks in profile. Do not include if you want infer_constraints == false                                                           | No       |
| `--max_records_analyzed_per_partition` | INT      | Number of max records analyzed per partition                                                                                                     | No       |
| `--max_count_testing_sample`           | INT      | The number of records accumulated during profiling for validation of inferred checks. Capped at 100,000                                          | No       |
| `--percent_testing_threshold`          | FLOAT    | Percent of testing threshold                                                                                                                     | No       |
| `--high_correlation_threshold`         | FLOAT    | Number of Correlation Threshold                                                                                                                  | No       |
| `--greater_than_time`                  | DATETIME | Only include rows where the incremental field's value is greater than this time. Use one of these formats %Y-%m-%dT%H:%M:%S or %Y-%m-%d %H:%M:%S | No       |
| `--greater_than_batch`                 | FLOAT    | Only include rows where the incremental field's value is greater than this number                                                                | No       |
| `--histogram_max_distinct_values`      | INT      | Number of max distinct values of the histogram                                                                                                   | No       |
| `--background`                         | BOOL     | Starts the catalog but does not wait for the operation to finish                                                                                 | No       |

### Run a Scan Operation on a Datastore

Allows you to trigger a scan operation on a datastore (datastore permission required by admin)

<!-- ![Screenshot](../assets/cli/qualytics-run-scan-background.gif) -->
=== "Bash Example"
    ```bash
    qualytics run scan 
        --datastore "DATSTORE_ID_LIST"
        --container_names "CONTAINER_NAMES_LIST" 
        --container_tags "CONTAINER_TAGS_LIST"
        --incremental 
        --remediation 
        --max_records_analyzed_per_partition "MAX_RECORDS_ANALYZED_PER_PARTITION" 
        --enrichment_source_records_limit
        --greater_then_date "GREATER_THAN_TIME" 
        --greater_than_batch "GREATER_THAN_BATCH" 
        --background
    ```
=== "Python Example"
    ```python
        import qualytics.qualytics as qualytics
        
        DATASTORE_ID = 1172
        CONTAINER_NAMES = "CUSTOMER, NATION"
        qualytics.scan_operation(
            datastores=str(DATASTORE_ID),
            container_names=None,
            container_tags=None,
            incremental=False,
            remediation="none",
            enrichment_source_record_limit=10,
            greater_than_batch=None,
            greater_than_time=None,
            max_records_analyzed_per_partition=10000,
            background=False
        )
    ```
    ```bash
        Successfully Started Scan 29467 for datastore: 1172 
        Waiting for operation to finish
        Waiting for operation to finish
        Waiting for operation to finish
        Waiting for operation to finish
        Waiting for operation to finish
        Successfully Finished Scan operation 29467 for datastore: 1172 
        Processing... ---------------------------------------- 100% 0:03:04
    ```

Options:

| Option                                 | Type     | Description                                                                                                                                      | Required |
|----------------------------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------|----------|
| `--datastore`                          | TEXT     | Comma-separated list of Datastore IDs or array-like format. Example: 1,2,3,4,5 or "[1,2,3,4,5]"                                                  | Yes      |
| `--container_names`                    | TEXT     | Comma-separated list of include types or array-like format. Example: "container1,container2" or "[container1,container2]"                        | No       |
| `--container_tags`                     | TEXT     | Comma-separated list of include types or array-like format. Example: "tag1,tag2" or "[tag1,tag2]"                                                | No       |
| `--incremental`                        | BOOL     | Process only new or records updated since the last incremental scan                                                                              | No       |
| `--remediation`                        | TEXT     | Replication strategy for source tables in the enrichment datastore. Either 'append', 'overwrite', or 'none'                                      | No       |
| `--max_records_analyzed_per_partition` | INT      | Number of max records analyzed per partition. Value must be Greater than or equal to 0                                                           | No       |
| `--enrichment_source_record_limit`     | INT      | Limit of enrichment source records per . Value must be Greater than or equal to -1                                                               | No       |
| `--greater_than_date`                  | DATETIME | Only include rows where the incremental field's value is greater than this time. Use one of these formats %Y-%m-%dT%H:%M:%S or %Y-%m-%d %H:%M:%S | No       |
| `--greater_than_batch`                 | FLOAT    | Only include rows where the incremental field's value is greater than this number                                                                | No       |
| `--background`                         | BOOL     | Starts the catalog but does not wait for the operation to finish                                                                                 | No       |

_Note_: Errors during any of the three operations will be logged in `$HOME/.qualytics/operation-error.log`.

### Check Operation Status

To check the status of operations:
=== "Bash Example"
    ```bash
    qualytics operation check_status 
        --ids "OPERATION_IDS"
    ```
=== "Python Example"
    ```python
        import qualytics.qualytics as qualytics
        
        qualytics.operation_status(ids="29468")
    ```
    ```bash
        Operation: 29468 is still running 
        Processing... ---------------------------------------- 100% 0:00:00
    ```

<!-- ![Screenshot](../assets/cli/qualytics-operation-aborted.gif)
![Screenshot](../assets/cli/qualytics-operation-running.gif)
![Screenshot](../assets/cli/qualytics-operation-success.gif) -->


Options:

| Option              | Type     | Description                                                                                                               | Required |
|---------------------|----------|---------------------------------------------------------------------------------------------------------------------------|----------|
| `--ids`             | TEXT     | Comma-separated list of Operation IDs or array-like format. Example: 1,2,3,4,5 or "[1,2,3,4,5]"                           | Yes      |
