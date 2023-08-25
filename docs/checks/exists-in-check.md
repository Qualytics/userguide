# Exists In <spam id='single-field'>`single field`</spam>

---

The `ExistsIn` rule type ensures that your fact table's values are valid where the valid values are maintained in a dimension table elsewhere (including in an entirely separate datastore). 
Within the same OLTP this scenario would typically be enforced with a foreign key, but there are many scenarios where foreign key integrity constraints are unavailable such as:
- the source (e.g. fact table) and reference (e.g. dimension table) are held in different databases or mediums
- the datastore technology does not enforce foreign key integrity constraints
  
`ExistsIn` enables you to verify that all corresponding records in your source hold valid values, even in extreme examples such as source data in a spreadsheet in object storage. 

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

