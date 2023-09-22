# Is Credit Card <spam id='single-field'>`single field`</spam>

---

*Asserts that the values are credit card numbers.*

| Accepted Field Types   |                      |
| :--------------------: | :------------------: |
| `Date`                 | :octicons-check-16:   |
| `Timestamp`            | :octicons-check-16:   |
| `Integral`             | :octicons-check-16:   |
| `Fractional`           | :octicons-check-16:   |
| `String`               | :octicons-check-16:   |
| `Boolean`              | :octicons-check-16:   |

![Screenshot](../assets/checks/rule-types/is-credit-card-check-light.png#only-light)
![Screenshot](../assets/checks/rule-types/is-credit-card-check-dark.png#only-dark)


!!! example
    `payment_type` is formatted as a credit card number.

=== "![Screenshot](../assets/checks/rule-types/icons/icon-record-anomaly-dark.svg)`Record Anomaly` error message"

    The `[field_name]` value of '`[x value]`' does not adhere to a credit card format.

=== "![Screenshot](../assets/checks/rule-types/icons/icon-shape-anomaly-dark.svg)`Shape Anomaly` error message"
    In `[field_names]`, `[x]`% do not adhere to a credit card format.

