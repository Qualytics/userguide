# Manage Anomalies

You can manage anomalies to ensure your data remains accurate and any quality issues are addressed efficiently. Anomalies, which occur due to errors or inconsistencies in data, can be categorized as **Open** or **Archived**, helping you track their status and take the appropriate actions. You can acknowledge anomalies that have been reviewed, archive those that no longer need attention, and delete any that are irrelevant or logged by mistake. 

Bulk actions further simplify the process, allowing you to manage multiple anomalies at once, saving time and effort. This guide will walk you through the steps of acknowledging, archiving, restoring, editing, and deleting anomalies, whether individually or in bulk.

Let's get started 🚀

## Navigation

**Step 1:** Log in to your Qualytics account and select the datastore from the left menu on which you want to manage your anomalies.

![datastore](../assets/datastores/manage-anomalies/datastore-light-1.png#only-light)
![datastore](../assets/datastores/manage-anomalies/datastore-dark-1.png#only-dark)

**Step 2:** Click on the **“Anomalies”** from the Navigation Tab.

![anomalies](../assets/datastores/manage-anomalies/anomalies-light-2.png#only-light)
![anomalies](../assets/datastores/manage-anomalies/anomalies-dark-2.png#only-dark)

## Categories Anomalies

Anomalies can be classified into different categories based on their status and actions taken. These categories include Open and Archived anomalies. Managing anomalies effectively helps in maintaining data integrity and ensuring quick response to issues.

### Open

By selecting Open Anomalies, you can view anomalies that have been detected but remain unacknowledged or unresolved. These anomalies require attention and may need further investigation or corrective action. 

![open-anomalies](../assets/datastores/manage-anomalies/open-anomalies-light-2.png#only-light)
![open-anomalies](../assets/datastores/manage-anomalies/open-anomalies-dark-2.png#only-dark)

This option helps focus on unaddressed issues while allowing seamless navigation to **All**, **Active**, or **Acknowledged** anomalies as needed.

**1. Active**: By selecting **Active Anomalies**, you can focus on anomalies that are currently unresolved or require immediate attention. These are the anomalies that are still in play and have not yet been acknowledged, archived, or resolved.

![active-anomalies](../assets/datastores/manage-anomalies/active-anomalies-light-4.png#only-light)
![active-anomalies](../assets/datastores/manage-anomalies/active-anomalies-dark-4.png#only-dark)

**2. Acknowledged**: By selecting **Acknowledged Anomalies**, you can see all anomalies that have been reviewed and marked as acknowledged. This status indicates that the anomalies have been noted, though they may still require further action.

![acknowledged-anomalies](../assets/datastores/manage-anomalies/acknowledged-anomalies-light-5.png#only-light)
![acknowledged-anomalies](../assets/datastores/manage-anomalies/acknowledged-anomalies-dark-5.png#only-dark)

**3. All**: By selecting **All Anomalies**, you can view the complete list of anomalies, regardless of their status. This option helps you get a comprehensive overview of all issues that have been detected, whether they are currently active, acknowledged, or archived.

![all-anomalies](../assets/datastores/manage-anomalies/all-anomalies-light-3.png#only-light)
![all-anomalies](../assets/datastores/manage-anomalies/all-anomalies-dark-3.png#only-dark)

### Archived

By selecting **Archived Anomalies**, you can view anomalies that have been resolved or moved out of active consideration. Archiving anomalies allows you to keep a record of past issues without cluttering the active list.

![archived-anomalies](../assets/datastores/manage-anomalies/archived-anomalies-light-6.png#only-light)
![archived-anomalies](../assets/datastores/manage-anomalies/archived-anomalies-dark-6.png#only-dark)

You can also categorize the archived anomalies based on their status as **Resolved**, **Duplicate** and **Invalid**, to manage and review them effectively.

**1. Resolved**: This indicates that the anomaly was a legitimate data quality concern and has been addressed.

![resolved](../assets/datastores/manage-anomalies/resolved-light-7.png#only-light)
![resolved](../assets/datastores/manage-anomalies/resolved-dark-7.png#only-dark)

**2. Duplicate**: This indicates that the anomaly is a duplicate of an existing record and has already been addressed.

![duplicate](../assets/datastores/manage-anomalies/duplicate-light.png#only-light)
![duplicate](../assets/datastores/manage-anomalies/duplicate-dark.png#only-dark)

**3. Invalid**: This indicates that the anomaly is not a legitimate data quality concern and does not require further action.

![invalid](../assets/datastores/manage-anomalies/invalid-light-8.png#only-light)
![invalid](../assets/datastores/manage-anomalies/invalid-dark-8.png#only-dark)

**4. All**: Displays all archived anomalies, including those marked as Resolved, Duplicate, and Invalid, giving a comprehensive view of all past issues. 

![all](../assets/datastores/manage-anomalies/all-light-9.png#only-light)
![all](../assets/datastores/manage-anomalies/all-dark-9.png#only-dark)

## Acknowledge Anomalies

By acknowledging anomalies, you indicate that they have been reviewed or recognized. This can be done either individually or in bulk, depending on your workflow. Acknowledging anomalies helps you keep track of issues that have been addressed, even if further action is still required.

!!! warning 
    Once an anomaly is acknowledged, it remains acknowledged and never reverts to the active state.

### Method I. Acknowledge Specific Anomaly

You can acknowledge individual anomalies either directly or through the action menu, giving you precise control over each anomaly's status.

#### 1. Acknowledge Directly

**Step 1:** Locate the active anomaly you want to acknowledge, and click on the acknowledge icon (represented by an **eye** icon) located on the right side of the anomaly. 

![acknowledge-directly](../assets/datastores/manage-anomalies/acknowledge-directly-light-10.png#only-light)
![acknowledge-directly](../assets/datastores/manage-anomalies/acknowledge-directly-dark-10.png#only-dark)

**Step 2:** After clicking on the **Acknowledge** button your anomaly is successfully moved to the acknowledge and a flash message will appear saying **“The Anomaly has been successfully acknowledged.”**

![acknowledge-msg](../assets/datastores/manage-anomalies/acknowledge-msg-light-13.png#only-light)
![acknowledge-msg](../assets/datastores/manage-anomalies/acknowledge-msg-dark-13.png#only-dark)

#### 2. Acknowledge via Action Menu

**Step 1**: Click on the active anomaly from the list of available anomalies that you want to acknowledge.

![active-anomaly](../assets/datastores/manage-anomalies/active-anomaly-light-14.png#only-light)
![active-anomaly](../assets/datastores/manage-anomalies/active-anomaly-dark-14.png#only-dark)

**Step 2:** A modal window will appear displaying the anomaly details. Click on the **Acknowledge** icon ( represented by an **eye** icon ) located in the upper-right corner of the modal window.

![vertical-acknowledge](../assets/datastores/manage-anomalies/vertical-acknowledge-light-15.png#only-light)
![vertical-acknowledge](../assets/datastores/manage-anomalies/vertical-acknowledge-dark-15.png#only-dark)

**Step 3:** After clicking on the **Acknowledge** button your anomaly is successfully moved to the acknowledge and a flash message will appear saying **“The Anomaly has been successfully acknowledged.”**

![acknowledge-message](../assets/datastores/manage-anomalies/acknowledge-message-light-18.png#only-light)
![acknowledge-message](../assets/datastores/manage-anomalies/acknowledge-message-dark-18.png#only-dark)

### Method II. Acknowledge Anomalies in Bulk

By acknowledging anomalies in bulk, you can quickly mark multiple anomalies as reviewed at once, saving time and ensuring that all relevant issues are addressed simultaneously.

**Step 1:** Hover over the active anomalies and click on the checkbox to select multiple anomalies.

![acknowledge-bulk](../assets/datastores/manage-anomalies/acknowledge-bulk-light-19.png#only-light)
![acknowledge-bulk](../assets/datastores/manage-anomalies/acknowledge-bulk-dark-19.png#only-dark)

When multiple anomalies are selected, an action toolbar appears, displaying the total number of selected anomalies along with a vertical ellipsis for additional bulk action options.

![action-toolbar](../assets/datastores/manage-anomalies/action-toolbar-light-20.png#only-light)
![action-toolbar](../assets/datastores/manage-anomalies/action-toolbar-dark-20.png#only-dark)

**Step 2:** Click on the **vertical ellipsis (⋮)** and choose **"Acknowledge"** from the dropdown menu to acknowledge the selected anomalies.

![vertical-acknowledge](../assets/datastores/manage-anomalies/vertical-acknowledge-light-21.png#only-light)
![vertical-acknowledge](../assets/datastores/manage-anomalies/vertical-acknowledge-dark-21.png#only-dark)

A modal window titled **“Acknowledge Anomalies”** will appear, confirming that this action acknowledges the anomalies as a legitimate data quality concern.

You also have the option to leave a comment in the provided field to provide additional context or details. 

![acknowledge-anomalies](../assets/datastores/manage-anomalies/acknowledge-anomalies-light-22.png#only-light)
![acknowledge-anomalies](../assets/datastores/manage-anomalies/acknowledge-anomalies-dark-22.png#only-dark)

**Step 3:** Click on the **Acknowledge** button to acknowledge the anomalies.

![acknowledge-button](../assets/datastores/manage-anomalies/acknowledge-button-light-23.png#only-light)
![acknowledge-button](../assets/datastores/manage-anomalies/acknowledge-button-dark-23.png#only-dark)

**Step 4:** After clicking on the **Acknowledge** button your anomalies are successfully moved to the acknowledge state and a flash message will appear saying **“The Anomalies have been successfully acknowledged”**

![acknowledge-button](../assets/datastores/manage-anomalies/acknowledge-button-light-24.png#only-light)
![acknowledge-button](../assets/datastores/manage-anomalies/acknowledge-button-dark-24.png#only-dark)

## Archive Anomalies

By archiving anomalies, you move them to an inactive state, while still keeping them available for future reference or analysis. Archiving helps keep your active anomaly list clean without permanently deleting the records.

### Method I. Archive Specific Anomalies

You can archive individual anomalies either directly or through the action menu.

#### 1. Archive Directly

**Step 1:** Locate the anomaly (whether Active or Acknowledged) you want to archive and click on the **Archive** icon (represented by a box with a downward arrow) located on the right side of the anomaly. 

![archived-directly](../assets/datastores/manage-anomalies/archived-directly-light-25.png#only-light)
![archived-directly](../assets/datastores/manage-anomalies/archived-directly-dark-25.png#only-dark)

**Step 2:** A modal window titled **“Archive Anomaly”** will appear, providing you with the following archive options:

* **Resolved**: Choose this option if the anomaly was a legitimate data quality concern and has been addressed. This helps maintain a record of resolved issues while ensuring that they are no longer active.

* **Duplicate**: Choose this option if the anomaly is a duplicate of an existing record and has already been addressed. No further action is required as the issue has been previously resolved.

* **Invalid**: Select this option if the anomaly is not a legitimate data quality concern and does not require further action. Archiving anomalies as invalid helps differentiate between real issues and those that can be dismissed, improving overall data quality management.

![archive-anomaly](../assets/datastores/manage-anomalies/archive-anomaly-light-26.png#only-light)
![archive-anomaly](../assets/datastores/manage-anomalies/archive-anomaly-dark-26.png#only-dark)

**Step 3:** Once you've made your selection, click the **Archive** button to proceed.

![archive-button](../assets/datastores/manage-anomalies/archive-button-light-27.png#only-light)
![archive-button](../assets/datastores/manage-anomalies/archive-button-dark-27.png#only-dark)

**Step 4:** After clicking on the **Archive** button your anomaly is moved to the archive and a flash message will appear saying **“Anomaly has been successfully archived”**

![archive-message](../assets/datastores/manage-anomalies/archive-message-light-28.png#only-light)
![archive-message](../assets/datastores/manage-anomalies/archive-message-dark-28.png#only-dark)

#### 2. Archive via Action Menu

**Step 1**: Click on the anomaly from the list of available (whether Active or Acknowledged) anomalies that you want to archive.

![archive-action](../assets/datastores/manage-anomalies/archive-action-light-29.png#only-light)
![archive-action](../assets/datastores/manage-anomalies/archive-action-dark-29.png#only-dark)

**Step 2:** A modal window will appear displaying the anomaly details. Click on the **Archive** icon ( represented by a box with a downward arrow ) located in the upper-right corner of the modal window.

![vertical-archive](../assets/datastores/manage-anomalies/vertical-archive-light-30.png#only-light)
![vertical-archive](../assets/datastores/manage-anomalies/vertical-archive-dark-30.png#only-dark)

**Step 3:** A modal window titled **“Archive Anomaly”** will appear, providing you with the following archive options:

* **Resolved**: Choose this option if the anomaly was a legitimate data quality concern and has been addressed. This helps maintain a record of resolved issues while ensuring that they are no longer active.

* **Duplicate**: Choose this option if the anomaly is a duplicate of an existing record and has already been addressed. No further action is required as the issue has been previously resolved.

* **Invalid**: Select this option if the anomaly is not a legitimate data quality concern and does not require further action. Archiving anomalies as invalid helps differentiate between real issues and those that can be dismissed, improving overall data quality management.

![archive-anomaly](../assets/datastores/manage-anomalies/archive-anomaly-light-31.png#only-light)
![archive-anomaly](../assets/datastores/manage-anomalies/archive-anomaly-dark-31.png#only-dark)

**Step 4:** Once you've made your selection, click the **Archive** button to proceed.

![archive-button](../assets/datastores/manage-anomalies/archive-button-light-32.png#only-light)
![archive-button](../assets/datastores/manage-anomalies/archive-button-dark-32.png#only-dark)

**Step 5:** After clicking on the **Archive** button your anomaly is moved to the archive and a flash message will appear saying **“Anomaly has been successfully archived”**

![archive-message](../assets/datastores/manage-anomalies/archive-message-light-33.png#only-light)
![archive-message](../assets/datastores/manage-anomalies/archive-message-dark-33.png#only-dark)

### Method II. Archive Anomalies in Bulk

To handle multiple anomalies efficiently, you can archive them in bulk, allowing you to quickly move large volumes of anomalies into the archived state.

**Step 1:** Hover over the anomaly (whether Active or Acknowledged) and click on the checkbox to select multiple anomalies.

![archive-bulk](../assets/datastores/manage-anomalies/archive-bulk-light-34.png#only-light)
![archive-bulk](../assets/datastores/manage-anomalies/archive-bulk-dark-34.png#only-dark)

When multiple anomalies are selected, an action toolbar appears, displaying the total number of selected anomalies along with a vertical ellipsis for additional bulk action options.

![action-option](../assets/datastores/manage-anomalies/action-option-light-35.png#only-light)
![action-option](../assets/datastores/manage-anomalies/action-option-dark-35.png#only-dark)

**Step 2:** Click on the **vertical ellipsis (⋮)** and choose **"Archive"** from the dropdown menu to archive the selected anomalies.

![vertical-archive](../assets/datastores/manage-anomalies/vertical-archive-light-36.png#only-light)
![vertical-archive](../assets/datastores/manage-anomalies/vertical-archive-dark-36.png#only-dark)

**Step 3:** A modal window titled **“Archive Anomaly”** will appear, providing you with the following archive options:

* **Resolved**: Choose this option if the anomaly was a legitimate data quality concern and has been addressed. This helps maintain a record of resolved issues while ensuring that they are no longer active.

* **Duplicate**: Choose this option if the anomaly is a duplicate of an existing record and has already been addressed. No further action is required as the issue has been previously resolved.

* **Invalid**: Select this option if the anomaly is not a legitimate data quality concern and does not require further action. Archiving anomalies as invalid helps differentiate between real issues and those that can be dismissed, improving overall data quality management.

![archive-anomalies](../assets/datastores/manage-anomalies/archive-anomalies-light-37.png#only-light)
![archive-anomalies](../assets/datastores/manage-anomalies/archive-anomalies-dark-37.png#only-dark)

**Step 4:** Once you've made your selection, click on the **Archive** button to proceed.

![archive-button](../assets/datastores/manage-anomalies/archive-button-light-38.png#only-light)
![archive-button](../assets/datastores/manage-anomalies/archive-button-dark-38.png#only-dark)

**Step 5:** After clicking on the **Archive** button your anomaly is moved to the archive and a flash message will appear saying **“Anomalies has been successfully archived”**

![archive-message](../assets/datastores/manage-anomalies/archive-message-light-39.png#only-light)
![archive-message](../assets/datastores/manage-anomalies/archive-message-dark-39.png#only-dark)

## Restore Archive Anomalies

By restoring archived anomalies, you can bring them back into the **acknowledged** state for further investigation or review. These anomalies will not return to the **active** state once they have been acknowledged.

**Step 1**: Click on the anomaly that you want to restore from the list of archived anomalies.

![restore-archive](../assets/datastores/manage-anomalies/restore-archive-light-40.png#only-light)
![restore-archive](../assets/datastores/manage-anomalies/restore-archive-dark-40.png#only-dark)

**Step 2:** A modal window will appear displaying the anomaly details. Click on the **vertical ellipsis** **(⋮)** located in the upper-right corner of the modal window, and click on **“Restore”** from the drop-down menu. 

![vertical-restore](../assets/datastores/manage-anomalies/vertical-restore-light-41.png#only-light)
![vertical-restore](../assets/datastores/manage-anomalies/vertical-restore-dark-41.png#only-dark)

**Step 3:** After clicking on the **“Restore”** button, the selected anomaly is now restored as in acknowledged state.

![restore-acknow](../assets/datastores/manage-anomalies/restore-acknow-light-42.png#only-light)
![restore-acknow](../assets/datastores/manage-anomalies/restore-acknow-dark-42.png#only-dark)

## Edit Anomalies

By editing anomalies, you can only update their tags, allowing you to categorize and organize anomalies more effectively without altering their core details.

!!! note 
    When editing multiple anomalies in bulk, only the tags can be modified.

**Step 1:** Hover over the anomaly (whether Active or Acknowledged) and click on the checkbox. 

![edit-anomalies](../assets/datastores/manage-anomalies/edit-anomalies-light-43.png#only-light)
![edit-anomalies](../assets/datastores/manage-anomalies/edit-anomalies-dark-43.png#only-dark)

You can edit multiple checks by selecting the checkboxes next to each anomaly to choose multiple anomalies at once.

![multiple-anomalies](../assets/datastores/manage-anomalies/multiple-anomalies-light-44.png#only-light)
![multiple-anomalies](../assets/datastores/manage-anomalies/multiple-anomalies-dark-44.png#only-dark)

When multiple anomalies are selected, an action toolbar appears, displaying the total number of selected anomalies along with a vertical ellipsis for additional bulk action options.

![action-toolbar](../assets/datastores/manage-anomalies/action-toolbar-light-45.png#only-light)
![action-toolbar](../assets/datastores/manage-anomalies/action-toolbar-dark-45.png#only-dark)

**Step 2:** Click on the **vertical ellipsis (⋮)** and choose **"Edit"** from the dropdown menu to edit the selected anomalies.

![vertical-edit](../assets/datastores/manage-anomalies/vertical-edit-light-46.png#only-light)
![vertical-edit](../assets/datastores/manage-anomalies/vertical-edit-dark-46.png#only-dark)

A modal window titled **“Bulk Edit Anomalies”** will appear. Here you can only modify the **“tags”** of the selected anomalies.  

![bulk-edit](../assets/datastores/manage-anomalies/bulk-edit-light-47.png#only-light)
![bulk-edit](../assets/datastores/manage-anomalies/bulk-edit-dark-47.png#only-dark)

**Step 3**: Turn on the toggle and assign tags to the selected anomalies.

![toggle-button](../assets/datastores/manage-anomalies/toggle-button-light-48.png#only-light)
![toggle-button](../assets/datastores/manage-anomalies/toggle-button-dark-48.png#only-dark)

**Step 4:** Once you have assigned the tags, click on the **“Save”** button. 

After clicking the **Save** button, the selected anomalies will be updated with the assigned tags.

![save-button](../assets/datastores/manage-anomalies/save-button-light-49.png#only-light)
![save-button](../assets/datastores/manage-anomalies/save-button-dark-49.png#only-dark)

## Delete Anomalies

Deleting anomalies allows you to permanently remove records that are no longer relevant or were logged in error. This can be done individually or for multiple anomalies at once, ensuring that your anomaly records remain clean and up to date.

!!! note 
    You can only delete archived anomalies, not active or acknowledged checks. If you want to delete an active or acknowledged anomaly, you must first move it to the archive, and then you can delete it.

!!! warning 
    Deleting an anomaly is a one-time action. It cannot be restored after deletion.

### Method I. Delete Specific Anomaly

You can delete individual anomalies using one of two methods:

#### 1. Delete Directly

**Step 1:** Click on **Archived** from the **navigation bar** in the **Anomalies** section to view all archived anomalies.

![delete-archive](../assets/datastores/manage-anomalies/delete-archive-light-50.png#only-light)
![delete-archive](../assets/datastores/manage-anomalies/delete-archive-dark-50.png#only-dark)

**Step 2:** Locate the anomaly, that you want to delete and click on the **Delete** icon located on the right side of the anomaly.

![delete-icon](../assets/datastores/manage-anomalies/delete-icon-light-51.png#only-light)
![delete-icon](../assets/datastores/manage-anomalies/delete-icon-dark-51.png#only-dark)

**Step 3:** A confirmation modal window will appear, click on the **Delete** button to permanently remove the anomaly from the system.

![delete-button](../assets/datastores/manage-anomalies/delete-button-light-52.png#only-light)
![delete-button](../assets/datastores/manage-anomalies/delete-button-dark-52.png#only-dark)

**Step 4:** After clicking on the delete button, your anomaly is successfully deleted and a success flash message will appear saying **“Anomaly has been successfully deleted”**

![success-msg](../assets/datastores/manage-anomalies/success-msg-light-53.png#only-light)
![success-msg](../assets/datastores/manage-anomalies/success-msg-dark-53.png#only-dark)

#### 2. Delete via Action Menu

**Step 1:** Click on the archive anomaly from the list of archived anomalies that you want to delete.

![delete-button](../assets/datastores/manage-anomalies/delete-button-light-54.png#only-light)
![delete-button](../assets/datastores/manage-anomalies/delete-button-dark-54.png#only-dark)

**Step 2:** A modal window will appear displaying the anomaly details. Click on the **vertical ellipsis** **(⋮)** located in the upper-right corner of the modal window, and click on **“Delete”** from the drop-down menu. 

![vertical-delete](../assets/datastores/manage-anomalies/vertical-delete-light-55.png#only-light)
![vertical-delete](../assets/datastores/manage-anomalies/vertical-delete-dark-55.png#only-dark)

**Step 3:** A confirmation modal window will appear, click on the **Delete** button to permanently remove the anomaly from the system.

![delete-button](../assets/datastores/manage-anomalies/delete-button-light-56.png#only-light)
![delete-button](../assets/datastores/manage-anomalies/delete-button-dark-56.png#only-dark)

**Step 4:** After clicking on the delete button, your anomaly is successfully deleted and a success flash message will appear saying **“Anomaly has been successfully deleted”**

![delete-msg](../assets/datastores/manage-anomalies/delete-msg-light-57.png#only-light)
![delete-msg](../assets/datastores/manage-anomalies/delete-msg-dark-57.png#only-dark)

### Method II. Delete Anomalies in Bulk

For more efficient management, you can delete multiple anomalies at once using the bulk delete option, allowing for faster cleanup of unwanted records.

**Step 1:** Hover over the archived anomalies and click on the checkbox to select anomalies in bulk.

![delete-bulk](../assets/datastores/manage-anomalies/delete-bulk-light-58.png#only-light)
![delete-bulk](../assets/datastores/manage-anomalies/delete-bulk-dark-58.png#only-dark)

When multiple checks are selected, an action toolbar appears, displaying the total number of checks chosen along with a vertical ellipsis for additional bulk action options.

![action-toolbar](../assets/datastores/manage-anomalies/action-toolbar-light-59.png#only-light)
![action-toolbar](../assets/datastores/manage-anomalies/action-toolbar-dark-59.png#only-dark)

**Step 2:** Click on the **vertical ellipsis (⋮)** and choose **"Delete"** from the dropdown menu to delete the selected anomalies.

![vertical-delete](../assets/datastores/manage-anomalies/vertical-delete-light-60.png#only-light)
![vertical-delete](../assets/datastores/manage-anomalies/vertical-delete-dark-60.png#only-dark)

**Step 3:** A confirmation modal window will appear, click on the **Delete** button to permanently remove the selected anomalies from the system.

![delete-button](../assets/datastores/manage-anomalies/delete-button-light-61.png#only-light)
![delete-button](../assets/datastores/manage-anomalies/delete-button-dark-61.png#only-dark)

**Step 4:** After clicking on the delete button, your anomalies are successfully deleted and a success flash message will appear saying **“Anomalies has been successfully deleted”**

![delete-msg](../assets/datastores/manage-anomalies/delete-msg-light-62.png#only-light)
![delete-msg](../assets/datastores/manage-anomalies/delete-msg-dark-62.png#only-dark)

## Filter and Sort
Filter and Sort options allow you to organize your anomaly by various criteria, such as Weight, Anomalous Record, Created Date. You can also apply filters to refine your list of anomaly based on Timeframe, Type and Rule etc.

### Sort

You can sort your anomalies by **Anomalous Record**, **Created Date**, and **Weight** to easily organize and prioritize them according to your needs.

![sort](../assets/datastores/manage-anomalies/sort-light.png#only-light)
![sort](../assets/datastores/manage-anomalies/sort-dark.png#only-dark)

| No | Sort By Option | Description |
| :---- | :---- | :---- |
| **1** | **Anomalous Record** | Sorts anomalies based on the number of anomalous records identified. |
| **2** | **Created Date** | Sorts anomalies according to the date they were detected. |
| **3** | **Weight** | Sort anomalies by their assigned weight or importance level. |

Whatever sorting option is selected, you can arrange the data either in ascending or descending order by clicking the caret button next to the selected sorting criteria.

![arrange](../assets/datastores/manage-anomalies/arrange-light.png#only-light)
![arrange](../assets/datastores/manage-anomalies/arrange-dark.png#only-dark)

### Filter

You can filter your anomalies based on values like **Timeframe**, **Type**, **Rule**, and **Tags** etc.

![filter](../assets/datastores/manage-anomalies/filter-light.png#only-light)
![filter](../assets/datastores/manage-anomalies/filter-dark.png#only-dark)

| No. | Filter | Description |
| :---- | :---- | :---- |
| **1** | **Timeframe** | Filtering anomalies detected within specific time ranges (e.g., anomalies detected in the last week or year). |
| **2** | **Type** | Filter anomalies based on anomaly type (Record or Shape). |
| **3** | **Rule** | Filter anomalies based on specific rules applied to the anomaly. By clicking on the caret down button next to the Rule field, the available rule types will be dynamically populated based on the rule types present in the results. The rules displayed are based on the current dataset and provide more granular control over filtering. <br> <br> Each rule type will show a counter next to it, displaying the total number of occurrences for that rule in the dataset.<br> <br> For example, the rule type **Between** is displayed with a total of **13** occurrences. |
| **4** | **Table** | Filters anomalies based on the table where they occurred. |
| **5** | **Field** | Filters anomalies based on the column in the table where the issue was found. |
| **6** | **Check** | Filters anomalies based on the check that generated them. |
| **7** | **Tags** | Filters anomalies by tags that have been applied to checks or rules. |


