# Field Count <spam id='single-field'>`single field`</spam>

---

*Asserts that there must be exactly a specified number of fields.*

| Accepted Field Types   |                      |
| :--------------------: | :------------------: |
| `Date`                 | :octicons-check-16:   |
| `Timestamp`            | :octicons-check-16:   |
| `Integral`             | :octicons-check-16:   |
| `Fractional`           | :octicons-check-16:   |
| `String`               | :octicons-check-16:   |
| `Boolean`              | :octicons-check-16:   |

![Screenshot](../assets/checks/rule-types/field-count-check-light.png#only-light)
![Screenshot](../assets/checks/rule-types/field-count-check-dark.png#only-dark)

!!! example
    `orders` has a field count of `10`.

=== "![Screenshot](../assets/checks/rule-types/icons/icon-shape-anomaly-dark.svg)`Shape Anomaly` error message"
    In `[field_names]`, the field count is not `[value]`.

---