# Greater Than Field <spam id='single-field'>`single field`</spam>

---

*Asserts that this field is greater than another field.*

| Accepted Field Types   |                      |
| :--------------------: | :------------------: |
| `Date`                 | :octicons-check-16:   |
| `Timestamp`            | :octicons-check-16:   |
| `Integral`             | :octicons-check-16:   |
| `Fractional`           | :octicons-check-16:   |

![Screenshot](../assets/checks/rule-types/greater-than-field-check-light.png#only-light)
![Screenshot](../assets/checks/rule-types/greater-than-field-check-dark.png#only-dark)
!!! example
    `price` has a value greater than `discount`.

=== "![Screenshot](../assets/checks/rule-types/icons/icon-record-anomaly-dark.svg)`Record Anomaly` error message"

    The `[field_name]` value of '`[x value]`' is not greater than the value of `[value]`.

=== "![Screenshot](../assets/checks/rule-types/icons/icon-shape-anomaly-dark.svg)`Shape Anomaly` error message"
    In `[field_names]`, `[x]`% are not equal to `[compared_field_name]`.

---