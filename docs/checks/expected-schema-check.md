# Expected Schema

### Definition

*Asserts that all of the selected fields must be present in the datastore.*

### Behavior:

The expected schema is the first check to be tested during a scan operation. If it fails, the scan operation will result as `Failure` with the following message:

*`<container-name>`: Aborted because schema check anomalies were identified*.

### Field Scope

**Multi:** The rule evaluates multiple specified fields.

**Accepted Types**

| Type        |                          |
|-------------|--------------------------|
| `Date`      | <div style="text-align:center">:octicons-check-16:</div> |
| `Timestamp` | <div style="text-align:center">:octicons-check-16:</div> |
| `Integral`  | <div style="text-align:center">:octicons-check-16:</div> |
| `Fractional`| <div style="text-align:center">:octicons-check-16:</div> |
| `String`    | <div style="text-align:center">:octicons-check-16:</div> |
| `Boolean`   | <div style="text-align:center">:octicons-check-16:</div> |

### General Properties

<!-- none-props--start -->
=== "Details"
    | Name    | Supported                |
    |---------|--------------------------|
    | <div class="grayscale" style="color: #357AE3;">Allow other fields</div><div>Allows additional fields during a scan if it's enabled</div>      | <div style="text-align:center">:octicons-check-16:</div>  |
<!-- none-props--end -->


### Anomaly Types

{%
    include-markdown "components/anomaly-support/index.md"
    start='<!-- shape-only--start -->'
    end='<!-- shape-only--end -->'
%}

### Example

**Objective**: *Ensure that expected fields such as L_ORDERKEY, L_PARTKEY, and L_SUPPKEY are always present in the LINEITEM table.*

**Sample Data**

???+ success "Valid"
    | FIELD_NAME      | FIELD_TYPE |
    |-----------------|------------|
    | L_ORDERKEY      | NUMBER     |
    | L_PARTKEY       | NUMBER     |
    | L_SUPPKEY       | NUMBER     |
    | L_LINENUMBER    | NUMBER     |
    | L_QUANTITY      | NUMBER     |
    | L_EXTENDEDPRICE | NUMBER     |
    | ...             | ...        |

???+ failure "Invalid"
    *L_SUPPKEY is missing from the schema*

    | FIELD_NAME      | FIELD_TYPE |
    |-----------------|------------|
    | L_ORDERKEY      | NUMBER     |
    | L_PARTKEY       | NUMBER     |
    | L_LINENUMBER    | NUMBER     |
    | L_QUANTITY      | NUMBER     |
    | L_EXTENDEDPRICE | NUMBER     |
    | ...             | ...        |

**Anomaly Explanation**

Among the presented sample schemas, the second one is missing one of the expected schema. Only the first schema has the correct expected schema.

=== "Flowchart"
    ```mermaid
    graph TD
    A[Start] --> B{Check for Field Presence}
    B -.->|Field is missing| C[Mark as Shape Anomaly]
    B -.->|All fields present| D[End]
    ```

=== "SQL"
    ```sql
    -- An illustrative SQL query to check the existence of columns.
    select 
        column_name 
    from 
        information_schema.columns 
    where 
        table_name = 'LINEITEM' and 
        column_name in ('L_ORDERKEY', 'L_PARTKEY', 'L_SUPPKEY');
    ```

**Potential Violation Messages**

!!! example "Shape Anomaly"
    The required fields (`L_SUPPKEY`) are not present.
