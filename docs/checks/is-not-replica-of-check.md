# Is Not Replica Of <spam id='multiple-fields'>`multiple fields`</spam>
---

The `IsNotReplicaOf` feature verifies that a complete table or column in your source datastore is not mirrored in your destination datastore. This ensures that the data, structure, and relationships of your original tables or columns are distinct and do not appear identically in the referred tables or columns.

By using the `IsNotReplicaOf` feature, you're taking a proactive step in ensuring data differentiation and uniqueness across your datasets. This tool ensures that there are deliberate and distinguishable differences between the source and destination, guaranteeing that datasets remain distinct and that there are no unintended replications.

---

*Asserts that the dataset created by the targeted field(s) is not replicated by the referred field(s).*

| Accepted Field Types   |                      |
| :--------------------: | :------------------: |
| `Date`                 | :octicons-check-16:   |
| `Timestamp`            | :octicons-check-16:   |
| `Integral`             | :octicons-check-16:   |
| `Fractional`           | :octicons-check-16:   |
| `String`               | :octicons-check-16:   |
| `Boolean`              | :octicons-check-16:   |

![Screenshot](../assets/checks/rule-types/is-not-replica-of-check-light.png#only-light)
![Screenshot](../assets/checks/rule-types/is-not-replica-of-check-dark.png#only-dark)


!!! example
    `bank` (target) is not a mirror of `bank_transactions` (reference).


=== "![Screenshot](../assets/checks/rule-types/icons/icon-shape-anomaly-dark.svg)`Shape Anomaly` error message"
    For `[column_names]`, the referred fields do replicate the targeted fields



---