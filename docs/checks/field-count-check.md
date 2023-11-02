# Field Count

### Definition

*Asserts that there must be exactly a specified number of fields.*

### General Properties

{% 
    include-markdown "components/general-props/index.md"
    start='<!-- none-props--start -->'
    end='<!-- none-props--end -->' 
%}

### Specific Properties

Specify the exact number of fields expected in the profile.

| Name                      | Description                                                   |
|---------------------------|---------------------------------------------------------------|
| <div class="text-primary">Number of Fields</div> | The exact number of fields that should be present in the profile. |

### Anomaly Types

{% 
    include-markdown "components/anomaly-support/index.md"
    start='<!-- shape-only--start -->'
    end='<!-- shape-only--end -->' 
%}

### Example

**Objective**: *Ensure that the ORDERS profile contains exactly 9 fields.*

**Sample Profile**

???+ success "Valid"
    | FIELD_NAME      | FIELD_TYPE |
    |-----------------|------------|
    | O_ORDERKEY      | STRING     |
    | O_CUSTKEY       | STRING     |
    | O_ORDERSTATUS   | STRING     |
    | O_TOTALPRICE    | FLOAT      |
    | O_ORDERDATE     | DATE       |
    | O_ORDERPRIORITY | STRING     |
    | O_CLERK         | STRING     |
    | O_SHIPPRIORITY  | STRING     |
    | O_COMMENT       | STRING     |

???+ failure "Invalid"
    *count (8) less than expected (9)*

    | FIELD_NAME      | FIELD_TYPE |
    |-----------------|------------|
    | O_ORDERKEY      | STRING     |
    | O_CUSTKEY       | STRING     |
    | O_ORDERSTATUS   | STRING     |
    | O_TOTALPRICE    | FLOAT      |
    | O_ORDERDATE     | DATE       |
    | O_ORDERPRIORITY | STRING     |
    | O_CLERK         | STRING     |
    | O_COMMENT       | STRING     |

    *count (10) greater than expected (9)*

    | FIELD_NAME      | FIELD_TYPE |
    |-----------------|------------|
    | O_ORDERKEY      | STRING     |
    | O_CUSTKEY       | STRING     |
    | O_ORDERSTATUS   | STRING     |
    | O_TOTALPRICE    | FLOAT      |
    | O_ORDERDATE     | DATE       |
    | O_ORDERPRIORITY | STRING     |
    | O_CLERK         | STRING     |
    | O_COMMENT       | STRING     |
    | EXTRA_FIELD     | UNKOWN     |

**Anomaly Explanation**

Among the presented sample profiles, the second one is missing a field, while the third one contains an extra field. Only the first profile has the correct number of fields, which is 9.

=== "Flowchart"
    ``` mermaid
    graph TD
    A[Start] --> B[Retrieve Profile Fields]
    B --> C{Does the profile have exactly 9 fields?}
    C -->|Yes| D[End]
    C -->|No| E[Mark as Anomalous]
    E --> D
    ```

=== "SQL"
    ```sql
    -- An illustrative SQL query related to the rule.
    select
        table_name, count(column_name) as number_of_fields
    from information_schema.columns 
    where table_name = 'orders'
    group by table_name
    having count(column_name) <> 9
    ```

**Potential Violation Messages**

=== "Shape Anomaly"
    !!! example
        In `ORDERS`, the field count is not `9`.

