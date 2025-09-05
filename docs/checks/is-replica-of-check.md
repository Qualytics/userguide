# Is Replica Of (_Is sunsetting_)

!!! warning "Deprecation Warning"
    This check is being deprecated and will be replaced by the [Data Diff](data-diff-check.md) check, which provides the same functionality with improved performance and features. 
    
    This change is a rename from `isReplicaOf` to `dataDiff`. The `isReplicaOf` checks that exist in your system will continue to exist but as a `dataDiff`.
    Some things to keep in mind:
    
    1. Qualytics endpoint will no longer return the keyword `isReplicaOf`. You need to check if you have any pipeline or script that references that keyword specifically.
    For example:
    ```
    data = response.json()
    rule_type = data["rule_type"]
    print(rule_type)  # prints dataDiff instead of isReplicaOf
    ```
    
    2. The endpoint `GET /quality-checks/specifications/rules` will no longer return isReplicaOf, but dataDiff.
    3. The violation message for anomalies was tweaked slightly.
    Here's some example of violation message:

        3.1 Shape Anomaly
        ```
        For `PART` and `PART_REPLICA`, differences were found between the targeted fields and the referred fields
        ```
        3.2 Record Anomaly
        ```
        There are 7 records that differ between `PART` (15 records) and `PART_REPLICA` (15 records) in `TPCH-1`
        ```

    If you still need help [Contact our support team](mailto:support@qualytics.co)

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

### General Properties

{%
include-markdown "components/general-props/index.md"
start='<!-- filter-only--start -->'
end='<!-- filter-only--end -->'
%}


### Specific Properties

Specify the datastore and table/file where the replica of the targeted fields is located for comparison.

| Name       | Description                                                   |
|------------|---------------------------------------------------------------|
| <div class="text-primary">Row Identifiers</div>  | The list of fields defining the compound key to identify rows in the comparison analysis. |
| <div class="text-primary">Datastore</div>  | The source datastore where the replica of the targeted field(s) is located. |
| <div class="text-primary">Table/file</div> | The table, view or file in the source datastore that should serve as the replica. |
| <div class="text-primary">Comparators</div> | {{ comparator_short_desc }} |

!!! info
    The `IsReplicaOf` rule supports editing of `Row Identifiers` and `Passthrough Fields`, allowing for more tailored configuration.

!!! note "Details"
    <div style="margin-top: -12px;">
    ### Row Identifiers
    </div>

    This optional input allows row comparison analysis by defining a list of fields as row identifiers, it enables a more detailed comparison between tables/files, where each row compound key is used to identify its presence or absence in the reference table/file compared to the target table/file.  Qualytics can inform if the row exists or not and distinguish which field values differ in each row present in the reference table/file, helping to determine if it is a replica.

    !!! info
        Anomalies produced by a `IsReplicaOf` quality check making use of `Row Identifiers` have their source records presented in a different visualization. <br><br>
        See more at: *[Comparison Source Records](../anomalies/source-record.md/#comparison-source-records)*
    {%
        include-markdown "components/comparators/index.md"
    %}
    {%
        include-markdown "components/comparators/numeric.md"
    %}
    {%
        include-markdown "components/comparators/duration.md"
    %}
    {%
        include-markdown "components/comparators/string.md"
    %}




### Anomaly Types

{%
    include-markdown "components/anomaly-support/index.md"
    start='<!-- shape-only--start -->'
    end='<!-- shape-only--end -->'
%}

### Example

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

=== "Payload example"
    ``` json
    {
        "description": "Ensure that N_NATIONKEY and N_NATIONNAME from the NATION table are replicas in the NATION_BACKUP table",
        "coverage": 1,
        "properties": {
            "ref_container_id": {ref_container_id},
            "ref_datastore_id": {ref_datastore_id}
        },
        "tags": [],
        "fields": ["N_NATIONKEY", "N_NATIONNAME"],
        "additional_metadata": {"key 1": "value 1", "key 2": "value 2"},
        "rule": "isReplicaOf",
        "container_id": {container_id},
        "template_id": {template_id},
        "filter": "1=1"
    }
    ```

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

!!! example "Shape Anomaly"
    There is 1 record that differs between `NATION_BACKUP` (3 records) and `NATION` (3 records) in `<datastore_name>`

        data = response.json()
    rule_type = data["rule_type"]
    print(rule_type)  # prints dataDiff instead of isReplicaOf