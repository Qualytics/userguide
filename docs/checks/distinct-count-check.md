# Distinct Count <spam id='single-field'>`single field`</spam>

---

*Asserts on the approximate count distinct of the given column.*

| Accepted Field Types   |                      |
| :--------------------: | :------------------: |
| `Date`                 | :white_check_mark:   |
| `Timestamp`            | :white_check_mark:   |
| `Integral`             | :white_check_mark:   |
| `Fractional`           | :white_check_mark:   |
| `String`               | :white_check_mark:   |
| `Boolean`              | :white_check_mark:   |

![Screenshot](../assets/checks/rule-types/distinct-count-check.png){: style="height:450px"}

!!! example
    The distinct count of `Record_Id` is `0.0`.

=== "![Screenshot](../assets/checks/rule-types/icons/icon-shape-anomaly-dark.svg)`Shape Anomaly only` error message"
    In `[field_names]`, The distinct count of the records is not `0.0`.

---