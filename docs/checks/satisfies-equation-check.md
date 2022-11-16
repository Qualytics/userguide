### Satisfies Equation <spam id='multiple-fields'>`multiple fields`</spam>

---

*Evaluates the given equation (any valid Spark SQL) for each record.*

| Accepted Field Types   |                      |
| :--------------------: | :------------------: |
| `Date`                 | :white_check_mark:   |
| `Timestamp`            | :white_check_mark:   |
| `Integral`             | :white_check_mark:   |
| `Fractional`           | :white_check_mark:   |
| `String`               | :white_check_mark:   |
| `Boolean`              | :white_check_mark:   |

![Screenshot](../assets/checks/rule-types/satisfies-equation-check.png){: style="height:450px"}

!!! example
    The record satisfies the give equation.
    
=== "![Screenshot](../assets/checks/rule-types/icons/icon-record-anomaly-dark.svg)`Record Anomaly` error message"
    The record does not satisfy the give equation.

=== "![Screenshot](../assets/checks/rule-types/icons/icon-shape-anomaly-dark.svg)`Shape Anomaly` error message"
    `[x]`% of records do not satisfy the give query equation.

---