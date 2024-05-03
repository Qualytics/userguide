# Equal To

### Definition

*Asserts that all of the selected fields' equal a value.*

### Field Scope

**Multi:** The rule evaluates multiple specified fields.

**Accepted Types**

| Type        |                          |
|-------------|--------------------------|
| `Integral`  | <div style="text-align:center">:octicons-check-16:</div>      |
| `Fractional`| <div style="text-align:center">:octicons-check-16:</div>      |

### General Properties

{%
    include-markdown "components/general-props/index.md"
    start='<!-- all-props--start -->'
    end='<!-- all-props--end -->'
%}

### Specific Properties

Specify the field to compare for equality with the selected field.

| Name                 | Description                                                                   |
|----------------------|-------------------------------------------------------------------------------|
| <div class="text-primary">Value</div> | Specifies the value a field should be equal to. |

### Anomaly Types

{%
    include-markdown "components/anomaly-support/index.md"
    start='<!-- all-types--start -->'
    end='<!-- all-types--end -->'
%}


### Example

**Objective**: *Ensure that the quantity of items (L_QUANTITY) in the LINEITEM table is equal to a value of 10.*

**Sample Data**

| L_ORDERKEY | L_LINENUMBER | L_QUANTITY |
|------------|--------------|------------|
| 1          | 1            | 10         |
| 2          | 2            | <span class="text-negative">5</span>  |
| 3          | 3            | 10         |
| 4          | 4            | <span class="text-negative">8</span>  |

**Anomaly Explanation**

In the sample data above, the entries with `L_ORDERKEY` **2** and **4** do not satisfy the rule because their `L_QUANTITY` values are below the specified minimum value of 10.

=== "Flowchart"
    ```mermaid
    graph TD
    A[Start] --> B[Retrieve L_QUANTITY]
    B --> C{Is L_QUANTITY = 10?}
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
    Not all of the fields equal are equal to the value of `10`

!!! example "Shape Anomaly"
    In `L_QUANTITY`, 2 of 4 filtered records (4) are not equal to the value of `10`
