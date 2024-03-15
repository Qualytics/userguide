---
hide:
  - navigation
---

## Release Notes

### 2024.03.15 { id=2024.03.15}

#### Feature Enhancements

- Enhanced Observability
    - Automated daily volumetric measurements for all tables and file patterns
    - Time-series capture and visualizations for volume, freshness, and identified anomalies
- Overview Tab:
    - Introduced a new "Overview" tab with information related to monitoring at the datastore and container level.
    - This dashboard interface is designed for monitoring and managing data related to qualytics for datastore and containers.
    - Users can see:
        - Totals: Quality Score, Tables, Records, Checks and Anomalies
        - Total of Quality Checks grouped by Rule type
        - Data Volume Over Time: A line graph that shows the total amount of data associated with the project over time.
        - Anomalies Over Time: A line graph that shows the number of anomalies detected in the project over time.

- Datastore Field List Update:
    - The datastore field profiles list has been updated to match the existing list views design.
    - All card-listed pages now display information in a column format, conditionally using scrolling for smaller and larger screens.
    - Now the field details will show on a modal with Profiling and Histogram

- Heatmap Simplification:
    - Simplified the heatmap to consider only operations counted.

- Datastore Metrics:
    - Improved distinction between 0 and null values in the datastore metrics (total records, total fields, etc).

- Explore Page Update:
    - Added new metrics to the Explore page.
    - We are now adding data volume over time (records and size).
    - Improved distinction between 0 and null values in metrics (total records, total fields, etc).

#### General Fixes

- UI Wording and Display for Cataloged vs Profiled Fields:
    - Addressed user confusion surrounding the display and wording used to differentiate between fields that have been cataloged versus those that have been profiled.
    - Updated the messaging within the tree view and other relevant UI components to accurately reflect the state of fields post-catalog operation.
    - Implemented a clear distinction between non-profiled and profiled fields in the field count indicators.
    - Conducted a thorough review of the CTAs and descriptive text surrounding the Catalog, Profile, and Scan operations to improve clarity and user understanding.

- General fixes and improvements

### 2024.03.07 { id=2024.03.07}

- Corrected MatchesPattern Checks Inference:
    - Fixed an issue where the inference engine generated MatchesPattern checks that erroneously asserted false on more than 10% of training data. This resolution ensures all inferred checks now meet the 99% coverage criterion, aligning accurately with their training datasets.

- Fixed Multi-Field Check Parsing Error in DFS:
    - Addressed a bug in DFS environments that caused parsing errors for checks asserting against multiple fields, such as AnyNotNull and NotNull, when selected fields contained white spaces. This resolution ensures that checks involving multiple fields with spaces are now accurately parsed and executed.

- Volumetric Measurements Tracking Fix:
    - Addressed a bug that prevented the recording of volumetric measurements for containers without a last modified time. This fix corrects the problem by treating last_modification_time as nullable, ensuring that containers are now accurately tracked for volumetric measurements regardless of their modification date status.

- General fixes and improvements

### 2024.03.05 { id=2024.03.05}

#### Feature Enhancements

- Check Validation Improvement:
    - Enhanced the validation process for the "Is Replica Of" check. Previously, the system did not validate the field name and type, potentially leading to undetected issues until a Scan Operation was executed. Now, the validation process includes checking the field name and type, providing users with immediate feedback on any issues.

#### General Fixes

- Matches Pattern Data Quality Check Handling White Space:
    - Resolved a bug in the Matches Pattern data quality check that caused white space to be ignored during training. With this fix, the system now accounts for white space during training, ensuring accurate pattern inference even with data containing significant white space. If 1% or more of the training data contains blanks, the system will derive a pattern that includes blanks as a valid value, improving data quality assessment.

- General fixes and improvements

### 2024.02.28 { id=2024.02.28 }

#### Feature Enhancements

- User Token Management:
    - Transitioned from Generic Tokens to a more robust User Token system accessible under Settings for all users. This enhancement includes features to list, create, revoke, and delete tokens, offering granular control of API access. User activities through the API are now attributable, aligning actions with user accounts for improved accountability and traceability.

#### General Fixes

- Datetime Validation in API Requests:
    - Strict validation of datetime entries in API requests has been implemented to require the Zulu datetime format. This update addresses and resolves issues where incomplete datetime entries could disrupt Scan operations, enhancing API reliability.

- Context-Aware Redirection Post-Operation:
    - Enhanced the operation modal redirect functionality to be context-sensitive, ensuring that users are directed to the appropriate activity tab after an operation, whether at the container or datastore level. This enhancement ensures a logical and intuitive post-operation navigation experience.

- Template Details Page Responsiveness:
    - Addressed layout issues on the Template Details page caused by long descriptions. Adjustments ensure that the description section now accommodates larger text volumes without disrupting the page layout, maintaining a clean and accessible interface.

- General fixes and improvements

### 2024.02.23 { id=2024.02.23 }

#### Feature Enhancements

- Introduction of Operations Management at the Table/File Level:
    - The Activity tab has been added at the table/file level, extending its previous implementation at the source datastore level. This update provides users with the ability to view detailed information on operations for individual tables/files, including scan metrics, and histories of operation runs and schedules. It enhances the user's ability to monitor and analyze operations at a granular level.

- Enhanced Breadcrumb Navigation UX:
    - Breadcrumb navigation has been improved for better user interaction. Users can now click on the breadcrumb representing their current context, enabling more intuitive navigation. In addition, selecting the Source Datastore breadcrumb takes users directly to the Activity tab, streamlining the flow of user interactions.

#### General Fixes

- Improved Accuracy in Profile and Scan Metrics:
    - Enhanced the accuracy of metrics for profiled and scanned operations by excluding failed containers from the count. Now, metrics accurately reflect only those containers that have been successfully processed.

- Streamlined input display for Aggregation Comparison rule in Check/Template forms:
    - Removed the "Coverage" input for the "Aggregation Comparison" rule in Check/Template Forms, as the rule does not support coverage customization. This simplification helps avoid confusion during rule configuration.

- Increased Backend Process Timeouts:
    - In response to frequent timeout issues, the backend process timeouts have been adjusted. This change aims to reduce interruptions and improve service reliability by ensuring that processes have sufficient time to complete.

- General fixes and improvements

### 2024.02.19 { id=2024.02.19 }

#### Feature Enhancements

- Support for exporting Check Templates to the Enrichment Datastore:
    - Added the ability to export Check Library metadata to the enrichment datastore. This feature helps users export their Check Library, making it easier to share and analyze check templates.

- File Upload Size Limit Handling:
    - Implemented a user-friendly error message for file uploads that exceed the 20MB limit. This enhancement aims to improve user experience by providing clear feedback when the file size limit is breached, replacing the generic error message previously displayed.

#### General Fixes

- Resolved Parsing Errors in Expected Values Rule:
    - Fixed an issue where single quotes in the list of expected values caused parsing errors in the Analytics Engine, preventing the Expected Values rule from asserting correctly. This correction ensures values, including those with quotes or special characters, are now accurately parsed and asserted.

- General fixes and improvements

### 2024.02.17 { id=2024.02.17}

#### General Fixes

- Corrected Typing for Expected Values Check:
    - Resolved an issue with the expectedValues rule, where numeric comparisons were inaccurately processed due to a misalignment between the API and the analytics engine. This fix ensures numeric values are correctly typed and compared, enhancing the reliability of validations.

- Fixed Anomaly Filtering in Scan Results dialog:
    - Addressed a flaw where scan results did not consistently filter anomalies based on the operation ID. The fix guarantees that anomalies are only displayed once the operation ID parameter is accurately defined in the URL, ensuring more precise and relevant scan outcome presentations.

- Check Validation Sampling Behavior Adjustment:
    - Fixed intermittent validation issues encountered in specific source datastore types (DB2, Microsoft SQL Server). The problem, where validation could unpredictably fail or succeed based on container size, was corrected by fine-tuning the sampling method for these technologies, leading to consistent validation performance.

- General fixes and improvements

### 2024.02.15 { id=2024.02.15}

#### Feature Enhancements

- UX Improvements for Profile and Scan Operation Dialogs:
    - Implemented significant UX enhancements to Profile & Scan Operation Dialogs for improved clarity and user flow. Key improvements include:
        - Visibility of incremental fields and their current starting positions in Scan Operation dialogs.
        - Logical reordering of Profile and Scan Operation steps to align with user workflows, including prioritizing container selection and clarifying the distinction between "Starting Threshold" and "Limit" settings.
    - Simplified operation initiation, allowing users to start operations directly before the final scheduling step, streamlining the process for immediate execution.

