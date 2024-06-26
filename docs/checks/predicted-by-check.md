# Predicted By

### Definition

*Asserts that the actual value of a field falls within an expected predicted range.*

### In-Depth Overview

The `Predicted By` rule is used to verify whether the actual values of a specific field align with a set of expected values that are derived from a prediction expression. This expression could be a mathematical formula, statistical calculation, or any other valid predictive logic.

### Field Scope

**Single:** The rule evaluates a single specified field.

**Accepted Fields**

| Type         |                             |
|--------------|-----------------------------|
| `Integral`   | <div style="text-align:center">:octicons-check-16:</div>         |
| `Fractional` | <div style="text-align:center">:octicons-check-16:</div>         |
| `Date`       | <div style="text-align:center">:octicons-check-16:</div>         |
| `Timestamp`  | <div style="text-align:center">:octicons-check-16:</div>         |

### General Properties

{%
    include-markdown "components/general-props/index.md"
    start='<!-- all-props--start -->'
    end='<!-- all-props--end -->'
%}

### Specific Properties

Determines if the actual value of a field falls within an expected predicted range.

| Name               | Description                                       |
|--------------------|---------------------------------------------------|
| <div class="text-primary">Expression</div> | The prediction expression or formula for the field. |
| <div class="text-primary">Tolerance</div> | The allowed deviation from the predicted value.      |

???+ note
    The **tolerance** level must be defined to allow a permissible range of deviation from the predicted values.

    Here’s a simple breakdown:

    - An **expression** predicts what the value of a field should be.
    - A **tolerance** value specifies how much deviation from the predicted value is acceptable.
    - The actual value is then compared against the range defined by the predicted value ± tolerance.

### Anomaly Types

{%
    include-markdown "components/anomaly-support/index.md"
    start='<!-- all-types--start -->'
    end='<!-- all-types--end -->'
%}

### Example

**Objective**: *Ensure that the discount (L_DISCOUNT) in the LINEITEM table is calculated correctly based on the actual price (L_EXTENDEDPRICE). A correct discount should be approximately 8% less than the actual price, within a tolerance of ±2.*

**Sample Data**

| L_ORDERKEY | L_LINENUMBER | L_EXTENDEDPRICE | L_DISCOUNT |
|------------|--------------|-----------------|------------|
| 1          | 1            | 100             | 8          |
| 2          | 1            | 100             | <span class="text-negative">12</span>         |
| 3          | 1            | 100             | 9          |

??? example "Inputs"
    - **Expression**: L_EXTENDEDPRICE × 0.08
    - **Tolerance**: 2

=== "Payload example"
    ``` json
    {
        "description": "Ensure that the discount (L_DISCOUNT) in the LINEITEM table is calculated correctly based on the actual price (L_EXTENDEDPRICE). A correct discount should be approximately 8% less than the actual price, within a tolerance of ±2",
        "coverage": 1,
        "properties": {
            "expression": "L_EXTENDEDPRICE × 0.08",
            "tolerance": 2
        },
        "tags": [],
        "fields": ["L_DISCOUNT"],
        "additional_metadata": {"key 1": "value 1", "key 2": "value 2"},
        "rule": "predictedBy",
        "container_id": {container_id},
        "template_id": {template_id},
        "filter": "1=1"
    }
    ```

**Anomaly Explanation**

For the entry with `L_ORDERKEY` **2**, the discount is 12, which is outside of the computed range. Based on an 8% expected discount with a tolerance of ±2, the discount should be between 6 and 10 (calculated from the actual price of 100). Therefore, this record is marked as anomalous.

=== "Flowchart"
    ```mermaid
    graph TD
    A[Start] --> B[Retrieve L_EXTENDEDPRICE and L_DISCOUNT]
    B --> C{Is Discount within Predicted Range?}
    C -->|Yes| D[Move to Next Record/End]
    C -->|No| E[Mark as Anomalous]
    E --> D
    ```

=== "SQL"
    ```sql
    -- An illustrative SQL query demonstrating the rule applied to example dataset(s).
    select
        l_orderkey,
        l_linenumber,
        l_extendedprice,
        l_discount
    from lineitem 
    where
        l_discount not between l_extendedprice * 0.06 and l_extendedprice * 0.10;
    ```

**Potential Violation Messages**

!!! example "Record Anomaly"
    The `L_DISCOUNT` value of '12' is not within the predicted range defined by L_EXTENDEDPRICE * 0.08 +/- 2.0

!!! example "Shape Anomaly"
    In `L_DISCOUNT`, 33.333% of 3 filtered records (1) are not within the predicted range defined by L_EXTENDEDPRICE * 0.08 +/- 2.0
