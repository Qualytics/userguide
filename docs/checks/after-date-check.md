# After Date Time

### Definition

*Asserts that the field is a timestamp later than a specific date and time.*

### Field Scope

**Single:** The rule evaluates a single specified field.

**Accepted Types**

| Type    |                          |
|---------|--------------------------|
| `Date`      | <div style="text-align:center">:octicons-check-16:</div>  |
| `Timestamp` | <div style="text-align:center">:octicons-check-16:</div>  |

### General Properties

{%
    include-markdown "components/general-props/index.md"
    start='<!-- all-props--start -->'
    end='<!-- all-props--end -->'
%}

### Specific Properties

Specify a particular date and time to act as the threshold for the rule.

| Name           | Description                                                   |
|----------------|---------------------------------------------------------------|
| <div class="text-primary">Date</div>  | The timestamp used as the lower boundary. Values in the selected field should be after this timestamp. |

### Anomaly Types

{%
    include-markdown "components/anomaly-support/index.md"
    start='<!-- all-types--start -->'
    end='<!-- all-types--end -->'
%}

### Example

**Objective**: *Ensure that all O_ORDERDATE entries in the ORDERS table are later than 10:30 AM on December 31st, 1991.*

**Sample Data**

| O_ORDERKEY | O_ORDERDATE |
|------------|-------------|
| 1  | <span class="text-negative">1991-12-31 10:30:00</span> |
| 2  | 1992-01-02 09:15:00 |
| 3  | <span class="text-negative">1991-12-14 10:25:00</span> |

**Anomaly Explanation**

In the sample data above, the entries with `O_ORDERKEY` **1** and **3** do not satisfy the rule because their `O_ORDERDATE` values are not after **1991-12-31 10:30:00**.

=== "Flowchart"
    ``` mermaid
    graph TD
    A[Start] --> B[Retrieve O_ORDERDATE]
    B --> C{Is O_ORDERDATE > '1991-12-31 10:30:00'?}
    C -->|Yes| D[Move to Next Record/End]
    C -->|No| E[Mark as Anomalous]
    E --> D
    ```
=== "SQL"
    ```sql
    -- An illustrative SQL query demonstrating the rule applied to example dataset(s)
    select
        o_orderkey
        , o_orderdate
    from orders 
    where
        o_orderdate <= '1991-12-31 10:30:00'
    ```

**Potential Violation Messages**

=== "Record Anomaly"
    !!! example
        The `O_ORDERDATE` value of `1991-12-14 10:30:00` is not later than **1991-12-31 10:30:00**
=== "Shape Anomaly"
    !!! example
        In `O_ORDERDATE`, 66.667% of 3 filtered records (2) are not later than **1991-12-31 10:30:00**
