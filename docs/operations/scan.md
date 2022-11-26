# Scan Operation

The Scan Operation is executed on a Datastore to assert the data quality checks defined for the named collections of data (e.g. tables, views, files, topics) within it. The operation will:

* produce a record anomaly for any record where anomalous values are detected
* produce a shape anomaly for anomalous values that span multiple records
* record the anomaly data along with related analysis in the associated Enrichment Datastore

---
# Operation Configuration

![Screenshot](../assets/operations/operation-scan.png)

A Scan Operation can be configured with the following options:

* `Full` - To process all records ignoring the previous scan.
* `Incremental` - To scan only new data updated since the previous scan.
* `Record limit` - To limit the total number of records scanned.
* `Remediation strategy` - To specify how enrichment tables should be migrated to reflect changes in source tables.
* `Target selection` 
    - You can select to all tables.
    - To target only a subset of the available named collections.

    ![Screenshot](../assets/operations/operation-scan-specific-tables.png)

