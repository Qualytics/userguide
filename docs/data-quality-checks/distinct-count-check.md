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
| <div class="text-primary">Comparison</div> | Specifies how the distinct count should be compared against the value. |
| <div class="text-primary">Value</div>  | The value to compare the distinct count against. |

!!! note "Details"
    **Comparison** is a required property that accepts the following values:

    | Comparison | Description |
    |------------|-------------|
    | `eq` | Equal To - Assert distinct count equals the value |
    | `gt` | Greater Than - Assert distinct count is greater than the value |
    | `gte` | Greater Than Or Equal To - Assert distinct count is ≥ value |
    | `lt` | Less Than - Assert distinct count is less than the value |
    | `lte` | Less Than Or Equal To - Assert distinct count is ≤ value |

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
            "comparison": "eq",
            "value": 3
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

In the sample data above, the rule is violated because the `O_ORDERSTATUS` contains 4 distinct values, which is not equal to 3. The expected values were 'O' (Open), 'F' (Finished), and 'P' (In Progress), but an unexpected value 'X' was found.

=== "Flowchart"
    ``` mermaid
    graph TD
    A[Start] --> B[Retrieve all O_ORDERSTATUS entries and count distinct values]
    B --> C{Does distinct count satisfy comparison condition?}
    C -->|No| D[Mark as Anomalous]
    C -->|Yes| E[End]
    ```

=== "SQL"
    ```sql
    -- An illustrative SQL query demonstrating the rule applied to example dataset(s).
    -- Using comparison = 'eq' (equal to)
    select
        count(distinct o_orderstatus)
    from orders
    having count(distinct o_orderstatus) <> 3
    ```

**Potential Violation Messages**

!!! example "Shape Anomaly (eq)"
    The distinct count of values in `O_ORDERSTATUS` is **4** which is not equal to **3**.

!!! example "Shape Anomaly (gte)"
    The distinct count of values in `O_ORDERSTATUS` is **2** which is not greater than or equal to **3**.

!!! example "Shape Anomaly (lte)"
    The distinct count of values in `O_ORDERSTATUS` is **5** which is not less than or equal to **3**.
