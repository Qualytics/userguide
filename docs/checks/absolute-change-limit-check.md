# Absolute Change Limit <spam id='single-field'>`single field`</spam>

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