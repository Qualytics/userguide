# Required Values <spam id='single-field'>`single field`</spam>

---

*Asserts that all of the defined values must be present at least once within a field.*

| Accepted Field Types   |                      |
| :--------------------: | :------------------: |
| `Date`                 | :white_check_mark:   |
| `Timestamp`            | :white_check_mark:   |
| `Integral`             | :white_check_mark:   |
| `Fractional`           | :white_check_mark:   |
| `String`               | :white_check_mark:   |
| `Boolean`              | :white_check_mark:   |

![Screenshot](../assets/checks/rule-types/required-values-check.png){: style="height:450px"}

!!! example
    `Ship Date` is assigned all of the listed values at least once `[2022-10-15, 2022-11-12, 2022-12-12]`.

=== "![Screenshot](../assets/checks/rule-types/icons/icon-shape-anomaly-dark.svg)`Shape Anomaly` error message"
    In `[field_names]`, required values are missing in the sample of `[x]` records.

---