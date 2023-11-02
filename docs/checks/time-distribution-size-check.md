# Time Distribution Size

### Definition

*Asserts that the count of records for each interval of a timestamp is between two numbers.*

### In-Depth Overview

The `Time Distribution Size` rule helps in identifying irregularities in the distribution of records over time intervals such as hours, days, or months.

For instance, in a retail context, it could ensure that there’s a consistent number of orders each month to meet business targets. A sudden drop in orders might highlight operational issues or shifts in market demand that require immediate attention.

### Field Scope

**Single:** The rule evaluates a single specified field.

**Accepted Types**

| Type        |                          |
|-------------|--------------------------|
| `Timestamp` | <div style="text-align:center">:octicons-check-16:</div> |
| `Date`      | <div style="text-align:center">:octicons-check-16:</div> |

### Specific Properties

| Name          | Description                                            |
|---------------|--------------------------------------------------------|
| <div class="text-primary">Interval</div>      | Defines the time interval for segmentation.            |
| <div class="text-primary">Min Count</div>     | Specifies the minimum count of records in each segment. |
| <div class="text-primary">Max Count</div>     | Specifies the maximum count of records in each segment. |

### Anomaly Types

{%
    include-markdown "components/anomaly-support/index.md"
    start='<!-- shape-only--start -->'
    end='<!-- shape-only--end -->'
%}

### Example

**Objective**: *Ensure that the number of orders for each month is consistently between 5 and 10.*

**Sample Data**

| O_ORDERKEY | O_ORDERDATE  |
|------------|--------------|
| 1          | 2023-01-01   |
| 2          | 2023-01-15   |
| 3          | 2023-01-20   |
| 4          | 2023-01-25   |
| 5          | 2023-02-01   |
| 6          | 2023-02-05   |
| 7          | 2023-02-10   |
| 8          | 2023-02-15   |
| 9          | 2023-02-20   |
| 10         | 2023-02-25   |
| 11         | 2023-02-28   |

**Anomaly Explanation**

In the sample data above, the January segment fails the rule because there are only 4 orders, which is below the specified minimum count of 5.

=== "Flowchart"
    ```mermaid
    graph TD
    A[Start] --> B[Retrieve O_ORDERDATE]
    B --> C{Segment data by month}
    C --> D{Is count of records in each segment between 5 and 10?}
    D -->|Yes| E[End]
    D -->|No| F[Mark as Anomalous]
    F --> E
    ```

=== "SQL"
    ```sql
    -- An illustrative SQL query demonstrating the rule applied to example dataset(s).
    select 
        extract(month from o_orderdate) as month,
        count(*) as order_count
    from 
        orders 
    group by 
        extract(month from o_orderdate)
    having 
        count(*) < 5
        or count(*) > 10;
    ```

**Potential Violation Messages**

!!! example "Shape Anomaly"
    50.000% of the monthly segments of `O_ORDERDATE` have record counts not between 5 and 10.
