# Observability

Observability helps users track changes in data volume and quality over time, ensuring data accuracy and integrity. Within the Source Datastore section, the Observability tab provides visibility into observability metrics across tables or files within a specific datastore. It introduces two main categories: **Measures** and **Metric Checks**. Measures include **Volumetric Checks**, which monitor fluctuations in row counts, and **Freshness Tracking**, which ensures data is updated on time. **Metric Checks** focus on specific fields and offer deeper insights derived from scan operations. These tools work together to help detect anomalies early and maintain the reliability of your data assets.

Users can access the Observability tab in the Source Datastore section to analyze particular datastore in detail. However, to get an overview of observability metrics across multiple source datastores and tables, navigate to the [**Observability**](../explore/observability.md) documentation for centralized overview of data behavior across your entire environment.

Let’s get started 🚀

## Navigation

**Step 1:** Log in to your Qualytics account and select the datastore from the left menu that you want to monitor.

![datastore](../assets/observability/source-light-1.png)

**Step 2:** Click on the **“Observability”** from the Navigation tab.

![observability](../assets/observability/observability-light-2.png)

Observability metrics for tables of the selected source datastore are shown, enabling you to view their detailed insights.

![observability-metrics](../assets/observability/observability-metrics-light.png)

## Observability Categories

Observability in data checks is divided into two key categories: **Measures** and **Metric Checks**. Measures focus on overall data trends and include **Volumetric Checks**, which monitor data volume to identify trends and anomalies, and **Freshness Tracking**, which tracks when data was last added or updated to ensure timeliness. **Metric Checks**, on the other hand, analyze specific data attributes, providing detailed insights into data quality.

![category](../assets/observability/category-light-3.png)

For more information regarding measures please refer to the [measure documentation](../observability/measures.md).

For more information regarding metric please refer to the [metric documentation](../observability/metric-check.md).