# Understanding JDBC

## What is JDBC?

**JDBC (Java Database Connectivity)** is a standard Java API that provides a universal interface for connecting to relational databases. It acts as a bridge between applications and databases, allowing programs to execute SQL queries, retrieve results, and manage data — regardless of which database vendor is being used.

JDBC has been the industry standard for database connectivity since its introduction in 1997 and is supported by virtually every relational database management system (RDBMS) available today.

!!! info "Learn more"
    For a deeper understanding of the JDBC standard, see the [JDBC Overview](https://docs.oracle.com/javase/tutorial/jdbc/overview/index.html){:target="_blank"} from Oracle's official Java documentation.

## How JDBC Works in Qualytics

Qualytics uses JDBC connectors powered by [Apache Spark](https://spark.apache.org/){:target="_blank"} to connect to relational databases. When you add a JDBC datastore, Qualytics:

1. **Establishes a secure connection** to your database using the credentials and connection properties you provide (host, port, username, password, database, schema).
2. **Discovers your schema** by reading the database catalog — tables, views, columns, and data types are automatically detected during the Sync operation.
3. **Reads data through Spark** using optimized JDBC queries, enabling parallel reads across partitions for large datasets.
4. **Writes enrichment data** (for connectors with enrichment support) back to the database to persist scan results, anomalies, and remediation records.

Because Qualytics is built on Apache Spark, additional JDBC-accessible databases beyond the verified list may be technically compatible — contact us to evaluate feasibility for your specific datastore.

### Data Organization

In JDBC datastores, data is organized as:

- **Containers** — Tables and views in the database. Each container represents a structured dataset that Qualytics can profile, scan, and monitor.
- **Fields** — Columns within each table/view. Qualytics detects field names, data types, and constraints automatically.
- **Records** — Rows of data within each container, analyzed during profile and scan operations.

!!! info "Containers"
    For a detailed understanding of how Qualytics manages containers in JDBC datastores, see the [Containers Overview](../../container/overview.md){:target="_blank"} documentation.

### Field Type Inference

During the Sync operation, Qualytics employs **weighted histogram analysis** to automatically infer field types. This advanced method ensures accurate detection of data types within the JDBC datastore — including distinguishing between integers, decimals, dates, timestamps, and text fields — enhancing the precision of data profiling and quality checks.

### Multi-Schema Support

JDBC datastores support **multi-schema creation**, allowing you to discover and select multiple schemas from a single connection and create all corresponding source datastores in one step. This eliminates the need to add each schema individually.

!!! info "Multiple-Schema"
    For detailed instructions on multi-schema creation, refer to the [Multiple-Schema](multi-schema/overview.md){:target="_blank"} documentation.

## Getting Started

!!! info "Add a JDBC Datastore"
    To add a new JDBC datastore, follow the step-by-step guide in the [Add Datastore with a New Connection](connections/new-connection.md){:target="_blank"} or [Add Datastore with an Existing Connection](connections/existing-connection.md){:target="_blank"} documentation.

!!! info "Available JDBC Connectors"
    For the full list of supported JDBC connectors, see the [Available Datastore Connectors](available-datastore-connectors.md){:target="_blank"} page.

!!! info "Connections"
    To learn how to configure connection details (host, port, credentials, secrets management), see the [Connections Overview](connections/overview-of-a-connection.md){:target="_blank"} documentation.

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
