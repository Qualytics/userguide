# Min Value

### Definition

*Asserts that a field has a minimum value.*

### Field Scope

**Single:** The rule evaluates a single specified field.

**Accepted Types**

| Type        |                          |
|-------------|--------------------------|
| `Integral`  | <div style="text-align:center">:octicons-check-16:</div> |
| `Fractional`| <div style="text-align:center">:octicons-check-16:</div> |

### General Properties

{%
    include-markdown "components/general-props/index.md"
    start='<!-- all-props--start -->'
    end='<!-- all-props--end -->'
%}

### Specific Properties

Determines the minimum allowable value for the field.

| Name               | Description                              |
|--------------------|------------------------------------------|
| <div class="text-primary">Value</div> | Specifies the minimum value a field should have. |

### Anomaly Types

{%
    include-markdown "components/anomaly-support/index.md"
    start='<!-- all-types--start -->'
    end='<!-- all-types--end -->'
%}

### Example

**Objective**: *Ensure that the quantity of items (L_QUANTITY) in the LINEITEM table is not below a value of 10.*

**Sample Data**

| L_ORDERKEY | L_LINENUMBER | L_QUANTITY |
|------------|--------------|------------|
| 1          | 1            | 40         |
| 1          | 2            | <span class="text-negative">5</span>  |
| 2          | 1            | 20         |
| 3          | 1            | <span class="text-negative">8</span>  |

=== "Payload example"
    ``` json
    {
        "description": "Ensure that the quantity of items (L_QUANTITY) in the LINEITEM table is not below a value of 10",
        "coverage": 1,
        "properties": {
            "value": 10
        },
        "tags": [],
        "fields": ["L_QUANTITY"],
        "additional_metadata": {"key 1": "value 1", "key 2": "value 2"},
        "rule": "minValue",
        "container_id": {container_id},
        "template_id": {template_id},
        "filter": "1=1"
    }
    ```

**Anomaly Explanation**

In the sample data above, the entries with `L_ORDERKEY` **1** and **3** do not satisfy the rule because their `L_QUANTITY` values are below the specified minimum value of 10.

=== "Flowchart"
    ```mermaid
    graph TD
    A[Start] --> B[Retrieve L_QUANTITY]
    B --> C{Is L_QUANTITY >= 10?}
    C -->|Yes| D[Move to Next Record/End]
    C -->|No| E[Mark as Anomalous]
    E --> D
    ```

=== "SQL"
    ```sql
    -- An illustrative SQL query demonstrating the rule applied to example dataset(s).
    select
        l_orderkey,
        l_linenumber,
        l_quantity
    from lineitem 
    where
        l_quantity < 10;
    ```

**Potential Violation Messages**

!!! example "Record Anomaly"
    The `L_QUANTITY` value of `5` is less than the min value of `10`.

!!! example "Shape Anomaly"
    In `L_QUANTITY`, 50.000% of 4 filtered records (2) are less than the min value of `10`.
