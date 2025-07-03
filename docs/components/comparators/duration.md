#### Duration

Duration comparators support time-based comparisons, allowing for flexibility in how duration differences are managed. This flexibility is crucial for datasets where time measurements are essential but can vary slightly.

##### Unit

The unit of time you select determines how granular the comparison is:

- **Millis**: Measures time in milliseconds, ideal for high-precision needs.
- **Seconds**: Suitable for most general purposes where precision is important but doesn't need to be to the millisecond.
- **Days**: Best for longer durations.

##### Value

Value sets the maximum acceptable difference in time to consider two values as equal. It serves to define the margin of error, accommodating small discrepancies that naturally occur over time.

??? example "Illustration using Duration Comparator"

    | Unit      | Value A | Value B | Difference | Threshold | Are equal? |
    |-----------|--------------------|------------------|------------|-------------------------------|------------------|
    | Millis    | 500 ms             | 520 ms           | 20 ms      | 25 ms                         | True               |
    | Seconds   | 30 sec             | 31 sec           | 1 sec      | 2 sec                         | True               |
    | Days      | 5 days             | 7 days | 2 days   | 1 day                      | <div class="text-negative">False</div>               |
    | Millis    | 1000 ms            | 1040 ms          | 40 ms      | 25 ms                         | <div class="text-negative">False</div> |
    | Seconds   | 45 sec             | 48 sec           | 3 sec      | 2 sec                         | <div class="text-negative">False</div> |


