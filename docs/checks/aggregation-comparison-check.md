# Aggregation Comparison

### Definition

*Verifies that the specified comparison operator evaluates true when applied to two aggregation expressions.*

### In-Depth Overview

The `Aggregation Comparison` is a rule that allows for the dynamic analysis of aggregations across different datasets. It empowers users to establish data integrity by ensuring that aggregate values meet expected comparisons, whether they are totals, averages, counts, or any other aggregated metric.

By setting a comparison between aggregates from potentially different tables or even source datastores, this rule confirms that relationships between data points adhere to business logic or historical data patterns. This is particularly useful when trying to validate interrelated financial reports, summary metrics, or when monitoring the consistency of data ingestion over time.

### Field Scope

**Calculated:** The rule automatically identifies the fields involved, without requiring explicit field selection.

### General Properties

{%
    include-markdown "components/general-props/index.md"
    start='<!-- all-props--start -->'
    end='<!-- all-props--end -->'
%}

### Specific Properties

Facilitates the comparison between a `target` aggregate metric and a `reference` aggregate metric across different datasets.

| Name                           | Description                                               |
|--------------------------------|-----------------------------------------------------------|
| <div class="text-primary">Target Aggregation</div> | Specifies the aggregation expression to evaluate |
| <div class="text-primary">Comparison</div>            | Select the comparison operator (e.g., greater than, less than, etc.) |
| <div class="text-primary">Datastore</div>             | Identifies the source datastore for the reference aggregation |
| <div class="text-primary">Table/File</div>            | Specifies the table or file for the reference aggregation |
| <div class="text-primary">Reference Aggregation</div> | Defines the reference aggregation expression to compare against |
| <div class="text-primary">Reference Filter</div>      | Applies a filter to the reference aggregation if necessary |

!!! info

    Refers to the **Filter Guide** in the [**General Properties**](#general-properties) topic for examples of valid Spark SQL expressions.

### Anomaly Types

{%
    include-markdown "components/anomaly-support/index.md"
    start='<!-- shape-only--start -->'
    end='<!-- shape-only--end -->'
%}

### Example

**Objective**: *Ensure that the total price of orders from the `ORDERS` table is always greater than the total discount given in the `LINEITEM` table.*

**Sample Data**

| O_ORDERKEY | TOTAL_PRICE (ORDERS) | TOTAL_DISCOUNT (LINEITEM) |
|------------|----------------------|---------------------------|
| 1          | 50000                | 1000                      |
| 2          | <span class="text-negative">25000</span>                | <span class="text-negative">30000</span> |
| 3          | 75000                | 2000                      |
| 4          | <span class="text-negative">15000</span> | <span class="text-negative">500</span>                       |

**Anomaly Explanation**

In the sample data above, the entries with `O_ORDERKEY` **2** and **4** do not satisfy the rule because the `TOTAL_PRICE` for these orders is not greater than the `TOTAL_DISCOUNT`, which violates the business logic that the total price should always exceed the total discount.

=== "Flowchart"
    ```mermaid
    graph TD
    A[Start] --> B[Retrieve Aggregated Values]
    B --> C{Does Target and Reference aggregations meet comparison criteria?}
    C -->|Yes| D[End]
    C -->|No| E[Mark as Anomalous]
    E --> D
    ```

=== "SQL"
    ```sql
    -- An illustrative SQL query demonstrating the rule applied to example datasets
    with target as (
        select 
            o_orderkey, 
            sum(o_totalprice) as totalorderprice
        from 
            orders
        group by 
            o_orderkey
    ),
    reference as (
        select 
            l_orderkey, 
            sum(l_discount) as totaldiscount
        from 
            lineitem
        group by 
            l_orderkey
    )
    select 
        o.o_orderkey, 
        o.totalorderprice, 
        l.totaldiscount
    from 
        target o
    join 
        reference l on o.o_orderkey = l.l_orderkey
    where 
        o.totalorderprice <= l.totaldiscount;
    ```

**Potential Violation Messages**

!!! example "Shape Anomaly"
    `TOTAL_PRICE` is not greater than `TOTAL_DISCOUNT` for `O_ORDERKEY`.
