# Expected Schema

### Definition

*Asserts that all of the selected fields must be present in the datastore.*

### Behavior

The expected schema is the first check to be tested during a scan operation. If it fails, the scan operation will result as `Failure` with the following message:

*`<container-name>`: Aborted because schema check anomalies were identified*.

### General Properties

{% 
    include-markdown "components/general-props/index.md"
    start='<!-- none-props--start -->'
    end='<!-- none-props--end -->' 
%}

### Specific Properties

Specify the fields that must be present in the schema, and determine if a schema change caused by additional fields should fail or pass the assertion.

| Name                      | Description                                                   |
|---------------------------|---------------------------------------------------------------|
| <div class="text-primary">Fields</div> | List of fields that must be presented in the schema. |
| <div class="text-primary">Allow other fields</div> | If true, then new fields are allowed to be presented in the schema. Otherwise, the assertion will be stricter. |

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
