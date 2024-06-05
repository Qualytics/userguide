# Unique

### Definition

*Asserts that the field's value is unique.*

### Field Scope

**Multi:** The rule evaluates multiple specified fields.

**Accepted Types**

| Type        |                           |
|-------------|---------------------------|
| `Date`      | <div style="text-align:center">:octicons-check-16:</div>       |
| `Timestamp` | <div style="text-align:center">:octicons-check-16:</div>       |
| `Integral`  | <div style="text-align:center">:octicons-check-16:</div>       |
| `Fractional`| <div style="text-align:center">:octicons-check-16:</div>       |
| `String`    | <div style="text-align:center">:octicons-check-16:</div>       |
| `Boolean`   | <div style="text-align:center">:octicons-check-16:</div>       |

### General Properties

{%
    include-markdown "components/general-props/index.md"
    start='<!-- all-props--start -->'
    end='<!-- all-props--end -->'
%}

### Anomaly Types

{%
    include-markdown "components/anomaly-support/index.md"
    start='<!-- shape-only--start -->'
    end='<!-- shape-only--end -->'
%}

### Example

**Objective**: *Ensure that each combination of C_NAME and C_ADDRESS in the CUSTOMER table is unique.*

**Sample Data**

| C_CUSTKEY | C_NAME      | C_ADDRESS            |
|-----------|-------------|----------------------|
| 1         | <span class="text-negative">Customer_A</span>  | <span class="text-negative">123 Main St</span> |
| 2         | Customer_B  | 456 Oak Ave          |
| 3         | <span class="text-negative">Customer_A</span>  | <span class="text-negative">123 Main St</span> |
| 4         | Customer_C  | 789 Elm St           |

=== "Payload example"
    ``` json
    {
        "description": "Ensure that each combination of C_NAME and C_ADDRESS in the CUSTOMER table is unique",
        "coverage": 1,
        "properties": null,
        "tags": [],
        "fields": ["C_NAME", "DEATH_RATE"],
        "additional_metadata": {"key 1": "value 1", "key 2": "value 2"},
        "rule": "unique",
        "container_id": {container_id},
        "template_id": {template_id},
        "filter": "1=1"
    }
    ```

**Anomaly Explanation**

In the sample data above, the entries with `C_CUSTKEY` **1** and **3** have the same `C_NAME` and `C_ADDRESS`, which violates the rule because this combination of keys should be unique.

=== "Flowchart"
    ```mermaid
    graph TD
    A[Start] --> B[Retrieve C_NAME and C_ADDRESS]
    B --> C{Is the combination unique?}
    C -->|Yes| D[Move to Next Record/End]
    C -->|No| E[Mark as Anomalous]
    E --> D
    ```

=== "SQL"
    ```sql
    -- An illustrative SQL query to find non-unique C_NAME and C_ADDRESS combinations.
    select
        c_custkey,
        c_name,
        c_address
    from customer 
    group by c_name, c_address
    having count(*) > 1;
    ```

**Potential Violation Messages**

!!! example "Shape Anomaly"
    In `C_NAME` and `C_ADDRESS`, 25.000% of 4 filtered records (1) are not unique.