- Naming for Scheduled Operations:
    - Added a name field to scheduled operations, enabling users to assign descriptive names or aliases. This feature aids in distinguishing and managing multiple scheduled operations more effectively.

- Container Name Filters for Operations:
    - Provided filtering options for operations and scheduled operations by container name, improving the ability to quickly locate and manage specific operations.

- Improved Design for Field Identifiers in Tooltips:
    - The design of field identifiers within tooltips has been refined for greater clarity. Enhancements focus on displaying Grouping Fields, Excluded Fields, Incremental Fields, and Partition Fields, aiming to offer users a more intuitive experience.

#### General Fixes

- External Scan Rollup Threshold Correction:
    - Fixed an issue in external scans where the rollup threshold was not applied as intended. This correction ensures that anomalies exceeding the threshold are now accurately consolidated into a single shape anomaly, rather than being reported as multiple individual record anomalies.

- Repetitive Release Notification and Live Update Fixes:
    - Resolved a recurring issue with release notifications continually prompting users to refresh despite acknowledgment. Additionally, it restored the live update notifications' functionality, ensuring users are correctly alerted to new features while actively using the system, with suggestions for a hard refresh to access the latest version.

- Corrected Field Input Logic in Check & Template Forms:
    - Addressed a logic error that incorrectly disabled field inputs for certain rules in check and template forms. This correction re-enables the necessary field input, removing a significant barrier that previously prevented users from creating checks affected by this issue.

- Addressed Absence of Feedback for No-Match Field Filters on Explore Page:
    - Rectified the absence of feedback when field filters on the Explore Page yield no results, ensuring users receive a clear message indicating no items match the specified filter criteria.

- General fixes and improvements

### 2024.02.10 { id=2024.02.10}

#### Feature Enhancements

- Immediate Execution Option for Scheduled Operations:
    - Introduced a "Run Now" feature for scheduled operations, enabling users to execute operations immediately without waiting for the scheduled time. This addition provides flexibility in operation management, ensuring immediate execution as needed without altering the original schedule.

- Simplified Customization of Notification Messages:
    - Removed the "use custom message" toggle from the notification form, making the message input field always editable. This change simplifies the user interface and improves usability by allowing direct editing of notification messages.
    - Enhanced default messages for each notification trigger type have also been implemented to improve clarity.

- Performance Improvement in User Notifications Management:
    - Implemented infinite scrolling pagination for the user notifications side panel. This update addresses performance issues with loading large numbers of notifications, ensuring a smoother and more responsive experience for users with extensive notification histories.

- Enhanced Archive Template Confirmation:
    - Updated the archive dialog for templates to include information on the number of checks associated with archiving the template. This enhancement ensures users are aware of the impact of checks linked to the template, promoting informed decision-making.

- Improved Interaction with Computed Tables:
    - Refined the Containers list UX to allow navigation to container details immediately after the creation of a computed table, addressing delays caused by background profiling. This improvement ensures users can access computed table details without waiting for the profile operation to complete, drawing inspiration from Tree View functionality for a more seamless experience.

#### General Fixes

- General fixes and improvements

### 2024.02.02 { id=2024.02.02}

#### Feature Enhancements

- Excluded Fields Inclusion in Drop-downs:
    - Refined container settings to incorporate previously excluded fields in the dropdown list, enhancing user flexibility. In addition, a warning message has been added to notify users if a profile operation is required when deselecting excluded fields that were previously selected.

#### General Fixes

- Linkable Scan Results for Direct Access:
    - Made Scan Results dialogs accessible via direct URL links, addressing previous issues with broken anomaly notification links. This enhancement provides users with a straightforward path to detailed scan outcomes.

- Property Display Refinement for Various Field Types:
    - Corrected illogical property displays for specific field types like Date/Timestamp. The system now intelligently displays only properties relevant to the selected data type, eliminating inappropriate options. This update also includes renaming 'Declared Type' to 'Inferred Type' and adjusting the logic for accurate representation.

- Timezone Consistency in Insights and Activity Pages:
    - Implemented improvements in timezone handling across Insights and Activity pages. These changes ensure that date aggregations are accurately aligned with the user's local time, eliminating previous inconsistencies compared to the Operations list results.

- Fixed breadcrumb display in the datastore for members with restricted permissions
    - Enhanced the datastore interface to address issues faced by members with limited permissions. This update also fixes misleading breadcrumb displays and ensures that correct datastore enhancement information is visible.

- Resolved State Issue in Bulk Check Archive:
    - Addressed a bug in the bulk selection process for archiving checks. The fix corrects an issue where the system recognized individual selections instead of the intended group selection due to an overlooked edge case.

- Improved Operation Modal State Management:
    - Tackled state management inconsistencies in Operation Modals. Fixes include resetting the remediation strategy to its default and ensuring 'include' options do not carry over previous states erroneously.

- Eliminating Infinite Load for Non-Admin Enrichment Editing:
    - Solved a persistent loading issue in the Enrichment form for non-admin users. Updates ensure a smoother, error-free interaction for these users, improving accessibility and functionality.

- General fixes and improvements

### 2024.01.30 { id=2024.01.30}

#### Feature Enhancements

- Enhanced External Scan Operations:
    - Improved data handling in External Scans by applying type casting to uploaded data using Spark. This update is particularly significant for date-time fields, which now expect and conform to ISO 8601 standards.

- Optimized DFS File Reading:
    - Streamlined file reading in DFS by storing and utilizing the 'file_format' identified during the Catalog operation. This change eliminates the need for repeated format inspection on each read, significantly reducing overhead, especially for partitioned file types.

#### General Fixes

- Resolved DFS Reading Issues with Special Character Headers:
    - Fixed a DFS reading issue where columns with headers containing special characters (like pipes |) adversely affected field profiling, including inaccuracies in histogram generation.

- General fixes and improvements

### 2024.01.26 { id=2024.01.26}

#### Feature Enhancements

- Incremental Scan Starting Threshold:
    - Introduced a "Starting Threshold" option for incremental Scans. This feature allows users to manually set a starting value for the incremental field in large tables, bypassing the need to scan the entire dataset initially. It's handy for first-time scans of massive databases, facilitating more efficient and targeted data scanning.

- Add Support for Archiving Anomalies:
    - Implemented the capability of archiving anomalies. Users can now remove anomalies from view without permanently deleting them, providing greater control and flexibility in anomaly management.

- External Scan Operation for Ad hoc Processes:
    - Introduced 'External Scan Operation' as a new feature enabling ad hoc data validation for all containers. This operation allows users to validate ad hoc data, such as Excel or CSV files, against a container's existing checks and enrichment configuration. The provided file's structure must align with the container's schema, ensuring a seamless validation process.

#### General Fixes

- Preventing Unrelated Entity Selection in Check Form:
    - Fixed an issue in the Check Form where users could inadvertently select unrelated entities. Selecting datastores, containers, and fields is restricted during any ongoing data loading, preventing mismatched entity selections.

- Performance enhancements for BigQuery and Snowflake removing the need for count operations during full table analysis

- General fixes and improvements

### 2024.01.23 { id=2024.01.23}

#### Feature Enhancements

- Introduction of 'Expected Schema' Rule for Advanced Schema Validation:
    - Introduced the 'Expected Schema' rule, replacing the 'Required Fields' rule. This new rule asserts that all selected fields are present and their data types match predefined expectations, offering more comprehensive schema validation. It also includes an option to validate additional fields added to the schema, allowing users to specify whether the presence of new fields should cause the check to fail.

- Refined Tree Navigation Experience:
    - Updated the tree navigation to prevent automatic expansion of nodes upon selection and eliminated the auto-reset behavior when re-selecting an active node. These changes provide a smoother and more user-friendly navigation experience, especially in tables/files with numerous fields.

- Locked/Unlocked Status Filter in Library Page:
    - Added a new filter feature to the Library page, enabling users to categorize and view check templates based on their Locked or Unlocked status. This enhancement simplifies the management and selection of templates.

- Improved Messaging for Locked Template Properties in Check Form:
    - Enhanced the Check Form UX by adding informative messages explaining why certain inputs are disabled when a check is associated with a locked template. This update enhances user understanding and interaction with the form.

