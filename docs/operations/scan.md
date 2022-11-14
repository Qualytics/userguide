# Scan Operation

The Scan Operation is executed on a Datastore to assert the data quality checks defined for the named collections of data (e.g. tables, views, files, topics) within it. The operation will:

* produce a record anomaly for any record where anomalous values are detected
* produce a shape anomaly for anomalous values that span multiple records
* record the anomaly data along with related analysis in the associated Enrichment Datastore

---
# Operation Configuration

A Scan Operation can be configured with the following options:

* Incremental - to scan only new data updated since the previous scan
* Record limit - to limit the total number of records scanned
* Target selection - to target only a subset of the available named collections
* Remediation strategy - to specify how enrichment tables should be migrated to reflect changes in source tables
