# Not Null <spam id='multiple-fields'>`multiple fields`</spam>

---

*Asserts that the field's value is not explicitly set to nothing.*

| Accepted Field Types   |                      |
| :--------------------: | :------------------: |
| `Date`                 | :octicons-check-16:   |
| `Timestamp`            | :octicons-check-16:   |
| `Integral`             | :octicons-check-16:   |
| `Fractional`           | :octicons-check-16:   |
| `String`               | :octicons-check-16:   |
| `Boolean`              | :octicons-check-16:   |

![Screenshot](../assets/checks/rule-types/not-null-check-light.png#only-light)
![Screenshot](../assets/checks/rule-types/not-null-check-dark.png#only-dark)

!!! example
    `price` and `id` are a non-negative number.

=== "![Screenshot](../assets/checks/rule-types/icons/icon-record-anomaly-dark.svg)`Record Anomaly` error message"

    The is not assigned value for `[field_name]`.

=== "![Screenshot](../assets/checks/rule-types/icons/icon-shape-anomaly-dark.svg)`Shape Anomaly` error message"
    In `[field_names]`, `[x]`% are not assigned values.