#### General Fixes

- Corrected Insights Metrics for Check Templates:
    - Fixed an issue where check templates were incorrectly counted as checks in related metrics and counts on the Insights page. Templates are now appropriately filtered out, ensuring accurate representation of check-related data.

- Enabled Template Creation with Calculated Rules:
    - Resolved a limitation that prevented the creation of templates using calculated rules like 'Satisfies Expression' and 'Aggregation Comparison'. This fix expands the capabilities and flexibility of template creation.

- General fixes and improvements

### 2024-01-11 { id=2024.01.11}

#### Feature Enhancements

- Introduction of Check Templates:
    - Implemented Check Templates to offer a balance between flexibility and consistency in quality check management. Checks can now be associated with templates in either a 'locked' or 'unlocked' state, allowing for synchronized properties or independent customization, respectively. This feature streamlines check management and enables efficient tracking and review of anomalies across all checks associated with a template.

- isType Rule Implementation:
    - Replaced the previous dataType rule with the new isType rule for improved accuracy and understanding. The isType rule is now specifically tailored to assert only against string fields, enhancing its applicability and effectiveness.

- Enhanced Container Details Page with Identifier Icons:
    - Updated the Container Details page to display icons for key container identifiers, including Partition Field, Grouping Fields, and Exclude Fields. This enhancement provides a more intuitive and informative user interface, facilitating easier identification and understanding of container characteristics.

#### General Fixes

- Notification System Reliability Improvement:
    - Fixed intermittent failures in the notifications system. Users will now receive reliable notifications for identified anomalies, ensuring timely awareness and response to data irregularities.

- Safeguard Against Overlapping Scheduled Operations:
    - Implemented a mechanism to prevent the overloading of deployments due to overlapping scheduled operations. If a scheduled operation doesn’t complete before its next scheduled run, the subsequent run will be skipped, thereby avoiding potential strain on system resources.

- Correction of Group-by Field Display in Containers:
    - Resolved an issue where selected grouping fields were not appearing in the list fields of a container. This fix ensures that user-specified fields for group-by operations are correctly displayed, maintaining the integrity of data organization and analysis.

- General fixes and improvements

### 2024.01.04 { id=2024.01.04}

#### Feature Enhancements

- Enhanced Warnings for Schema Inconsistencies in Files Profiled
    - Improved the warning message for cases where the user profiles files with different schemas under a single glob pattern. This update ensures users receive clear, helpful information when files within a glob have inconsistent structures.

#### General Fixes

- Containers with 'Group By' settings Leading to Erroneous Profile Operation
    - Fixed an issue affecting profile operations which included containers with 'Group By' settings. Previously, running a profile without inferring checks resulted in all fields being erroneously removed from the field list.

- General fixes and improvements

### 2023.12.20 { id=2023.12.20}

#### General Fixes

- Resolved Datastore Creation Issue with Databricks:
    - Fixed an issue encountered when creating source datastores using Databricks with catalog names other than the default `hive_metastore`. This fix ensures a smoother and more flexible datastore creation process in Databricks environments.

- Conflict Resolution for 'anomaly_uuid' Field in Source Container:
    - Corrected a problem where source containers with a field named `anomaly_uuid` were unable to run scan operations. This fix eliminates the conflict with internal system columns, allowing for uninterrupted operation of these containers.

- General fixes and improvements

### 2023.12.14 { id=2023.12.14}

#### Feature Enhancements

- Auto-Detection of Partitioned Files:
    - Improved file handling to automatically detect partitioned files like `*.delta` without the need for an explicit extension. This update resolves the issue of previously unrecognized delta tables.

- Anomaly Weight Threshold for Notifications:
    - Enhanced the notification system to support a minimum anomaly weight threshold for the trigger type "An anomaly is detected". Notifications will now be triggered only for anomalies that meet or exceed the defined weight threshold.

- Team Assignment in Datastore Forms:
    - Updated the Datastore Forms to enable users to manage teams. This enhancement provides Admins with the flexibility to assign or adjust teams right at the point of datastore setup, moving away from the default assignment to the Public team.

#### General Fixes

- Corrected Health Page Duplication:
    - Addressed an issue on the Health Page where "Max Executors" information was being displayed twice. This duplication has been removed for clearer and more accurate reporting.

- General fixes and improvements

### 2023.12.12 { id=2023.12.12}

#### Feature Enhancements

- Incremental Catalog Results Posting:
    - Enhanced the catalog operation to post results incrementally for each container catalogued. Previously, results were only available after the entire operation was completed. With this enhancement, results from successfully catalogued containers are now preserved and posted incrementally, ensuring containers identified are not lost even if the operation does not complete successfully.

#### General Fixes

- Aggregation Comparison Rule Filter:
    - Resolved an issue where filters were not being applied to the Aggregation Comparison Check, affecting both the reference and target filters.

- Case Sensitivity File Extension Support
    - Addressed a limitation in handling file extensions, ensuring that uppercase formats like .TXT and .CSV are now correctly recognized and processed. This update enhances the system's ability to handle files consistently, irrespective of extension case.

- SLA Violation Notification Adjustment:
    - Modified the SLA violation notifications to trigger only once per violation, preventing a flood of repetitive alerts and improving the overall user experience.

- Source record not Available for Max Length Rule
    - Addressed a bug where the Max Length Rule was not producing source records in cases involving null values. The rule has been updated to correctly handle null values, ensuring accurate anomaly marking and data enrichment.

- General fixes and improvements

### 2023.12.08 { id=2023.12.08}

#### Breaking Changes

- Renaming of Enrichment Datastore Tables

	Due to lack of consistency and to avoid conflicts between different categories of Enrichments tables, changes were performed to the table name patterns:

	- The Enrichment table previously named `<enrichment_prefix>_anomalies` has been renamed to `<enrichment_prefix>_failed_checks` due to its content and granularity.
	- The terms `remediation` and `export` were added to distinguish Enrichment Remediation and Export tables from others, resulting in:
	    -  `<enrichment_prefix>_remediation_<container_name>` for Remediation tables.
	    -  `<enrichment_prefix>_export_<asset>` for Export tables.

#### Feature Enhancements

- Refactor Notifications Panel:
    - Introduced a new side panel for Notifications, categorizing alerts by type (Operations, Anomalies, SLA) for improved organization.
    - Added notification tags, receivers, and an action menu enabling users to mute or edit notifications directly from the panel
    - Enhanced UI for better readability and interaction, providing an overall improved user experience.
- Add Enrichment Export Anomalies available asset: 
    - Anomalies are now supported as a type of asset for export to an enrichment datastore, enhancing data export capabilities.
- Add files count metric to profile operation summary 
    - Displayed file count (number of partitions) in addition to existing file patterns count metric in profile operations for DFS datastores.
- Improve Globing Logic:
    - Optimized support for multiple subgroups when globing files from DFS datastores during profile operations, enhancing efficiency.

#### General Fixes

- General fixes and improvements

### 2023.12.05 { id=2023.12.05}

#### Feature Enhancements

- Navigation Improvements in Explore Profiles Page:
    - Upgraded the Explore Profiles Page by adding direct link icons for more precise navigation. Users can now use these links on container and field cards/lists for a direct redirection to detailed views.

#### General Fixes

- General fixes and improvements

### 2023.12.01 { id=2023.12.01}

#### Feature Enhancements

- List View Layout Support:
    - Introduced list view layouts for Datastores, Profiles, Checks, and Anomalies, providing users with an alternative way to display and navigate through their data.

- Bulk Acknowledgement Performance:
    - Improved the performance of bulk acknowledging in-app notifications, streamlining the user experience and enhancing the application's responsiveness.

#### General Fixes

- Checks and Anomalies Dialog Navigation:
    - Resolved an issue with arrow key navigation in Checks and Anomalies dialogs where unintended slider movement occurred when using keyboard navigation. This fix ensures that arrow keys will only trigger slider navigation when the dialog is the main focus.

- Profiled Container Count Inconsistency
    - Ensured that containers that fail to load data during profiling are not mistakenly counted as successfully profiled, improving the accuracy of the profiling process.

- Histogram Field Selection Update:
    - Fixed a bug where histograms were not updating correctly when navigating to a new field. Histograms now properly reflect the data of the newly selected field.

- General fixes and improvements

### 2023.11.28 { id=2023.11.28}

#### Feature Enhancements

