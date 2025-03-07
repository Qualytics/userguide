# Observability

Observability in the Explore section provides structured tracking through **Measures** and **Metrics**, enabling users to monitor data behavior, detect anomalies, and identify trends. **Volume Tracking** analyzes daily data volumes, **Freshness Tracking** ensures data timeliness, and **Metric Tracking** monitors field-specific values against predefined thresholds. Automated scans and visual insights help maintain data integrity. Visual tools like heatmaps and customizable checks make it easy to identify issues, set thresholds, set maximum energy, and adjust monitoring parameters for efficient data management.

Let’s get started 🚀

## Navigation

**Step 1:** Log in to your Qualytics account and click the **Explore** button on the left side panel of the interface.

![explore](../assets/explore/observability/explore-light.png#only-light)
![explore](../assets/explore/observability/explore-dark.png#only-dark)

**Step 2:** Click on the **"Observability"** from the Navigation Tab.

![observability](../assets/explore/observability/observability-light.png#only-light)
![observability](../assets/explore/observability/observability-dark.png#only-dark)

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

Volumetric help monitor data volumes over time to keep data accurate and reliable. They automatically count rows in a table and spot any unusual changes, like problems with data loading. This makes it easier to catch issues early and keep everything running smoothly. Volumetric checks also let you track data over different time periods, like daily or weekly. The system sets limits based on past data, and if the row count goes above or below those limits, an anomaly alert is triggered.

![fields](../assets/explore/observability/fields-light.png#only-light)
![fields](../assets/explore/observability/fields-dark.png#only-dark)

| No | Field | Description |
| :---- | :---- | :---- |
| 1. | Search  | This feature helps users quickly find specific identifiers or names in the data. |
| 2. | Report Data | **Report Date** lets users pick a specific date to view data trends for that day. |
| 3. | Time Frame | The **time frame** option lets users choose a period (week, month, quarter, or year.) to view data trends. |
| 4. | Sort By |  **Sort By** option helps users organize data by criteria like Anoamlies, Created Date, Checks, Name, Type or Last Scanned for quick access. |
| 5. |  Favorite | Mark this as a favorite for quick access and easy monitoring in the future. |
| 6. | Datastore | Displays the Datastore name for which the volumetric check is being performed . |
| 7. | Table | Displays the table for which the volumetric check is being performed (e.g., customer, nation). Each table has its own Volumetric Check. |
| 8. | Weight | Weight shows how important a check is for finding anomalies and sending alerts. |
| 9. | Anomaly Detection | The Volumetric Check detects anomalies when row counts exceed set min or max thresholds, triggering an alert for sudden changes. |
| 10. | Edit Checks | Edit the check to modify settings, or add tags for better customization and monitoring. |
| 11. | Volumetric Check (# ID) | Each check is assigned a unique identifier, followed by the time period it applies to (e.g., 1 Day for the customer table). This ID helps in tracking the specific check in the system. |
| 12. | Group By | Users can also Group By specific intervals, such as day, week, or month, to observe trends over different periods. |
| 13. | Measurement Period | Defines the time period over which the volumetric check is evaluated. It can be customized to 1 day, week, or other timeframes. |
| 14. | Comparision | These indicate the comparision type Absolute value, Percentage Value and Absolute Change. |
| 15. |  Min Values  | These indicate the minimum thresholds for the row count of the table being checked (e.g., 150,139 Rows) |
| 16. |  Max Values. | These indicate the maximum thresholds for the row count of the table being checked |
| 17. |  Last Asserted | This shows the date the last check was asserted, which is the last time the system evaluated the Volumetric Check (e.g., Oct 02, 2024). |
| 18. | Edit Threshold | Edit Threshold lets users set custom limits for alerts, helping them control when they’re notified about changes in data. |
| 19. | Graph Visualization | The graph provides a visual representation of the row count trends. It shows fluctuations in data volume over the selected period. This visual allows users to quickly identify any irregularities or anomalies. |

### Observability Heatmap

The heatmap provides a visual overview of data anomalies by day, using color codes for quick understanding:

* **Blue square**: Blue square represent days with no anomalies, meaning data stayed within the expected range.

* **Orange square**: Orange square indicate days where data exceeded the minimum or maximum threshold range but didn’t qualify as a critical anomaly.

* **Red square**: Red square highlight days with anomalies, signaling significant deviations from expected values that need further investigation.

![heatmap](../assets/explore/observability/heatmap-light.png#only-light)
![heatmap](../assets/explore/observability/heatmap-dark.png#only-dark)

By hovering over each square, you can view additional details for that specific day, including the **date**, **last row count**, and **anomaly count**, allowing you to easily pinpoint and analyze data issues over time.

![hover](../assets/explore/observability/hover-light.png#only-light)
![hover](../assets/explore/observability/hover-dark.png#only-dark)

### Edit Check

Editing a Volumetric Check lets users customize settings like measurement period, row count limits, and description. This helps improve data monitoring and anomaly detection, ensuring the check fits specific needs. Users can also add tags for better organization.

**Step 1:** Click the edit icon to modify the check.

![edit](../assets/explore/observability/edit-light.png#only-light)
![edit](../assets/explore/observability/edit-dark.png#only-dark)

A modal window will appear with the check details.

![window](../assets/explore/observability/window-light.png#only-light)
![window](../assets/explore/observability/window-dark.png#only-dark)

**Step 2:** Modify the check details as needed based on your preferences:

| No |              Fields |                      Description |
| :---- | :---- | :---- |
| 1 | Comparision | Edits the type of comparison to Absolute Change, Absolute Value, or Percentage Change. |
| 2. | Measurement Periods Days | Edit the **Measurement Period Days** to change how often the check runs (e.g., 1 day, 2 days, etc). |
| 3. | Min Value and Max Value | Edit the **Min Value** and **Max Value** to set new row count limits. If the row count exceeds these limits, an alert will be triggered. |
| 4. | Description | Edit the **Description** to better explain what the check does. |
| 5. | Tags | Edit the **Tags** to organize and easily find the check later. |
| 6. | Additional Metadata(Optional) | Edit the **Additional Metadata** section to add any new custom details for more context. |

![details](../assets/explore/observability/details-light.png#only-light)
![details](../assets/explore/observability/details-dark.png#only-dark)

**Step 3:** Once you have edited the check details, then click on the **Validate** button. This will perform a validation operation on the check without saving it. The validation allows you to verify that the logic and parameters defined for the check are correct.

![validate](../assets/explore/observability/validate-light.png#only-light)
![validate](../assets/explore/observability/validate-dark.png#only-dark)

If the validation is successful, a green message saying **"Validation Successful"** will appear.

![success](../assets/explore/observability/success-light.png#only-light)
![success](../assets/explore/observability/success-dark.png#only-dark)

If the validation fails, a red message saying **"Failed Validation"** will appear. This typically occurs when the check logic or parameters do not match the data properly.

![failed](../assets/explore/observability/failed-light.png#only-light)
![failed](../assets/explore/observability/failed-dark.png#only-dark)

**Step 3:** Once you have a successful validation, click the **"Update"** button. The system will update the changes you've made to the check, including changes to the properties, description, tags, or additional metadata.

![update](../assets/explore/observability/update-light.png#only-light)
![update](../assets/explore/observability/update-dark.png#only-dark)

After clicking on the Update button, your check is successfully updated and a success flash message will appear stating **"Check successfully updated"**.

![msg](../assets/explore/observability/msg-light.png#only-light)
![msg](../assets/explore/observability/msg-dark.png#only-dark)

### Edit Threshold

Edit thresholds to set specific row count limits for your data checks. By defining minimum and maximum values, you ensure alerts are triggered when data goes beyond the expected range. This helps you monitor unusual changes in data volume. It gives you better control over tracking your data's behavior.

!!! note 
    When Editing the threshold, only the min and max values can be modified. 

**Step 1:**  Click the **Edit Thresholds** button on the right side of the graph.

![threshold](../assets/explore/observability/threshold-light.png#only-light)
![threshold](../assets/explore/observability/threshold-dark.png#only-dark)

**Step 2:** After clicking **Edit Thresholds**, you enter the editing mode where the **Min** and **Max** values become editable, allowing you to input new row count limits.

![min](../assets/explore/observability/min-light.png#only-light)
![min](../assets/explore/observability/min-dark.png#only-dark)

**Step 3:** Once you've updated the **Min** and **Max** values, click **Save** to apply the changes and update the thresholds.

![save](../assets/explore/observability/save-light.png#only-light)
![save](../assets/explore/observability/save-dark.png#only-dark)

After clicking on the Save button, your threshold is successfully updated and a success flash message will appear stating **"Check successfully updated"**.

![msg](../assets/explore/observability/msg-light.png#only-light)
![msg](../assets/explore/observability/msg-dark.png#only-dark)

### Freshness

This measures the timeliness of data by monitoring when new data was last added or updated. It helps ensure that data remains up-to-date and relevant for decision-making. If data updates are delayed or missing, it may indicate pipeline failures, system lag, or unexpected data source changes. Regular freshness checks prevent outdated information from impacting analytics, reporting, or automated workflows.

![freshness](../assets/explore/observability/freshness-light.png#only-light)
![freshness](../assets/explore/observability/freshness-dark.png#only-dark)

| No. | Field | Description |
| :---- | :---- | :---- |
| 1. | **Search Bar** | This feature helps users quickly find specific identifiers or names in the data. |
| 2. | **Report Date** | **Report Date** lets users pick a specific date to view data trends for that day. |
| 3. | **Timeframe** | The **time frame** option lets users choose a period (week, month, quarter, or year.) to view data trends. |
| 4. | **Sort By** | **Sort By** option helps users organize data by criteria like Anomalies, Checks, Created Date, Name, or Last Scanned for quick access. |
| 5. | **Favorite** | Mark this as a favorite for quick access and easy monitoring in the future. |
| 6. | **Datastore** | Displays the Datastore name for which the freshness check is being performed . |
| 7. | **Table** | Displays the name of the selected table being analyzed. |
| 8. | **Weight** | Weight shows how important a check is for finding anomalies and sending alerts. |
| 9. | **Anomaly Detection** | Represents active anomalies detected in the data. |
| 10. | **Edit Check** | Edit the check to modify settings, or add tags for better customization. |
| 11. | **Freshness (# ID)** | Each freshness check is assigned a unique identifier, corresponding to the specified time period it monitors (e.g., 1 Day for the customer table). This identifier facilitates precise tracking and management within the system. |
| 12. | **Group By** | Users can also Group By specific intervals, such as day, week to observe trends over different periods. |
| 13. | **Unit** | The unit used to measure data freshness, shown in milliseconds. |
| 14. | **Maximum Age** | Displays the maximum recorded age of data in milliseconds. |
| 15. | **Last Asserted** | Shows the latest date when the data was validated or checked. |
| 16. | **Edit Maximum Age** | Edit **Maximum Age** lets users set custom limits for data freshness, allowing control over when alerts are triggered based on the age of the data. |
| 17. | **Graph Visualization** | Graph illustrates consistent data patterns over time, with sudden anomalies marked by spikes in red. It reflects changes in data freshness and highlights when the data was last updated. |

### Edit Check

Editing a Check enables users to modify settings such as the unit of measurement, maximum age, description, and metadata. Additionally, they can add tags to streamline organization and retrieval.

**Step 1:** Click the edit icon to modify the check.

![freshness](../assets/explore/observability/icons-light.png#only-light)
![freshness](../assets/explore/observability/icons-dark.png#only-dark)

A modal window will appear with the check details.

![freshness](../assets/explore/observability/windows-light.png#only-light)
![freshness](../assets/explore/observability/windows-dark.png#only-dark)

**Step 2:** Modify the check details as needed based on your preferences:

| No. | Field | Description |
| :---- | :---- | :---- |
| 1. | Unit | Edit the unit of measurement for the freshness check, such as milliseconds (Millis), Minutes, Hours etc. |
| 2. | Maximum Age | Edit the maximum allowed age (in the specified unit) for data to be considered fresh. |
| 3. | Description | Edit the **Description** to better explain what the check does. |
| 4. | Tags | Edit the **Tags** to organize and easily find the check later. |
| 5. | Additional Metadata(Optional) | Edit the **Additional Metadata** section to add any new custom |

![table](../assets/explore/observability/tabless-light.png#only-light)
![table](../assets/explore/observability/tabless-dark.png#only-dark)

**Step 3:** Once you have edited the check details, then click on the **Validate** button. This will perform a validation operation on the check without saving it. The validation allows you to verify that the logic and parameters defined for the check are correct.

![validate](../assets/explore/observability/validates-light.png#only-light)
![validate](../assets/explore/observability/validates-dark.png#only-dark)

If the validation is successful, a green message saying **"Validation Successful"** will appear.

![freshness](../assets/explore/observability/mesg-light.png#only-light)
![freshness](../assets/explore/observability/mesg-dark.png#only-dark)

**Step 4:** Once you have a successful validation, click the **"Update"** button. The system will update the changes you've made to the check, including changes to the properties, description, tags, or additional metadata.

![freshness](../assets/explore/observability/updates-light.png#only-light)
![freshness](../assets/explore/observability/updates-dark.png#only-dark)

After clicking on the Update button, your check is successfully updated and a success flash message will appear stating **"Check successfully updated"**.

![freshness](../assets/explore/observability/mesgs-light.png#only-light)
![freshness](../assets/explore/observability/mesgs-dark.png#only-dark)

### Edit Maximum Age

**Maximum Age** sets the limit for how long data can remain unchanged before it’s flagged as outdated. This ensures your data stays fresh and reliable for decision-making.

**Step 1:** Click the **Edit Maximum Age** button on the right side of the graph.

![freshness](../assets/explore/observability/age-light.png#only-light)
![freshness](../assets/explore/observability/age-dark.png#only-dark)

**Step 2:** After clicking **Edit Maximum Age**, the field becomes editable, allowing you to modify the maximum age value.

![freshness](../assets/explore/observability/editables-light.png#only-light)
![freshness](../assets/explore/observability/editables-dark.png#only-dark)

**Step 3:** Once you've updated the **maximum age** values, click **Save** to apply the changes.

![freshness](../assets/explore/observability/saves-light.png#only-light)
![freshness](../assets/explore/observability/saves-dark.png#only-dark)

After clicking on the Save button, a success flash message will appear stating **"Check successfully updated"**.

![freshness](../assets/explore/observability/msg-light.png#only-light)
![freshness](../assets/explore/observability/msg-dark.png#only-dark)

## Metric

Metric track changes in data over time to ensure accuracy and reliability. They check specific fields against set limits to identify when values, like averages, go beyond expected ranges. With scheduled scans, Metrics automatically log and analyze these data points, making it easy for users to spot any issues. This functionality enhances users' understanding of data patterns, ensuring high quality and dependability. With Metrics, managing and monitoring data becomes straightforward and efficient.

![field](../assets/explore/observability/field-light.png#only-light)
![field](../assets/explore/observability/field-dark.png#only-dark)

| No | Field | Description |
| :---- | :---- | :---- |
| 1 | Select Source Datastore | Select specific source datastores to focus on their data. |
| 2 | Tag | Filter data by specific tags to categorize and refine results. |
| 3 | Search   | The search bar helps users find specific metrics or data by entering an identifier or description. |
| 4 | Sort By  |  Sort By allows users to organize data by **Weight, Anomalies,** or **Created Date** for easier analysis and prioritization. |
| 5 |  Metric(ID) | Represents the tracked data metric with a unique ID**.** |
| 6 | Datastore | Shows the Datastore name. |
| 7 | Table | Shows the table name. |
| 8 |  Description  |  A brief label or note about the metric, in this case, it's labeled as **test** |
| 9 |  Weight | Weight shows how important a check is for finding anomalies and sending alerts. |
| 10 | Anomalies  |  Anomalies show unexpected changes or issues in the data that need attention. |
| 11 |  Favorite | Mark this as a favorite for quick access and easy monitoring in the future. |
| 12 | Edit Checks  |  Edit the check to modify settings, or add tags for better customization and monitoring. |
| 13 |  Field | This refers to the specific field being measured, here the **max\_value,** which tracks the highest value observed for the metric. |
| 14 |  Min  | This indicates the minimum value for the metric, which is set to **1**. If not defined, no lower limit is applied. |
| 15 | Max | This field shows the maximum threshold for the metric, set at **8**. Exceeding this may indicate an issue or anomaly. |
| 16 | Created Date | This field shows when the metric was first set up, in this case, **June 18, 2024\.** |
| 17 |  Last Asserted |  Last Asserted field shows the last time the metric was checked, in this case **July 25, 2024\.** |
| 18 |  Edit Threshold | Edit Threshold lets users set custom limits for alerts, helping them control when they’re notified about changes in data. |
| 19 | Group By  | This option lets users group data by periods like **Day,** **Week,** or **Month**. In this example, it's set to **Day.**  |

### Comparisons

When you add a metric check, you can choose from three comparison options:

* Absolute Change  
* Absolute Value  
* Percentage Change.

These options help define how the system will evaluate your data during scan operations on the datastore.

Once a scan is run, the system analyzes the data based on the selected comparison type. For example, Absolute Change will look for significant differences between scans, Absolute Value checks if the data falls within a predefined range, and Percentage Change identifies shifts in data as a percentage.

Based on the chosen comparison type, the system flags any deviations from the defined thresholds. These deviations are then visually represented on a chart, displaying how the metric has fluctuated over time between scans. If the data crosses the upper or lower limits during any scan, the system will highlight this in the chart for further analysis.

**1. Absolute Change:** The Absolute Change comparison checks how much a numeric field's value has changed between scans. If the change exceeds a set limit (Min/Max), it flags this as an anomaly.

![absolute](../assets/explore/observability/absolute-light.png#only-light)
![absolute](../assets/explore/observability/absolute-dark.png#only-dark)

**2. Absolute Value:** The Absolute Value comparison checks whether a numeric field's value falls within a defined range (between Min and Max) during each scan. If the value goes beyond this range, it identifies it as an anomaly.

![value](../assets/explore/observability/value-light.png#only-light)
![value](../assets/explore/observability/value-dark.png#only-dark)

**3. Percentage Change:** The Percentage Change comparison monitors how much a numeric field's value has shifted in percentage terms. If the change surpasses the set percentage threshold between scans, it triggers an anomaly.

![percentage](../assets/explore/observability/percentage-light.png#only-light)
![percentage](../assets/explore/observability/percentage-dark.png#only-dark)

### Edit Check

**Edit Check** allows users to modify the parameters of an existing metric check. It enables adjusting values, thresholds, or comparison logic to ensure that the metric accurately reflects current monitoring needs.

**Step 1:** Click the edit icon to modify the check.

![icon](../assets/explore/observability/icon-light.png#only-light)
![icon](../assets/explore/observability/icon-dark.png#only-dark)

A modal window will appear with the check details.

![modal](../assets/explore/observability/modal-light.png#only-light)
![modal](../assets/explore/observability/modal-dark.png#only-dark)

**Step 2:** Modify the check details as needed based on your preferences:

| No | Field | Description |
| :---- | :---- | :---- |
| 1. | Min Value and Max Value | Edit the **Min Value** and **Max Value** to set new row count limits. If the row count exceeds these limits, an alert will be triggered. |
| 2. | Description | Edit the **Description** to better explain what the check does. |
| 3. | Tags | Edit the **Tags** to organize and easily find the check later. |
| 4. | Additional Metadata(Optional) | Edit the **Additional Metadata** section to add any new custom details for more context. |

![detailss](../assets/explore/observability/detailss-light.png#only-light)
![detailss](../assets/explore/observability/detailss-dark.png#only-dark)

**Step 3:** Once you have edited the check details, then click on the **Validate** button. This will perform a validation operation on the check without saving it. The validation allows you to verify that the logic and parameters defined for the check are correct.

![validatee](../assets/explore/observability/validatee-light.png#only-light)
![validatee](../assets/explore/observability/validatee-dark.png#only-dark)

If the validation is successful, a green message saying **"Validation Successful"** will appear.

![successs](../assets/explore/observability/successs-light.png#only-light)
![successs](../assets/explore/observability/successs-dark.png#only-dark)

**Step 4:** Once you have a successful validation, click the **"Update"** button. The system will update the changes you've made to the check, including changes to the properties, description, tags, or additional metadata.

![updatee](../assets/explore/observability/updatee-light.png#only-light)
![updatee](../assets/explore/observability/updatee-dark.png#only-dark)

After clicking on the Update button, your check is successfully updated and a success flash message will appear stating **"Check successfully updated"**.

![msg](../assets/explore/observability/msg-light.png#only-light)
![msg](../assets/explore/observability/msg-dark.png#only-dark)

### Edit Threshold

**Edit Threshold** allows you to change the upper and lower limits of a metric. This ensures the metric tracks data within the desired range and only triggers alerts when those limits are exceeded.

!!! note 
    When editing the threshold, only the min and max values can be modified. 

**Step 1:** Click the **Edit Thresholds** button on the right side of the graph.

![thresholdss](../assets/explore/observability/thresholdss-light.png#only-light)
![thresholdss](../assets/explore/observability/thresholdss-dark.png#only-dark)

**Step 2:** After clicking **Edit Thresholds**, you enter the editing mode where the **Min** and **Max** values become editable, allowing you to input new row count limits.

![max](../assets/explore/observability/max-light.png#only-light)
![max](../assets/explore/observability/max-dark.png#only-dark)

**Step 3:** Once you've updated the **Min** and **Max** values, click **Save** to apply the changes and update the thresholds.

![savee](../assets/explore/observability/savee-light.png#only-light)
![savee](../assets/explore/observability/savee-dark.png#only-dark)

After clicking on the Save button, your threshold is successfully updated and a success flash message will appear stating **"Check successfully updated"**.

![msg](../assets/explore/observability/msg-light.png#only-light)
![msg](../assets/explore/observability/msg-dark.png#only-dark)
