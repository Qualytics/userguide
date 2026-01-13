# Enrichment Tables

When anomalies are detected, the platform writes metadata into four primary enrichment tables:

- <enrichment_prefix\>_check_metrics
- <enrichment_prefix\>_failed_checks
- <enrichment_prefix\>_source_records
- <enrichment_prefix\>_scan_operations

## _CHECK_METRICS_Table

Captures and logs detailed metrics for every data quality check performed within the Qualytics Platform, providing insights into asserted and anomalous records across datasets.

**Columns**

| Name                    | Data Type | Description                                          |
|-----------------------------|---------------|----------------------------------------------------------|
| OPERATION_ID            | NUMBER        | Unique Identifier for the check metric.                 |
| CONTAINER_ID            | NUMBER        | Identifier for the container associated with the check metric. |
| SOURCE_DATASTORE        | STRING        | Datastore where the source data resides.                |
| SOURCE_CONTAINER        | STRING        | Name of the source data container.                      |
| SOURCE_PARTITION        | STRING        | Partition of the source data.                           |
| ASSERTION_RESULT        | STRING        | Result of the check assertion: one of `passed`, `failed`, or `unasserted`.  |
| ASSERTION_DETAILS       | STRING        | Text description explaining any warnings, errors, or notes from the check.                           |
| QUALITY_CHECK_ID        | NUMBER        | Unique identifier for the quality check performed.      |
| ASSERTED_RECORDS_COUNT  | NUMBER        | Count of records expected or asserted in the source.    |
| ANOMALOUS_RECORDS_COUNT | NUMBER        | Count of records identified as anomalous.               |
| _QUALYTICS_SOURCE_PARTITION | STRING    | Partition information specific to Qualytics metrics.    |

## _FAILED_CHECKS Table

Acts as an associative entity that consolidates information on failed checks, associating anomalies with their respective quality checks.

**Columns**

| Name                            | Data Type          | Description                                      |
|---------------------------------|--------------------|--------------------------------------------------|
| QUALITY_CHECK_ID                | NUMBER             | Unique identifier for the quality check.         |
| ANOMALY_UUID                    | STRING             | UUID for the anomaly detected.                   |
| QUALITY_CHECK_MESSAGE           | STRING             | Message describing the quality check outcome.    |
| SUGGESTED_REMEDIATION_FIELD     | STRING             | Field suggesting remediation.                    |
| SUGGESTED_REMEDIATION_VALUE     | STRING             | Suggested value for remediation.                 |
| SUGGESTED_REMEDIATION_SCORE     | FLOAT              | Score indicating confidence in remediation.      |
| QUALITY_CHECK_RULE_TYPE         | STRING             | Type of rule applied for quality check.          |
| QUALITY_CHECK_TAGS              | STRING             | Tags associated with the quality check.          |
| QUALITY_CHECK_PARAMETERS        | STRING             | Parameters used for the quality check.           |
| QUALITY_CHECK_DESCRIPTION       | STRING             | Description of the quality check.                |
| QUALITY_CHECK_METADATA          | STRING             | Optional JSON string containing additional check metadata. |
| OPERATION_ID                    | NUMBER             | Identifier for the operation detecting anomaly.  |
| DETECTED_TIME                   | TIMESTAMP          | Timestamp when the anomaly was detected.         |
| SOURCE_CONTAINER                | STRING             | Name of the source data container.               |
| SOURCE_PARTITION                | STRING             | Partition of the source data.                    |
| SOURCE_DATASTORE                | STRING             | Datastore where the source data resides.         |
| FINGERPRINT                     | INTEGER            | Unique identifier created when Reactivate Recurring Anomalies is enabled.         |

!!! info
	This table is not characterized by unique `ANOMALY_UUID` or `QUALITY_CHECK_ID` values alone. Instead, the combination of `ANOMALY_UUID` and `QUALITY_CHECK_ID` serves as a composite key, uniquely identifying each record in the table.

## _SOURCE_RECORDS Table

Stores source records in JSON format, primarily to enable the preview source record feature in the Qualytics App.

**Columns**

| Name               | Data Type          | Description                               |
|--------------------|--------------------|-------------------------------------------|
| SOURCE_CONTAINER   | STRING             | Name of the source data container.        |
| SOURCE_PARTITION   | STRING             | Partition of the source data.             |
| ANOMALY_UUID       | STRING             | UUID for the associated anomaly.          |
| CONTEXT            | STRING             | Contextual information for the anomaly.   |
| RECORD             | STRING             | JSON representation of the source record. |

## _SCAN_OPERATIONS Table

Captures and stores the results of every scan operation conducted on the Qualytics Platform.

**Columns**

| Name                              | Data Type          | Description                                                            |
|-----------------------------------|--------------------|------------------------------------------------------------------------|
|  OPERATION_ID           			|   NUMBER           | Unique identifier for the scan operation.                              |
|  DATASTORE_ID      			    |   NUMBER         	 | Identifier for the source datastore associated with the operation.     |
|  CONTAINER_ID      			    |   NUMBER         	 | Identifier for the container associated with the operation.            |
|  CONTAINER_SCAN_ID      			|   NUMBER         	 | Identifier for the container scan associated with the operation.       |
|  PARTITION_NAME         			|   STRING           | Name of the source partition on which the scan operation is performed. |
|  INCREMENTAL                      |   BOOLEAN          | Boolean flag indicating whether the scan operation is incremental.     |
|  RECORDS_PROCESSED                |   NUMBER           | Total number of records processed during the scan operation.           |
|  ENRICHMENT_SOURCE_RECORD_LIMIT   |   NUMBER           | Maximum number of records written to the enrichment for each anomaly detected. |
|  MAX_RECORDS_ANALYZED        		|   NUMBER           | Maximum number of records analyzed in the scan operation.              |
|  ANOMALY_COUNT        			|   NUMBER           | Total number of anomalies identified in the scan operation.            |
|  START_TIME        				|   TIMESTAMP        | Timestamp marking the start of the scan operation.                     |
|  END_TIME        					|   TIMESTAMP        | Timestamp marking the end of the scan operation.                       |
|  RESULT        					|   STRING           | Textual representation of the scan operation's status.                 |
|  MESSAGE        					|   STRING           | Detailed message regarding the process of the scan operation.          |