# Required Values

### Definition

*Asserts that all of the defined values must be present at least once within a field.*

{% 
    include-markdown "components/general-props/warning.md" 
    start='<!-- SPACING-WARNING --start -->'
    end='<!-- SPACING-WARNING --end -->'
%}

### Field Scope

**Single:** The rule evaluates a single specified field.

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
    start='<!-- all-props--start -->'
    end='<!-- all-props--end -->' 
%}

### Specific Properties

Ensures that a specific set of values is present within a field.

| Name     | Description                                               |
|----------|-----------------------------------------------------------|
| <div class="text-primary">Values</div> | Specifies the list of values that must exist in the field. |

### Anomaly Types

{%
    include-markdown "components/anomaly-support/index.md"
    start='<!-- shape-only--start -->'
    end='<!-- shape-only--end -->'
%}

### Example

**Objective**: *Ensure that orders have priorities labeled as '1-URGENT', '2-HIGH', '3-MEDIUM', '4-LOW', and '5-NOT URGENT'.*

**Sample Data**

| O_ORDERKEY | O_ORDERPRIORITY |
|------------|-----------------|
| 1          | 1-URGENT        |
| 2          | 2-HIGH          |
| 3          | 3-MEDIUM        |
| 4          | 3-MEDIUM        |

=== "Payload example"
    ``` json
    {
        "description": "Ensure that orders have priorities labeled as '1-URGENT', '2-HIGH', '3-MEDIUM', '4-LOW', and '5-NOT URGENT'",
        "coverage": 1,
        "properties": {
            "list":["1-URGENT","2-HIGH","3-MEDIUM","4-LOW","5-NOT URGENT"]
        },
        "tags": [],
        "fields": ["O_ORDERPRIORITY"],
        "additional_metadata": {"key 1": "value 1", "key 2": "value 2"},
        "rule": "requiredValues",
        "container_id": {container_id},
        "template_id": {template_id},
        "filter": "1=1"
    }
    ```

**Anomaly Explanation**

In the sample data above, the rule is violated because the values '4-LOW' and '5-NOT URGENT' are not present in the `O_ORDERPRIORITY` field of the ORDERS table.

=== "Flowchart"
    ```mermaid
    graph TD
    A[Start] --> B{Check if all specified values exist in the field}
    B -->|Yes| C[End: No Anomalies]
    B -->|No| D[Mark as Anomalous: Missing Values]
    D --> C
    ```

=== "SQL"
    ```sql
    -- An illustrative SQL query demonstrating the rule applied to example dataset(s).
    select distinct
        o_orderpriority
    from orders
    where o_orderpriority in ('1-URGENT', '2-HIGH', '3-MEDIUM', '4-LOW', '5-NOT URGENT');
    ```

**Potential Violation Messages**

!!! example "Shape Anomaly"
    In `O_ORDERPRIORITY`, required values are missing in 40.000% of filtered records.
