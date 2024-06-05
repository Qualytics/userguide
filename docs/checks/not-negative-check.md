# Not Negative

### Definition

*Asserts that this is a non-negative number.*

### Field Scope

**Single:** The rule evaluates a single specified field.

**Accepted Fields**

| Type        |                             |
|-------------|-----------------------------|
| `Integral`  | <div style="text-align:center">:octicons-check-16:</div>         |
| `Fractional`| <div style="text-align:center">:octicons-check-16:</div>         |

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

**Objective**: *Ensure that the quantity of items (L_QUANTITY) in the LINEITEM table is a non-negative number.*

**Sample Data**

| L_ORDERKEY | L_LINENUMBER | L_QUANTITY |
|------------|--------------|------------|
| 1          | 1            | 40         |
| 2          | 2            | <span class="text-negative">-5</span>         |
| 3          | 1            | 20         |

=== "Payload example"
    ``` json
    {
        "description": "Ensure that the quantity of items (L_QUANTITY) in the LINEITEM table is a non-negative number",
        "coverage": 1,
        "properties": null,
        "tags": [],
        "fields": ["L_QUANTITY"],
        "additional_metadata": {"key 1": "value 1", "key 2": "value 2"},
        "rule": "notNegative",
        "container_id": {container_id},
        "template_id": {template_id},
        "filter": "1=1"
    }
    ```

**Anomaly Explanation**

In the sample data above, the entry with `L_ORDERKEY` **2** does not satisfy the rule because its `L_QUANTITY` value is a negative number.

=== "Flowchart"
    ```mermaid
    graph TD
    A[Start] --> B[Retrieve L_QUANTITY]
    B --> C{Is L_QUANTITY >= 0?}
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
        l_quantity < 0;
    ```

**Potential Violation Messages**

!!! example "Record Anomaly"
    The value for `L_QUANTITY` of `-5` is a negative number.

!!! example "Shape Anomaly"
    In `L_QUANTITY`, 33.333% of 3 filtered records (1) are negative numbers.
