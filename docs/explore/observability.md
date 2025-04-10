# Observability

Observability provides a structured way to monitor data behavior, detect anomalies, and identify trends across datastores and tables. It supports consistent tracking through **Measures** and **Metrics**, including daily data volumes, data freshness, and specific field-level values measured against predefined thresholds. Automated scans, heatmaps, and visual insights make it easier to spot issues, set thresholds, and adjust monitoring settings to maintain data integrity.

Users can access the Observability tab in the Explore section to get an overview of observability metrics across multiple source datastores and tables. However, to analyze a specific datastore in detail, navigate to the [**Observability**](../observability/observability.md) documentation for detailed insights at the source level.

Let’s get started 🚀

## Navigation

**Step 1:** Log in to your Qualytics account and click the **Explore** button on the left side panel of the interface.

![explore](../assets/explore/observability/explore-light.png#only-light)
![explore](../assets/explore/observability/explore-dark.png#only-dark)

**Step 2:** Click on the **"Observability"** from the Navigation Tab.

![observability](../assets/explore/observability/observability-light.png#only-light)
![observability](../assets/explore/observability/observability-dark.png#only-dark)

Observability metrics for multiple source datastores and tables are shown, enabling you to view their detailed insights.

![observability-metrics](../assets/explore/observability/observability-metrics-light.png#only-light)
![observability-metrics](../assets/explore/observability/observability-metrics-dark.png#only-dark)

## Observability Categorized

Observability in data checks is divided into two key categories: **Measures** and **Metric Checks**. Measures focus on overall data trends and include **Volumetric Checks**, which monitor data volume to identify trends and anomalies, and **Freshness Tracking**, which tracks when data was last added or updated to ensure timeliness. **Metric Checks**, on the other hand, analyze specific data attributes, providing detailed insights into data quality.

![category](../assets/explore/observability/category-light.png#only-light)
![category](../assets/explore/observability/category-dark.png#only-dark)

**1.Measures:** Measures focus on monitoring overall data trends to ensure consistency and reliability. This includes **Volumetric Checks**, which track data volume to identify trends and detect anomalies, and **Freshness** Tracking, which measures the last update or addition of data to ensure timeliness. These checks help maintain data integrity by highlighting unexpected changes in volume or delays in data updates.

![volumetric](../assets/explore/observability/volumetric-light.png#only-light)
![volumetric](../assets/explore/observability/volumetric-dark.png#only-dark)

**2. Metric:** Metric measures data based on predefined fields and thresholds, tracking changes in data values over time. It detects if the value of a specific field, like the average or absolute value, goes beyond the expected range. Using scheduled scans, it automatically records and analyzes these values, helping users quickly spot any anomalies. This check gives deeper insights into data behavior, ensuring data integrity and identifying irregular patterns easily.

![metric](../assets/explore/observability/metric-light.png#only-light)
![metric](../assets/explore/observability/metric-dark.png#only-dark)

## **Measures**

**Measures** focus on tracking overall data trends to ensure stability, consistency, and reliability. This category includes two key checks:

### Volumetric

Volumetric help monitor data volumes over time to keep data accurate and reliable. They automatically count rows in a table and spot any unusual changes, like problems with data loading. This makes it easier to catch issues early and keep everything running smoothly.

![fields](../assets/explore/observability/fields-light.png#only-light)
![fields](../assets/explore/observability/fields-dark.png#only-dark)

For more information on volumetric checks, please refer to the [**Volumetric**](../observability/observability.md/#volumetric) section in the documentation.

### Observability Heatmap

The heatmap provides a visual overview of data anomalies by day, using color codes for quick understanding:

![heatmap](../assets/explore/observability/heatmap-light.png#only-light)
![heatmap](../assets/explore/observability/heatmap-dark.png#only-dark)

For more information on observability heatmap, please refer to the [**Observability Heatmap**](../observability/observability.md/#observability-heatmap) section in the documentation.

### Edit Check

Editing a Volumetric Check lets users customize settings like measurement period, row count limits, and description. This helps improve data monitoring and anomaly detection, ensuring the check fits specific needs. Users can also add tags for better organization.

**Step 1:** Click the edit icon to modify the check.

![edit](../assets/explore/observability/edit-light.png#only-light)
![edit](../assets/explore/observability/edit-dark.png#only-dark)

To understand how to edit checks, you can follow the remaining steps from the documentation [**Edit Check**](../observability/observability.md/#edit-check).

### Edit Threshold

Edit thresholds to set specific row count limits for your data checks. By defining minimum and maximum values, you ensure alerts are triggered when data goes beyond the expected range. This helps you monitor unusual changes in data volume. It gives you better control over tracking your data's behavior.

**Step 1:**  Click the **Edit Thresholds** button on the right side of the graph.

![threshold](../assets/explore/observability/threshold-light.png#only-light)
![threshold](../assets/explore/observability/threshold-dark.png#only-dark)

To understand how to edit threshold, you can follow the remaining steps from the documentation [**Edit Threshold**](../observability/observability.md/#edit-threshold).

### Freshness

This measures the timeliness of data by monitoring when new data was last added or updated. It helps ensure that data remains up-to-date and relevant for decision-making. If data updates are delayed or missing, it may indicate pipeline failures, system lag, or unexpected data source changes.

![freshness](../assets/explore/observability/freshness-light.png#only-light)
![freshness](../assets/explore/observability/freshness-dark.png#only-dark)

For more information on freshness checks, please refer to the [**Freshness**](../observability/observability.md/#freshness) section in the documentation.

### Edit Check

Editing a Check enables users to modify settings such as the unit of measurement, maximum age, description, and metadata. Additionally, they can add tags to streamline organization and retrieval.

**Step 1:** Click the edit icon to modify the check.

![freshness](../assets/explore/observability/icons-light.png#only-light)
![freshness](../assets/explore/observability/icons-dark.png#only-dark)

To understand how to edit checks, you can follow the remaining steps from the documentation [**Edit Check**](../observability/observability.md/#edit-check-1).

### Edit Maximum Age

**Maximum Age** sets the limit for how long data can remain unchanged before it’s flagged as outdated. This ensures your data stays fresh and reliable for decision-making.

**Step 1:** Click the **Edit Maximum Age** button on the right side of the graph.

![freshness](../assets/explore/observability/age-light.png#only-light)
![freshness](../assets/explore/observability/age-dark.png#only-dark)

To understand how to edit maximum age, you can follow the remaining steps from the documentation [**Edit Maximum Age**](../observability/observability.md/#edit-maximum-age).

## Metric

Metric track changes in data over time to ensure accuracy and reliability. They check specific fields against set limits to identify when values, like averages, go beyond expected ranges. With scheduled scans, Metrics automatically log and analyze these data points, making it easy for users to spot any issues. This functionality enhances users' understanding of data patterns, ensuring high quality and dependability. With Metrics, managing and monitoring data becomes straightforward and efficient.

![field](../assets/explore/observability/field-light.png#only-light)
![field](../assets/explore/observability/field-dark.png#only-dark)

### Comparisons

When you add a metric check, you can choose from three comparison options:

* Absolute Change  
* Absolute Value  
* Percentage Change.

These options help define how the system will evaluate your data during scan operations on the datastore.

Once a scan is run, the system analyzes the data based on the selected comparison type. For example, Absolute Change will look for significant differences between scans, Absolute Value checks if the data falls within a predefined range, and Percentage Change identifies shifts in data as a percentage.

For more information on comparisons, please refer to the [**Comparisons**](../observability/observability.md/#comparisons) section in the documentation.

### Edit Check

**Edit Check** allows users to modify the parameters of an existing metric check. It enables adjusting values, thresholds, or comparison logic to ensure that the metric accurately reflects current monitoring needs.

**Step 1:** Click the edit icon to modify the check.

![icon](../assets/explore/observability/icon-light.png#only-light)
![icon](../assets/explore/observability/icon-dark.png#only-dark)

To understand how to edit checks, you can follow the remaining steps from the documentation [**Edit Check**](../observability/observability.md/#edit-check-2).

### Edit Threshold

**Edit Threshold** allows you to change the upper and lower limits of a metric. This ensures the metric tracks data within the desired range and only triggers alerts when those limits are exceeded.

**Step 1:** Click the **Edit Thresholds** button on the right side of the graph.

![thresholdss](../assets/explore/observability/thresholdss-light.png#only-light)
![thresholdss](../assets/explore/observability/thresholdss-dark.png#only-dark)

To understand how to edit thresholds, you can follow the remaining steps from the documentation [**Edit Threshold**](../observability/observability.md/#edit-threshold-1).