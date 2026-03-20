# Max Length

### Definition

*Asserts that a string has a maximum length.*

### Field Scope

**Single:** The rule evaluates a single specified field.

**Accepted Types**

| Type        |                          |
|-------------|--------------------------|
| `String`    | <div style="text-align:center">:octicons-check-16:</div>      |

### General Properties

{%
    include-markdown "components/general-props/index.md"
    start='<!-- all-props--start -->'
    end='<!-- all-props--end -->'
%}

### Specific Properties

Determines the maximum acceptable length of the string.

| Name               | Description           |
|--------------------|-----------------------|
| <div class="text-primary">Length</div>             | Specifies the maximum number of characters a string in the field should have. |

### Anomaly Types

{%
    include-markdown "components/anomaly-support/index.md"
    start='<!-- all-types--start -->'
    end='<!-- all-types--end -->'
%}

### Example

**Objective**: *Ensure that P_DESCRIPTION in the PART table do not exceed 50 characters in length.*

**Sample Data**

| P_PARTKEY | P_DESCRIPTION                      |
|-----------|------------------------------------|
| 1         | Standard industrial widget         |
| 2         |  <span class="text-negative">A product description that clearly goes way beyond the specified fifty characters limit.</span> |
| 3         | Basic office equipment             |

=== "Payload example"
    ``` json
    {
        "description": "Ensure that P_DESCRIPTION in the PART table do not exceed 50 characters in length",
        "coverage": 1,
        "properties": {
            "value": 3
        },
        "tags": [],
        "fields": ["C_BLOOD_GROUP"],
        "additional_metadata": {"key 1": "value 1", "key 2": "value 2"},
        "rule": "maxLength",
        "container_id": {container_id},
        "template_id": {template_id},
        "filter": "1=1"
    }
    ```

**Anomaly Explanation**

In the sample data above, the entry with `P_PARTKEY` **2** does not satisfy the rule because its `P_DESCRIPTION` exceeds 50 characters in length.

=== "Flowchart"
    ```mermaid
    graph TD
    A[Start] --> B[Retrieve P_DESCRIPTION]
    B --> C{Is P_DESCRIPTION length <= 50 characters?}
    C -->|Yes| D[Move to Next Record/End]
    C -->|No| E[Mark as Anomalous]
    E --> D
    ```

=== "SQL"
    ```sql
    -- An illustrative SQL query demonstrating the rule applied to example dataset(s).
    select
        p_partkey,
        p_description
    from part 
    where
        length(p_description) > 50;
    ```

**Potential Violation Messages**

!!! example "Record Anomaly"
    The `P_DESCRIPTION` length of `A product description that clearly goes way beyond the specified fifty characters limit.` is greater than the max length of 50.
        
!!! example "Shape Anomaly"
    In `P_DESCRIPTION`, 33.333% of 3 filtered records (1) have a length greater than 50.