- Operations with Tag Selectors:
    - Users can now configure operations (including schedules) with multiple tags, enabling dynamic profile evaluation based on tags at the operation's trigger time.

- Asserted State Filter for Checks:
    - Introduced a new check list filter, allowing users to filter checks by those that have passed or identified active anomalies.

- Bulk Delete for Profiles:
    - Enhanced the system to allow bulk deletion of multiple profiles, streamlining the management process where previously only individual deletions were possible.

- Resizable Columns in Source Records Table:
    - Columns in the anomaly dialog source records can now be manually resized, improving visibility and preventing content truncation.

- Automated Partition Field Setting for BigQuery:
    - For BigQuery tables constrained by a required partition filter, the profile partition field setting is now automatically populated during the Catalog operation.

#### General Fixes

- Sharable Link Authentication Flow:
    - Fixed an issue where direct links did not work if the user was not signed in. Now, users are redirected to the intended page post-authentication.

- Clarified Violation Messages for 'isUnique' Check:
    - Updated the violation message for the 'isUnique' check to describe the anomaly, reducing misinterpretation clearly.

- Access Restriction and Loading Fix for Health Page:
    - Corrected the health page visibility so only admin users can view it, and improved loading behavior for Qualytics services.

- Availability of Requested Tables During Operations:
    - The dialog displaying requested tables/files is now accessible immediately after an operation starts, enhancing transparency for both Profile and Scan operations.

- General fixes and improvements

### 2023.11.14 { id=2023.11.14}

#### Feature Enhancements

- Qualytics App Color Palette and Design Update:
    - Implemented a comprehensive design update across the Qualytics App, introducing a new color palette for a refreshed and modern look. This update includes a significant change to the anomalies color, transitioning from red to orange for a more distinct visual cue. Additionally, the font-family has been updated to enhance readability and provide a more cohesive aesthetic experience across the application.
- System Health Readout:
    - A new `Health` tab has been added to the Admin menu, offering a comprehensive view of each deployment's operational status. This feature encompasses critical details such as the status of app services, current app version, and analytics engine information, enabling better control over system health.
- Enhanced Check with Metadata Input:
    - The Check form now includes a new input field for custom metadata. This enhancement allows users to add key-value pairs for tailored metadata, significantly increasing the flexibility and customization of the Check definition.
- Responsiveness Improvement in Cards Layout:
    - The Cards layout has been refined to improve responsiveness and compactness. This adjustment addresses previous UI inconsistencies and ensures a consistent visual experience across different devices, enhancing overall usability and aesthetic appeal.
- Source Record Enrichment for 'isUnique' Checks:
    - The `isUnique` check has been enhanced to support source record enrichment. This significant update allows users to view specific records that fail to meet the 'isUnique' condition. This feature adds a layer of transparency and detail to data validation processes, enabling users to easily identify and address data uniqueness issues.
- New Enrichment Data:
    - Scan operations now record operation metadata in a new enrichment table with the suffix `scan_operations` including an entry for each table/file scanned with the number of records processed and anomalies identified as well as start/stop time and other relevant details. 
- Insights Enhancement with Check Pass/Fail Metrics:
    - Insights now features the checks section with new metrics indicating the total number of checks passed and failed. This enhancement also offers a visual representation through a chart, detailing the passed and failed checks over a specified reporting period.

#### General Fixes

- `isAddress` now supports defining multiple checks against the same field with different required label permutations
- General fixes and improvements

### 2023.11.08 { id=2023.11.08}

#### Feature Enhancements

- Is Address Check:
    - Introduced a new check for address conformity that ensures the presence of required components such as road, city, and state, enhancing data quality controls for address fields. This check leverages machine learning to support multilingual street address parsing/normalization trained on over 1.2 billion records of data from over 230 countries, in 100+ languages. It achieves 99.45% full-parse accuracy on held-out addresses (i.e. addresses from the training set that were purposefully removed so we could evaluate the parser on addresses it hasn’t seen before).

- Revamped Heatmap Flow in Activity Tab:
    - Improved the user interaction with the heatmap by filtering the operation list upon selecting a date. A new feature has been added to operation details allowing users to view comprehensive information about the profiles scanned, with the ability to drill down to partitions and anomalies.

- Link to Schedule in Operation List:
    - Enhanced the operation list with a new "Schedule" column, providing direct links to the schedules triggering the operations, thus improving traceability and scheduling visibility.

- Insights Tag Filtering Improvement:
    - Enhanced the tag filtering capability on the Insights page to now include table/file-level analysis. This ensures a more granular and accurate reflection of data when using tags to filter insights.

- Support for Incremental Scanning of Partitioned Files:
    - Optimized the incremental scanning process by tracking changes at the record level rather than the last modified timestamp of the folder. This enhancement prevents the unnecessary scanning of all records and focuses on newly added data.

#### General Fixes

- General fixes and improvements

### 2023.11.02 { id=2023.11.02}

#### Feature Enhancements

- Auto Selection of All Fields in Check Form:
    - Improved the user experience in the Check Form by introducing a "select all" option for fields. Users can now auto-select all fields when applying rules that expects a multi select input, streamlining the process especially for profiles with a large number of fields.

- Enhanced Profile Operations with User-Defined Starting Points for Profiling:
    - Users can now specify a value for the incremental identifier, to determine the comprehensive set that will be analyzed.
    - Two new options have been added:
        - Greater Than Time: Targets profiles with incremental timestamp strategies, allowing the inclusion of rows where the incremental field's value surpasses a specified time threshold.
        - Greater Than Batch: Tailored for profiles employing an incremental batch strategy, focusing the analysis on rows where the incremental field’s value is beyond a certain numeric threshold.

- Configurable Enrichment Source Record Limit in Scan Operations:
    - Users can now configure the `enrichment_source_record_limit` to dictate the number of anomalous records retained for analysis, adapting to various use case necessities beyond the default sample limit of 10 per anomaly. This improvement allows for a more tailored and comprehensive analysis based on user requirements.

- Introduction of Passed Status in Check Card:
    - A new indicative icon has been added to the Check Card to assure users of a "passed" status based on the last scan. This icon will be displayed only when there are no active anomalies.

- Inclusion of Last Asserted Time in Check Card:
    - Enhanced the Check Card by including the last asserted time, offering users more detailed and up-to-date information regarding the checks.

- Enhanced Anomaly Search with UUID Support:
    - Improved the anomaly search functionality by enabling users to search anomalies using the UUID of the anomaly, making the search process more flexible and comprehensive.

#### General Fixes

- General fixes and improvements

### 2023.10.27 { id=2023.10.27}

#### Feature Enhancements

- Check Creation through Field Details Page:
    - Users can now initiate check creation directly from the Field Details page, streamlining the check creation process and improving usability.

- Tree View Enhancements:
    - Introduced a favorite group feature where favorite datastores are displayed in a specific section, making them quicker and easier to access.
    - Added search functionalities at both Profile and Field levels to improve the navigation experience.
    - Nodes now follow the default sorting of pages, creating consistency across various views.
    - Enhanced the descriptions in tree view nodes for non-catalogued datastores and non-profiled profiles, providing a clearer explanation for the absence of sub-items.

- Bulk Actions for Freshness & SLAs:
    - Users can now perform bulk actions in Freshness & SLAs, enabling or disabling freshness tracking and setting or unsetting SLAs for profiles efficiently.

- Archived Check Details Visualization:
    - Enhanced the anomaly modal to allow users to view the details of archived checks in a read-only mode, improving the visibility and accessibility of archived checks’ information.

- User Pictures as Avatars:
    - User pictures have been incorporated across the application as avatars, enhancing the visual representation in user listings, teams, and anomaly comments.

- Slide Navigation in Card Dialogs:
    - Introduced a slide navigation feature in the Anomalies and Checks dialogs, enhancing user navigation. Users can now effortlessly navigate between items using navigational arrows, eliminating the need to close the dialog to view next or previous items.

#### General Fixes

- General fixes and improvements

### 2023.10.23 { id=2023.10.23}

#### Feature Enhancements

- Enhanced Data Asset Navigation:
    - Tree View Implementation: Easily navigate through your data assets with our new organized tree view structure
    - Context-Specific Actions: Access settings and actions that matter most depending on your current level of interaction.
    - Simplified User Experience: This update is designed to streamline and simplify your data asset navigation and management.

