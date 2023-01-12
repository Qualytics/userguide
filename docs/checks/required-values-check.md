# Required Values <spam id='single-field'>`single field`</spam>

---

*Asserts that all of the defined values must be present at least once within a field.*

| Accepted Field Types   |                      |
| :--------------------: | :------------------: |
| `Date`                 | :octicons-check-16:   |
| `Timestamp`            | :octicons-check-16:   |
| `Integral`             | :octicons-check-16:   |
| `Fractional`           | :octicons-check-16:   |
| `String`               | :octicons-check-16:   |
| `Boolean`              | :octicons-check-16:   |

![Screenshot](../assets/checks/rule-types/required-values-check-light.png#only-light)
![Screenshot](../assets/checks/rule-types/required-values-check-dark.png#only-dark)

!!! example
    `Ship Date` is assigned all of the listed values at least once `[2022-10-15, 2022-11-12, 2022-12-12]`.

=== "![Screenshot](../assets/checks/rule-types/icons/icon-shape-anomaly-dark.svg)`Shape Anomaly` error message"
    In `[field_names]`, required values are missing in the sample of `[x]` records.

---