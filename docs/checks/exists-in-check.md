# Exists In

### Definition

*Asserts that values assigned to a field exist as values in another field.*

#### In-Depth Overview

The `ExistsIn` rule allows you to cross-validate data between different sources, whether it’s object storage systems or databases.

Traditionally, databases might utilize foreign key constraints (if available) to enforce data integrity between related tables. The `ExistsIn` rule extends this concept in two powerful ways:

1. **Cross-System Integrity**: it allows for integrity checks to span across different databases or even entirely separate systems. This is particularly advantageous in scenarios where data sources are fragmented across diverse platforms.
2. **Flexible Data Formats**: Beyond just databases, this rule can validate values against various data formats, such as ensuring values in a file align with those in a table.

These enhancements enable businesses to maintain data integrity even in complex, multi-system environments.

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

### General Properties

{% 
    include-markdown "components/general-props/index.md"
    start='<!-- all-props--start -->'
    end='<!-- all-props--end -->' 
%}

### Specific Properties

Define the datastore, table/file, and field where the rule should look for matching values.

| Name                            | Description                                                   |
|---------------------------------|---------------------------------------------------------------|
| <div class="text-primary">Datastore</div>   | The source datastore where the profile of the reference field is located. |
| <div class="text-primary">Table/file</div>   | The profile (e.g. table, view or file) containing the reference field. |
| <div class="text-primary">Field</div>       | The field name whose values should match those of the selected field.  |

### Anomaly Types

{% 
    include-markdown "components/anomaly-support/index.md"
    start='<!-- all-types--start -->'
    end='<!-- all-types--end -->' 
%}

### Example

**Objective**: *Ensure that all NATION_NAME entries in the NATION table match entries under the COUNTRY_NAME column in an external lookup file listing official country names.*

**Sample Data**

| N_NATIONKEY | N_NATIONNAME       |
|-------------|--------------------|
| 1           | Algeria            |
| 2           | Argentina          |
| 3           | <span class="text-negative">Atlantida</span>   |

**Lookup File Sample**

| COUNTRY_NAME       |
|--------------------|
| Algeria            |
| Argentina          |
| Brazil             |
| Canada             |
| ...                |
| Zimbabwe           |


**Anomaly Explanation**

In the sample data above, the entry with `N_NATIONKEY` **3** does not satisfy the rule because the `N_NATIONNAME` "Atlantida" does not match any `COUNTRY_NAME` in the official country names lookup file.

=== "Flowchart"
    ``` mermaid
    graph TD
    A[Start] --> B[Retrieve COUNTRY_NAME]
    B --> C[Retrieve N_NATIONNAME]
    C --> D{Does N_NATIONNAME exists in COUNTRY_NAME?}
    D -->|Yes| E[Move to Next Record/End]
    D -->|No| F[Mark as Anomalous]
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
        n_nationname not in ('Algeria', 'Argentina', ... /* other valid countries */)
    ```

**Potential Violation Messages**

=== "Record Anomaly"
    !!! example
        The `N_NATIONNAME` value of `'Atlantida'` does not exist in `COUNTRY_NAME`.
=== "Shape Anomaly"
    !!! example
        In `N_NATIONNAME`, 33.333% of 3 filtered records (1) do not match any `COUNTRY_NAME`.
