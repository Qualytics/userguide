# Understanding Field Status

Field Status is a property assigned to every field in Qualytics that determines how the platform interacts with it. It acts as a lifecycle indicator, controlling whether a field is included in profiling (collecting metadata and statistics), scanning (detecting anomalies), and quality check evaluations — and whether its values are visible or hidden.

Understanding field status is essential for managing data quality effectively, as it directly influences which fields are monitored, how schema changes are detected, how quality checks behave over time, and how sensitive data is protected.

## The Role of Field Status in Data Quality

In any data quality platform, not every field in a dataset requires the same level of attention. Some fields are critical to business operations and need continuous monitoring, while others may be deprecated, irrelevant, or temporarily unavailable. Some fields contain sensitive data that must be protected while still being monitored. Field status provides a mechanism to manage these differences systematically.

Rather than treating all fields equally, Qualytics uses field status to:

- **Control the scope of quality operations** — Only operational fields (active and masked) are profiled and scanned, ensuring that resources are focused on relevant data.
- **Track schema evolution** — When fields appear or disappear from source data, the system automatically updates their status, providing visibility into schema changes.
- **Manage the quality check lifecycle** — Field status transitions trigger automatic actions on associated quality checks, keeping your monitoring configuration consistent with the actual state of your data.
- **Protect sensitive data** — Masked fields remain fully operational for quality monitoring while hiding raw values from API responses, with audit-logged access controls.

## How Field Status Supports Data Quality

Field status plays a direct role in how you manage and maintain data quality across your datasets:

### Focused Quality Monitoring

By excluding fields that are not relevant to your data quality goals, you can concentrate your quality checks on the fields that truly matter. This reduces noise in your anomaly reports and helps your team focus on actionable insights.

For example, if a table contains legacy columns that are no longer populated but still exist in the schema, excluding those fields prevents unnecessary anomaly alerts and keeps your quality dashboards clean.

### Sensitive Data Protection

Masking allows you to protect fields containing sensitive data (PII, financial data, health records) while maintaining full quality monitoring. Masked fields continue to be profiled, scanned, and evaluated by quality checks — the only difference is that their actual values are hidden across the platform by default.

Masking is enforced at every point where field values are surfaced or written:

- **Data Preview** — values are obfuscated and require an explicit reveal action
- **Anomaly Source Records** — values are obfuscated by default; users can toggle reveal per anomaly (all source records for the anomaly are revealed together)
- **Field Profile Histograms** — chart values are obfuscated for masked fields
- **Anomaly Assertion Context** — check detail values are unconditionally obfuscated; no inline reveal is available
- **Export Operation (Field Profiles)** — histogram bucket values are obfuscated in the `_field_profiles_export` file written to the enrichment datastore
- **Materialize Operation** — source record values are obfuscated in container snapshots written to the enrichment datastore

Users with Editor permission can request to reveal values in the surfaces that support reveal (Data Preview and Anomaly Source Records), and every reveal action is recorded in the masking audit log for compliance purposes. Export and materialize operations also support reveal via the `include_masked` API parameter — this is not available in the UI.

### Schema Change Detection

When a field disappears from the source data, Qualytics automatically marks it as **Missing**. This serves as an early warning system for schema changes, allowing you to investigate whether the change was intentional or indicates a problem in your data pipeline.

Common scenarios that trigger the Missing status:

- A column was renamed during a database migration
- A table was restructured and certain fields were removed
- A data source experienced an issue and is returning incomplete schemas
- An upstream ETL process changed its output format

In all these cases, the Missing status gives you immediate visibility without requiring manual monitoring of your data schemas.

### Quality Check Lifecycle Management

Field status directly impacts the lifecycle of quality checks:

- When a field is **excluded**, its associated quality checks are archived, preventing false alerts from running against a field that should not be monitored.
- When a field goes **missing**, its quality checks remain intact, ready to resume when the field reappears. This is because missing is considered a transient state — the field is expected to return.
- When a field is **active** or **masked**, all configured quality checks run normally during scan operations.

