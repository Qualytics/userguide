# Data Sources

The Qualytics platform connects to your enterprise data sources through "Datastores" - our unified connection framework that enables organizations to:
- Connect to any Apache Spark-compatible data source
- Support both traditional databases and modern object storage
- Profile and monitor structured data across your ecosystem
- Maintain secure, performant data access
- Scale data quality operations across diverse data platforms
- Centralize data quality management across sources

These data source integrations ensure comprehensive quality management across your entire data landscape, regardless of where your data resides.

## Understanding Datastores

A Datastore in Qualytics represents any structured data source, including:
- Traditional relational databases (RDBMS)
- Raw files (CSV, XLSX, JSON, Avro, Parquet)
- Cloud storage platforms (AWS S3, Azure Blob Storage, GCP Cloud Storage)

Qualytics integrates with these data sources through a layered architecture:

![Screenshot](../assets/datastores/what-is/qualytics-architecture.png)

## Configuring Data Sources

Start connecting your data sources by adding a new Datastore:

1. Navigate to the Datastores tab in the main menu
2. Click the Add Source Datastore button:

![Screenshot](../assets/datastores/what-is/add-new-datastore-button-light.png#only-light)
![Screenshot](../assets/datastores/what-is/add-new-datastore-button-dark.png#only-dark)

![Screenshot](../assets/datastores/what-is/add-datastore-light.png#only-light){: style="width:450px"}
![Screenshot](../assets/datastores/what-is/add-datastore-dark.png#only-dark){: style="width:450px"}

!!! info
Qualytics supports any Apache Spark-compatible data source:

    1. Traditional RDBMS 
    2. Raw files (CSV, XLSX, JSON, Avro, Parquet) on:
        - AWS S3
        - Azure Blob Storage
        - GCP Cloud Storage

![Screenshot](../assets/datastores/what-is/listing-datastores-light.png#only-light){: style="width:450px"}
![Screenshot](../assets/datastores/what-is/listing-datastores-dark.png#only-dark){: style="width:450px"}

## Connection Management

Each Datastore type requires specific connection credentials. For example, here's a Snowflake connection configuration:

![Screenshot](../assets/datastores/what-is/add-snowflake-datastore-light.png#only-light){: style="width:450px"}
![Screenshot](../assets/datastores/what-is/add-snowflake-datastore-dark.png#only-dark){: style="width:450px"}

Successfully configured Datastores appear on your home screen:

![Screenshot](../assets/datastores/what-is/show-all-created-datastores-light.png#only-light)
![Screenshot](../assets/datastores/what-is/show-all-created-datastores-dark.png#only-dark)

## Datastore Operations

Each Datastore provides access to Qualytics' core capabilities and operations:

Initial Datastore View:
![Screenshot](../assets/datastores/what-is/specific-datastore-light.png#only-light)
![Screenshot](../assets/datastores/what-is/specific-datastore-dark.png#only-dark)

Activity Monitoring:
![Screenshot](../assets/datastores/what-is/data-volume-light.png#only-light)
![Screenshot](../assets/datastores/what-is/data-volume-dark.png#only-dark)

## Getting Started with a New Datastore

When you first configure a Datastore:

1. An automatic Catalog operation initiates to discover your data assets
2. After cataloging completes, run a Profile operation to:
  - Generate comprehensive metadata
  - Infer data quality checks
  - Enable quality monitoring

To start profiling:

![Screenshot](../assets/datastores/what-is/running-profile-menu-light.png#only-light)
![Screenshot](../assets/datastores/what-is/running-profile-menu-dark.png#only-dark)

![Screenshot](../assets/datastores/what-is/running-profile-light.png#only-light){: style="height:auto"}
![Screenshot](../assets/datastores/what-is/running-profile-dark.png#only-dark){: style="height:auto"}
