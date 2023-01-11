# Distinct Count <spam id='single-field'>`single field`</spam>

---

*Asserts on the approximate count distinct of the given column.*

| Accepted Field Types   |                      |
| :--------------------: | :------------------: |
| `Date`                 | :octicons-check-16:   |
| `Timestamp`            | :octicons-check-16:   |
| `Integral`             | :octicons-check-16:   |
| `Fractional`           | :octicons-check-16:   |
| `String`               | :octicons-check-16:   |
| `Boolean`              | :octicons-check-16:   |

![Screenshot](../assets/checks/rule-types/distinct-count-check-light.png#only-light)
![Screenshot](../assets/checks/rule-types/distinct-count-check-dark.png#only-dark)

!!! example
    The distinct count of `Record_Id` is `0.0`.

=== "![Screenshot](../assets/checks/rule-types/icons/icon-shape-anomaly-dark.svg)`Shape Anomaly only` error message"
    In `[field_names]`, The distinct count of the records is not `0.0`.

---
