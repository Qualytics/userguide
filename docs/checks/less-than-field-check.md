# Less Than Field

### Definition

*Asserts that the field is less than another field.*

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

**Objective**: *Ensure that all O_DISCOUNT entries in the ORDERS table are less than their respective O_TOTALPRICE.*

**Sample Data**

| O_ORDERKEY | O_TOTALPRICE | O_DISCOUNT |
|------------|--------------|------------|
| 1          | 105          | 100        |
| 2          | 500          | 10         |
| 3          | 121          | <span class="text-negative">125</span> |

**Anomaly Explanation**

In the sample data above, the entry with `O_ORDERKEY` **3** does not satisfy the rule because its `O_DISCOUNT` value is not less than its respective `O_TOTALPRICE` value.

=== "Flowchart"
    ```mermaid
    graph TD
    A[Start] --> B[Retrieve O_TOTALPRICE and O_DISCOUNT]
    B --> C{Is O_DISCOUNT < O_TOTALPRICE?}
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
        o_discount >= o_totalprice;
    ```

**Potential Violation Messages**

!!! example "Record Anomaly"
    The `O_DISCOUNT` value of `125` is not less than the value of `O_TOTALPRICE`.
        
!!! example "Shape Anomaly"
    In `O_DISCOUNT`, 33.333% of 3 filtered records (1) is not less than `O_TOTALPRICE`.