- Aggregation Comparison Check:
    - New Rule Added: Ensure valid comparisons by checking the legitimacy of operators between two aggregation expressions. 
    - Improved Monitoring: Conduct in-depth comparisons, such as verifying if total row counts match across different source assets.

- Efficient Synchronization for Schema Changes:
    - Seamless Integration: Our system now adeptly synchronizes schema changes in source datastores with Qualytics profiles. 
    - Avoid Potential Errors: We reduced the risk of creating checks with fields that have been removed or altered in the source datastore.

- Clarity in Quality Check Editors:
    - Distinct Update Sources: Easily identify if an update was made manually by a user or automatically through the API.

- Dynamic Quality Score Updates:
    - Live Anomaly Status Integration: Quality Scores now reflect real-time changes based on anomaly status updates.

#### General Fixes

- Various bug fixes and system improvements for a smoother experience.

### 2023.10.13 { id=2023.10.13}

#### Feature Enhancements

- Export Metadata Enhancements:
    - Added a "weight" property to the quality check asset
    
- New AWS Athena Connector:
    - Introduced support for a new connector, AWS Athena, expanding the options and flexibility for users managing data connections.

- Operations List:
    - Introduced a multi-select filter to the operation list, enabling users to efficiently view operations based on their status such as running, success, failure, and warning, thereby streamlining navigation and issue tracking.

#### General Fixes

- Logging Adjustments:
    - Enhanced logging for catalog operations, ensuring that logs are visible and accessible even for catalogs with a warning status, facilitating improved tracking and resolution of issues.
- General fixes and improvements

### 2023.10.09 { id=2023.10.09}

#### Feature Enhancements

- Check Categorization:
    - Introduced new check categories on the checks page to streamline UX and prioritize viewing:
        1. **Important**: Designed around a check's weight value, this category will by default comprise authored checks and inferred checks with active anomalies.
        2. **Favorite**: Featuring all user-favorited checks
        3. **Metrics**: Incorporating all metric checks
        4. **All**: Displaying all checks, whether inferred, authored, or anomalous
    - The default view is set to "Important" (if available) to highlight critical checks and avoid overwhelming users

- Anomalies Page Update:
    - Revamped the Anomalies page with a simplified status filter, adopting a design in alignment with the checks page:
        - **Quick Status Filter**: Facilitates an effortless switch between anomaly statuses.
        - The "Active" tab is presented as the default, providing immediate visibility into ongoing anomalies.

- Notification Testing:
    - Enhanced the Notification Form with a "Test Notification" button, enabling users to validate notification settings before saving

- Metadata Export to Enrichment Stores:
    - Enabled users to export metadata from their datastore directly into enrichment datastores, with initial options for quality checks and field profiles.
    - Users can specify which profiles to include in the export operation, ensuring relevant data transfer.

#### General Fixes

- General fixes and improvements

### 2023.10.04 { id=2023.10.04}

#### Feature Enhancements

- Anomalies Details User Experience:
    - Implemented a "skeleton loading" feature in the Anomaly Details dialog, enhancing user feedback during data loading.

- Enhanced Check Dialog:
    - Added "Last Updated" date to the Check Dialog to provide users with additional insights regarding check modifications.

- API Engine Control:
    - Exposed a new endpoint allowing users to gracefully restart the analytics engine through the API.

#### General Fixes

- Timezone Handling on MacOS:
    - Resolved an issue affecting timezone retrieval due to MacOS privacy updates, ensuring accurate timezone handling.
- Notifications and Alerts:
    - Pager Duty Integration: Resolved issues preventing message sending and improved UI for easier configuration.
    - HTTP Action Notification: Fixed Anomaly meta-data serialization issues affecting successful delivery in some circumstances.
- Scan Duration Accuracy:
    - Adjusted scan duration calculations to accurately represent the actual processing time, excluding time between a failed scan and a successful retry.
- Spark Partitioning:
    - Certain datastores may fail to properly coerce types into Spark-compatible partition column values if that column itself contains anomalous values. When this occurs, an attempt will be made to load the data without a partition column and a warning will be generated for the user.
- General fixes and improvements

### 2023.09.29 { id=2023.09.29}

#### Feature Enhancements
  
- Operations & Schedules UI Update:
    - Redesigned the UI for the operations and schedules lists for a more intuitive UX and to provide additional information.
        - Introduced pagination, filtering, and sorting for the schedules list.
        - Added a "Next Trigger" column to the schedules list to inform users of upcoming schedule triggers.
    - Improved Profile List Modal:
        - Enhanced the profile list modal accessible from operations and schedules.
        - Users can now search by both ID and profile name.
  
- Check Navigation Enhancements:
    - Enhanced navigation between Standard and Metric Cards by introducing direct links that allow users to access metric charts seamlessly from check forms.
    - The checks page navigation state is now reflected in the URL, enhancing UX and enabling precise redirect capabilities.

- Computed Table Enhancements:
    - Upon the creation or update of a computed table, a minimalistic profile operation is now automatically triggered. This basic profile limits sampling to 1,000 and does not infer quality checks.
    - This enhancement streamlines the process when working with computed tables. Users can now directly create checks after computed table creation without manually initiating a profile operation, as the system auto-fetches required field data types.

- Analytics Engine Enhancements:
    - This release replaces our previous consistency model with a more robust one relying upon AMQP brokered durable messaging. The change dramatically improves Qualytics' internal fault tolerance with accompanying performance enhancements for common operations.

#### General Fixes

- Insights Filter Consistency:
    - Fixed an inconsistency issue with the datastore filter that was affecting a couple of charts in Insights
- General fixes and improvements

### 2023.09.21 { id=2023.09.21}

#### Feature Enhancements

- Anomalies Modal Redesign:
    - Streamlined the presentation of Failed Checks by removing the Anomalous Fields grouping. The new layout focuses on a list of Failed Checks, each tagged with the associated field(s) name, if applicable. This eliminates redundancy and simplifies the UI, making it easier to compare failed checks directly against the highlighted anomalous fields in the Source Record.
    - Added the ability to filter Failed Checks by anomalous fields.
    - Introduced direct links to datastores and profiles for enhanced navigation.
    - Updated the tag input component for better UX.
    - Removed the 'Hide Anomalous' option and replaced it with an 'Only Anomalous' option for more focused analysis.
    - Included a feature to display the number of failed checks a field has across the modal.
    - Implemented a menu allowing users to copy Violation messages easily.

- Bulk Operation for Profiles:
    - Extended the profile selection functionality to allow initiating bulk operations like profiling and scanning directly from the selection interface.

#### General Fixes

- DFS Incremental Scans:
    - Addressed an issue that caused incremental scans to fail when no new files were detected on globs. Scans will now proceed without failure or warning in such cases.
- Improve performance of the Containers endpoint
- General fixes and improvements

### 2023.09.16 { id=2023.09.16}

#### Feature Enhancements

- Insights Timeframe and Grouping:
    - Trend tooltips have been refined to change responsively based on the selected timeframe and grouping, ensuring that users receive the most relevant information at a glance.

- Enhanced PDF export for Insights:
    - Incorporated the selected timeframe and grouping settings into the exported PDF, ensuring that users experience consistent detail and clarity both within the application and in the exported document.
    - Added a "generated at" timestamp to the PDF exports, providing traceability and context to when the data was captured, further enhancing the comprehensiveness of exported insights.

- Source Record Display Improvements:
    - The internal columns' background color has been calibrated to offer a seamless appearance in both light and dark themes.

#### General Fixes

- Time Series Chart Rendering:
    - Addressed an issue where the time series chart would not display data points despite having valid measurements. The core of the problem was pinpointed to how the system handled `0` values, especially when set as min and/or max thresholds.
    - Resolved inconsistencies in how undefined min/max thresholds were displayed across different comparison types. While we previously had a UI indicator displaying for some comparison types, this was missing for "Absolute Change" and "Absolute Value".

- General fixes and improvements

### 2023.09.14 { id=2023.09.14 }

#### Feature Enhancements

- Insights Improvements:
    - Performance has been significantly optimized for smoother interactions.
    - Introduced timeframe filters, allowing users to view insights data by week, month, quarter, or year.
    - Introduced grouping capabilities, enabling users to segment visualizations within a timeframe, such as by days or weeks.

- Metric Checks Enhancements:
    - Introduced a new Metric Checks tab in both the datastore and explore perspectives.
    - Added a Time Series Chart within the Metric Checks tab:
        - Displays check measurements over time.
        - Allows on-the-fly adjustments of min/max threshold values.
        - Showcases enhanced check metadata including tags, active anomaly counts, and check weights.

