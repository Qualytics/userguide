# Enrichment Table Schema Changelog

This page tracks column additions, removals, and type changes to the four primary enrichment tables. If you manage downstream pipelines or queries that depend on these schemas, review this changelog when upgrading.

!!! tip
    The Qualytics platform automatically migrates existing enrichment tables when schema changes are detected. New columns are added and type changes are applied during the next scan operation that writes to your enrichment datastore.

---

## _scan_operations

| Date | Change | Column | Details |
|------|--------|--------|---------|
| Nov 2023 | **Created** | — | Initial table with `OPERATION_ID`, `CONTAINER_SCAN_ID`, `PARTITION_NAME`, `INCREMENTAL`, `RECORDS_PROCESSED`, `ENRICHMENT_SOURCE_RECORD_LIMIT`, `MAX_RECORDS_ANALYZED`, `ANOMALY_COUNT`, `START_TIME`, `END_TIME`, `RESULT`, `MESSAGE`. |
| Nov 2023 | **Added** | `DATASTORE_ID`, `CONTAINER_ID` | Added to enable direct identification of source datastore and container. |
| Dec 2024 | **Removed** | `CONTAINER_SCAN_ID` | Deprecated and removed. Use `CONTAINER_ID` to identify the container associated with a scan operation. |

---

## _failed_checks

| Date | Change | Column | Details |
|------|--------|--------|---------|
| Jul 2022 | **Created** | — | Initial table with `OPERATION_ID`, `ANOMALY_UUID`, `DETECTED_TIME`, `SOURCE_DATASTORE`, `SOURCE_CONTAINER`, `SOURCE_PARTITION`, `QUALITY_CHECK_ID`, `QUALITY_CHECK_RULE_TYPE`, `QUALITY_CHECK_PARAMETERS`, `QUALITY_CHECK_MESSAGE`, `QUALITY_CHECK_TAGS`, `SUGGESTED_REMEDIATION_FIELD`, `SUGGESTED_REMEDIATION_VALUE`, `SUGGESTED_REMEDIATION_SCORE`. |
| May 2023 | **Added** | `QUALITY_CHECK_DESCRIPTION` | Description text for the quality check. |
| Jul 2023 | **Removed** | `RECORD_ID_FIELD`, `RECORD_ID_VALUE` | These legacy fields were removed. |
| May 2024 | **Added** | `ANOMALOUS_RECORDS_COUNT` | Total anomalous record count, independent of source record sampling limits. |
| Mar 2025 | **Added** | `FINGERPRINT` | Hash fingerprint for anomaly deduplication (used with Reactivate Recurring Anomalies). |
| Mar 2025 | **Type change** | `QUALITY_CHECK_ID` | Changed from STRING to NUMBER. Existing tables are auto-migrated. |
| Jun 2025 | **Added** | `QUALITY_CHECK_FIELDS` | Names of the fields targeted by the quality check. |
| Jan 2026 | **Added** | `QUALITY_CHECK_METADATA` | Optional JSON string containing additional check metadata. |

---

## _check_metrics

| Date | Change | Column | Details |
|------|--------|--------|---------|
| Sep 2024 | **Created** | — | Initial table with `OPERATION_ID`, `QUALITY_CHECK_ID`, `ASSERTED_RECORDS_COUNT`, `ANOMALOUS_RECORDS_COUNT`. |
| Sep 2024 | **Added** | `CONTAINER_ID`, `SOURCE_DATASTORE`, `SOURCE_CONTAINER`, `SOURCE_PARTITION` | Added for easier joining with other tables. |
| Mar 2025 | **Type change** | `OPERATION_ID`, `QUALITY_CHECK_ID` | Changed from STRING to NUMBER. Existing tables are auto-migrated. |
| Mar 2025 | **Added** | `ASSERTION_RESULT`, `ASSERTION_DETAILS` | Assertion outcome and explanatory details for each check. |

---

## _source_records

| Date | Change | Column | Details |
|------|--------|--------|---------|
| Jul 2022 | **Created** | — | Initial table with `SOURCE_CONTAINER`, `SOURCE_PARTITION`, `ANOMALY_UUID`, `CONTEXT`, `RECORD`. No changes since creation. |
