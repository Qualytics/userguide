#### Numeric

Numeric comparators enable you to compare numbers with a specified margin, which can be a fixed absolute value or a percentage. This allows for minor numerical differences that are often acceptable in real-world data.

##### Comparison Type

- **Absolute Value**: Uses a fixed threshold for determining equality. It's ideal when you need consistent precision across measurements.
- **Percentage Value**: Uses a percentage of the original value as the threshold for equality comparisons. It's suitable for floating point numbers where precision varies.

##### Threshold

The threshold is the value you set to define the margin of error:

- When using **Absolute Value**, the threshold represents the maximum allowable difference between two values for them to be considered equal.
- For **Percentage Value**, the threshold is the percentage that describes how much a value can deviate from a reference value and still be considered equal.

??? example "Illustration using Absolute Value"
    _TBD_

    **Thresholds**: Min Value = 100, Max Value = 300

    | Scan | Current Value | Anomaly Detected |
    |------|---------------|------------------|
    | #1    | 150           | No              |
    | #2    | <div class="text-negative">90</div> | <div class="text-negative">Yes</div> |
    | #3    | 250           | No               |
    | #4    | <div class="text-negative">310</div> | <div class="text-negative">Yes</div> |

??? example "Illustration using Percentage Value"
    _TBD_

    **Thresholds**: Min Percentage Change = -20%, Max Percentage Change = 50%

    **Percentage Change Formula**: ( (current_value - previous_value) / previous_value ) * 100

    | Scan | Previous Value | Current Value | Percentage Change           | Anomaly Detected |
    |------|----------------|---------------|-----------------------------|------------------|
    | 1    | -              | 100           | -                           | No               |
    | 2    | 100            | 150           | 50%                         | No               |
    | 3    | 150            | 120           | -20%                        | No               |
    | 4    | 120            | 65            | <div class="text-negative">-45.83%</div> | <div class="text-negative">Yes</div> |
    | 5    | 65             | 110           | <div class="text-negative">69.23%</div>  | <div class="text-negative">Yes</div>  |
