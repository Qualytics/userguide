# Quick Start Guide

This guide is designed to help you quickly get started with using Qualytics. From onboarding to the platform and signing in to configuring your first datastore and performing essential operations, this quick start guide will walk you through every step of the process to ensure you can effectively utilize the powerful features of Qualytics.

Let's get started 🚀

## Onboarding

The Qualytics onboarding process ensures a smooth setup and deployment tailored to your needs. This streamlined process ensures that your environment is set up according to your specifications, facilitating a quick and efficient start with Qualytics.  

### 1. Screening and Criteria Gathering

Qualytics conducts a screening to determine if sample data (e.g. customer records), should be included and gathers the primary customer success criteria for the new environment, such as exploring specific use cases.  

### 2. Deployment URL Creation

Based on the domain name (DNS) information you provide, Qualytics creates and provides a customized deployment URL.

### 3. Cloud Provider and Region Selection

The Qualytics team will ask for your preferred cloud providers and deployment region to finalize the deployment and go-live process.  

### 4. User Invitations

After deployment, Qualytics sends invitations to the provided email addresses, assigning admin or member roles based on your preferences.

## Signing In
  
After onboarding to Qualytics, you will receive login credentials to access the Qualytics dashboard.

### Method 1: Using Sign-in Credentials

This method outlines an approach for customers who have not yet integrated their Identity Provider (IdP), thereby not benefiting from Single Sign-On (SSO). Typically, this approach is used during a trial period or Proof of Concept (POC). Once the customer transitions to a paid plan, they generally move to an SSO configuration for enhanced security and convenience.

For instance, the step involving the invitation link (as explained in the onboarding process above) is predominantly associated with this method (Using Sign-in Credentials), which relies on standard email and password credentials.

This allows users to access the system without the need for an integrated IdP during the initial trial phase. This approach is intended to provide ease of access and evaluate the platform's capabilities before committing to full integration with their IdP for SSO.
  
Once the customer completes the onboarding through the invitation link sent to the email, the credentials are produced that can be used for signing in to your Qualytics account and accessing the dashboard.

