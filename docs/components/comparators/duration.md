#### Duration

Duration comparators support time-based comparisons, allowing for flexibility in how duration differences are managed. This flexibility is crucial for datasets where time measurements are essential but can vary slightly.

##### Unit

The unit of time you select determines how granular the comparison is:

- **Millis**: Measures time in milliseconds, ideal for high-precision needs.
- **Seconds**: Suitable for most general purposes where precision is important but doesn't need to be to the millisecond.
- **Days**: Best for longer durations.

##### Value

Value sets the maximum acceptable difference in time to consider two values as equal. It serves to define the margin of error, accommodating small discrepancies that naturally occur over time.

??? example "Illustration"
    _TBD_

    **Thresholds**: Min Value = 100, Max Value = 300

    | Scan | Current Value | Anomaly Detected |
    |------|---------------|------------------|
    | #1    | 150           | No              |
    | #2    | <div class="text-negative">90</div> | <div class="text-negative">Yes</div> |
    | #3    | 250           | No               |
    | #4    | <div class="text-negative">310</div> | <div class="text-negative">Yes</div> |
