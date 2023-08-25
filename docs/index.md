---
hide:
  - navigation
---

# User Guide: Introduction to Qualytics

Qualytics is the Active Data Quality Platform that enables teams to manage data quality at scale through advanced automation. Qualytics analyzes your historic data for its shapes and patterns in order to infer contextual data quality rules that are then asserted against new data (often in incremental loads) to identify anomalies. When an anomaly is identified, Qualytics provides your team with everything needed to take corrective actions using their existing data tooling & preferred monitoring solutions.

## Managing Data Quality

With Qualytics, your data teams can quickly address data issues in a proactive way by automating the discovery and maintenance of data quality measures you need.

Here's how it works:

1. **Analyzing Historical Data**: Qualytics examines your historical data to understand its patterns and characteristics, allowing it to create rules that define good data quality.

2. **Finding Anomalies**: These rules, combined with any rules you create yourself, are used to identify any abnormalities or inconsistencies in your historical data or new data (even when new data is added incrementally).

3. **Taking Corrective Actions**: When an anomaly is detected, Qualytics helps your team take appropriate actions. Utilizing tags, it can send notifications through the platforms you use (such as Teams, Slack, or PagerDuty), trigger workflows in tools (like Airflow, Fivetran or Airbyte), provide additional information about the anomaly to your chosen datastore (compatible with SQL-based integrations like dbt), and even suggest the best course of action through its user interface and API.

4. **Continuous Monitoring and Improvement**: Qualytics continuously monitors and scores your data quality. It keeps your quality checks up to date, taking into account any changes in your actual data and your business needs. This ongoing process helps improve your overall data quality and boosts trust and confidence in your organization's data.

By leveraging Qualytics, you can efficiently manage data quality, proactively address issues, and enhance trust in the data driving your organization.

## Key Features

Qualytics offers a range of powerful features designed to enhance your data quality management:

1. **Automated Data Profiling**: Qualytics leverages your existing data to automatically generate profiles for each of your data assets. These profiles provide valuable insights into your data and serve as the foundation for maintaining data quality.

2. **Rule Inference**: Crafting and maintaining data quality rules at scale can be a daunting task. Qualytics simplifies this process by automatically inferring appropriate data quality rules based on your data profiles. This saves you time and effort while ensuring accurate anomaly detection.

3. **Anomaly Detection**: Identifying anomalies within your data is crucial for maintaining data quality. Qualytics excels in detecting anomalies at rest and in flight throughout your data ecosystem. By highlighting outliers and irregularities, it helps you identify and address data quality issues effectively.

4. **Anomaly Remediation**: Once anomalies are detected, Qualytics provides the necessary tools to take corrective actions. It enables you to seamlessly integrate with your preferred data tooling and initiate remediation workflows. This ensures that data outliers are addressed promptly and efficiently.

5. **Freshness Monitoring**: Qualytics includes functionality for monitoring data freshness Service Level Agreements (SLAs). It allows you to define and track SLAs for the timeliness of data updates, ensuring that your data remains up-to-date and meets the required service level agreements.

6. **Insights Dashboard**: Qualytics provides an intuitive executive dashboard called Insights. This dashboard gives you a holistic view of the health and quality of your data. You can easily visualize key data quality metrics, track progress, and gain actionable insights. With the executive dashboard, you can make informed decisions and drive data-driven strategies for your organization.

## Seamless Integration and Deployment

Qualytics offers flexible integration options to fit your data infrastructure seamlessly:

- **Deployment Options**: Whether you prefer an on-premise, single-tenant cloud, or SaaS deployment, Qualytics adapts to your specific needs. It meets you where your data resides, ensuring a hassle-free integration process.

- **Support for Modern & Legacy Data Stacks**: Qualytics seamlessly integrates with a wide range of data platforms. From modern solutions like Snowflake and Amazon S3 to legacy systems like Oracle and MSSQL, Qualytics supports your data stack. This versatility ensures that data quality remains a priority across all your data sources.

## Demo
Here is a short video demonstrating the platform with a quick walkthrough:
<iframe width="760" height="415" src="https://www.loom.com/embed/788412013bd34366a1800fee54190379" title="Qualytics - Full Demo of Qualytics Platform" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>



<!-- moved Implementation to Quick Start -->

## Embarking on Your Journey

This user guide will walk you through the key functionalities of Qualytics and provide step-by-step instructions to help you make the most of this powerful platform. Whether you are new to Qualytics or looking to deepen your understanding, this guide will be your companion in optimizing your data quality management.

Let's embark on this journey to empower your organization with accurate, reliable, and trustworthy data using Qualytics!


<!-- * TODO - ADD FRESHNESS SLA FUNCTIONALITY, INCLUDE DETAILS FROM API DOCUMENTATION -->
