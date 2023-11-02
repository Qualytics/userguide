# Not Future

### Definition

*Asserts that the field's value is not in the future.*

### Field Scope

**Single:** The rule evaluates a single specified field.

**Accepted Fields**

| Field       |                             |
|-------------|-----------------------------|
| `Date`      | <div style="text-align:center">:octicons-check-16:</div>         |
| `Timestamp` | <div style="text-align:center">:octicons-check-16:</div>         |

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

**Objective**: *Ensure that the delivery dates (O_DELIVERYDATE) in the ORDERS table are not set in the future.*

**Sample Data**

| O_ORDERKEY | O_DELIVERYDATE              |
|------------|-----------------------------|
| 1          | 2023-09-20                  |
| 2          | <span class="text-negative">2023-10-25 (Future Date)</span>    |
| 3          | 2023-10-10                  |

**Anomaly Explanation**

In the sample data above, the entry with `O_ORDERKEY` **2** does not satisfy the rule because its `O_DELIVERYDATE` is set in the future.

=== "Flowchart"
    ```mermaid
    graph TD
    A[Start] --> B[Retrieve O_DELIVERYDATE]
    B --> C{Is O_DELIVERYDATE <= Current Date?}
    C -->|Yes| D[Move to Next Record/End]
    C -->|No| E[Mark as Anomalous]
    E --> D
    ```

=== "SQL"
    ```sql
    -- An illustrative SQL query demonstrating the rule applied to example dataset(s).
    select
        o_orderkey,
        o_deliverydate
    from orders 
    where
        o_deliverydate > current_date;
    ```

**Potential Violation Messages**

=== "Record Anomaly"
    !!! example
        The value for `O_DELIVERYDATE` of `2023-10-25` is in the future.

=== "Shape Anomaly"
    !!! example
        In `O_DELIVERYDATE`, 33.333% of 3 filtered records (1) are future times.
