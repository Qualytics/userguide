# Less Than <spam id='single-field'>`single field`</spam>

---

*Asserts that the field is a number less than (or equal to) a value.*

| Accepted Field Types   |                      |
| :--------------------: | :------------------: |
| `Integral`             | :octicons-check-16:   |
| `Fractional`           | :octicons-check-16:   |

![Screenshot](../assets/checks/rule-types/less-than-check-light.png#only-light)
![Screenshot](../assets/checks/rule-types/less-than-check-dark.png#only-dark)

!!! example
    `discount` is less then `25`.

=== "![Screenshot](../assets/checks/rule-types/icons/icon-record-anomaly-dark.svg)`Record Anomaly` error message"

    The `[field_name]` value of '`[x value]`' is not less than `[value]`.

=== "![Screenshot](../assets/checks/rule-types/icons/icon-shape-anomaly-dark.svg)`Shape Anomaly` error message"
    In `[field_names]`, `[x]`% are not less than `[value]`.

---