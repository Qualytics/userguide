# Min Value <spam id='single-field'>`single field`</spam>

---

*Asserts that a field has a minimum value.*

| Accepted Field Types   |                      |
| :--------------------: | :------------------: |
| `Integral`             | :white_check_mark:   |
| `Fractional`           | :white_check_mark:   |

![Screenshot](../assets/checks/rule-types/min-value-check.png){: style="height:450px"}

!!! example
    `discount` has a minimum value of `0`.

=== "![Screenshot](../assets/checks/rule-types/icons/icon-record-anomaly-dark.svg)`Record Anomaly` error message"

    The `[field_name]` value of '`[x value]`' is less than the min value of `[value]`

=== "![Screenshot](../assets/checks/rule-types/icons/icon-shape-anomaly-dark.svg)`Shape Anomaly` error message"
    In `[field_names]`, `[x]`% are less than the min value of `[value]`.

---