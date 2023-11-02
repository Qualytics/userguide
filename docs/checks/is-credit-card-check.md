# Is Credit Card

### Definition

*Asserts that the values are credit card numbers.*

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

### Anomaly Types

{%
    include-markdown "components/anomaly-support/index.md"
    start='<!-- all-types--start -->'
    end='<!-- all-types--end -->'
%}

### TPC-H Example

**Objective**: *Ensure that all C_CREDIT_CARD entries in the CUSTOMER table are valid credit card numbers.*

**Sample Data**

| C_CUSTKEY | C_CREDIT_CARD                           |
|-----------|----------------------------------------|
| 1         | 5105105105105100                        |
| 2         | <span class="text-negative">ABC12345XYZ</span>        |
| 3         | 4111111111111111                        |

**Anomaly Explanation**

In the sample data above, the entry with `C_CUSTKEY` **2** does not satisfy the rule because its `C_CREDIT_CARD` value is not a valid credit card number.

=== "Flowchart"
    ``` mermaid
    graph TD
    A[Start] --> B[Retrieve C_CREDIT_CARD]
    B --> C{Is C_CREDIT_CARD valid?}
    C -->|Yes| D[Move to Next Record/End]
    C -->|No| E[Mark as Anomalous]
    E --> D
    ```

=== "SQL"
    ```sql
    -- An illustrative SQL query related to the rule using TPC-H tables.
    select
        c_custkey
        , c_credit_card
    from customer 
    where
        not regexp_like(replace(c_credit_card, '-', ''), '^[0-9]{16}$')
    ```

**Potential Violation Messages**

=== "Record Anomaly"
    !!! example
        The `C_CREDIT_CARD` value of `ABC12345XYZ` is not a valid credit card number.

=== "Shape Anomaly"
    !!! example
        In `C_CREDIT_CARD`, 33.33% of 3 filtered records (1) are not valid credit card numbers.
