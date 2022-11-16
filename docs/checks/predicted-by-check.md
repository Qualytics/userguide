# Predicted By <spam id='single-field'>`single field`</spam>

---

*Asserts that the actual value of a field falls within the expected predicted range.*

| Accepted Field Types   |                      |
| :--------------------: | :------------------: |
| `Date`                 | :white_check_mark:   |
| `Timestamp`            | :white_check_mark:   |
| `Integral`             | :white_check_mark:   |
| `Fractional`           | :white_check_mark:   |

![Screenshot](../assets/checks/rule-types/predicted-by-check.png){: style="height:450px"}

!!! example
    The `price` is predicted by `[expression] profit *10 + cogs *-10` +/- `[tolerance] 100.0`
    
=== "![Screenshot](../assets/checks/rule-types/icons/icon-record-anomaly-dark.svg)`Record Anomaly` error message"
    The `[field_name]` value of `['x']` is not within the predicted range defined by `[expression]`+/- `[tolerance]`

=== "![Screenshot](../assets/checks/rule-types/icons/icon-shape-anomaly-dark.svg)`Shape Anomaly` error message"
    In `[field_names]`, `[x]`% are not within the predicted range defined by `[expression]` +/- `[tolerance]`

---