- Check Form Adjustments:
    - Disabled the `Comparison Type` input for asserted checks

#### General Fixes

- Configuring Metric Checks through the Check Form:
    - Resolved a bug where users were unable to clear optional inputs such as "min" or "max".
- General fixes and improvements

### 2023.09.08 { id=2023.09.08 }

#### Feature Enhancements

- Presto & Trino Connectors:
    - We've enhanced our suite of JDBC connectors by introducing dedicated support for both Presto and Trino. Whether you're utilizing the well-established Presto or the emerging Trino, our platform ensures seamless compatibility to suit your data infrastructure needs.

#### General Fixes

- Incremental Scan: 
    - Resolved an issue where the scan operation would fail during the "Exists In Check" if there were no records to be processed.
- General fixes and improvements

### 2023.09.07 { id=2023.09.07 }

#### Feature Enhancements

- Concurrent Operations:
    - Introduced the ability to run multiple operations of the same type concurrently within a single datastore, even if one is yet to finish. This brings more flexibility and efficiency in executing operations
  
- Autocomplete Widget:
    - A hint for a shortcut has been added, allowing users to manually trigger the autocomplete widget and enhancing usability
  
- Source Record Display Enhancements:
    - Added a new 'Hide Anomalous' option, providing users with the choice to hide anomalous records for clearer viewing
    - Transitioned from hover-based tooltips to click-activated ones for better UX
    - For a consistent data presentation, internal columns will now always be displayed first
  
- Check Form Improvements:
    - Users now receive feedback directly within the form upon successful validation, replacing the previous toast notification method
    - Additionally, for 504 validation timeouts, a more detailed and context-specific message is provided

#### General Fixes

- Addressed issues for 'Is Replica Of' failed checks in source record handling
- General fixes and improvements

### 2023.08.31 { id=2023.08.31}

#### General Fixes

- Fixed an issue where the Source Record remediation was incorrectly displayed for all fields
- Adjusted the display of field Quality Scores and Suggestion Scores within the Source Record
- Fixed a bug in the Check Form where the field input wouldn’t display when cloning a check that hasn’t been part of a scan yet
- Resolved an issue where failed checks for shape anomalies were not receiving violation messages

### 2023.08.30 { id=2023.08.30}

#### Feature Enhancements

- Anomaly Dialog Updates:
    - Optimized Source Data Columns Presentation: To facilitate faster identification of issues, anomalous fields are now presented first. This enhancement will prove particularly useful for data sources with a large number of columns.
    - Enhanced Sorting Capabilities: Users can now sort the source record data by name, weight, and quality score, providing more flexible navigation and ease of use.
    - Field Information at a Glance: A new menu box has been introduced to deliver quick insights about individual fields. Users can now view weight, quality score, and suggested remediation for each field directly from this menu box.

- Syntax Highlighting Autocomplete Widget:
    - Improved UX: The widget has been enhanced to better identify and display hint types, including distinctions between tables, keywords, views, and columns. This enhancement enriches the autocomplete experience.

#### General Fixes

- Check Dialog Accessibility:
    - Addressed an issue where the check dialog was not opening as expected when accessed through a direct link from the profile page.
- General fixes and improvements

### 2023.08.23 { id=2023.08.23}

#### Feature Enhancements

- Profiles Page:
    - Introduced two new sorting methods to provide users with more intuitive ways to explore their profiles: Sort by **last profiled** and Sort by **last scanned**.
    - Updated the default sorting behavior. Profiles will now be ordered by name right from the start, rather than by their creation date.

- Add New isNotReplicaOf Check:
    - With this rule, users can assert that certain datasets are distinct and don't contain matching data, enhancing the precision and reliability of data comparisons and assertions.

- Introduce new Metric Check
    - We've added a new Metric check tailored specifically for handling timeseries data. This new check is set to replace the previous Absolute and Relative Change Checks.
    - To offer a more comprehensive and customizable checking mechanism, the Metric check comes with a comparison input:
        - **Percentage Change**: Asserts that the field hasn't deviated by more than a certain percentage (inclusive) since the last scan.
        - **Absolute Change**: Ensures the field hasn't shifted by more than a predetermined fixed amount (inclusive) from the previous scan.
        - **Absolute Value**: During each scan, this option records the field value and asserts that it remains within a specified range (inclusive).

#### General Fixes

- Schema Validation:
    - We've resolved an issue where the system was permitting the persistence of empty values under certain conditions for datastores and checks. This fix aims to prevent unintentional data inconsistencies, ensuring data integrity.

- General fixes and improvements

### 2023.08.18 { id=2023.08.18}

#### Feature Enhancements

- Auditing:
    - Introduced significant enhancements to the auditing capabilities of the platform, designed to provide better insights and control over changes. The new auditing features empower users to keep track of change sets across all entities, offering transparency and accountability like never before. A new activity endpoint has been introduced, providing a log of user interactions across the application.

- Search Enhancements:
    - Profiles and Anomalies lists can now be searched by both identifiers and descriptions using the same search input.

- Catalog Operation Flow Update:
    - Made a minor update to the datastore creation and catalog flow to enhance user flexibility and experience. Instead of automatically running a catalog operation post datastore creation, users now have a clearer, intuitive manual process. This change offers users the flexibility to set custom catalog configurations, like syncing only tables or views.

- Operation Flow Error Handling:
    - Enhanced user experience during failures in the Operation Flow. Along with the failure message, a "Try Again" link has been added. Clicking this link will revert to the configuration state, allowing users to make necessary edits without restarting the entire operation process.

- Sorting Enhancements:
    - Introduced new sorting options: "Completeness" and "Quality Score". These options are now available on the profiles & fields pages.

#### General Fixes

- Datastore Connection Edit:
    - Improved the Datastore connection edit experience, especially for platforms like BigQuery. Resolved an issue where file inputs were previously obligatory for minor edits. For instance, renaming a BigQuery Datastore no longer requires a file input, addressing this past inconvenience.

- Pagination issues:
    - Resolved an issue with paginated endpoints returning 500 instead of 422 on requests with invalid parameters.

### 2023.08.11 { id=2023.08.11}

#### Feature Enhancements

- Insights Export: Added a new feature that allows users to export Insights directly to PDF, making it easier to share and review data insights.
- Check Form UX: 
    - Fields in the Check Form can now be updated if the check hasn't been used in a Scan operation, offering more flexibility to users.
    - Enhanced visual cues in the form with boxed information to clarify the limitations certain properties have, depending on the state of the form.
    - A new icon has been introduced to represent the number of scan operations that have utilized the check, providing users with a clearer overview.
- SLA Form UX: 
    - Revamped Date Time handling for enhanced time zone coverage, allowing for user-specified date time configurations based on their preferred time zone.
- Filter and Sorting:
    - Added Datastore Type filter and sorting for source datastores
    - Added Profile Completeness sorting and type filtering and sorting
    - Added Check search by identifier or description

#### General Fixes

- SparkSQL Expressions: Added support to field names with special characters to SparkSQL expressions using backticks
- Pagination Adjustment: The pagination limit has been fine-tuned to support a maximum of 100 items per page, improving readability and navigation.

### 2023.08.03 { id=2023.08.03}

#### Maintenance Release ####
- Updated enrichment sidebar details design.
- Tweaked SQL input dialog sizing.
- Fixed filter components width bug.
- Retain the start time of operation on restart.
- Fixed exclude fields to throw exceptions on errors.
- Improved performance when using DFS to load reference data.

### 2023.07.31 { id=2023.07.31}

#### Maintenance Release ####
- Changed UX verbiage and iconography for Anomaly status updates.
- Fixed intermittent notification template failure.
- Fixed UI handling of certain rule types where unused properties were required.
- Improved error messages when containers are no longer accessible.
- Fixed Hadoop authentication conflicts with ABFS.
- Fixed an issue where a Profile operation run on an empty container threw a runtime exception.

### 2023.07.29 { id=2023.07.29}

#### Feature Enhancements ####

- Added a NotExistsIn Check Type: Introducing a new rule type that asserts that values assigned to this field do not exist as values in another field.
- Check Authoring UI enhancements: Improved user interface with larger edit surfaces and parenthesis highlighting for better usability.
- Container Details UI enhancement: Improved presentation of container information in sidebars for easier accessibility and understanding.
- Added Check Authoring Validation: Users can now perform a dry run of the proposed check against representative data to ensure accuracy and effectiveness.
- Change in default linkage between Checks and Anomalies: Filters now default to "Active" status, providing more refined results and support for specific use cases.


