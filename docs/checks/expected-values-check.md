# Expected Values <spam id='single-field'>`single field`</spam>

---

*Asserts that values are contained within a list of expected values.*

| Accepted Field Types   |                      |
| :--------------------: | :------------------: |
| `Date`                 | :octicons-check-16:   |
| `Timestamp`            | :octicons-check-16:   |
| `Integral`             | :octicons-check-16:   |
| `Fractional`           | :octicons-check-16:   |
| `String`               | :octicons-check-16:   |
| `Boolean`              | :octicons-check-16:   |

![Screenshot](../assets/checks/rule-types/expected-values-check-light.png#only-light)
![Screenshot](../assets/checks/rule-types/expected-values-check-dark.png#only-dark)


!!! example
    `discount` is one of the expected values `[5, 10, 15]`

=== "![Screenshot](../assets/checks/rule-types/icons/icon-record-anomaly-dark.svg)`Record Anomaly` error message"

    The `[field_name]` value of '`[x value]`' does not appear in the list of expected values.

=== "![Screenshot](../assets/checks/rule-types/icons/icon-shape-anomaly-dark.svg)`Shape Anomaly` error message"
    In `[field_names]`, `[x]`% of values do not appear in the list of expected values.

---