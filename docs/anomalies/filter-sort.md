# Filter and Sort

Filter and Sort functionalities play a crucial role in helping users efficiently navigate large volumes of anomalies. By applying these tools, users can quickly locate the most critical data quality issues, prioritize resolutions, and streamline their review process. Whether you're focusing on anomalies within a single datastore or exploring issues across the entire platform, these capabilities allow for a more targeted and manageable experience.

Let’s get started 🚀

## Filter and Sort Anomalies from Datastore

Filter and sort options in the datastore view allow users to organize anomalies within a specific data source. Anomalies can be sorted by weight, creation date, or number of anomalous records. Filters like timeframe, rule, type, and tags help refine the view for targeted analysis.

**Step 1:** Log in to your Qualytics account and select the datastore from the left menu on which you want to manage your anomalies.

![datastore](../assets/datastores/manage-anomalies/datastore-light-1.png#only-light)
![datastore](../assets/datastores/manage-anomalies/datastore-dark-1.png#only-dark)

**Step 2:** Click on the **“Anomalies”** from the Navigation Tab.

![anomalies](../assets/datastores/manage-anomalies/anomalies-light-2.png#only-light)
![anomalies](../assets/datastores/manage-anomalies/anomalies-dark-2.png#only-dark)

### Sort

You can sort your anomalies by **Anomalous Records**, **Created Date**, and **Weight** to easily organize and prioritize them according to your needs.

![sort](../assets/datastores/manage-anomalies/sort-light-1.png#only-light)
![sort](../assets/datastores/manage-anomalies/sort-dark-1.png#only-dark)

| No | Sort By Option | Description |
| :---- | :---- | :---- |
| **1** | **Anomalous Records** | Sorts anomalies based on the number of anomalous records identified. |
| **2** | **Created Date** | Sorts anomalies according to the date they were detected. |
| **3** | **Weight** | Sort anomalies by their assigned weight or importance level. |

Whatever sorting option is selected, you can arrange the data either in ascending or descending order by clicking the caret button next to the selected sorting criteria.

![arrange](../assets/datastores/manage-anomalies/arrange-light.png#only-light)
![arrange](../assets/datastores/manage-anomalies/arrange-dark.png#only-dark)

### Filter

You can filter your anomalies based on values like **Timeframe**, **Type**, **Rule**, and **Tags** etc.

![filter](../assets/datastores/manage-anomalies/filter-light-1.png#only-light)
![filter](../assets/datastores/manage-anomalies/filter-dark-1.png#only-dark)

| No. | Filter | Description |
| :---- | :---- | :---- |
| **1** | **Timeframe** | Filtering anomalies detected within specific time ranges (e.g., anomalies detected in the last week or year). |
| **2** | **Type** | Filter anomalies based on anomaly type (Record or Shape). |
| **3** | **Rule** | Filter anomalies based on specific rules applied to the anomaly. By clicking on the caret down button next to the Rule field, the available rule types will be dynamically populated based on the rule types present in the results. The rules displayed are based on the current dataset and provide more granular control over filtering. <br> <br> Each rule type will show a counter next to it, displaying the total number of occurrences for that rule in the dataset.<br> <br> For example, the rule type **Between** is displayed with a total of **3** occurrences. |
| **4** | **Table** | Filters anomalies based on the table where they occurred. |
| **5** | **Field** | Filters anomalies based on the column in the table where the issue was found. |
| **6** | **Check** | Filters anomalies based on the check that generated them. |

![filter](../assets/datastores/manage-anomalies/filters-light.png#only-light)
![filter](../assets/datastores/manage-anomalies/filters-dark.png#only-dark)

| No. | Filter | Description |
| :---- | :---- | :---- |
| **7** | **Tags** | Tag Filter displays only the tags associated with the currently visible items, along with their color icon, name, type, and the number of matching records. Selecting one or more tags refines the list based on your selection. If no matching items are found, a No options found message is displayed. |

## Filter and Sort Anomalies from Explore page

The Explore page provides a cross-datastore view of anomalies, enabling users to analyze issues across multiple sources. Users can apply filters such as source datastore, rule type, tags, and timeframe. This helps in identifying widespread data quality issues and patterns efficiently.

**Step 1:** Log in to your Qualytics account and click the **Explore** button on the left side panel of the interface.

![explore](../assets/explore/anomalies/explore-light.png#only-light)
![explore](../assets/explore/anomalies/explore-dark.png#only-dark)

**Step 2:** Click on the **"Anomalies"** from the Navigation Tab.

![anomalies](../assets/explore/anomalies/anomalies-light.png#only-light)
![anomalies](../assets/explore/anomalies/anomalies-dark.png#only-dark)

You will be navigated to the **Anomalies** tab, where you'll see a list of all the detected anomalies across various tables and fields from different source datastores, based on the applied data quality checks.

![all](../assets/explore/anomalies/all-anomalies-light.png#only-light)
![all](../assets/explore/anomalies/all-anomalies-dark.png#only-dark)

### Sort

You can sort your anomalies by **Anomalous Record**, **Created Date**, and **Weight** to easily organize and prioritize them according to your needs.

![sort](../assets/explore/anomalies/sort-light.png#only-light)
![sort](../assets/explore/anomalies/sort-dark.png#only-dark)

| No | Sort By Option | Description |
| :---- | :---- | :---- |
| **1** | **Anomalous Record** | Sorts anomalies based on the number of anomalous records identified. |
| **2** | **Created Date** | Sorts anomalies according to the date they were detected. |
| **3** | **Weight** | Sort anomalies by their assigned weight or importance level. |

Whatever sorting option is selected, you can arrange the data either in ascending or descending order by clicking the caret button next to the selected sorting criteria.

![caret](../assets/explore/anomalies/caret-light.png#only-light)
![caret](../assets/explore/anomalies/caret-dark.png#only-dark)

### Filter

You can filter your anomalies based on values like **Source Datastores, Timeframe**, **Type**, **Rule**, and **Tags**.

![filter](../assets/explore/anomalies/filter-1-light.png#only-light)
![filter](../assets/explore/anomalies/filter-1-dark.png#only-dark)

![filter](../assets/explore/anomalies/filter-2-light.png#only-light)
![filter](../assets/explore/anomalies/filter-2-dark.png#only-dark)

| No. | Filter | Description |
| :---- | :---- | :---- |
| **1** | **Selected Source Datastore** | Select specific source datastores to focus on their anomalies. |
| **2** | **Select Tags** | Filter anomalies by specific tags to categorize and prioritize issues effectively. |
| **3** | **Timeframe** | Filtering anomalies detected within specific time ranges (e.g., anomalies detected in the last week or year). |
| **4** | **Type** | Filter anomalies based on anomaly type (Record or Shape). |
| **5** | **Rule** | Filter anomalies based on specific rules applied to the anomaly. By clicking on the caret down button next to the Rule field, the available rule types will be dynamically populated based on the rule types present in the results. The rules displayed are based on the current dataset and provide more granular control over filtering. <br> <br> Each rule type will show a counter next to it, displaying the total number of occurrences for that rule in the dataset.<br> <br> For example, the rule type **After Date Time** is displayed with a total of **14** occurrences. |