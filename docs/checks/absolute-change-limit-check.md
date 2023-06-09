# Absolute Change Limit <spam id='single-field'>`single field`</spam>

---
The `Absolute Change Limit` check works by comparing the change in a numeric field's value to a pre-set limit (Min or Max). If the field's value changes by more than this specified limit since the last relevant scan, an anomaly is identified.

- This feature plays a critical role in maintaining data integrity and ensuring no significant changes go unnoticed. Join us as we delve into the specifics of how to use the `Absolute Change Limit` check to monitor your data more effectively. 

---
*Asserts that the field has not changed by more than a fixed amount since the last applicable scan.*

| Accepted Field Types   |                      |
| :--------------------: | :------------------: |
| `Integral`                 | :octicons-check-16:   |
| `Fractional`            | :octicons-check-16:   |


![Screenshot](../assets/checks/rule-types/absolute-change-limit-light.png#only-light)
![Screenshot](../assets/checks/rule-types/absolute-change-limit-dark.png#only-dark)

!!! example
    `balance` has min `0` and max `200`

=== "![Screenshot](../assets/checks/rule-types/icons/icon-record-anomaly-dark.svg)`Record Anomaly` error message"
    The absolute change of `[field_name]` from '`[min value]`' to `[max value]` exceeds the declared limits.
--- 