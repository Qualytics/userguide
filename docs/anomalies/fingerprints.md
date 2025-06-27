# Anomaly Fingerprints

Anomalies are uniquely fingerprinted to allow the system to recognize duplicates. This fingerprinting mechanism helps streamline anomaly management by preventing redundant work on identical problems.

## Duplicate Handling Configuration

When configuring a scan operation to identify anomalies in your data, you can specify how duplicates should be treated:

* **Duplicate Status**: You can select to set the status of newly identified anomalies that are identical to existing open anomalies to "duplicate" so that they will be automatically archived in favor of the existing anomaly.  
* **Re-opening Option**: You can also optionally re-open any identical anomalies that were previously identified but marked archived.

## Fingerprinting Criteria

### Record Anomalies

When record anomalies are fingerprinted, the system considers:

* The identifying check  
* All source data from the anomalous record

!!! note
    Identical rows will generate identical anomalies.

### Shape Anomalies

When shape anomalies are fingerprinted, the system considers:

* The identifying check(s)  
* The percentage of asserted records that failed the check(s)  
* The maximum value of the incremental identifier in the scanned dataset

!!! tip
    A data asset must have an incremental identifier to support fingerprinting of shape anomalies. This is because the maximum value of that identifier in the scanned dataset is used to generate the shape anomaly's fingerprint. This requirement helps ensure that only shape anomalies derived from the same underlying data are considered identical. Shape anomalies with the same details derived from different ranges of data are not considered identical.

For more details on Anomaly Fingerprints, please refer to the [Copy Anomaly Fingerprint](../anomalies/anomalies-overview.md#copy-anomaly-fingerprint) section in the documentation.