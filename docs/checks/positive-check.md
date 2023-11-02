# Positive

### Definition

*Asserts that this is a positive number.*

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

**Objective**: *Ensure that the quantity of items (L_QUANTITY) in the LINEITEM table is a positive number.*

**Sample Data**

| L_ORDERKEY | L_LINENUMBER | L_QUANTITY |
|------------|--------------|------------|
| 1          | 1            | 40         |
| 2          | 1            | <span class="text-negative">0</span>          |
| 3          | 1            | <span class="text-negative">-5</span>         |
| 4          | 1            | 20         |

**Anomaly Explanation**

In the sample data above, the entries with `L_ORDERKEY` **2** and **3** do not satisfy the rule because their `L_QUANTITY` values are not positive numbers.

=== "Flowchart"
    ```mermaid
    graph TD
    A[Start] --> B[Retrieve L_QUANTITY]
    B --> C{Is L_QUANTITY Positive?}
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
        l_quantity <= 0;
    ```

**Potential Violation Messages**

!!! example "Record Anomaly"
    The value for `L_QUANTITY` of `-5` is not a positive number.

!!! example "Shape Anomaly"
    In `L_QUANTITY`, 50.000% of 4 filtered records (2) are not positive numbers.
