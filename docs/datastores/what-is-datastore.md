# What is a Data Store?

* A `Data Store` can be any Apache Spark-compatible data source, such as:
    1. Traditional `RDBMS`.
    2. Raw files (`CSV`, `XLSX`, `JSON`, `Avro`, `Parquet`) on:
        2.1 AWS S3.
        2.2 Azure Blob Storage.
        2.3 GCP Cloud Storage.
        2.4 streaming data such as Kafka.
* 
A `Data Store` is a medium holding structured data. Qualytics supports Spark-compatible Data Stores via the conceptual layers depicted below

![Screenshot](../assets/what-is/qualytics-architecture.png)