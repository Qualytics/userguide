# Checks

Checks tab provides a quick overview of the various checks applied across different tables and fields in multiple source datastores. In Qualytics, checks act as rules applied to data tables and fields to ensure accuracy and maintain data integrity. You can filter and sort the checks based on your preferences, making it easy to see which checks are active, in draft, or archived. This section is designed to simplify the review of applied checks across datasets without focusing on data quality or performance.

Let’s get started 🚀

## Navigation

**Step 1:** Log in to your Qualytics account and click the **Explore** button on the left side panel of the interface.

![explore](../assets/explore/checks/explore-light.png#only-light)
![explore](../assets/explore/checks/explore-dark.png#only-dark)

**Step 2:** Click on the **"Checks"** from the Navigation Tab.

![check-tab](../assets/explore/checks/checks-tab-light.png#only-light)
![check-tab](../assets/explore/checks/checks-tab-dark.png#only-dark)

You will be navigated to the **Checks** tabs here and you'll see a list of all the checks that have been applied to various tables and fields across different source datastores.

## Categories Check

You can categorize your checks based on their status, such as Active, Draft, Archived (Invalid and Discarded), or All, according to your preference. This categorization offers a clear view of the data quality validation process, helping you manage checks efficiently and maintain data integrity.

### All

By selecting **All Checks**, you can view a comprehensive list of all the checks in the datastores, including both **active** and **draft** checks, allowing you to focus on the checks that are currently being managed or are in progress. However, archived checks are not displayed in this.

![all-check](../assets/explore/checks/all-tab-light.png#only-light)
![all-check](../assets/explore/checks/all-tab-dark.png#only-dark)

### Active 

By selecting **Active**, you can view checks that are currently applied and being enforced on the data. These operational checks are used to validate data quality in real-time, allowing you to monitor all active checks and their performance.

![active-check](../assets/explore/checks/active-tab-light.png#only-light)
![active-check](../assets/explore/checks/active-tab-dark.png#only-dark)

You can also categorize the active checks based on their importance, favorites, or specific metrics to streamline your data quality monitoring.

**1. Important:** Shows only checks that are marked as important. These checks are prioritized based on their significance, typically assigned a weight of 7 or higher.

!!! note 
    Important checks are prioritized based on a weight of 7 or higher.

![important](../assets/explore/checks/important-light-5.png#only-light)
![important](../assets/explore/checks/important-dark-5.png#only-dark)

**2. Favorite:** Displays checks that have been marked as favorites. This allows you to quickly access checks that you use or monitor frequently. 

![favorite](../assets/explore/checks/favorite-light-6.png#only-light)
![favorite](../assets/explore/checks/favorite-dark-6.png#only-dark)

**3. All:** Displays a comprehensive view of all active checks, including important, favorite and any checks that do not fall under these specific categories. 

![all](../assets/explore/checks/all-light-8.png#only-light)
![all](../assets/explore/checks/all-dark-8.png#only-dark)

### Draft Checks

By selecting **Draft**, you can view checks that have been created but have not yet been applied to the data. These checks are in the drafting stage, allowing for adjustments and reviews before activation. Draft checks provide flexibility to experiment with different validation rules without affecting the actual data.

![draft-tab](../assets/explore/checks/draft-tab-light.png#only-light)
![draft-tab](../assets/explore/checks/draft-tab-dark.png#only-dark)

You can also categorize the draft checks based on their importance, favorites, or specific metrics to prioritize and organize them effectively during the review and adjustment process.

**1. Important:** Shows only checks that are marked as important. These checks are prioritized based on their significance, typically assigned a weight of 7 or higher.

![important](../assets/explore/checks/important-light-10.png#only-light)
![important](../assets/explore/checks/important-dark-10.png#only-dark)

**2 Favorite:** Displays checks that have been marked as favorites. This allows you to quickly access checks that you use or monitor frequently.  

![favorite](../assets/explore/checks/favorite-light-11.png#only-light)
![favorite](../assets/explore/checks/favorite-dark-11.png#only-dark)

**3. All:** Displays a comprehensive view of all draft checks, including important, favorite and any checks that do not fall under these specific categories.

![all](../assets/explore/checks/all-light-13.png#only-light)
![all](../assets/explore/checks/all-dark-13.png#only-dark)

### Archived Checks

By selecting **Archived**, you can view checks that have been marked as discarded or invalid from use but are still stored for future reference or restoration. Although these checks are no longer active, they can be restored if needed.

![archived-check](../assets/explore/checks/archived-tab-light.png#only-light)
![archived-check](../assets/explore/checks/archived-tab-dark.png#only-dark)

You can also categorize the archived checks based on their status as **Discarded**, **Invalid**, or view **All** archived checks to manage and review them effectively.

**1. Discarded**: Shows checks that have been marked as no longer useful or relevant and have been discarded from use.

![discarded](../assets/explore/checks/discarded-light-15.png#only-light)
![discarded](../assets/explore/checks/discarded-dark-15.png#only-dark)

**2. Invalid**: Displays checks that are deemed invalid due to errors or misconfigurations, requiring review or deletion.

![invalid](../assets/explore/checks/invalid-light-16.png#only-light)
![invalid](../assets/explore/checks/invalid-dark-16.png#only-dark)

**3. All**: Provides a view of all archive checks within this category including discarded and invalid checks.

![all](../assets/explore/checks/all-light-17.png#only-light)
![all](../assets/explore/checks/all-dark-17.png#only-dark)

## Details

Check Details provides important information about each check in the system. It shows when a check was last run, how often it has been used, when it was last updated, who made changes to it, and when it was created. This section helps users understand the status and history of the check, making it easier to manage and track its use over time. 

**Step 1:** Locate the check you want to review, then hover over the info icon to view the Check Details.

![check-detail](../assets/explore/checks/check-detail-light.png#only-light)
![check-detail](../assets/explore/checks/check-detail-dark.png#only-dark)

A popup will appear with additional details about the check.

![popup](../assets/explore/checks/popup-light-17.png#only-light)
![popup](../assets/explore/checks/popup-dark-17.png#only-dark)

### Last Asserted
Last Asserted At shows the most recent time the check was run, indicating when the last validation occurred. For example, the check was last asserted on **Mar 27, 2025, at 2:16 AM (GMT+5:30).**

![popup](../assets/explore/checks/asserted-light-17.png#only-light)
![popup](../assets/explore/checks/asserted-dark-17.png#only-dark)

### Scans
Scans show how many times the check has been used in different operations. It helps you track how often the check has been applied. For example, the check was used in **17 operations.**

![scan](../assets/explore/checks/scan-light-17.png#only-light)
![scan](../assets/explore/checks/scan-dark-17.png#only-dark)

### Updated At
Updated At shows the most recent time the check was modified or updated. It helps you see when any changes were made to the check’s configuration or settings. For example, the check was last updated on **Nov 8, 2024, at 6:37 PM (GMT+5:30).**

![update](../assets/explore/checks/update-light-17.png#only-light)
![update](../assets/explore/checks/update-dark-17.png#only-dark)

### Last Editor
Last Editor indicates who most recently made changes to the check. It helps track who is responsible for the latest updates or modifications. This is useful for accountability and collaboration within teams.

![editor](../assets/explore/checks/editor-light-17.png#only-light)
![editor](../assets/explore/checks/editor-dark-17.png#only-dark)

### Created At
Created At shows when the check was first made. It helps you know how long the check has been in use. This is useful for tracking its history. For example, the check was created on **Oct 17, 2024, at 11:13 AM (GMT+5:30).**

![created](../assets/explore/checks/created-light-17.png#only-light)
![created](../assets/explore/checks/created-dark-17.png#only-dark)

## Status Management of Checks

### Set Check as Draft

You can move an active check into a draft state, allowing you to work on the check, make adjustments, and refine the validation rules without affecting live data. This is useful when you need to temporarily deactivate a check for review and updates.

**Step 1:** Click on the active check that you want to move to the draft state.

![draft](../assets/explore/checks/draft-check-light.png#only-light)
![draft](../assets/explore/checks/draft-check-dark.png#only-dark)

**Step 2**: A modal window will appear displaying the check details. Click on the **vertical ellipsis (⋮)** located in the upper-right corner of the modal window, and select **"Draft"** from the drop-down menu.

![draft](../assets/explore/checks/draft-light-19.png#only-light)
![draft](../assets/explore/checks/draft-dark-19.png#only-dark)

**Step 3:** After clicking on **"Draft"**, the check will be successfully moved to the draft state, and a success flash message will appear stating, **"The checks have been successfully updated."**

![success-updated](../assets/explore/checks/success-updated-light-20.png#only-light)
![success-updated](../assets/explore/checks/success-updated-dark-20.png#only-dark)

### Activate Draft Check

You can activate the draft checks after when you have worked on the check, make adjustments, and refine the validation rules. By activating the draft check and making it live, ensures that the defined criteria are enforced on the data. 

**Step 1:** Navigate to the Draft check section, and click on the drafted check that you want to activate, whether you have made changes or wish to activate it as is.

![activate](../assets/explore/checks/activate-light.png#only-light)
![activate](../assets/explore/checks/activate-dark.png#only-dark)

A modal window will appear with the check details. If you want to make any changes to the [check details](https://userguide.qualytics.io/checks/checks-template/#:~:text=Enter%20the%20following%20details%20to%20add%20the%20check%20template%3A), you can edit them.

![check-details](../assets/explore/checks/check-details-light-27.png#only-light)
![check-details](../assets/explore/checks/check-details-dark-27.png#only-dark)

**Step 2:** Click on the **down arrow** icon with the **Update** button. A dropdown menu will appear, click on the **Activate** button.  

![activate](../assets/explore/checks/activate-light-28.png#only-light)
![activate](../assets/explore/checks/activate-dark-28.png#only-dark)

**Step 3:** After clicking on the activate button, your check is now successfully moved to the active checks and a success flash message will appear stating **"Check successfully updated"**.

![success-updated](../assets/explore/checks/success-updated-light-29.png#only-light)
![success-updated](../assets/explore/checks/success-updated-dark-29.png#only-dark)

### Set Check as Archived 

You can move an active or draft check into the archive when it is no longer relevant but may still be needed for historical purposes or future use. Archiving helps keep your checks organized without permanently deleting them.

**Step 1**: Click on the check from the list of available (whether Active or Draft) checks that you want to archive.

![archived](../assets/explore/checks/archived-checks-light.png#only-light)
![archived](../assets/explore/checks/archived-checks-dark.png#only-dark)

**Step 2:** A modal window will appear displaying the check details. Click on the **vertical ellipsis** **(⋮)** located in the upper-right corner of the modal window, and click on the **"Archive"** from the drop-down menu. 

![archive](../assets/explore/checks/archive-light-35.png#only-light)
![archive](../assets/explore/checks/archive-dark-35.png#only-dark)

**Step 3:** A modal window titled **“Archive Check”** will appear, providing you with the following archive options:

* **Discarded**: Select this option if the check is no longer relevant or suitable for the current business rules or data requirements. This helps in archiving checks that are obsolete but still exist for historical reference.

* **Invalid**: Choose this option if the check is not valid and should be retired from future inference. This helps the system learn from invalid checks and improves its ability to infer valid checks in the future.

![archive-check](../assets/explore/checks/archive-check-light-36.png#only-light)
![archive-check](../assets/explore/checks/archive-check-dark-36.png#only-dark)

**Step 4:** Once you've made your selection, click the **Archive** button to proceed.

![archive](../assets/explore/checks/archive-light-37.png#only-light)
![archive](../assets/explore/checks/archive-dark-37.png#only-dark)

**Step 5:** After clicking on the **Archive** button your check is moved to the archive and a flash message will appear saying **"The Check has been successfully archived"**.

![success-archive](../assets/explore/checks/success-archive-light-38.png#only-light)
![success-archive](../assets/explore/checks/success-archive-dark-38.png#only-dark)

### Restore Archived Checks 

If a check has been archived, then you can restore it back to an active state or in a draft state. This allows you to reuse your checks that were previously archived without having to recreate them from scratch.

**Step 1:** Click on **Archived** from the **navigation bar** in the **Checks** section to view all archived checks.

![restore](../assets/explore/checks/restore-light.png#only-light)
![restore](../assets/explore/checks/restore-dark.png#only-dark)

**Step 2**: Click on the archived check which you want to restore as an active or draft check.

For Demonstration purpose, we have selected the **"Metric"** check.

![archive-checks](../assets/explore/checks/archive-checks-light-46.png#only-light)
![archive-checks](../assets/explore/checks/archive-checks-dark-46.png#only-dark)

A modal window will appear with the check details.

![check-details](../assets/explore/checks/check-details-light-47.png#only-light)
![check-details](../assets/explore/checks/check-details-dark-47.png#only-dark)

**Step 3**: If you want to make any changes to the check, you can edit it. Otherwise, click on the **Restore** button to restore it as an active check.

![restore-check](../assets/explore/checks/restore-check-light-48.png#only-light)
![restore-check](../assets/explore/checks/restore-check-dark-48.png#only-dark)

To restore the check as a draft, click on the arrow icon next to the **Restore** button. A dropdown menu will appear—select **Restore as Draft** from the options.

![restore-as-draft](../assets/explore/checks/restore-as-draft-light-49.png#only-light)
![restore-as-draft](../assets/explore/checks/restore-as-draft-dark-49.png#only-dark)

After clicking the **Restore** button, the check will be successfully restored as either an active or draft check, depending on your selection. A success message will appear confirming, **"Check successfully updated."**

![success-updated](../assets/explore/checks/success-updated-light-50.png#only-light)
![success-updated](../assets/explore/checks/success-updated-dark-50.png#only-dark)

### Edit Check

You can edit an existing check to modify its properties, such as the rule type, coverage, filter clause, or description. Updating a check ensures that it stays aligned with evolving data requirements and maintains data quality as conditions change.

**Step 1:** Click on the check you want to edit, whether it is an active or draft check.

![edit-check](../assets/explore/checks/edit-checks-light.png#only-light)
![edit-check](../assets/explore/checks/edit-checks-dark.png#only-dark)

A modal window will appear with the check details. 

![modal-win](../assets/explore/checks/modal-win-light-52.png#only-light)
![modal-win](../assets/explore/checks/modal-win-dark-52.png#only-dark)

**Step 2:** Modify the [check details](https://userguide.qualytics.io/checks/checks-template/#:~:text=Enter%20the%20following%20details%20to%20add%20the%20check%20template%3A) as needed based on your preferences.

![check-detail](../assets/explore/checks/check-detail-light-53.png#only-light)
![check-detail](../assets/explore/checks/check-detail-dark-53.png#only-dark)

**Step 3:** Once you have edited the check details, then click on the **Validate** button. This will perform a validation operation on the check without saving it. The validation allows you to verify that the logic and parameters defined for the check are correct.

![validate-btn](../assets/explore/checks/validate-btn-light-54.png#only-light)
![validate-btn](../assets/explore/checks/validate-btn-dark-54.png#only-dark)

If the validation is successful, a green message saying **"Validation Successful"** will appear. 

![validate-msg](../assets/explore/checks/validate-msg-light-55.png#only-light)
![validate-msg](../assets/explore/checks/validate-msg-dark-55.png#only-dark)

If the validation fails, a red message saying **"Failed Validation"** will appear. This typically occurs when the check logic or parameters do not match the data properly.

![failed-msg](../assets/explore/checks/failed-msg-light-56.png#only-light)
![failed-msg](../assets/explore/checks/failed-msg-dark-56.png#only-dark)

**Step 3:** Once you have a successful validation, click the **"Update"** button. The system will update the changes you've made to the check, including changes to the fields, filter clause, coverage, description, tags, or metadata.

![update-btn](../assets/explore/checks/update-btn-light-57.png#only-light)
![update-btn](../assets/explore/checks/update-btn-dark-57.png#only-dark)

After clicking on the Update button, your check is successfully updated and a success flash message will appear stating **"Check successfully updated"**.

![update-msg](../assets/explore/checks/update-msg-light-58.png#only-light)
![update-msg](../assets/explore/checks/update-msg-dark-58.png#only-dark)

### Mark Check as Favorite

Marking a check as a favorite allows you to quickly access and prioritize the checks that are most important to your data validation process. This helps streamline workflows by keeping frequently used or critical checks easily accessible, ensuring you can monitor and manage them efficiently. By marking a check as a favorite, it will appear in the "Favorite" category for faster retrieval and management.

**Step 1:** Locate the check which you want to mark as a favorite and click on the bookmark icon located on the right side of the check.

![favorite](../assets/explore/checks/favorite-light.png#only-light)
![favorite](../assets/explore/checks/favorite-dark.png#only-dark)

After Clicking on the bookmark icon your check is successfully marked as a favorite and a success flash message will appear stating **"Check has been favorited"**.

![fav-msg](../assets/explore/checks/fav-msg-light-76.png#only-light)
![fav-msg](../assets/explore/checks/fav-msg-dark-76.png#only-dark)

To unmark a check, simply click on the bookmark icon of the marked check.

![remove-fav](../assets/explore/checks/remove-fav-light-77.png#only-light)
![remove-fav](../assets/explore/checks/remove-fav-dark-77.png#only-dark)

This will remove it from your favorites.A success flash message will appear stating **"The Check has been unfavorited"**.

![successfully-unfav](../assets/explore/checks/successfully-unfav-light.png#only-light)
![successfully-unfav](../assets/explore/checks/successfully-unfav-dark.png#only-dark)

## Clone Check

You can clone both active and draft checks to create a duplicate copy of an existing check. This is useful when you want to create a new check based on the structure of an existing one, allowing you to make adjustments without affecting the original check.

**Step 1**: Click on the check (whether Active or Draft) that you want to clone.

![clone](../assets/explore/checks/clone-checks-light.png#only-light)
![clone](../assets/explore/checks/clone-checks-dark.png#only-dark)

**Step 2**: A modal window will appear displaying the check details. Click on the **vertical ellipsis (⋮)** located in the upper-right corner of the modal window, and select **"Clone"** from the drop-down menu.

![clone-btn](../assets/explore/checks/clone-btn-light-79.png#only-light)
![clone-btn](../assets/explore/checks/clone-btn-dark-79.png#only-dark)

**Step 3:** After clicking the Clone button, a modal window will appear. This window allows you to adjust the cloned check's details.

![modal-window](../assets/explore/checks/modal-window-light-80.png#only-light)
![modal-window](../assets/explore/checks/modal-window-dark-80.png#only-dark)

**1.** If you toggle on the **"Associate with a Check Template"** option, the cloned check will be linked to a specific template.

![toggle-on](../assets/explore/checks/toggle-on-light-81.png#only-light)
![toggle-on](../assets/explore/checks/toggle-on-dark-81.png#only-dark)

Choose a **Template** from the dropdown menu that you want to associate with the cloned check. The check will inherit properties from the selected template.

* **Locked:** The check will automatically sync with any future updates made to the template, but you won't be able to modify the check's properties directly.

* **Unlocked:** You can modify the check, but future updates to the template will no longer affect this check.

![associate-check](../assets/explore/checks/associate-check-light-82.png#only-light)
![associate-check](../assets/explore/checks/associate-check-dark-82.png#only-dark)

**2.** If you toggle off the **"Associate with a Check Template"** option, the cloned check will not be linked to any template, which allows you full control to modify the properties independently.

![toggle-off](../assets/explore/checks/toggle-off-light-83.png#only-light)
![toggle-off](../assets/explore/checks/toggle-off-dark-83.png#only-dark)

Select the appropriate **Rule type** for the check from the dropdown menu.

![rule-type](../assets/explore/checks/rule-type-light-84.png#only-light)
![rule-type](../assets/explore/checks/rule-type-dark-84.png#only-dark)

**Step 4:** Once you have selected the template or rule type, fill up the remaining [check details](https://userguide.qualytics.io/checks/checks-template/#:~:text=Enter%20the%20following%20details%20to%20add%20the%20check%20template%3A) as required. 

![check-detail](../assets/explore/checks/check-detail-light-85.png#only-light)
![check-detail](../assets/explore/checks/check-detail-dark-85.png#only-dark)

**Step 5:** After completing all the check details, click on the **"Validate"** button. This will perform a validation operation on the check without saving it. The validation allows you to verify that the logic and parameters defined for the check are correct. It ensures that the check will work as expected by running it against the data without committing any changes.

![validate-btn](../assets/explore/checks/validate-btn-light-86.png#only-light)
![validate-btn](../assets/explore/checks/validate-btn-dark-86.png#only-dark)

If the validation is successful, a green message saying **"Validation Successful"** will appear. 

![validation-success](../assets/explore/checks/validation-success-light-87.png#only-light)
![validation-success](../assets/explore/checks/validation-success-dark-87.png#only-dark)

If the validation fails, a red message saying **"Failed Validation"** will appear. This typically occurs when the check logic or parameters do not match the data properly.

![failed-validation](../assets/explore/checks/failed-validation-light-88.png#only-light)
![failed-validation](../assets/explore/checks/failed-validation-dark-88.png#only-dark)

**Step 6:** Once you have a successful validation, click the **"Save"** button. The system will save any modifications you've made to the check, and create a clone of that check on basis of your changes.  

![save-btn](../assets/explore/checks/save-btn-light-89.png#only-light)
![save-btn](../assets/explore/checks/save-btn-dark-89.png#only-dark)

After clicking on the **"Save"** button your check is successfully created and a success flash message will appear stating **"Check successfully created".**

![success-msgs](../assets/explore/checks/success-msgs-light-90.png#only-light)
![success-msgs](../assets/explore/checks/success-msgs-dark-90.png#only-dark)

## Create a Quality Check template

You can add checks as a Template, which allows you to create a reusable framework for quality checks. By using templates, you standardize the validation process, enabling the creation of multiple checks with similar rules and criteria across different datastores. This ensures consistency and efficiency in managing data quality checks.

**Step 1:** Locate the check (whether Active or Draft) you want to archive and click on that check.

![quality-check](../assets/explore/checks/quality-checks-light.png#only-light)
![quality-check](../assets/explore/checks/quality-checks-dark.png#only-dark)

**Step 2:** A modal window will appear displaying the check details. Click on the **vertical ellipsis (⋮)** located in the upper-right corner of the modal window, and select **"Template"** from the drop-down menu.

![template-btn](../assets/explore/checks/template-btn-light-92.png#only-light)
![template-btn](../assets/explore/checks/template-btn-dark-92.png#only-dark)

After clicking the **"Template"** button, the check will be saved and created as a template in the library, and a success flash message will appear stating, **"The quality check template has been successfully created."** This allows you to reuse the template for future checks, streamlining the validation process.

![quality-check](../assets/explore/checks/quality-check-light-93.png#only-light)
![quality-check](../assets/explore/checks/quality-check-dark-93.png#only-dark)

## Filter and Sort

Filter and Sort options allow you to organize your checks by various criteria, such as Weight, Anomalies, Coverage, Created Date, and Rules. You can also apply filters to refine your list of checks based on Selected Source Datastores, Check Type, Asserted State (Passed, Failed, Not Asserted), Tags, Files, and Fields.

### Sort

You can sort your checks by **Active Anomalies**, **Coverage**, **Created Date**, **Last Asserted**, **Rules**, and **Weight** to easily organize and prioritize them according to your needs.

![sort](../assets/explore/checks/sort-light.png#only-light)
![sort](../assets/explore/checks/sort-dark.png#only-dark)

| No  | Sort By Option | Description |
| :---- | :---- | :---- |
| **1** | **Active Anomalies** | Sort checks based on the number of active anomalies. |
| **2** | **Coverage** | Sort checks by data coverage percentage. |
| **3** | **Created Date** | Sort checks according to the date they were created. |
| **4** | **Last Asserted** | Sorts by the last time the check was executed. |
| **5** | **Rules** | Sort checks based on specific rules applied to the checks. |
| **6** | **Weight** | Sort checks by their assigned weight or importance level. |

Whatever sorting option is selected, you can arrange the data either in ascending or descending order by clicking the caret button next to the selected sorting criteria.

![caret](../assets/explore/checks/caret-light.png#only-light)
![caret](../assets/explore/checks/caret-dark.png#only-dark)

### Filter

You can filter your checks based on values like **Source Datastores Check Type**, **Asserted State**, **Rule**, **Tags**, **File**, **Field**, and **Template**.

![filter](../assets/explore/checks/filter-light.png#only-light)
![filter](../assets/explore/checks/filter-dark.png#only-dark)

| No | Filter | Filter Value | Description |
| :---- | :---- | :---- | :---- |
| **1** | **Selected Source Datastores** | **N/A** | Select specific source datastores to focus on their checks. |
| **2** | **Select Tags** | **N/A** | Filter checks by specific tags to categorize and refine results. |

![filter](../assets/explore/checks/filter2-light.png#only-light)
![filter](../assets/explore/checks/filter2-dark.png#only-dark)

|No     |     Filter  |   Filter Value  |  Description|
| :---- |  :----       |  :----         |  :----      |
| **3** | **Check Type** | **All** | Displays all types of checks, both [inferred](../checks/inferred-check.md) and [authored](../checks/authored-check.md). |
|  |  | **Inferred** | Shows system-generated checks that automatically validate data based on detected patterns or logic. |
|  |  | **Authored** | Displays user-created checks, allowing the user to focus on custom validations tailored to specific requirements. |
| **4** | **Asserted State** | **All** | Displays all checks, regardless of their asserted status. This provides a full overview of both passed, failed, and not asserted checks. |
|  |  | **Passed** | Shows checks that have been asserted successfully, meaning no active anomalies were found during the validation process. |
|  |  | **Failed** | Displays checks that have failed assertion, indicating active anomalies or issues that need attention. |
|  |  | **Not Asserted** | Filters out checks that have not yet been asserted, either because they haven’t been processed or validated yet. |
| **5** | **Rule** | **N/A** | Select this to filter the checks based on specific rule type for data validation, such as checking non-null values, matching patterns, comparing numerical ranges, or verifying date-time constraints. By clicking on the caret down button next to the Rule field, the available rule types will be dynamically populated based on the rule types present in the results.<br> <br>The rules displayed are based on the current dataset and provide more granular control over filtering. Each rule type will show a counter next to it, displaying the total number of occurrences for that rule in the dataset.<br> <br>For example, the rule type **After Date Time** is displayed with a total of **46** occurrences.|
| **6** | **Template** | **N/A** | This filter allows users to view and apply predefined [check templates](../checks/checks-template.md). |