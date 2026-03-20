# Understanding Field Status

Field Status is a property assigned to every field in Qualytics that determines how the platform interacts with it. It acts as a lifecycle indicator, controlling whether a field is included in profiling (collecting metadata and statistics), scanning (detecting anomalies), and quality check evaluations — and whether its values are visible or hidden.

Understanding field status is essential for managing data quality effectively, as it directly influences which fields are monitored, how schema changes are detected, how quality checks behave over time, and how sensitive data is protected.

## The Role of Field Status in Data Quality

In any data quality platform, not every field in a dataset requires the same level of attention. Some fields are critical to business operations and need continuous monitoring, while others may be deprecated, irrelevant, or temporarily unavailable. Some fields contain sensitive data that must be protected while still being monitored. Field status provides a mechanism to manage these differences systematically.

Rather than treating all fields equally, Qualytics uses field status to:

- **Control the scope of quality operations** — Only operational fields (active and masked) are profiled and scanned, ensuring that resources are focused on relevant data.
- **Track schema evolution** — Each time a profile operation runs, Qualytics compares the source fields against the ones it already knows about and updates their statuses accordingly, giving you a clear picture of how your schema has changed.
- **Manage the quality check lifecycle** — Field status transitions trigger automatic actions on associated quality checks, keeping your monitoring configuration consistent with the actual state of your data.
- **Protect sensitive data** — Masked fields remain fully operational for quality monitoring while hiding raw values from API responses, with audit-logged access controls.

## How Field Status Supports Data Quality?

Field status plays a direct role in how you manage and maintain data quality across your datasets:

### Focused Quality Monitoring

By excluding fields that are not relevant to your data quality goals, you can concentrate your quality checks on the fields that truly matter. This reduces noise in your anomaly reports and helps your team focus on actionable insights.

For example, if a table contains legacy columns that are no longer populated but still exist in the schema, excluding those fields prevents unnecessary anomaly alerts and keeps your quality dashboards clean.

### Sensitive Data Protection

Masking allows you to protect fields containing sensitive data (PII, financial data, health records) while maintaining full quality monitoring. Masked fields continue to be profiled, scanned, and evaluated by quality checks — the only difference is that their actual values are hidden across the platform by default.

Users with Editor permission can request to view unmasked values when needed, and every reveal action is recorded in the masking audit log for compliance purposes.

### Schema Change Detection

Each time a profile runs, Qualytics compares the fields it finds in the source against the ones it already knows about. If a previously active field is no longer present, it is marked as **Missing** — a clear signal that something has changed in your data pipeline or schema.

!!! info
    Qualytics does not monitor source schemas in real time. The Missing status is assigned during profile operations, whether those are scheduled or triggered manually. If your source changes between profiles, Qualytics won't know until the next profile runs.

Common scenarios that lead to the Missing status include:

- A column was renamed during a database migration
- A table was restructured and certain fields were removed
- A data source experienced an issue and returned an incomplete schema
- An upstream ETL process changed its output format

In each case, the next profile run reveals the change — without you having to manually compare schemas.

### Quality Check Lifecycle Management

Field status directly impacts the lifecycle of quality checks:

- When a field is **excluded**, its associated quality checks are archived, preventing false alerts from running against a field that should not be monitored.
- When a field goes **missing**, its quality checks remain intact, ready to resume when the field reappears. This is because missing is considered a transient state — the field is expected to return.
- When a field is **active** or **masked**, all configured quality checks run normally during scan operations.

This distinction between excluded and missing is intentional: archiving checks for excluded fields prevents unnecessary work, while keeping checks for missing fields ensures scans surface failures when a referenced field is no longer present—acting as a signal to users that the schema has changed.

### Computed Field Dependencies

Field status cascades through computed field dependencies, though the timing depends on what triggered the change. When a user excludes a source field, its dependent computed fields are excluded immediately. When a profile operation marks a source field as Missing, those same computed fields are also marked as Missing within that same run.

The cascade behavior differs by status:

- **Missing cascade**: When a profile marks a source field as Missing, its dependent computed fields are marked as Missing in the same run. If the source field reappears in a later profile, both the source and its computed dependents are restored automatically. Quality checks on computed fields are **not** archived during this transition.
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
3. When your database team eventually drops the column, the next profile operation will not mark it as Missing because the field is already excluded.

### Scenario 2: Protecting sensitive data

Your dataset contains a `social_security_number` column that must be monitored for quality but should not be visible anywhere in the platform. You mask the field:

1. Quality checks continue to run — you still detect anomalies in the SSN field.
2. Actual SSN values are replaced with `***MASKED***` everywhere in the platform.
3. In Data Preview and Anomaly Source Records, values are hidden by default.
4. When an analyst needs to investigate a specific anomaly, they can reveal the masked values — and that access is audit-logged.

### Scenario 3: Detecting an upstream schema change

After a routine profile operation, you notice that several fields are now marked as **Missing**. Investigation reveals that an upstream team renamed columns during a migration without notifying your team. The Missing status served as an early alert, allowing you to:

1. Identify the affected fields quickly using the Missing tab filter.
2. Coordinate with the upstream team to understand the changes.
3. Update your quality checks to reference the new column names.
4. Exclude the old missing fields once the new columns are configured.

## Best Practices

| Practice | Rationale |
| :--- | :--- |
| **Mask sensitive fields** | Masking protects sensitive data while maintaining full quality monitoring. Use it for PII, financial data, or any field that should not be freely visible. |
| **Exclude rather than delete** | Excluding preserves field history and allows restoration. Only hard-delete missing fields that were created by mistake and have no quality check references. |
| **Investigate missing fields promptly** | Missing fields may indicate unplanned schema changes or data pipeline issues that require attention. |
| **Use [merge](merge-fields.md){:target="_blank"} for column renames** | Merging preserves all historical profiles, anomalies, and quality checks under the new column name. |
| **Review excluded fields periodically** | Fields that were excluded may become relevant again as business requirements change. |
| **Re-enable quality checks after restoring** | Archived checks are not automatically restored — always verify that the appropriate checks are re-enabled after restoring a field. |
| **Use status filters to monitor field health** | Regularly review the Missing and Excluded tabs to maintain awareness of your data model's current state. |
