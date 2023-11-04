# Rule Name

### Definition

*Provide a concise and clear description of what this rule checks for.*

### In-Depth Overview 

<!--
    Optional: Use this section to give more context about the rule's purpose, logic, and importance.
-->

### Field Scope

<!--
    If the rule does not evaluate specific fields (fiedless) and thus does not have a field scope, this section can be omitted.
-->

<!--
    Choose only one type based on the rule's functionality.
    
    **Single:** The rule evaluates a single specified field.  
    **Multiple:** The rule evaluates multiple specified fields.  
    **Calculated:** The rule automatically identifies the fields involved, without requiring explicit field selection. 
-->

**Single:** The rule evaluates a single specified field.

**Accepted Types**

<!--
    Specify which data types are accepted by the rule.
-->

| Type          | Accepted                       |
|---------------|--------------------------------|
| `Date`        | <div style="text-align:center">:octicons-check-16:</div> |
| `Timestamp`   | <div style="text-align:center">:octicons-check-16:</div> |
| `Integral`    | <div style="text-align:center">:octicons-check-16:</div> |
| `Fractional`  | <div style="text-align:center">:octicons-check-16:</div> |
| `String`      | <div style="text-align:center">:octicons-check-16:</div> |
| `Boolean`     | <div style="text-align:center">:octicons-check-16:</div> |

### General Properties

<!--
    This section describes general properties applicable to the rule. The content is included from a markdown component, which allows for different configurations based on the rule's needs.
-->

<!--
    Use the include-markdown component with the appropriate arguments to include general properties that are relevant to the rule.
    The arguments determine which set of properties are included:
    - all-props
    - filter-only
    - coverage-only
    - none-props
    
    Below is an example of how to include all general properties. Replace 'all-props' with the appropriate argument for your rule.
-->

{%
    include-markdown "components/general-props/index.md"
    start='<!-- all-props--start -->'
    end='<!-- all-props--end -->'
%}

### Specific Properties

<!--
    If the rule does not have specific properties then this section can be omitted.
-->

<!--
    This section lists properties that are unique to a particular rule.
    When defining the properties, ensure consistency in the naming to avoid confusion.
    Use the same input name in the "Name" column as it appears in the rule configuration or user interface.

    Below is an example of how to structure the properties:
-->

| Name        | Description                                                    |
|-------------|----------------------------------------------------------------|
| <div class="text-primary">Input Name 1</div> | Defines a brief description related to the input. |
| <div class="text-primary">Input Name 2</div> | Defines a brief description related to the input. |


### Anomaly Types

<!--
    This section outlines the types of anomalies the rule can detect.
    The content is dynamically included from a markdown component and can vary depending on the rule's capabilities.
-->

<!--
    Utilize the include-markdown component with the correct arguments to display the anomaly types supported by the rule.
    The available arguments are:
    - all-types
    - record-only
    - shape-only
    
    The example below demonstrates how to include content that supports all types of anomalies. Adjust 'all-types' to match the anomaly detection capabilities of the rule.
-->

{%
    include-markdown "components/anomaly-support/index.md"
    start='<!-- all-types--start -->'
    end='<!-- all-types--end -->'
%}

### Example

<!--
    This section provides a practical example to illustrate how the rule can be applied.
    It should help users understand the rule's operation and its application in a real-world scenario.
-->

**Objective**: *<Provide a clear objective for the rule example>*

**Sample Data**

<!--
    Present sample data in a table format. Highlight rows with anomalies if applicable.

    Below is an example of how to structure the sample data:
-->

| O_ORDERKEY | O_COMMENT          | O_ORDERSTATUS   |
|------------|--------------------|-----------------|
| 1          | <span class="text-negative">NULL</span> | <span class="text-negative">NULL</span> |
| 2          | Good product       | NULL            |
| 3          | NULL               | Shipped         |

**Anomaly Explanation**

<!--
    Provide an explanation for the anomalies identified, whether they are specific data points or broader data patterns, as dictated by the rule's logic and the set objective
-->

<!-- 
    This section also includes a mandatory flowchart for visual representation and an optional illustrative SQL query for rules where applicable. 

    Below is an example of how to structure the Flowchart and SQL query:
-->

=== "Flowchart"
    ``` mermaid
    graph TD
    A[Start] --> B[Retrieve O_COMMENT and O_ORDERSTATUS]
    B --> C{Is Either Field Not Null?}
    C -->|Yes| D[Move to Next Record/End]
    C -->|No| E[Mark as Anomalous]
    E --> D
    ```

=== "SQL"
    ```sql
    -- An illustrative SQL query demonstrating the rule applied to example dataset(s).
    select
        o_orderkey
        , o_comment
        , o_orderstatus
    from orders 
    where
        o_comment is null
        and o_orderstatus is null
    ```

**Potential Violation Messages**

<!--
    Provide examples of violation messages that would be generated for the anomalies highlighted in the sample data.
    These should be formatted similarly to how they would appear in the system.
    
    It's required to provide at least one type of violation message (Record Anomaly or Shape Anomaly). If both types of anomalies are applicable to the rule, examples of both should be included. If only one type is relevant, omit the other.

    Below is an example based on the Any Not Null rule:
-->

!!! example "Record Anomaly"
    <!-- Format: There is no value set for any of '{0.field_names}' -->
    There is no value set for any of `O_COMMENT, O_ORDERSTATUS`

!!! example "Shape Anomaly"
    <!-- Format: In {0.field_names}, {1:.3f}%  of {2:d} filtered records ({4:d}) have no value set for any of '{0.field_names}' -->
    In `O_COMMENT, O_ORDERSTATUS`, 33.333% of 3 filtered records (1) have no value set for any of `O_COMMENT, O_ORDERSTATUS`

---

### Reference Examples

For inspiration on rule creation, see these examples:

- Single Field: *Contains Email* rule.
- Multiple Fields: *Any Not Null* rule.
- Calculated Scope: *Satisfies Expression* rule.

For a Comprehensive Documentation you can refer to the *Metric* rule.

_Note that these are for reference only and not part of this guide._
