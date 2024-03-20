# Overview of containers

Containers are fundamental entities representing structured data sets. These containers could manifest as tables in JDBC datastores or as files within DFS datastores. They play a pivotal role in data organization, profiling, and quality checks within the Qualytics application.

## Types of containers

There are two main types of containers in Qualytics:

* **JDBC containers:** These containers represent tables, views, and other objects in a relational database.
* **DFS containers:** These containers represent files, such as CSV, JSON, and parquet files, typically stored in distributed file systems like Hadoop or cloud storage.


## Container Attributes Reference

The following table outlines the key attributes of a container and their significance:

| Attribute | Description |
|-----------|-------------|
| **Freshness** | Indicates the recency of the data within the container. Not applicable to computed tables. |
| **Service Level Agreement (SLA)** | Reflects compliance with defined performance metrics and thresholds. |
| **Timestamps** | Timestamp of the last profiled operation and the last scanned operation on the container. |
| **Tags** | Metadata labels assigned to the container for identification and categorization purposes. |
| **Incremental Strategy** | The strategy employed to track and apply row-level changes for incremental profiling and scanning. |
| **Quality Score & Completeness** | Metrics that represent the integrity and usability of the data within the container. |
| **Records & Fields** | The count of total records and the structure of fields, including columns or headers, within the container. |
| **Checks & Anomalies** | The total number of quality checks performed and anomalies detected within the container. |

## Actions on Containers

Users can perform various operations on containers:

1. **Settings:** Configure incremental strategy, partitioning fields, and exclude specific fields from analysis.
2. **Quality Checks:** Add authored quality checks tailored to the container.
3. **Operate:** Execute profiling and scanning operations.
4. **Freshness:** Schedule and manage data freshness checks, applicable only to certain container types.
5. **Export:** Export quality checks and field profiles to an enrichment datastore for further action or analysis.
6. **Deletion and Recreation:** Containers can be deleted with the option to be recreated if necessary.

## Field Profiles

After profiling a container, individual field profiles offer granular insights:

- **Type:** Classifies the data type of the field (e.g., String, Fractional, Integral).
- **Tags:** Attached tags.
- **Quality Score:** Quantitative measure of data quality for the field.
- **Completeness:** Indicates the presence of all expected data within the field.
- **Quality Checks:** Number of quality checks associated with the field.
- **Anomalies:** Count and details of any anomalies detected in the field.
