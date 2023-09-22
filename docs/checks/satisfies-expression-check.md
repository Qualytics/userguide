### Satisfies Expression <spam id='multiple-fields'>`multiple fields`</spam>

---

*Evaluates the given expression (any valid Spark SQL) for each record.*

| Accepted Field Types   |                      |
| :--------------------: | :------------------: |
| `Date`                 | :octicons-check-16:   |
| `Timestamp`            | :octicons-check-16:   |
| `Integral`             | :octicons-check-16:   |
| `Fractional`           | :octicons-check-16:   |
| `String`               | :octicons-check-16:   |
| `Boolean`              | :octicons-check-16:   |

![Screenshot](../assets/checks/rule-types/satisfies-expression-check-light.png#only-light)
![Screenshot](../assets/checks/rule-types/satisfies-expression-check-dark.png#only-dark)

!!! example
    The record satisfies the give expression.
    
=== "![Screenshot](../assets/checks/rule-types/icons/icon-record-anomaly-dark.svg)`Record Anomaly` error message"
    The record does not satisfy the give expression.

=== "![Screenshot](../assets/checks/rule-types/icons/icon-shape-anomaly-dark.svg)`Shape Anomaly` error message"
    `[x]`% of records do not satisfy the give query expression.

