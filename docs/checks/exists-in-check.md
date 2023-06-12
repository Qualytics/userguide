# Exists In <spam id='single-field'>`single field`</spam>

---
The `ExistsIn` feature is crucial in situations where you need to confirm that key information from your reference table in the source datastore exists in the corresponding table in your destination datastore. In data migration and replication tasks, this can be extremely valuable to ensure that all important reference data has been successfully transferred.

When working with reference tables, these checks are vital to maintain data integrity and to ensure that foreign key relationships remain consistent. `ExistsIn` enables you to verify that all corresponding records in your tables align correctly, ensuring no orphaned records or missing relationships.

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
    The `[field_name]` value of '`[x value]`' does not exist in `[compared_field_name]`.

=== "![Screenshot](../assets/checks/rule-types/icons/icon-shape-anomaly-dark.svg)`Shape Anomaly` error message"
    In `[field_names]`, `[x]`% of the filtered values do not exist in `[compared_field_name]`.
---