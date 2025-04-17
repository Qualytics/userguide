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

For more details on Active Checks, please refer to the [**Active Checks**](../checks/manage-checks.md/#active) section in the documentation.

### Draft Checks

By selecting **Draft**, you can view checks that have been created but have not yet been applied to the data. These checks are in the drafting stage, allowing for adjustments and reviews before activation. Draft checks provide flexibility to experiment with different validation rules without affecting the actual data.

![draft-tab](../assets/explore/checks/draft-tab-light.png#only-light)
![draft-tab](../assets/explore/checks/draft-tab-dark.png#only-dark)

You can also categorize the draft checks based on their importance, favorites, or specific metrics to prioritize and organize them effectively during the review and adjustment process.

For more details on Draft Checks, please refer to the [**Draft Checks**](../checks/manage-checks.md/#draft-checks) section in the documentation.

### Archived Checks

By selecting **Archived**, you can view checks that have been marked as discarded or invalid from use but are still stored for future reference or restoration. Although these checks are no longer active, they can be restored if needed.

![archived-check](../assets/explore/checks/archived-tab-light.png#only-light)
![archived-check](../assets/explore/checks/archived-tab-dark.png#only-dark)

You can also categorize the archived checks based on their status as **Discarded**, **Invalid**, or view **All** archived checks to manage and review them effectively.

For more details on Archived Checks, please refer to the [**Archived Checks**](../checks/manage-checks.md/#archived-checks) section in the documentation.

## Check Details

Check Details provides important information about each check in the system. It shows when a check was last run, how often it has been used, when it was last updated, who made changes to it, and when it was created. This section helps users understand the status and history of the check, making it easier to manage and track its use over time. 

**Step 1:** Locate the check you want to review, then hover over the info icon to view the Check Details.

![check-detail](../assets/explore/checks/check-detail-light.png#only-light)
![check-detail](../assets/explore/checks/check-detail-dark.png#only-dark)

For more steps and further information, please refer to the [**Check Details**](../checks/manage-checks.md/#check-details) section in the documentation.

## Status Management of Checks

### Set Check as Draft

You can move an active check into a draft state, allowing you to work on the check, make adjustments, and refine the validation rules without affecting live data. This is useful when you need to temporarily deactivate a check for review and updates.

**Step 1:** Click on the active check that you want to move to the draft state.

![draft](../assets/explore/checks/draft-check-light.png#only-light)
![draft](../assets/explore/checks/draft-check-dark.png#only-dark)

To understand how to draft checks, you can follow the remaining steps from the documentation [**Draft Specific Check.**](../checks/manage-checks.md/#method-i-draft-specific-check)

### Activate Draft Check

You can activate the draft checks after when you have worked on the check, make adjustments, and refine the validation rules. By activating the draft check and making it live, ensures that the defined criteria are enforced on the data. 

**Step 1:** Navigate to the Draft check section, and click on the drafted check that you want to activate, whether you have made changes or wish to activate it as is.

![activate](../assets/explore/checks/activate-light.png#only-light)
![activate](../assets/explore/checks/activate-dark.png#only-dark)

To understand how to activate draft checks, you can follow the remaining steps from the documentation [**Activate Draft Checks.**](../checks/manage-checks.md/#activate-draft-check)

### Set Check as Archived 

You can move an active or draft check into the archive when it is no longer relevant but may still be needed for historical purposes or future use. Archiving helps keep your checks organized without permanently deleting them.

**Step 1**: Click on the check from the list of available (whether Active or Draft) checks that you want to archive.

For Demonstration purposes, we have selected the **"Metric"** check.

![archived](../assets/explore/checks/archived-checks-light.png#only-light)
![archived](../assets/explore/checks/archived-checks-dark.png#only-dark)

To understand how to set check as archived, you can follow the remaining steps from the documentation [**Set Check As Archived.**](../checks/manage-checks.md/#2-archive-from-action-menu)

### Restore Archived Checks 

If a check has been archived, then you can restore it back to an active state or in a draft state. This allows you to reuse your checks that were previously archived without having to recreate them from scratch.

**Step 1:** Click on **Archived** from the **navigation bar** in the **Checks** section to view all archived checks.

![restore](../assets/explore/checks/restore-light.png#only-light)
![restore](../assets/explore/checks/restore-dark.png#only-dark)

To understand how to restore archived checks, you can follow the remaining steps from the documentation [**Restore Archived Checks.**](../checks/manage-checks.md/#restore-archived-checks)

### Edit Check

You can edit an existing check to modify its properties, such as the rule type, coverage, filter clause, or description. Updating a check ensures that it stays aligned with evolving data requirements and maintains data quality as conditions change.

**Step 1:** Click on the check you want to edit, whether it is an active or draft check.

For Demonstration purposes, we have selected the **"Metric"** check.

![edit-check](../assets/explore/checks/edit-checks-light.png#only-light)
![edit-check](../assets/explore/checks/edit-checks-dark.png#only-dark)

To understand how to edit checks, you can follow the remaining steps from the [**Edit Checks**](../checks/manage-checks.md/#edit-check) section in the documentation.

### Mark Check as Favorite

Marking a check as a favorite allows you to quickly access and prioritize the checks that are most important to your data validation process. This helps streamline workflows by keeping frequently used or critical checks easily accessible, ensuring you can monitor and manage them efficiently. By marking a check as a favorite, it will appear in the "Favorite" category for faster retrieval and management.

**Step 1:** Locate the check which you want to mark as a favorite and click on the bookmark icon located on the right side of the check.

![favorite](../assets/explore/checks/favorite-light.png#only-light)
![favorite](../assets/explore/checks/favorite-dark.png#only-dark)

To understand how to mark check as favorite, you can follow the remaining steps from the [**Mark Check as Favorite**](../checks/manage-checks.md/#mark-check-as-favorite) section in the documentation.

## Clone Check

You can clone both active and draft checks to create a duplicate copy of an existing check. This is useful when you want to create a new check based on the structure of an existing one, allowing you to make adjustments without affecting the original check.

**Step 1**: Click on the check (whether Active or Draft) that you want to clone.

For Demonstration purposes, we have selected the **"Metric"** check.

![clone](../assets/explore/checks/clone-checks-light.png#only-light)
![clone](../assets/explore/checks/clone-checks-dark.png#only-dark)

To understand how to clone check, you can follow the remaining steps from the [**Clone Check**](../checks/manage-checks.md/#clone-check) section in the documentation.

## Create a Quality Check template

You can add checks as a Template, which allows you to create a reusable framework for quality checks. By using templates, you standardize the validation process, enabling the creation of multiple checks with similar rules and criteria across different datastores. This ensures consistency and efficiency in managing data quality checks.

**Step 1:** Locate the check (whether Active or Draft) you want to archive and click on that check.

![quality-check](../assets/explore/checks/quality-checks-light.png#only-light)
![quality-check](../assets/explore/checks/quality-checks-dark.png#only-dark)

To understand how to create a quality check template, you can follow the remaining steps from the [**Quality Check Template**](../checks/manage-checks.md/#create-a-quality-check-template) section in the documentation.

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




