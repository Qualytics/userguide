# Min Partition Size

### Definition

*Asserts the minimum number of records that should be loaded from each file or table partition.*

### In-Depth Overview

When working with large datasets that are often partitioned for better performance and scalability, ensuring a certain minimum number of records from each partition becomes crucial. This could be to ensure that each partition is well-represented in the analysis, to maintain data consistency or even to verify that data ingestion or migration processes are functioning properly.

The Min Partition Size rule allows users to set a threshold ensuring that each partition has loaded at least the specified minimum number of records.

### General Properties

{%
    include-markdown "components/general-props/index.md"
    start='<!-- coverage-only--start -->'
    end='<!-- coverage-only--end -->'
%}

### Specific Properties

Sets the required minimum record count for each data partition

| Name                              | Description |
|-----------------------------------|-------------|
| <div class="text-primary">Minimum partition size</div> | Specifies the minimum number of records that should be loaded from each partition |

### Anomaly Types

{%
    include-markdown "components/anomaly-support/index.md"
    start='<!-- shape-only--start -->'
    end='<!-- shape-only--end -->'
%}

### TPC-H Example

**Objective**: *Ensure that each partition of the LINEITEM table has at least 1000 records.*

**Sample Data for Partition P3**

| Row Number | L_ITEM |
|------------|-------|
| 1          | Data  |
| 2          | Data  |
| ...        | ...   |
| 900        | Data  |

The sample data above does not satisfy the rule because it contains only 900 records, which is less than the required minimum of 1000 records.

=== "Flowchart"
    ```mermaid
    graph TD
    A[Start] --> B[Retrieve Number of Records for Each Partition]
    B --> C{Does Partition have >= 1000 records?}
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
    having count(*) < 1000;
    ```

**Potential Violation Messages**

=== "Shape Anomaly"
    !!! example
        In `LINEITEM`, fewer than 900 records were loaded.
