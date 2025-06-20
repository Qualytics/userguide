# Anomalies in Datastore

Anomalies in Qualytics are indicators of data that deviate from expected patterns or defined quality rules, often pointing to inconsistencies, errors, or unusual behavior within your datasets. These anomalies can arise when records or columns fail to meet validation checks—whether those checks are inferred by the system or authored manually by users.

Let’s get started 🚀

## Navigation

**Step 1:** Log in to your Qualytics account and select the datastore from the left menu on which you want to manage your anomalies.

![datastore](../assets/datastores/anomalies-datastore/datastore-light-1.png#only-light)
![datastore](../assets/datastores/anomalies-datastore/datastore-dark-1.png#only-dark)

**Step 2:** Click on the **“Anomalies”** from the Navigation Tab.

![anomalies](../assets/datastores/anomalies-datastore/anomalies-light-2.png#only-light)
![anomalies](../assets/datastores/anomalies-datastore/anomalies-dark-2.png#only-dark)

## Anomaly Status Categories

Anomalies exist in one of five distinct statuses, which are grouped into two broad categories:

### Open Anomalies

By selecting Open Anomalies, you can view anomalies that have been detected but remain unacknowledged or unresolved. These anomalies require attention and may need further investigation or corrective action.

![open-anomalies](../assets/datastores/anomalies-datastore/open-anomalies-light-2.png#only-light)
![open-anomalies](../assets/datastores/anomalies-datastore/open-anomalies-dark-2.png#only-dark)

This option helps focus on unaddressed issues while allowing seamless navigation to **All**, **Active**, or **Acknowledged** anomalies as needed.

**1. Active**: By selecting **Active Anomalies**, you can focus on anomalies that are currently unresolved or require immediate attention. These are the anomalies that are still in play and have not yet been acknowledged, archived, or resolved.

![active-anomalies](../assets/datastores/anomalies-datastore/active-anomalies-light-4.png#only-light)
![active-anomalies](../assets/datastores/anomalies-datastore/active-anomalies-dark-4.png#only-dark)

**2. Acknowledged**: By selecting **Acknowledged Anomalies**, you can see all anomalies that have been reviewed and marked as acknowledged. This status indicates that the anomalies have been noted, though they may still require further action.

![acknowledged-anomalies](../assets/datastores/anomalies-datastore/acknowledged-anomalies-light-5.png#only-light)
![acknowledged-anomalies](../assets/datastores/anomalies-datastore/acknowledged-anomalies-dark-5.png#only-dark)

**3. All**: By selecting **All Anomalies**, you can view the complete list of anomalies, regardless of their status. This option helps you get a comprehensive overview of all issues that have been detected, whether they are currently active, acknowledged, or archived.

![all-anomalies](../assets/datastores/anomalies-datastore/all-anomalies-light-3.png#only-light)
![all-anomalies](../assets/datastores/anomalies-datastore/all-anomalies-dark-3.png#only-dark)

### Archived Anomalies

By selecting **Archived Anomalies**, you can view anomalies that have been resolved or moved out of active consideration. Archiving anomalies allows you to keep a record of past issues without cluttering the active list.

![archived-anomalies](../assets/datastores/anomalies-datastore/archived-anomalies-light-6.png#only-light)
![archived-anomalies](../assets/datastores/anomalies-datastore/archived-anomalies-dark-6.png#only-dark)

You can also categorize the archived anomalies based on their status as **Resolved**, **Duplicate** and **Invalid**, to manage and review them effectively.

**1. Resolved**: This indicates that the anomaly was a legitimate data quality concern and has been addressed.

![resolved](../assets/datastores/anomalies-datastore/resolved-light-7.png#only-light)
![resolved](../assets/datastores/anomalies-datastore/resolved-dark-7.png#only-dark)

**2. Duplicate**: This indicates that the anomaly is a duplicate of an existing record and has already been addressed.

![duplicate](../assets/datastores/anomalies-datastore/duplicate-light.png#only-light)
![duplicate](../assets/datastores/anomalies-datastore/duplicate-dark.png#only-dark)

**3. Invalid**: This indicates that the anomaly is not a legitimate data quality concern and does not require further action.

![invalid](../assets/datastores/anomalies-datastore/invalid-light-8.png#only-light)
![invalid](../assets/datastores/anomalies-datastore/invalid-dark-8.png#only-dark)

**4. All**: Displays all archived anomalies, including those marked as Resolved, Duplicate, and Invalid, giving a comprehensive view of all past issues. 

![all](../assets/datastores/anomalies-datastore/all-light-9.png#only-light)
![all](../assets/datastores/anomalies-datastore/all-dark-9.png#only-dark)

## Anomaly Details

Anomaly Details View provides key insights into a specific data anomaly, including its status, anomalous record count, failed checks, and weight. It also shows when the anomaly was detected, the triggering scan, and the related datastore, table, and location. This view helps users quickly understand the scope and source of the anomaly for easier investigation and resolution.

**Step 1:** Click on the anomaly that you want to see the details of.

![anomaly-details](../assets/datastores/anomalies-datastore/anomaly-details-light-1.png#only-light)
![anomaly-details](../assets/datastores/anomalies-datastore/anomaly-details-dark-1.png#only-dark)

You will be navigated to the detail section, where you can view the **Summary**, **Failed Checks**, **Source Records** and **Activity** information.

![anomaly-details-view](../assets/datastores/anomalies-datastore/anomaly-details-view-light.png#only-light)
![anomaly-details-view](../assets/datastores/anomalies-datastore/anomaly-details-view-dark.png#only-dark)

### Summary Section

The **Summary** section provides a quick overview of the anomaly's key attributes. It includes the anomaly’s status, total anomalous records, failed checks, weight, detection time, scan information, and the corresponding datastore and table. This section helps users quickly understand where the anomaly occurred and its potential impact.

![summary](../assets/datastores/anomalies-datastore/summary-light.png#only-light)
![summary](../assets/datastores/anomalies-datastore/summary-dark.png#only-dark)

**1. Status and Type:** Shows the current state and category of the anomaly. In this case, the anomaly is **Active** and of type **Shape**, indicating it relates to the structure or distribution of the data.

![status](../assets/datastores/anomalies-datastore/status-light.png#only-light)
![status](../assets/datastores/anomalies-datastore/status-dark.png#only-dark)

**2. Anomalous Records:** Indicates the total number of records affected by the anomaly. Here, **102** records were identified as anomalous.

![anomalous-records](../assets/datastores/anomalies-datastore/anomalous-records-light.png#only-light)
![anomalous-records](../assets/datastores/anomalies-datastore/anomalous-records-dark.png#only-dark)

**3. Failed Check:** Displays the number of data quality checks that were violated and triggered this anomaly. In this instance, **1** check was failed.

![failed-check](../assets/datastores/anomalies-datastore/failed-check-light.png#only-light)
![failed-check](../assets/datastores/anomalies-datastore/failed-check-dark.png#only-dark)

**4. Weight:** Represents the significance or impact of the anomaly. A higher weight value implies a more critical issue. This anomaly has a weight of **8**.

![weight](../assets/datastores/anomalies-datastore/weight-light.png#only-light)
![weight](../assets/datastores/anomalies-datastore/weight-dark.png#only-dark)

**5. Detected:** Shows how long ago the anomaly was first detected.

![detected](../assets/datastores/anomalies-datastore/detected-light.png#only-light)
![detected](../assets/datastores/anomalies-datastore/detected-dark.png#only-dark)

When you hover over the time the anomaly was detected, a pop-up appears displaying the complete date and time.

![detected-at](../assets/datastores/anomalies-datastore/detected-at-light.png#only-light)
![detected-at](../assets/datastores/anomalies-datastore/detected-at-dark.png#only-dark)

**6. Scan:** Indicates the scan operation that detected the anomaly. Scan ID **#21379** is shown here, and it was an incremental scan.

![scan](../assets/datastores/anomalies-datastore/scan-light.png#only-light)
![scan](../assets/datastores/anomalies-datastore/scan-dark.png#only-dark)

!!! info 
    When you click on the expand icon , then you will be directed to the Scan Results page where you can view the specific scan that detected the anomaly.

**7. Source Datastore:** Identifies the dataset where the anomaly was found. This anomaly was found in the **Qualytics Databricks POC** datastore.

![source-datastore-section](../assets/datastores/anomalies-datastore/source-datastore-section-light.png#only-light)
![source-datastore-section](../assets/datastores/anomalies-datastore/source-datastore-section-dark.png#only-dark)

!!! info 
    Clicking on the expand icon opens a detailed view and navigates to the dataset’s page, providing more information about the source datastore where the anomaly was found.

**8. Table:** Points to the specific table involved in the anomaly. The affected table is **raw_order**.

![table](../assets/datastores/anomalies-datastore/table-light.png#only-light)
![table](../assets/datastores/anomalies-datastore/table-dark.png#only-dark)

!!! info 
    Clicking on the expand icon navigates to the table’s page, providing more in-depth information about the table structure and contents.

**9. Location:** Displays the full path of the table in the datastore. This helps users trace the exact location of the anomaly within the data pipeline.

![location](../assets/datastores/anomalies-datastore/location-light.png#only-light)
![location](../assets/datastores/anomalies-datastore/location-dark.png#only-dark)

You can click on the **copy** icon to copy the full location path of the table where the anomaly was detected.

![copy-location](../assets/datastores/anomalies-datastore/copy-location-light.png#only-light)
![copy-location](../assets/datastores/anomalies-datastore/copy-location-dark.png#only-dark)

**10. Tags:** Highlights the severity or categorization of the anomaly. The tag **High** indicates a high-priority issue.

![tags](../assets/datastores/anomalies-datastore/tags-light.png#only-light)
![tags](../assets/datastores/anomalies-datastore/tags-dark.png#only-dark)

#### Copy Anomaly Link

Click on the **Copy Anomaly Link** icon(represented by share icon) located at the right corner of the summary section to copy a direct link to the selected anomaly. 

![copy-anomaly](../assets/datastores/anomalies-datastore/copy-anomaly-light.png#only-light)
![copy-anomaly](../assets/datastores/anomalies-datastore/copy-anomaly-dark.png#only-dark)

You can then use this link for easy access to the specific anomaly.

#### Copy Anomaly UUID

Click the **Copy Anomaly UUID** icon (represented by the key icon) located at the top-right corner of the Summary section to copy the unique identifier of the anomaly. This UUID can be used for reference, tracking, or integration with other tools.

![copy-id](../assets/datastores/anomalies-datastore/copy-id-light.png#only-light)
![copy-id](../assets/datastores/anomalies-datastore/copy-id-dark.png#only-dark)

#### Copy Anomaly Fingerprint

Click on the **Copy Anomaly Fingerprint** icon (represented by fingerprint icon) located at the top right corner of the Summary section to copy a unique identifier that represents the structural and behavioral characteristics of an anomaly. This fingerprint helps in tracking and comparing anomalies across different datasets or timeframes.

![copy-fingerprint](../assets/datastores/anomalies-datastore/copy-fingerprint-light.png#only-light)
![copy-fingerprint](../assets/datastores/anomalies-datastore/copy-fingerprint-dark.png#only-dark)

**View Related Anomalies**

The **View Related Anomalies** option helps users identify and analyze anomalies that share the same fingerprint. It groups together anomalies that share the same violation rule, affected field, and anomalous record pattern.

**Step 1:** Click on **View Related Anomalies** option to view anomalies associated with the same fingerprint.

![view-anomalies](../assets/datastores/anomalies-datastore/view-anomalies-light.png#only-light)
![view-anomalies](../assets/datastores/anomalies-datastore/view-anomalies-dark.png#only-dark)

A panel will open on the right side, listing related anomalies with the same violation rule, field and record pattern.

![related-anomalies](../assets/datastores/anomalies-datastore/related-anomalies-light.png#only-light)
![related-anomalies](../assets/datastores/anomalies-datastore/related-anomalies-dark.png#only-dark)

**Step 2:** Click on the anomaly from the list of related anomalies to view its details.

![click-anomaly](../assets/datastores/anomalies-datastore/click-anomaly-light.png#only-light)
![click-anomaly](../assets/datastores/anomalies-datastore/click-anomaly-dark.png#only-dark)

A modal window titled **“Anomaly Details”** will appear, displaying all the details of the selected anomaly.

![anomaly-details](../assets/datastores/anomalies-datastore/anomaly-details-light.png#only-light)
![anomaly-details](../assets/datastores/anomalies-datastore/anomaly-details-dark.png#only-dark)

For more details on Anomaly Details, please refer to the [**Anomaly Details**](../anomalies/anomalies.md#anomaly-details) section in the documentation.

### Failed Checks

The **Failed Checks** section lists the data quality checks that were violated and subsequently triggered the anomaly. Each listed item displays the check ID, type of violation, and a summarized description of the failure condition.

![failed-checks-section](../assets/datastores/anomalies-datastore/failed-checks-section-light.png#only-light)
![failed-checks-section](../assets/datastores/anomalies-datastore/failed-checks-section-dark.png#only-dark)

Click on a failed check to view the corresponding quality check information.

![check](../assets/datastores/anomalies-datastore/check-light.png#only-light)
![check](../assets/datastores/anomalies-datastore/check-dark.png#only-dark)

A right-side panel will open, allowing you to view the details without navigating to a different page.

![right-panel](../assets/datastores/anomalies-datastore/right-panel-light.png#only-light)
![right-panel](../assets/datastores/anomalies-datastore/right-panel-dark.png#only-dark)

| No. | Field | Description |
| :---- | :---- | :---- |
| **1** | **Check ID & Name** | This is the name and unique number of the check. It’s checking if dates fall within a specific range. |
| **2** | **Description** | Tells you what this check is doing. Here it is making sure values are between a minimum and maximum time. |
| **3** | **Tags** | Shows how important this issue is. In this case, it's marked as **High** priority. |
| **4** | **Table** | The name of the dataset or table where this issue was found. |
| **5** | **Field** | The specific column being checked. Here it is LAST_UPDATED_DATE. |
| **6** | **Filter Clause** | Lets you narrow down the data being checked. No filter is applied here. |
| **7** | **Min** | The earliest allowed date/time value. Anything before this is marked as failed. |
| **8** | **Max** | The latest allowed date/time value. Anything after this is marked as failed. |
| **9** | **Coverage** | Defines how many records must meet the condition. A 100% coverage means all records must comply with this check. |

![check-fields](../assets/datastores/anomalies-datastore/check-fields-light.png#only-light)
![check-fields](../assets/datastores/anomalies-datastore/check-fields-dark.png#only-dark)

#### Filter by Anomalous Fields

The **Filter by anomalous fields** section enables users to refine failed checks by selecting specific fields where anomalies were detected, helping to focus the analysis on relevant data issues.

![filter](../assets/datastores/anomalies-datastore/filter-light.png#only-light)
![filter](../assets/datastores/anomalies-datastore/filter-dark.png#only-dark)

| No. | Filter | Description |
| :---- | :---- | :---- |
| **1** | **All** | Selects or deselects all anomalous fields at once for bulk filtering. |
| **2** | **LAST_UPDATED_DATE** | Filters records based on anomalies detected in the LAST_UPDATED_DATE field. A clock icon indicates it's a date/time field, and the red badge shows active checks or issues associated with it. |

#### Failed Check Description

This allows users to view detailed explanations of each failed check by hovering over the information icon, helping users better understand the nature of the violation.

![description](../assets/datastores/anomalies-datastore/description-light.png#only-light)
![description](../assets/datastores/anomalies-datastore/description-dark.png#only-dark)

### Source Records

The **Source Records** section displays all the data and fields related to the detected anomaly from the dataset. It is an **Enrichment Datastore** that is used to store the analyzed results, including any anomalies and additional metadata in files, hence it is recommended to add/link an enrichment datastore with your connected source datastore.

![source-records-section](../assets/datastores/anomalies-datastore/source-records-section-light.png#only-light)
![source-records-section](../assets/datastores/anomalies-datastore/source-records-section-dark.png#only-dark)

!!! note 
    In anomaly detection, source records are displayed as part of the Anomaly Details. For a Record anomaly, the specific record is highlighted. For a Shape anomaly, 10 samples from the underlying anomalous records are highlighted.

#### Sort Options

The **Sort By** dropdown allows you to organize the failed source records based on the selected criteria.

![sort](../assets/datastores/anomalies-datastore/sort-light.png#only-light)
![sort](../assets/datastores/anomalies-datastore/sort-dark.png#only-dark)

| No. | Sort By | Description |
| :---- | :---- | :---- |
| **1** | **Name** | This is the name and unique number of the check. It’s checking if dates fall within a specific range. |
| **2** | **Weight** | Tells you what this check is doing. Here it is making sure values are between a minimum and maximum time. |
| **3** | **Quality Score** | Shows how important this issue is. In this case, it's marked as **High** priority. |

#### Download Source Records

Download and export all source records (up to 250MB in a compressed .csv) for further analysis or external use.

![download-records](../assets/datastores/anomalies-datastore/download-records-light.png#only-light)
![download-records](../assets/datastores/anomalies-datastore/download-records-dark.png#only-dark)

### Activity Section

The **Activity** section provides a complete timeline of actions and events related to the anomaly. It helps users track how the anomaly has been handled and by whom, ensuring better collaboration and accountability.

![activity-section](../assets/datastores/anomalies-datastore/activity-section-light.png#only-light)
![activity-section](../assets/datastores/anomalies-datastore/activity-section-dark.png#only-dark)

Users can leave comments to discuss the issue, add context, or communicate decisions. All comments are timestamped and attributed to the respective user.

![comment](../assets/datastores/anomalies-datastore/comment-light.png#only-light)
![comment](../assets/datastores/anomalies-datastore/comment-dark.png#only-dark)