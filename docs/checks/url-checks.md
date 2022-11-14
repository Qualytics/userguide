### Url <spam id='single-field'>`single field`</spam>
* *Asserts that the values contain valid URLs.*

                                           record_anomaly_message="The {0.field_names} value of '{1}' does not contain a URL",
                                           shape_anomaly_message="In {0.field_names}, {1:.3f}% do not contain a URL"),

![Screenshot](../assets/checks/rule-types/contains-url.png){: style="height:450px"}

!!! example
    `Sales Channel` contains a URL.
    
=== "![Screenshot](../assets/checks/rule-types/icons/icon-record-anomaly-dark.svg)`Record Anomaly` error message"
    The `[field_name]` value of `['x']` does not contain a URL.

=== "![Screenshot](../assets/checks/rule-types/icons/icon-shape-anomaly-dark.svg)`Shape Anomaly` error message"
    In `[field_names]`, `[x]`% do not contain a URL.

---