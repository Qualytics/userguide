# Between

### Definition

*Asserts that values are equal to or between two numbers.*

### Field Scope

**Single:** The rule evaluates a single specified field.

**Accepted Types**

| Type          |                          |
|---------------|--------------------------|
| `Integral`    | <div style="text-align:center">:octicons-check-16:</div>  |
| `Fractional`  | <div style="text-align:center">:octicons-check-16:</div>  |

### General Properties

{%
    include-markdown "components/general-props/index.md"
    start='<!-- all-props--start -->'
    end='<!-- all-props--end -->'
%}

### Specific Properties

Specify both minimum and maximum boundaries, and determine if these boundaries should be inclusive.

| Name                   | Explanation                                                                                                 |
|------------------------|-------------------------------------------------------------------------------------------------------------|
| <div class="text-primary">Max</div>                | The upper boundary of the range.                                                                             |
| <div class="text-primary">Inclusive (Max)</div>    | If true, the upper boundary is considered a valid value within the range. Otherwise, it's exclusive.     |
| <div class="text-primary">Min</div>                | The lower boundary of the range.                                                                             |
| <div class="text-primary">Inclusive (Min)</div>    | If true, the lower boundary is considered a valid value within the range. Otherwise, it's exclusive.     |

### Anomaly Types

{%
    include-markdown "components/anomaly-support/index.md"
    start='<!-- all-types--start -->'
    end='<!-- all-types--end -->'
%}

### Example

**Objective**: *Ensure that all L_QUANTITY entries in the LINEITEM table are between 5 and 20 (inclusive).*

**Sample Data**

| L_ORDERKEY | L_QUANTITY |
|------------|------------|
| 1          | <span class="text-negative">4<span>          |
| 2          | 15         |
| 3          | <span class="text-negative">21<span>         |

=== "Payload example"
    ``` json
    {
        "description": "Ensure that all L_QUANTITY entries in the LINEITEM table are between 5 and 20 (inclusive)",
        "coverage": 1,
        "properties": {
            "min":5
            "inclusive_min":true,
            "max":20,
            "inclusive_max":true,
        },
        "tags": [],
        "fields": ["L_QUANTITY"],
        "additional_metadata": {"key 1": "value 1", "key 2": "value 2"},
        "rule": "between",
        "container_id": {container_id},
        "template_id": {template_id},
        "filter": "1=1"
    }
    ```

**Anomaly Explanation**

In the sample data above, the entries with `L_ORDERKEY` **1** and **3** do not satisfy the rule because their `L_QUANTITY` values are not between **5** and **20** inclusive.

=== "Flowcharts"
    ``` mermaid
    graph TD
    A[Start] --> B[Retrieve L_QUANTITY]
    B --> C{Is 5 <= L_QUANTITY <= 20?}
    C -->|Yes| D[Move to Next Record/End]
    C -->|No| E[Mark as Anomalous]
    E --> D
    ```

=== "SQL"
    ```sql
    -- An illustrative SQL query demonstrating the rule applied to example dataset(s).
    select
        l_orderkey
        , l_quantity
    from lineitem 
    where
        l_quantity < 5
        or l_quantity > 20
    ```

**Potential Violation Messages**

!!! example "Record Anomaly"
    The value for `L_QUANTITY` of 4 is not between **5.000** and **20.000**.
        
!!! example "Shape Anomaly"
    In `L_QUANTITY`, 66.67% of 3 filtered records (2) are not between **5.000** and **20.000**.
