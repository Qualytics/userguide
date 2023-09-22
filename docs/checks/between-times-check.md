# Between Times <spam id='single-field'>`single field`</spam>

---

*Asserts that values are equal to or between two dates or times.*

| Accepted Field Types   |                      |
| :--------------------: | :------------------: |
| `Date`                 | :octicons-check-16:   |
| `Timestamp`            | :octicons-check-16:   |

![Screenshot](../assets/checks/rule-types/between-times-check-light.png#only-light)
![Screenshot](../assets/checks/rule-types/between-times-check-dark.png#only-dark)

!!! example
    `order_time` is between `2021-01-01` and `2022-12-31`

=== "![Screenshot](../assets/checks/rule-types/icons/icon-record-anomaly-dark.svg)`Record Anomaly` error message"

    The value for `[field_name]` of '`[x value]`' is not between `[min_value]` and `[max_value]`.

=== "![Screenshot](../assets/checks/rule-types/icons/icon-shape-anomaly-dark.svg)`Shape Anomaly` error message"
    In `[field_names]`, `[x]`% are not not between `[min_value]` and `[max_value]`.

