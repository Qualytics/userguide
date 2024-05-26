# Entity Resolution

### Definition

*Asserts that every distinct entity is appropriately represented once and only once*

### In-Depth Overview

This check performs automated entity name clustering to identify entities with similar names that likely represent
the same entity. It then assigns each cluster a unique entity identifier and asserts that every row with the same 
entity identifier shares the same value for the designated `distinction field`

### Field Scope

**Single:** The rule evaluates a single specified field.

**Accepted Types**

| Type     |                                                          |
|----------|----------------------------------------------------------|
| `String` | <div style="text-align:center">:octicons-check-16:</div> |

### General Properties

{%
include-markdown "components/general-props/index.md"
start='<!-- filter-only--start -->'
end='<!-- filter-only--end -->'
%}

### Specific Properties

| Name                                                | Description                                                                 |
|-----------------------------------------------------|-----------------------------------------------------------------------------|
| <div class="text-primary">Distinction Field</div>   | The field that must hold a distinct value for every distinct entity         |
| <div class="text-primary">Pair Substrings</div>     | Considers entities a match if one entity is part of the other               |
| <div class="text-primary">Pair Homophones</div>     | Considers entities a match if they sound alike, even if spelled differently |
| <div class="text-primary">Spelling Similarity</div> | The minimum similarity required for clustering two entity names             |


### Anomaly Types

{%
include-markdown "components/anomaly-support/index.md"
start='<!-- record-only--start -->'
end='<!-- record-only--end -->'
%}

### Example

**Objective**: *If you have a `businesses` table with an `id` field and a `name` field, this check can be configured to
resolve `name` and use `id` as the `distinction field`.  During each scan, similar names will be grouped and assigned the
same `entity identifier` and any rows that share the same `entity identifier` but have different values for `id` will be
identified as anomalies.*

**Sample Data**

| BUSINESS_ID | BUSINESS_NAME   |
|-------------|-----------------|
| 1           | ACME Boxing     |
| 2           | Frank's Flowers |
| 3           | ACME Boxes      |

**Anomaly Explanation**

In the sample data above, the entries with `BUSINESS_ID` **1** and **3** do not satisfy the rule because their `BUSINESS_NAME`
values will be marked as similar yet they do not share the same `BUSINESS_ID` 

=== "Flowchart"
```mermaid
graph TD
A[Start] --> B[Retrieve Original Data]
B --> C{Which entities are similar?}
C --> D[Assign each record an entity identifier]
D --> E[Cluster records by entity identifier]
E --> F{Do records with same<br/>entity identifier share the<br/>same distinction field value?}
F -->|Yes| I[End]
F -->|No| H[Mark as Anomalous]
H --> I
```

