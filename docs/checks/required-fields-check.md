# Required Fields <spam id='multiple-fields'>`multiple fields`</spam>

---

*Asserts that all of the selected fields must be present in the datastore.*

| Accepted Field Types   |                      |
| :--------------------: | :------------------: |
| `Date`                 | :octicons-check-16:   |
| `Timestamp`            | :octicons-check-16:   |
| `Integral`             | :octicons-check-16:   |
| `Fractional`           | :octicons-check-16:   |
| `String`               | :octicons-check-16:   |
| `Boolean`              | :octicons-check-16:   |

![Screenshot](../assets/checks/rule-types/required-fields-check-light.png#only-light)
![Screenshot](../assets/checks/rule-types/required-fields-check-dark.png#only-dark)

!!! example 
    `SalesRecord` table has all of the defined fields `[Id, Order ID, Order Date, Total Cost]`

=== "![Screenshot](../assets/checks/rule-types/icons/icon-shape-anomaly-dark.svg)`Shape Anomaly` error message"
    One of the required fields `[field_names]`, are missing.

