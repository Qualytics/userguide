# Metadata Tables

The Qualytics platform enables users to manually export metadata into the enrichment datastore, providing a structured approach to data analysis and management. These metadata tables are structured to reflect the evolving characteristics of data entities, primarily focusing on aspects that are subject to changes.

Currently, the following assets are available for exporting:

- _<enrichment_prefix\>_export_anomalies
- _<enrichment_prefix\>_export_checks
- _<enrichment_prefix\>_export_field_profiles

!!! Note
	The strategy used for managing these metadata tables employs a `create or replace` approach, meaning that the export process will create a new table if one does not exist, or replace it entirely if it does. This means that any previous data will be overwritten.
	
	For more detailed information on exporting metadata, please refer to the [export operation documentation](../container/export-operation.md)

## _EXPORT_ANOMALIES Table

Contains metadata from anomalies in a distinct normalized format. This table is specifically designed to capture the mutable states of anomalies, emphasizing their status changes.

**Columns**

| Name             | Data Type | Description                                     |
|------------------|-----------|-------------------------------------------------|
| ID               | NUMBER    | Unique identifier for the anomaly.              |
| CREATED          | TIMESTAMP | Timestamp of anomaly creation.                  |
| UUID             | UUID      | Universal Unique Identifier of the anomaly.     |
| TYPE             | STRING    | Type of the anomaly (e.g., 'shape').            |
| STATUS           | STRING    | Current status of the anomaly (e.g., 'Active'). |
| GLOBAL_TAGS      | STRING    | Tags associated globally with the anomaly.      |
| CONTAINER_ID     | NUMBER    | Identifier for the associated container.        |
| SOURCE_CONTAINER | STRING    | Name of the source container.                   |
| DATASTORE_ID     | NUMBER    | Identifier for the associated datastore.        |
| SOURCE_DATASTORE | STRING    | Name of the source datastore.                   |
| GENERATED_AT     | TIMESTAMP | Timestamp when the export was generated.        |

## _EXPORT_CHECKS Table

Contains metadata from quality checks.

**Columns**

| Name                  | Data Type          | Description                                                     |
|-----------------------|--------------------|-----------------------------------------------------------------|
| ADDITIONAL_METADATA   | STRING             | JSON-formatted string containing additional metadata for the check. |
| COVERAGE              | FLOAT              | Represents the expected tolerance of the rule.                  |
| CREATED               | STRING             | Created timestamp of the check.                                 |
| DELETED_AT            | STRING             | Deleted timestamp of the check.                                 |
| DESCRIPTION           | STRING             | Description of the check.                                       |
| FIELDS                | STRING             | Fields involved in the check separated by comma.                |
| FILTER                | STRING             | Criteria used to filter data when asserting the check.          |
| GENERATED_AT          | STRING             | Indicates when the export was generated.                        |
| GLOBAL_TAGS           | STRING             | Represents the global tags of the check separated by comma.     |
| HAS_PASSED            | BOOLEAN            | Boolean indicator of whether the check has passed its last assertion . |
| ID                    | NUMBER             | Unique identifier for the check.                                |
| INFERRED              | BOOLEAN            | Indicates whether the check was inferred by the platform.       |
| IS_NEW                | BOOLEAN            | Flags if the check is new.                                      |
| LAST_ASSERTED         | STRING             | Timestamp of the last assertion performed on the check.         |
| LAST_EDITOR           | STRING             | Represents the last editor of the check.                        |
| LAST_UPDATED          | STRING             | Represents the last updated timestamp of the check.             |
| NUM_CONTAINER_SCANS   | NUMBER             | Number of containers scanned.                                   |
| PROPERTIES            | STRING             | Specific properties for the check in a JSON format.             |
| RULE_TYPE             | STRING             | Type of rule applied in the check.                              |
| WEIGHT                | FLOAT              | Represents the weight of the check.                             |
| DATASTORE_ID          | NUMBER         	 | Identifier of the datastore used in the check.                  |
| CONTAINER_ID          | NUMBER         	 | Identifier of the container used in the check.                  |
| TEMPLATE_ID           | NUMBER         	 | Identifier of the template id associated to the check.           |
| IS_TEMPLATE           | BOOLEAN         	 | Indicates whether the check is a template or not.                |
| SOURCE_CONTAINER      | STRING             | Name of the container used in the check.                        |
| SOURCE_DATASTORE      | STRING             | Name of the datastore used in the check.                        |

## _EXPORT_CHECK_TEMPLATES Table

Contains metadata from check templates.

**Columns**

