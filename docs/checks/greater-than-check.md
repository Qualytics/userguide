# Greater Than <spam id='single-field'>`single field`</spam>

---

*Asserts that the field is a number greater than (or equal to) a value.*

| Accepted Field Types   |                      |
| :--------------------: | :------------------: |
| `Integral`             | :octicons-check-16:   |
| `Fractional`           | :octicons-check-16:   |

![Screenshot](../assets/checks/rule-types/greater-than-check-light.png#only-light)
![Screenshot](../assets/checks/rule-types/greater-than-check-dark.png#only-dark)

!!! example
    `price` is greater than `150`

=== "![Screenshot](../assets/checks/rule-types/icons/icon-record-anomaly-dark.svg)`Record Anomaly` error message"

    The `[field_name]` value of '`[x value]`' is not greater than `[value]`.

=== "![Screenshot](../assets/checks/rule-types/icons/icon-shape-anomaly-dark.svg)`Shape Anomaly` error message"
    In `[field_names]`, `[x]`% are not greater than`[value]`.
