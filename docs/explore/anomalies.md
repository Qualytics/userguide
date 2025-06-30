# Anomalies

Anomalies tab provides a quick overview of all detected anomalies across your source datastores. In Qualytics, An Anomaly refers to a dataset (record or column) that fails to meet specified data quality checks, indicating a deviation from expected standards or norms. These anomalies are identified when the data does not satisfy the applied validation criteria. You can filter and sort anomalies based on your preferences, making it easy to see which anomalies are active,  acknowledged, or archived. This section is designed to help you quickly identify and address any issues.

Let’s get started 🚀

## Navigation

**Step 1:** Log in to your Qualytics account and click the **Explore** button on the left side panel of the interface.

![explore](../assets/explore/anomalies/explore-light.png#only-light)
![explore](../assets/explore/anomalies/explore-dark.png#only-dark)

**Step 2:** Click on the **"Anomalies"** from the Navigation Tab.

![anomalies](../assets/explore/anomalies/anomalies-light.png#only-light)
![anomalies](../assets/explore/anomalies/anomalies-dark.png#only-dark)

You will be navigated to the **Anomalies** tab, where you'll see a list of all the detected anomalies across various tables and fields from different source datastores, based on the applied data quality checks.

![all](../assets/explore/anomalies/all-anomalies-light.png#only-light)
![all](../assets/explore/anomalies/all-anomalies-dark.png#only-dark)

## Categories Anomalies

Anomalies can be classified into different categories based on their status and actions taken. These categories include Open and Archived anomalies. Managing anomalies effectively helps in maintaining data integrity and ensuring quick response to issues.

For more details on categories of anomalies, please refer to the [Anomaly Status](../anomalies/anomaly-status.md/#anomaly-categories-in-explore) section in the documentation.

## Anomaly Details

**Anomaly Details** window provides information about anomalies identified during scan operations. It displays details such as the anomaly ID, status, type, detection time, and where it is in the data, such as the datastore and table.  Additionally, it offers options to explore datasets, share details, and collaborate, making it easier to resolve data issues.

**Step 1:** Click on the anomaly from the list of available (whether Active, Acknowledged or Archived) anomalies to view its details.

![details](../assets/explore/anomalies/details-light.png#only-light)
![details](../assets/explore/anomalies/details-dark.png#only-dark)

A modal window titled **“Anomaly Details”** will appear, displaying all the details of the selected anomaly.

![modal](../assets/explore/anomalies/modal-light.png#only-light)
![modal](../assets/explore/anomalies/modal-dark.png#only-dark)

For more details on Anomaly Details, please refer to the [**Anomaly Insights**](../anomalies/anomaly-insights.md) section in the documentation.

## Acknowledged Anomalies

By acknowledging anomalies, you indicate that they have been reviewed or recognized. Acknowledging anomalies helps you keep track of issues that have been addressed, even if further action is still required.

!!! warning 
    Once an anomaly is acknowledged, it remains acknowledged and never reverts to the active state. 

For more details on how to acknowledge anomalies, please refer to the documentation on [Acknowledge Anomalies](../anomalies/acknowledge-anomalies.md/#acknowledge-anomalies-using-dialogue).

## Archive Anomalies

By archiving anomalies, you move them to an inactive state, while still keeping them available for future reference or analysis. Archiving helps keep your active anomaly list clean without permanently deleting the records.

For more details on how to archive anomalies, please refer to the documentation on [Archive Anomalies](../anomalies/archived-anomalies.md/#archive-anomalies-using-dialogue).

## Restore Archived Anomalies

By restoring archived anomalies, you can bring them back into the **acknowledged** state for further investigation or review. These anomalies will not return to the **active** state once they have been acknowledged.

For more details on how to restore anomalies, please refer to the documentation on [Restore Anomalies](../anomalies/restore-anomalies.md/#restore-anomalies-using-dialogue).

## Assign Tags

Assigning tags to an anomaly serves the purpose of labeling and grouping anomalies and driving downstream workflows.

For more details on how to assign tags, please refer to the documentation on [Assign Tags](../anomalies/records.md/#assign-tags).

## Delete Anomalies

Deleting an anomaly allows you to permanently remove a record that is no longer relevant or was logged in error. This action is done individually, ensuring that your anomaly records remain clean and up to date.

!!! note 
    You can only delete archived anomalies, not active or acknowledged checks. If you want to delete an active or acknowledged anomaly, you must first move it to the archive, and then you can delete it. 

For more details on how to delete anomalies, please refer to the documentation on [Delete Anomalies](../anomalies/delete-anomalies.md/#delete-anomalies-using-dialogue).

## Filter and Sort

Filter and Sort options allow you to organize your anomaly by various criteria, such as Weight, Anomalous Record, Created Date. You can also apply filters to refine your list of anomaly based on Selected Source Datastores, Selected Tag, Timeframe, Type and Rule .

For more details on how to filter and sort anomalies, please refer to the documentation on [Filter and Sort Anomalies](../anomalies/filter-sort.md/#filter-and-sort-anomalies-from-explore-page).