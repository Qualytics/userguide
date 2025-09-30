# Data Diff

!!! info "Recommended Check"
    Qualytics recommends using the `dataDiff` rule type instead of the `isReplicaOf`.
    
    The `isReplicaOf` check is sunsetting and will no longer be maintained, while `dataDiff` provides the same functionality with enhanced performance and additional capabilities.

## What Is DataDiff

The **DataDiff** check compares one dataset against another usually a source and its replica or backup to confirm they are aligned. It validates both the structure (schema, keys, and relationships) and the values of selected fields, helping you quickly spot missing, extra, or altered records.

## What It Does  

- Confirms that a target dataset is identical to a reference dataset.  
- Flags differences in schema or data values.  
- Helps prevent silent mismatches from propagating into pipelines, dashboards, or downstream systems.  

**Example:** Compare a production `Orders` table with its nightly `Orders_Replica`.  
If any orders are missing, duplicated, or altered (e.g., “USA” vs “United States”), the check raises an anomaly.  

## How DataDiff Works

1. **Select Fields and Identifiers** – Choose the fields you want compared, and optionally define row identifiers that uniquely identify each record.

2. **Retrieve Both Datasets** – Qualytics pulls the target data and the reference data from their configured datastores.

3. **Match and Compare** – Each row is matched on the identifiers, then each field’s values are compared.

4. **Flag Differences** – Any discrepancies in structure or values are surfaced as anomalies for review.

This automated process replaces manual SQL joins or spreadsheets with a repeatable, auditable quality check.

## Why Use DataDiff

- **Validate Replication and ETL** – Ensure backups, downstream tables, or warehouses are exact copies of their source.

- **Detect Silent Errors Early** – Catch discrepancies caused by network issues, transformation bugs, or manual mistakes before they propagate.

- **Maintain Data Integrity** – Confirm schema, keys, and relationships remain intact across systems.

- **Automate Data Reconciliation** – Build a repeatable safeguard into your data pipelines without custom code.

**Example:** Compare a production `Orders` table with its nightly `Orders_Replica` in your reporting warehouse to verify every order matches before dashboards refresh.

#### In-Depth Overview

The `DataDiff` rule ensures that data integrity is maintained when comparing data between different sources. This involves checking not only the data values themselves but also ensuring that the structure and relationships are preserved.

In a distributed data ecosystem, data comparison often occurs to validate consistency across systems, verify data transfers, or ensure data quality between sources. However, discrepancies might arise due to various reasons such as network glitches, software bugs, or human errors. The `DataDiff` rule serves as a safeguard against these issues by:

1. **Preserving Data Structure**: Ensuring that the structure of the compared data matches between sources.
2. **Checking Data Values**: Ensuring that every piece of data in the source matches the reference data.

### Field Scope

**Multi:** The rule evaluates multiple specified fields.

**Accepted Types**

| Type        |                          |
|-------------|--------------------------|
| `Date`      | <div style="text-align:center">:octicons-check-16:</div>      |
| `Timestamp` | <div style="text-align:center">:octicons-check-16:</div>      |
| `Integral`  | <div style="text-align:center">:octicons-check-16:</div>      |
| `Fractional`| <div style="text-align:center">:octicons-check-16:</div>      |
| `String`    | <div style="text-align:center">:octicons-check-16:</div>      |
| `Boolean`   | <div style="text-align:center">:octicons-check-16:</div>      |

### General Properties

{%
include-markdown "components/general-props/index.md"
start='<!-- filter-only--start -->'
end='<!-- filter-only--end -->'
%}

### Specific Properties

Specify the datastore and table/file where the reference data for the targeted fields is located for comparison.

| Name       | Description                                                   |
|------------|---------------------------------------------------------------|
| <div class="text-primary">Row Identifiers</div>  | The list of fields defining the compound key to identify rows in the comparison analysis. |
| <div class="text-primary">Datastore</div>  | The source datastore where the reference data for the targeted field(s) is located. |
| <div class="text-primary">Table/file</div> | The table, view or file in the source datastore that should serve as the reference for comparison. |
| <div class="text-primary">Comparators</div> | {{ comparator_short_desc }} |

