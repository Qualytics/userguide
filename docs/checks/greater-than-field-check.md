# Greater Than Field

### Definition

*Asserts that the field is greater than another field.*

### Field Scope

**Single:** The rule evaluates a single specified field.

**Accepted Types**

| Type        |                          |
|-------------|--------------------------|
| `Date`      | <div style="text-align:center">:octicons-check-16:</div>  |
| `Timestamp` | <div style="text-align:center">:octicons-check-16:</div>  |
| `Integral`  | <div style="text-align:center">:octicons-check-16:</div>  |
| `Fractional`| <div style="text-align:center">:octicons-check-16:</div>  |

### General Properties

{%
    include-markdown "components/general-props/index.md"
    start='<!-- all-props--start -->'
    end='<!-- all-props--end -->'
%}

### Specific Properties

Allows specifying another field against which the value comparison will be performed.

| Name               | Description |
|--------------------|-------------|
| <div class="text-primary">Field to compare</div> | Specifies the name of the field against which the value will be compared. |
| <div class="text-primary">Inclusive</div>        | If true, the comparison will also allow values equal to the value of the other field. Otherwise, it's exclusive. |
| <div class="text-primary">Comparators</div> | {{ comparator_short_desc }} |

!!! note "Details"
    {%
        include-markdown "components/comparators/index.md"
    %}
    {%
        include-markdown "components/comparators/numeric.md"
    %}
    {%
        include-markdown "components/comparators/duration.md"
    %}

### Anomaly Types

{%
    include-markdown "components/anomaly-support/index.md"
    start='<!-- all-types--start -->'
    end='<!-- all-types--end -->'
%}

### Example

**Objective**: *Ensure that all O_TOTALPRICE entries in the ORDERS table are greater than their respective O_DISCOUNT.*

**Sample Data**

| O_ORDERKEY | O_TOTALPRICE | O_DISCOUNT |
|------------|--------------|------------|
| 1          | 100          | <span class="text-negative">105</span> |
| 2          | 500          | 10         |
| 3          | 120          | <span class="text-negative">121</span> |

**Anomaly Explanation**

In the sample data above, the entries with `O_ORDERKEY` **1** and **3** do not satisfy the rule because their `O_TOTALPRICE` values are not greater than their respective `O_DISCOUNT` values.

=== "Flowchart"
    ```mermaid
    graph TD
    A[Start] --> B[Retrieve O_TOTALPRICE and O_DISCOUNT]
    B --> C{Is O_TOTALPRICE > O_DISCOUNT?}
    C -->|Yes| D[Move to Next Record/End]
    C -->|No| E[Mark as Anomalous]
    E --> D
    ```

=== "SQL"
    ```sql
    -- An illustrative SQL query demonstrating the rule applied to example dataset(s).
    select
        o_orderkey,
        o_totalprice,
        o_discount
    from orders 
    where
        o_totalprice <= o_discount;
    ```

**Potential Violation Messages**

!!! example "Record Anomaly"
    The `O_TOTALPRICE` value of `100` is not greater than the value of `O_DISCOUNT`.
        
!!! example "Shape Anomaly"
    In `O_TOTALPRICE`, 66.667% of 3 filtered records (2) are not greater than `O_DISCOUNT`.
