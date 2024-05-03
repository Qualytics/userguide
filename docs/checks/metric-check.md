# Metric

### Definition

*Records the value of the selected field during each scan operation and asserts limits based upon an expected change or absolute range (inclusive).*

### In-Depth Overview

The `Metric` rule is designed to monitor the values of a selected field over time. It is particularly useful in a time-series context where values are expected to evolve within certain bounds or limits. This rule allows for tracking absolute values or changes, ensuring they remain within predefined thresholds.

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

Determines the evaluation method and allowable limits for field value comparisons over time.

| Name               | Description                                                        |
|--------------------|--------------------------------------------------------------------|
| <div class="text-primary">Comparison</div> | Specifies the type of comparison: Absolute Change, Absolute Value, or Percentage Change. |
| <div class="text-primary">Min Value</div> | Indicates the minimum allowable increase in value. Use a negative value to represent an allowable decrease. |
| <div class="text-primary">Max Value</div> | Indicates the maximum allowable increase in value. |

!!! note "Details"
    ### Comparison Options

    **Absolute Change**

    The `Absolute Change` comparison works by comparing the change in a numeric field's value to a pre-set limit (Min / Max). If the field's value changes by more than this specified limit since the last relevant scan, an anomaly is identified.

    ??? example "Illustration"
        _Any record with a value change smaller than 30 or greater than 70 compared to the last scan should be flagged as anomalous_
        
        **Thresholds**: Min Change = 30, Max Change = 70

        | Scan | Previous Value | Current Value | Absolute Change | Anomaly Detected |
        |------|----------------|---------------|-----------------|------------------|
        | #1    | -              | 100           | -               | No               |
        | #2    | 100            | 150           | 50              | No               |
        | #3    | 150            | 220           | 70              | No               |
        | #4    | 220            | <div class="text-negative">300</div> | <div class="text-negative">80</div>  | <div class="text-negative">Yes</div> |

    **Absolute Value**

    The `Absolute Value` comparison works by comparing the change in a numeric field's value to a pre-set limit `between` Min and Max values. If the field's value changes by more than this specified range since the last relevant scan, an anomaly is identified.

    ??? example "Illustration"
        _The value of the record in each scan should be within 100 and 300 to be considered normal_

        **Thresholds**: Min Value = 100, Max Value = 300

        | Scan | Current Value | Anomaly Detected |
        |------|---------------|------------------|
        | #1    | 150           | No              |
        | #2    | <div class="text-negative">90</div> | <div class="text-negative">Yes</div> |
        | #3    | 250           | No               |
        | #4    | <div class="text-negative">310</div> | <div class="text-negative">Yes</div> |

    **Percentage Change**

    The `Percentage Change` comparison operates by tracking changes in a numeric field's value relative to its previous value. If the change exceeds the predefined percentage (%) limit since the last relevant scan, an anomaly is generated.

    ??? example "Illustration"
        _An anomaly is identified if the record's value decreases by more than 20% or increases by more than 50% compared to the last scan._

        **Thresholds**: Min Percentage Change = -20%, Max Percentage Change = 50%

        **Percentage Change Formula**: ( (current_value - previous_value) / previous_value ) * 100

        | Scan | Previous Value | Current Value | Percentage Change           | Anomaly Detected |
        |------|----------------|---------------|-----------------------------|------------------|
        | 1    | -              | 100           | -                           | No               |
        | 2    | 100            | 150           | 50%                         | No               |
        | 3    | 150            | 120           | -20%                        | No               |
        | 4    | 120            | 65            | <div class="text-negative">-45.83%</div> | <div class="text-negative">Yes</div> |
        | 5    | 65             | 110           | <div class="text-negative">69.23%</div>  | <div class="text-negative">Yes</div>  |

    ### Thresholds

    At least the Min or Max value must be specified, and including both is optional. These values determine the acceptable range or limit of change in the field's value.

    **Min Value**

    - Represents the minimum allowable increase in the field's value.
    - A negative Min Value signifies an allowable decrease, determining the minimum value the field can drop to be considered valid.

    **Max Value**

    - Indicates the maximum allowable increase in the field’s value, setting an upper limit for the value's acceptable growth or change.
        
### Anomaly Types

{%
    include-markdown "components/anomaly-support/index.md"
    start='<!-- record-only--start -->'
    end='<!-- record-only--end -->'
%}

### Example

**Objective**: *Ensure that the total price in the ORDERS table does not fluctuate beyond a predefined percentage limit between scans.*

**Thresholds**: Min Percentage Change = -30%, Max Percentage Change = 30%

**Sample Scan History**

| Scan | O_ORDERKEY | Previous O_TOTALPRICE | Current O_TOTALPRICE | Percentage Change | Anomaly Detected |
|------|------------|-----------------------|----------------------|-------------------|------------------|
| #1    | 1          | -                     | 100                  | -                 | No               |
| #2    | 1          | 100                   | 110                  | 10%               | No               |
| #3    | 1          | 110                   | <span class="text-negative">200</span> | <span class="text-negative">81.8%</span> | <span class="text-negative">Yes</span> |
| #4    | 1          | 200                   | <span class="text-negative">105</span> | <span class="text-negative">-47.5%</span> | <span class="text-negative">Yes</span> |

**Anomaly Explanation**

In the sample scan history above, anomalies are identified in scans #3 and #4. The `O_TOTALPRICE` values in these scans fall outside the declared percentage change limits of -30% and 30%, indicating that something unusual might be happening and further investigation is needed.

=== "Flowchart"
    ```mermaid
    graph TD
    A[Start] --> B[Retrieve O_TOTALPRICE]
    B --> C{Is Percentage Change in O_TOTALPRICE within -30% and 30%?}
    C -->|Yes| D[End]
    C -->|No| E[Mark as Anomalous]
    E --> D
    ```

=== "SQL"
    ```sql
    -- An illustrative SQL query demonstrating the rule applied to example dataset(s)
    select 
        o_orderkey,
        o_totalprice,
        lag(o_totalprice) over (order by o_orderkey) as previous_o_totalprice
    from
        orders
    having
        abs((o_totalprice - previous_o_totalprice) / previous_o_totalprice) * 100 > 30
        or
        abs((o_totalprice - previous_o_totalprice) / previous_o_totalprice) * 100 < -30;
    ```

**Potential Violation Messages**

!!! example "Record Anomaly (Percentage Change)"
    The percentage change of `O_TOTALPRICE` from '110' to '200' falls outside the declared limits

!!! example "Record Anomaly (Absolute Change)"
    _using hypothetical numbers_

    The absolute change of `O_TOTALPRICE` from '150' to '300' falls outside the declared limits

!!! example "Record Anomaly (Absolute Value)"
    _using hypothetical numbers_

    The value for `O_TOTALPRICE` of '50' is not between the declared limits

