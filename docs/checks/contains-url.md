# Contains URL

### Definition

*Asserts that the values contain valid URLs.*

### Field Scope

**Single:** The rule evaluates a single specified field.

**Accepted Types**

| Type    |                          |
|---------|--------------------------|
| `String`  | <div style="text-align:center">:octicons-check-16:</div>  |

### General Properties

{%
    include-markdown "components/general-props/index.md"
    start='<!-- all-props--start -->'
    end='<!-- all-props--end -->'
%}

### Anomaly Types

{%
    include-markdown "components/anomaly-support/index.md"
    start='<!-- all-types--start -->'
    end='<!-- all-types--end -->'
%}

### Example

**Objective**: *Ensure that all S_DETAILS entries in the SUPPLIER table contain valid URLs.*

**Sample Data**

| S_SUPPKEY | S_DETAILS                       |
|-----------|---------------------------------|
| 1         | <span class="text-negative">{"name": "Tech Parts", "website": "www.techparts.com"}</span>   |
| 2         | {"name": "Hardwarepro", "website": "https://www.hardwarepro.com"}   |
| 3         | <span class="text-negative">{"name": "Smith's Tools", "website": "ftp:server:8080"}</span>     |


=== "Payload example"
    ``` json
    {
        "description": "Ensure that all S_DETAILS entries in the SUPPLIER table contain valid URLs",
        "coverage": 1,
        "properties": {},
        "tags": [],
        "fields": ["S_DETAILS"],
        "additional_metadata": {"key 1": "value 1", "key 2": "value 2"},
        "rule": "containsUrl",
        "container_id": {container_id},
        "template_id": {template_id},
        "filter": "1=1"
    }
    ```


**Anomaly Explanation**

In the sample data above, the entries with `S_SUPPKEY` **1** and **3** do not satisfy the rule because their `S_DETAILS` values do not contain a valid URL pattern.

=== "Flowchart"
    ```mermaid
    graph TD
    A[Start] --> B[Retrieve S_DETAILS]
    B --> C{Does S_DETAILS contain a valid URL?}
    C -->|Yes| D[Move to Next Record/End]
    C -->|No| E[Mark as Anomalous]
    E --> D
    ```

=== "SQL"
    ```sql
    -- An illustrative SQL query demonstrating the rule applied to example dataset(s).
    select
        s_suppkey,
        s_details
    from supplier 
    where
        not regexp_like(url, '^https?://.+')
    ```

**Potential Violation Messages**

!!! example "Record Anomaly"
    The `S_DETAILS` value of `{"name": "Tech Parts", "website": "www.techparts.com"}` does not contain a valid URL.

!!! example "Shape Anomaly"
    In `S_DETAILS`, 66.667% of 3 filtered records (2) do not contain a valid URL.
