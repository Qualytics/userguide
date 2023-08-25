# Matches Pattern <spam id='single-field'>`single field`</spam>

---

*Asserts that a field must match a pattern.*

| Accepted Field Types   |                      |
| :--------------------: | :------------------: |
| `String`               | :octicons-check-16:   |

![Screenshot](../assets/checks/rule-types/matches-pattern-check-light.png#only-light)
![Screenshot](../assets/checks/rule-types/matches-pattern-check-dark.png#only-dark)

!!! example
    `Date_of_Payment` matches the pattern `\d{4}-\d{2}-\d{2}`.

=== "![Screenshot](../assets/checks/rule-types/icons/icon-record-anomaly-dark.svg)`Record Anomaly` error message"

    The `[field_name]` value of '`[x value]`' does not matche the pattern `[pattern]`

=== "![Screenshot](../assets/checks/rule-types/icons/icon-shape-anomaly-dark.svg)`Shape Anomaly` error message"
    In `[field_names]`, `[x]`% do not match the pattern `[pattern]`.

