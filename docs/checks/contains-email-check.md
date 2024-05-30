# Contains Email

### Definition

*Asserts that the values contain email addresses.*

### Field Scope

**Single:** The rule evaluates a single specified field.

**Accepted Types**

| Type     |                          |
|----------|--------------------------|
| `String` | <div style="text-align:center">:octicons-check-16:</div> |

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

**Objective**: *.*

**Sample Data**

| C_CUSTKEY | C_CONTACT_DETAILS                          |
|-----------|----------------------------------|
| 1         | {"name": "John Doe", "email": "john.doe@example.com"}             |
| 2         | <span class="text-negative">{"name": "Amy Lu", "email": "amy.lu@"}</span> |
| 3         | {"name": "Jane Smith", "email": "jane.smith@domain.org"}            |

=== "Payload example"
    ``` json
    {
        "description": "Ensure that all C_CONTACT_DETAILS entries in the CUSTOMER table contain valid email addresses",
        "coverage": 1,
        "properties": {},
        "tags": [],
        "fields": ["C_EMAIL_JSON"],
        "additional_metadata": {"key 1": "value 1", "key 2": "value 2"},
        "rule": "containsEmail",
        "container_id": {container_id},
        "template_id": {template_id},
        "filter": "1=1"
    }
    ```

**Anomaly Explanation**

In the sample data above, the entry with `C_CUSTKEY` **2** does not satisfy the rule because its `C_CONTACT_DETAILS` value does not follow a typical email format.

=== "Flowchart"
    ``` mermaid
    graph TD
    A[Start] --> B[Retrieve C_CONTACT_DETAILS]
    B --> C{Does C_CONTACT_DETAILS contain an email address?}
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
        not regexp_like(c_contact_details, '^[a-za-z0-9._%-]+@[a-za-z0-9.-]+\.[a-za-z]{2,4}$')
    ```

**Potential Violation Messages**

!!! example "Record Anomaly"
    The `C_CONTACT_DETAILS` value of `{"name": "Amy Lu", "email": "amy.lu@"}` does not contain an email address.

!!! example "Shape Anomaly"
    In `C_CONTACT_DETAILS`, 33.333% of 3 filtered records (1) do not contain email addresses.
