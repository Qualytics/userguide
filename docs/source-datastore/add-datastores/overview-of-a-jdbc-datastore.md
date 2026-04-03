# Understanding JDBC

## What is JDBC?

**JDBC (Java Database Connectivity)** is a standard Java API that provides a universal interface for connecting to relational databases. It acts as a bridge between applications and databases, allowing programs to execute SQL queries, retrieve results, and manage data — regardless of which database vendor is being used.

## How JDBC Works in Qualytics

Qualytics uses JDBC connectors powered by [Apache Spark](https://spark.apache.org/){:target="_blank"} to connect to relational databases. When you add a JDBC datastore, Qualytics:

1. **Establishes a connection** to your database using the credentials and connection properties you provide (host, port, username, password, database, schema).
2. **Discovers your schema** by reading the database catalog — tables, views, columns, and data types are automatically detected during the Sync operation.
3. **Reads data through Spark** using optimized JDBC queries, enabling parallel reads across partitions for large datasets.
4. **Writes enrichment data** (for connectors with enrichment support) back to the database to persist scan results, anomalies, and remediation records.

!!! info "Connections and Security"
    For details on connection configuration, authentication methods (Basic, Keypair, Service Principal, OAuth), and secrets management (HashiCorp Vault integration), see the [How Connections Work](connections/how-it-works.md){:target="_blank"} documentation.

### Data Organization

In JDBC datastores, data is organized as:

- **Containers** — Tables and views in the database. Each container represents a structured dataset that Qualytics can profile, scan, and monitor.
- **Fields** — Columns within each table/view. Qualytics detects field names, data types, and constraints automatically.
- **Records** — Rows of data within each container, analyzed during Profile and Scan operations.

!!! info "Containers"
    For a detailed understanding of how Qualytics manages containers in JDBC datastores, see the [Containers Overview](../../container/overview.md){:target="_blank"} documentation.

### Field Type Inference

During the Sync operation, Qualytics uses **weighted histogram analysis** to infer field types automatically. This detects data types such as integers, decimals, dates, timestamps, and text fields based on actual data distribution — not just the declared database column type. Inferred types can be reviewed and overridden manually on each field.

### Multi-Schema Support

JDBC datastores support **multi-schema creation**, allowing you to discover and select multiple schemas from a single connection and create a separate source datastore for each selected schema in one step. This eliminates the need to add each schema individually.

!!! info "Multiple-Schema"
    For detailed instructions on multi-schema creation, refer to the [Multiple-Schema](multi-schema/overview.md){:target="_blank"} documentation.

## Getting Started

<div class="grid cards" markdown>

-   :material-plus-circle:{ .lg .middle } **Add with New Connection**

    ---

    Create a new JDBC datastore by setting up a new connection from scratch.

    [:octicons-arrow-right-24: New Connection](connections/new-connection.md)

-   :material-link-variant:{ .lg .middle } **Add with Existing Connection**

    ---

    Create a new JDBC datastore by reusing credentials from an existing connection.

    [:octicons-arrow-right-24: Existing Connection](connections/existing-connection.md)

-   :material-view-list:{ .lg .middle } **Available JDBC Connectors**

    ---

    Browse the full list of supported JDBC connectors and multi-schema support.

    [:octicons-arrow-right-24: View Connectors](available-datastore-connectors.md)

-   :material-connection:{ .lg .middle } **Connections**

    ---

    Configure connection details, authentication, and secrets management.

    [:octicons-arrow-right-24: Connections](connections/introduction.md)

</div>

## Available Operations

Once a JDBC datastore is added, you can run the following operations to manage and ensure data quality:

| Operation | Description |
| :--- | :--- |
| [Sync](../../source-datastore/operations/sync.md){:target="_blank"} | Discovers tables, views, and fields from your database. Detects new, changed, or removed containers incrementally. This is always the first operation after adding a datastore. |
| [Profile](../../source-datastore/operations/profile.md){:target="_blank"} | Analyzes records across containers to compute statistics, detect data patterns, and automatically infer quality checks using the Qualytics Inference Engine. |
| [Scan](../../source-datastore/operations/scan.md){:target="_blank"} | Executes quality checks against the data, measures data quality metrics, and detects anomalies at the record and schema levels. |
| [External Scan](../../source-datastore/operations/external-scan.md){:target="_blank"} | Runs scan operations using externally provided data files instead of reading directly from the database. |

!!! tip
    The recommended sequence is **Sync → Profile → Scan**. This cycle is repeatable — as your data evolves, re-running these operations keeps your quality checks and anomaly detection up to date.
