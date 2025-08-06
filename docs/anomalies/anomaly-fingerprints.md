# Anomaly Fingerprints

Anomaly fingerprints are unique identifiers generated for each detected anomaly to help the system recognize and manage duplicates effectively. By comparing these fingerprints, Qualytics can determine whether a newly detected anomaly matches a previously identified one. This mechanism reduces redundancy, ensures consistency in anomaly tracking, and simplifies decision-making during data quality operations.

## Duplicate Handling Configuration

Once anomalies are fingerprinted, Qualytics can use these unique identifiers to determine whether a newly detected anomaly matches any existing one. This fingerprint-based recognition powers the **duplicate handling configuration** during scan setup.

When configuring a scan operation, you can define how the system should respond to anomalies that share fingerprints with previously detected ones:

* **Duplicate Status:** You can instruct the system to automatically mark newly detected anomalies as **“Duplicate”** if their fingerprints match those of any open anomalies. These duplicates are then archived, ensuring focus remains on the original issue without creating redundant records.

* **Re-opening Option:** If a new anomaly matches an archived one, you can configure the system to **automatically re-open** the earlier anomaly. This ensures that reoccurring issues are not overlooked simply because they were resolved or dismissed in a prior scan.

## Fingerprinting Criteria

To determine whether anomalies are identical, Qualytics generates unique fingerprints based on specific criteria. These criteria differ depending on the type of anomaly being evaluated. This approach ensures that anomalies are only considered duplicates when they are truly the same in both nature and context.

### Record Anomalies

For **record-level anomalies**, fingerprinting is based on the specific check that identified the issue and the complete source data of the anomalous record. This ensures that every unique row is evaluated precisely:

* **Identifying check:** The check responsible for detecting the anomaly (e.g., a null value or out-of-range check).

* **Source record data:** All field values within the affected row.

!!! note 
    Identical records across multiple scans will generate the same fingerprint and therefore be flagged as duplicates.

### Shape Anomalies

For **shape anomalies**—which refer to patterns or distributions of data rather than individual records, the fingerprint is derived from a broader set of attributes:

* **Identifying check(s):** The rule(s) that triggered the anomaly at the dataset level.

* **Failure percentage:** The proportion of records that failed the check(s) within the scanned batch.

* **Maximum incremental identifier:** The highest value of a designated incremental field (e.g., timestamp, ID) in the scanned dataset.

!!! tip 
    Shape anomalies can only be fingerprinted if the data asset includes an incremental identifier. This field anchors the fingerprint to a specific range of data, ensuring accurate comparisons across different scans.

This fingerprinting mechanism ensures consistent anomaly tracking by minimizing false duplicates and keeping historical issues relevant when they reoccur.