# Understanding DFS

## What is DFS?

A **Distributed File System (DFS)** is a storage architecture that allows data to be stored across multiple machines or locations, while providing access to it as if it were on a single local system. DFS splits files into chunks and distributes them across nodes, enabling scalable storage, fault tolerance through replication, and parallel access for high-performance data processing.

In the context of modern cloud platforms, DFS encompasses cloud object storage services like **Amazon S3**, **Azure Data Lake Storage**, and **Google Cloud Storage** — which store data as objects (files) organized in buckets and folders, supporting formats like Parquet, AVRO, CSV, and JSON.

!!! info "Learn more"
    For a deeper understanding of distributed file systems, see [Distributed File System](https://learn.microsoft.com/en-us/windows/win32/dfs/distributed-file-system){:target="_blank"} on Microsoft Learn.

## How DFS Works in Qualytics

Qualytics uses DFS connectors powered by [Apache Spark](https://spark.apache.org/){:target="_blank"} to connect to cloud object storage and distributed file systems. When you add a DFS datastore, Qualytics:

1. **Establishes a secure connection** to your storage platform using credentials (access keys, service accounts, or connection strings).
2. **Walks the directory tree** during the Sync operation — reading files with supported extensions and creating containers based on file metadata and naming patterns.
3. **Reads data through Spark** using native cloud connectors for optimized, parallel file reads across partitions.
4. **Writes enrichment data** (all 3 DFS connectors support enrichment) back to the storage platform to persist scan results, anomalies, and remediation records.

### Data Organization

In DFS datastores, data is organized as:

- **Containers** — Files in a folder that share a common schema. Qualytics automatically groups files with similar naming patterns into a single globbed container (e.g., `orders_*.csv`).
- **Fields** — Columns within each file, detected automatically based on the file format and schema.
- **Records** — Rows of data within each file, analyzed during profile and scan operations.

!!! info "Containers"
    For a detailed understanding of how Qualytics manages containers in DFS datastores, see the [Containers Overview](../../container/overview.md){:target="_blank"} documentation.

## Getting Started

!!! info "Add a DFS Datastore"
    To add a new DFS datastore, follow the step-by-step guide for your connector: [Amazon S3](amazon-s3.md){:target="_blank"}, [Azure Data Lake Storage](azure-datalake-storage.md){:target="_blank"}, or [Google Cloud Storage](google-cloud-storage.md){:target="_blank"}.

!!! info "Available DFS Connectors"
    For the full list of supported DFS connectors, see the [Available Datastore Connectors](available-datastore-connectors.md){:target="_blank"} page.

!!! info "Connections"
    To learn how to configure connection details (access keys, service accounts, connection strings), see the [Connections Overview](connections/overview-of-a-connection.md){:target="_blank"} documentation.

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

## Deep Dive

!!! info "Supported File Formats"
    Qualytics supports 14 file formats including AVRO, Parquet, CSV, JSON, Delta, Iceberg, and more. See the [Supported File Formats](dfs-supported-file-formats.md){:target="_blank"} page for the full list.

!!! info "Filename Globbing"
    Learn how Qualytics automatically groups files with similar naming patterns into containers, and best practices for organizing your files. See the [Filename Globbing and Container Formation](dfs-filename-globbing.md){:target="_blank"} page.
