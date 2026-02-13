# API Payload Examples

## Retrieving Enrichment Datastore Tables

### Endpoint (Get)

`/api/datastores/{enrichment-datastore-id}/listing` _(get)_


=== "Example result response"
    ```json
		[
			{
				"name":"_datastore_prefix_scan_operations",
				"label":"scan_operations",
				"datastore":{
					"id":123,
					"name":"My Datastore",
					"store_type":"jdbc",
					"type":"postgresql",
					"enrich_only":false,
					"enrich_container_prefix":"_datastore_prefix",
					"favorite":false
				}
			},
			{
				"name":"_datastore_prefix_source_records",
				"label":"source_records",
				"datastore":{
					"id":123,
					"name":"My Datastore",
					"store_type":"jdbc",
					"type":"postgresql",
					"enrich_only":false,
					"enrich_container_prefix":"_datastore_prefix",
					"favorite":false
				}
			},
			{
				"name":"_datastore_prefix_failed_checks",
				"label":"failed_checks",
				"datastore":{
					"id":123,
					"name":"My Datastore",
					"store_type":"jdbc",
					"type":"postgresql",
					"enrich_only":false,
					"enrich_container_prefix":"_datastore_prefix",
					"favorite":false
				}
			},
			{
				"name": "_datastore_prefix_remediation_container_id",
				"label": "table_name",
				"datastore": {
					"id": 123,
					"name": "My Datastore",
					"store_type": "jdbc",
					"type": "postgresql",
					"enrich_only": false,
					"enrich_container_prefix": "_datastore_prefix",
					"favorite": false
				}
			}
		]
	```

## Retrieving Enrichment Datastore Source Records

### Endpoint (Get)

`/api/datastores/{enrichment-datastore-id}/source-records?path={_source-record-table-prefix}` _(get)_

### Endpoint With Filters (Get)

`/api/datastores/{enrichment-datastore-id}/source-records?filter=anomaly_uuid='{uuid}'&path={_source-record-table-prefix}` _(get)_

=== "Example result response"
    ```json
		{
			"source_records": "[{\"source_container\":\"table_name\",\"source_partition\":\"partition_name\",\"anomaly_uuid\":\"f11d4e7c-e757-4bf1-8cd6-d156d5bc4fa5\",\"context\":null,\"record\":\"{\\\"P_NAME\\\":\\\"\\\\\\\"strategize intuitive systems\\\\\\\"\\\",\\\"P_TYPE\\\":\\\"\\\\\\\"Radiographer, therapeutic\\\\\\\"\\\",\\\"P_RETAILPRICE\\\":\\\"-24.69\\\",\\\"LAST_MODIFIED_TIMESTAMP\\\":\\\"2023-09-29 11:17:19.048\\\",\\\"P_MFGR\\\":null,\\\"P_COMMENT\\\":\\\"\\\\\\\"Other take so.\\\\\\\"\\\",\\\"P_PARTKEY\\\":\\\"845004850\\\",\\\"P_SIZE\\\":\\\"4\\\",\\\"P_CONTAINER\\\":\\\"\\\\\\\"MED BOX\\\\\\\"\\\",\\\"P_BRAND\\\":\\\"\\\\\\\"PLC\\\\\\\"\\\"}\"}]"
		}
	```

## Retrieving Enrichment Datastore Remediation

### Endpoint (Get)

`/api/datastores/{enrichment-datastore-id}/source-records?path={_remediation-table-prefix}` _(get)_

### Endpoint With Filters (Get)
`/api/datastores/{enrichment-datastore-id}/source-records?filter=anomaly_uuid='{uuid}'&path={_remediation-table-prefix}` _(get)_

=== "Example result response"
    ```json
		{
			"source_records": "[{\"source_container\":\"table_name\",\"source_partition\":\"partition_name\",\"anomaly_uuid\":\"f11d4e7c-e757-4bf1-8cd6-d156d5bc4fa5\",\"context\":null,\"record\":\"{\\\"P_NAME\\\":\\\"\\\\\\\"strategize intuitive systems\\\\\\\"\\\",\\\"P_TYPE\\\":\\\"\\\\\\\"Radiographer, therapeutic\\\\\\\"\\\",\\\"P_RETAILPRICE\\\":\\\"-24.69\\\",\\\"LAST_MODIFIED_TIMESTAMP\\\":\\\"2023-09-29 11:17:19.048\\\",\\\"P_MFGR\\\":null,\\\"P_COMMENT\\\":\\\"\\\\\\\"Other take so.\\\\\\\"\\\",\\\"P_PARTKEY\\\":\\\"845004850\\\",\\\"P_SIZE\\\":\\\"4\\\",\\\"P_CONTAINER\\\":\\\"\\\\\\\"MED BOX\\\\\\\"\\\",\\\"P_BRAND\\\":\\\"\\\\\\\"PLC\\\\\\\"\\\"}\"}]"
		}
	```

## Retrieving Enrichment Datastore Failed Checks

### Endpoint (Get)

`/api/datastores/{enrichment-datastore-id}/source-records?path={_failed-checks-table-prefix}` _(get)_


### Endpoint With Filters (Get)

`/api/datastores/{enrichment-datastore-id}/source-records?filter=anomaly_uuid='{uuid}'&path={_failed-checks-table-prefix}` _(get)_


