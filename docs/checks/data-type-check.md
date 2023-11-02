# Data Type

### Definition

*Asserts that the data is of a specific type.*

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

Specify the expected type for the data in the field.

| Name           | Description                                                   |
|----------------|---------------------------------------------------------------|
| <div class="text-primary">Field Type</div> | The type that values in the selected field should conform to. |

### Anomaly Types

{%
    include-markdown "components/anomaly-support/index.md"
    start='<!-- all-types--start -->'
    end='<!-- all-types--end -->'
%}

### Example

**Objective**: *Ensure that all L_QUANTITY entries in the LINEITEM table are of Integral type.*

**Sample Data**

| L_ORDERKEY | L_QUANTITY              |
|------------|-------------------------|
| 1          | 10                      |
| 2          | <span class="text-negative">15.5</span>  |
| 3          | <span class="text-negative">Ten</span> |

**Anomaly Explanation**

In the sample data above, the entries with `L_ORDERKEY` **2** and **3** do not satisfy the rule because their `L_QUANTITY` values are not of Integral type.

=== "Flowchart"
    ```mermaid
    graph TD
    A[Start] --> B[Retrieve L_QUANTITY]
    B --> C{Is L_QUANTITY of Integral type?}
    C -->|Yes| D[Move to Next Record/End]
    C -->|No| E[Mark as Anomalous]
    E --> D
    ```

=== "SQL"
    ```sql
    -- An illustrative SQL query demonstrating the rule applied to example dataset(s).
    select
        l_orderkey,
        l_quantity
    from lineitem 
    where
        typeof(l_quantity) != 'INTEGER'
    ```

**Potential Violation Messages**

!!! example "Record Anomaly"
    The `L_QUANTITY` value of `Ten` is not a valid Integral.

!!! example "Shape Anomaly"
    In `L_QUANTITY`, 66.667% of 3 filtered records (2) are not a valid Integral.
