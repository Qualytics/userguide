# Understanding DFS

## What is DFS?

A **Distributed File System (DFS)** is a storage architecture that allows data to be stored across multiple machines or locations, while providing access to it as if it were on a single local system. In the context of modern cloud platforms, DFS encompasses cloud object storage services like **Amazon S3**, **Azure Data Lake Storage**, and **Google Cloud Storage** — which store data as objects (files) organized in buckets and folders, supporting formats like Parquet, AVRO, CSV, and JSON.

## How DFS Works in Qualytics

Qualytics uses DFS connectors powered by [Apache Spark](https://spark.apache.org/){:target="_blank"} to connect to cloud object storage and distributed file systems. When you add a DFS datastore, Qualytics:

1. **Establishes a connection** to your storage platform using credentials (access keys, service accounts, service principals, or connection strings).
2. **Walks the directory tree** during the Sync operation — reading files with supported extensions and creating containers based on file metadata and naming patterns.
3. **Reads data through Spark** using native cloud connectors for optimized, parallel file reads across partitions.
4. **Writes enrichment data** (all DFS connectors support enrichment) back to the storage platform to persist scan results, anomalies, and remediation records.

!!! info "Connections and Security"
    For details on connection configuration, authentication methods (Shared Key, Service Principal, IAM roles), and secrets management (HashiCorp Vault integration), see the [How Connections Work](connections/how-it-works.md){:target="_blank"} documentation.

### Data Organization

In DFS datastores, data is organized as:

- **Containers** — Files in a folder that share a common schema. Qualytics automatically groups files with similar naming patterns into a single **globbed container** (e.g., `orders_*.csv`). This grouping process is called [Filename Globbing](dfs-filename-globbing.md){:target="_blank"} and treats each file as a partition of the same logical dataset.
- **Fields** — Columns within each file, detected automatically based on the file format and schema.
- **Records** — Rows of data within each file, analyzed during Profile and Scan operations.

!!! info "Containers"
    For a detailed understanding of how Qualytics manages containers in DFS datastores, see the [Containers Overview](../../container/overview.md){:target="_blank"} documentation.

### Field Type Inference

During the Sync operation, Qualytics infers field types automatically based on the file format:

- **Schema-aware formats** (Parquet, AVRO, ORC, Delta, Iceberg) — Field types are read directly from the file's embedded schema.
- **Schema-less formats** (CSV, JSON) — Qualytics uses **weighted histogram analysis** to infer field types from actual data values, detecting integers, decimals, dates, timestamps, and text fields. Inferred types can be reviewed and overridden manually on each field.

### Multi-Schema Equivalent

DFS datastores do **not** support the multi-schema creation flow (which is designed for JDBC connectors with catalog/schema hierarchy). Each DFS datastore represents a single root path. To monitor multiple buckets or prefixes, create a separate DFS datastore for each one.

## Getting Started

<div class="grid cards" markdown>

-   :material-plus-circle:{ .lg .middle } **Add with New Connection**

    ---

    Create a new DFS datastore by setting up a new connection from scratch.

    [:octicons-arrow-right-24: New Connection](connections/new-connection.md)

-   :material-link-variant:{ .lg .middle } **Add with Existing Connection**

    ---

    Create a new DFS datastore by reusing credentials from an existing connection.

    [:octicons-arrow-right-24: Existing Connection](connections/existing-connection.md)

-   :material-view-list:{ .lg .middle } **Available DFS Connectors**

    ---

    Browse the full list of supported DFS connectors.

    [:octicons-arrow-right-24: View Connectors](available-datastore-connectors.md)

-   :material-connection:{ .lg .middle } **Connections**

    ---

    Configure connection details, authentication, and secrets management.

    [:octicons-arrow-right-24: Connections](connections/introduction.md)

-   :material-file-document-outline:{ .lg .middle } **Supported File Formats**

    ---

    Parquet, AVRO, CSV, JSON, Delta, Iceberg, ORC, and more.

    [:octicons-arrow-right-24: File Formats](dfs-supported-file-formats.md)

-   :material-folder-multiple-outline:{ .lg .middle } **Filename Globbing**

    ---

    How files are grouped into containers and best practices for organizing your data.

    [:octicons-arrow-right-24: Globbing](dfs-filename-globbing.md)

</div>

## Available Operations

Once a DFS datastore is added, you can run the following operations:

| Operation | Description |
| :--- | :--- |
| [Sync](../../source-datastore/operations/sync.md){:target="_blank"} | Walks the directory tree, reads files with supported extensions, and creates containers based on file metadata and naming patterns. Detects new, changed, or removed files incrementally. |
| [Profile](../../source-datastore/operations/profile.md){:target="_blank"} | Analyzes records across containers to compute statistics, detect data patterns, and automatically infer quality checks. |
| [Scan](../../source-datastore/operations/scan.md){:target="_blank"} | Executes quality checks against the data, measures data quality metrics, and detects anomalies at the record and schema levels. |
| [External Scan](../../source-datastore/operations/external-scan.md){:target="_blank"} | Runs scan operations using externally provided data files. |

!!! tip
    The recommended sequence is **Sync → Profile → Scan**. This cycle is repeatable — as your data evolves, re-running these operations keeps your quality checks and anomaly detection up to date.
