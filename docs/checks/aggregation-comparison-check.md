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
    start='<!-- filter-only--start -->'
    end='<!-- filter-only--end -->'
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

!!! note "Details"

    It's important to understand that each aggregation must result in a **single row**. Also, similar to Spark expressions, the aggregation expressions must be written in a valid format for DataFrames.

    !!! example "Examples"

        **Simple Aggregations**
        ```sql
        SUM(O_TOTALPRICE)
        ```

        **Combining with SparkSQL Functions**
        ```sql
        ROUND(SUM(O_TOTALPRICE))
        ```

        **Complex Aggregations**
        ```sql
        ROUND(SUM(L_EXTENDEDPRICE * (1 - L_DISCOUNT) * (1 + L_TAX)))
        ```

        **Aggregation Expressions**
        ```sql
        COUNT(CATEGORY) * MAX(VALUE) - FIRST(VALUE)
        ```

    Here are some common aggregate functions used in SparkSQL:

    - `SUM`: Calculates the sum of all values in a column.
    - `AVG`: Calculates the average of all values in a column.
    - `MAX`: Returns the maximum value in a column.
    - `MIN`: Returns the minimum value in a column.
    - `COUNT`: Counts the number of rows in a column.

    For a detailed list of valid SparkSQL aggregation functions, refer to the [Apache Spark SQL documentation](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/functions.html#aggregate-functions).

=== "Payload example"
    ``` json
    {
        "description": "The aggregation \"SUM(`TARGET_FIELD`)\" must be less than a reference value",
        "coverage": 1,
        "properties": {
            "ref_datastore_id": ref_datastore_id,
            "expression": "SUM(`TARGET_FIELD`)",
            "comparison": "lt",
            "ref_container_id": ref_container_id,
            "ref_expression": "MAX(`REFERENCE_FIELD`)"
        },
        "fields": fields,
        "status": "Active",
        "rule": "aggregationComparison",
        "additional_metadata": {"key 1": "value 1", "key 2": "value 2"},
        "container_id": {container_id},
        "template_id": {template_id},
    }
    ```

### Anomaly Types

{%
    include-markdown "components/anomaly-support/index.md"
    start='<!-- shape-only--start -->'
    end='<!-- shape-only--end -->'
%}

### Example

**Objective**: *Ensure that the aggregated sum of `total_price` from the `ORDERS` table matches the aggregated and rounded sum of `calculated_price` from the `LINEITEM` table.*

!!! info
    The `calculated_price` in this example is represented by the sum of each product's extended price, adjusted for discount and tax.
    
**Sample Data**

_Aggregated data from ORDERS (Target)_

| TOTAL_PRICE |
|-------------|
| 5000000     |

_Aggregated data from LINEITEM (Reference)_

| CALCULATED_PRICE |
|------------------|
| 4999800          |

??? example "Inputs"
    - **Target Aggregation**: ROUND(SUM(O_TOTALPRICE))
    - **Comparison**: eq (Equal To), lt (Less Than), lte (Less Than or Equal to), gte (Greater Than or Equal To), gt (Greater Than)
    - **Reference Aggregation**: ROUND(SUM(L_EXTENDEDPRICE * (1 - L_DISCOUNT) * (1 + L_TAX)))

=== "Payload example"
    ``` json
    {
        "description": "Ensure that the aggregated sum of total_price from the ORDERS table matches the aggregated and sum of l_totalprice from the LINEITEM table",
        "coverage": 1,
        "properties": {
            "comparison": "eq",
            "expression": f"SUM(O_TOTALPRICE)",
            "ref_container_id": ref_container_id,
            "ref_datastore_id": ref_datastore_id,
            "ref_expression": f"SUM(L_TOTALPRICE)",
            "ref_filter": "1=1",
        },
        "tags": [],
        "fields": ["O_TOTALPRICE"],
        "additional_metadata": {"key 1": "value 1", "key 2": "value 2"},
        "rule": "aggregationComparison",
        "container_id": {container_id},
        "template_id": {template_id},
        "filter": "1=1"
    }
    ```

**Anomaly Explanation**

In the sample data above, the aggregated `TOTAL_PRICE` from the `ORDERS` table is 5000000, while the aggregated and rounded `CALCULATED_PRICE` from the `LINEITEM` table is 4999800. The difference between these totals indicates a potential anomaly, suggesting issues in data calculation or recording methods.

=== "Flowchart"
    ```mermaid
    graph TD
    A[Start] --> B[Retrieve Aggregated Values]
    B --> C{Do Aggregated Totals Match?}
    C -->|Yes| D[End]
    C -->|No| E[Mark as Anomalous]
    E --> D
    ```

=== "SQL"
    ```sql
    -- An illustrative SQL query related to the rule using TPC-H tables.
    with orders_agg as (
        select 
            round(sum(o_totalprice)) as total_order_price
        from 
            orders
    ),
    lineitem_agg as (
        select 
            round(sum(l_extendedprice * (1 - l_discount) * (1 + l_tax))) as calculated_price
        from 
            lineitem
    ),
    comparison as (
        select
            o.total_order_price,
            l.calculated_price
        from
            orders_agg o
            cross join lineitem_agg l
    )
    select * from comparison
    where comparison.total_order_price != comparison.calculated_price;
    ```

**Potential Violation Messages**

!!! example "Shape Anomaly"
    `ROUND(SUM(O_TOTALPRICE))` is not equal to `ROUND(SUM(L_EXTENDEDPRICE * (1 - L_DISCOUNT) * (1 + L_TAX)))`.
