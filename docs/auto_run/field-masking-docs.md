# Field Masking Documentation — Auto Run Plan

## Context

Field masking allows data stewards to designate specific fields as sensitive. Once masked:

- Masked field values are replaced with `***MASKED***` everywhere in the platform.
- Controlplane masks `histogram_buckets` in field profile export data before writing to the enrichment datastore.
- Dataplane masks source record values in: scans (dry runs), materialize operations, container reads (data preview), and source record retrieval operations.
- Anomaly assertion context is unconditionally masked for masked fields (no bypass available).
- Revealing masked values requires `include_masked=true` where applicable, gated on Editor-level permission.
- Every reveal action is recorded in the masking audit log.

The existing `mask-a-field.md` and `field-status-faq.md` pages contain accurate baseline content but do not yet cover the full operational surface (export, materialize, dry run, anomaly context) or the "how to reveal" flows in detail.

---

## Tasks

### 1. Update `docs/fields/field-status/managing-field-status/mask-a-field.md`

- [ ] Expand the "What Happens When a Field is Masked" section to explicitly list all surfaces where `***MASKED***` appears:
  - Data Preview (container reads)
  - Anomaly Source Records (scans and dry runs)
  - Field Profile histogram buckets (exported field profiles)
  - Anomaly assertion context (check details, anomaly messages)
  - Materialize operation output (enrichment datastore copy)
  - Export operation field profile output (enrichment datastore)
- [ ] Add a new "Where Masking Is Applied" section (table format) mapping each surface to the operation that produces it and whether reveal is available.
- [ ] Expand the "Viewing Masked Values" section into a dedicated "Revealing Masked Values" section covering:
  - Data Preview: "Show masked values" button
  - Anomaly Source Records: per-record reveal toggle
  - Export / Materialize / Anomaly assertion context: note that these surfaces do NOT support inline reveal (values remain masked in the enrichment datastore output)
- [ ] Add a callout clarifying that anomaly assertion context masking is unconditional — it cannot be bypassed even with Editor permission.
- [ ] Verify the `!!! warning` audit-log callout is present and accurate.
- [ ] Review the "What Happens When a Field is Unmasked" section for completeness — confirm that unmasking restores values in all surfaces listed above.

### 2. Update `docs/fields/field-status/concepts/understanding-field-status.md`

- [ ] In the "Sensitive Data Protection" subsection, expand the description to mention all operation surfaces where masking is enforced (export, materialize, dry run source records, anomaly assertion context).
- [ ] Add a note that field profile histogram buckets are also masked in export output.

### 3. Update `docs/fields/field-status/concepts/field-status-faq.md`

- [ ] Update the "How are masked values protected?" answer to explicitly list all surfaces: Data Preview, Anomaly Source Records, field profile histograms (reads and export), anomaly assertion context, materialize output, and export output.
- [ ] Add a new FAQ entry: "Are masked values protected in Export and Materialize operation outputs?" — answer: yes, histogram buckets are masked in exported field profiles, and source record values are masked in materialize outputs; these cannot be bypassed inline.
- [ ] Add a new FAQ entry: "Are masked values in anomaly details (assertion context) revealable?" — answer: no, anomaly assertion context is unconditionally masked for compliance; reveal is not available in that surface.

### 4. Update `docs/anomalies/source-record.md`

- [ ] Add a "Masked Fields in Source Records" section explaining:
  - Masked field values display as `***MASKED***` by default.
  - Users with Editor permission can toggle reveal on individual records.
  - Every reveal action is audit-logged.
- [ ] Reference the `mask-a-field.md` page for details on managing field masking.

### 5. Update `docs/container/data-preview.md`

- [ ] Add a "Masked Fields in Data Preview" section explaining:
  - Masked field values display as hidden by default.
  - A "Show masked values" button reveals all masked values for the current view.
  - Requires Editor permission; the action is audit-logged.
- [ ] Reference the `mask-a-field.md` page for managing field masking.

### 6. Update `docs/container/enrichment-operation/export-operation.md`

- [ ] Add a "Field Masking and Export" section explaining:
  - When exporting Field Profiles, histogram bucket values for masked fields are replaced with `***MASKED***` in the export output written to the enrichment datastore.
  - The exported file (`_<prefix>_field_profiles_export`) will contain masked histogram data for any fields designated as masked.
  - The export output in the enrichment datastore cannot be "unmasked" — to get unmasked histogram data, the field must first be unmasked in Qualytics before re-running the export.
  - Anomaly and Quality Check exports are not affected by field masking.

### 7. Update `docs/container/enrichment-operation/materialize-operation.md`

- [ ] Add a "Field Masking and Materialize" section explaining:
  - When a Materialize Operation copies source data to the enrichment datastore, values for masked fields are replaced with `***MASKED***` in the materialize output.
  - This applies to every container included in the materialize run.
  - The materialized output in the enrichment datastore will contain masked values — to materialize unmasked data, the field must first be unmasked in Qualytics.

### 8. Update `docs/fields/field-status/concepts/field-status-api.md`

- [ ] Confirm that the `include_masked` parameter is documented on the relevant API endpoints:
  - Container read / data preview endpoint (if exposed publicly)
  - Source record retrieval endpoint
  - Dry run / check operation endpoint (if `include_masked` is a param)
- [ ] If `include_masked` is not yet documented on any of these endpoints, add parameter descriptions and note permission requirements.
- [ ] Verify that the masking audit log API section is complete and accurate.

### 9. (Optional) Create `docs/fields/field-masking-overview.md`

- [ ] Only create this page if the field-status section becomes too long or if stakeholders request a standalone "Field Masking" concept page.
- [ ] If created: cover the full masking surface in one place (where applied, how to reveal, audit log), and update `mkdocs.yml` nav accordingly.
- [ ] Otherwise: the existing `mask-a-field.md` updated in Task 1 is sufficient.

### 10. Review `mkdocs.yml` navigation

- [ ] Check that `mask-a-field.md` is correctly placed in the nav tree under Field Status > Managing Field Status.
- [ ] If a new standalone `field-masking-overview.md` is created (Task 9), add it to the nav.
- [ ] No other nav changes are expected.

### 11. Final consistency pass

- [ ] Search all docs for references to masking to confirm no pages were missed.
- [ ] Confirm `***MASKED***` placeholder text is consistently presented as inline code across all updated pages.
- [ ] Confirm all updated pages reference each other appropriately (cross-links).
- [ ] Run `pre-commit run --all-files` to check for spelling issues.
