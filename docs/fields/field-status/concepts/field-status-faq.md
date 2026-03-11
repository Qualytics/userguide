# Field Status FAQ

#### What is the difference between active and masked?

Both are **operational** statuses — profiling (collecting metadata and statistics), scanning (detecting anomalies), and quality checks run normally for both. The only difference is that masked field values are hidden across the platform by default (replaced with `***MASKED***`). Users with Editor permission can reveal masked values, and every access is audit-logged.

#### What happens to my quality checks when I mask a field?

Nothing — quality checks continue to run normally. Masking only affects the visibility of values across the platform (Data Preview, Anomaly Source Records, and integrations). It has no impact on profiling, scanning, or quality check execution.

#### What happens to my quality checks when I exclude a field?

All associated quality checks (except Expected Schema) are archived. Expected Schema checks are updated to remove the excluded field. The checks are not deleted, but they will no longer run during scan operations.

#### Can I restore archived quality checks after restoring a field?

No, restoring a field does not automatically restore its archived quality checks. You will need to manually re-enable any checks that were archived during exclusion.

#### What is the difference between excluding and deleting a field?

Excluding a field sets its status to **Excluded** and archives its quality checks, but the field and its history are preserved. You can restore it later. Permanently deleting a field removes it entirely and is only allowed for **missing** fields and **computed fields** that have never been referenced by any quality checks.

#### Which fields can be excluded?

Only **active** and **masked** fields can be excluded. Missing fields, computed fields, sub-fields (children of complex types), and fields configured as container identifiers cannot be excluded.

#### Which fields can be permanently deleted?

Only **missing** fields and **computed fields** can be permanently deleted. Additionally, the field must have never been referenced by any quality check (including past references).

#### How do I know if a field has changed status?

Fields display visual status indicators in the field listing. Masked fields show an amber shield icon, missing fields show a warning icon (yellow/orange), and excluded fields show a negative icon (red). You can also use the [status tabs](../managing-field-status/filtering-by-status.md) to filter and view fields by their current status.

#### Will a missing field affect my data quality score?

Missing fields are not included in profiling or scanning operations, so they do not directly affect new quality score calculations. However, any previously detected anomalies on the field remain in the system.

#### What happens if a missing field reappears in my data?

The field is automatically restored to **Active** status during the next profile operation. Its quality checks resume running normally without any manual intervention.

#### Can I manually restore a missing field?

No, a missing field cannot be manually restored. It is automatically restored to **Active** when the field reappears in the source data during a subsequent profile operation. If the field will not reappear, you can use the [merge](merge-fields.md) operation if the field was renamed.

#### Does excluding a field affect computed fields that depend on it?

Yes. When you exclude a field, any computed fields that use it as a source are also excluded recursively. This ensures that computed fields do not reference inactive data. The computed field definitions are preserved so they can be recovered when the source field is restored.

#### How does field status interact with Expected Schema checks?

Expected Schema checks are treated differently from other quality checks. When a field is excluded, the Expected Schema check is updated to remove that field from its definition rather than being archived entirely. This keeps the schema check accurate for the remaining operational fields.

#### Can I prevent a field from being automatically marked as Missing?

No, the Missing status is automatically assigned by the system during profiling when a field is not found in the source data. This behavior cannot be overridden. However, if the field reappears in a subsequent profile, it will be automatically restored to Active.

#### What happens when I merge two fields?

The source field (old, with history) adopts the target field's name, and the target field record is removed. All historical field profiles, anomalies, and quality checks from both fields are preserved under the merged field. The merged field is set to **Active** status. For more details, see [Merge Fields](merge-fields.md).

#### What happens to container identifiers when a field goes missing?

If a field that is configured as the container's incremental field or partition field goes missing, that container identifier is automatically cleared to prevent errors in subsequent operations.

#### Can computed fields be masked?

Yes. Computed fields are fully operational fields, so they can be masked just like regular fields. Masking a computed field hides its output values across the platform while keeping the transformation and quality checks running normally.

#### Who can view masked field values?

Users with **Editor** permission or above can request to view unmasked values. Every reveal action is recorded in the masking audit log with the user identity, timestamp, IP address, and the specific fields and resources accessed.

#### Where can I view the masking audit log?

Administrators can access the masking audit log to review all masked value reveal actions. The log records the user identity, timestamp, IP address, and the specific fields and resources accessed for each reveal event. It can be filtered by user, action type, resource, and date range.

#### How are masked values protected?

Masked field values are automatically hidden everywhere in the platform — including Data Preview, Anomaly Source Records, field profile histograms, and external integrations. The platform ensures values are protected at multiple stages of data processing.

#### Can I manage field status via API?

Yes. All field status operations — masking, excluding, restoring, deleting, and merging — are available through the Qualytics API. You can also perform bulk operations to update multiple fields at once. See the [Field Status API](field-status-api.md) page for endpoints, parameters, and examples.

#### Can I mask or exclude multiple fields at once?

Yes. The platform supports bulk operations for updating, excluding, and restoring fields. You can change the status of multiple fields in a single API request using the bulk endpoints. See the [Field Status API](field-status-api.md) for details.

#### Can I rename a field that is excluded or missing?

No. Only **active** and **masked** fields can be renamed. Excluded and missing fields must first be restored to active status before they can be renamed.
