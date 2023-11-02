# Max Partition Size

### Definition

*Asserts the maximum number of records that should be loaded from each file or table partition.*

### In-Depth Overview

Managing the volume of data in each partition is critical when dealing with partitioned datasets. This is especially pertinent when system limitations or data processing capabilities are considered, ensuring that no partition exceeds the system's ability to handle data efficiently.

The Max Partition Size rule is designed to set an upper limit on the number of records each partition can contain.

### General Properties

{%
    include-markdown "components/general-props/index.md"
    start='<!-- coverage-only--start -->'
    end='<!-- coverage-only--end -->'
%}

### Specific Properties

Specifies the maximum allowable record count for each data partition

| Name                              | Description |
|-----------------------------------|-------------|
| <div class="text-primary">Maximum partition size</div> | The maximum number of records that can be loaded from each partition. |

### Anomaly Types

{%
    include-markdown "components/anomaly-support/index.md"
    start='<!-- shape-only--start -->'
    end='<!-- shape-only--end -->'
%}

### TPC-H Example

**Objective**: *Ensure that no partition of the LINEITEM table contains more than 10,000 records to prevent data processing bottlenecks.*

**Sample Data for Partition P3**

| Row Number | L_ITEM |
|------------|--------|
| 1          | Data   |
| 2          | Data   |
| ...        | ...    |
| 10,050     | Data   |

In the sample data above, the rule is violated because partition P3 contains 10,050 records, which exceeds the set maximum of 10,000 records.

=== "Flowchart"
    ```mermaid
    graph TD
    A[Start] --> B[Retrieve Number of Records for Each Partition]
    B --> C{Does Partition have <= 10,000 records?}
    C -->|Yes| D[Move to Next Partition/End]
    C -->|No| E[Mark as Anomalous]
    E --> D
    ```

=== "SQL"
    ```sql
    -- An illustrative SQL query related to the rule using TPC-H tables. 
    select
        subset_name, -- or any column indicating the partition or subset
        count(*)
    from lineitem 
    group by subset_name
    having count(*) > 10000;
    ```

**Potential Violation Messages**

=== "Shape Anomaly"
    !!! example
        In `LINEITEM`, more than 10,000 records were loaded.
