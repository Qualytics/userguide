---
search:
  exclude: true
---

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
    
    In this example, it compares `Value A` and `Value B` according to the defined **Threshold** of **50**.

    | Value A | Value B | Difference | Are equal? |
    |---------|---------|------------|------------------|
    | 100     | 150     | 50         | True               |
    | 100     | 90      | 10         | True              |
    | 100     | 155     | 55         | <div class="text-negative">False</div> |
    | 100     | 49      | 51         | <div class="text-negative">False</div> |


??? example "Illustration using Percentage Value"

    In this example, it compares `Value A` and `Value B` according to the defined **Threshold** of **10%**.

    **Percentage Change Formula**: [ (`Value B` - `Value A`) / `Value A` ] * 100

    | Value A | Value B | Percentage Change | Are equal? |
    |-----------------|---------------|--------------------|------------------|
    | 120             | 132           | 10%                | True               |
    | 150             | 135           | 10%                | True               |
    | 200             | 180           | 10%                | True               |
    | 160             | 150           | 6.25%              | True               |
    | 180             | 200           | 11.11%             | <div class="text-negative">False</div> |