| Name                  | Data Type          | Description                                                     |
|-----------------------|--------------------|-----------------------------------------------------------------|
| ADDITIONAL_METADATA   | STRING             | JSON-formatted string containing additional metadata for the check. |
| COVERAGE              | FLOAT              | Represents the expected tolerance of the rule.                  | 
| CREATED               | STRING             | Created timestamp of the check.                                 | 
| DELETED_AT            | STRING             | Deleted timestamp of the check.                                 | 
| DESCRIPTION           | STRING             | Description of the check.                                       | 
| FIELDS                | STRING             | Fields involved in the check separated by comma.                | 
| FILTER                | STRING             | Criteria used to filter data when asserting the check.          | 
| GENERATED_AT          | STRING             | Indicates when the export was generated.                        |  
| GLOBAL_TAGS           | STRING             | Represents the global tags of the check separated by comma.     | 
| ID                    | NUMBER             | Unique identifier for the check.                                | 
| IS_NEW                | BOOLEAN            | Flags if the check is new.                                      | 
| IS_TEMPLATE           | BOOLEAN         	 | Indicates whether the check is a template or not.               | 
| LAST_EDITOR           | STRING             | Represents the last editor of the check.                        | 
| LAST_UPDATED          | STRING             | Represents the last updated timestamp of the check.             | 
| PROPERTIES            | STRING             | Specific properties for the check in a JSON format.             | 
| RULE_TYPE             | STRING             | Type of rule applied in the check.                              | 
| TEMPLATE_CHECKS_COUNT | NUMBER             | The count of associated checks to the template.                 | 
| TEMPLATE_LOCKED       | BOOLEAN            | Indicates whether the check template is locked or not.          | 
| WEIGHT                | FLOAT              | Represents the weight of the check.                             |

## _EXPORT_FIELD_PROFILES Table

Contains metadata from field profiles.

**Columns**

| Name                      | Data Type          | Description                                                      |
|---------------------------|--------------------|------------------------------------------------------------------|
| APPROXIMATE_DISTINCT_VALUES | FLOAT            | Estimated number of distinct values in the field.                |
| COMPLETENESS              | FLOAT              | Ratio of non-null entries to total entries in the field.         |
| CONTAINER_ID              | NUMBER             | Identifier for the container holding the field.                  |
| SOURCE_CONTAINER          | STRING             | Name of the container holding the field.                         |
| CONTAINER_STORE_TYPE      | STRING             | Storage type of the container.                                   |
| CREATED                   | STRING             | Date when the field profile was created.                         |
| DATASTORE_ID              | NUMBER             | Identifier for the datastore containing the field.               |
| SOURCE_DATASTORE          | STRING             | Name of the datastore containing the field.                      |
| DATASTORE_TYPE            | STRING             | Type of datastore.                                               |
| ENTROPY                   | FLOAT              | Measure of randomness in the information being processed.        |
| FIELD_GLOBAL_TAGS         | STRING             | Global tags associated with the field.                           |
| FIELD_ID                  | NUMBER             | Unique identifier for the field.                                 |
| FIELD_NAME                | STRING             | Name of the field being profiled.                                |
| FIELD_PROFILE_ID          | NUMBER             | Identifier for the field profile record.                         |
| FIELD_QUALITY_SCORE       | FLOAT              | Score representing the quality of the field.                     |
| FIELD_TYPE                | STRING             | Data type of the field.                                          |
| FIELD_WEIGHT              | NUMBER             | Weight assigned to the field for quality scoring.                |
| GENERATED_AT              | STRING             | Date when the field profile was generated.                       |
| HISTOGRAM_BUCKETS         | STRING             | Distribution of data within the field represented as buckets.    |
| IS_NOT_NORMAL             | BOOLEAN            | Indicator of whether the field data distribution is not normal.  |
| KLL                       | STRING             | Sketch summary of the field data distribution.                   |
| KURTOSIS                  | FLOAT              | Measure of the tailedness of the probability distribution.       |
| MAX                       | FLOAT              | Maximum value found in the field.                                |
| MAX_LENGTH                | FLOAT              | Maximum length of string entries in the field.                   |
| MEAN                      | FLOAT              | Average value of the field's data.                               |
| MEDIAN                    | FLOAT              | Middle value in the field's data distribution.                   |
| MIN                       | FLOAT              | Minimum value found in the field.                                |
| MIN_LENGTH                | FLOAT              | Minimum length of string entries in the field.                   |
| NAME                      | STRING             | Descriptive name of the field.                                   |
| Q1                        | FLOAT              | First quartile in the field's data distribution.                 |
| Q3                        | FLOAT              | Third quartile in the field's data distribution.                 |
| SKEWNESS                  | FLOAT              | Measure of the asymmetry of the probability distribution.        |
| STD_DEV                   | FLOAT              | Standard deviation of the field's data.                          |
| SUM                       | FLOAT              | Sum of all numerical values in the field.                        |
| TYPE_DECLARED             | BOOLEAN            | Indicator of whether the field type is explicitly declared.      |
| UNIQUE_DISTINCT_RATIO     | FLOAT              | Ratio of unique distinct values to the total distinct values.    |