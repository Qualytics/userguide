# Less Than

### Definition

*Asserts that the field is a number less than (or equal to) a value.*

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
| <div class="text-primary">Comparators</div> | {{ comparator_short_desc }} |

!!! note "Details"
    {%
        include-markdown "components/comparators/index.md"
    %}
    {%
        include-markdown "components/comparators/numeric.md"
    %}

### Anomaly Types

{%
    include-markdown "components/anomaly-support/index.md"
    start='<!-- all-types--start -->'
    end='<!-- all-types--end -->'
%}

### Example

**Objective**: *Ensure that all L_PRICE entries in the LINEITEM table are less than 20.*

**Sample Data**

| L_ORDERKEY | L_PRICE   |
|------------|------------|
| 1          | 18         |
| 2          | <span class="text-negative">25</span> |
| 3          | <span class="text-negative">23</span> |

**Anomaly Explanation**

In the sample data above, the entries with `L_ORDERKEY` **2** and **3** do not satisfy the rule because their `L_PRICE` values are not less than **20**.

=== "Flowchart"
    ```mermaid
    graph TD
    A[Start] --> B[Retrieve L_PRICE]
    B --> C{Is L_PRICE < 20?}
    C -->|Yes| D[Move to Next Record/End]
    C -->|No| E[Mark as Anomalous]
    E --> D
    ```

=== "SQL"
    ```sql
    -- An illustrative SQL query demonstrating the rule applied to example dataset(s).
    select
        l_orderkey,
        l_price
    from lineitem 
    where
        l_price >= 20;
    ```

**Potential Violation Messages**

!!! example "Record Anomaly"
    The `L_PRICE` value of `23` is not less than the value of **20**.
    
!!! example "Shape Anomaly"
    In `L_PRICE`, 66.667% of 3 filtered records (2) are not less than **20**.
