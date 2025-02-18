# Onboarding 

Qualytics is a [<u>comprehensive data quality management solution</u>](https://www.qualytics.ai/product/) that helps enterprises proactively manage their full data quality lifecycle at scale. Through automated profiling, contextual quality checks, rule inference, anomaly detection, remediation, and tailored notifications, Qualytics transforms how organizations approach data quality.

This guide will walk you through getting started with Qualytics, ensuring a smooth and efficient onboarding experience.

Let's get started 🚀

## Onboarding Process

Your Qualytics journey begins with understanding your enterprise's specific requirements. We'll work with you to create a tailored approach based on your data needs and goals.

### 1. Screening & Criteria Gathering

[<u>Schedule a demo</u>](https://calendly.com/gorkemsevinc/30min?month=2024-06) with our team to help us understand your enterprise data needs. During this session, we'll:
- Create a detailed plan
- Identify key success criteria
- Tailor the deployment to your specific requirements
- Explore relevant use cases for your business

### 2. User Invitations

Once your deployment setup is complete, we'll send invitations to your team members' email addresses. These invitations include:
- Instructions for accessing the platform
- Role assignments (admin or member) based on your preferences
- Access configuration details

Admins receive full platform configuration and management capabilities, while members receive access based on admin-defined permissions.

### Deployment Options

Qualytics offers flexible deployment options to seamlessly integrate with your existing data infrastructure:

### 1. SaaS Deployment (Default)

Our Software as a Service (SaaS) deployment provides a fully managed experience hosted by Qualytics. This option offers:
- Minimal maintenance requirements
- Rapid scalability
- Automatic updates and improvements
- Focus on data quality rather than infrastructure

### 2. On-Premise Deployment

For organizations that prefer complete control over their data environment, our on-premise deployment option allows you to:
- Maintain data within your own data centers
- Ensure compliance with internal policies and regulations
- Exercise complete control over your data and security

!!! tip
    This deployment option is recommended for customers with sensitive data

## Frequent Asked Questions (FAQs) 

**Q 1: What type of support is provided during a POC?**

**A 1:** A dedicated Customer Success Manager, with mandatory weekly check-ins.

**Q 2: What are the deployment options for POC?**

**A 2:** Qualytics offers deployment options for Proof of Concept (POC) primarily as a Software as a Service (SaaS) solution.

**Q 3: What type of data should we use for a POC?**

**A 3:** In most cases, potential customers use their actual data during a POC for the most realistic evaluation. Some customers opt to use cleaned data (removing PII) or sample test data.

**Q 4: Are there limitations to data size for POC?**

**A 4:** There are no limitations to data size for a Proof of Concept (POC).

**Q 5: What type of support is provided during the Onboarding process?**

**A 5:** A dedicated Customer Success Manager, with mandatory weekly check-ins.

**Q 6: What types of data stacks does Qualytics support?**

**A 6:** Qualytics supports both modern solutions and legacy systems:

- Modern Solutions
  > Qualytics seamlessly integrates with modern data platforms like Snowflake, Amazon S3, BigQuery, and more to ensure robust data quality management.

- Legacy Systems
  > We maintain high data quality standards across legacy systems including MySQL, Microsoft SQL Server, and other reliable relational database management systems.

For detailed integration instructions, please refer to the [<u>quick start guide</u>](https://userguide.qualytics.io/quick-start-guide/).

**Q 7: What types of database technology can you connect in Qualytics?**

**A 7:** Qualytics supports any Apache Spark-compatible datastore, including:
- Relational databases (RDBMS)
- Raw file formats (CSV, XLSX, JSON, Avro, Parquet)

**Q 8: What is an enrichment datastore?**

**A 8:** An Enrichment Datastore is a user-managed storage location where Qualytics records and accesses metadata through system-defined tables. It's specifically designed to capture metadata generated during profiling and scanning operations.

**Q 9: Can I download my metadata and data quality checks?**

**A 9:** Yes, Qualytics's metadata export feature captures the mutable states of various data entities. You can export Quality Checks, Field Profiles, and Anomalies metadata from selected profiles into your designated enrichment datastore.

**Q 10: How is the Quality Score calculated?**

**A 10:** Quality Scores measure data quality at the field, container, and datastore levels, recorded as a time series to track improvements. Scores range from 0-100, with higher scores indicating better quality.

**Q 11: What is a catalog operation?**

**A 11:** A Catalog Operation scans your datastore to import named collections (tables, views, files). It automatically identifies optimal approaches for:
- Incremental scanning
- Data partitioning
- Record identification

**Q 12: What is a profiling operation?**

**A 12:** A Profile Operation analyzes every available record across all containers in a datastore. Full Profiles deliver 100% fidelity metadata at the cost of maximum compute time.

**Q 13: What is a scan operation?**

**A 13:** The Scan Operation evaluates data quality checks across your datastore's collections, producing:
- Record anomalies for individual anomalous values
- Shape anomalies for multi-record anomalies
- Detailed analysis in your Enrichment Datastore