# Between <spam id='single-field'>`single field`</spam>

---

*Asserts that values are equal to or between two numbers.*

| Accepted Field Types   |                      |
| :--------------------: | :------------------: |
| `Integral`             | :octicons-check-16:   |
| `Fractional`           | :octicons-check-16:   |

![Screenshot](../assets/checks/rule-types/between-check-light.png#only-light)
![Screenshot](../assets/checks/rule-types/between-check-dark.png#only-dark)

!!! example
    `price` is between `200` and `865`

=== "![Screenshot](../assets/checks/rule-types/icons/icon-record-anomaly-dark.svg)`Record Anomaly` error message"

    The value for `[field_name]` of '`[x value]`' is not between `[min_value]` and `[max_value]`.

=== "![Screenshot](../assets/checks/rule-types/icons/icon-shape-anomaly-dark.svg)`Shape Anomaly` error message"
    In `[field_names]`, `[x]`% are not not between `[min_value]` and `[max_value]`.
---