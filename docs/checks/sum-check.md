# Sum

### Definition

*Asserts that the sum of a field is a specific amount.*

### Field Scope

**Single:** The rule evaluates a single specified field.

**Accepted Types**

| Type        |                          |
|-------------|--------------------------|
| `Integral`  | <div style="text-align:center">:octicons-check-16:</div> |
| `Fractional`| <div style="text-align:center">:octicons-check-16:</div> |

### General Properties

{%
    include-markdown "components/general-props/index.md"
    start='<!-- all-props--start -->'
    end='<!-- all-props--end -->'
%}

### Specific Properties

Ensures that the total sum of values in a specified field matches a defined amount.

| Name               | Description                                         |
|--------------------|-----------------------------------------------------|
| <div class="text-primary">Sum</div> | Specifies the expected sum of the values in the field. |

### Anomaly Types

{%
    include-markdown "components/anomaly-support/index.md"
    start='<!-- shape-only--start -->'
    end='<!-- shape-only--end -->'
%}

### TPC-H Example

**Objective**: *Ensure that the total discount value in the LINEITEM table does not exceed $2000.*

**Sample Data**

| L_ORDERKEY | L_LINENUMBER | L_EXTENDEDPRICE | L_DISCOUNT | L_DISCOUNT_VALUE |
|------------|--------------|-----------------|------------|------------------|
| 1          | 1            | 10000           | 0.05       | 500              |
| 2          | 1            | 8000            | 0.10       | 800              |
| 3          | 1            | 7000            | 0.05       | 350              |
| 4          | 1            | 5000            | 0.10       | 500              |

**Anomaly Explanation**

In the sample data above, the total of the `L_DISCOUNT_VALUE` column is (500 + 800 + 350 + 500 = 2150), which exceeds the specified maximum total discount value of $2000.

=== "Flowchart"
    ```mermaid
    graph TD
    A[Start] --> B[Retrieve L_DISCOUNT_VALUE]
    B --> C{Sum of L_DISCOUNT_VALUE <= 2000?}
    C -->|Yes| D[End]
    C -->|No| E[Mark as Anomalous]
    E --> D
    ```

=== "SQL"
    ```sql
    -- An illustrative SQL query related to the rule using TPC-H tables.
    select 
        sum(l_discount_value) as total_discount_value
    from 
        lineitem 
    having 
        sum(l_discount_value) > 2000;
    ```

**Potential Violation Messages**

=== "Shape Anomaly"
    !!! example
        In `L_DISCOUNT_VALUE`, the sum of the 4 records is not 2000.000
