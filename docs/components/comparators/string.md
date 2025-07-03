#### String

String comparators facilitate comparisons of textual data by allowing variations in spacing. This capability is essential for ensuring data consistency, particularly where minor text inconsistencies may occur.

##### Ignore Whitespace

When enabled, this setting allows the comparator to ignore differences in whitespace. This means sequences of whitespace are collapsed into a single space, and any leading or trailing spaces are removed. This can be particularly useful in environments where data entry may vary in formatting but where those differences are not relevant to the data's integrity.

??? example "Illustration"

    In this example, it compares `Value A` and `Value B` according to the defined string comparison to `ignore whitespace` as `True`.

    | Value A   | Value B   | Are equal?                              | Has whitespace?|
    |-----------|-----------|-----------------------------------------|----------------|
    | `Leonidas`| `Leonidas`|  True                                   | No             | 
    | `Beth`    | ` Beth `  |  True                                   | Yes            |
    | `Ana`     | ` Anna `  |  <div class="text-negative">False</div> | Yes            |
    | `Joe`     | `Joel`    |  <div class="text-negative">False</div> | No             |
