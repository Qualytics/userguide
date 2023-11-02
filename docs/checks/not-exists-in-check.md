# Not Exists In

### Definition

*Asserts that values assigned to this field do not exist as values in another field.*

#### In-Depth Overview

The `Not ExistsIn` rule allows you to ensure data exclusivity between different sources, whether it’s object storage systems or databases.

While databases might utilize unique constraints to maintain data distinctiveness between related tables, the `Not ExistsIn` rule extends this capability in two significant ways:

1. **Cross-System Exclusivity**: it enables checks to ensure data does not overlap across different databases or even entirely separate systems. This can be essential in scenarios where data should be partitioned or isolated across platforms.
2. **Flexible Data Formats**: Not just limited to databases, this rule can validate values against various data formats, such as ensuring values in a file do not coincide with those in a table.

These functionalities enable businesses to maintain data exclusivity even in intricate, multi-system settings.

### Field Scope

**Single:** The rule evaluates a single specified field.

**Accepted Types**

| Type        |                          |
|-------------|--------------------------|
| `Date`      | <div style="text-align:center">:octicons-check-16:</div>  |
| `Timestamp` | <div style="text-align:center">:octicons-check-16:</div>  |
| `Integral`  | <div style="text-align:center">:octicons-check-16:</div>  |
| `Fractional`| <div style="text-align:center">:octicons-check-16:</div>  |
| `String`    | <div style="text-align:center">:octicons-check-16:</div>  |
| `Boolean`   | <div style="text-align:center">:octicons-check-16:</div>  |

### Specific Properties

Define the datastore, table/file, and field where the rule should look for non-matching values.

| Name                            | Description                                                   |
|---------------------------------|---------------------------------------------------------------|
| <div class="text-primary">Datastore</div>   | The source datastore where the profile of the reference field is located. |
| <div class="text-primary">Table/file</div>   | The profile (e.g. table, view or file) containing the reference field. |
| <div class="text-primary">Field</div>       | The field name whose values should not match those of the selected field.  |

### Anomaly Types

{% 
    include-markdown "components/anomaly-support/index.md"
    start='<!-- all-types--start -->'
    end='<!-- all-types--end -->' 
%}

### Example

**Scenario**: *A shipping company needs to ensure that all NATION_NAME entries in the NATION table aren't listed in an external unsupported regions file, which lists countries they don't ship to.*

**Sample Data**

| N_NATIONKEY | N_NATIONNAME       |
|-------------|--------------------|
| 1           | <span class="text-negative">Antarctica</span> |
| 2           | Argentina          |
| 3           | Atlantida          |

**Unsupported Regions File Sample**

| UNSUPPORTED_REGION |
|--------------------|
| Antarctica         |
| Mars               |
| ...                |

**Anomaly Explanation**

In the sample data above, the entry with `N_NATIONKEY` **1** does not satisfy the rule because the `N_NATIONNAME` "Antarctica" is listed as an `UNSUPPORTED_REGION` in the unsupported regions file, indicating the company doesn't ship there.

=== "Flowchart"
    ``` mermaid
    graph TD
    A[Start] --> B[Retrieve UNSUPPORTED_REGION]
    B --> C[Retrieve N_NATIONNAME]
    C --> D{Is N_NATIONNAME listed in UNSUPPORTED_REGION?}
    D -->|No| E[Move to Next Record/End]
    D -->|Yes| F[Mark as Anomalous]
    F --> E
    ```

=== "SQL"
    ```sql
    -- An illustrative SQL query demonstrating the rule applied to example dataset(s).
    select
        n_nationkey
        , n_nationname
    from nation 
    where
        n_nationname in ('Antarctica', 'Mars', ... /* other unsupported regions */)
    ```

**Potential Violation Messages**

!!! example "Record Anomaly"
    The `N_NATIONNAME` value of '`Antarctica`' is an `UNSUPPORTED_REGION`.

!!! example "Shape Anomaly"
    In `N_NATIONNAME`, 33.333% of 3 filtered records (1) do exist in `UNSUPPORTED_REGION`.
