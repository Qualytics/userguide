# User Define Function <spam id='single-field'>`single field`</spam>

---

*Asserts that the given user-defined function (as scala script) evaluates to true over the field's value"*.

| Accepted Field Types   |                      |
| :--------------------: | :------------------: |
| `String`               | :octicons-check-16:   |

![Screenshot](../assets/checks/rule-types/user-defined-function-check-light.png#only-light)
![Screenshot](../assets/checks/rule-types/user-defined-function-check-dark.png#only-dark)

!!! example
    The given UDF evaluates to true over `status`. If the `length` is greater than `2`.

=== "![Screenshot](../assets/checks/rule-types/icons/icon-shape-anomaly-dark.svg)`Shape Anomaly` error message"
    In `[field_names]`, `[x]`% of values to not evaluate true as a parameter to the given UDF.

---