!!! info
    The `DataDiff` rule supports editing of `Row Identifiers` and `Passthrough Fields`, allowing for more tailored configuration.

!!! note "Details"
    <div style="margin-top: -12px;">
    ### Row Identifiers
    </div>

    This optional input allows row comparison analysis by defining a list of fields as row identifiers, it enables a more detailed comparison between tables/files, where each row compound key is used to identify its presence or absence in the reference table/file compared to the target table/file.  Qualytics can inform if the row exists or not and distinguish which field values differ in each row present in the reference table/file, helping to determine if it is a data diff.

    !!! info
        Anomalies produced by a `DataDiff` quality check making use of `Row Identifiers` have their source records presented in a different visualization. <br><br>
        See more at: *[Comparison Source Records](../anomalies/source-record.md/#comparison-source-records)*

    {%
        include-markdown "components/comparators/index.md"
    %}
    {%
        include-markdown "components/comparators/numeric.md"
    %}
    {%
        include-markdown "components/comparators/duration.md"
    %}
    {%
        include-markdown "components/comparators/string.md"
    %}

### Anomaly Types

{%
    include-markdown "components/anomaly-support/index.md"
    start='<!-- shape-only--start -->'
    end='<!-- shape-only--end -->'
%}

### Example

**Scenario**: *Consider that the fields N_NATIONKEY and N_NATIONNAME in the NATION table need to be compared with a backup database for data validation purposes. The data engineering team wants to ensure that both fields in the backup accurately match the original.*

**Objective**: *Ensure that N_NATIONKEY and N_NATIONNAME from the NATION table match the data in the NATION_BACKUP table.*

**Sample Data from NATION**

| N_NATIONKEY | N_NATIONNAME       |
|-------------|--------------------|
| 1           | Australia          |
| 2           | United States      |
| 3           | Uruguay            |

**Reference Sample Data from NATION_BACKUP**

| N_NATIONKEY | N_NATIONNAME       |
|-------------|--------------------|
| 1           | Australia          |
| 2           | USA                |
| 3           | Uruguay            |

=== "Payload example"
    ``` json
    {
        "description": "Ensure that N_NATIONKEY and N_NATIONNAME from the NATION table match the data in the NATION_BACKUP table",
        "coverage": 1,
        "properties": {
            "ref_container_id": {ref_container_id},
            "ref_datastore_id": {ref_datastore_id}
        },
        "tags": [],
        "fields": ["N_NATIONKEY", "N_NATIONNAME"],
        "additional_metadata": {"key 1": "value 1", "key 2": "value 2"},
        "rule": "dataDiff",
        "container_id": {container_id},
        "template_id": {template_id},
        "filter": "1=1"
    }
    ```

**Anomaly Explanation**

The datasets representing the fields `N_NATIONKEY` and `N_NATIONNAME` in the original and the reference data are not completely identical, indicating a possible discrepancy in the data or an unintended change.

=== "Flowchart"
    ```mermaid
    graph TD
    A[Start] --> B[Retrieve Original Data]
    B --> C[Retrieve Reference Data]
    C --> D{Do datasets match for both fields?}
    D -->|Yes| E[End]
    D -->|No| F[Mark as Anomalous]
    F --> E
    ```

=== "SQL"
    ```sql
    -- An illustrative SQL query comparing original to reference data for both fields.
    select
        orig.n_nationkey as original_key,
        orig.n_nationname as original_name,
        ref.n_nationkey as reference_key,
        ref.n_nationname as reference_name
    from nation as orig
    left join nation_backup as ref on orig.n_nationkey = ref.n_nationkey
    where
        orig.n_nationname <> ref.n_nationname
    or
        orig.n_nationkey <> ref.n_nationkey
    ```

**Potential Violation Messages**

!!! example "Shape Anomaly"
    There is 1 record that differs between `NATION_BACKUP` (3 records) and `NATION` (3 records) in `<datastore_name>`