# Matches Pattern

### Definition

*Asserts that a field must match a pattern.*

#### In-Depth Overview

Patterns, typically expressed as regular expressions, allow for the enforcement of custom structural norms for data fields. For complex patterns, regular expressions offer a powerful tool to ensure conformity to the expected format.

### Field Scope

**Single:** The rule evaluates a single specified field.

**Accepted Types**

| Type        |                          |
|-------------|--------------------------|
| `String`    | <div style="text-align:center">:octicons-check-16:</div>  |

### General Properties

{%
    include-markdown "components/general-props/index.md"
    start='<!-- all-props--start -->'
    end='<!-- all-props--end -->'
%}

### Specific Properties

Allows specifying a pattern against which the field will be checked.

| Name                 | Description |
|----------------------|-------------|
| <div class="text-primary">Pattern</div>          | Specifies the regular expression pattern the field must match. |

### Anomaly Types

{%
    include-markdown "components/anomaly-support/index.md"
    start='<!-- all-types--start -->'
    end='<!-- all-types--end -->'
%}

### TPC-H Example

**Objective**: *Ensure that all P_SERIAL entries in the PART table match the pattern for product serial numbers: `TPCH-XXXX-####`, where `XXXX` are uppercase alphabetic characters and `####` are numbers.*

**Sample Data**

| P_PARTKEY | P_SERIAL                    |
|-----------|-----------------------------|
| 1         | TPCH-ABCD-1234              |
| 2         | <span class="text-negative">TPCH-1234-ABCD</span>  |
| 3         | TPCH-WXYZ-9876              |

**Anomaly Explanation**

In the sample data above, the entry with `P_PARTKEY` **2** does not satisfy the rule because its `P_SERIAL` does not match the required pattern.

=== "Flowchart"
    ```mermaid
    graph TD
    A[Start] --> B[Retrieve P_SERIAL]
    B --> C{Does P_SERIAL match TPCH-XXXX-#### format?}
    C -->|Yes| D[Move to Next Record/End]
    C -->|No| E[Mark as Anomalous]
    E --> D
    ```

=== "SQL"
    ```sql
    -- An illustrative SQL query related to the rule using TPC-H tables.
    select
        p_partkey,
        p_serial
    from part 
    where
        not regexp_like(p_serial, '^tpch-[a-z]{4}-[0-9]{4}$')
    ```

**Potential Violation Messages**

=== "Record Anomaly"
    !!! example
        The `P_SERIAL` value of `TPCH-1234-ABCD` does not match the pattern `TPCH-XXXX-####`.
        
=== "Shape Anomaly"
    !!! example
        In `P_SERIAL`, 33.333% of 3 filtered records (1) do not match the pattern `TPCH-XXXX-####`.
