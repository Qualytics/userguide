# Merge Fields

When a column is renamed in the source data, the next profile operation creates a new **Active** field with the updated name and marks the original field as **Missing**. The merge operation combines these two fields into one, preserving all historical data under the new column name.

## Why Merge?

Without merging, a column rename results in:

- A **Missing** field that retains all historical profiles, anomalies, and quality checks
- A new **Active** field with no history

Merging transfers the historical context from the old field to the new one, ensuring continuity in your quality monitoring.

## What Happens During a Merge?

When you merge a **source field** (the old field with history) into a **target field** (the new field with the desired name):

| Step | Action |
| :--- | :--- |
| 1 | The source field adopts the target field's name |
| 2 | The target field record is removed |
| 3 | The source field status is set to **Active** |
| 4 | All historical field profiles are renamed to match the new field name |
| 5 | Quality checks from the target field are reassociated to the source field |

## What Is Preserved?

| Asset | Behavior |
| :--- | :--- |
| **Field profiles** | All historical profiles from the source field are preserved and renamed |
| **Quality checks** | Checks from both fields are combined under the merged field |
| **Anomalies** | Historical anomalies from the source field remain linked to the merged field |
| **Computed field definitions** | Definitions referencing the source field remain intact |

## Restrictions

- Both fields must belong to the **same container**
- A field cannot be merged with itself
- Bulk merge is **not supported** — each merge must be performed individually

## Example

Your database team renames the column `cust_id` to `customer_id`. After the next profile operation, you see `cust_id` marked as **Missing** and a new `customer_id` field created as **Active**. To preserve all historical data:

1. Use the merge operation to combine `cust_id` (source) into `customer_id` (target).
2. All field profiles, anomalies, and quality checks from `cust_id` are preserved under the `customer_id` name.
3. Quality monitoring continues seamlessly with full historical context.

!!! tip
    Merge is the recommended approach when dealing with column renames. It preserves your complete quality monitoring history and avoids the need to reconfigure quality checks from scratch on the renamed field.
