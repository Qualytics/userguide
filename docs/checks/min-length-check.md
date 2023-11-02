# Min Length

### Definition

*Asserts that a string has a minimum length.*

### Field Scope

**Single:** The rule evaluates a single specified field.

**Accepted Types**

| Type       |                          |
|------------|--------------------------|
| `String`   | <div style="text-align:center">:octicons-check-16:</div>  |

### General Properties

{%
    include-markdown "components/general-props/index.md"
    start='<!-- all-props--start -->'
    end='<!-- all-props--end -->'
%}

### Specific Properties

Determines the minimum allowable length for the field.

| Name               | Description |
|--------------------|-------------|
| <div class="text-primary">Value</div> | Specifies the minimum length that the string field should have. |

### Anomaly Types

{%
    include-markdown "components/anomaly-support/index.md"
    start='<!-- all-types--start -->'
    end='<!-- all-types--end -->'
%}

### Example

**Objective**: *Ensure that all C_COMMENT entries in the CUSTOMER table have a minimum length of 5 characters.*

**Sample Data**

| C_CUSTKEY | C_COMMENT                                       |
|-----------|------------------------------------------------|
| 1         | <span class="text-negative">Ok</span>       |
| 2         | Excellent customer service, very satisfied!    |
| 3         | Nice staff          |

**Anomaly Explanation**

In the sample data above, the entry with `C_CUSTKEY` **1** does not satisfy the rule because the length of its `C_COMMENT` values is below the required minimum length of 5 characters.

=== "Flowchart"
    ```mermaid
    graph TD
    A[Start] --> B[Retrieve C_COMMENT]
    B --> C{Is C_COMMENT length >= 5?}
    C -->|Yes| D[Move to Next Record/End]
    C -->|No| E[Mark as Anomalous]
    E --> D
    ```

=== "SQL"
    ```sql
    -- An illustrative SQL query demonstrating the rule applied to example dataset(s).
    select
        c_custkey,
        c_comment
    from customer 
    where
        length(c_comment) < 5;
    ```

**Potential Violation Messages**

!!! example "Record Anomaly"
    The `C_COMMENT` length of `Ok` is less than the min length of 5.
    
!!! example "Shape Anomaly"
    In `C_COMMENT`, 33.333% of 3 filtered records (1) have a length less than 5.
