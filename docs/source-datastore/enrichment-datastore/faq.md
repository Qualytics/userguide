# Datastore Enrichment FAQ

Answers to common questions about linking, unlinking, and managing enrichment datastores specifically on source datastores in Qualytics.

!!! info "General Enrichment Datastores"
    For questions about enrichment datastore concepts, table types, and schema details (not specific to source datastores), see the [Enrichment Datastores](../../enrichment/overview-of-an-enrichment-datastore.md){:target="_blank"} documentation.

## Linking

### Do I need to link an enrichment datastore to use Qualytics?

No. You can run **Sync**, **Profile**, and **Scan** operations without an enrichment datastore. However, without one linked, scan results and anomalies will only exist within the Qualytics platform — they won't be persisted in your own infrastructure.

### Can I link an enrichment datastore after creating my source datastore?

Yes. You can link an enrichment datastore at any time — either during datastore creation or afterward through the [Link Enrichment Datastore](../managing-datastores/link-enrichment.md){:target="_blank"} flow.

### Can multiple source datastores share the same enrichment datastore?

Yes. Multiple source datastores can link to the same enrichment datastore. Each source datastore maintains its own settings (prefix, source record limit, remediation strategy), so there is no conflict — even when writing to the same enrichment target.

### Which connectors support enrichment?

Not all connectors can be used as enrichment datastores. Only datastores created with `enrichment_only=true` and a connector that supports write-back capabilities can be used as enrichment targets. See the [Supported Enrichment Datastores](../../enrichment-support/supported-enrichment-datastores.md){:target="_blank"} page for the full list.

## Settings

### What is the enrichment prefix?

The prefix is added to all enrichment table/file names created for a source datastore. It is automatically normalized to snake_case with a leading underscore (e.g., `Analytics Bronze` becomes `_analytics_bronze`). Maximum length is 60 characters.

### Do I need a unique prefix for each source datastore?

Yes. Each source datastore linked to the same enrichment datastore **must have a unique prefix**. The system does **not** validate prefix uniqueness at link time — if two source datastores use the same prefix, their enrichment tables will collide and data will be mixed or overwritten silently. It is your responsibility to ensure prefixes are unique.

### What happens if I change the prefix after linking?

Qualytics will start writing to **new** enrichment tables using the updated prefix. The old tables (with the previous prefix) are **not renamed or deleted** — they remain in the enrichment datastore as orphaned tables. If you no longer need the old data, manually drop the old tables using your database tools.

### What does the remediation strategy control?

It controls whether and how anomalous source data is replicated to the enrichment datastore during Scan:

- **None** (default) — No source records are written. Only anomaly metadata is tracked within Qualytics.
- **Append** — Anomalous records are appended after each scan, building a historical audit trail.
- **Overwrite** — Enrichment tables are replaced with the latest anomalous records.

### What is the "Maximum Source Examples per Anomaly"?

It controls how many actual source data rows are written to the enrichment datastore when a quality check fails. Default is 10. Range: 1 to 1,000,000,000. For practical recommendations on which values to use, see the [Source Examples: Practical Recommendations](introduction.md#source-examples-practical-recommendations){:target="_blank"} section.

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

### Can I re-link the same enrichment datastore after unlinking?

Yes. Unlinking only breaks the connection — it does not delete any data. If you re-link the **same** enrichment datastore with the **same prefix**, future Scans will continue writing to the existing enrichment tables as if nothing changed.

### Can I switch to a different enrichment datastore?

Yes, but you must first **unlink** the current one and then **link** the new one. You cannot directly swap enrichment datastores.

### How do I clean up enrichment tables after unlinking?

Qualytics does not automatically delete enrichment tables when you unlink. If you want to remove the historical data, you must **manually drop** the enrichment tables (e.g., `_prefix_check_metrics`, `_prefix_failed_checks`, `_prefix_source_records`, `_prefix_scan_operations`) directly in the enrichment datastore using your database tools.

### What happens to existing anomalies in Qualytics if I unlink?

Anomalies tracked within Qualytics are **not affected** by unlinking. They remain visible in the UI and API. Only the enrichment datastore stops receiving new data — anomalies continue to be detected and tracked internally.

### Why can't I unlink my enrichment datastore?

You cannot unlink if the source datastore has active **Export** or **Materialize** operations in flows or scheduled operations. Remove those operations first, then try unlinking again.

## Storage

### How much storage does enrichment use?

Storage depends on your configuration. As a rough estimate:

- **Default settings** (10 source examples, None remediation, daily scans) — Typically a few MB per scan for a moderate datastore (50 tables, ~100 anomalies per scan).
- **High source examples** (1,000+ per anomaly, Append remediation) — Can grow to hundreds of MB or GB over months for large datastores with many recurring anomalies.
- **Overwrite remediation** — Bounded storage since data is replaced each scan, typically similar in size to a single Append cycle.

Start with the default settings and increase as needed. Monitor storage using your database tools.

### How do I monitor how much storage my enrichment datastore is using?

Qualytics does not provide built-in storage monitoring for enrichment datastores. Use your database or cloud provider's native tools to monitor table sizes (e.g., `pg_total_relation_size` for PostgreSQL, `INFORMATION_SCHEMA.TABLES` for Snowflake, S3 bucket metrics for DFS).

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

### What permissions do I need?

- **Linking** and **editing settings** requires the **Member** user role and **Editor** team permission on the source datastore.
- **Unlinking** requires the **Admin** user role (no team permission check).
- **Viewing** enrichment info requires the **Member** user role and **Reporter** team permission.

See the [Permissions](permissions.md){:target="_blank"} page for the full matrix.

## Troubleshooting

### My Scan failed with an enrichment error. What should I check?

Common causes:

- **No enrichment datastore linked** — If the remediation strategy is set to Append or Overwrite but no enrichment datastore is linked, the Scan will fail. Link an enrichment datastore or set the strategy to None.
- **Prefix conflict** — If two source datastores use the same prefix on the same enrichment datastore, writes may fail or produce unexpected results. Ensure each prefix is unique.
- **Write permissions** — The enrichment datastore credentials must have write (DDL) permissions on the target schema/bucket. Verify that the enrichment connection can create and write to tables.
- **Enrichment datastore offline** — If the enrichment target is unreachable, the Scan may fail or complete with warnings. Check the enrichment datastore connection status.

### My enrichment tables have a different schema than expected. What happened?

Qualytics manages the enrichment table schema automatically. If the schema has changed between platform versions (e.g., new columns added to `_failed_checks`), Qualytics applies DDL changes automatically during the next Scan. If a table cannot be altered (e.g., due to permissions), the Scan may fail — ensure the enrichment connection has DDL permissions (CREATE, ALTER, INSERT).

## API

### Can I link and configure enrichment in a single API call?

No. Linking uses `PATCH /api/datastores/{id}/enrichment/{enrich_id}` and configuring settings uses `PUT /api/datastores/{id}`. These are two separate endpoints — you need two requests. See the [API](api.md){:target="_blank"} page for examples of both.
