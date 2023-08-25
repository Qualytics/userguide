# Metric <spam id='single-field'>`single field`</spam>

---

| Accepted Field Types   |                      |
| :--------------------: | :------------------: |
| `Integral`             | :octicons-check-16:   |
| `Fractional`           | :octicons-check-16:   |

![Screenshot](../assets/checks/rule-types/metric-check-light.png#only-light)
![Screenshot](../assets/checks/rule-types/metric-check-dark.png#only-dark)


## `Comparsion` options:

![Screenshot](../assets/checks/rule-types/comparison-options-light.png#only-light)
![Screenshot](../assets/checks/rule-types/comparison-options-dark.png#only-dark)

### Absolute Change

The `Absolute Change` comparison works by comparing the change in a numeric field's value to a pre-set limit (Min or Max). If the field's value changes by more than this specified limit since the last relevant scan, an anomaly is identified.

- This feature plays a critical role in maintaining data integrity and ensuring no significant changes go unnoticed.

---
*Asserts that the field has not changed by more than a fixed amount (inclusive) since the last applicable scan*

!!!example
    `balance` has min `0` and max `200`

=== "![Screenshot](../assets/checks/rule-types/icons/icon-record-anomaly-dark.svg)`Record Anomaly` error message"
    The absolute change of `[field_name]` from '`[min value]`' to `[max value]` falls outside the declared limits
--- 

### Absolute Value

The `Absolute Value` comparison works by comparing the change in a numeric field's value to a pre-set limit `between` Min and Max values. If the field's value changes by more than this specified range since the last relevant scan, an anomaly is identified.

- This feature plays a critical role in maintaining data integrity and ensuring no significant changes go unnoticed

---
*Records the value of the selected field during each scan operation and asserts that the value is within a specified range (inclusive)*

!!!example
    `price` is between `200` and `865`

=== "![Screenshot](../assets/checks/rule-types/icons/icon-record-anomaly-dark.svg)`Record Anomaly` error message"
    The value for {0.field_names} of {1} is not between '`[min value]`' and `[max value]`
--- 


### Percentage Change

The `Percentage Change` comparison operates by tracking changes in a numeric field's value relative to its previous value. If the change exceeds the predefined percentage (%) limit since the last relevant scan, an anomaly is generated.

- This tool is crucial for maintaining data consistency, especially when dealing with large datasets where percentage changes might be more informative than absolute ones.

---
*Asserts that the field has not changed by more than a percentage amount (inclusive) since the last applicable scan*


!!!example
    `balance` has min `0` and max `200`

=== "![Screenshot](../assets/checks/rule-types/icons/icon-record-anomaly-dark.svg)`Record Anomaly` error message"
    The absolute change of `[field_name]` from '`[min value]`' to `[max value]` falls outside the declared limits

