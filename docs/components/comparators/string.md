#### String

String comparators facilitate comparisons of textual data by allowing variations in spacing. This capability is essential for ensuring data consistency, particularly where minor text inconsistencies may occur.

##### Ignore Whitespace

When enabled, this setting allows the comparator to ignore differences in whitespace. This means sequences of whitespace are collapsed into a single space, and any leading or trailing spaces are removed. This can be particularly useful in environments where data entry may vary in formatting but where those differences are not relevant to the data's integrity.

??? example "Illustration"
    _TBD_

    **Thresholds**: Min Value = 100, Max Value = 300

    | Scan | Current Value | Anomaly Detected |
    |------|---------------|------------------|
    | #1    | 150           | No              |
    | #2    | <div class="text-negative">90</div> | <div class="text-negative">Yes</div> |
    | #3    | 250           | No               |
    | #4    | <div class="text-negative">310</div> | <div class="text-negative">Yes</div> |
