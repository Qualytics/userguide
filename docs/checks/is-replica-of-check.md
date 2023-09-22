# Is Replica Of <spam id='multiple-fields'>`multiple fields`</spam>
---

The `IsReplicaOf` feature asserts if a complete table or column in your source datastore is accurately replicated in your destination datastore. This ensures that not only the data, but also the structure and relationships of your original tables or columns, are preserved during the replication process.

By using the `IsReplicaOf` feature, you're taking a significant step in maintaining data integrity across your datasets. This tool ensures that the replication process is comprehensive and accurate, leaving no room for missing data or structural anomalies.

---

*Asserts that the dataset created by the targeted field(s) is replicated by the referred field(s).*

| Accepted Field Types   |                      |
| :--------------------: | :------------------: |
| `Date`                 | :octicons-check-16:   |
| `Timestamp`            | :octicons-check-16:   |
| `Integral`             | :octicons-check-16:   |
| `Fractional`           | :octicons-check-16:   |
| `String`               | :octicons-check-16:   |
| `Boolean`              | :octicons-check-16:   |

![Screenshot](../assets/checks/rule-types/is-replica-of-check-light.png#only-light)
![Screenshot](../assets/checks/rule-types/is-replica-of-check-dark.png#only-dark)


!!! example
    `materials` (target) is a replica of `samples` (reference).


=== "![Screenshot](../assets/checks/rule-types/icons/icon-shape-anomaly-dark.svg)`Shape Anomaly` error message"
    For `[column_names]`, the referred fields do not replicate the targeted fields.