This distinction between excluded and missing is intentional: archiving checks for excluded fields prevents unnecessary work, while keeping checks for missing fields avoids the overhead of reconfiguring them when the field returns.

### Computed Field Dependencies

Field status cascades through computed field dependencies. If a source field goes missing or is excluded, any computed fields that depend on it are automatically updated to reflect the same status, ensuring consistency across your data model.

The cascade behavior differs by status:

- **Missing cascade**: If a source field goes missing, its dependent computed fields are also marked as Missing. When the source field returns, the computed fields are restored automatically. Quality checks on computed fields are **not** archived during this transition.
- **Excluded cascade**: If a source field is excluded, its dependent computed fields are also excluded recursively. Quality checks on the computed fields are archived. The computed field definitions are preserved so they can be recovered when the source field is restored.

!!! info
    When restoring an excluded field that has dependent computed fields, the computed output fields can only be restored if **all** of their source fields are active. If any source field is still excluded or missing, the restore operation for the computed field will be blocked.

### Expected Schema Integration

Expected Schema checks receive special treatment during status transitions. When a field is excluded:

- Regular quality checks are **archived** (suspended but preserved)
- Expected Schema checks are **updated** to remove the excluded field from their definition

This ensures that your Expected Schema check always reflects the current set of operational fields, rather than failing because an intentionally excluded field is "missing" from the schema.

## Practical Scenarios

### Scenario 1: Deprecating a legacy field

Your team has decided to stop using the `legacy_customer_id` column. Instead of deleting the column from the database immediately, you exclude the field in Qualytics:

1. The field's quality checks are archived — no more alerts about this column.
2. Computed fields that depend on `legacy_customer_id` are automatically excluded.
3. When your database team eventually drops the column, it does not trigger a Missing status because the field is already excluded.

### Scenario 2: Protecting sensitive data

Your dataset contains a `social_security_number` column that must be monitored for quality but should not be visible anywhere in the platform. You mask the field:

1. Quality checks continue to run — you still detect anomalies in the SSN field.
2. Actual SSN values are obfuscated everywhere in the platform.
3. In Data Preview and Anomaly Source Records, values are hidden by default.
4. When an analyst needs to investigate a specific anomaly, they can reveal the masked values — and that access is audit-logged.

### Scenario 3: Detecting an upstream schema change

After a routine profile operation, you notice that several fields are now marked as **Missing**. Investigation reveals that an upstream team renamed columns during a migration without notifying your team. The Missing status served as an early alert, allowing you to:

1. Identify the affected fields quickly using the Missing tab filter.
2. Coordinate with the upstream team to understand the changes.
3. Update your quality checks to reference the new column names.
4. Exclude the old missing fields once the new columns are configured.

### Scenario 4: Temporary data source outage

A data source experiences a temporary outage, and the next profile operation returns an incomplete schema. Several fields are marked as **Missing**, but their quality checks remain intact. When the data source recovers and the next profile runs, all fields return to **Active** automatically and quality checks resume without any manual intervention.

## Best Practices

| Practice | Rationale |
| :--- | :--- |
| **Mask sensitive fields** | Masking protects sensitive data while maintaining full quality monitoring. Use it for PII, financial data, or any field that should not be freely visible. |
| **Exclude rather than delete** | Excluding preserves field history and allows restoration. Only hard-delete missing fields that were created by mistake and have no quality check references. |
| **Investigate missing fields promptly** | Missing fields may indicate unplanned schema changes or data pipeline issues that require attention. |
| **Use [merge](merge-fields.md) for column renames** | Merging preserves all historical profiles, anomalies, and quality checks under the new column name. |
| **Review excluded fields periodically** | Fields that were excluded may become relevant again as business requirements change. |
| **Re-enable quality checks after restoring** | Archived checks are not automatically restored — always verify that the appropriate checks are re-enabled after restoring a field. |
| **Use status filters to monitor field health** | Regularly review the Missing and Excluded tabs to maintain awareness of your data model's current state. |
