# Anomalies

Anomalies in Qualytics represent data points that deviate from expected patterns or violate defined quality rules, often highlighting issues such as missing values, structural inconsistencies, or incorrect data. These anomalies are detected during scan operations through system-inferred or user-authored checks. Users can access anomalies in two ways, by navigating through a specific datastore to review source-specific issues, or via the Explore page to get a centralized view of all anomalies across datastores.

* [Datastore Anomaly](#datastore-anomaly)

* [Explore Anomaly](#explore-anomaly)

Let’s get started 🚀

## Datastore Anomaly

Datastore anomalies are scoped to a specific data source, allowing users to investigate and address data quality issues within that particular datastore. This view offers contextual insights—such as affected tables, checks, and records—enabling precise root cause analysis and resolution at the source level.

### Navigation To Datastores

Accessing anomalies through a specific datastore lets you focus on data quality issues within that individual source. This view offers a detailed, contextual look at anomalies tied to a particular datastore, making it easier to drill down into affected tables and address issues at the source level.

**Step 1:** Log in to your Qualytics account and select the datastore from the left menu on which you want to manage your anomalies.

![datastore](../assets/datastores/manage-anomalies/datastore-light-1.png#only-light)
![datastore](../assets/datastores/manage-anomalies/datastore-dark-1.png#only-dark)

**Step 2:** Click on the **“Anomalies”** from the Navigation Tab.

![anomalies](../assets/datastores/manage-anomalies/anomalies-light-2.png#only-light)
![anomalies](../assets/datastores/manage-anomalies/anomalies-dark-2.png#only-dark)

### Anomaly Review

Anomaly Review provides key insights into a specific data anomaly, including its status, anomalous record count, failed checks, and weight. It also shows when the anomaly was detected, the triggering scan, and the related datastore, table, and location. This view helps users quickly understand the scope and source of the anomaly for easier investigation and resolution.

**Step 1:** Click on the anomaly that you want to see the details of.

![anomaly-details](../assets/datastores/anomalies-datastore/anomaly-details-light-1.png#only-light)
![anomaly-details](../assets/datastores/anomalies-datastore/anomaly-details-dark-1.png#only-dark)

You will be navigated to the review section, where you can view the **Summary**, **Failed Checks**, **Source Records** and **Activity** information.

![anomaly-details-view](../assets/datastores/anomalies-datastore/anomaly-details-view-light.png#only-light)
![anomaly-details-view](../assets/datastores/anomalies-datastore/anomaly-details-view-dark.png#only-dark)

#### Summary Section

The **Summary** section provides a quick overview of the anomaly's key attributes. It includes the anomaly’s status, total anomalous records, failed checks, weight, detection time, scan information, and the corresponding datastore and table. This section helps users quickly understand where the anomaly occurred and its potential impact.

![summary](../assets/datastores/anomalies-datastore/summary-light.png#only-light)
![summary](../assets/datastores/anomalies-datastore/summary-dark.png#only-dark)

| No. | Field | Description |
| :---- | :---- | :---- |
| **1** | **Status and Type** | Shows the current state and category of the anomaly. In this case, the anomaly is **Active** and of type **Shape**, indicating it relates to the structure or distribution of the data. |
| **2** | **Anomalous Records** | Indicates the total number of records affected by the anomaly. Here, **102** records were identified as anomalous. |
| **3** | **Failed Check** | Displays the number of data quality checks that were violated and triggered this anomaly. In this instance, **1** check was failed. |
| **4** | **Weight** | Represents the significance or impact of the anomaly. A higher weight value implies a more critical issue. This anomaly has a weight of **8**. |
| **5** | **Detected** | Shows how long ago the anomaly was first detected. When you hover over the time the anomaly was detected, a pop-up appears displaying the complete date and time. |
| **6** | **Scan** | Indicates the scan operation that detected the anomaly. Scan ID **#21379** is shown here, and it was an incremental scan.<br></br>When you click on the expand icon, then you will be directed to the Scan Results page where you can view the specific scan that detected the anomaly. |
| **7** | **Source Datastore** | Identifies the dataset where the anomaly was found. This anomaly was found in the Qualytics Databricks POC datastore.<br></br>Clicking on the expand icon opens a detailed view and navigates to the dataset’s page, providing more information about the source datastore where the anomaly was found. |
| **8** | **Table** | Points to the specific table involved in the anomaly. The affected table is raw_order. <br></br>Clicking on the expand icon navigates to the table’s page, providing more in-depth information about the table structure and contents. |
| **9** | **Location** | Displays the full path of the table in the datastore. This helps users trace the exact location of the anomaly within the data pipeline.<br></br>You can click on the copy icon to copy the full location path of the table where the anomaly was detected. |
| **10** | **Tags** | Highlights the severity or categorization of the anomaly.<br></br>The tag **High** indicates a high-priority issue. You can add or remove tags from the anomaly by clicking on the tag badge. |

![summary-details](../assets/datastores/anomalies-datastore/summary-details-light.png#only-light)
![summary-details](../assets/datastores/anomalies-datastore/summary-details-dark.png#only-dark)

**Copy Anomaly Link**

Click on the **Copy Anomaly Link** icon (represented by share icon) located at the right corner of the summary section to copy a direct link to the selected anomaly.

![copy-anomaly](../assets/datastores/anomalies-datastore/copy-anomaly-light.png#only-light)
![copy-anomaly](../assets/datastores/anomalies-datastore/copy-anomaly-dark.png#only-dark)

You can then use this link for easy access to the specific anomaly.

**Copy Anomaly UUID**

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

#### Failed Checks

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

**Failed Check Description**

This allows users to view detailed explanations of each failed check by hovering over the information icon, helping users better understand the nature of the violation.

![description](../assets/datastores/anomalies-datastore/description-light.png#only-light)
![description](../assets/datastores/anomalies-datastore/description-dark.png#only-dark)

#### Source Records

The Source Records section displays all the data and fields related to the detected anomaly from the dataset. It is an Enrichment Datastore that is used to store the analyzed results, including any anomalies and additional metadata in files, hence it is recommended to add/link an enrichment datastore with your connected source datastore.

![source-records-section](../assets/datastores/anomalies-datastore/source-records-section-light.png#only-light)
![source-records-section](../assets/datastores/anomalies-datastore/source-records-section-dark.png#only-dark)

For more information on Source Records, please refer to the [Source Records](../anomalies/records.md) section in the documentation.

#### Activity Section

The **Activity** section provides a complete timeline of actions and events related to the anomaly. It helps users track how the anomaly has been handled and by whom, ensuring better collaboration and accountability.

![activity-section](../assets/datastores/anomalies-datastore/activity-section-light.png#only-light)
![activity-section](../assets/datastores/anomalies-datastore/activity-section-dark.png#only-dark)

Users can leave comments to discuss the issue, add context, or communicate decisions. All comments are timestamped and attributed to the respective user.

![comment](../assets/datastores/anomalies-datastore/comment-light.png#only-light)
![comment](../assets/datastores/anomalies-datastore/comment-dark.png#only-dark)

## Explore Anomaly

Explore anomalies offer a unified, cross-datastore view of all anomalies detected across your environment. This centralized view is ideal for monitoring overall data quality, managing large volumes of anomalies efficiently, and taking bulk actions without needing to navigate into each datastore individually.

### Navigation To Explore

The Explore view provides a centralized list of all anomalies detected across multiple datastores. This is useful for getting a global view of data issues and managing them in bulk without switching between individual datastores.

**Step 1:** Log in to your Qualytics account and click the **Explore** button on the left side panel of the interface.

![explore](../assets/explore/anomalies/explore-light.png#only-light)
![explore](../assets/explore/anomalies/explore-dark.png#only-dark)

**Step 2:** Click on the **"Anomalies"** from the Navigation Tab.

![anomalies](../assets/explore/anomalies/anomalies-light.png#only-light)
![anomalies](../assets/explore/anomalies/anomalies-dark.png#only-dark)

You will be navigated to the **Anomalies** tab, where you'll see a list of all the detected anomalies across various tables and fields from different source datastores, based on the applied data quality checks.

![all](../assets/explore/anomalies/all-anomalies-light.png#only-light)
![all](../assets/explore/anomalies/all-anomalies-dark.png#only-dark)

### Anomaly Details

**Anomaly Details** window provides information about anomalies identified during scan operations. It displays details such as the anomaly ID, status, type, detection time, and where it is in the data, such as the datastore and table.  Additionally, it offers options to explore datasets, share details, and collaborate, making it easier to resolve data issues.

**Step 1:** Click on the anomaly from the list of available (whether Active, Acknowledged or Archived) anomalies to view its details.

![details](../assets/explore/anomalies/details-light.png#only-light)
![details](../assets/explore/anomalies/details-dark.png#only-dark)

A modal window titled **“Anomaly Details”** will appear, displaying all the details of the selected anomaly.

![modal](../assets/explore/anomalies/modal-light.png#only-light)
![modal](../assets/explore/anomalies/modal-dark.png#only-dark)

For more details on Anomaly Details, please refer to the [Anomaly Insights](../anomalies/anomaly-insights.md) section in the documentation.