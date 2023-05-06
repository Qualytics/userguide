# What is Qualytics?

The `Active Data Quality Platform` that enables teams to manage data quality at scale through advanced automation. Qualytics is the complete solution to instill trust and confidence in your enterprise data ecosystem through automated `data profiling`, `data quality rule inference`, `anomaly detection` & `remediation`.

## Data Quality Management

Qualytics enables your data teams to `address data issues faster` in a proactive manner by automating the `discovery` and `maintenance` of data quality measures you need.

1. Your `historic data` is analyzed for its shapes and patterns in order to infer contextual data quality rules.
1. These rules are combined with any you self-author and then asserted to find anomalies in historic data or new data (with auto-detected incremental support).
1. When an anomaly is identified, Qualytics enables your team to `take corrective actions` using their existing data tooling and can initiate remediation by:
    - delivering a notification through your desired integration (Teams, Slack, PagerDuty, etc...)
    - triggering a downstream workflow (Airflow, Airbyte, Fivetran)
    - `enriching` a selected datastore with details of the anomaly (supportive of SQL-based integrations such as DBT)
    - suggesting the appropriate value (suggested remediation) through our user interface and API
1. Your data quality is proactively monitored and scored & your quality checks are continuously updated to reflect changes in your actuals and your business

Through this process Qualytics continuouly improves your data quality and promotes trust & confidence in your organization's data.

## Focus areas

* __Automated Profiling__:
Qualytics utilizes your existing data to automatically build and expose profiles for each of your data assets. This profile metadata is also used to automatically infer data quality rules that will identify outliers in your existing or future data. Those rules are automatically kept up to date with changes in the shape and range of your data as it evolves over time.

* __Anomaly Detection__:
Data Quality rules are notoriously hard to author and maintain at scale. Qualytics solves this by automatically inferring appropriate data quality rules and then asserting them to identify anomalies at-rest and in-flight throughout your data ecosystem.

* __Anomaly Remediation__:
Qualytics asserts your automatically inferred and your human-authored data quality checks against your data at user-defined intervals (or continuously) to identifiy anomalies within your data.  Qualytics then provides the mechanisms required to take corrective actions to address these data outliers using your team's preferred data tooling.

* __Flexible Deployment__:
On-premise, single-tenant cloud, or SaaS. We meet you where your data is.

* __Support Modern & Legacy Data Stacks__:
From Snowflake to Oracle, Amazon S3 to MSSQL - Data Quality is important everywhere. Qualytics fits seamlessly into your data stack, with effortless integrations with any Spark-compatible datastore.

* As a quick reference, here is a short video demonstrating the platform with a quick walkthrough:

    <iframe width="760" height="415" src="https://www.loom.com/embed/6d40de8bb6784cf2933e78b4fc0b3d0a" title="Qualytics Demo" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


## Standard Management Steps

Qualytics is employed for myriad usecases by organizations both large and small. Yet using it to implement a robust data management process requires just a few simple steps:

1. [Add your datastores](datastores/what-is-datastore.md) using your intuitive web app or API
    - We recommend you add at least one [Enrichment Datastore](enrichment/what-is-enrichment.md) to support easier anomalous data identification & remediation
1. [Run a Profile Operation on your datastore](operations/profile.md) to generate metadata insights for all its data assets and infer customized [data quality checks](checks/what-is.md)
1. [Scan your datastore](operations/scan.md) to assert the automatically inferred checks (and any you human-author) against the historical or new data in your datastore
1. [Review identified anomalies](anomalies/what-is-an-anomaly.md) and flag them with appropriate status. Qualytics will learn about hour business and preferences and tune future operations accordingly!


## About this guide
This User Guide is here to help you adopt our platform to achieve your data quality goals.

<!-- * TODO - ADD FRESHNESS SLA FUNCTIONALITY, INCLUDE DETAILS FROM API DOCUMENTATION -->
