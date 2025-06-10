# Quick Start Guide

Welcome to Qualytics! This guide will help you quickly get up and running with the platform, from initial setup through your first data quality operations. Whether you're a business user or technical administrator, you'll find everything needed to start managing data quality at scale.

Let's get started 🚀

## Deployment Access

Each Qualytics deployment is a single-tenant, dedicated cloud instance, configured to your organization's requirements. Your deployment will be accessible via a custom URL (e.g., `https://acme.qualytics.io`), with corresponding API documentation at `/api/docs`.

## Onboarding Process

The [Qualytics onboarding process](./onboarding.md) ensures your environment is perfectly tailored to your needs:

### 1. Screening and Criteria Gathering

Our team works with you to understand your specific needs, including:

- Evaluating sample data requirements
- Identifying primary success criteria
- Exploring relevant use cases for your environment
- Determining deployment specifications

### 2. Environment Setup

Based on your requirements, we:

- Create your custom deployment URL
- Configure your preferred cloud provider and region
- Set up initial security parameters
- Establish integration endpoints

### 3. User Access

Once deployment is complete:

- Team members receive email invitations
- Roles are assigned based on your specifications
- Access credentials are securely distributed

!!!tip
    Please check your spam folder if you don't see the invite.

See [our onboarding page](./onboarding.md) for a more detailed view of what to expect during onboarding!

## Signing In

Qualytics supports two authentication methods:

### Method 1: Direct Credentials

Ideal for:

- Initial platform evaluation
- Proof of Concept (POC) phases
- Environments without SSO integration

