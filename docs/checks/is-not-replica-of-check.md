# Is Not Replica Of

### Definition

*Asserts that the dataset created by the targeted field(s) is not replicated by the referred field(s).*

#### In-Depth Overview

The `IsNotReplicaOf` rule is designed to verify the distinctiveness of data across two sources. In scenarios where data uniqueness is imperative, this rule helps ensure that a given dataset isn't inadvertently duplicated in another location. By using this rule:

1. **Guarantee Data Differentiation**: It's crucial, especially in analytics and data science, to avoid working with redundant datasets that might skew interpretations or waste resources.
2. **Avoid Unintended Replications**: This rule serves as a preventive measure against unintended data replications which can result from misconfigurations or human error.

The utility of the `IsNotReplicaOf` feature extends to ensuring deliberate differences between data sources and guaranteeing that datasets remain distinct.

### Field Scope

**Multi:** The rule evaluates multiple specified fields.

**Accepted Types**

| Type        |                          |
|-------------|--------------------------|
| `Date`      | <div style="text-align:center">:octicons-check-16:</div>      |
| `Timestamp` | <div style="text-align:center">:octicons-check-16:</div>      |
| `Integral`  | <div style="text-align:center">:octicons-check-16:</div>      |
| `Fractional`| <div style="text-align:center">:octicons-check-16:</div>      |
| `String`    | <div style="text-align:center">:octicons-check-16:</div>      |
| `Boolean`   | <div style="text-align:center">:octicons-check-16:</div>      |

### Specific Properties

Specify the datastore and table/file to compare against the targeted fields to ensure data is not replicated.

| Name       | Description                                                   |
|------------|---------------------------------------------------------------|
| <div class="text-primary">Datastore</div>  | The source datastore where the comparison for the targeted field(s) is located. |
| <div class="text-primary">Table/file</div> | The table, view or file in the source datastore that should serve as the comparison point. |

### Anomaly Types

{%
    include-markdown "components/anomaly-support/index.md"
    start='<!-- shape-only--start -->'
    end='<!-- shape-only--end -->'
%}

### Example

**Scenario**: *Consider these 2 datasets: SALES and SALES_ARCHIVE. The SALES dataset contains transactions from the current year based on PRODUCT_NAME and SALE_DATE, while the SALES_ARCHIVE dataset contains archived transactions from previous years. Due to the nature of archiving, while some records from SALES might eventually move to SALES_ARCHIVE at the end of the year, the data subsets defined by the PRODUCT_NAME and SALE_DATE fields in the SALES dataset should never be an exact replica of the corresponding data in the SALES_ARCHIVE dataset at any given time.*

**Objective**: *Ensure that PRODUCT_NAME and SALE_DATE from SALES table are not replicas in the SALES_ARCHIVE table.*

**Sample Data from SALES**

| SALE_ID | PRODUCT_NAME | SALE_DATE   |
|---------|--------------|-------------|
| S1      | Laptop      | 2023-09-01  |
| S2      | Mobile      | 2023-09-02  |
| S3      | Headphones  | 2023-09-03  |

**Sample Data from SALES_ARCHIVE**

| SALE_ID | PRODUCT_NAME | SALE_DATE   |
|---------|--------------|-------------|
| A1      | Laptop      | 2023-09-01  |
| A2      | Mobile      | 2023-09-02  |
| A3      | Headphones  | 2023-09-03  |

**Anomaly Explanation**

The datasets defined by `PRODUCT_NAME` and `SALE_DATE` in `SALES` and `SALES_ARCHIVE` should have distinct entries. However, in this instance, they are identical, which would indicate a serious issue—potentially a data mishandling or a malfunction in the data archiving process.

=== "Flowchart"
    ```mermaid
    graph TD
    A[Start] --> B[Retrieve SALES Data]
    B --> C[Retrieve SALES_ARCHIVE Data]
    C --> D{Are PRODUCT_NAME and SALE_DATE identical across the datasets?}
    D -->|No| E[End]
    D -->|Yes| F[Mark as Anomalous]
    F --> E
    ```

=== "SQL"
    ```sql
    -- An illustrative SQL query comparing the current sales to sales archive based on PRODUCT_NAME and SALE_DATE.
    select
        product_name, 
        sale_date 
    from 
        sales 
    except 
    select 
        product_name, 
        sale_date 
    from 
        sales_archive
    ```

**Potential Violation Messages**

!!! example "Shape Anomaly"
    `SALES` and `SALES_ARCHIVE` are replicas with 3 records each

