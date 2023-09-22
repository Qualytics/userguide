# Not Exists In <spam id='single-field'>`single field`</spam>
---

The `NotExistIn` rule type serves to validate data integrity by ensuring that values assigned to a specific field in a table do not exist as values in another field. This type of rule is useful in scenarios where you want to enforce uniqueness or exclusion constraints between two tables.

---

*Asserts that values assigned to this field do not exist as values in another field.*

| Accepted Field Types   |                      |
| :--------------------: | :------------------: |
| `Date`                 | :octicons-check-16:   |
| `Timestamp`            | :octicons-check-16:   |
| `Integral`             | :octicons-check-16:   |
| `Fractional`           | :octicons-check-16:   |
| `String`               | :octicons-check-16:   |
| `Boolean`              | :octicons-check-16:   |


![Screenshot](../assets/checks/rule-types/not-exists-in-light.png#only-light)
![Screenshot](../assets/checks/rule-types/not-exists-in-dark.png#only-dark)

!!! example
    `Account_fk` not exists in `Account_id`.

    You can select the same or a different datastore to assert that the compared table/file not exists in the source table/file.

=== "![Screenshot](../assets/checks/rule-types/icons/icon-record-anomaly-dark.svg)`Record Anomaly` error message"
    The `[field_name]` value of '`[x value]`' does exist in `[compared_field_name]`.

=== "![Screenshot](../assets/checks/rule-types/icons/icon-shape-anomaly-dark.svg)`Shape Anomaly` error message"
    In `[field_names]`, `[x]`% of the filtered values do exist in `[compared_field_name]`.

