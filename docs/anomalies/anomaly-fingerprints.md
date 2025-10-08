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

## Use Case: Handling Daily Truncate-and-Reload Tables

### Scenario

Many data pipelines use staging tables that follow a **truncate-and-reload** pattern daily. These tables present a unique challenge:

- No last update timestamp for incremental strategy  
- Table is completely truncated and reloaded each day  
- Same data anomalies appear repeatedly across scans  
- Standard incremental detection cannot identify "already seen" records  

### Problem
Without fingerprinting, each daily scan treats truncated-and-reloaded data as entirely new:

- **Day 1:** Scan identifies 127 anomalies → Team acknowledges all 127  
- **Day 2:** Table truncated, data reloaded → Same 127 anomalies flagged as "new"  
- **Day 3:** Process repeats → Team faces anomaly fatigue from duplicate alerts  

The lack of a persistent identifier means **Qualytics** cannot distinguish between truly new anomalies and recurring issues from reloaded data.

### Solution

Enable both duplicate handling options in your [**Scan Operation configuration**](../source-datastore/scan.md#configuration):

- **Archive Duplicate Anomalies:** When the same 127 anomalies appear again after the table reload, Qualytics recognizes their fingerprints and automatically marks them as duplicates rather than new anomalies.  
- **Reactivate Recurring Anomalies:** If an anomaly was previously archived or resolved but reappears in subsequent scans, Qualytics reactivates the original anomaly record, maintaining full historical context.  

### Benefits

- Eliminates daily re-acknowledgment of the same known issues  
- Maintains clean anomaly counts reflecting only truly new problems  
- Preserves audit trail through anomaly reactivation  
- Reduces alert fatigue while ensuring genuine recurrences are tracked  

### Configuration

Enable these settings in Scan Settings of your Scan Operation:  

✅ **Archive Duplicate Anomalies**  
✅ **Reactivate Recurring Anomalies**  

Set an appropriate **Anomaly Rollup Threshold** based on your data volume and tolerance for grouped anomalies.