# Between Times

### Definition

*Asserts that values are equal to or between two dates or times.*

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

Specify the range of dates or times that values in the selected field should fall between.

| Name           | Description                                                   |
|----------------|---------------------------------------------------------------|
| <div class="text-primary">Min</div>  | The timestamp used as the lower boundary. Values in the selected field should be after this timestamp. |
| <div class="text-primary">Max</div>  | The timestamp used as the upper boundary. Values in the selected field should be before this timestamp. |

### Anomaly Types

{%
    include-markdown "components/anomaly-support/index.md"
    start='<!-- all-types--start -->'
    end='<!-- all-types--end -->'
%}

### Example

**Objective**: *Ensure that all O_ORDERDATE entries in the ORDERS table are between 10:30 AM on January 1st, 1991 and 3:00 PM on December 31st, 1991.*

**Sample Data**

| O_ORDERKEY | O_ORDERDATE |
|------------|-------------|
| 1  | <span class="text-negative">1990-12-31 10:30:00</span> |
| 2  | 1991-06-02 09:15:00 |
| 3  | <span class="text-negative">1992-01-01 01:25:00</span> |

**Anomaly Explanation**

In the sample data above, the entries with `O_ORDERKEY` **1** and **3** do not satisfy the rule because their `O_ORDERDATE` values are not between **1991-01-01 10:30:00** and **1991-12-31 15:00:00**.

=== "Flowchart"
    ``` mermaid
    graph TD
    A[Start] --> B[Retrieve O_ORDERDATE]
    B --> C{Is '1991-01-01 10:30:00' <= O_ORDERDATE <= '1991-12-31 15:00:00'?}
    C -->|Yes| D[Move to Next Record/End]
    C -->|No| E[Mark as Anomalous]
    E --> D
    ```

=== "SQL"
    ```sql
    -- An illustrative SQL query demonstrating the rule applied to example dataset(s).
    select
        o_orderkey
        , o_orderdate
    from orders 
    where
        o_orderdate < '1991-01-01 10:30:00'
        or o_orderdate > '1991-12-31 15:00:00'
    ```

**Potential Violation Messages**

=== "Record Anomaly"
    !!! example
        The value for `O_ORDERDATE` of `1990-12-31 10:30:00` is not between **1991-01-01 10:30:00** and **1991-12-31 15:00:00**.
=== "Shape Anomaly"
    !!! example
        In `O_ORDERDATE`, 66.667% of 3 filtered records (2) are not between **1991-01-01 10:30:00** and **1991-12-31 15:00:00**.
