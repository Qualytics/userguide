# What is an Enrichment Datastore?

* An `Enrichment Datastore` is a `Datastore` that is used to record the results (`anomalies` and associated `metadata`) of a Scan Operation.  Those results include the original source data `enriched` with data such as an anomaly identifier, the type of rule that the anomaly violates, any custom tags associated with the relevant data assets, etc...

!!! info
    Before running a Scan Operation, the user should configure an Enrichment Datastore for each datastore.

## Enrichment Data Structure

Within the `Enrichment Datastore`, data for each scanned data asset (Table, View, Fileset, etc..) is recorded in two tables with the structure (defined here in Spark SQL DDL):

```
CREATE OR REPLACE TABLE _DATA_ASSET_NAME_ANOMALIES (
	QUALITY_CHECK_ID BIGINT,
	ANOMALY_UUID STRING,
	QUALITY_CHECK_MESSAGE STRING,
	SUGGESTED_REMEDIATION_FIELD STRING,
	SUGGESTED_REMEDIATION_VALUE STRING,
	SUGGESTED_REMEDIATION_SCORE FLOAT,
	QUALITY_CHECK_RULE_TYPE STRING,
	QUALITY_CHECK_TAGS STRING,
	QUALITY_CHECK_PARAMETERS STRING,
	QUALITY_CHECK_DESCRIPTION STRING,
	OPERATION_ID BIGINT,
	DETECTED_TIME TIMESTAMP,
	SOURCE_CONTAINER STRING,
	SOURCE_PARTITION STRING,
	SOURCE_DATASTORE STRING
)

CREATE OR REPLACE TABLE _DATA_ASSET_NAME_SOURCE_RECORDS (
	SOURCE_CONTAINER STRING,
	SOURCE_PARTITION STRING,
	ANOMALY_UUID STRING,
	CONTEXT STRING,
	RECORD STRING -- this field holds the source record as a json object
)

```
