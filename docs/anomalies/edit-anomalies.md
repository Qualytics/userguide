# Edit Anomalies

Anomalies support two editable properties: **description** and **tags**. The description allows you to add business context or investigation findings, while tags help you categorize and organize anomalies for downstream workflows.

!!! note
    - Individual anomalies can have both their description and tags edited
    - When editing multiple anomalies in bulk, only tags can be modified
    - Only users with **Update** permission on non-archived anomalies can make edits

## Edit Description

The anomaly description provides a detailed explanation of the data quality issue. You can edit it to add additional context, clarify the business impact, or document investigation findings.

For detailed instructions on editing the description, see the [**Description**](anomaly-insights.md#description) section in the Anomaly Insights documentation.

## Edit Tags (Bulk Edit)

**Step 1:** Hover over the anomaly (whether Active or Acknowledged) and click on the checkbox.

![edit-anomaly](../assets/datastores/edit-anomalies/edit-anomaly.png)

You can edit multiple anomalies by selecting the checkboxes next to each anomaly to choose multiple anomalies at once.

![hover-edit](../assets/datastores/edit-anomalies/hover-edit.png)

When multiple anomalies are selected, an action toolbar appears, displaying the total number of selected anomalies along with a vertical ellipsis for additional bulk action options.

![vertical-edit](../assets/datastores/edit-anomalies/vertical-edit.png)

**Step 2:** Click on the **vertical ellipsis (⋮)** and choose **"Edit"** from the dropdown menu to edit the selected anomalies.

![vertical-edit-options](../assets/datastores/edit-anomalies/vertical-edit-options.png)

A modal window titled **“Bulk Edit Anomalies”** will appear. Here you can only modify the **“tags”** of the selected anomalies.

![edit-modal](../assets/datastores/edit-anomalies/edit-modal.png)

**Step 3**: Turn on the toggle and assign tags to the selected anomalies.

![edit-bulk](../assets/datastores/edit-anomalies/edit-bulk.png)

**Step 4:** Once you have assigned the tags, click on the **“Save”** button.

After clicking the **Save** button, the selected anomalies will be updated with the assigned tags.

![save-button](../assets/datastores/edit-anomalies/save-button.png)