### 2023.07.25 { id=2023.07.25}

#### Feature Enhancements #####

- Satisfies Expression Enhancement: The Satisfies Expression feature has been upgraded to automatically bind fields referenced in the user-defined expressions, streamlining integration and improving usability.

#### Added Support ####

- Extended Support for ExistsIn Checks: The ExistsIn checks now offer support for computed tables, empowering users to perform comprehensive data validation on computed data.

#### General Fixes ####

- Enhanced Check Referencing: Checks can now efficiently reference the full dataframe by using the alias "qualytics_self," simplifying referencing and providing better context within checks.

- Improved Shape Anomaly Descriptions: Shape anomaly descriptions now include totals alongside percentages, providing more comprehensive insights into data irregularities.

- Fix for Computed Table Record Calculation: A fix has been implemented to ensure accurate calculation of the total number of records in computed tables, improving data accuracy and reporting.

- Enhanced Sampling Source Records Anomaly Detection: For shape anomalies, sampling source records now explicitly exclude replacement, leading to more precise anomaly detection and preserving data integrity during analysis.


### 2023.07.23 { id=2023.07.23}

#### Bug Fixes

-  Fix for total record counts when profiling large tables



### 2023.07.21 { id=2023.07.21}

#### Feature Enhancements

- Notification Form: Enhanced the user interface and experience by transforming the Channel and Tag inputs into a more friendly format.
- Checks & Anomalies: Updated the default Sort By criterion to be based on "Weight", enabling a more effective overview of checks and anomalies.
- Profile Details (Side Panel): Introduced a tooltip to display the actual value of the records metric, providing clearer and instant information.
- Freshness Page: Added a new navigation button that directly leads to the Profile Details page, making navigation more seamless.
- Profile Details: Introduced a settings option for the user to perform actions identical to those from the Profile Card, such as changing profile settings and configuring Checks and SLAs.
- SparkSQL Inputs: Implemented a new autocomplete feature to enhance user experience. Writing SQL queries is now more comfortable and less error-prone.



### 2023.07.19 { id=2023.07.19}

#### General Fixes

- General fixes and improvements



### 2023.07.14 { id=2023.07.14}

#### Feature Enhancements

- API enhancements 
    - Improved performance of our json validation through the adoption of Pydantic 2.0
      - Upgraded our API specification to OpenAPI 3.1.0 compatible, this uses JSON Schema 2020-12.
- Upgraded to Spark 3.4
     - Significant performance enhancements for long-running tasks and shuffles
- Added support for Kerberos authentication for Hive datastores
- Enhanced processing for large dataframes with JDBC sources
    - Handle arbitrarily large tables and views by chunking into sequentially processed dataframes
- Improvements for Insights view when limited data is available
- Various user experience enhancements

#### Bug Fixes

- Date Picker fix for Authored Checks
- Allow tags with special characters to be edited

### 2023.07.03 { id=2023.07.03 }


#### Feature Enhancements

- Insights Made Default View on Data Explorer
    - Gain valuable data insights more efficiently with the revamped Insights feature, now set as the default view on the Data Explorer.
- Reworked Freshness with Sorting and Grouping
    - Easily analyze and track data freshness based on specific requirements thanks to the improved Freshness feature, now equipped with sorting and grouping functionalities.
- Enhanced Tables/Files Cards Design:
    - Experience improved data analysis with the updated design of tables/files cards, including added average completeness information and reorganized identifiers.

#### Added Support

- Support for Recording Sample Shape Anomalies to Remediation Tables
    - Address potential data shape issues more effectively as the platform now supports recording a sample of shape anomalies to remediation tables.

- New Metrics and Redirect to Anomalies for Profile/Scan Results
      - Access additional metrics for profile/scan results and easily redirect to anomalies generated by a scan from Activity tab for efficient identification and resolution of data issues.

#### General Fixes

- Reduced Margin Between Form Input Fields:
      - Enjoy a more compact and streamlined design with a reduced margin between form input fields for an improved user experience.

#### Bug Fixes

- Fixed Pagination Reset Issue During Check Updates
      - Pagination will no longer reset when checks are updated, providing a smoother user experience, with reset now occurring only during filtering.
- Resolved Vertical Misalignment of Check and Anomaly Icons
    - The issue causing vertical misalignment between Check and Anomaly icons on the Field Profile page has been fixed, resulting in a visually pleasing and intuitive user interface.


### 2023.06.24 { id=2023.06.24 }

#### Feature Enhancements

- Refactored Partition Reads on JDBC 
    - Refactored partitioned reads on JDBC to improve performance, resulting in faster and more efficient data retrieval.

#### Bug Fixes

- Fixed Inputs on Change Checks
    - Refined inputs on change checks to differentiate between Absolute and Relative measurements, ensuring precise detection and handling of data modifications based on numeric values (Absolute) and percentage (Relative) variations.

- Resolved Enum Type Ordering Bug for Paginated Views
    - Fixed bug causing inconsistent and incorrect sorting of enum values across all paginated views, ensuring consistent and accurate sorting of enum types.
#### General Fixes

- Added Success Effect
    - Added effect when a datastore is configured successfully, enhancing the user experience by providing visual confirmation of a successful configuration process.


### 2023.06.20 { id=2023.06.20 }

#### Feature Enhancements

- Reworked Tags View
    - Improved the usability and visual appeal of the tags view. Added new properties like description and weight modifier to provide more detailed information and assign relative importance to tags. The weight value directly correlates with the level of importance, where a higher weight indicates higher significance.

- Inherited Tags Support
    - Implemented support for inherited tags in taggable entities. Now tags can be inherited from parent entities, streamlining the tagging process and ensuring consistency across related items. Inherited Tags will be applied to anomalies AFTER a Scan operation.

- Added Total Data Under Management to Insights
    - Introduced a new metric under Insights that displays the total data under management. This provides users with valuable insights into the overall data volume being managed within the system.

#### Added Support

- Bulk Update Support
    - Introduced bulk update functionality for tables, files, and fields. Users can now efficiently Tag multiple items simultaneously, saving time and reducing repetitive tasks.

- Smart Partitioning of BigQuery
    - Enabled smart partitioning in BigQuery using cluster keys. Optimized data organization within BigQuery for improved query performance and cost savings.

#### Bug Fixes

- Fixed Scheduling Operation Issues
    - Addressed a bug causing scheduling operations to fail with invalid days in crontabs. Users can now rely on accurate scheduling for time-based tasks without encountering errors.

#### General Fixes

- Improved Backend Performance
    - Implemented various internal fixes to optimize backend performance. This results in faster response times, smoother operations, and an overall better user experience.

- Enhanced Tag Input:
    - Improved tag input functionality in the Check form dialog. Users can now input tags more efficiently with enhanced suggestions and auto-complete features, streamlining the tagging process.

- Enhanced File Input Component
    - Upgraded the file input component in the Datastore form dialog, providing a more intuitive and user-friendly interface for uploading files. Simplifies attaching files to data entries and improves overall usability.

### 2023.06.12 { id=2023.06.12 }

#### Feature Enhancements

- [**Explore**](/userguide/explore/global-explore/) is the new centralized view of Activities, Containers (Profiles, Tables, Computed Tables), Checks, Anomalies and Insights across ALL Datastores. This new view allows for filtering by Datastores & Tags, which will persist the filters across all of the submenu tabs. The goal is to help with Critical Data Elements and filter out irrelevant information.
- Enhanced Navigation Features
    - The navigation tabs have been refined for increased user-friendliness.
    - Enhanced the Profile View and added a toggle between card and list views.
    - `Datastores` and `Enrichment Datastores` have been unified, with a tabular view introduced to distinguish between your Source Datastores and Enrichment Datastores.
    - `Explore` has been added to the main navigation, and `Insights` has been conveniently relocated into the Explore submenu.
    - Renamed `Tables/Files` to `Profiles` in the Datastore details page.

#### Added Support