=== "Example result response"
    ```json
		{
			"source_records": "[{\"quality_check_id\":155481,\"anomaly_uuid\":\"1a937875-6bce-4bfe-8701-075ba66be364\",\"quality_check_message\":\"{\\\"SNPSHT_TIMESTAMP\\\":\\\"2023-09-03 10:26:15.0\\\"}\",\"suggested_remediation_field\":null,\"suggested_remediation_value\":null,\"suggested_remediation_score\":null,\"quality_check_rule_type\":\"greaterThanField\",\"quality_check_tags\":\"Time-Sensitive\",\"quality_check_parameters\":\"{\\\"field_name\\\":\\\"SNPSHT_DT\\\",\\\"inclusive\\\":false}\",\"quality_check_description\":\"Must have a value greater than the value of SNPSHT_DT\",\"operation_id\":28162,\"detected_time\":\"2024-03-29T15:08:07.585Z\",\"source_container\":\"ACTION_TEST_CLIENT_V3\",\"source_partition\":\"ACTION_TEST_CLIENT_V3\",\"source_datastore\":\"DB2 Dataset\"}]"
		}
	```

## Retrieving Enrichment Datastore Scan Operations

### Endpoint (Get)

`/api/datastores/{enrichment-datastore-id}/source-records?path={_scan-operations-table-prefix}` _(get)_

### Endpoint With Filters (Get)

`/api/datastores/{enrichment-datastore-id}/source-records?filter=operation_id='{operation-id}'&path={_scan-operations-table-prefix}` _(get)_

=== "Example result response"
    ```json
		{
			"source_records": "[{\"operation_id\":22871,\"datastore_id\":850,\"container_id\":7239,\"container_scan_id\":43837,\"partition_name\":\"ACTION_TEST_CLIENT_V3\",\"incremental\":true,\"records_processed\":0,\"enrichment_source_record_limit\":10,\"max_records_analyzed\":-1,\"anomaly_count\":0,\"start_time\":\"2023-12-04T20:35:54.194Z\",\"end_time\":\"2023-12-04T20:35:54.692Z\",\"result\":\"success\",\"message\":null}]"
		}
	```
	

## Retrieving Enrichment Datastore Exported Metadata

### Endpoint (Get)

`/api/datastores/{enrichment-datastore-id}/source-records?path={_export-metadata-table-prefix}` _(get)_

### Endpoint With Filters (Get)

`/api/datastores/{enrichment-datastore-id}/source-records?filter=container_id='{container-id}'&path={_export-metadata-table-prefix}` _(get)_

=== "Example result of export anomalies response"
    ```json
		{
			"source_records": "[{\"container_id\":13511,\"created\":\"2024-06-10T17:07:20.751438Z\",\"datastore_id\":1198,\"generated_at\":\"2024-06-11 18:42:31+0000\",\"global_tags\":\"\",\"id\":224818,\"source_container\":\"PARTSUPP-FORMATTED.csv\",\"source_datastore\":\"TPCH GCS\",\"status\":\"Active\",\"type\":\"shape\",\"uuid\":\"f2d4fae3-982b-45a1-b289-5854b7af4b03\"}]"
		}
	```

=== "Example result of export checks response"
    ```json
		{
			"source_records": "[{\"additional_metadata\":null,\"container_id\":13515,\"coverage\":1.0,\"created\":\"2024-06-10T16:27:05.600041Z\",\"datastore_id\":1198,\"deleted_at\":null,\"description\":\"Must have a numeric value above >= 0\",\"fields\":\"L_QUANTITY\",\"filter\":null,\"generated_at\":\"2024-06-11 18:42:38+0000\",\"global_tags\":\"\",\"has_passed\":false,\"id\":196810,\"inferred\":true,\"is_new\":false,\"is_template\":false,\"last_asserted\":\"2024-06-11T18:04:24.480899Z\",\"last_editor\":null,\"last_updated\":\"2024-06-10T17:07:43.248644Z\",\"num_container_scans\":4,\"properties\":null,\"rule_type\":\"notNegative\",\"source_container\":\"LINEITEM-FORMATTED.csv\",\"source_datastore\":\"TPCH GCS\",\"template_id\":null,\"weight\":7.0}]"
		}
	```

=== "Example result of field profiles response"
    ```json
		{
			"source_records": "[{\"approximate_distinct_values\":106944.0,\"completeness\":0.7493389459,\"container_container_type\":\"file\",\"container_id\":13509,\"created\":\"2024-06-10T16:23:48.457907Z\",\"datastore_id\":1198,\"datastore_type\":\"gcs\",\"entropy\":null,\"field_global_tags\":\"\",\"field_id\":145476,\"field_name\":\"C_ACCTBAL\",\"field_profile_id\":882170,\"field_quality_score\":\"{\\\"total\\\": 81.70052209952111, \\\"completeness\\\": 74.93389459101233, \\\"coverage\\\": 66.66666666666666, \\\"conformity\\\": null, \\\"consistency\\\": 100.0, \\\"precision\\\": 100.0, \\\"timeliness\\\": null, \\\"volumetrics\\\": null, \\\"accuracy\\\": 100.0}\",\"field_type\":\"Fractional\",\"field_weight\":1,\"generated_at\":\"2024-06-11 18:42:32+0000\",\"histogram_buckets\":null,\"is_not_normal\":true,\"kll\":null,\"kurtosis\":-1.204241522,\"max\":9999.99,\"max_length\":null,\"mean\":4488.8079264033,\"median\":4468.34,\"min\":-999.99,\"min_length\":null,\"name\":\"C_ACCTBAL\",\"q1\":1738.87,\"q3\":7241.17,\"skewness\":0.0051837205,\"source_container\":\"CUSTOMER-FORMATTED.csv\",\"source_datastore\":\"TPCH GCS\",\"std_dev\":3177.3005493585,\"sum\":5.0501333575999904E8,\"type_declared\":false,\"unique_distinct_ratio\":null}]"
		}
	```
