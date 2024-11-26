# Is Replica Of

**Is Replica Of** rule ensures that data copied from one place to another is exactly the same in both content and structure. This rule checks that everything from the original is accurately reflected in the copy, making sure no data is missing, altered, or incorrectly formatted.

### Why It Matters

Data is often replicated for important reasons, such as:

1. **Availability**: Keeping data accessible even if the main system goes down.  
2. **Backup**: Creating a backup copy to prevent data loss.  
3. **Analysis**: Sending data to systems that analyze or report on it.

However, things can go wrong during this process, such as:

* Network issues  
* Software bugs  
* Human errors

The Is Replica Of rule helps prevent or spot problems like these, making sure the copied data is still accurate and complete.

### How It Works

This rule ensures:

1. **Data Structure Matches**: The way the data is organized (like tables, rows, or columns) in the copy is the same as in the original.  
2. **Data Values Match**: Every value in the original data is present and correct in the copy.  

### Field Scope

* **Scope:**

This rule evaluates multiple fields to ensure all required data is correctly replicated.

* **Supported Types:**  

The rule supports the following field types:

| No. | Field Type |  Supported |
| :---- | :---- | :---- |
| 1. | Date | Yes |
| 2. | Timestamp | Yes |
| 3. | Integral | Yes |
| 4. | Fractional | Yes |
| 5. | String | Yes |
| 6. | Boolean | Yes |

### General Properties

{%
include-markdown "components/general-props/index.md"
start='<!-- filter-only--start -->'
end='<!-- filter-only--end -->'
%}

### Configuration Properties

To set up the IsReplicaOf rule, the following properties must be defined:

| No. | Property | Description |
| :---- | :---- | :---- |
| 1 | Row Identifiers | A compound key comprising fields that uniquely identify rows for detailed comparison. |
| 2 | Datastore | Specifies the datastore containing the replica for comparison. |
| 3 | Table/File | Refers to the table, view, or file in the datastore that serves as the replica. |
| 4 | Comparators | Methods for comparing field values (e.g., numeric or string-based comparisons). |

### Anomaly Types

{%
    include-markdown "components/anomaly-support/index.md"
    start='<!-- shape-only--start -->'
    end='<!-- shape-only--end -->'
%}

### Example

**Scenario:** Your company keeps a table of country information, such as country keys (IDs) and names, in a main database. For disaster recovery, this data is regularly copied to a backup system. The goal is to ensure that the backup data exactly matches the original data.

**Objective:** Verify that the N_NATIONKEY and N_NATIONNAME fields in the main table (NATION) match exactly with those in the backup table (NATION_BACKUP).

**Original Data from NATION Table:**

| Country ID (N_NATIONKEY) | Country Name (N_NATIONNAME) |
| ----- | ----- |
| 1 | Australia |
| 2 | United States |
| 3 | Uruguay |

**Replica Data from NATION_BACKUP Table:**

| Country ID (N_NATIONKEY) | Country Name (N_NATIONNAME) |
| ----- | :---- |
|  1 | Australia |
| 2 | USA |
| 3 | Uruguay |

In this example, the country name for ID 2 is different in the backup (USA instead of United States), which may indicate an issue with the replication process.

### What Happens:

1. **The Check:** The system compares both the original and backup data for any differences.

2. **The Result:** If the data doesn't match (like the name difference), it flags it as an anomaly, indicating something might have gone wrong during replication.

**How It Works:**

* **Data Comparison:** The system will check both the country IDs and names.  
* **Flagging Issues:** If the names or IDs don’t match between the original and the backup, an alert is raised.

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

### Anomaly Explanation

The datasets representing the fields N_NATIONKEY and N_NATIONNAME in the original and the replica are not completely identical, indicating a possible discrepancy in the replication process or an unintended change.

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
    There is 1 record that differ between `NATION_BACKUP` (3 records) and `NATION` (3 records) in `<datastore_name>`





































































