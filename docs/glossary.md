# Glossary

 <a href="anomaly"></a>__Anomaly__: Something that deviates from the standard, normal, or expected. This can be in the form of a single data point, record, or a batch of data

 <a href="accuracy"></a>__Accuracy__: The data represents the real-world values they are expected to model.

 <a href="catalog"></a>__Catalog Operation__: used to read fundamental metadata from a Datastore required for the proper functioning of subsequent Operations such as Profile, Hash and Scan

 <a href="comparison"></a>__Comparison__: An evaluation to determine if the structure and content of the source and target data stores match

 <a href="comparison"></a>__Comparison Runs__: An action to perform a comparison

 <a href="completeness"></a>__Completeness__: Required fields are fully populated.

 <a href="conformity"></a>__Conformity__: Alignment of the content to the required standards, schemas, and formats.

 <a href="connectors"></a>__Connectors__: Components that can be easily connected to and used to integrate with other applications and databases. Common uses include sending and receiving data.

!!! info
    We can connect to any Apache Spark accessible datastore. If you have a data store we don’t yet support, talk to us! We currently support: Files (CSV, JSON, XLSX, Parquet) on Object Storage (S3, Azure Blob, GCS); ETL/ELT Providers (Fivetran, Stitch, Airbyte, Matillion – and any of their connectors!); Data Warehouses (BigQuery, Snowflake, Redshift); Data Pipelining (Airflow, DBT, Prefect), Databases (MySQL, PostgreSQL, MSSQL, SQLite, etc.) and any other JDBC source

 <a href="consistency"></a>__Consistency__: The value is the same across all datastores within the organization.

 <a href="container"></a>__Container (of a Datastore)__: the uniquely named abstractions within a Datastore that hold data adhering to a known schema.  The Containers within a RDBMS are tables, the containers in a filesystem are well formatted files, etc…

 <a href="dataatrest"></a>__Data-at-rest__: Data that is stored in a database, warehouse, file system, data lake, or other data store.

 <a href="drift"></a>__Data Drift__: Changes in a data set’s properties or characteristics over time.

 <a href="datainflight"></a>__Data-in-flight__: Data that is on the move, transporting from one location to another, such as through a message queue, API, or other pipeline

 <a href="datalake"></a>__Data Lake__: ​​A centralized repository that allows you to store all your structured and unstructured data at any scale. (**)

 <a href="dataquality"></a>__Data Quality__: Ensuring data is free from errors, including duplicates, inaccuracies, inappropriate fields, irrelevant data, missing elements, non-conforming data, and poor data entry.

 <a href="check"></a>__Data Quality Check__: aka “Check” is an expression regarding the values of a Container that can be evaluated to determine whether the actual values are expected or not.

 <a href="datastore"></a>__Datastore__: Where data is persisted in a database, file system, or other connected retrieval systems. You can check more in [what is a Data store](/datastores/what-is-datastore).

 <a href="datawarehouse"></a>__Data Warehouse__: A system that aggregates data from different sources into a single, central, consistent data store to support data analysis, data mining, artificial intelligence (AI), and machine learning.

 <a href="distinctness"></a>__Distinctness (of a Field)__: the fraction of distinct values (appear at least once) to total values that appear in a Field

 <a href="enrichment"></a>__Enrichment__: Additional properties that are added to a data set to enhance its meaning. Qualytics enrichment includes whether a record is anomalous, what caused it to be an anomaly, what characteristics it was expected to have, and flags that allow other systems to act upon the data.

 <a href="favorite"></a>__Favorite __: users can mark instances of an abstraction (Field, Container, Datastore, Check, Anomaly, etc..) as a personalized favorite to ensure it ranks higher in default ordering and is prioritized in other personalized views & workflows.

 <a href="firewall"></a>__Firewall__: An application that protects a system from contamination due to inputs, reducing the likelihood of contamination from an outside source. A firewall will quarantine data that is problematic, allowing the user to act upon quarantined items.

 <a href="incremental"></a>__Incremental Identifier - a Field that can be used to group the records in the Table Container into distinct ordered Qualytics Partitions in support of incremental operations upon those partitions__:

