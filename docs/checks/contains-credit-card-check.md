# Contains Credit Card <spam id='single-field'>`single field`</spam>

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

![Screenshot](../assets/checks/rule-types/contains-credit-card-check-light.png#only-light)
![Screenshot](../assets/checks/rule-types/contains-credit-card-check-dark.png#only-dark)

!!! example
    `Form_of_Payment_or_Transfer_of_Value` contains a credit card number.

=== "![Screenshot](../assets/checks/rule-types/icons/icon-record-anomaly-dark.svg)`Record Anomaly` error message"

    The `[field_name]`value of '`[x value]`' does not contain a credit card number.

=== "![Screenshot](../assets/checks/rule-types/icons/icon-shape-anomaly-dark.svg)`Shape Anomaly` error message"
    In `[field_names]`, `[x]`% do not contain credit card numbers.

--- 