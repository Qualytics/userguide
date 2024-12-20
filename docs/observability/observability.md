# Observability

Observability gives users an easy way to track changes in data volume over time. It introduces two types of checks: **Volumetric** and **Metric.** The Volumetric check automatically monitors the number of rows in a table and flags unusual changes, while the Metric check focuses on specific fields, providing more detailed insights from scan operations. Together, these tools help users spot data anomalies quickly and keep their data accurate. 

Let’s get started 🚀

## Navigation

**Step 1:** Log in to your Qualytics account and select the datastore from the left menu that you want to monitor

![datastore](../assets/observability/source-light-1.png#only-light)
![datastore](../assets/observability/source-dark-1.png#only-dark)

**Step 2:** Click on the **“Observability”** from the Navigation tab.

![observability](../assets/observability/observability-light-2.png#only-light)
![observability](../assets/observability/observability-dark-2.png#only-dark)

## Observability Categories

Observability, data checks are divided into two categories: Volumetric and Metric. Volumetric checks track overall data volume, while Metric checks focus on specific data attributes. These two categories work together to offer comprehensive insights into data trends and anomalies.

![category](../assets/observability/category-light-3.png#only-light)
![category](../assets/observability/category-dark-3.png#only-dark)

**1. Volumetric:** Volumetric is a tool that automatically tracks changes in the amount of data within a table over time. It monitors row counts and compares them to expected ranges based on historical data. If the data volume increases or decreases unexpectedly, the check flags it for further review. This feature helps users easily identify unusual data patterns without manual monitoring.

![volumetric](../assets/observability/volumetric-light-4.png#only-light)
![volumetric](../assets/observability/volumetric-dark-4.png#only-dark)

**2. Metric:** Metric measures data based on predefined fields and thresholds, tracking changes in data values over time. It detects if the value of a specific field, like the average or absolute value, goes beyond the expected range. Using scheduled scans, it automatically records and analyzes these values, helping users quickly spot any anomalies. This check gives deeper insights into data behavior, ensuring data integrity and identifying irregular patterns easily.

![metric](../assets/observability/metric-light-5.png#only-light)
![metric](../assets/observability/metric-dark-5.png#only-dark)

### Volumetric

Volumetric help monitor data volumes over time to keep data accurate and reliable. They automatically count rows in a table and spot any unusual changes, like problems with data loading. This makes it easier to catch issues early and keep everything running smoothly. Volumetric checks also let you track data over different time periods, like daily or weekly. The system sets limits based on past data, and if the row count goes above or below those limits, an anomaly alert is triggered.

![details](../assets/observability/volumetric-detail-light-6.png#only-light)
![detail](../assets/observability/volumetric-detail-dark-6.png#only-dark)

| No | Field | Description |
| :---- | :---- | :---- |
| 1 | Search  | This feature helps users quickly find specific identifiers or names in the data. |
| 2 | Report Data | **Report Date** lets users pick a specific date to view data trends for that day. |
| 3 | Time Frame | The **time frame** option lets users choose a period (week, month, quarter, or year.) to view data trends. |
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
| 14 |  Min Values  | These indicate the minimum thresholds for the row count of the table being checked (e.g., 150,139 Rows) |
| 15 |  Max Values. | These indicate the maximum thresholds for the row count of the table being checked |
| 16 |  Last Asserted | This shows the date the last check was asserted, which is the last time the system evaluated the Volumetric Check (e.g., Oct 02, 2024). |
| 17 | Edit Threshold | Edit Threshold lets users set custom limits for alerts, helping them control when they’re notified about changes in data. |
| 18 | Graph Visualization | The graph provides a visual representation of the row count trends. It shows fluctuations in data volume over the selected period. This visual allows users to quickly identify any irregularities or anomalies. |

### Observability Heatmap

The heatmap provides a visual overview of data anomalies by day, using color codes for quick understanding:

![heatmap-square](../assets/observability/heatmap-light.png#only-light)
![heatmap-square](../assets/observability/heatmap-dark.png#only-dark)

- **Blue square**: Blue square represent days with no anomalies, meaning data stayed within the expected range.
- **Orange square**: Orange square indicate days where data exceeded the minimum or maximum threshold range but didn’t qualify as a critical anomaly.
- **Red square**: Red square highlight days with anomalies, signaling significant deviations from expected values that need further investigation.

![heatmap-square](../assets/observability/hover-light.png#only-light)
![heatmap-square](../assets/observability/hover-dark.png#only-dark)

By hovering over each square, you can view additional details for that specific day, including the **date**, **last row count**, and **anomaly count**, allowing you to easily pinpoint and analyze data issues over time.

### Edit Check

Editing a Volumetric Check lets users customize settings like measurement period, row count limits, and description. This helps improve data monitoring and anomaly detection, ensuring the check fits specific needs. Users can also add tags for better organization.

!!! note 
    When editing checks, only the properties and metadata can be modified. |

**Step 1:** Click the edit icon to modify the check.

![edit](../assets/observability/edit-check-light-7.png#only-light)
![edit](../assets/observability/edit-check-dark-7.png#only-dark)

A modal window will appear with the check details.

![observability](../assets/observability/check-light-8.png#only-light)
![observability](../assets/observability/check-dark-8.png#only-dark)

**Step 2:** Modify the check details as needed based on your preferences:

| No | Fields | Description |
| :---- | :---- | :---- |
| 1 | Measurement Periods Days | Edit the **Measurement Period Days** to change how often the check runs (e.g., 1 day, 2 days, etc). |
| 2 | Min Value and Max Value | Edit the **Min Value** and **Max Value** to set new row count limits. If the row count exceeds these limits, an alert will be triggered. |
| 3 | Description | Edit the **Description** to better explain what the check does. |
| 4 | Tags | Edit the **Tags** to organize and easily find the check later. |
| 5 | Additional Metadata(Optional) | Edit the **Additional Metadata** section to add any new custom details for more context.  |

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

### Metric

Metric track changes in data over time to ensure accuracy and reliability. They check specific fields against set limits to identify when values, like averages, go beyond expected ranges. With scheduled scans, Metrics automatically log and analyze these data points, making it easy for users to spot any issues. This functionality enhances users' understanding of data patterns, ensuring high quality and dependability. With Metrics, managing and monitoring data becomes straightforward and efficient.

![observability](../assets/observability/metric-detail-light-22.png#only-light)
![observability](../assets/observability/metric-detail-dark-22.png#only-dark)

| No | Field | Description |
| :---- | :---- | :---- |
| 1 | Search   | The search bar helps users find specific metrics or data by entering an identifier or description. |
| 2 | Sort By  |  Sort By allows users to organize data by **Weight, Anomalies,** or **Created Date** for easier analysis and prioritization. |
| 3 | Filter | Filter lets users refine data by **Tags** or **Tables**. Use **Apply** to filter or **Clear** to reset. |
| 4 |  Metric(ID) | Represents the tracked data metric with a unique ID**.** |
| 5 |  Description  |  A brief label or note about the metric, in this case, it's labeled as **test** |
| 6 |  Weight | Weight shows how important a check is for finding anomalies and sending alerts. |
| 7 | Anomalies  |  Anomalies show unexpected changes or issues in the data that need attention. |
| 8 |  Favorite | Mark this as a favorite for quick access and easy monitoring in the future. |
| 9 | Edit Checks  |  Edit the check to modify settings, or add tags for better customization and monitoring. |
| 10 |  Field | This refers to the specific field being measured, here the **max\_value,** which tracks the highest value observed for the metric. |
| 11 |  Min  | This indicates the minimum value for the metric, which is set to **1**. If not defined, no lower limit is applied. |
| 12 | Max | This field shows the maximum threshold for the metric, set at **8**. Exceeding this may indicate an issue or anomaly. |
| 13 | Created Date | This field shows when the metric was first set up, in this case, **June 18, 2024\.** |
| 14 |  Last Asserted |  Last Asserted field shows the last time the metric was checked, in this case **July 25, 2024\.** |
| 15 | Group By  Edit Threshold | Edit Threshold lets users set custom limits for alerts, helping them control when they’re notified about changes in data. |
| 16 | Group By  | This option lets users group data by periods like **Day,** **Week,** or **Month**. In this example, it's set to **Day.**  |

### Comparisons

When you [add a metric](https://userguide.qualytics.io/checks/metric-check/) check, you can choose from three comparison options: 

* Absolute Change  
* Absolute Value  
* Percentage Change. 

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
    When editing the threshold, only the min and max values can be modified. |

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

After Clicking on the bookmark icon your check is successfully marked as a favorite and a success flash message will appear stating **“Check has been favorited”**

![observability](../assets/observability/success-msg-light-38.png#only-light)
![observability](../assets/observability/success-msg-dark-38.png#only-dark)

To unmark a check, simply click on the bookmark icon of the marked check. This will remove it from your favorites 

![observability](../assets/observability/unfav-light-39.png#only-light)
![observability](../assets/observability/unfav-dark-39.png#only-dark)