* a whole number - then all records with the same partition_id value are considered part of the same partition
* a float or timestamp - then all records between two defined values are considered part of the same partition (the defining values will be set by incremental scan/profile business logic) Since Qualytics Partitions are required to support Incremental Operations, an Incremental Identifier is required for a Table Container to support incremental Operations.

 <a href="incremental"></a>__Incremental Scan Operation __: a Scan Operation where only new records (inserted since the last Scan Operation) are analyzed. The underlying Container must support determining which records are new for incremental scanning to be a valid option for it.

 <a href="inference"></a>__Inference Engine__: after Firewall gathers all the metadata generated by a profiling operation, it feeds that metadata into our Inference Engine. The inference engine then initiates a “true machine learning” (specifically, this is referred to as Inductive Learning) process whereby the available customer data is partitioned into a training set and a testing set.  The engine applies numerous machine learning models & techniques to the training data in an effort to discover well-fitting data quality constraints. Those inferred constraints are then filtered by testing them against the held out testing set & only those that assert true are converted to inferred data quality Checks.

 <a href="metadata"></a>__Metadata__: Data about other data, including descriptions and additional information.

 <a href="object"></a>__Object Storage__: A type of data storage used for handling large amounts of unstructured data managed as objects.

 <a href="operation"></a>__Operation__: the asynchronous (often long running) tasks that operate on Datastores are collectively referred to as “Operations.”  Examples include Catalog, Profile, Hash, and Scan

 <a href="partition"></a>__Partition Identifier__: a Field that can be used by Spark to group the records in a Dataframe into smaller sets that fit within our Spark worker’s memory. The ideal Partition Identifier is an Incremental Identifier of type datetime since that can serve as both but we identify alternatives should that not be available.

 <a href="pipeline"></a>__Pipeline__: A workflow that processes and moves data between systems.

 <a href="precision"></a>__Precision__: Your data is the resolution that is expected- How tightly can you define your data?

 <a href="profile"></a>__Profile Operation __: a Profile Operation where no limits are explicitly set and an attempt is made to analyze every available record in all available Containers. Full Profiles provide the benefit of generating metadata with 100% fidelity at the cost of maximum compute time.

 <a href="profiling"></a>__Profiling__: The process of collecting statistics on the characteristics of a dataset involving examining, analyzing, and reviewing the data.

 <a href="proprietary"></a>__Proprietary Algorithms__: A procedure utilizing a combination of processes, tools, or systems of interrelated connections that are the property of a business or individual in order to solve a problem. (**)

 <a href="quality"></a>__Quality Score__: a proprietary measure of data quality as measured at the Field, Container, Partition, and Datastore level.  Quality Scores include both a spot score that measure the ratio of anomalies in a set at a given time as well as a measure of the change of that ratio versus the average for the last 30 days.

 <a href="qualytics"></a>__Qualytics App__: aka “App” this is the user interface for our Product delivered as a web application

 <a href="qualytics"></a>__Qualytics Deployment__: a single instance of our product (the k8s cluster, postgres database, hub/app/firewall pods, etc…)

 <a href="qualytics"></a>__Qualytics Firewall__: aka “Firewall” this is the layer of our Product that connects to Datastores and directly operates on users’ data.

 <a href="qualytics"></a>__Qualytics Implementation__: a customer’s Deployment plus any associated integrations

 <a href="qualytics"></a>__Qualytics Surveillance Hub__: aka “Hub” this is the layer of our Product that exposes an Application Programming Interface (API).

 <a href="qualytics"></a>__Qualytics Partition__: the smallest grouping of records that can be incrementally processed. For DFS datastores, each file is a Qualytics Partition. For JDBC datastores, partitions are defined by each table’s incremental identifier values.

 <a href="record"></a>__Record (of a Container)__: a distinct set of values for all Fields defined for a Container (e.g. a row of a table)

 <a href="schema"></a>__Schema__: The organization of data in a data store. This could be the columns of a table, the header of a CSV file, the fields in a JSON file, or other structural constraints.

 <a href="schema"></a>__Schema Differences__: Differences in the organization of information between two data stores that are supposed to hold the same content.

 <a href="source"></a>__Source__: The origin of data in a pipeline, migration, or other ELT/ETL process. It’s where data gets extracted.

 <a href="target"></a>__Target__: The destination of data in a pipeline, migration, or other ELT/ETL process. It’s where data gets loaded.

 <a href="third"></a>__Third-party data__: Data acquired from a source outside of your company which may not be controlled by the same data quality processes. You may not have the same level of confidence in the data and it may not be as trustworthy as internally vetted datasets.

 <a href="timeliness"></a>__Timeliness__: It can be calculated as the time between when information should be available and when it is actually available, focused on if data is available when it’s expected.

 <a href="volumetrics"></a>__Volumetrics__: Data has the same size and shape across similar cycles. It includes statistics about the size of a data set including calculations or predictions on the rate of change over time.