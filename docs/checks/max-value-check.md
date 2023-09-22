# Max Value <spam id='single-field'>`single field`</spam>

---

*Asserts that a field has a maximum value.*

| Accepted Field Types   |                      |
| :--------------------: | :------------------: |
| `Integral`             | :octicons-check-16:   |
| `Fractional`           | :octicons-check-16:   |

![Screenshot](../assets/checks/rule-types/max-value-check-light.png#only-light)
![Screenshot](../assets/checks/rule-types/max-value-check-dark.png#only-dark)
!!! example
    `Period` has a maximum value of `900`.

=== "![Screenshot](../assets/checks/rule-types/icons/icon-record-anomaly-dark.svg)`Record Anomaly` error message"

    The `[field_name]` value of '`[x value]`' is greater than the max value of `[value]`

=== "![Screenshot](../assets/checks/rule-types/icons/icon-shape-anomaly-dark.svg)`Shape Anomaly` error message"
    In `[field_names]`, `[x]`% are greater than the max value of `[value]`.

