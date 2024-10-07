# Manage Checks in Datastore

Managing your checks within a datastore is important to maintain data integrity and ensure quality. You can categorize, create, update, archive, restore, delete, and clone checks, making it easier to apply validation rules across the datastores. The system allows for checks to be set as active, draft, or archived based on their current state of use. You can also define reusable templates for quality checks to streamline the creation of multiple checks with similar criteria. With options for important, favorite, and metric-based checks, users have full flexibility to manage data quality efficiently.

Let's get started 🚀

## Navigation

**Step 1:** Log in to your Qualytics account and select the datastore from the left menu on which you want to manage your checks.

![datastore](../assets/checks/manage-checks/datastore-light-1.png#only-light)
![datastore](../assets/checks/manage-checks/datastore-dark-1.png#only-dark)

**Step 2:** Click on the **"Checks"** from the Navigation Tab.

![checks](../assets/checks/manage-checks/checks-light-2.png#only-light)
![checks](../assets/checks/manage-checks/checks-dark-2.png#only-dark)

## Categories Checks

You can categorize your checks based on their status, such as Active, Draft, Archived (Invalid and Discarded), or All, according to your preference. This categorization offers a clear view of the data quality validation process, helping you manage checks efficiently and maintain data integrity.

### All 

By selecting **All Checks**, you can view a comprehensive list of all the checks in the datastore, including both **active** and **draft** checks, allowing you to focus on the checks that are currently being managed or are in progress. However, archived checks are not displayed in this.  

![all](../assets/checks/manage-checks/all-light-3.png#only-light)
![all](../assets/checks/manage-checks/all-dark-3.png#only-dark)

### Active

By selecting **Active**, you can view checks that are currently applied and being enforced on the data. These operational checks are used to validate data quality in real time, allowing you to monitor all active checks and their performance.

![active](../assets/checks/manage-checks/active-light-4.png#only-light)
![active](../assets/checks/manage-checks/active-dark-4.png#only-dark)

You can also categorize the active checks based on their importance, favorites, or specific metrics to streamline your data quality monitoring.

**1. Important:** Shows only checks that are marked as important. These checks are prioritized based on their significance, typically assigned a weight of 7 or higher.

!!! note 
    Important checks are prioritized based on a weight of 7 or higher.

![important](../assets/checks/manage-checks/important-light-5.png#only-light)
![important](../assets/checks/manage-checks/important-dark-5.png#only-dark)

**2. Favorite:** Displays checks that have been marked as favorites. This allows you to quickly access checks that you use or monitor frequently. 

![favorite](../assets/checks/manage-checks/favorite-light-6.png#only-light)
![favorite](../assets/checks/manage-checks/favorite-dark-6.png#only-dark)

**3. All:** Displays a comprehensive view of all active checks, including important, favorite, metrics, and any checks that do not fall under these specific categories. 

![all](../assets/checks/manage-checks/all-light-8.png#only-light)
![all](../assets/checks/manage-checks/all-dark-8.png#only-dark)

### Draft Checks

By selecting **Draft**, you can view checks that have been created but have not yet been applied to the data. These checks are in the drafting stage, allowing for adjustments and reviews before activation. Draft checks provide flexibility to experiment with different validation rules without affecting the actual data.

![draft](../assets/checks/manage-checks/draft-light-9.png#only-light)
![draft](../assets/checks/manage-checks/draft-dark-9.png#only-dark)

You can also categorize the draft checks based on their importance, favorites, or specific metrics to prioritize and organize them effectively during the review and adjustment process.

**1. Important:** Shows only checks that are marked as important. These checks are prioritized based on their significance, typically assigned a weight of 7 or higher. 

![important](../assets/checks/manage-checks/important-light-10.png#only-light)
![important](../assets/checks/manage-checks/important-dark-10.png#only-dark)

**2 Favorite:** Displays checks that have been marked as favorites. This allows you to quickly access checks that you use or monitor frequently.  

![favorite](../assets/checks/manage-checks/favorite-light-11.png#only-light)
![favorite](../assets/checks/manage-checks/favorite-dark-11.png#only-dark)

**3. All:** Displays a comprehensive view of all draft checks, including important, favorite, metrics, and any checks that do not fall under these specific categories.   

![all](../assets/checks/manage-checks/all-light-13.png#only-light)
![all](../assets/checks/manage-checks/all-dark-13.png#only-dark)

### Archived Checks

By selecting **Archived**, you can view checks that have been marked as discarded or invalid from use but are still stored for future reference or restoration. Although these checks are no longer active, they can be restored if needed.

![archived](../assets/checks/manage-checks/archived-light-14.png#only-light)
![archived](../assets/checks/manage-checks/archived-dark-14.png#only-dark)

You can also categorize the archived checks based on their status as **Discarded**, **Invalid**, or view **All** archived checks to manage and review them effectively.

**1. Discarded**: Shows checks that have been marked as no longer useful or relevant and have been discarded from use.

![discarded](../assets/checks/manage-checks/discarded-light-15.png#only-light)
![discarded](../assets/checks/manage-checks/discarded-dark-15.png#only-dark)

**2. Invalid**: Displays checks that are deemed invalid due to errors or misconfigurations, requiring review or deletion.

![invalid](../assets/checks/manage-checks/invalid-light-16.png#only-light)
![invalid](../assets/checks/manage-checks/invalid-dark-16.png#only-dark)

**3. All**: Provides a view of all archive checks within this category including discarded and invalid checks.

![all](../assets/checks/manage-checks/all-light-17.png#only-light)
![all](../assets/checks/manage-checks/all-dark-17.png#only-dark)

## Check Details

Check Details provides important information about each check in the system. It shows when a check was last run, how often it has been used, when it was last updated, who made changes to it, and when it was created. This section helps users understand the status and history of the check, making it easier to manage and track its use over time.

**Step 1:** 
Locate the check you want to review, then hover over the info icon to view the Check Details. 

![hover](../assets/checks/manage-checks/hover-light-17.png#only-light)
![hover](../assets/checks/manage-checks/hover-dark-17.png#only-dark)

A popup will appear with additional details about the check.

![popup](../assets/checks/manage-checks/popup-light-17.png#only-light)
![popup](../assets/checks/manage-checks/popup-dark-17.png#only-dark)

### Last Asserted
Last Asserted At shows the most recent time the check was run, indicating when the last validation occurred. For example, the check was last asserted on **Oct 17, 2023, at 2:37 AM (GMT+5:30).**

![popup](../assets/checks/manage-checks/asserted-light-17.png#only-light)
![popup](../assets/checks/manage-checks/asserted-dark-17.png#only-dark)

### Scans
Scans show how many times the check has been used in different operations. It helps you track how often the check has been applied. For example, the check was used in **30 operations.**

![scan](../assets/checks/manage-checks/scan-light-17.png#only-light)
![scan](../assets/checks/manage-checks/scan-dark-17.png#only-dark)

### Updated At
Updated At shows the most recent time the check was modified or updated. It helps you see when any changes were made to the check’s configuration or settings. For example, the check was last updated on **Sep 9, 2024, at 3:18 PM (GMT+5:30).**

![update](../assets/checks/manage-checks/update-light-17.png#only-light)
![update](../assets/checks/manage-checks/update-dark-17.png#only-dark)

### Last Editor
Last Editor indicates who most recently made changes to the check. It helps track who is responsible for the latest updates or modifications. This is useful for accountability and collaboration within teams. For example, the last person who edited the check is **Rodrigo Ogawa.**

![editor](../assets/checks/manage-checks/editor-light-17.png#only-light)
![editor](../assets/checks/manage-checks/editor-dark-17.png#only-dark)

### Created At
Created At shows when the check was first made. It helps you know how long the check has been in use. This is useful for tracking its history. For example, the check was created on **Oct 17, 2023, at 2:19 PM (GMT+5:30).**

![created](../assets/checks/manage-checks/created-light-17.png#only-light)
![created](../assets/checks/manage-checks/created-dark-17.png#only-dark)


## Status Management of Checks

### Set Check as Draft

You can move an active check into a draft state, allowing you to work on the check, make adjustments, and refine the validation rules without affecting live data. This is useful when you need to temporarily deactivate a check for review and updates. There are two methods from which you can move your active check to draft: you can either draft specific checks or draft multiple checks in bulk.

#### Method I: Draft Specific Check

**Step 1:** Click on the active check that you want to move to the draft state.

For Demonstration purpose, we have selected the **"Time Distribution Size"** check.

![checks-list](../assets/checks/manage-checks/checks-list-light-18.png#only-light)
![checks-list](../assets/checks/manage-checks/checks-list-dark-18.png#only-dark)

**Step 2**: A modal window will appear displaying the check details. Click on the **vertical ellipsis (⋮)** located in the upper-right corner of the modal window, and select **"Draft"** from the drop-down menu.

![draft](../assets/checks/manage-checks/draft-light-19.png#only-light)
![draft](../assets/checks/manage-checks/draft-dark-19.png#only-dark)

**Step 3:** After clicking on **"Draft"**, the check will be successfully moved to the draft state, and a success flash message will appear stating, **"Selected checks have been successfully updated."**

![success-updated](../assets/checks/manage-checks/success-updated-light-20.png#only-light)
![success-updated](../assets/checks/manage-checks/success-updated-dark-20.png#only-dark)

#### Method II. Draft Checks in Bulk

You can move multiple checks into the draft state in one action, allowing you to pause or make adjustments to several checks without affecting your active validation process.

**Step 1:** Hover over the active checks and click on the checkbox to select multiple checks.

![check-box](../assets/checks/manage-checks/check-box-light-21.png#only-light)
![check-box](../assets/checks/manage-checks/check-box-dark-21.png#only-dark)

**Step 2:** Click on the vertical ellipses **(⋮)** and select **"Draft"** from the dropdown menu to move active checks to the draft state.

![draft](../assets/checks/manage-checks/draft-light-22.png#only-light)
![draft](../assets/checks/manage-checks/draft-dark-22.png#only-dark)

A confirmation modal window titled **Bulk Update Checks to Draft** will appear, indicating the number of checks being moved to draft. 

![modal](../assets/checks/manage-checks/modal-light-23.png#only-light)
![modal](../assets/checks/manage-checks/modal-dark-23.png#only-dark)

**Step 3:** Click the **"Update"** button to move the selected active checks to draft.

![update](../assets/checks/manage-checks/update-light-24.png#only-light)
![update](../assets/checks/manage-checks/update-dark-24.png#only-dark)

After clicking the **"Update"** button, your selected checks will be moved to draft, and a success message will appear stating, **"Selected checks have been successfully updated."**

![success-updated](../assets/checks/manage-checks/success-updated-light-25.png#only-light)
![success-updated](../assets/checks/manage-checks/success-updated-dark-25.png#only-dark)

### Activate Draft Check

You can activate the draft checks after when you have worked on the check, make adjustments, and refine the validation rules. By activating the draft check and making it live, ensures that the defined criteria are enforced on the data. There are two ways to activate draft checks: you can activate specific checks or activate multiple checks in bulk.
 
#### Method I. Activate Specific Check

**Step 1:** Navigate to the **Draft** check section, and click on the drafted check that you want to activate, whether you have made changes or wish to activate it as is.

For Demonstration purpose, we have selected the **"Time Distribution Size"** check.

![checks-list](../assets/checks/manage-checks/checks-list-light-26.png#only-light)
![checks-list](../assets/checks/manage-checks/checks-list-dark-26.png#only-dark)

A modal window will appear with the check details. If you want to make any changes to the [check details](https://userguide.qualytics.io/checks/checks-template/#:~:text=Enter%20the%20following%20details%20to%20add%20the%20check%20template%3A), you can edit them.

![check-details](../assets/checks/manage-checks/check-details-light-27.png#only-light)
![check-details](../assets/checks/manage-checks/check-details-dark-27.png#only-dark)

**Step 2:** Click on the **down arrow** icon with the **Update** button. A dropdown menu will appear, click on the **Activate** button.  

![activate](../assets/checks/manage-checks/activate-light-28.png#only-light)
![activate](../assets/checks/manage-checks/activate-dark-28.png#only-dark)

**Step 3:** After clicking on the activate button, your check is now successfully moved to the active checks and a success flash message will appear stating **"Check successfully updated"**  

![success-updated](../assets/checks/manage-checks/success-updated-light-29.png#only-light)
![success-updated](../assets/checks/manage-checks/success-updated-dark-29.png#only-dark)

#### Method II. Activate Draft Checks in Bulk

**Step 1**. Hover over the draft checks and click on the checkbox to select multiple checks in bulk.

![bulk-draft](../assets/checks/manage-checks/bulk-draft-light-94.png#only-light)
![bulk-draft](../assets/checks/manage-checks/bulk-draft-dark-94.png#only-dark)
 
When multiple checks are selected, an action toolbar appears, displaying the total number of checks chosen along with a vertical ellipsis for additional bulk action options.

![action-toolbar](../assets/checks/manage-checks/action-toolbar-light-95.png#only-light)
![action-toolbar](../assets/checks/manage-checks/action-toolbar-dark-95.png#only-dark)

**Step 2**. Click on the vertical ellipsis **(⋮)** and choose **"Activate"** from the dropdown menu to activate the selected checks.

![activate-btn](../assets/checks/manage-checks/activate-btn-light-96.png#only-light)
![activate-btn](../assets/checks/manage-checks/activate-btn-dark-96.png#only-dark)

**Step 3**. A confirmation modal window **“Bulk Activate Check”** will appear, click on the **“Activate”** button to activate the draft checks.

![modal-window](../assets/checks/manage-checks/modal-window-light-97.png#only-light)
![modal-window](../assets/checks/manage-checks/modal-window-dark-97.png#only-dark)

After clicking on the activate button, your drafts checks will be activated and a success message flash will appear stating **“Selected checks have been successfully updated”**

![success-msg](../assets/checks/manage-checks/success-msg-light-98.png#only-light)
![success-msg](../assets/checks/manage-checks/success-msg-dark-98.png#only-dark)

### Set Check as Archived 

You can move an active or draft check into the archive when it is no longer relevant but may still be needed for historical purposes or future use. Archiving helps keep your checks organized without permanently deleting them. There are two ways to archive checks: you can archive individual checks or archive multiple checks in bulk.

#### Method I: Archive Specific Check

You can archive a specific check using two ways: either by directly clicking the archive button on the check or by opening the check and selecting the archive option from the action menu.

##### 1. Archive Directly

**Step 1:** Locate the check (whether Active or Draft) which you want to archive and click on the **Archive** icon (represented by a box with a downward arrow) located on the right side of the check. 

For Demonstration purpose, we have selected the **"Metric"** check.

![archive-icon](../assets/checks/manage-checks/archive-icon-light-30.png#only-light)
![archive-icon](../assets/checks/manage-checks/archive-icon-dark-30.png#only-dark)

**Step 2:** A modal window titled **"Archive Check"** will appear, providing you with the following archive options:

* **Discarded**: Select this option if the check is no longer relevant or suitable for the current business rules or data requirements. This helps in archiving checks that are obsolete but still exist for historical reference.

* **Invalid**: Choose this option if the check is not valid and should be retired from future inference. This helps the system learn from invalid checks and improves its ability to infer valid checks in the future.

![archive-option](../assets/checks/manage-checks/archive-option-light-31.png#only-light)
![archive-option](../assets/checks/manage-checks/archive-option-dark-31.png#only-dark)

**Step 3:** Once you've made your selection, click the **Archive** button to proceed.

![archive](../assets/checks/manage-checks/archive-light-32.png#only-light)
![archive](../assets/checks/manage-checks/archive-dark-32.png#only-dark)

**Step 4:** After clicking on the **Archive** button your check is moved to the archive and a flash message will appear saying **"Check has been successfully archived"**

![archive-success](../assets/checks/manage-checks/archive-success-light-33.png#only-light)
![archive-success](../assets/checks/manage-checks/archive-success-dark-33.png#only-dark)

##### 2. Archive from Action Menu

**Step 1**: Click on the check from the list of available (whether Active or Draft) checks that you want to archive.

For Demonstration purpose, we have selected the **"Not Future"** check.

![checks-list](../assets/checks/manage-checks/checks-list-light-34.png#only-light)
![checks-list](../assets/checks/manage-checks/checks-list-dark-34.png#only-dark)

**Step 2:** A modal window will appear displaying the check details. Click on the **vertical ellipsis** **(⋮)** located in the upper-right corner of the modal window, and click on the **"Archive"** from the drop-down menu. 

![archive](../assets/checks/manage-checks/archive-light-35.png#only-light)
![archive](../assets/checks/manage-checks/archive-dark-35.png#only-dark)

**Step 3:** A modal window titled **“Archive Check”** will appear, providing you with the following archive options:

* **Discarded**: Select this option if the check is no longer relevant or suitable for the current business rules or data requirements. This helps in archiving checks that are obsolete but still exist for historical reference.

* **Invalid**: Choose this option if the check is not valid and should be retired from future inference. This helps the system learn from invalid checks and improves its ability to infer valid checks in the future.

![archive-check](../assets/checks/manage-checks/archive-check-light-36.png#only-light)
![archive-check](../assets/checks/manage-checks/archive-check-dark-36.png#only-dark)

**Step 4:** Once you've made your selection, click the **Archive** button to proceed.

![archive](../assets/checks/manage-checks/archive-light-37.png#only-light)
![archive](../assets/checks/manage-checks/archive-dark-37.png#only-dark)

**Step 5:** After clicking on the **Archive** button your check is moved to the archive and a flash message will appear saying **"Check has been successfully archived"**

![success-archive](../assets/checks/manage-checks/success-archive-light-38.png#only-light)
![success-archive](../assets/checks/manage-checks/success-archive-dark-38.png#only-dark)

#### Method II: Archive Checks in Bulk

You can archive multiple checks in a single step, deactivating and storing them for future reference or restoration while keeping your active checks uncluttered.

**Step 1:** Hover over the checks (whether Active or Draft) and click on the checkbox to select multiple checks.

![check-box](../assets/checks/manage-checks/check-box-light-39.png#only-light)
![check-box](../assets/checks/manage-checks/check-box-dark-39.png#only-dark)

When multiple checks are selected, an action toolbar appears, displaying the total number of selected checks along with a vertical ellipsis for additional bulk action options.

![action-menu](../assets/checks/manage-checks/action-menu-light-40.png#only-light)
![action-menu](../assets/checks/manage-checks/action-menu-dark-40.png#only-dark)

**Step 2:** Click on the **vertical ellipsis (⋮)** and choose **"Archive"** from the dropdown menu to archive the selected checks.

![archive](../assets/checks/manage-checks/archive-light-41.png#only-light)
![archive](../assets/checks/manage-checks/archive-dark-41.png#only-dark)

A modal window will appear, providing you with the following archive options:

**1. Delete all anomalies associated with the checks**: Toggle this option **"On"** if you want to delete any anomalies related to the selected checks when archiving them.

**2. Archive Options**: You are presented with two options to categorize why the checks are being archived:

* **Discarded**: Select this option if the check is no longer relevant or suitable for the current business rules or data requirements. This helps in archiving checks that are obsolete but still exist for historical reference.

* **Invalid**: Choose this option if the check is not valid and should be retired from future inference. This helps the system learn from invalid checks and improves its ability to infer valid checks in the future.

![archive-check](../assets/checks/manage-checks/archive-check-light-42.png#only-light)
![archive-check](../assets/checks/manage-checks/archive-check-dark-42.png#only-dark)

**Step 3:**  Once you've made your selections, click the **"Archive"** button to confirm and archive the checks.  

![archive](../assets/checks/manage-checks/archive-light-43.png#only-light)
![archive](../assets/checks/manage-checks/archive-dark-43.png#only-dark)

**Step 4:** After clicking the **"Archive"** button, your selected checks (whether Active or Draft) will be archived successfully and a success flash message will appear stating, **"Checks have been successfully archived."**

![success-archive](../assets/checks/manage-checks/success-archive-light-44.png#only-light)
![success-archive](../assets/checks/manage-checks/success-archive-dark-44.png#only-dark)

### Restore Archived Checks

If a check has been archived, then you can restore it back to an active state or in a draft state. This allows you to reuse your checks that were previously archived without having to recreate them from scratch.

**Step 1:** Click on **Archived** from the **navigation bar** in the **Checks** section to view all archived checks.

![archive](../assets/checks/manage-checks/archive-light-45.png#only-light)
![archive](../assets/checks/manage-checks/archive-dark-45.png#only-dark)

**Step 2**: Click on the archived check which you want to restore as an active or draft check.

For Demonstration purpose, we have selected the **"Time Distribution Size"** check.

![archive-checks](../assets/checks/manage-checks/archive-checks-light-46.png#only-light)
![archive-checks](../assets/checks/manage-checks/archive-checks-dark-46.png#only-dark)

A modal window will appear with the check details.

![check-details](../assets/checks/manage-checks/check-details-light-47.png#only-light)
![check-details](../assets/checks/manage-checks/check-details-dark-47.png#only-dark)

**Step 3**: If you want to make any changes to the check, you can edit it. Otherwise, click on the **Restore** button to restore it as an active check.

![restore-check](../assets/checks/manage-checks/restore-check-light-48.png#only-light)
![restore-check](../assets/checks/manage-checks/restore-check-dark-48.png#only-dark)

To restore the check as a draft, click on the arrow icon next to the **Restore** button. A dropdown menu will appear—select **Restore as Draft** from the options.

![restore-as-draft](../assets/checks/manage-checks/restore-as-draft-light-49.png#only-light)
![restore-as-draft](../assets/checks/manage-checks/restore-as-draft-dark-49.png#only-dark)

After clicking the **Restore** button, the check will be successfully restored as either an active or draft check, depending on your selection. A success message will appear confirming, **"Check successfully updated."**

![success-updated](../assets/checks/manage-checks/success-updated-light-50.png#only-light)
![success-updated](../assets/checks/manage-checks/success-updated-dark-50.png#only-dark)

### Edit Check

You can edit an existing check to modify its properties, such as the rule type, coverage, filter clause, or description. Updating a check ensures that it stays aligned with evolving data requirements and maintains data quality as conditions change. There are two methods for editing checks: you can either edit specific checks or edit multiple checks in bulk.

!!! note 
       When editing multiple checks in bulk, only the filter clause and tags can be modified. 

#### Method I. Edit Specific Check

**Step 1:** Click on the check you want to edit, whether it is an active or draft check.

For Demonstration purpose, we have selected the **"Metric"** check.

![edit-check](../assets/checks/manage-checks/edit-check-light-51.png#only-light)
![edit-check](../assets/checks/manage-checks/edit-check-dark-51.png#only-dark)

A modal window will appear with the check details. 

![modal-win](../assets/checks/manage-checks/modal-win-light-52.png#only-light)
![modal-win](../assets/checks/manage-checks/modal-win-dark-52.png#only-dark)

**Step 2:** Modify the [check details](https://userguide.qualytics.io/checks/checks-template/#:~:text=Enter%20the%20following%20details%20to%20add%20the%20check%20template%3A) as needed based on your preferences.

![check-detail](../assets/checks/manage-checks/check-detail-light-53.png#only-light)
![check-detail](../assets/checks/manage-checks/check-detail-dark-53.png#only-dark)

**Step 3:** Once you have edited the check details, then click on the **Validate** button. This will perform a validation operation on the check without saving it. The validation allows you to verify that the logic and parameters defined for the check are correct.

![validate-btn](../assets/checks/manage-checks/validate-btn-light-54.png#only-light)
![validate-btn](../assets/checks/manage-checks/validate-btn-dark-54.png#only-dark)

If the validation is successful, a green message saying **"Validation Successful"** will appear. 

![validate-msg](../assets/checks/manage-checks/validate-msg-light-55.png#only-light)
![validate-msg](../assets/checks/manage-checks/validate-msg-dark-55.png#only-dark)

If the validation fails, a red message saying **"Failed Validation"** will appear. This typically occurs when the check logic or parameters do not match the data properly.

![failed-msg](../assets/checks/manage-checks/failed-msg-light-56.png#only-light)
![failed-msg](../assets/checks/manage-checks/failed-msg-dark-56.png#only-dark)

**Step 3:** Once you have a successful validation, click the **"Update"** button. The system will update the changes you've made to the check, including changes to the fields, filter clause, coverage, description, tags, or metadata.

![update-btn](../assets/checks/manage-checks/update-btn-light-57.png#only-light)
![update-btn](../assets/checks/manage-checks/update-btn-dark-57.png#only-dark)

After clicking on the Update button, your check is successfully updated and a success flash message will appear stating **"Check successfully updated"**.

![update-msg](../assets/checks/manage-checks/update-msg-light-58.png#only-light)
![update-msg](../assets/checks/manage-checks/update-msg-dark-58.png#only-dark)

#### Method II. Edit Checks in Bulk

You can easily apply changes to multiple checks at once, saving time by editing several checks simultaneously without having to modify each one individually.

**Step 1:** Hover over the checks (whether Active or Draft) and click on the checkbox to select multiple checks.

![edit-check](../assets/checks/manage-checks/edit-check-light-59.png#only-light)
![edit-check](../assets/checks/manage-checks/edit-check-dark-59.png#only-dark)

When multiple checks are selected, an action toolbar appears, displaying the total number of selected checks along with a vertical ellipsis for additional bulk action options.

![select](../assets/checks/manage-checks/select-light-60.png#only-light)
![select](../assets/checks/manage-checks/select-dark-60.png#only-dark)

**Step 2:** Click on the vertical ellipses **(⋮)** and select **"Edit"** from the dropdown menu to make changes to the selected checks.

![edit-btn](../assets/checks/manage-checks/edit-btn-light-61.png#only-light)
![edit-btn](../assets/checks/manage-checks/edit-btn-dark-61.png#only-dark)

**Step 3:** A modal window titled **"Bulk Edit Checks"** will appear. Here you can only modify the **"filter clause"** and **"tags"** of the selected checks.

![modal-window](../assets/checks/manage-checks/modal-window-light-62.png#only-light)
![modal-window](../assets/checks/manage-checks/modal-window-dark-62.png#only-dark)

**Step 4:** Toggle on the options (Filter Clause or Tags) that you want to modify for the selected checks, and make the necessary changes.

!!! note
       This action will overwrite the existing data for the selected checks.

![modal-window](../assets/checks/manage-checks/modal-window-light-63.png#only-light)
![modal-window](../assets/checks/manage-checks/modal-window-dark-63.png#only-dark)

**Step 5:** Once you have made the changes, click on the **"Save"** button.

![save-btn](../assets/checks/manage-checks/save-btn-light-64.png#only-light)
![save-btn](../assets/checks/manage-checks/save-btn-dark-64.png#only-dark)

After clicking the "Save" button, your selected checks will be updated with the new changes. A success message will appear stating, **"Selected checks have been successfully updated."**

![update-msg](../assets/checks/manage-checks/update-msg-light-65.png#only-light)
![update-msg](../assets/checks/manage-checks/update-msg-dark-65.png#only-dark)

### Delete Checks

You can delete a check permanently, removing it from the system, and this is an **irreversible action**. Once you delete it, the check cannot be restored. By deleting the check, you ensure it will no longer appear in active or archived lists, making the system more streamlined and organized. There are two methods for deleting checks: you can either delete individual checks or delete multiple checks in bulk.

!!! note 
       You can only delete archived checks. If you want to delete an active or draft check, you must first move it to the archive, and then you can delete it.

!!! warning 
       Deleting a check is a one-time action. It cannot be restored after deletion.

#### Method I. Delete Specific Check

**Step 1:** Click on **Archived** from the **navigation bar** in the **Checks** section to view all archived checks.

![archived-btn](../assets/checks/manage-checks/archived-btn-light-66.png#only-light)
![archived-btn](../assets/checks/manage-checks/archived-btn-dark-66.png#only-dark)

**Step 2:** Locate the check, that you want to delete and click on the **Delete** icon located on the right side of the check.

For Demonstration purpose, we have selected the **"Time Distribution Size"** check.

![delete-btn](../assets/checks/manage-checks/delete-btn-light-67.png#only-light)
![delete-btn](../assets/checks/manage-checks/delete-btn-dark-67.png#only-dark)

**Step 3:** A confirmation modal window will appear, click on the **Delete** button to permanently remove the check from the system. 

![delete-btn](../assets/checks/manage-checks/delete-btn-light-68.png#only-light)
![delete-btn](../assets/checks/manage-checks/delete-btn-dark-68.png#only-dark)

**Step 4:** After clicking on the delete button, your check is successfully deleted and a success flash message will appear saying **"Check has been successfully deleted"**

![success-msg](../assets/checks/manage-checks/success-msg-light-69.png#only-light)
![success-msg](../assets/checks/manage-checks/success-msg-dark-69.png#only-dark)

#### Method II. Delete Check in Bulk

You can permanently delete multiple checks from the system in one action. This process is irreversible, so it should be used when you are certain that the checks are no longer needed.

!!! note 
       For bulk archiving checks, the only available option is Bulk Delete. There is no option to Bulk Restore to draft or activate archived checks.

**Step 1:** Hover over the archived checks and click on the checkbox to select checks in bulk.  

![dlt-bulk](../assets/checks/manage-checks/dlt-bulk-light-70.png#only-light)
![dlt-bulk](../assets/checks/manage-checks/dlt-bulk-dark-70.png#only-dark)

When multiple checks are selected, an action toolbar appears, displaying the total number of selected checks along with a vertical ellipsis for additional bulk action options.

![select](../assets/checks/manage-checks/select-light-71.png#only-light)
![select](../assets/checks/manage-checks/select-dark-71.png#only-dark)

**Step 2:** Click on the **vertical ellipsis (⋮)** and choose **"Delete"** from the dropdown menu to delete the selected checks.  

![delete-ellp](../assets/checks/manage-checks/delete-ellp-light-72.png#only-light)
![delete-ellp](../assets/checks/manage-checks/delete-ellp-dark-72.png#only-dark)

**Step 3:** A confirmation modal window will appear, click on the **"Delete"** button to permanently delete the selected checks.

![delete-btn](../assets/checks/manage-checks/delete-btn-light-73.png#only-light)
![delete-btn](../assets/checks/manage-checks/delete-btn-dark-73.png#only-dark)

After clicking on the "Delete" button, your selected checks will be permanently deleted, and a success flash message will appear stating, **"Checks have been successfully deleted."**  
   
![delete-msg](../assets/checks/manage-checks/delete-msg-light-74.png#only-light)
![delete-msg](../assets/checks/manage-checks/delete-msg-dark-74.png#only-dark)

### Mark Check as Favorite

Marking a check as a favorite allows you to quickly access and prioritize the checks that are most important to your data validation process. This helps streamline workflows by keeping frequently used or critical checks easily accessible, ensuring you can monitor and manage them efficiently. By marking a check as a favorite, it will appear in the "Favorite" category for faster retrieval and management.

**Step 1:** Locate the check which you want to mark as a favorite and click on the bookmark icon located on the right side of the check.

![mark-fav](../assets/checks/manage-checks/mark-fav-light-75.png#only-light)
![mark-fav](../assets/checks/manage-checks/mark-fav-dark-75.png#only-dark)

After Clicking on the bookmark icon your check is successfully marked as a favorite and a success flash message will appear stating **"Check has been favorited"**

![fav-msg](../assets/checks/manage-checks/fav-msg-light-76.png#only-light)
![fav-msg](../assets/checks/manage-checks/fav-msg-dark-76.png#only-dark)

To unmark a check, simply click on the bookmark icon of the marked check. This will remove it from your favorites.

![remove-fav](../assets/checks/manage-checks/remove-fav-light-77.png#only-light)
![remove-fav](../assets/checks/manage-checks/remove-fav-dark-77.png#only-dark)

## Clone Check

You can clone both active and draft checks to create a duplicate copy of an existing check. This is useful when you want to create a new check based on the structure of an existing one, allowing you to make adjustments without affecting the original check.

**Step 1**: Click on the check (whether Active or Draft) that you want to clone.

For Demonstration purpose, we have selected the **"Greater Than Field"** check.

![clone-check](../assets/checks/manage-checks/clone-check-light-78.png#only-light)
![clone-check](../assets/checks/manage-checks/clone-check-dark-78.png#only-dark)

**Step 2**: A modal window will appear displaying the check details. Click on the **vertical ellipsis (⋮)** located in the upper-right corner of the modal window, and select **"Clone"** from the drop-down menu.

![clone-btn](../assets/checks/manage-checks/clone-btn-light-79.png#only-light)
![clone-btn](../assets/checks/manage-checks/clone-btn-dark-79.png#only-dark)

**Step 3:** After clicking the Clone button, a modal window will appear. This window allows you to adjust the cloned check's details.

![modal-window](../assets/checks/manage-checks/modal-window-light-80.png#only-light)
![modal-window](../assets/checks/manage-checks/modal-window-dark-80.png#only-dark)

**1.** If you toggle on the **"Associate with a Check Template"** option, the cloned check will be linked to a specific template.

![toggle-on](../assets/checks/manage-checks/toggle-on-light-81.png#only-light)
![toggle-on](../assets/checks/manage-checks/toggle-on-dark-81.png#only-dark)

Choose a **Template** from the dropdown menu that you want to associate with the cloned check. The check will inherit properties from the selected template.

* **Locked:** The check will automatically sync with any future updates made to the template, but you won't be able to modify the check's properties directly.

* **Unlocked:** You can modify the check, but future updates to the template will no longer affect this check.

![associate-check](../assets/checks/manage-checks/associate-check-light-82.png#only-light)
![associate-check](../assets/checks/manage-checks/associate-check-dark-82.png#only-dark)

**2.** If you toggle off the **"Associate with a Check Template"** option, the cloned check will not be linked to any template, which allows you full control to modify the properties independently.

![toggle-off](../assets/checks/manage-checks/toggle-off-light-83.png#only-light)
![toggle-off](../assets/checks/manage-checks/toggle-off-dark-83.png#only-dark)

Select the appropriate **Rule type** for the check from the dropdown menu.

![rule-type](../assets/checks/manage-checks/rule-type-light-84.png#only-light)
![rule-type](../assets/checks/manage-checks/rule-type-dark-84.png#only-dark)

**Step 4:** Once you have selected the template or rule type, fill up the remaining [check details](https://userguide.qualytics.io/checks/checks-template/#:~:text=Enter%20the%20following%20details%20to%20add%20the%20check%20template%3A) as required. 

![check-detail](../assets/checks/manage-checks/check-detail-light-85.png#only-light)
![check-detail](../assets/checks/manage-checks/check-detail-dark-85.png#only-dark)

**Step 5:** After completing all the check details, click on the **"Validate"** button. This will perform a validation operation on the check without saving it. The validation allows you to verify that the logic and parameters defined for the check are correct. It ensures that the check will work as expected by running it against the data without committing any changes.

![validate-btn](../assets/checks/manage-checks/validate-btn-light-86.png#only-light)
![validate-btn](../assets/checks/manage-checks/validate-btn-dark-86.png#only-dark)

If the validation is successful, a green message saying **"Validation Successful"** will appear. 

![validation-success](../assets/checks/manage-checks/validation-success-light-87.png#only-light)
![validation-success](../assets/checks/manage-checks/validation-success-dark-87.png#only-dark)

If the validation fails, a red message saying **"Failed Validation"** will appear. This typically occurs when the check logic or parameters do not match the data properly.

![failed-validation](../assets/checks/manage-checks/failed-validation-light-88.png#only-light)
![failed-validation](../assets/checks/manage-checks/failed-validation-dark-88.png#only-dark)

**Step 6:** Once you have a successful validation, click the **"Save"** button. The system will save any modifications you've made to the check, and create a clone of that check on basis of your changes.  

![save-btn](../assets/checks/manage-checks/save-btn-light-89.png#only-light)
![save-btn](../assets/checks/manage-checks/save-btn-dark-89.png#only-dark)

After clicking on the **"Save"** button your check is successfully created and a success flash message will appear stating **"Check successfully created".**

![success-msgs](../assets/checks/manage-checks/success-msgs-light-90.png#only-light)
![success-msgs](../assets/checks/manage-checks/success-msgs-dark-90.png#only-dark)

## Create a Quality Check template

You can add checks as a Template, which allows you to create a reusable framework for quality checks. By using templates, you standardize the validation process, enabling the creation of multiple checks with similar rules and criteria across different datastores. This ensures consistency and efficiency in managing data quality checks.

**Step 1:** Locate the check (whether Active or Draft) which you want to archive and click on that check.

For Demonstration purpose, we have selected the **"Matches Pattern"** check.

![select-check](../assets/checks/manage-checks/select-check-light-91.png#only-light)
![select-check](../assets/checks/manage-checks/select-check-dark-91.png#only-dark)

**Step 2:** A modal window will appear displaying the check details. Click on the **vertical ellipsis (⋮)** located in the upper-right corner of the modal window, and select **"Template"** from the drop-down menu.

![template-btn](../assets/checks/manage-checks/template-btn-light-92.png#only-light)
![template-btn](../assets/checks/manage-checks/template-btn-dark-92.png#only-dark)

After clicking the **"Template"** button, the check will be saved and created as a template in the library, and a success flash message will appear stating, **"The quality check template has been created successfully."** This allows you to reuse the template for future checks, streamlining the validation process.

![quality-check](../assets/checks/manage-checks/quality-check-light-93.png#only-light)
![quality-check](../assets/checks/manage-checks/quality-check-dark-93.png#only-dark)

#### Method II: Activate Draft Checks in Bulk

Once you have completed refining the validation rules and made the necessary adjustments, you can activate multiple draft checks in bulk. Activating these checks in bulk ensures that all the defined criteria are enforced across the data simultaneously.

**Step 1**. Hover over the draft checks and click on the checkbox to select multiple checks in bulk.

![bulk-draft](../assets/checks/manage-checks/bulk-draft-light-94.png#only-light)
![bulk-draft](../assets/checks/manage-checks/bulk-draft-dark-94.png#only-dark)
 
When multiple checks are selected, an action toolbar appears, displaying the total number of checks chosen along with a vertical ellipsis for additional bulk action options.

![action-toolbar](../assets/checks/manage-checks/action-toolbar-light-95.png#only-light)
![action-toolbar](../assets/checks/manage-checks/action-toolbar-dark-95.png#only-dark)

**Step 2**. Click on the vertical ellipsis (⋮) and choose **"Activate"** from the dropdown menu to activate the selected checks.

![activate-btn](../assets/checks/manage-checks/activate-btn-light-96.png#only-light)
![activate-btn](../assets/checks/manage-checks/activate-btn-dark-96.png#only-dark)

**Step 3**. A confirmation modal window “Bulk Activate Check” will appear, click on the **“Activate”** button to activate the draft checks.

![modal-window](../assets/checks/manage-checks/modal-window-light-97.png#only-light)
![modal-window](../assets/checks/manage-checks/modal-window-dark-97.png#only-dark)

After clicking on the activate button, your drafts checks will be activated and a success message flash will appear stating **“Selected checks have been successfully updated”**

![success-msg](../assets/checks/manage-checks/success-msg-light-98.png#only-light)
![success-msg](../assets/checks/manage-checks/success-msg-dark-98.png#only-dark)