![sign-in](assets/quick-start-guide/sign-in-light.png#light-only)

### Method 2: Enterprise SSO

For production deployments:

- Integrates with your organization's Identity Provider
- Supports standard SSO protocols
- Provides seamless access management

![sign-in](assets/quick-start-guide/welcome-screen-light.png#light-only)

## Getting Started Checklist

To begin using Qualytics, you'll complete these key steps:

1. Connect Your First Datastore
2. Run Initial Profile Operation
3. Review Generated Quality Checks
4. Configure Monitoring & Alerts

Let's walk through each step in detail.

## Understanding Datastores

In Qualytics, a Datastore represents your data source connection. Qualytics supports any Apache Spark-compatible data source, including:

### JDBC Datastores

- Traditional relational databases (RDBMS)
- Data warehouses
- Analytical databases

### Distributed File System (DFS) Datastores

- Cloud storage (AWS S3, Azure Blob, GCP)
- Raw files (CSV, XLSX, JSON, Avro, Parquet)
- Local file systems

## Connecting Your First Datastore

### Adding a Source Datastore

1. From the main menu, select "Add Source Datastore":
   ![add-first-datastore](assets/quick-start-guide/add-first-datastore-light.png#only-light)
   ![add-first-datastore](assets/quick-start-guide/add-first-datastore-dark.png#only-dark)

2. Select your datastore type
3. Provide connection details
4. Test connectivity
5. Configure an Enrichment Datastore (strongly recommended)

!!!warning
    While optional, not configuring an Enrichment Datastore limits platform capabilities.

### Enrichment Datastores

An Enrichment Datastore serves as the storage location for:

- Anomaly detection results
- Metadata and profiling information
- Quality check outcomes
- Historical analysis data

You can either:

1. Configure a new Enrichment Datastore
2. Select an existing one from the dropdown

## Core Operations

After connecting your datastore, three fundamental operations manage data quality:

### 1. Catalog Operation

The first step in understanding your data:

- Systematically collects data structures
- Analyzes existing metadata
- Prepares for profiling and scanning
- Runs automatically on datastore creation

![catalog-operation](./assets/quick-start-guide/catalog-operation-light.png#only-light)
![catalog-operation](./assets/quick-start-guide/catalog-operation-dark.png#only-dark)

### 2. Profile Operation

The Profile operation performs deep analysis of your data:

- Generates comprehensive metadata
- Calculates statistical measures:
    - Basic metrics (type, min/max, lengths)
    - Advanced analytics (skewness, kurtosis, correlations)
    - Value distributions and patterns
- Automatically infers data quality rules
- Uses machine learning for pattern detection

![profile-operation](./assets/quick-start-guide/profile-operation-light.png#only-light)
![profile-operation](./assets/quick-start-guide/profile-operation-dark.png#only-dark)

Our profiling engine analyzes:

- Field types and patterns
- Value distributions
- Statistical relationships
- Data quality patterns
- Structural consistency

The engine uses machine learning to:

- Identify column data types
- Discover relationships
- Generate quality rules
- Detect anomaly patterns

### 3. Scan Operation

The Scan operation actively monitors data quality:

- Asserts all defined quality checks
- Identifies anomalies and violations
- Records results in the Enrichment Datastore
- Generates quality scores

![scan-operation](./assets/quick-start-guide/scan-operation-light.png#only-light)
![scan-operation](./assets/quick-start-guide/scan-operation-dark.png#only-dark)

The first scan runs as a "Full" scan to establish baselines. After completion, you can review:

- Start and finish times
- Records processed
- Anomalies detected
- Quality scores

## Managing Data Quality

### Quality Checks

Qualytics uses two types of quality checks:

#### 1. Inferred Checks

- Automatically generated during profiling
- Cover 80-90% of common quality rules
- Based on statistical analysis and ML
- Continuously refined through operation

![inferred-check-details](./assets/quick-start-guide/inferred-check-details-light.png#only-light)
![inferred-check-details](./assets/quick-start-guide/inferred-check-details-dark.png#only-dark)

#### 2. Authored Checks

- Manually created by users
- Support complex business rules
- Use Spark SQL or Scala UDFs
- Can be templated and shared

![authored-check-details](./assets/quick-start-guide/authored-check-details-light.png#only-light)
![authored-check-details](./assets/quick-start-guide/authored-check-details-dark.png#only-dark)

## Platform Navigation

### Explore Dashboard

The Explore interface provides comprehensive visibility:

#### 1. Insights

- Overview of anomaly detection
- Quality monitoring metrics
- Filterable by source, tags, dates

  ![explore-insights](./assets/quick-start-guide/explore-insights-light.png#only-light)
  ![explore-insights](./assets/quick-start-guide/explore-insights-dark.png#only-dark)
  
#### 2. Activity

- Operation history and status
- Data volume heatmaps
- Anomaly tracking

  ![explore-activity](./assets/quick-start-guide/explore-activity-light.png#only-light)
  ![explore-activity](./assets/quick-start-guide/explore-activity-dark.png#only-dark)

#### 3. Profiles

Unified view of all data assets:

- Tables and Views
- Computed Assets
- Field-level Details

  ![explore-profiles](./assets/quick-start-guide/explore-profiles-light.png#only-light)
  ![explore-profiles](./assets/quick-start-guide/explore-profiles-dark.png#only-dark)

#### 4. Observability

Monitor platform health and performance:

- Volume metrics
- Quality trends
- System health

  ![Observability](./assets/quick-start-guide/observability-light.png#only-light)
  ![Observability](./assets/quick-start-guide/observability-dark.png#only-dark)

## Configuration & Management

### Tags

Organize and prioritize:

- Categorize data assets
- Drive notifications
- Weight importance

  ![settings-tags](./assets/quick-start-guide/settings-tags-light.png#only-light)
  ![settings-tags](./assets/quick-start-guide/settings-tags-dark.png#only-dark)

### Flows

Automate and streamline:

- Trigger actions based on specific events
- Manage workflows efficiently
- Monitor and track execution status

  ![flows](./assets/quick-start-guide/flows-light.png#only-light)
  ![flows](./assets/quick-start-guide/flows-dark.png#only-dark)

### Platform Settings

Access key configuration areas:

1. **Connections**
    - Manage datastores
    - Configure integrations

      ![settings-connection](./assets/quick-start-guide/settings-connections-light.png#only-light)
      ![settings-connection](./assets/quick-start-guide/settings-connections-dark.png#only-dark)

2. **Security**
    - User management
    - Role assignments

      ![settings-security](./assets/quick-start-guide/settings-security-light.png#only-light)
      ![settings-security](./assets/quick-start-guide/settings-security-dark.png#only-dark)

3. **Integrations**
    - External tool setup
    - API configuration

      ![settings-integrations](./assets/quick-start-guide/settings-integrations-light.png#only-light)
      ![settings-integrations](./assets/quick-start-guide/settings-integrations-dark.png#only-dark)

4. **Status**
    - Deployment status
    - Analytics engine management

      ![settings-status](./assets/quick-start-guide/settings-status-light.png#only-light)
      ![settings-status](./assets/quick-start-guide/settings-status-dark.png#only-dark)

## Next Steps

Now that you're familiar with Qualytics basics, consider:

1. Setting up additional datastores
2. Creating custom quality checks
3. Configuring notifications
4. Exploring advanced features

For detailed information on any topic, explore the relevant sections in our documentation.
