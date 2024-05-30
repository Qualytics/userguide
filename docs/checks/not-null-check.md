# Not Null

### Definition

*Asserts that none of the selected fields' values are explicitly set to nothing.*

### Field Scope

**Multi:** The rule evaluates multiple specified fields.

**Accepted Fields**

| Type        |                             |
|-------------|-----------------------------|
| `Date`      | <div style="text-align:center">:octicons-check-16:</div>         |
| `Timestamp` | <div style="text-align:center">:octicons-check-16:</div>         |
| `Integral`  | <div style="text-align:center">:octicons-check-16:</div>         |
| `Fractional`| <div style="text-align:center">:octicons-check-16:</div>         |
| `String`    | <div style="text-align:center">:octicons-check-16:</div>         |
| `Boolean`   | <div style="text-align:center">:octicons-check-16:</div>         |

### General Properties

{%
    include-markdown "components/general-props/index.md"
    start='<!-- all-props--start -->'
    end='<!-- all-props--end -->'
%}

### Anomaly Types

{%
    include-markdown "components/anomaly-support/index.md"
    start='<!-- all-types--start -->'
    end='<!-- all-types--end -->'
%}

### Example

**Objective**: *Ensure that every record in the CUSTOMER table has an assigned value for the C_NAME and C_ADDRESS fields.*

**Sample Data**

| C_CUSTKEY | C_NAME   | C_ADDRESS       |
|-----------|----------|-----------------|
| 1         | Alice    | 123 Oak St      |
| 2         | Bob      | <span class="text-negative">NULL</span>            |
| 3         | Charlie  | 789 Maple Ave   |
| 4         | <span class="text-negative">NULL</span>     | 456 Pine Rd     |

=== "Payload example"
    ``` json
    {
        "description": "Ensure that every record in the CUSTOMER table has an assigned value for the C_NAME and C_ADDRESS fields",
        "coverage": 1,
        "properties": null,
        "tags": [],
        "fields": ["C_ADDRESS","C_NAME"],
        "additional_metadata": {"key 1": "value 1", "key 2": "value 2"},
        "rule": "notNull",
        "container_id": {container_id},
        "template_id": {template_id},
        "filter": "1=1"
    }
    ```

**Anomaly Explanation**

In the sample data above, the entries with `C_CUSTKEY` **2** and **4** do not satisfy the rule because they have `NULL` values in the `C_NAME` or `C_ADDRESS` fields.

=== "Flowchart"
    ```mermaid
    graph TD
    A[Start] --> B[Retrieve C_NAME and C_ADDRESS]
    B --> C{Are C_NAME and C_ADDRESS non-null?}
    C -->|Yes| D[Move to Next Record/End]
    C -->|No| E[Mark as Anomalous]
    E --> D
    ```

=== "SQL"
    ```sql
    -- An illustrative SQL query demonstrating the rule applied to example dataset(s).
    select
        c_custkey,
        c_name,
        c_address
    from customer 
    where
        c_name is null or c_address is null;
    ```

**Potential Violation Messages**

!!! example "Record Anomaly"
    There is no assigned value for `C_NAME`.

!!! example "Shape Anomaly"
    In `C_NAME` and `C_ADDRESS`, 50.000% of 4 filtered records (2) are not assigned values.
