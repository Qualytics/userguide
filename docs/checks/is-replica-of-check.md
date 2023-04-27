# Is Replica Of <spam id='multiple-fields'>`multiple fields`</spam>

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
    There are `[x]` records that differ between 
    `[target_table]` and `[reference_table]` in `[datastore_name]`



---