- We're thrilled to introduce two new checks, the `Absolute Change Limit` and the `Relative Change Limit`, tailored to augment data change monitoring. These checks enable users to set thresholds on their numeric data fields and monitor fluctuations from one scan to the next. If the changes breach the predefined limits, an anomaly is generated. 

    - ![Screenshot](assets/changelog/absolute-relative-change-limit.png#only-light){: style="height:100px"}
    ![Screenshot](assets/changelog/absolute-relative-change-limit.png#only-dark){: style="height:100px"}
    - The [`Absolute Change Limit`](/userguide/checks/absolute-change-limit-check) check is designed to monitor changes in a field's value by a fixed amount. If the field's value changes by more than the specified limit since the last applicable scan, an anomaly is generated.
    - The [`Relative Change Limit`](/userguide/checks/relative-change-limit-check) check works similarly but tracks changes in terms of percentages. If the change in a field's value exceeds the defined percentage limit since the last applicable scan, an anomaly is generated.

#### General Fixes

- General UI fixes with new navigational tabs
- Resolved an issue when creating a computed table
- Incorporated functionality to execute delete operations and their related results.
- Renamed "Rerun" button to "Retry" in the operation list

### 2023.06.02 { id=2023.06.02 }
#### General Fixes
- Added GCS connector with Keyfile support:
    - The GCS connector now supports Keyfile authentication, allowing users to securely connect to Google Cloud Storage.

- Improved BigQuery connector by removing unnecessary inputs:
    - Enhancements have been made to the BigQuery connector by streamlining the inputs, eliminating any unnecessary fields or options.
    - This results in a more user-friendly and efficient experience.

- Renamed satisfiesEquation to satisfiesExpression:
    - The function "satisfiesEquation" has been renamed to "satisfiesExpression" to better reflect its functionality.
    - This change makes it easier for users to understand and use the function.

#### Added Support

- Added Check Description to Notification rule messages:
    - Notification rule messages now include the Check Description.
    - This allows users to add additional context and information about the specific rule triggering the notification and passing that information to downstream workflows.
  
- Added API support for tuning operations with a high correlation threshold for profiles and high count rollup threshold for anomalies in scan:
    - The API now supports tuning operations by allowing users to set a higher correlation threshold for profiles.
    - It also enables users to set a higher count rollup threshold for anomalies in scan.
    - This customization capability helps users fine-tune the behavior of the system according to their specific needs and preferences.
    
### 2023.05.26 { id=2023.05.26 }
#### Usability

- Improved the navigation in the Activity tab’s side panel for easier and more intuitive browsing including exposing the ability to comment directly into an anomaly
- Added a redirect to the Activity tab when an operation is initiated for a smoother workflow.

#### Bug Fixes
- Resolved an issue where the date and time were not displaying correctly for the highest value in profiles.
- Fixed a problem with scheduled operations when the configured timing was corrupted.
- Addressed an issue where filtered checks were causing unexpected errors outside of the intended dataset.

### 2023.05.23 { id=2023.05.23 }
#### Feature Enhancements

- Scheduled operation editing
    - Added the ability for users to edit a scheduled operation. This allows users to make changes to the schedule of an operation.
- Catalog includes filters
    - Added catalog include filters to only process tables, views, or both in JDBC datastores. This allows users to control which object types are processed in the datastore.
- isReplicaOf check filters
    - Added filter support to the isReplicaOf check. This allows users to control which tables are checked for replication.
- Side panel updates
    - Updated side panel design and added an enrichment redirect option.
#### Added Support

- IBM DB2 datastore
    - Added support for the IBM DB2 datastore. This allows users to connect to and process data from IBM DB2 databases.
- API support for tagging fields
    - Added API support for tagging fields. This allows users to tag fields in the datastore with custom metadata.
#### Bug Fixes

- Freshness attempting to measure views
    - Fixed an issue with freshness attempting to measure views.
- Enrichment to Redshift and string data types
    - Fixed an issue with enrichment to Redshift and string data types. This issue caused enrichment to fail for tables that contained string data types

### 2023.05.10 { id="2023.05.10" }

#### Feature Enhancements
- Container Settings
    - Introducing the ability to Group fields for improved insights and profiling precision.
    - Added functionality to Exclude fields from the container, allowing associated checks to be ignored during operations, leading to reduced processing time and power consumption.
    - We now support identifiers on commuted tables during profiling operations.

- Checks
    - Improved usability by enabling quick cloning of checks within the same datastore.
        - Users can now easily create a new check with minor edits to tables, fields, descriptions, and tags based on an existing check.
    - Introducing the ability to write Check Descriptions to the Enrichment store, enabling better organization and management of check-related data downstream. 
        - *Note: Updating the Enrichment store data requires a new Scan operation.*
    - Enhanced anomaly management by providing a convenient way to filter and view all anomalies generated by a specific check.
        - Users can now access the Anomaly warning sign icon within the Check dialog, providing quick access to two options: View Anomalies and Archive Anomalies.
- Usability
    - Introducing the ability to generate an API token from within the user interface.
        - This can be done through the Settings > Security section, providing a convenient way to manage API authentication.
    - Added the ability to search tables/files and apply filters to running operations.
        - This feature eliminates the need to rely solely on pagination, making it easier to select specific tables/files for operations.
    - Included API and SparkSQL links in the documentation for easy access to additional resources and reference materials.

#### Added Support

- Hive datastore support has been added, allowing seamless integration with Hive data sources.
- Timescale datastore support has been added, enabling efficient handling of time-series data.
- Added support for HTTP(S) and SOCKS5 proxies, allowing users to configure proxy settings for data operations.
- Default encryption for rabbitMQ has been implemented, enhancing security for data transmission.

#### Bug Fixes
- Resolved a bug related to updating tag names, ensuring that tag name changes are properly applied.
- Fixed an overflow bug in freshness measurements for data size, resulting in accurate measurements and improved reliability.

#### General Fixes
- Updated default weighting for shape anomalies, enhancing the accuracy of anomaly detection and analysis.
- Increased datastore connection timeouts, improving stability and resilience when connecting to data sources.
- Implemented general bug fixes and made various improvements to enhance overall performance and user experience.


### 2023.04.19 { id=2023.04.19 }

We're pleased to announce the latest update that includes enhancements to UI for an overall better experience:
#### Feature Enhancements
- Added Volumetric measurements to Freshness Dashboard:
    - Gain valuable insights into your data's scale and storage requirements with our new volumetric measurements. SortBy Row Count or Data Size to make informed decisions about your data resources.
- Added `isReplicaOf` check:
    - The new `isReplicaOf` check allows you to easily compare data between two different tables or fields, helping you identify and resolve data inconsistencies across your datastores.

#### Added Support
- Redesigned Checks and Anomalies listing:
    - Enjoy a cleaner, more organized layout with more information that makes navigating and managing checks and anomalies even easier.
    - <iframe width="760" height="415" src="https://www.loom.com/embed/22b561a7d4764e9d9876ba7515084c10" title="Checks Listing Page" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
- Redesigned Anomaly Details view:
    - The updated anomaly view provides a more thoughtful and organized layout.
    - <iframe width="760" height="415" src="https://www.loom.com/embed/6e975e5297bb4daa95ed4a1b52fd8648" title="Anomalies Listing Page & Dialog" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
- Improved Filter components:
    - With a streamlined layout and organized categories, filtering your data is now more intuitive. Dropdown options are now to the right to allow view of the Clear and Apply buttons
- Updated Importance score to Weight & added SortBy support:
    - Manage checks and anomalies more effectively with our updated ‘Weight' feature (formerly ‘Importance Score') and the new SortBy support function, allowing you to quickly identify high-priority issues.

#### General Fixes

- General fixes and performance improvements


### 2023.04.07 { id=2023.04.07 }

#### Feature Enhancements

- We've just deployed an MVP version of the Freshness Dashboard! This feature lets you create, manage, and monitor all of the SLAs for each of your datastores and their child files/tables/containers, all in one place. It's like having a birds-eye view of how your datastores are doing in relation to their freshness.
    - To access the Freshness Dashboard, just locate and click on the clock icon in the top navigation between Insights and Anomalies. By default, you'll see a rollup of all the datastores in a list view with their child files/tables/containers collapsed. Simply click on a datastore row to expand the list.
- We've also made some improvements to the UI, including more sorting and filtering options in Datastores, Files/Tables, Checks, and Anomalies. Plus, we've added the ability to search the description field in checks, making it easier to find what you're looking for.
- Last but not least, we've added a cool new feature to checks - the ability to archive ALL anomalies generated by a check. Simply click on the anomaly warning icon at the top of the check details box to bring up the archive anomalies dialog box.
