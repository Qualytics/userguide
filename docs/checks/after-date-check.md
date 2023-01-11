# After Date Time <spam id='single-field'>`single field`</spam>

---
*Asserts that the field is a timestamp later than a specific date and time.*

| Accepted Field Types   |                      |
| :--------------------: | :------------------: |
| `Date`                 | :octicons-check-16:   |
| `Timestamp`            | :octicons-check-16:   |


![Screenshot](../assets/checks/rule-types/after-date-time-check-light.png#only-light)
![Screenshot](../assets/checks/rule-types/after-date-time-check-dark.png#only-dark)

!!! example
    `order_time` is later than `2021-01-01`

=== "![Screenshot](../assets/checks/rule-types/icons/icon-record-anomaly-dark.svg)`Record Anomaly` error message"
    The `[field_name]` value of '`[x date time]`' is not later than `[selected_date_time]`

=== "![Screenshot](../assets/checks/rule-types/icons/icon-shape-anomaly-dark.svg)`Shape Anomaly` error message"
    In `[field_names]`, `[x]`% are not later than `[selected_date_time]`

--- 