# Greater Than

### Definition

*Asserts that the field is a number greater than (or equal to) a value.*

### Field Scope

**Single:** The rule evaluates a single specified field.

**Accepted Types**

| Type        |                          |
|-------------|--------------------------|
| `Integral`  | <div style="text-align:center">:octicons-check-16:</div>  |
| `Fractional`| <div style="text-align:center">:octicons-check-16:</div>  |

### General Properties

{%
    include-markdown "components/general-props/index.md"
    start='<!-- all-props--start -->'
    end='<!-- all-props--end -->'
%}

### Specific Properties

Allows specifying a numeric value that acts as the threshold.

| Name       | Description |
|------------|-------------|
| <div class="text-primary">Value</div>    | The number to use as the base comparison. |
| <div class="text-primary">Inclusive</div> | If true, the comparison will also allow values equal to the threshold. Otherwise, it's exclusive. |

### Anomaly Types

{%
    include-markdown "components/anomaly-support/index.md"
    start='<!-- all-types--start -->'
    end='<!-- all-types--end -->'
%}

### Example

**Objective**: *Ensure that all L_QUANTITY entries in the LINEITEM table are greater than 10.*

**Sample Data**

| L_ORDERKEY | L_QUANTITY |
|------------|------------|
| 1          | <span class="text-negative">9</span> |
| 2          | 15 |
| 3          | <span class="text-negative">5</span> |

**Anomaly Explanation**

In the sample data above, the entries with `L_ORDERKEY` **1** and **3** do not satisfy the rule because their `L_QUANTITY` values are not greater than **10**.

=== "Flowchart"
    ```mermaid
    graph TD
    A[Start] --> B[Retrieve L_QUANTITY]
    B --> C{Is L_QUANTITY > 10?}
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
        l_quantity <= 10;
    ```

**Potential Violation Messages**

=== "Record Anomaly"
    !!! example
        The `L_QUANTITY` value of `5` is not greater than the value of **10**.
        
=== "Shape Anomaly"
    !!! example
        In `L_QUANTITY`, 66.667% of 3 filtered records (2) are not greater than **10**.
