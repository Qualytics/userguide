# Remediation Tables

When anomalies are detected in a container, the platform has the capability to create remediation tables in the Enrichment Datastore. These tables are detailed snapshots of the affected container, capturing the state of the data at the time of anomaly detection. They also include additional columns for metadata and remediation purposes. However, the creation of these tables depends upon the chosen remediation strategy during the scan operation.

Currently, there are three types of remediation strategies:

- **None**: No remediation tables will be created, regardless of anomaly detection.
- **Append**: Replicate source containers using an append-first strategy.
- **Overwrite**: Replicate source containers using an overwrite strategy.

!!! Note
	The naming convention for the remediation tables follows the pattern of `<enrichment_prefix>_remediation_<container_id>`, where `<enrichment_prefix>` is user-defined during the Enrichment Datastore configuration and `<container_name>` corresponds to the original source container.

## Illustrative Table

`_{ENRICHMENT_CONTAINER_PREFIX}_REMEDIATION_{CONTAINER_ID}`

This remediation table is an illustrative snapshot of the "Orders" container for reference purposes.

| Name                       | Data Type          | Description                                                         |
|----------------------------|--------------------|---------------------------------------------------------------------|
|_QUALYTICS_SOURCE_PARTITION | STRING            | The partition from the source data container.                      |
| ANOMALY_UUID                | STRING            | Unique identifier of the anomaly.                                  |
| ORDERKEY                   | NUMBER       | Unique identifier of the order.                                    |
| CUSTKEY                    | NUMBER       | The customer key related to the order.                             |
| ORDERSTATUS                | CHAR         | The status of the order (e.g., 'F' for 'finished').                |
| TOTALPRICE                 | FLOAT        | The total price of the order.                                      |
| ORDERDATE                  | DATE         | The date when the order was placed.                                |
| ORDERPRIORITY              | STRING       | Priority of the order (e.g., 'urgent').                            |
| CLERK                      | STRING       | The clerk who took the order.                                      |
| SHIPPRIORITY               | INTEGER      | The priority given to the order for shipping.                      |
| COMMENT                    | STRING       | Comments related to the order.                                     |

!!! Note
	In addition to capturing the original container fields, the platform includes two metadata columns designed to assist in the analysis and remediation process.

    - _QUALYTICS_SOURCE_PARTITION
    - ANOMALY_UUID

## Understanding Remediation Tables vs. Source Record Tables

When managing data anomalies in containers, it's important to understand the structures of Remediation Tables and Source Record Tables in the Enrichment Datastore.

### Remediation Tables

**Purpose:** Remediation tables are designed to capture detailed snapshots of the affected containers at the time of anomaly detection. They serve as a primary tool for remediation actions.

**Creation:** These tables are generated based on the remediation strategy selected during the scan operation:

- **None**: No tables are created.
- **Append**: Tables are created with new data appended.
- **Overwrite**: Tables are created and existing data is overwritten.

**Structure:** The structure includes all columns from the source container, along with additional columns for metadata and remediation purposes. The naming convention for these tables is `<enrichment_prefix>_remediation_<container_id>`, where `<enrichment_prefix>` is defined during the Enrichment Datastore configuration.

### Source Record Tables

**Purpose:** The Source Record Table is mainly used within the Qualytics App to display anomalies directly to users by showing the source records.

**Structure:** Unlike remediation tables, the Source Record Table stores each record in a JSON format within a single column named `RECORD`, along with other metadata columns like `SOURCE_CONTAINER`, `SOURCE_PARTITION`, `ANOMALY_UUID`, and `CONTEXT`.

### Key Differences

- **Format**: Remediation tables are structured with separate columns for each data field, making them easier to use for consulting and remediation processes. 

	Source Record Tables store data in a JSON format within a single column, which can be less convenient for direct data operations.

- **Usage**: Remediation tables are optimal for performing corrective actions and are designed to integrate easily with data workflows. 

	Source Record Tables are best suited for reviewing specific anomalies within the Qualytics App due to their format and presentation.

### Recommendation

For users intending to perform querying or need detailed snapshots for audit purposes, **Remediation Tables** are recommended. 

For those who need to quickly review anomalies directly within the Qualytics App, **Source Record Tables** are more suitable due to their straightforward presentation of data.
