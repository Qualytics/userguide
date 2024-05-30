# Expected Values

### Definition

*Asserts that values are contained within a list of expected values.*

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

Specify the list of expected values for the data in the field.

| Name       | Description                                                   |
|------------|---------------------------------------------------------------|
| <div class="text-primary">List</div> | A predefined set of values against which the data is validated. |

### Anomaly Types

{% 
    include-markdown "components/anomaly-support/index.md"
    start='<!-- all-types--start -->'
    end='<!-- all-types--end -->' 
%}

### Example

**Objective**: *Ensure that all O_ORDERSTATUS entries in the ORDERS table only contain expected order statuses: "O", "F", and "P".*

**Sample Data**

| O_ORDERKEY | O_ORDERSTATUS   |
|------------|----------------|
| 1          | F              |
| 2          | O              |
| 3          | P              |
| 4          | <span class="text-negative">X</span> |

=== "Payload example"
    ``` json
    {
        "description": "Ensure that all O_ORDERSTATUS entries in the ORDERS table only contain expected order statuses: "O", "F", and "P"",
        "coverage": 1,
        "properties": {
            "list":["O","F","P"]
        },
        "tags": [],
        "fields": ["O_ORDERSTATUS"],
        "additional_metadata": {"key 1": "value 1", "key 2": "value 2"},
        "rule": "expectedValues",
        "container_id": {container_id},
        "template_id": {template_id},
        "filter": "1=1"
    }
    ```

**Anomaly Explanation**

In the sample data above, the entry with `O_ORDERKEY` **4** does not satisfy the rule because the `O_ORDERSTATUS` "X" is not on the list of expected order statuses ("O", "F", "P").

=== "Flowchart"
    ``` mermaid
    graph TD
    A[Start] --> B[Retrieve O_ORDERSTATUS]
    B --> C{Is O_ORDERSTATUS in 'O', 'F', 'P'?}
    C -->|Yes| D[Move to Next Record/End]
    C -->|No| E[Mark as Anomalous]
    E --> D
    ```

=== "SQL"
    ```sql
    -- An illustrative SQL query demonstrating the rule applied to example dataset(s).
    select
        o_orderkey
        , o_orderstatus
    from orders 
    where
        o_orderstatus not in ('O', 'F', 'P')
    ```

**Potential Violation Messages**

!!! example "Record Anomaly"
    The `O_ORDERSTATUS` value of `'X'` does not appear in the list of expected values

!!! example "Shape Anomaly"
    In `O_ORDERSTATUS`, 25.000% of 4 filtered records (1) do not appear in the list of expected values
