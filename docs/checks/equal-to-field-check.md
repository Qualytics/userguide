# Equal To Field <spam id='single-field'>`single field`</spam>

---

*Asserts that this field is equal to another field.*

| Accepted Field Types   |                      |
| :--------------------: | :------------------: |
| `Date`                 | :octicons-check-16:   |
| `Timestamp`            | :octicons-check-16:   |
| `Integral`             | :octicons-check-16:   |
| `Fractional`           | :octicons-check-16:   |


![Screenshot](../assets/checks/rule-types/equal-to-field-check-light.png#only-light)
![Screenshot](../assets/checks/rule-types/equal-to-field-check-dark.png#only-dark)

!!! example
    `Record_Id` has the same values as `Id`.

=== "![Screenshot](../assets/checks/rule-types/icons/icon-record-anomaly-dark.svg)`Record Anomaly` error message"

    The `[field_name]` value of '`[x value]`' is not equal to the value of `[compared_field_name]`.

=== "![Screenshot](../assets/checks/rule-types/icons/icon-shape-anomaly-dark.svg)`Shape Anomaly` error message"
    In `[field_names]`, `[x]`% of the field are not equal.

