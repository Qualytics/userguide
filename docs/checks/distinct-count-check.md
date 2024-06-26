# Distinct Count

### Definition

*Asserts on the approximate count distinct of the given column.*

### Field Scope

**Single:** The rule evaluates a single specified field.

**Accepted Types**

| Type        |                          |
|-------------|--------------------------|
| `Date`      | <div style="text-align:center">:octicons-check-16:</div>  |
| `Timestamp` | <div style="text-align:center">:octicons-check-16:</div>  |
| `Integral`  | <div style="text-align:center">:octicons-check-16:</div>  |
| `Fractional`| <div style="text-align:center">:octicons-check-16:</div>  |
| `String`    | <div style="text-align:center">:octicons-check-16:</div>  |
| `Boolean`   | <div style="text-align:center">:octicons-check-16:</div>  |

### General Properties

{%
    include-markdown "components/general-props/index.md"
    start='<!-- all-props--start -->'
    end='<!-- all-props--end -->'
%}

### Specific Properties

Specify the distinct count expectation for the values in the field.

| Name           | Description                                                   |
|----------------|---------------------------------------------------------------|
| <div class="text-primary">Value</div>  | The exact count of distinct values expected in the selected field. |

### Anomaly Types

{%
    include-markdown "components/anomaly-support/index.md"
    start='<!-- shape-only--start -->'
    end='<!-- shape-only--end -->'
%}

### Example

**Objective**: *Ensure that there are exactly 3 distinct O_ORDERSTATUS in the ORDERS table: 'O' (Open), 'F' (Finished), and 'P' (In Progress).*

**Sample Data**

| O_ORDERKEY | O_ORDERSTATUS          |
|------------|------------------------|
| 1          | O                      |
| 2          | F                      |
| ...        | ...                    |
| 20         | X                      |
| 21         | O                      |

=== "Payload example"
    ``` json
    {
        "description": "Ensure that there are exactly 3 distinct O_ORDERSTATUS in the ORDERS table: 'O' (Open), 'F' (Finished), and 'P' (In Progress)",
        "coverage": 1,
        "properties": {
            "value":3
        },
        "tags": [],
        "fields": ["O_ORDERSTATUS"],
        "additional_metadata": {"key 1": "value 1", "key 2": "value 2"},
        "rule": "distinctCount",
        "container_id": {container_id},
        "template_id": {template_id},
        "filter": "1=1"
    }
    ```

**Anomaly Explanation**

In the sample data above, the rule is violated because the `O_ORDERSTATUS` contains 4 distinct values and not 3: 'O' (Open), 'F' (Finished), and 'P' (In Progress).

=== "Flowchart"
    ``` mermaid
    graph TD
    A[Start] --> B[Retrieve all O_ORDERSTATUS entries and count distinct values]
    B --> C{Is distinct count of O_ORDERSTATUS != 3?}
    C -->|Yes| D[Mark as Anomalous]
    C -->|No| E[End]
    ```

=== "SQL"
    ```sql
    -- An illustrative SQL query demonstrating the rule applied to example dataset(s).
    select
        count(distinct o_orderstatus)
    from orders
    having count(distinct o_orderstatus) <> 3
    ```

**Potential Violation Messages**

!!! example "Shape Anomaly"
    In `O_ORDERSTATUS`, the distinct count of the records is not **3**.
