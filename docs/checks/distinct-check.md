# Distinct <spam id='single-field'>`single field`</spam>

---

*The ratio of the count of distinct values (e.g. [a, a, b] is 2/3).*

| Accepted Field Types   |                      |
| :--------------------: | :------------------: |
| `Date`                 | :white_check_mark:   |
| `Timestamp`            | :white_check_mark:   |
| `Integral`             | :white_check_mark:   |
| `Fractional`           | :white_check_mark:   |
| `String`               | :white_check_mark:   |
| `Boolean`              | :white_check_mark:   |

![Screenshot](../assets/checks/rule-types/distinct-check.png){: style="height:450px"}

!!! example
    `Payment_Publication_Name` has a distinct ratio of `[value]`

=== "![Screenshot](../assets/checks/rule-types/icons/icon-shape-anomaly-dark.svg)`Shape Anomaly only` error message"
    In `[field_names]`, The distinct ratio of the `[field]` records is not `0.0`

---