![sign-in](assets/quick-start-guide/sign-in-light.png#light-only)

### Method 2: Qualytics SSO

With SSO (Single Sign-On), you can access Qualytics more quickly and conveniently without having to go through separate authentication processes for each session.

Most customers will have their own SSO integration. Typically, the login screen will display two buttons:

-   **Qualytics SSO:** Intended for use by Qualytics employees to provide support to customers.  
    
-   **Customer SSO:** Used by the organization's users, leveraging their own SSO for seamless access.

![sign-in](assets/quick-start-guide/welcome-screen-light.png#light-only)

## Datastore

Adding a datastore in Qualytics builds a symbolic link to the location where your data is stored, such as a database or file system. During operations like cataloging, profiling, and scanning, Qualytics reads data from this source location you connect to the platform.

Additionally, Qualytics supports an "Enrichment Datastore," used solely for writing metadata. Even though Qualytics writes to this location, it is still managed by the user, ensuring full control over their data.

When the user is authenticated, the Qualytics onboarding screen appears, where you can click and add your datastore to the Qualytics platform.

![add-first-datastore](assets/quick-start-guide/add-first-datastore-light.png#only-light)
![add-first-datastore](assets/quick-start-guide/add-first-datastore-dark.png#only-dark)

## Configuring Datastores

Qualytics allows you to configure the datastore according to where your data is stored. These datastores are categorized into two types based on their characteristics:

### 1. JDBC Datastores

JDBC datastores are relational databases that support connectivity through the JDBC API, providing universal data access and integration with relational databases.

Here is a list of available JDBC datastores you can add and configure in Qualytics:

| REF | ADD DATASTORE          | DESCRIPTION                                                                                           |
|-----|------------------------|-------------------------------------------------------------------------------------------------------|
| 1.  | BigQuery               | A fully managed, serverless data warehouse that enables scalable analysis over petabytes of data.     |
| 2.  | Databricks             | A unified analytics platform that stores your data to accelerate innovation by unifying data science, engineering, and business. |
| 3.  | DB2                    | It is an IBM database known for its scalability, performance, and availability, primarily used for large enterprises. |
| 4.  | Hive                   | A data warehouse infrastructure built on top of Hadoop for providing data query and analysis.         |
| 5.  | MariaDB                | An open-source relational database management system, a fork of MySQL, renowned for its performance and reliability. |
| 6.  | Microsoft SQL Server   | A relational database management system developed by Microsoft, offering a wide range of data tools and services. |
| 7.  | MySQL                  | An open-source relational database management system widely used for web applications and various other uses. |
| 8.  | Oracle                 | A multi-model database management system widely used for running online transaction processing and data warehousing. |
| 9.  | PostgreSQL             | An advanced, open-source relational database known for its robustness, extensibility, and standards compliance. |
| 10. | Presto                 | A distributed SQL query engine for big data, allowing users to run interactive analytic queries against data sources. |
| 11. | Amazon RedShift        | A fully managed data warehouse service in the cloud, designed to handle large-scale data sets and analytics. |
| 12. | Snowflake              | A cloud-based data warehousing solution that provides data storage, processing, and analytics.        |
| 13. | Synapse                | An analytics service that brings together big data and data warehousing.                              |
| 14. | Timescale DB           | A relational database for time-series data, built on PostgreSQL.                                      |
| 15. | Trino                  | A distributed SQL query engine for big data, designed to query large data sets across multiple data sources. |

### 2. DFS (Distributed File Systems) Datastores

A distributed file system datastore manages files and directories across different servers, designed for scalability and high availability in Qualytics.

Here is a list of available DFS datastores you can configure in the Qualytics platform:

| REF | ADD DATASTORE            | DESCRIPTION                                                                                       |
|-----|--------------------------|---------------------------------------------------------------------------------------------------|
| 1.  | Amazon S3                | A scalable object storage service from Amazon Web Services, used for storing and retrieving any amount of data. |
| 2.  | Azure Blob Storage       | A Microsoft Azure service for storing large amounts of unstructured data, such as text or binary data. |
| 3.  | Azure DataLake Storage   | A scalable data storage and analytics service from Microsoft Azure designed for big data analytics. |
| 4.  | Google Cloud Storage     | A scalable, fully managed object storage service for unstructured data in Google Cloud.           |
| 5.  | Qualytics File System (QFS) | A custom file system designed by Qualytics for optimized data storage and retrieval within the platform. |


## Operations

When you configure and add your datastore in the Qualytics platform you will be redirected to the data assets section where you can perform data operations to analyze metadata, gather statistics, and create profiles. These operations help identify data fitness and anomalies to improve data quality through feedback loops. The operations are categorized as follows.

### 1. Catalog Operation

The Catalog operation involves systematically collecting data structures along with their corresponding metadata. This process also includes a thorough analysis of the existing metadata within the datastore. This ensures a solid foundation for the subsequent Profile and Scan operations.

![catalog-operation](./assets/quick-start-guide/catalog-operation-light.png#only-light)
![catalog-operation](./assets/quick-start-guide/catalog-operation-dark.png#only-dark)

### 2. Profile Operation

The Profile operation enables training of the collected data structures and their associated metadata values. This is crucial for gathering comprehensive aggregating statistics on the selected data, providing deeper insights, and preparing the data for quality assessment.

![profile-operation](./assets/quick-start-guide/profile-operation-light.png#only-light)
![profile-operation](./assets/quick-start-guide/profile-operation-dark.png#only-dark)

### 3. Scan Operation

The Scan operation asserts rigorous quality checks to identify any anomalies within the data. This step ensures data integrity and reliability by recording the analyzed data in your configured enrichment datastore, facilitating continuous data quality improvement.

![scan-operation](./assets/quick-start-guide/scan-operation-light.png#only-light)
![scan-operation](./assets/quick-start-guide/scan-operation-dark.png#only-dark)

## Checks & Rules

Checks and rules are essential components for maintaining data quality in Qualytics. A check encapsulates a data quality rule along with additional contexts such as tags, filters, and tolerances. Rules define the criteria that data must meet, and checks enforce these rules to ensure data integrity.

In Qualytics, you will come across two types of checks:

### 1. Inferred Checks

Qualytics automatically generates inferred checks during a Profile operation. These checks typically cover 80-90% of the rules needed by users. They are created and maintained through profiling, which involves statistical analysis and machine learning methods.

![inferred-check-details](./assets/quick-start-guide/inferred-check-details-light.png#only-light)
![inferred-check-details](./assets/quick-start-guide/inferred-check-details-dark.png#only-dark)

### 2. Authored Checks

Authored checks are manually created by users within the Qualytics platform or API. You can author many types of checks, ranging from simple templates for common checks to complex rules using Spark SQL and User-Defined Functions (UDF) in Scala.

![authored-check-details](./assets/quick-start-guide/authored-check-details-light.png#only-light)
![authored-check-details](./assets/quick-start-guide/authored-check-details-dark.png#only-dark)

## Explore

The Explore dashboard helps manage and analyze your data effectively. It includes several sections, each offering specific functionalities:

### 1. Insights

The Insights section provides an overview of anomaly detection and comprehensive data monitoring options. You can fine-tune the view by source datastores, tags, and dates. You can also check the profile data, applied checks, quality scores, and records scanned for your connected source datastores.

![explore-insights](./assets/quick-start-guide/explore-insights-light.png#only-light)
![explore-inghits](./assets/quick-start-guide/explore-insights-dark.png#only-dark)

### 2. Activity

The Activity section offers an in-depth look at activities across source datastores. It includes a heatmap to visualize the daily volume of operations, along with any detected anomalies.

![explore-activity](./assets/quick-start-guide/explore-activity-light.png#only-light)
![explore-activity](./assets/quick-start-guide/explore-activity-dark.png#only-dark)

### 3. Profiles

The Profiles section provides a unified view of all containers under one roof including:

-   Tables
-   Views
-   Computed Tables
-   Computed Files
-   Fields

It also offers search, sort, and filter functionality to help you efficiently find what you need.

![explore-profiles](./assets/quick-start-guide/explore-profiles-light.png#only-light)
![explore-profiles](./assets/quick-start-guide/explore-profiles-dark.png#only-dark)

### 4. Observability

Observability in the Explore section provides insights into platform data, enabling users to monitor volumes, metrics, trends, and anomalies. Organized into Volumetric and Metric checks, it offers heatmaps and customizable thresholds for efficient data management.

![Observability](./assets/quick-start-guide/observability-light.png#only-light)
![Observability](./assets/quick-start-guide/observability-dark.png#only-dark)

### 5. Checks

The Checks section provides an overview of all applied checks, including both inferred and authored checks, across all source datastores. This allows you to monitor and manage the rules ensuring your data quality.

![explore-checks](./assets/quick-start-guide/explore-checks-light.png#only-light)
![explore-checks](./assets/quick-start-guide/explore-checks-dark.png#only-dark)

### 6. Anomalies

The Anomalies section gives an overview of all detected anomalies across your source datastores. This helps in quickly identifying and addressing any issues.

![explore-anomalies](./assets/quick-start-guide/explore-anomalies-light.png#only-light)
![explore-anomalies](./assets/quick-start-guide/explore-anomalies-dark.png#only-dark)

## Library

The library dashboard offers various options for managing check templates and editing applied checks in your configured source datastores. It includes the following functionalities:

### 1. Add Check Templates

Easily add new check templates to manage and apply standardized checks across different source datastores efficiently.

![check-template-details](./assets/quick-start-guide/check-template-details-light.png#only-light)
![check-template-details](./assets/quick-start-guide/check-template-details-dark.png#only-dark)

### 2. Export Check Templates

The export feature is an operation that writes metadata to a specified Enrichment datastore. In the case of “Check Templates”, Qualytics will write check template metadata to the selected Enrichment datastore from the dropdown list.

![export-check-templates](./assets/quick-start-guide/export-check-templates-light.png#only-light)
![export-check-templates](./assets/quick-start-guide/export-check-templates-dark.png#only-dark)

## Tags

The Tags allow users to categorize and organize entities effectively, while also providing the ability to assign weights for prioritization. They can drive notifications and downstream workflows, and users can configure tags, associate notifications based on Tags, and associate tags to specific properties.

![settings-tags](./assets/quick-start-guide/settings-tags-light.png#only-light)
![settings-tags](./assets/quick-start-guide/settings-tags-dark.png#only-dark)

## Notifications

You can set up notifications when an operation is completed (e.g.- catalog/profile/scan) or when anomalies are identified.

![settings-notifications](./assets/quick-start-guide/settings-notifications-light.png#only-light)
![settings-notfications](./assets/quick-start-guide/settings-notifications-dark.png#only-dark)


## Settings

This section allows you to manage global configurations. You can configure various settings as explained below

### 1. Connection

Delete, edit, or add new datastore sources, ensuring efficient management of your configured datastores.

![settings-connection](./assets/quick-start-guide/settings-connections-light.png#only-light)
![settings-connection](./assets/quick-start-guide/settings-connections-dark.png#only-dark)

### 2. Security

Delete, edit, or add new teams, and assign roles to users for better access control and management.

![settings-security](./assets/quick-start-guide/settings-security-light.png#only-light)
![settings-security](./assets/quick-start-guide/settings-security-dark.png#only-dark)

### 3. Integration

Configure necessary parameters to integrate external tools with the Qualytics dashboard.

![settings-integrations](./assets/quick-start-guide/settings-integrations-light.png#only-light)
![settings-integrations](./assets/quick-start-guide/settings-integrations-dark.png#only-dark)

### 4. Tokens

Create tokens to enable secure and direct interaction with the Qualytics API.

![settings-tokens](./assets/quick-start-guide/settings-tokens-light.png#only-light)
![settings-tokens](./assets/quick-start-guide/settings-tokens-dark.png#only-dark)

### 5. Health

This page provides an easy way to monitor the health of Qualytics deployment while also providing the option to restart the Analytics engine.

![settings-health](./assets/quick-start-guide/settings-health-light.png#only-light)
![settings-health](./assets/quick-start-guide/settings-health-dark.png#only-dark)
