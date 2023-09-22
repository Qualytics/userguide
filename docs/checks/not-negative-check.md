# Not Negative <spam id='single-field'>`single field`</spam>

---

*Asserts that this is a non-negative number.*

| Accepted Field Types   |                      |
| :--------------------: | :------------------: |
| `Date`                 | :octicons-check-16:   |
| `Timestamp`            | :octicons-check-16:   |
| `Integral`             | :octicons-check-16:   |
| `Fractional`           | :octicons-check-16:   |
| `String`               | :octicons-check-16:   |
| `Boolean`              | :octicons-check-16:   |

![Screenshot](../assets/checks/rule-types/not-negative-check-light.png#only-light)
![Screenshot](../assets/checks/rule-types/not-negative-check-dark.png#only-dark)

!!! example
    `price`is a non-negative number.

=== "![Screenshot](../assets/checks/rule-types/icons/icon-record-anomaly-dark.svg)`Record Anomaly` error message"

    The value for `[field_name]` of '`[x value]`' is a negative number.

=== "![Screenshot](../assets/checks/rule-types/icons/icon-shape-anomaly-dark.svg)`Shape Anomaly` error message"
    In `[field_names]`, `[x]`% are negative numbers.

