# Min Partition Size <spam id='none-field'>`none field`</spam>

---

*Asserts the minimum number of records that should be loaded from each file or table partition.*

| Accepted Field Types   |                      |
| :--------------------: | :------------------: |
| `Date`                 | :octicons-check-16:   |
| `Timestamp`            | :octicons-check-16:   |
| `Integral`             | :octicons-check-16:   |
| `Fractional`           | :octicons-check-16:   |
| `String`               | :octicons-check-16:   |
| `Boolean`              | :octicons-check-16:   |

![Screenshot](../assets/checks/rule-types/min-partition-size-check-light.png#only-light)
![Screenshot](../assets/checks/rule-types/min-partition-size-check-dark.png#only-dark)
!!! example
    `orders` has at least `1000` records.

=== "![Screenshot](../assets/checks/rule-types/icons/icon-shape-anomaly-dark.svg)`Shape Anomaly` error message"
    In `[field_names]`, fewer than `[value]` records were loaded.

