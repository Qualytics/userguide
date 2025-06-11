# Manage Checks in Datastore

Managing your checks within a datastore is important to maintain data integrity and ensure quality. You can categorize, create, update, archive, restore, delete, and clone checks, making it easier to apply validation rules across the datastores. The system allows for checks to be set as active, draft, or archived based on their current state of use. You can also define reusable templates for quality checks to streamline the creation of multiple checks with similar criteria. With options for important and favorite, users have full flexibility to manage data quality efficiently.

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

You can also categorize the active checks based on their importance and favorites to streamline your data quality monitoring.

**1. Important:** Shows only checks that are marked as important. These checks are prioritized based on their significance, typically assigned a weight of 7 or higher.

!!! note 
    Important checks are prioritized based on a weight of 7 or higher.

![important](../assets/checks/manage-checks/important-light-5.png#only-light)
![important](../assets/checks/manage-checks/important-dark-5.png#only-dark)

**2. Favorite:** Displays checks that have been marked as favorites. This allows you to quickly access checks that you use or monitor frequently. 

![favorite](../assets/checks/manage-checks/favorite-light-6.png#only-light)
![favorite](../assets/checks/manage-checks/favorite-dark-6.png#only-dark)

**3. All:** Displays a comprehensive view of all active checks, including important, favorite and any checks that do not fall under these specific categories. 

![all](../assets/checks/manage-checks/all-light-8.png#only-light)
![all](../assets/checks/manage-checks/all-dark-8.png#only-dark)

### Draft Checks

By selecting **Draft**, you can view checks that have been created but have not yet been applied to the data. These checks are in the drafting stage, allowing for adjustments and reviews before activation. Draft checks provide flexibility to experiment with different validation rules without affecting the actual data.

![draft](../assets/checks/manage-checks/draft-light-9.png#only-light)
![draft](../assets/checks/manage-checks/draft-dark-9.png#only-dark)

You can also categorize the draft checks based on their importance and favorites to prioritize and organize them effectively during the review and adjustment process.

**1. Important:** Shows only checks that are marked as important. These checks are prioritized based on their significance, typically assigned a weight of 7 or higher. 

![important](../assets/checks/manage-checks/important-light-10.png#only-light)
![important](../assets/checks/manage-checks/important-dark-10.png#only-dark)

**2 Favorite:** Displays checks that have been marked as favorites. This allows you to quickly access checks that you use or monitor frequently.  

![favorite](../assets/checks/manage-checks/favorite-light-11.png#only-light)
![favorite](../assets/checks/manage-checks/favorite-dark-11.png#only-dark)

**3. All:** Displays a comprehensive view of all draft checks, including important, favorite and any checks that do not fall under these specific categories.   

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
Last Editor indicates who most recently made changes to the check. It helps track who is responsible for the latest updates or modifications. This is useful for accountability and collaboration within teams.

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

**Step 1:** Click on the vertical ellipsis (⋮) next to the active check you want to move to draft state, and select Edit from the dropdown menu.

For Demonstration purpose, we have selected the **"After Date Time"** check.

![checks-list](../assets/checks/manage-checks/checks-list-light-18.png#only-light)
![checks-list](../assets/checks/manage-checks/checks-list-dark-18.png#only-dark)

**Step 2**: A modal window will appear displaying the check details. Click on the **vertical ellipsis (⋮)** located in the upper-right corner of the modal window, and select **"Draft"** from the drop-down menu.

![draft](../assets/checks/manage-checks/draft-light-19.png#only-light)
![draft](../assets/checks/manage-checks/draft-dark-19.png#only-dark)

**Step 3:** After clicking on **"Draft"**, the check will be successfully moved to the draft state, and a success flash message will appear stating, **"The checks have been successfully updated."**

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

After clicking the **"Update"** button, your selected checks will be moved to draft, and a success message will appear stating, **"The checks have been successfully updated."**

![success-updated](../assets/checks/manage-checks/success-updated-light-25.png#only-light)
![success-updated](../assets/checks/manage-checks/success-updated-dark-25.png#only-dark)

### Activate Draft Check

You can activate the draft checks after when you have worked on the check, make adjustments, and refine the validation rules. By activating the draft check and making it live, ensures that the defined criteria are enforced on the data. There are two ways to activate draft checks: you can activate specific checks or activate multiple checks in bulk.
 
#### Method I. Activate Specific Check

**Step 1:** Navigate to the **Draft** check section, and click on the vertical ellipsis (⋮) next to the draft check you want to activate, and select Edit from the dropdown menu.

For Demonstration purpose, we have selected the **"Metric"** check.

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

After clicking on the activate button, your drafts checks will be activated and a success message flash will appear stating **“The checks have been successfully updated”**

![success-msg](../assets/checks/manage-checks/success-msg-light-98.png#only-light)
![success-msg](../assets/checks/manage-checks/success-msg-dark-98.png#only-dark)

### Set Check as Archived 

You can move an active or draft check into the archive when it is no longer relevant but may still be needed for historical purposes or future use. Archiving helps keep your checks organized without permanently deleting them. There are two ways to archive checks: you can archive individual checks or archive multiple checks in bulk.

#### Method I: Archive Specific Check

You can archive a specific check using two ways: either by directly clicking the archive button on the check or by opening the check and selecting the archive option from the action menu.

##### 1. Archive Directly

**Step 1:** Locate the check (whether Active or Draft) which you want to archive and click the vertical ellipsis (⋮) next to it, and select Archive from the dropdown menu.

For Demonstration purpose, we have selected the **"After Date Time"** check.

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

**Step 4:** After clicking on the **Archive** button your check is moved to the archive and a flash message will appear saying **" The check has been successfully archived"**

![archive-success](../assets/checks/manage-checks/archive-success-light-33.png#only-light)
![archive-success](../assets/checks/manage-checks/archive-success-dark-33.png#only-dark)

##### 2. Archive from Action Menu

**Step 1**: Locate the check (whether Active or Draft) which you want to archive and click the vertical ellipsis (⋮) next to it, and select Edit from the dropdown menu.

For Demonstration purpose, we have selected the **"Metric"** check.

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

**Step 5:** After clicking on the **Archive** button your check is moved to the archive and a flash message will appear saying **" The check has been successfully archived"**

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

**Step 4:** After clicking the **"Archive"** button, your selected checks (whether Active or Draft) will be archived successfully and a success flash message will appear stating, **"The checks have been successfully archived."**

![success-archive](../assets/checks/manage-checks/success-archive-light-44.png#only-light)
![success-archive](../assets/checks/manage-checks/success-archive-dark-44.png#only-dark)

### Restore Archived Checks

If a check has been archived, then you can restore it back to an active state or in a draft state. This allows you to reuse your checks that were previously archived without having to recreate them from scratch.

**Step 1:** Click on **Archived** from the **navigation bar** in the **Checks** section to view all archived checks.

![archive](../assets/checks/manage-checks/archive-light-45.png#only-light)
![archive](../assets/checks/manage-checks/archive-dark-45.png#only-dark)

**Step 2**: Click on the vertical ellipsis (⋮) next to the active check you want to restore as an active or draft check and select edit form the drop down menu.

For Demonstration purpose, we have selected the **"Metric"** check.

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

**Step 1:** Click on the vertical ellipsis (⋮) next to the check you want to edit, whether it is an active or draft check and select **Edit** from the drop down menu

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

After clicking on the Update button, your check is successfully updated and a success flash message will appear stating **"The check has been successfully updated"**.

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

After clicking the "Save" button, your selected checks will be updated with the new changes. A success message will appear stating, **"The checks have been successfully updated."**

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

**Step 2:** Locate the check, that you want to delete and click on the vertical ellipsis (⋮) and select **Delete** from the drop-down menu. 

For Demonstration purpose, we have selected the **"Time Distribution Size"** check.

![delete-btn](../assets/checks/manage-checks/delete-btn-light-67.png#only-light)
![delete-btn](../assets/checks/manage-checks/delete-btn-dark-67.png#only-dark)

**Step 3:** A confirmation modal window will appear, click on the **Delete** button to permanently remove the check from the system. 

![delete-btn](../assets/checks/manage-checks/delete-btn-light-68.png#only-light)
![delete-btn](../assets/checks/manage-checks/delete-btn-dark-68.png#only-dark)

**Step 4:** After clicking on the delete button, your check is successfully deleted and a success flash message will appear saying **"The check has been successfully deleted"**

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

After clicking on the "Delete" button, your selected checks will be permanently deleted, and a success flash message will appear stating, **"The checks have been successfully deleted."**  
   
![delete-msg](../assets/checks/manage-checks/delete-msg-light-74.png#only-light)
![delete-msg](../assets/checks/manage-checks/delete-msg-dark-74.png#only-dark)

### Mark Check as Favorite

Marking a check as a favorite allows you to quickly access and prioritize the checks that are most important to your data validation process. This helps streamline workflows by keeping frequently used or critical checks easily accessible, ensuring you can monitor and manage them efficiently. By marking a check as a favorite, it will appear in the "Favorite" category for faster retrieval and management.

**Step 1:** Locate the check which you want to mark as a favorite and click on the bookmark icon located on the right side of the check.

![mark-fav](../assets/checks/manage-checks/mark-fav-light-75.png#only-light)
![mark-fav](../assets/checks/manage-checks/mark-fav-dark-75.png#only-dark)

After Clicking on the bookmark icon your check is successfully marked as a favorite and a success flash message will appear stating **"The check has been favorited"**

![fav-msg](../assets/checks/manage-checks/fav-msg-light-76.png#only-light)
![fav-msg](../assets/checks/manage-checks/fav-msg-dark-76.png#only-dark)

To unmark a check, simply click on the bookmark icon of the marked check. This will remove it from your favorites.

![remove-fav](../assets/checks/manage-checks/remove-fav-light-77.png#only-light)
![remove-fav](../assets/checks/manage-checks/remove-fav-dark-77.png#only-dark)

## Clone Check

You can clone both active and draft checks to create a duplicate copy of an existing check. This is useful when you want to create a new check based on the structure of an existing one, allowing you to make adjustments without affecting the original check.

**Step 1**: Click the vertical ellipsis (⋮) next to the check (whether Active or Draft) that you want to clone and select **Edit** from the drop- down menu.

For Demonstration purpose, we have selected the **"Metric"** check.

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

For Demonstration purpose, we have selected the **"Not Exists In"** check.

![select-check](../assets/checks/manage-checks/clone-check-light-78.png#only-light)
![select-check](../assets/checks/manage-checks/clone-check-dark-78.png#only-dark)

**Step 2:** A modal window will appear displaying the check details. Click on the **vertical ellipsis (⋮)** located in the upper-right corner of the modal window, and select **"Template"** from the drop-down menu.

![template-btn](../assets/checks/manage-checks/template-btn-light-92.png#only-light)
![template-btn](../assets/checks/manage-checks/template-btn-dark-92.png#only-dark)

After clicking the **"Template"** button, the check will be saved and created as a template in the library, and a success flash message will appear stating, **"The quality check template has been created successfully."** This allows you to reuse the template for future checks, streamlining the validation process.

![quality-check](../assets/checks/manage-checks/quality-check-light-93.png#only-light)
![quality-check](../assets/checks/manage-checks/quality-check-dark-93.png#only-dark)

## Check Details

Check Detail View displays all key information related to a specific data quality check. It shows what the check is monitoring, how it's configured, where it's applied in the dataset, and whether any issues have been found. It also includes sections for viewing the check’s recent performance, related activities, and any additional metadata. This view helps users easily understand the purpose and current state of the check.

**Step 1:** Click on the check that you want to see the details of.

![success-msg](../assets/checks/manage-checks/see-light-98.png#only-light)
![success-msg](../assets/checks/manage-checks/see-dark-98.png#only-dark)

You will be navigated to the detail section, where you can view the **Summary**, **Observability,** **Properties**, **Activity**, and **Metadata** information.

![detail](../assets/checks/manage-checks/detail-light-98.png#only-light)
![detail](../assets/checks/manage-checks/detail-dark-98.png#only-dark)

### Summary Section

The Summary section shows that a data quality check is applied to a field and is currently active. It indicates that the check was created automatically by the system, is being applied to the entire dataset, and has a set importance level. It also shows when the check last ran and whether there are any current issues found in the data.

| No. | Field | Description |
| :---- | :---- | :---- |
| 1. | Check & Status| The type of check applied to the data. In this case, it's a **Unique** check to ensure no duplicate values and the check is **Active**, meaning it's currently being applied. |
| 2. | Type | This check is **Inferred**, meaning it was automatically created by the system. |
| 3. | Last Asserted | Shows when the check was last run – **13 hours ago** in this case. |
| 4. | Weight | Indicates the importance or priority of this check – the weight is **8**. |
| 5. | Coverage | How much data this check applies to – here it's **100%**, meaning it applies to the whole dataset. |
| 6. | Active Anomalies | Number of current issues found – **5 anomalies** are active right now. |
| 7. | Description | Explains the rule or condition that the check is validating. |
| 8. | Tags | Displays any tags linked to the check. Users can also add new tags by clicking on the tag area. |

![summary-msg](../assets/checks/manage-checks/summary-light-98.png#only-light)
![summary-msg](../assets/checks/manage-checks/summary-dark-98.png#only-dark)

### Observability Section

**Observability** provides a visual overview of how a check performs over time by tracking assertion results. It helps identify trends, failures, or anomalies using daily status indicators across a selected timeframe.

![observability](../assets/checks/manage-checks/observability-light-98.png#only-light)
![observability](../assets/checks/manage-checks/observability-dark-98.png#only-dark)

Users can hover over any date in the timeline to view detailed assertion information, including result status, number of asserted records, and anomalous records for that day.

![hover](../assets/checks/manage-checks/hover-light-98.png#only-light)
![hover](../assets/checks/manage-checks/hover-dark-98.png#only-dark)

### Properties Section

The Properties section explains where this check is applied. In this case, the check is applied to a table called **customer**. It's focused on the **phone string** field to ensure that no two records have the same phone number. There is no filter added, so the check is applied to all rows in the table. This helps maintain clean and trustworthy data, especially when phone numbers must be unique per customer.

![properties](../assets/checks/manage-checks/properties-light-98.png#only-light)
![properties](../assets/checks/manage-checks/properties-dark-98.png#only-dark)

### Activity Section

The Activity section shows a brief history of what has happened with this check. First, the system (Qualytics) created the check one day ago. Later, the system also changed the weight of the check to 8. These changes help keep track of how the check is evolving over time and who made the updates.

![activity](../assets/checks/manage-checks/activity-light-98.png#only-light)
![activity](../assets/checks/manage-checks/activity-dark-98.png#only-dark)

### Metadata Section

Currently, there is no extra metadata added to this check. Metadata can include additional notes or properties, but in this case, it's left blank.

![metadata](../assets/checks/manage-checks/metadata-light-98.png#only-light)
![metadata](../assets/checks/manage-checks/metadata-dark-98.png#only-dark)

## Filter and Sort

Filter and Sort options allow you to organize your checks by various criteria, such as Weight, Active Anomalies, Coverage, Created Date, and Rules. You can also apply filters to refine your list of checks based on Check Type, Asserted State (Passed, Failed, Not Asserted), Tags, Tables, and Fields.

### Sort

You can sort your checks by **Active Anomalies**, **Coverage**, **Created Date**, **Last Asserted**, **Rules**, and **Weight** to easily organize and prioritize them according to your needs.

![sort](../assets/checks/manage-checks/sort-light.png#only-light)
![sort](../assets/checks/manage-checks/sort-dark.png#only-dark)

| No  | Sort By Option | Description |
| :---- | :---- | :---- |
| **1** | **Active Anomalies** | Sort checks based on the number of active anomalies. |
| **2** | **Coverage** | Sort checks by data coverage percentage. |
| **3** | **Created Date** | Sort checks according to the date they were created. |
| **4** | **Last Asserted** | Sorts by the last time the check was executed. |
| **5** | **Rules** | Sort checks based on specific rules applied to the checks. |
| **6** | **Weight** | Sort checks by their assigned weight or importance level. |

Whatever sorting option is selected, you can arrange the data either in ascending or descending order by clicking the caret button next to the selected sorting criteria.

![arrange](../assets/checks/manage-checks/arrange-light.png#only-light)
![arrange](../assets/checks/manage-checks/arrange-dark.png#only-dark)

### Filter

You can filter your checks based on values like **Check Type**, **Asserted State**, **Rule**, **Tags**, **Table**, **Field**, and **Template**.

![filter](../assets/checks/manage-checks/filter-light.png#only-light)
![filter](../assets/checks/manage-checks/filter-dark.png#only-dark)

|No     |     Filter  |   Filter Value  |  Description|
| :---- |  :----       |  :----         |  :----      |
| **1** | **Check Type** | **All** | Displays all types of checks, both [inferred](../checks/inferred-check.md) and [authored](../checks/authored-check.md). |
|  |  | **Inferred** | Shows system-generated checks that automatically validate data based on detected patterns or logic. |
|  |  | **Authored** | Displays user-created checks, allowing the user to focus on custom validations tailored to specific requirements. |
| **2** | **Asserted State** | **All** | Displays all checks, regardless of their asserted status. This provides a full overview of both passed, failed, and not asserted checks. |
|  |  | **Passed** | Shows checks that have been asserted successfully, meaning no active anomalies were found during the validation process. |
|  |  | **Failed** | Displays checks that have failed assertion, indicating active anomalies or issues that need attention. |
|  |  | **Not Asserted** | Filters out checks that have not yet been asserted, either because they haven’t been processed or validated yet. |
| **3** | **Rule** | **N/A** | Select this to filter the checks based on specific rule type for data validation, such as checking non-null values, matching patterns, comparing numerical ranges, or verifying date-time constraints. By clicking on the caret down button next to the Rule field, the available rule types will be dynamically populated based on the rule types present in the results.<br> <br>The rules displayed are based on the current dataset and provide more granular control over filtering. Each rule type will show a counter next to it, displaying the total number of occurrences for that rule in the dataset.<br> <br>For example, the rule type **After Date Time** is displayed with a total of **2** occurrences.|

![filter](../assets/checks/manage-checks/filters-light.png#only-light)
![filter](../assets/checks/manage-checks/filters-dark.png#only-dark)

|No     |     Filter  |   Filter Value  |  Description|
| :---- |  :----       |  :----         |  :----      |
| **4** | Tag | **N/A**| Tag Filter displays only the tags associated with the currently visible items, along with their color icon, name, type, and the number of matching records. Selecting one or more tags refines the list based on your selection. If no matching items are found, a No option found message is displayed.|
| **5** | **Table** | **N/A** | Filters checks by the table to which they are applied. |
| **6** | **Field** | **N/A** | Filters checks by the specific field/column name within a table. |
| **7** | **Template** | **N/A** | This filter allows users to view and apply predefined [check templates](../checks/checks-template.md). |
