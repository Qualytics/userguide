# Contains Social Security Number

### Definition

*Asserts that the values contain a social security number.*

### Field Scope

**Single:** The rule evaluates a single specified field.

**Accepted Types**

| Type    |                          |
|---------|--------------------------|
| `String` | <div style="text-align:center">:octicons-check-16:</div>     |

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

**Objective**: *Ensure that all C_CONTACT_DETAILS entries in the CUSTOMER table contain valid social security numbers.*

**Sample Data**

| C_CUSTKEY | C_CONTACT_DETAILS              |
|-----------|--------------------|
| 1         | {"name": "John Doe", "ssn": "234567890"}        |
| 2         | <span class="text-negative">{"name": "Amy Lu", "ssn": "666-12-3456"}</span> |
| 3         | {"name": "Jane Smith", "ssn": "429-14-2216"}        |

=== "Payload example"
    ``` json
    {
        "description": "Ensure that all C_CONTACT_DETAILS entries in the CUSTOMER table contain valid social security numbers",
        "coverage": 1,
        "properties": {},
        "tags": [],
        "fields": ["C_CONTACT_DETAILS"],
        "additional_metadata": {"key 1": "value 1", "key 2": "value 2"},
        "rule": "containsSocialSecurityNumber",
        "container_id": {container_id},
        "template_id": {template_id},
        "filter": "1=1"
    }
    ```

**Anomaly Explanation**

In the sample data above, the entry with `C_CUSTKEY` **2** does not satisfy the rule because its `C_CONTACT_DETAILS` value does not contain the typical social security number format.

=== "Flowchart"
    ``` mermaid
    graph TD
    A[Start] --> B[Retrieve C_CONTACT_DETAILS]
    B --> C{Does C_CONTACT_DETAILS contain a valid SSN format?}
    C -->|Yes| D[Move to Next Record/End]
    C -->|No| E[Mark as Anomalous]
    E --> D
    ```

=== "SQL"
    ```sql
    -- An illustrative SQL query demonstrating the rule applied to example dataset(s).
    select
        c_custkey,
        c_contact_details
    from customer 
    where
        not regexp_like(ssn, '^[0-9]{3}-[0-9]{2}-[0-9]{4}$')
    ```

**Potential Violation Messages**

!!! example "Record Anomaly"
    The `C_CONTACT_DETAILS` value of `{"name": "Amy Lu", "ssn": "666-12-3456"}` does not contain a social security number.

!!! example "Shape Anomaly"
    In `C_CONTACT_DETAILS`, 33.333% of 3 filtered records (1) do not contain social security numbers.
