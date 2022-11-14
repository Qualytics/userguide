# Before Date Time <spam id='single-field'>`single field`</spam>

---

*Asserts that the field is a timestamp earlier than a specific date and time.*

![Screenshot](../assets/checks/rule-types/before-date-time-check.png){: style="height:450px"}

!!! example
    `order_time` is earlier than `2021-01-01`

=== "![Screenshot](../assets/checks/rule-types/icons/icon-record-anomaly-dark.svg)`Record Anomaly` error message"

    The `[field_name]` value of '`[x date time]`' is not earlier than `[selected_date_time]`

=== "![Screenshot](../assets/checks/rule-types/icons/icon-shape-anomaly-dark.svg)`Shape Anomaly` error message"
    In `[field_names]`, `[x]`% are not earlier than `[selected_field_name]`

---