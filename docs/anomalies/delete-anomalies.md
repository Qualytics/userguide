# Delete Anomalies

Deleting anomalies allows you to permanently remove entries that are no longer relevant, were resolved, or were captured in error. This ensures your anomaly list remains clean, focused, and easy to manage. Whether you're addressing a few outdated records or performing a bulk cleanup, deleting anomalies helps maintain clarity and accuracy in your data quality monitoring process. Only archived anomalies can be deleted to preserve the integrity of active investigations.

!!! note
    You can only delete archived anomalies, not active or acknowledged anomalies. If you want to delete an active or acknowledged anomaly, you must first move it to the archive, and then you can delete it.

!!! warning
    Deleting an anomaly is a one-time action. It cannot be restored after deletion.

Let’s get started 🚀

## Delete Specific Anomaly

**Step 1:** Log in to your Qualytics account and select the datastore from the left menu on which you want to manage your anomalies.

![datastore](../assets/datastores/manage-anomalies/datastore-light-1.png#only-light)
![datastore](../assets/datastores/manage-anomalies/datastore-dark-1.png#only-dark)

**Step 2:** Click on the “Anomalies” from the Navigation Tab.

![anomalies](../assets/datastores/manage-anomalies/anomalies-light-2.png#only-light)
![anomalies](../assets/datastores/manage-anomalies/anomalies-dark-2.png#only-dark)

You can delete individual anomalies using one of two methods:

### 1. Delete Directly

**Step 1:** Click on **Archived** from the **navigation bar** in the **Anomalies** section to view all archived anomalies.

![delete-archive](../assets/datastores/manage-anomalies/delete-archive-light-50.png#only-light)
![delete-archive](../assets/datastores/manage-anomalies/delete-archive-dark-50.png#only-dark)

**Step 2:** Locate the anomaly, that you want to delete and click on the **Delete** icon located on the right side of the anomaly.

![delete-icon](../assets/datastores/manage-anomalies/delete-icon-light-51.png#only-light)
![delete-icon](../assets/datastores/manage-anomalies/delete-icon-dark-51.png#only-dark)

**Step 3:** A confirmation modal window will appear, click on the **Delete** button to permanently remove the anomaly from the system.

![delete-button](../assets/datastores/manage-anomalies/delete-button-light-52.png#only-light)
![delete-button](../assets/datastores/manage-anomalies/delete-button-dark-52.png#only-dark)

**Step 4:** After clicking on the **Delete** button, your anomaly is successfully deleted and a success flash message will appear saying **“The Anomaly has been successfully deleted”**.

![success-msg](../assets/datastores/manage-anomalies/success-msg-light-53.png#only-light)
![success-msg](../assets/datastores/manage-anomalies/success-msg-dark-53.png#only-dark)

### 2. Delete via Action Menu

**Step 1:** Click on the archived anomaly from the list of archived anomalies that you want to delete.

![delete-button](../assets/datastores/manage-anomalies/delete-button-light-54.png#only-light)
![delete-button](../assets/datastores/manage-anomalies/delete-button-dark-54.png#only-dark)

**Step 2:** You will be directed to the anomaly details page. Click on the **Settings** icon located at the top right corner of the page and select **“Delete”** from the drop down menu.

![vertical-delete](../assets/datastores/manage-anomalies/vertical-delete-light-55.png#only-light)
![vertical-delete](../assets/datastores/manage-anomalies/vertical-delete-dark-55.png#only-dark)

**Step 3:** A confirmation modal window will appear, click on the **Delete** button to permanently remove the anomaly from the system.

![delete-button](../assets/datastores/manage-anomalies/delete-button-light-56.png#only-light)
![delete-button](../assets/datastores/manage-anomalies/delete-button-dark-56.png#only-dark)

**Step 4:** After clicking on the **Delete** button, your anomaly is successfully deleted and a success flash message will appear saying **“The Anomaly has been successfully deleted”**.

![delete-msg](../assets/datastores/manage-anomalies/delete-msg-light-57.png#only-light)
![delete-msg](../assets/datastores/manage-anomalies/delete-msg-dark-57.png#only-dark)

## Delete Anomalies in Bulk

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

**Step 4:** After clicking on the **Delete** button, your anomalies are successfully deleted and a success flash message will appear saying **“The Anomalies have been successfully deleted”**.

![delete-msg](../assets/datastores/manage-anomalies/delete-msg-light-62.png#only-light)
![delete-msg](../assets/datastores/manage-anomalies/delete-msg-dark-62.png#only-dark)

## Delete Anomalies using Dialogue

You can delete archived anomalies using dialogue, across all datastores through a unified view  from the Explore page. This helps efficiently remove outdated or unnecessary records at scale.

**Step 1:** Log in to your Qualytics account and click the **Explore** button on the left side panel of the interface.

![explore](../assets/explore/anomalies/explore-light.png#only-light)
![explore](../assets/explore/anomalies/explore-dark.png#only-dark)

**Step 2:** Click on the **"Anomalies"** from the Navigation Tab.

![anomalies](../assets/explore/anomalies/anomalies-light.png#only-light)
![anomalies](../assets/explore/anomalies/anomalies-dark.png#only-dark)

You will be navigated to the **Anomalies** tab, where you'll see a list of all the detected anomalies across various tables and fields from different source datastores, based on the applied data quality checks.

![all](../assets/explore/anomalies/all-anomalies-light.png#only-light)
![all](../assets/explore/anomalies/all-anomalies-dark.png#only-dark)

You can delete individual anomalies using one of two methods:

### 1. Delete Directly

For deleting an anomaly directly, please refer to the [Delete Directly](#1-delete-directly) section.

### 2. Delete via Action Menu

**Step 1:** Click on the archive anomaly from the list of archived anomalies that you want to delete.

![action](../assets/explore/anomalies/select-anomalies-light.png#only-light)
![action](../assets/explore/anomalies/select-anomalies-dark.png#only-dark)

**Step 2:** A modal window will appear displaying the anomaly details. Click on the **vertical ellipsis** **(⋮)** located in the upper-right corner of the modal window, and click on **“Delete”** from the drop-down menu.

![vertical](../assets/explore/anomalies/vertical-light.png#only-light)
![vertical](../assets/explore/anomalies/vertical-dark.png#only-dark)

**Step 3:** A confirmation modal window will appear, click on the **Delete** button to permanently remove the anomaly from the system.

![dlt](../assets/explore/anomalies/dlt-button-light.png#only-light)
![dlt](../assets/explore/anomalies/dlt-button-dark.png#only-dark)

**Step 4:** After clicking on the delete button, your anomaly is successfully deleted and a success flash message will appear saying **“Anomaly has been successfully deleted”.**

![msg](../assets/explore/anomalies/flash-1-light.png#only-light)
![msg](../assets/explore/anomalies/flash-1-dark.png#only-dark)