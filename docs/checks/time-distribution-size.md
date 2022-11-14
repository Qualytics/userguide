### Time Distribution Size
* *Asserts that the count of records for each interval of a timestamp is between two numbers.*

![Screenshot](../assets/checks/rule-types/time-distribution-size-check.png){: style="height:450px"}

!!! example
    The count of records in `[interval]` segments of `[field_name]` is between `[min_size]` and `[max_size]`.
    
=== "![Screenshot](../assets/checks/rule-types/icons/icon-shape-anomaly-dark.svg)`Shape Anomaly` error message"
    The count of records in `[interval]` segments of `[field_names]` is not between `[min_size]` and `[max_size]`.

---