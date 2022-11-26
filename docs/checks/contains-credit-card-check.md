# Contains Credit Card <spam id='single-field'>`single field`</spam>

---

*Asserts that the values are credit card numbers.*

| Accepted Field Types   |                      |
| :--------------------: | :------------------: |
| `Date`                 | :white_check_mark:   |
| `Timestamp`            | :white_check_mark:   |
| `Integral`             | :white_check_mark:   |
| `Fractional`           | :white_check_mark:   |
| `String`               | :white_check_mark:   |
| `Boolean`              | :white_check_mark:   |

![Screenshot](../assets/checks/rule-types/contains-credit-card-check.png){: style="height:450px"}                                                  

!!! example
    `Form_of_Payment_or_Transfer_of_Value` contains a credit card number.

=== "![Screenshot](../assets/checks/rule-types/icons/icon-record-anomaly-dark.svg)`Record Anomaly` error message"

    The `[field_name]`value of '`[x value]`' does not contain a credit card number.

=== "![Screenshot](../assets/checks/rule-types/icons/icon-shape-anomaly-dark.svg)`Shape Anomaly` error message"
    In `[field_names]`, `[x]`% do not contain credit card numbers.

--- 