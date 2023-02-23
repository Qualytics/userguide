# Exists In

---

*Asserts if the rows of a compared table/field of a specific Datastore exists in the selected table/field.*

| Accepted Field Types   |                      |
| :--------------------: | :------------------: |
| `Date`                 | :octicons-check-16:   |
| `Timestamp`            | :octicons-check-16:   |
| `Integral`             | :octicons-check-16:   |
| `Fractional`           | :octicons-check-16:   |
| `String`               | :octicons-check-16:   |
| `Boolean`              | :octicons-check-16:   |


![Screenshot](../assets/checks/rule-types/exists-in-light.png#only-light)
![Screenshot](../assets/checks/rule-types/exists-in-dark.png#only-dark)

!!! example
    `Account_fk` exists in `Account_id`.

    You can select the same or a different datastore to assert that the compared table/file exists in the source table/file.

=== "![Screenshot](../assets/checks/rule-types/icons/icon-record-anomaly-dark.svg)`Record Anomaly` error message"

    The `[field_name]` value of '`[x value]`' is not equal to the value of `[compared_field_name]`.

=== "![Screenshot](../assets/checks/rule-types/icons/icon-shape-anomaly-dark.svg)`Shape Anomaly` error message"
    In `[field_names]`, `[x]`% of the fiels are not equal.

---