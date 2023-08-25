# Data Type <spam id='single-field'>`single field`</spam>

---

*Asserts that the data is of a specific type.*

| Accepted Field Types   |                      |
| :--------------------: | :------------------: |
| `Date`                 | :octicons-check-16:   |
| `Timestamp`            | :octicons-check-16:   |
| `Integral`             | :octicons-check-16:   |
| `Fractional`           | :octicons-check-16:   |
| `String`               | :octicons-check-16:   |
| `Boolean`              | :octicons-check-16:   |

![Screenshot](../assets/checks/rule-types/data-type-check-light.png#only-light)
![Screenshot](../assets/checks/rule-types/data-type-check-dark.png#only-dark)

!!! example
    `Name_of_associated_Covered_Device` is a valid `String`

* You can list any of the following data types:

![Screenshot](../assets/checks/rule-types/list-all-data-types-check-light.png#only-light)
![Screenshot](../assets/checks/rule-types/list-all-data-types-check-dark.png#only-dark)

=== "![Screenshot](../assets/checks/rule-types/icons/icon-record-anomaly-dark.svg)`Record Anomaly` error message"

    The `[field_name]` value of '`[x value]`' is not a valid `[data type]`.

=== "![Screenshot](../assets/checks/rule-types/icons/icon-shape-anomaly-dark.svg)`Shape Anomaly` error message"
    In `[field_names]`, `[x]`% are not a valid `[data type]`.
