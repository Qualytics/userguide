# Required Fields

### Definition

*Asserts that all of the selected fields must be present in the datastore.*

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

{%
    include-markdown "components/general-props/index.md"
    start='<!-- none-props--start -->'
    end='<!-- none-props--end -->' 
%}

### Anomaly Types

{%
    include-markdown "components/anomaly-support/index.md"
    start='<!-- shape-only--start -->'
    end='<!-- shape-only--end -->'
%}

### Example

**Objective**: *Ensure that required fields such as L_ORDERKEY, L_PARTKEY, and L_SUPPKEY are always present in the LINEITEM table.*

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

Among the presented sample schemas, the second one is missing one of the required fields. Only the first schema has the correct required fields.

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
    One of the required fields (`L_SUPPKEY`) are missing.
