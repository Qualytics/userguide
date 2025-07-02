# Observability

Observability helps users track changes in data volume and quality over time, ensuring data accuracy and integrity. Within the Source Datastore section, the Observability tab provides visibility into observability metrics across tables or files within a specific datastore. It introduces two main categories: **Measures** and **Metric** Checks. Measures include **Volumetric Checks**, which monitor fluctuations in row counts, and **Freshness Tracking**, which ensures data is updated on time. **Metric Checks** focus on specific fields and offer deeper insights derived from scan operations. These tools work together to help detect anomalies early and maintain the reliability of your data assets.

Users can access the Observability tab in the Source Datastore section to analyze particular datastore in detail. However, to get an overview of observability metrics across multiple source datastores and tables, navigate to the [**Observability**](../explore/observability.md) documentation for centralized overview of data behavior across your entire environment.

Let’s get started 🚀

## Navigation

**Step 1:** Log in to your Qualytics account and select the datastore from the left menu that you want to monitor.

![datastore](../assets/observability/source-light-1.png#only-light)
![datastore](../assets/observability/source-dark-1.png#only-dark)

**Step 2:** Click on the **“Observability”** from the Navigation tab.

![observability](../assets/observability/observability-light-2.png#only-light)
![observability](../assets/observability/observability-dark-2.png#only-dark)

Observability metrics for tables of the selected source datastore are shown, enabling you to view their detailed insights.

![observability-metrics](../assets/observability/observability-metrics-light.png#only-light)
![observability-metrics](../assets/observability/observability-metrics-dark.png#only-dark)

## Observability Categories

Observability in data checks is divided into two key categories: **Measures** and **Metric Checks**. Measures focus on overall data trends and include **Volumetric Checks**, which monitor data volume to identify trends and anomalies, and **Freshness Tracking**, which tracks when data was last added or updated to ensure timeliness. **Metric Checks**, on the other hand, analyze specific data attributes, providing detailed insights into data quality.

![category](../assets/observability/category-light-3.png#only-light)
![category](../assets/observability/category-dark-3.png#only-dark)

**1. Measures:** Measures focus on monitoring overall data trends to ensure consistency and reliability. This includes **Volumetric Checks**, which track data volume to identify trends and detect anomalies, and **Freshness** Tracking, which measures the last update or addition of data to ensure timeliness. These checks help maintain data integrity by highlighting unexpected changes in volume or delays in data updates.

![volumetric](../assets/observability/volumetric-light-4.png#only-light)
![volumetric](../assets/observability/volumetric-dark-4.png#only-dark)

**2. Metric:** Metric measures data based on predefined fields and thresholds, tracking changes in data values over time. It detects if the value of a specific field, like the average or absolute value, goes beyond the expected range. Using scheduled scans, it automatically records and analyzes these values, helping users quickly spot any anomalies. This check gives deeper insights into data behavior, ensuring data integrity and identifying irregular patterns easily.

![metric](../assets/observability/metric-light-5.png#only-light)
![metric](../assets/observability/metric-dark-5.png#only-dark)

For demonstration purposes, we have selected the **partsupp_clone** table of **TPCH Postgres** datastore.

![selected-table](../assets/observability/selected-table-light.png#only-light)
![selected-table](../assets/observability/selected-table-dark.png#only-dark)

## **Measures**

**Measures** focus on tracking overall data trends to ensure stability, consistency, and reliability. This category includes two key checks:

### Volumetric

Volumetric help monitor data volumes over time to keep data accurate and reliable. They automatically count rows in a table and spot any unusual changes, like problems with data loading. This makes it easier to catch issues early and keep everything running smoothly. Volumetric checks also let you track data over different time periods, like daily or weekly. The system sets limits based on past data, and if the row count goes above or below those limits, an anomaly alert is triggered.

![details](../assets/observability/volumetric-detail-light-6.png#only-light)
![detail](../assets/observability/volumetric-detail-dark-6.png#only-dark)

| No | Field | Description |
| :---- | :---- | :---- |
| 1 | Search  | This feature helps users quickly find specific identifiers or names in the data. |
| 2 | Report Data | **Report Date** lets users pick a specific date to view data trends for that day. |
| 3 | Time Frame | The **time frame** option lets users choose a period (week, month, quarter, or year) to view data trends. |
| 4 | Sort By |  **Sort By** option helps users organize data by criteria like Volumetrics Count, Name, or Last Scanned for quick access. |
| 5 |  Filter | The filter lets users easily refine results by choosing specific tags or tables to view. |
| 6 |  Favorite | Mark this as a favorite for quick access and easy monitoring in the future. |
| 7 | Table | Displays the table for which the volumetric check is being performed (e.g., customer_view, nation). Each table has its own Volumetric Check. |
| 8 | Check (# ID) | Each check is assigned a unique identifier, followed by the time period it applies to (e.g., 1 Day for the customer table). This ID helps in tracking the specific check in the system. |
| 9 | Weight | Weight shows how important a check is for finding anomalies and sending alerts. |
| 10 | Anomaly Detection | The Volumetric Check detects anomalies when row counts exceed set min or max thresholds, triggering an alert for sudden changes. |
| 11 | Edit Checks | Edit the check to modify settings, or add tags for better customization and monitoring. |
| 12 | Group By  | Users can also Group By specific intervals, such as day, week, or month, to observe trends over different periods. |
| 13 |  Measurement Period  | Defines the time period over which the volumetric check is evaluated. It can be customized to 1 day, week, or other timeframes. |
| 14 |  Comparison  | These indicate the type of comparison used, indicating the "Absolute Value" method. |
| 15 |  Min Values  | These indicate the minimum thresholds for the row count of the table being checked (e.g., 150,139 Rows). |
| 16 |  Max Values | These indicate the maximum thresholds for the row count of the table being checked. |
| 17 |  Last Asserted | This shows the date the last check was asserted, which is the last time the system evaluated the Volumetric Check (e.g., Oct 02, 2024). |
| 18 | Edit Threshold | Edit Threshold lets users set custom limits for alerts, helping them control when they’re notified about changes in data. |
| 19. | Graph Visualization | The graph provides a visual representation of the row count trends. It shows fluctuations in data volume over the selected period. This visual allows users to quickly identify any irregularities or anomalies. |

### Observability Heatmap

The heatmap provides a visual overview of data anomalies by day, using color codes for quick understanding:

![heatmap-square](../assets/observability/heatmap-light.png#only-light)
![heatmap-square](../assets/observability/heatmap-dark.png#only-dark)

- **Blue square**: Blue square represent days with no anomalies, meaning data stayed within the expected range.
- **Orange square**: Orange square indicate days where data exceeded the minimum or maximum threshold range but didn’t qualify as a critical anomaly.
- **Red square**: Red square highlight days with anomalies, signaling significant deviations from expected values that need further investigation.

![heatmap-square](../assets/observability/hover-light.png#only-light)
![heatmap-square](../assets/observability/hover-dark.png#only-dark)

By hovering over each square, you can view additional details for that specific day, including the **date**, **anomaly count**, **last row count**,and **last modification time** allowing you to easily pinpoint and analyze data issues over time.

### Edit Check

Editing a Volumetric Check lets users customize settings like measurement period, row count limits, and description. This helps improve data monitoring and anomaly detection, ensuring the check fits specific needs. Users can also add tags for better organization.

!!! note 
    When editing checks, only the properties and metadata can be modified. 

**Step 1:** Click the edit icon to modify the check.

![edit](../assets/observability/edit-check-light-7.png#only-light)
![edit](../assets/observability/edit-check-dark-7.png#only-dark)

A modal window will appear with the check details.

![observability](../assets/observability/check-light-8.png#only-light)
![observability](../assets/observability/check-dark-8.png#only-dark)

**Step 2:** Modify the check details as needed based on your preferences:

| No | Fields | Description |
| :---- | :---- | :---- |
| 1 | Comparison | Edits the type of comparison to Absolute Change, Absolute Value, or Percentage Change. |
| 2 | Measurement Periods Days | Edit the **Measurement Period Days** to change how often the check runs (e.g., 1 day, 2 days, etc). |
| 3 | Min Value and Max Value | Edit the **Min Value** and **Max Value** to set new row count limits. If the row count exceeds these limits, an alert will be triggered. |
| 4 | Description | Edit the **Description** to better explain what the check does. |
| 5 | Tags | Edit the **Tags** to organize and easily find the check later. |
| 6 | Additional Metadata(Optional) | Edit the **Additional Metadata** section to add any new custom details for more context.  |

![observability](../assets/observability/check-detail-light-9.png#only-light)
![observability](../assets/observability/check-detail-dark-9.png#only-dark)

**Step 3:** Once you have edited the check details, then click on the **Validate** button. This will perform a validation operation on the check without saving it. The validation allows you to verify that the logic and parameters defined for the check are correct.

![observability](../assets/observability/validate-btn-light-10.png#only-light)
![observability](../assets/observability/validate-btn-dark-10.png#only-dark)

If the validation is successful, a green message saying **"Validation Successful"** will appear.

![observability](../assets/observability/validate-btn-light-11.png#only-light)
![observability](../assets/observability/validate-btn-dark-11.png#only-dark)

If the validation fails, a red message saying **"Failed Validation"** will appear. This typically occurs when the check logic or parameters do not match the data properly.

![observability](../assets/observability/failed-light-12.png#only-light)
![observability](../assets/observability/failed-dark-12.png#only-dark)

**Step 3:** Once you have a successful validation, click the **"Update"** button. The system will update the changes you've made to the check, including changes to the properties, description, tags, or additional metadata.

![observability](../assets/observability/update-btn-light-13.png#only-light)
![observability](../assets/observability/update-btn-dark-13.png#only-dark)

After clicking on the Update button, your check is successfully updated and a success flash message will appear stating **"Check successfully updated"**.

![observability](../assets/observability/success-msg-light-14.png#only-light)
![observability](../assets/observability/success-msg-dark-14.png#only-dark)

### Edit Threshold

Edit thresholds to set specific row count limits for your data checks. By defining minimum and maximum values, you ensure alerts are triggered when data goes beyond the expected range. This helps you monitor unusual changes in data volume. It gives you better control over tracking your data's behavior.

!!! note
    When editing the threshold, only the min and max values can be modified.

**Step 1:** Click the **Edit Thresholds** button on the right side of the graph.

![observability](../assets/observability/edit-threshold-light-15.png#only-light)
![observability](../assets/observability/edit-threshold-dark-15.png#only-dark)

**Step 2:** After clicking **Edit Thresholds**, you enter the editing mode where the **Min** and **Max** values become editable, allowing you to input new row count limits.

![observability](../assets/observability/min-max-light-16.png#only-light)
![observability](../assets/observability/min-max-dark-16.png#only-dark)

**Step 3:** Once you've updated the **Min** and **Max** values, click **Save** to apply the changes and update the thresholds.

![observability](../assets/observability/save-btn-light-17.png#only-light)
![observability](../assets/observability/save-btn-dark-17.png#only-dark)

After clicking on the Save button, your threshold is successfully updated and a success flash message will appear stating **"Check successfully updated"**.

![observability](../assets/observability/success-msg-light-18.png#only-light)
![observability](../assets/observability/success-msg-dark-18.png#only-dark)

### Mark Check as Favorite

Marking a Volumetric Check as a favorite allows you to easily access important checks quickly. This feature helps you prioritize and manage the checks you frequently use, making data monitoring more efficient.

**Step 1:** Click on the bookmark icon to mark the Volumetric Check as a favorite.

![observability](../assets/observability/mark-fav-light-19.png#only-light)
![observability](../assets/observability/mark-fav-dark-19.png#only-dark)

After Clicking on the bookmark icon your check is successfully marked as a favorite and a success flash message will appear stating **“Check has been favorited”.**

![observability](../assets/observability/success-msg-light-20.png#only-light)
![observability](../assets/observability/success-msg-dark-20.png#only-dark)

To unmark a check, simply click on the bookmark icon of the marked check. This will remove it from your favorites.

![observability](../assets/observability/fav-btn-light-21.png#only-light)
![observability](../assets/observability/fav-btn-dark-21.png#only-dark)

### **Freshness**

This measures the timeliness of data by monitoring when new data was last added or updated. It helps ensure that data remains up-to-date and relevant for decision-making. Users can view timestamp values in a clear date and time format, making it easier to analyze data freshness while maintaining millisecond-level precision in the background. If data updates are delayed or missing, it may indicate pipeline failures, system lag, or unexpected data source changes. Regular freshness checks prevent outdated information from impacting analytics, reporting, or automated workflows.

![freshness](../assets/observability/freshness-detail-light-666.png#only-light)
![freshness](../assets/observability/freshness-detail-dark-666.png#only-dark)

|     No. |                Field  |                         Description |
| :---- | :---- | :---- |
|      1. |           **Search Bar** | This feature helps users quickly find specific identifiers or names in the data. |
|      2. |          **Report Date** | **Report Date** lets users pick a specific date to view data trends for that day. |
|      3. |         **Timeframe** | The **time frame** option lets users choose a period (week, month, quarter, or year.) to view data trends. |
|      4. |         **Sort By** | **Sort By** option helps users organize data by criteria like Anomalies, Checks, Created Date, Name, or Last Scanned for quick access. |
|      5. |         **Filters** | The filter lets users easily refine results by choosing specific tags or tables to view. |
|      6. |        **Favorite** | Mark this as a favorite for quick access and easy monitoring in the future. |
|      7. |        **Table** | Displays the name of the selected table being analyzed. |
|      8. |       **Weight** | Weight shows how important a check is for finding anomalies and sending alerts. |
|    9. |    **Anomaly Detection** | Represents active anomalies detected in the data. |
|    10. |      **Edit Check** | Edit the check to modify settings, or add tags for better customization. |
|    11. |     **Freshness (# ID)** | Each freshness check is assigned a unique identifier, corresponding to the specified time period it monitors (e.g., 1 Day for the customer table). This identifier facilitates precise tracking and management within the system. |
|    12. |     **Group By** | Users can also Group By specific intervals, such as day, week to observe trends over different periods. |
|    13. |     **Unit** | The unit used to measure data freshness, shown in milliseconds. |
|    14. |     **Maximum Age** | Displays the maximum recorded age of data in milliseconds. |
|    15. |     **Last Asserted** | Shows the latest date when the data was validated or checked. |
|     16. |     **Edit Maximum Age** | Edit **Maximum Age** lets users set custom limits for data freshness, allowing control over when alerts are triggered based on the age of the data. |
|     17. |   **Graph Visualization** |  Graph illustrates consistent data patterns over time, with sudden anomalies marked by spikes in red. It reflects changes in data freshness and highlights when the data was last updated. |

### **Edit Check**

Editing a Check enables users to modify settings such as the unit of measurement, maximum age, description, and metadata. Additionally, they can add tags to streamline organization and retrieval.

**Step 1:** Click the edit icon to modify the check.

![freshness](../assets/observability/modify-detail-light-667.png#only-light)
![freshness](../assets/observability/modify-detail-dark-667.png#only-dark)

A modal window will appear with the check details.

![freshness](../assets/observability/check-detail-light-668.png#only-light)
![freshness](../assets/observability/check-detail-dark-668.png#only-dark)

**Step 2:** Modify the check details as needed based on your preferences:

|     No. |                       Field |                           Description |
| :---- | :---- | :---- |
|     1. |                  Unit | Edit the unit of measurement for the freshness check, such as milliseconds (Millis), Minutes, Hours etc. |
|     2. |           Maximum Age | Edit the maximum allowed age (in the specified unit) for data to be considered fresh. |
|    3. |           Description | Edit the **Description** to better explain what the check does. |
|    4. |           Tags | Edit the **Tags** to organize and easily find the check later. |
|    5. |          Additional Metadata(Optional) | Edit the **Additional Metadata** section to add any new custom details for more context. |

![freshness](../assets/observability/detail-light-669.png#only-light)
![freshness](../assets/observability/detail-dark-669.png#only-dark)

**Step 3:** Once you have edited the check details, then click on the **Validate** button. This will perform a validation operation on the check without saving it. The validation allows you to verify that the logic and parameters defined for the check are correct.

![freshness](../assets/observability/validate-light-670.png#only-light)
![freshness](../assets/observability/validate-dark-670.png#only-dark)

If the validation is successful, a green message saying **"Validation Successful"** will appear.

![freshness](../assets/observability/msg-light-671.png#only-light)
![freshness](../assets/observability/msg-dark-671.png#only-dark)

**Step 4:** Once you have a successful validation, click the **"Update"** button. The system will update the changes you've made to the check, including changes to the properties, description, tags, or additional metadata.

![freshness](../assets/observability/update-light-672.png#only-light)
![freshness](../assets/observability/update-dark-672.png#only-dark)

After clicking on the Update button, your check is successfully updated and a success flash message will appear stating **"Check successfully updated"**.

![freshness](../assets/observability/msg-light-673.png#only-light)
![freshness](../assets/observability/msg-dark-673.png#only-dark)

### Edit Maximum Age

**Maximum Age** sets the limit for how long data can remain unchanged before it’s flagged as outdated. This ensures your data stays fresh and reliable for decision-making.

**Step 1:** Click the **Edit Maximum Age** button on the right side of the graph.

![age](../assets/observability/age-light-674.png#only-light)
![age](../assets/observability/age-dark-674.png#only-dark)

**Step 2:** After clicking  **Edit Maximum Age**, the field becomes editable, allowing you to modify the maximum age value.

![age](../assets/observability/age-light-675.png#only-light)
![age](../assets/observability/age-dark-675.png#only-dark)

**Step 3:** Once you've updated the **maximum age** values, click **Save** to apply the changes.

![age](../assets/observability/save-light-676.png#only-light)
![age](../assets/observability/save-dark-676.png#only-dark)

After clicking on the Save button, a success flash message will appear stating **"Check successfully updated"**.

![age](../assets/observability/msg-light-673.png#only-light)
![age](../assets/observability/msg-dark-673.png#only-dark)

### Metric

Metric track changes in data over time to ensure accuracy and reliability. They check specific fields against set limits to identify when values, like averages, go beyond expected ranges. With scheduled scans, Metrics automatically log and analyze these data points, making it easy for users to spot any issues. This functionality enhances users' understanding of data patterns, ensuring high quality and dependability. With Metrics, managing and monitoring data becomes straightforward and efficient.

![observability](../assets/observability/metric-detail-light-22.png#only-light)
![observability](../assets/observability/metric-detail-dark-22.png#only-dark)

| No | Field | Description |
| :---- | :---- | :---- |
| 1 | Search   | The search bar helps users find specific metrics or data by entering an identifier or description. |
| 2 | Sort By  |  Sort By allows users to organize data by **Weight, Anomalies,** or **Created Date** for easier analysis and prioritization. |
| 3 | Filter | Filter lets users refine data by **Tags** or **Tables**. Use **Apply** to filter or **Clear** to reset. |
| 4 |  Metric(ID) | Represents the tracked data metric with a unique **ID**. |
| 5 |  Description  |  A brief label or note about the metric, in this case, it's labeled as **test**. |
| 6 |  Weight | Weight shows how important a check is for finding anomalies and sending alerts. |
| 7 | Anomalies  |  Anomalies show unexpected changes or issues in the data that need attention. |
| 8 |  Favorite | Mark this as a favorite for quick access and easy monitoring in the future. |
| 9 | Edit Checks  |  Edit the check to modify settings, or add tags for better customization and monitoring. |
| 10 |  Field | This refers to the specific field being measured, here the **max_value,** which tracks the highest value observed for the metric. |
| 11 |  Min  | This indicates the minimum value for the metric, which is set to **1**. If not defined, no lower limit is applied. |
| 12 | Max | This field shows the maximum threshold for the metric, set at **8**. Exceeding this may indicate an issue or anomaly. |
| 13 | Created Date | This field shows when the metric was first set up, in this case, **June 18, 2024.** |
| 14 |  Last Asserted |  Last Asserted field shows the last time the metric was checked, in this case **July 25, 2024.** |
| 15 | Group By  Edit Threshold | Edit Threshold lets users set custom limits for alerts, helping them control when they’re notified about changes in data. |
| 16 | Group By  | This option lets users group data by periods like **Day,** **Week,** or **Month**. In this example, it's set to **Day.**  |

### Comparisons

When you [add a metric](https://userguide.qualytics.io/checks/metric-check/) check, you can choose from three comparison options:

* Absolute Change  
* Absolute Value  
* Percentage Change

These options help define how the system will evaluate your data during scan operations on the datastore.

Once a scan is run, the system analyzes the data based on the selected comparison type. For example, Absolute Change will look for significant differences between scans, Absolute Value checks if the data falls within a predefined range, and Percentage Change identifies shifts in data as a percentage.

Based on the chosen comparison type, the system flags any deviations from the defined thresholds. These deviations are then visually represented on a chart, displaying how the metric has fluctuated over time between scans. If the data crosses the upper or lower limits during any scan, the system will highlight this in the chart for further analysis.

**1. Absolute Change:** The Absolute Change comparison checks how much a numeric field's value has changed between scans. If the change exceeds a set limit (Min/Max), it flags this as an anomaly.

![observability](../assets/observability/change-light-23.png#only-light)
![observability](../assets/observability/change-dark-23.png#only-dark)

**2. Absolute Value:** The Absolute Value comparison checks whether a numeric field's value falls within a defined range (between Min and Max) during each scan. If the value goes beyond this range, it identifies it as an anomaly.

![observability](../assets/observability/value-light-24.png#only-light)
![observability](../assets/observability/value-dark-24.png#only-dark)

**3. Percentage Change:** The Percentage Change comparison monitors how much a numeric field's value has shifted in percentage terms. If the change surpasses the set percentage threshold between scans, it triggers an anomaly.

![observability](../assets/observability/percentage-light-25.png#only-light)
![observability](../assets/observability/percentage-dark-25.png#only-dark)

### Minimum Measurements for Chart Rendering

To display metric charts in the UI, a minimum number of measurements must be recorded. If the required number of measurements is not met, the chart remains empty even though some measurements exist.

* **Absolute Value:** Requires at least 2 measurements to render.

* **Absolute Change:** Requires at least 3 measurements to render.

* **Percentage Change:** Requires at least 3 measurements to render.

These thresholds ensure meaningful visual representation by preventing incomplete or misleading chart data.

### Edit Check

**Edit Check** allows users to modify the parameters of an existing metric check. It enables adjusting values, thresholds, or comparison logic to ensure that the metric accurately reflects current monitoring needs.

!!! note
    When editing checks, only the properties and metadata can be modified.

**Step 1:** Click the edit icon to modify the check.

![observability](../assets/observability/edit-check-light-26.png#only-light)
![observability](../assets/observability/edit-check-dark-26.png#only-dark)

A modal window will appear with the check details.

![observability](../assets/observability/modal-window-light-27.png#only-light)
![observability](../assets/observability/modal-window-dark-27.png#only-dark)

**Step 2:** Modify the check details as needed based on your preferences:

| No | Field | Description |
| :---- | :---- | :---- |
| 1 | Min Value and Max Value   | Edit the **Min Value** and **Max Value** to set new row count limits. If the row count exceeds these limits, an alert will be triggered. |
| 2 | Description | Edit the **Description** to better explain what the check does.  |
| 3 | Tags |  Edit the **Tags** to organize and easily find the check later. |
| 4 | Additional Metadata(Optional) |  Edit the **Additional Metadata** section to add any new custom details for more context.  |

![observability](../assets/observability/check-detail-light-28.png#only-light)
![observability](../assets/observability/check-detail-dark-28.png#only-dark)

**Step 3:** Once you have edited the check details, then click on the **Validate** button. This will perform a validation operation on the check without saving it. The validation allows you to verify that the logic and parameters defined for the check are correct.

![observability](../assets/observability/validate-btn-light-29.png#only-light)
![observability](../assets/observability/validate-btn-dark-29.png#only-dark)

If the validation is successful, a green message saying **"Validation Successful"** will appear.

![observability](../assets/observability/success-msg-light-30.png#only-light)
![observability](../assets/observability/success-msg-dark-30.png#only-dark)

**Step 3:** Once you have a successful validation, click the **"Update"** button. The system will update the changes you've made to the check, including changes to the properties, description, tags, or additional metadata.

![observability](../assets/observability/update-btn-light-31.png#only-light)
![observability](../assets/observability/update-btn-dark-31.png#only-dark)

After clicking on the Update button, your check is successfully updated and a success flash message will appear stating **"Check successfully updated"**.

![observability](../assets/observability/success-msg-light-32.png#only-light)
![observability](../assets/observability/success-msg-dark-32.png#only-dark)

### Edit Threshold

**Edit Threshold** allows you to change the upper and lower limits of a metric. This ensures the metric tracks data within the desired range and only triggers alerts when those limits are exceeded.

!!! note
    When editing the threshold, only the min and max values can be modified.

**Step 1:** Click the **Edit Thresholds** button on the right side of the graph.

![observability](../assets/observability/edit-threshold-light-33.png#only-light)
![observability](../assets/observability/edit-threshold-dark-33.png#only-dark)

**Step 2:** After clicking **Edit Thresholds**, you enter the editing mode where the **Min** and **Max** values become editable, allowing you to input new row count limits.

![observability](../assets/observability/edit-threshold-light-34.png#only-light)
![observability](../assets/observability/edit-threshold-dark-34.png#only-dark)

**Step 3:** Once you've updated the **Min** and **Max** values, click **Save** to apply the changes and update the thresholds.

![observability](../assets/observability/save-btn-light-35.png#only-light)
![observability](../assets/observability/save-btn-dark-35.png#only-dark)

After clicking on the Save button, your threshold is successfully updated and a success flash message will appear stating **"Check successfully updated"**.

![observability](../assets/observability/success-msg-light-36.png#only-light)
![observability](../assets/observability/success-msg-dark-36.png#only-dark)

### Mark Check as Favorite

Marking a Metric Check as a favorite allows you to easily access important checks quickly. This feature helps you prioritize and manage the checks you frequently use, making data monitoring more efficient.

**Step 1:** Click on the bookmark icon to mark the Metric Check as a favorite.

![observability](../assets/observability/fav-light-37.png#only-light)
![observability](../assets/observability/fav-dark-37.png#only-dark)

After Clicking on the bookmark icon your check is successfully marked as a favorite and a success flash message will appear stating **“Check has been favorited”**.

![observability](../assets/observability/success-msg-light-38.png#only-light)
![observability](../assets/observability/success-msg-dark-38.png#only-dark)

To unmark a check, simply click on the bookmark icon of the marked check. This will remove it from your favorites.

![observability](../assets/observability/unfav-light-39.png#only-light)
![observability](../assets/observability/unfav-dark-39.png#only-dark)