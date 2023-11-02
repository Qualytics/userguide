# Before Date Time

### Definition

*Asserts that the field is a timestamp earlier than a specific date and time.*

### Field Scope

**Single:** The rule evaluates a single specified field.

**Accepted Types**

| Type       |                          |
|------------|--------------------------|
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
| <div class="text-primary">Date</div>  | The timestamp used as the upper boundary. Values in the selected field should be before this timestamp. |


### Anomaly Types

{%
    include-markdown "components/anomaly-support/index.md"
    start='<!-- all-types--start -->'
    end='<!-- all-types--end -->'
%}

### Example

**Objective**: *Ensure that all L_SHIPDATE entries in the LINEITEM table are earlier than 3:00 PM on December 1st, 1998.*

**Sample Data**

| L_ORDERKEY | L_SHIPDATE           |
|------------|-----------------------|
| 1          | <span style="color: #E91E63">1998-12-01 15:30:00</span> |
| 2          | 1998-11-02 12:45:00   |
| 3          | 1998-08-01 10:20:00   |

**Anomaly Explanation**

In the sample data above, the entry with `L_ORDERKEY` **1** does not satisfy the rule because its `L_SHIPDATE` value is not before **1998-12-01 15:00:00**.

=== "Flowcharts"
    ``` mermaid
    graph TD
    A[Start] --> B[Retrieve L_SHIPDATE]
    B --> C{Is L_SHIPDATE < '1998-12-01 15:00:00'?}
    C -->|Yes| D[Move to Next Record/End]
    C -->|No| E[Mark as Anomalous]
    E --> D
    ```

=== "SQL"
    ```sql
    -- An illustrative SQL query demonstrating the rule applied to example dataset(s).
    select
        l_orderkey
        , l_shipdate
    from lineitem 
    where
        l_shipdate >= '1998-12-01 15:00:00'
    ```

**Potential Violation Messages**

!!! example "Record Anomaly"
    The `L_SHIPDATE` value of `1998-12-01 15:30:00` is not earlier than **1998-12-01 15:00:00**.
        
!!! example "Shape Anomaly"
    In `L_SHIPDATE`, 33.33% of 3 filtered records (1) are not earlier than **1998-12-01 15:00:00**.
