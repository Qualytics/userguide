# Distinct <spam id='single-field'>`single field`</spam>

---

*The ratio of the count of distinct values (e.g. [a, a, b] is 2/3).*

| Accepted Field Types   |                      |
| :--------------------: | :------------------: |
| `Date`                 | :octicons-check-16:   |
| `Timestamp`            | :octicons-check-16:   |
| `Integral`             | :octicons-check-16:   |
| `Fractional`           | :octicons-check-16:   |
| `String`               | :octicons-check-16:   |
| `Boolean`              | :octicons-check-16:   |

![Screenshot](../assets/checks/rule-types/distinct-check-light.png#only-light)
![Screenshot](../assets/checks/rule-types/distinct-check-dark.png#only-dark)

!!! example
    `Payment_Publication_Name` has a distinct ratio of `[value]`

=== "![Screenshot](../assets/checks/rule-types/icons/icon-shape-anomaly-dark.svg)`Shape Anomaly only` error message"
    In `[field_names]`, The distinct ratio of the `[field]` records is not `0.0`

---