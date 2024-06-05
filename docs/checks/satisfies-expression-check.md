# Satisfies Expression

### Definition

*Evaluates the given expression (any valid Spark SQL) for each record.*

### In-Depth Overview

The `Satisfies Expression` rule allows for a wide range of custom validations on the dataset. By defining a Spark SQL expression, you can create customized conditions that the data should meet.

This rule will evaluate an expression against each record, marking those that do not satisfy the condition as anomalies. It provides the flexibility to create complex validation logic without being restricted to predefined rule structures.

### Field Scope

**Calculated:** The rule automatically identifies the fields involved, without requiring explicit field selection.

### General Properties

{%
    include-markdown "components/general-props/index.md"
    start='<!-- all-props--start -->'
    end='<!-- all-props--end -->'
%}

### Specific Properties

Evaluates each record against a specified Spark SQL expression to ensure it meets custom validation conditions.

| Name        | Description                                                    |
|-------------|----------------------------------------------------------------|
| <div class="text-primary">Expression</div> | Defines the Spark SQL expression that each record should meet. |

!!! info

    Refers to the **Filter Guide** in the [**General Properties**](#general-properties) topic for examples of valid Spark SQL expressions.

### Anomaly Types

{%
    include-markdown "components/anomaly-support/index.md"
    start='<!-- all-types--start -->'
    end='<!-- all-types--end -->'
%}

### Example

**Objective**: *Ensure that the total tax applied to each item in the LINEITEM table is not more than 10% of the extended price.*

**Sample Data**

| L_ORDERKEY | L_LINENUMBER | L_EXTENDEDPRICE | L_TAX |
|------------|--------------|-----------------|-------|
| 1          | 1            | 10000           | 900   |
| 2          | 1            | <span class="text-negative">15000</span>           | <span class="text-negative">2000</span> |
| 3          | 1            | 20000           | 1800  |
| 4          | 1            | <span class="text-negative">10000</span>           | <span class="text-negative">1500</span> |

??? example "Inputs"
    - **Expression**: L_TAX <= L_EXTENDEDPRICE * 0.10

=== "Payload example"
    ``` json
    {
        "description": "Ensure that the total tax applied to each item in the LINEITEM table is not more than 10% of the extended price",
        "coverage": 1,
        "properties": {
            "expression":"L_TAX <= L_EXTENDEDPRICE * 0.10"
            },
        "tags": [],
        "fields": ["L_TAX", "L_EXTENDEDPRICE"],
        "additional_metadata": {"key 1": "value 1", "key 2": "value 2"},
        "rule": "satisfiesExpression",
        "container_id": {container_id},
        "template_id": {template_id},
        "filter": "1=1"
    }
    ```

**Anomaly Explanation**

In the sample data above, the entries with `L_ORDERKEY` **2** and **4** do not satisfy the rule because the `L_TAX` values are more than 10% of their respective `L_EXTENDEDPRICE` values.

=== "Flowchart"
    ```mermaid
    graph TD
    A[Start] --> B[Retrieve L_EXTENDEDPRICE and L_TAX]
    B --> C{Is L_TAX <= L_EXTENDEDPRICE * 0.10?}
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
        l_tax
    from
        lineitem 
    where
        l_tax > l_extendedprice * 0.10;
    ```

**Potential Violation Messages**

!!! example "Record Anomaly"
    The record does not satisfy the expression: `L_TAX <= L_EXTENDEDPRICE * 0.10`

!!! example "Shape Anomaly"
    50.000% of 4 filtered records (2) do not satisfy the expression: `L_TAX <= L_EXTENDEDPRICE * 0.10`
