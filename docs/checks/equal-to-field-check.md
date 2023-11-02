# Equal To Field

### Definition

*Asserts that a field is equal to another field.*

### Field Scope

**Single:** The rule evaluates a single specified field.

**Accepted Types**

| Type        |                            |
|-------------|----------------------------|
| `Date`      | <div style="text-align:center">:octicons-check-16:</div>        |
| `Timestamp` | <div style="text-align:center">:octicons-check-16:</div>        |
| `Integral`  | <div style="text-align:center">:octicons-check-16:</div>        |
| `Fractional`| <div style="text-align:center">:octicons-check-16:</div>        |

### General Properties

{%
    include-markdown "components/general-props/index.md"
    start='<!-- all-props--start -->'
    end='<!-- all-props--end -->'
%}

### Specific Properties

Specify the field to compare for equality with the selected field.

| Name                 | Description                                                                   |
|----------------------|-------------------------------------------------------------------------------|
| <div class="text-primary">Field to compare</div> | The field name whose values should match those of the selected field. |

### Anomaly Types

{%
    include-markdown "components/anomaly-support/index.md"
    start='<!-- all-types--start -->'
    end='<!-- all-types--end -->'
%}

### Example

**Scenario**: *An e-commerce platform sells digital products. The shipping date (when the digital product link is sent) should always be the same as the delivery date (when the customer acknowledges receiving the product).*

**Objective**: *Ensure that the O_SHIPDATE in the ORDERS table matches its delivery date O_DELIVERYDATE.*

**Sample Data**

| O_ORDERKEY | O_SHIPDATE  | O_DELIVERYDATE |
|------------|-------------|----------------|
| 1          | 1998-01-04  | 1998-01-04     |
| 2          | <span class="text-negative">1998-01-14</span>  | 1998-01-15 |
| 3          | 1998-01-12  | 1998-01-12     |

**Anomaly Explanation**

In the sample data above, the entry with `O_ORDERKEY` **2** does not satisfy the rule because its `O_SHIPDATE` of 1998-01-14 does not match the `O_DELIVERYDATE` of 1998-01-15.

=== "Flowchart"
    ``` mermaid
    graph TD
    A[Start] --> B[Retrieve O_SHIPDATE and O_DELIVERYDATE]
    B --> C{Is O_SHIPDATE = O_DELIVERYDATE?}
    C -->|Yes| D[Move to Next Record/End]
    C -->|No| E[Mark as Anomalous]
    E --> D
    ```

=== "SQL"
    ```sql
    -- An illustrative SQL query demonstrating the rule applied to example dataset(s).
    select
        o_orderkey,
        o_shipdate,
        o_deliverydate
    from orders 
    where
        o_shipdate != o_deliverydate
    ```

**Potential Violation Messages**

=== "Record Anomaly"
    !!! example
        The `O_SHIPDATE` value of 1998-01-14 is not equal to the value of O_DELIVERYDATE which is 1998-01-15.

=== "Shape Anomaly"
    !!! example
        In `O_SHIPDATE`, 33.333% of the filtered fields are not equal.
