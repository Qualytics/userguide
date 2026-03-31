# Datastore Enrichment FAQ

Answers to common questions about linking, unlinking, and managing enrichment datastores specifically on source datastores in Qualytics.

!!! info "General Enrichment Datastores"
    For questions about enrichment datastore concepts, table types, and schema details (not specific to source datastores), see the [Enrichment Datastores](../../enrichment/overview-of-an-enrichment-datastore.md){:target="_blank"} documentation.

## Linking

### Do I need to link an enrichment datastore to use Qualytics?

No. You can run **Sync**, **Profile**, and **Scan** operations without an enrichment datastore. However, without one linked, scan results and anomalies will only exist within the Qualytics platform — they won't be persisted in your own infrastructure.

### Can I link an enrichment datastore after creating my source datastore?

Yes. You can link an enrichment datastore at any time — either during datastore creation or afterward through the [Link Enrichment Datastore](../managing-datastores/link-enrichment.md) flow.

### Can multiple source datastores share the same enrichment datastore?

Yes. Multiple source datastores can link to the same enrichment datastore. Each source datastore maintains its own settings (prefix, source record limit, remediation strategy), so there is no conflict — even when writing to the same enrichment target.

### Do I need a unique prefix for each source datastore?

Yes. Each source datastore linked to the same enrichment datastore **must have a unique prefix** to avoid table name conflicts in the enrichment target.

### Can I link any datastore as an enrichment datastore?

No. Only datastores created with `enrichment_only=true` can be used as enrichment targets. Additionally, the connector must support write-back capabilities. See the [Supported Enrichment Datastores](../../enrichment-support/supported-enrichment-datastores.md){:target="_blank"} page for the full list.

## Settings

### What is the enrichment prefix?

The prefix is added to all enrichment table/file names created for a source datastore. It is automatically normalized to snake_case with a leading underscore (e.g., `Analytics Bronze` becomes `_analytics_bronze`). Maximum length is 60 characters.

### What does the remediation strategy control?

It controls whether and how anomalous source data is replicated to the enrichment datastore during Scan:

- **None** (default) — No source records are written. Only anomaly metadata is tracked within Qualytics.
- **Append** — Anomalous records are appended after each scan, building a historical audit trail.
- **Overwrite** — Enrichment tables are replaced with the latest anomalous records.

### What is the "Maximum Source Examples per Anomaly"?

It controls how many actual source data rows are written to the enrichment datastore when a quality check fails. Default is 10. Range: 1 to 1,000,000,000.

### What is the "Maximum Record Anomalies per Check"?

It controls how many individual anomalies can be created per quality check before they are grouped into a single rolled-up anomaly. Default is 10. Range: 1 to 1,000.

### Can I change enrichment settings after linking?

Yes. You can modify the prefix, source record limit, remediation strategy, and rollup threshold at any time. Changes take effect on the next Scan operation.

## Unlinking

### What happens when I unlink an enrichment datastore?

Three things happen:

1. The remediation strategy is automatically reset to **None**.
2. No new enrichment data will be written during future Scans.
3. **Historical enrichment data is preserved** — existing tables in the enrichment datastore are not deleted.

### Can I switch to a different enrichment datastore?

Yes, but you must first **unlink** the current one and then **link** the new one. You cannot directly swap enrichment datastores.

### Why can't I unlink my enrichment datastore?

You cannot unlink if the source datastore has active **Export** or **Materialize** operations in flows or scheduled operations. Remove those operations first, then try unlinking again.

### Who can unlink an enrichment datastore?

Only users with the **Admin** role can unlink. See the [Permissions](permissions.md) page for the full matrix.

## Operations

### What happens during a Scan when an enrichment datastore is linked?

During a Scan with an enrichment datastore linked:

1. Quality checks are executed against the source data.
2. Anomalies are detected from failed checks.
3. Source record examples (up to the configured limit) are written to the enrichment datastore.
4. If remediation strategy is Append or Overwrite, anomalous source tables are replicated.

### Can I run a Scan with remediation strategy other than "None" without an enrichment datastore?

No. Qualytics will return an error. You must either link an enrichment datastore or set the remediation strategy to `None`.

### Does the enrichment datastore affect Sync or Profile operations?

No. The enrichment datastore is only used during **Scan** operations. Sync and Profile operate independently.

## Permissions

### Who can link an enrichment datastore?

Users with at least **Member** role and **Editor** team permission on the source datastore. See the [Permissions](permissions.md) page for details.

### Who can change enrichment settings?

Users with at least **Member** role and **Editor** team permission on the source datastore.

## API

### Is there an API to link an enrichment datastore?

Yes. Use `PATCH /api/datastores/{id}/enrichment/{enrich_store_id}` to link. See the [API](api.md) page for examples.

### Is there an API to update enrichment settings?

Yes. Use `PUT /api/datastores/{id}` with the enrichment fields (prefix, source record limit, remediation strategy, rollup threshold). See the [API](api.md#update-enrichment-settings) page for examples.
