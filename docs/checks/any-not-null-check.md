# Any Not Null <spam id='multiple-fields'>`multiple fields`</spam>

--- 

*Asserts that one of the fields must not be null*

| Accepted Field Types   |                          |
| :--------------------: |   :------------------:   |
| `Date`                 |   :octicons-check-16:     |
| `Timestamp`            |   :octicons-check-16:     |
| `Integral`             |   :octicons-check-16:     |
| `Fractional`           |   :octicons-check-16:     |
| `String`               |   :octicons-check-16:     |
| `Boolean`              |   :octicons-check-16:     |

![Screenshot](../assets/checks/rule-types/any-not-null-check-light.png#only-light)
![Screenshot](../assets/checks/rule-types/any-not-null-check-dark.png#only-dark)

!!! example
    At least one of the fields `order_time` is not null.

=== "![Screenshot](../assets/checks/rule-types/icons/icon-record-anomaly-dark.svg)`Record Anomaly` error message"
    There is no value set for any of '`[field_name]`'

=== "![Screenshot](../assets/checks/rule-types/icons/icon-shape-anomaly-dark.svg)`Shape Anomaly` error message"
    In `[field_names]`, `[x]`% have no value set for any of `[selected_field_name]`
