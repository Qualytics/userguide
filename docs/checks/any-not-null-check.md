# Any Not Null

### Definition

*Asserts that at least one of the selected fields must hold a value.*

### Field Scope

**Multiple:** The rule evaluates multiple specified fields.

**Accepted Types**

| Type          |                          |
|---------------|--------------------------|
| `Date`        | <div style="text-align:center">:octicons-check-16:</div>  |
| `Timestamp`   | <div style="text-align:center">:octicons-check-16:</div>  |
| `Integral`    | <div style="text-align:center">:octicons-check-16:</div>  |
| `Fractional`  | <div style="text-align:center">:octicons-check-16:</div>  |
| `String`      | <div style="text-align:center">:octicons-check-16:</div>  |
| `Boolean`     | <div style="text-align:center">:octicons-check-16:</div>  |

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

**Objective**: *Ensure that for every record in the ORDERS table, at least one of the fields (O_COMMENT, O_ORDERSTATUS) isn't null.*

**Sample Data**

| O_ORDERKEY | O_COMMENT          | O_ORDERSTATUS |
|------------|--------------------|---------------|
| 1          | <span class="text-negative">NULL</span> | <span class="text-negative">NULL</span> |
| 2          | Good product      | NULL          |
| 3          | NULL               | Shipped       |

**Anomaly Explanation**

In the sample data above, the entry with `O_ORDERKEY` **1** does not satisfy the rule because both `O_COMMENT` and `O_ORDERSTATUS` does not hold a value.

=== "Flowchart"
    ``` mermaid
    graph TD
    A[Start] --> B[Retrieve O_COMMENT and O_ORDERSTATUS]
    B --> C{Is Either Field Not Null?}
    C -->|Yes| D[Move to Next Record/End]
    C -->|No| E[Mark as Anomalous]
    E --> D
    ```
=== "SQL"
    ```sql
    -- An illustrative SQL query demonstrating the rule applied to example dataset(s).
    select
        o_orderkey
        , o_comment
        , o_orderstatus
    from orders 
    where
        o_comment is null
        and o_orderstatus is null
    ```

**Potential Violation Messages**

=== "Record Anomaly"
    !!! example
        There is no value set for any of `O_COMMENT, O_ORDERSTATUS`

=== "Shape Anomaly"
    !!! example
        In `O_COMMENT, O_ORDERSTATUS`, 33.333% of 3 filtered records (1) have no value set for any of `O_COMMENT, O_ORDERSTATUS`
