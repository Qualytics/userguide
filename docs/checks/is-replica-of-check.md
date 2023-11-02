# Is Replica Of

### Definition

*Asserts that the dataset created by the targeted field(s) is replicated by the referred field(s).*

#### In-Depth Overview

The `IsReplicaOf` rule ensures that data integrity is maintained when data is replicated from one source to another. This involves checking not only the data values themselves but also ensuring that the structure and relationships are preserved.

In a distributed data ecosystem, replication often occurs to maintain high availability, create backups, or feed data into analytical systems. However, discrepancies might arise due to various reasons such as network glitches, software bugs, or human errors. The `IsReplicaOf` rule serves as a safeguard against these issues by:

1. **Preserving Data Structure**: Ensuring that the structure of the replicated data matches the original.
2. **Checking Data Values**: Ensuring that every piece of data in the source exists in the replica.

### Field Scope

**Multi:** The rule evaluates multiple specified fields.

**Accepted Types**

| Type        |                          |
|-------------|--------------------------|
| `Date`      | <div style="text-align:center">:octicons-check-16:</div>      |
| `Timestamp` | <div style="text-align:center">:octicons-check-16:</div>      |
| `Integral`  | <div style="text-align:center">:octicons-check-16:</div>      |
| `Fractional`| <div style="text-align:center">:octicons-check-16:</div>      |
| `String`    | <div style="text-align:center">:octicons-check-16:</div>      |
| `Boolean`   | <div style="text-align:center">:octicons-check-16:</div>      |

### Specific Properties

Specify the datastore and table/file where the replica of the targeted fields is located for comparison.

| Name       | Description                                                   |
|------------|---------------------------------------------------------------|
| <div class="text-primary">Datastore</div>  | The source datastore where the replica of the targeted field(s) is located. |
| <div class="text-primary">Table/file</div> | The table, view or file in the source datastore that should serve as the replica. |

### Anomaly Types

{%
    include-markdown "components/anomaly-support/index.md"
    start='<!-- shape-only--start -->'
    end='<!-- shape-only--end -->'
%}

### TPC-H Example

**Scenario**: *Consider that the fields N_NATIONKEY and N_NATIONNAME in the NATION table are being replicated to a backup database for disaster recovery purposes. The data engineering team wants to ensure that both fields in the replica in the backup accurately reflect the original.*

**Objective**: *Ensure that N_NATIONKEY and N_NATIONNAME from the NATION table are replicas in the NATION_BACKUP table.*

**Sample Data from NATION**

| N_NATIONKEY | N_NATIONNAME       |
|-------------|--------------------|
| 1           | Australia          |
| 2           | United States      |
| 3           | Uruguay            |

**Replica Sample Data from NATION_BACKUP**

| N_NATIONKEY | N_NATIONNAME       |
|-------------|--------------------|
| 1           | Australia          |
| 2           | USA                |
| 3           | Uruguay            |

**Anomaly Explanation**

The datasets representing the fields `N_NATIONKEY` and `N_NATIONNAME` in the original and the replica are not completely identical, indicating a possible discrepancy in the replication process or an unintended change.

=== "Flowchart"
    ```mermaid
    graph TD
    A[Start] --> B[Retrieve Original Data]
    B --> C[Retrieve Replica Data]
    C --> D{Do datasets match for both fields?}
    D -->|Yes| E[End]
    D -->|No| F[Mark as Anomalous]
    F --> E
    ```

=== "SQL"
    ```sql
    -- An illustrative SQL query comparing original to replica for both fields.
    select
        orig.n_nationkey as original_key,
        orig.n_nationname as original_name,
        replica.n_nationkey as replica_key,
        replica.n_nationname as replica_name
    from nation as orig
    left join nation_backup as replica on orig.n_nationkey = replica.n_nationkey
    where
        orig.n_nationname <> replica.n_nationname
    or
        orig.n_nationkey <> replica.n_nationkey
    ```

**Potential Violation Messages**

=== "Shape Anomaly"
    !!! example
        There is 1 record that differ between `NATION_BACKUP` (3 records) and `NATION` (3 records) in `<datastore_name>`
