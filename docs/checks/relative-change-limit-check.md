# Relative Change Limit <spam id='single-field'>`single field`</spam>
---

The `Relative Change Limit` check operates by tracking changes in a numeric field's value relative to its previous value. If the change exceeds the predefined percentage (%) limit since the last relevant scan, an anomaly is generated.

- This tool is crucial for maintaining data consistency, especially when dealing with large datasets where relative changes might be more informative than absolute ones. Join us as we explore the workings of the `Relative Change Limit` check to help you better manage your data.

---
*Asserts that the field has not changed by more than a relative amount since the last applicable scan.*

| Accepted Field Types   |                      |
| :--------------------: | :------------------: |
| `Integral`                 | :octicons-check-16:   |
| `Fractional`            | :octicons-check-16:   |


![Screenshot](../assets/checks/rule-types/relative-change-limit-light.png#only-light)
![Screenshot](../assets/checks/rule-types/relative-change-limit-dark.png#only-dark)

!!! example
    `balance` has min `0` and max `200`

=== "![Screenshot](../assets/checks/rule-types/icons/icon-record-anomaly-dark.svg)`Record Anomaly` error message"
    The absolute change of `[field_name]` from '`[min value]`' to `[max value]` exceeds the declared limits.
--- 