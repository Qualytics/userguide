# 2024 

## Release Notes

### 2024.12.23 { id=2024.12.23 }

#### Feature Enhancements

- User and Teams Permissions
    - We are excited to introduce an enhancement to User and Team Permissions.
        - Users can now have `Admin`, `Manager`, or `Member` roles.
            - The Manager role provides a subset of Admin permissions for global assets or settings but does not include the "Admin exemption to team roles."
        - Teams can have specific permissions: `Editor`, `Author`, `Drafter`, `Viewer`, and `Reporter`.
            - Each permission type includes restricted capabilities tailored to its role.
        - Admins can now create special tokens that grant access exclusively to SCIM endpoints. These tokens allow customers to enable SCIM integrations with minimal access, ensuring the holder cannot access other endpoints or log in to the platform.

- Improve Visibility of Datastore Teams
    - Users can now view respective teams in the tree view footer. Depending on privileges, they can manage this field.
    - Teams are also visible in the table and field context for improved collaboration and data transparency.

#### General Fixes

- Completeness Rounding
    - Added two more decimal places to the Completeness metric in the Overview tab.
        - Previously, percentages were being rounded up incorrectly.

- "Is Replica Of" Check Validation
    - Fixed a bug that occurred when users attempted to validate this check using the same container.

- Global Search
    - Fixed the label to better distinguish between Enrichment Datastores and Source Datastores.

- General Fixes and Improvements.

### 2024.12.11 { id=2024.12.11 }

#### Feature Enhancements

- Add `Max Parallelization` Field on Datastore Connection
    - Users can now configure the maximum parallelization level for certain datastores, providing greater control over operation performance.

#### General Fixes

- General Fixes and Improvements.

### 2024.11.29 { id=2024.11.29 }

#### Feature Enhancements

- Activity List
    - Removed the `Warning` status for a cleaner and more concise status display.
    - Added an alert icon to indicate if an operation completed with warnings, improving visibility into operation outcomes.

#### General Fixes

- Better handling of Oracle Date and Numeric columns during Catalog operations for improved partition field selection.
- General Fixes and Improvements.

### 2024.11.21 { id=2024.11.21 }

#### Feature Enhancements

- Improved Operations Container Dialogs
    - Added container status details based on profile and scan results, providing better visibility of container-level operations.
    - Introduced a loading tracker component for containers, enhancing feedback during operation processing.
    - Made the entire modal reactive to operation updates, enabling real-time tracking of operation progress within the modal.
    - Removed "containers requested" and "containers analyzed" dialogs for a cleaner interface.

#### General Fixes

- Resolved an issue where the table name was not rendering correctly in notifications when using the `{{customer_name}}` variable.

- General Fixes and Improvements.

### 2024.11.12 { id=2024.11.12 }

#### Feature Enhancements

- Enhance Data Catalog Integration
    - Introduced a new domain input field that allows users to select specific domains, enabling more granular control over assets synchronization.

- Scan Results Enhancements
    - Added partition label to the scan results modal for improved partition identification.
    - Removed unnecessary metadata partitions created solely for volumetric checks, reducing clutter in scan results.

- Activity Tab
    - Display of Unprocessed Containers in the Operation List
        - Unprocessed containers are now visible in the operation list within the operation summary.
        - A total count label was added to indicate if the number of analyzed containers exceeds the total requested.
        - The search icon now highlights in a different color if not all containers were analyzed, making it easier to identify incomplete operations.
    - Reorder the Datastore Column in the Activity Tab
        - Users can now reorder columns in the Activity tab for easier navigation and data organization.
    - Profile Operations
        - Users can now view added, updated, and total inferred checks within Profile operations.
    - Triggered by Column
        - Updated the term "Triggered by API" to "Triggered by System" for clarity.

#### General Fixes

- General Fixes and Improvements.

### 2024.11.1 { id=2024.11.1 }

#### Feature Enhancements

- Observability Enhancements
    - An observability heatmap was added to the volumetric card in the Observability tab.
        - The heatmap allows users to monitor volumetric status and check for new anomalies.
     - Improved observability chart for clearer insights.
        - Users can now view the count of volumetric anomalies produced over time, along with the last recorded measurements for each period.
        - Introduced new color indicators to help distinguish volumetric measures outside thresholds that didn’t produce anomalies from those that did.

- Editable Tags in Field Details
    - Users with write permissions can now manage tags directly in the Field Details within the Explore context.

- Distinct Count Rule Update
    - The Distinct Count rule now excludes the Coverage field for more accurate assessments.

- Support for Pasting into Expected Values
    - Users can now paste values from spreadsheets directly into Expected Values, saving time on data entry.

#### General Fixes

- General Fixes and Improvements.

### 2024.10.23 { id=2024.10.23 }

#### Feature Enhancements

- Dremio Connector
    - We’ve expanded our connectivity options by supporting a new connection with Dremio.

- Full View of Abbreviated Metrics in Operation Summary
    - Users can now hover over abbreviated metrics to see the full value for better clarity.

- Redirect to Conflicting Check
    - Added a redirect link to the conflicting check from the error message, improving navigation when addressing errors.

- Enhanced Visibility and Engagement for Tags and Notifications Setup
    - Introduced a Call to Action to encourage users to manage Tags and Notifications for better engagement.

- Favorite Containers
    - Users can now favorite individual containers.
    - The option to favorite datastores and containers is now available in both card and list views.

#### General Fixes

- General Fixes and Improvements.

### 2024.10.16 { id=2024.10.16 }

#### Feature Enhancements

- Improved Anomaly Modal
    - Introduced an information icon in each failed check to display the check's description.
    - Anomaly links now persist filters for sort order and displayed fields.
    - Added integration details to fields in a source record.

- Secrets Management
    - Added support for Secrets Manager in connection properties, enabling integration with Vault and other secrets management systems.

- Alation Data Dictionary
    - Enhanced the dictionary to display friendly names in anomaly screens for improved usability.
    - Added integration information to the datastore, container, and fields in the tree view footer.

- Tag Category
    - Introduced support for tag categories to improve tag management, with sorting and filtering options based on the category field.

- Call to Action for Volumetric Measurements
    - A call to action was added in the overview tab within the container context, and the observability page per container was added to enable volumetric measurements.

- Error Display for Check Operations
    - Bulk operations like Edit, Activate, Update, and Template Edit now display error messages clearly when validation fails.

- Check Validation
    - Improved check validation logic to enhance bulk check validation speed and prevent timeouts.

- Tag Filtering for Fields
    - Users can now filter fields by tags in the field list under the datastore context.

- Field Remarks in Native Field Properties
    - Added support for displaying field remarks alongside other native field properties.

- Customer Support Link
    - Users can now access the Qualytics Helpdesk via the Discover menu in the main header.

#### General Fixes

- General Fixes and Improvements.

### 2024.10.4 { id=2024.10.4 }

#### Feature Enhancements

- Insights Page Redesign
    - Introduced a new Overview card displaying key metrics such as `Data Under Management`, `Source Datastores`, and `Containers`.
    - Added a doughnut chart visualization for checks and anomalies, providing a clearer view of data health.
    - Expanded available metrics to include profile runs and scan runs.
    - Users can now easily navigate to Checks and Anomalies based on their current states and statuses.
    - Implemented data volume visualizations to give users better insight into data trends.
    - Introduced a legend option that allows users to compare specific metrics against the primary one.
    - Enhanced the check distribution visualization across the platform within the overview tabs.

- Check Filter
    - Now users can filter `Not Asserted` checks.

- Team Management
    - Now admin users can modify the `Read` and `Write` permissions of the `Public` Team.

- Reapplying Clone Field
    - Check cloning functionality by attempting to reapply the field from the original (source) check when a new container is selected. If the selected container matches the field and type from the original check, the cloned field will be reapplied automatically.

#### General Fixes

- Allow saving checks with attached templates as drafts
    - Adjusted the behavior to allow checks attached to a template to be saved as drafts. The `Save as draft` feature now remains functional when a template is attached.

- Incremental identifier strange behavior
    - When a user tries to modify a query in a computed table, the Incremental Modifier is set to null.

- General Fixes and Improvements

### 2024.9.25 { id=2024.9.25 }

#### Feature Enhancements

- Observability
    - Time-series charts are presented to monitor data volume and related anomalies for each data asset.
        - Custom thresholds were added to adjust minimum and maximum volume expectations.
    - The Metrics tab has been moved to the Observability tab.
    - The Observability tab has replaced the Freshness page.

- Check Category Options for Scan Operations
    - Users can select one or multiple check categories when running a scan operation.

- Anomaly Trigger Rule Type Filter
    - Added a filter by check rule types to anomaly triggers. A help component was added to the tags selector to improve clarity.

- Auto-Archive Anomalies
    - A new Duplicate status has been introduced for anomalies.
    - Users can now use Incremental Identifier ranges to auto-archive anomalies with the new Duplicate status.
    - An option has been added to scan operations to automatically archive anomalies identified as duplicates if the containers analyzed have incremental identifiers configured.
  - A dedicated tab for filtering duplicate anomalies has been added for better visibility.

- Tree View and Breadcrumb Context Menu
    - A context menu has been added, allowing users to copy essential information and open links in new tabs.
    - Users can access the context menu by right-clicking on the assets.

- Incremental Identifier Support
    - Users can manage incremental identifiers for computed tables and computed files.

- Native Field Properties
    - Users can now see native field properties in the field profile, displayed through an info icon next to the Type Inferred section.

- Qualytics CLI Update
    - Users can now import check templates.
    - A status filter has been added to check exports. Users can filter by `Active`, `Draft`, or `Archived` (which will include `Invalid` and `Discarded` statuses).

#### General Fixes

- The Oracle connector now handles invalid schemas when creating connections.
- Anomalies identified in scan operations were not counting archived statuses.
- Improved error message when a user creates a schedule name longer than 50 characters.
- General Fixes and Improvements.

#### Breaking Changes

- Freshness and SLA references have been removed from user notifications and notification rules, users should migrate to Observability using volumetric checks.

### 2024.9.14 { id=2024.9.14 }

#### Feature Enhancements

- Volumetric Measurement
    - We are excited to introduce support for volumetric measurements of views, computed tables and computed files.
  
- Enhanced Source Record CSV Download
    - Users can now download all source records as CSV that have been written to the enrichment datastores.

- Tags and Notifications Moved to Left-Side Navigation
    - Users can now quickly switch between Tags, Notifications, and Data Assets through the left-side navigation.
    - Access to the Settings page is restricted to admin users.

- Last Asserted Information in Checks
    - The `Created Date` information has been replaced with `Last Asserted` to improve visibility.
    - Users can hover over an info icon to view the `Created Date`.

- Auto-Generated Description in Check Template Dialog
  - Descriptions are now automatically generated in the Template Dialog based on the rule type, ensuring consistency with the check form.

- Exposed Properties in Profile and Scan Operations
    - Profile and scan operations now expose properties when listed:
        - Record Limit
        - Infer As Draft
        - Starting Threshold
        - Enrichment Record Limit

#### General Fixes

- Fixed a bug where the container list would not update when a user created a computed container.
- Fixed an issue where deactivated users were not filtered on the Settings page under the Security tab.
- Improved error messages when operations fail.
- Fixed a bug where the `Last Editor` field was empty after a user was deactivated by an admin.
- General Fixes and Improvements.

### 2024.9.10 { id=2024.9.10 }

#### Feature Enhancements

- Add Source Datastore Modal
    - Enhanced text messages and labels for better clarity and user experience.

- Add Datastore
    - Users can now add a datastore directly from the Settings page under the Connections tab, simplifying connection management.

#### General Fixes

- General Fixes and Improvements

### 2024.9.6 { id=2024.9.6 }

#### Feature Enhancements

- Introducing Bulk Activation on Draft Checks
    - Users can now activate and validate multiple draft checks at once, streamlining the workflow and reducing manual effort.

#### General Fixes

- Improved error message for BigQuery temporary dataset configuration exceptions.

- Added a retry operation for Snowflake when no active warehouse is selected in the current session.

- General Fixes and Improvements

#### Breaking Changes

- API fields (`type` and `container_type`) are now mandatory in request payloads where they were previously optional.
    - POST /global-tags: `type` is now required.
    - PUT /global-tags/{name}: `type` is now required.
     - POST /containers: `container_type` is now required.
    - PUT /containers/{id}: `container_type` is now required.
    - POST /operations/schedule: `type` is now required.
    - PUT /operations/schedule/{id}: `type` is now required.
    - POST /operations/run: `type` is now required.

### 2024.9.3 { id=2024.9.3 }

#### Feature Enhancements

- Introducing Catalog Scheduling
    - Users can now schedule a Catalog operation like Profile and Scan Operations, allowing automated metadata extraction.

#### General Fixes

- General Fixes and Improvements

### 2024.8.31 { id=2024.8.31 }

#### Feature Enhancements

- New Draft Status for Checks
    - Introduced a new 'draft' status for checks to enhance lifecycle management, allowing checks to be prepared and reviewed without impacting scan operations.
    - Validation is only applied to active checks, ensuring draft checks remain flexible for adjustments without triggering automatic validations.

- Introduce Draft Check Inference in Profile Operations
    - Added a new option to infer checks as drafts, offering more flexibility during data profiling.

- Improve Archive Capabilities for Checks and Anomalies
    - Enhanced the archive capabilities for both checks and anomalies, allowing recovery of archived items.
    - Introduced a hard delete option that allows permanent removal of archived items, providing greater control over their management.
    - The Anomaly statuses 'Resolved' and 'Invalid' are now treated as archived states, aligning with the consistent approach used for checks.

- Introduce a new Volumetric Check
    - Introduced the Volumetric Check to monitor and maintain data volume stability within a specified range. This check ensures that the volume of data assets does not fluctuate beyond acceptable limits based on a moving daily average.
    - Automatically inferred and maintained by the system for daily, weekly, and monthly averages, enabling proactive management of data volume trends.

- Incremental Identifier Warning in Scan Dialog
    - Enhanced the dialog to notify users when they attempt an incremental scan on containers lacking an incremental identifier, ensuring transparency and preventing unexpected full scans.

#### General Fixes

- Improve enrichment writes with queuing all writes (up to a queue threshold) for the entire scan operation. This will dramatically reduce the number of write operations performed.

- Explicit casting to avoid weak CSV parser support for typing.

- General Fixes and Improvements

### 2024.8.19 { id=2024.8.19 }

#### Feature Enhancements

- Enhance Auto-Refresh Mechanism on Tree View
    - The datastore and container tree footers are now automatically refreshed after specific actions, eliminating the need for manual page refreshes.

- Support Oracle Client-Side Encryption
    - Connections with Oracle now feature end-to-end encryption. Database connection encryption adds an extra layer of protection, especially for transmissions over long-distance, insecure channels.

#### General Fixes

- UI Label on Explore Page
    - Fixed an issue where the labels on the Explore page did not change based on the selected time frame.

- Inferred Field Type Enhancements
    - Behavior updated to infer field types at data load time rather than implicitly cast them to latest profiled type. This change supports more consistent expected schema verification for delimited file types and resolves issues when comparing inferred fields to non-inferred fields in some rule types.

- Boolean Type Inference
    - Behavior updated to align boolean inference with Spark Catalyst so that profiled types are more robustly handled during Spark based comparisons

- General Fixes and Improvements

### 2024.8.10 { id=2024.8.10 }

#### Feature Enhancements

- Introducing Profile Inference Threshold
    - This feature allows users to adjust which check types will be automatically created and updated during data profiling, enabling them to manage data quality expectations based on the complexity of inferred data quality rules.
- Anomaly Source Records Retrieval Retry Option
    - Enabled users to manually retry fetching anomaly source records when the initial request fails.

#### General Fixes

- General Fixes and Improvements

### 2024.7.31 { id=2024.7.31 }

#### Feature Enhancements

- Introducing Field Count to the Datastore Overview
    - This enhancement allows users to easily view the total number of fields present in a datastore across all containers.

- Search Template
    - Added a check filter to the templates page.
    - Added a template filter to the checks page in the datastore context and explore.

- Driver Free Memory
     - Added driver free memory information on the Health Page.

- Anomalous Record Count to the Anomaly Sidebar Card
     - Added the anomalous record count information to the anomaly sidebar card located under the Scan Results dialog.

#### General Fixes

- Enhanced write performance on scan operations with enrichment and relaxed hard timeouts.

- Updated Azure Blob Storage connector to use TLS encrypted access by default.

- Overview Tab is not refreshing asset details automatically.

- General Fixes and Improvements

### 2024.7.26 { id=2024.7.26 }

#### Feature Enhancements

- Introducing Event Bus for Extended Auto-Sync with Data Catalog Integrations
    - We are excited to expand our auto-sync capabilities with data catalog integrations by implementing an event bus pattern.
    - Added functionality to delete any DQ values that do not meet important checks.
    - Included support for a WARNING status in the Alation Data Health tab for checks that have not been asserted yet.

- Add Autocomplete to the Notification Form
    - Improved the notification message form by implementing autocomplete. Users can now easily include internal variables when crafting custom messages, streamlining the message creation process.

- Redesign the Analytics Engine Functions
    - The functions are now accessible through a menu, which displays the icon and full functionality.
    - Added a modal to alert users before proceeding with the restart. The modal informs users that the system will be unavailable for a period during the restart process.

- Improve Qualytics metadata presentation in Alation
    - Previously, multiple custom fields were used to persist data quality metrics measured by Qualytics. This process has been simplified by consolidating the metrics into a single rich text custom field formatted in HTML, making it easier for users to analyze the data.

#### General Fixes

- Normalize Enrichment Internal Containers
    - To improve user recognition and differentiate between our internal tables and those in source systems, we now preserve the original case of table names.

- Validation Error on Field Search Result
    - Resolved the logic for cascade deletion of dependencies on containers that have been soft deleted, ensuring proper handling of related data.

- Members Cannot Add Datastore on the Onboarding Screen
    - Updated permissions so that members can no longer add Datastores during the onboarding process. Only Admins now have this capability.

- General Fixes and Improvements

### 2024.7.19 { id=2024.7.19 }

#### Feature Enhancements

- Global Search
    - We are thrilled to introduce the “Global Search” feature into Qualytics! This enhancement is designed to streamline the search across the most crucial assets: Datastores, Containers, and Fields. It provides quick and precise search results, significantly improving navigation and user interaction.
    - Navigation Update: To integrate the new global search bar seamlessly, we have relocated the main menu icons to the left side of the interface. This adjustment ensures a smoother user experience.
- Teradata Connector
    - We’ve expanded our connectivity options by supporting a new connection with Teradata. This enhancement allows users to connect and interact with Teradata databases directly from Qualytics, facilitating more diverse data management capabilities.
- Snowflake Key-pair Authentication
    - In our ongoing efforts to enhance security, we have implemented support for Snowflake Key-pair authentication. This new feature provides an additional layer of security for our users accessing Snowflake, ensuring that data transactions are safe and reliable.

#### General Fixes

- General Fixes and Improvements

### 2024.7.15 { id=2024.7.15 }

#### Feature Enhancements

- Alation Data Catalog Integration
    - We're excited to introduce integration with Alation, enabling users to synchronize and manage assets across both Qualytics and Alation.
    - Metadata Customization:
        - Trust Check Flags: We now support warning flags at both the container and field levels, ensuring users are aware of deprecated items.
        - Data Health: Qualytics now pushes important checks to Alation's Data Health tab, providing a comprehensive view of data health at the container level.
        - Custom Fields: Quality scores and related metadata are pushed under a new section in the Overview page of Alation. This includes quality scores, quality score factors, URLs, anomaly counts, and check counts.

- Support for Never Expiration Option for Tokens
    - Users now have the option to create tokens that never expire, providing more flexibility and control over token management.

#### General Fixes

- General Fixes and Improvements

### 2024.7.5 { id=2024.7.5 }

#### Feature Enhancements

- Enhanced Operations Listing Performance
    - Optimized the performance of operations listings and streamlined the display of container-related information dialogs. These enhancements include improved handling of operations responses and the addition of pagination for enhanced usability

#### General Fixes

- Fix Computed Field Icon Visibility
    - Resolved an issue where the computed field icon was not being displayed in the table header.

- General Fixes and Improvements

### 2024.6.29 { id=2024.6.29 }

#### Feature Enhancements

- Computed Field Support
    - Introduced computed fields allowing users to dynamically create new virtual fields within a container by applying transformations to existing data.
    - Computed fields offer three transformation options to cater to various data manipulation needs. Each transformation type is designed to address specific data characteristics:
        - Cleaned Entity Name: Automates the removal of business signifiers such as 'Inc.' or 'Corp.' from entity names, simplifying entity recognition.
        - Convert Formatted Numeric: Strip formatting like parentheses (for negatives) and commas (as thousand separators) from numeric data, converting them into a clean, numerically-typed format.
        - Custom Expression: Allows users to apply any valid Spark SQL expression to combine or transform fields, enabling highly customized data manipulations.
    - Users can define specific checks on computed fields to automatically detect anomalies during scan operations.
    - Computed fields are also visible in the data preview tab, providing immediate insight into the results of the defined transformations.

- Autogenerated Descriptions for Authored Checks
    - Implemented an auto-generation feature for check descriptions to streamline the check authoring process. This feature automatically suggests descriptions based on the selected rule type, reducing manual input and simplifying the setup of checks.

- Event-Driven Catalog Integrations and Sync Enhancements
    - Enhanced the Atlan integration and synchronization functionalities to include event-driven support, automatically syncing assets during Profile and Scan operations. This update also refines the Sync and Integration dialogs, offering clearer control options and flexibility.

- Sorting by Anomalous Record Count
    - Added a new sorting filter in the Anomalies tabs that allow users to sort anomalies by record count, improving the manageability and analysis of detected anomalies.

- Refined Tag Sorting Hierarchy:
    - Updated the tag sorting logic to consistently apply a secondary alphabetical sort by name. This ensures that tags will additionally be organized by name within any primary sorting category.


#### General Fixes

- Profile Operation Support for Empty Containers
    - Resolved an issue where profiling operations failed to record fields in empty containers. Now, fields are generated even if no data rows are present.

- Persistent Filters on the Explore Page
    - Fixed a bug that caused Explore to disable when switching tabs on the Explore page. Filters now remain active and consistent, enhancing user navigation and interaction.

- Visibility of Scan Results Button
    - Corrected the visibility issue of the 'results' button in the scan operation list at the container level. The button now correctly appears whenever at least one anomaly is detected, ensuring users have immediate access to detailed anomaly results.

- General Fixes and Improvements

### 2024.6.18 { id=2024.6.18 }

#### Feature Enhancements

- Improvement to Anomaly Dialog
    - Enhanced the anomaly dialog to include a direct link to the operation that generated the anomaly. Users can now easily navigate from an anomaly to view other anomalies generated by the same operation directly from the Activity tab.
  
- Sorting by Duration in Activity Tab
    - Introduced the ability to sort by the duration of operations in the Activity tab by ascending or descending order.
  
- Last Editor Information for Scheduled Operations
    - Added visibility of which users have created or last updated scheduled operations, enhancing traceability in scheduling management.

- Display Total Anomalous Records for Anomalies
     - Added the total count of anomalous records in the anomalies listing view.

#### General Fixes

- Performance Fixes on Computed Table Creation and Check Validation
    - Optimized the processes for creating computed tables and validating checks. Users previously experiencing slow performance or timeouts during these operations will now find the processes significantly faster and more reliable.

- General Fixes and Improvements

### 2024.6.14 { id=2024.6.14 }

#### Feature Enhancements

- Improvements to Atlan Integration
    - When syncing Qualytics with Atlan, badges now display the "Quality Score Total," increasing visibility and emphasizing key data quality indicators on Atlan assets.

    - Improved performance of the synchronization operation.

    - Implemented the propagation of external tags to checks, now automatically aligned with the container synchronization process, enabling better accuracy and relevance of data tagging.

- Refactor Metric Check Creation
     - Enhanced the encapsulated Metric Check creation flow to improve user experience and efficiency. Users can now seamlessly create computed tables and schedule operations simultaneously with the metric check creation.

- Support Update of Weight Modifier for External Tags

- Add Validation on Updated Connections
    - Added support for testing the connection if there's at least one datastore attached to the connection, ensuring more reliable and accurate connection updates.

- Standardize Inner Tabs under the Settings Page
    - Tags and Notifications Improvements: The layout has been revamped for better consistency and clarity. General headers have been removed, and now each item features specific headers to enhance readability.

    - Security Tab Improvements: The redesign features chip tabs for improved navigation and consistency. Filters have been updated to ensure they meet application standards.
    
    - Tokens Tab Accessibility: Moved the action button to the top of the page to make it more accessible.
    
    - Refine Connector Icons Display: Improved the display of connector icons for Datastores and Enrichments in the Connections Tab.

- Streamlined Container Profiling and Scanning
    - In the container context, the profile and scan modals have been updated to automatically display the datastore and container, eliminating the need for a selection step and streamlining the process.

- Swap Order During Check Creation
    - Rule Type Positioning: The Rule Type now appears before the container selection, making the form more intuitive.
    
    - Edit Mode Header: In edit mode, the Rule Type is prominently displayed in the modal header, immediately under the check ID.

#### General Fixes

- Address Minor Issues in the Datastore Activity Page
    - Operation ID Auto-Search: Restored the auto-search feature by operation ID for URL access, enhancing navigation, especially for Catalog Operations.
    
    - Tree View Auto-Refresh: Implemented an auto-refresh feature for the tree view, which activates after any operation in the CTA flow (Catalog, Profile, Scan).

- Fix "Greater Than Field" Quality Check
    - Corrected the inclusive property of the greater than field quality check.
- Fix Exporting Field Profiles for Non-Admin User with Write Permission
    - Resolved issues for non-admin users with write permissions to allow proper exporting of field profile metadata to enrichment.
    
- Fix "Is Replica Of" Quality Check validation on Field Names with Special Characters
    - Improved validation logic to handle field names with special characters
    
- General Fixes and Improvements

### 2024.6.7 { id=2024.6.7 }

#### Feature Enhancements

- Atlan Integration Improvements
    - Enhanced the Atlan assets fetch and external tags syncing. 
    - Added support for external tag propagation to checks and anomalies. 
    - Merged Global and External tags section for streamlined tag management.

- Restart Button for Analytics Engine
    - Introduced a new "Restart" button under the Settings - Health section, allowing admins to manually restart the Analytics Engine if it is offline or unresponsive.

- Interactive Tooltip Component
    - Added a new interactive tooltip component that remains visible upon hovering, enhancing user interaction across various modules of the application.
    - Refactored existing tooltip usage to integrate this new component for a more consistent user experience.

- Defaulting to Last-Used Enrichment Datastore for Check Template Exports
    - Improved user experience by persisting the last selected enrichment datastore as the default option when exporting a check template.

#### General Fixes

- Shared Links Fixes
    - Fixed issues with shared operation result links, ensuring that dialogs for scan/profile results and anomalies now open correctly.
    - Addressed display inaccuracies in the "Field Profiles Updated" metrics.

- General Fixes and Improvements

### 2024.6.4 { id=2024.6.4 }

#### Feature Enhancements

- Atlan Data Catalog Integration
    - We're excited to introduce integration with Atlan, enabling users to synchronize and manage assets across both Qualytics and Atlan:
        - Tag Sync: Sync tags assigned to data assets in Atlan with the corresponding assets in Qualytics, enabling tag-based quality score reporting, notifications, and bulk data quality operations using Atlan-managed tags.
        - Metadata Sync: Automatically synchronize Atlan with Qualytics metadata, including asset URL, total score, and factor scores such as completeness, coverage, conformity, consistency, precision, timeliness, volume, and accuracy.

- Entity Resolution Check
    - We've removed the previous limitation on the maximum number of distinct entity names that could be resolved with the Entity Resolution rule type. This release includes various performance enhancements that support an unlimited number of entity names.

- Enhancements to Catalog Operation Results
    - We've improved the catalog operation results by now including detailed information on whether tables, views, or both were involved in each catalog operation.

- Enhancements to 'Equal to Field' Rule Type
    - The 'Equal to Field' rule now supports string values, allowing for direct comparisons between text-based data fields.

- Enhancements to Enrichment
    - Qualytics now includes a property for anomalousRecordCount on shape anomaly, which previously was neither populated nor persisted. This aims to accurately capture and record the total number of anomalous records identified in ShapeAnomaly, regardless of the max_source_records threshold.

- Dynamic Meta Titles
    - Pages such as Datastore Details, Container Details, and Field Details now feature dynamic meta titles that accurately describe the page content and are visible in browser tabs providing better searchability.

#### General Fixes

- Fix Trends of Quality Scores on the Insights Page
    - Addressed issues with displaying trends on the Insights page. Trends now accurately reflect changes and comparisons to the previous report period, providing more reliable and insightful analytics.

- Resolved a bug in Entity Resolution where the distinction constraint was only applied to entity names that differed.
  
- General Fixes and Improvements

### 2024.5.22 { id=2024.5.22 }

#### Feature Enhancements

- Datastore Connection Updates:
    - Users can now update the connection on a datastore if the new one has the same type as the current one.

- Enrichment Datastore Redirection:
    - Enhanced the user interface to facilitate easier redirection to enrichment datastores, streamlining the process and improving user experience.

- Label Enhancements for Data Completeness:
    - Updated labels to better distinguish between completeness percentages and Factor Scores. The label for completeness percentage has been changed to provide clear context when viewed alongside.

#### General Fixes

- Rule Type Anomaly Corrections:
    - Fixed an issue where the violation messages for record anomalies incorrectly included "None" for some rule types. This update ensures accurate messaging across all scenarios.

- Shape Anomaly Logic Adjustment:
    - Revised the logic for Shape Anomalies to prevent the combination of failed checks for high-count record checks on the same field. This change ensures that displayed sample rows have definitively failed the specific checks shown, enhancing the accuracy of anomaly reporting.

- Entity Resolution Anomalies:
    - Addressed an inconsistency where some Entity Resolution Checks did not return source records. Ongoing investigations and fixes have improved the reliability of finding source records for entity resolution checks across DFS and JDBC datastores.

- General Fixes and Improvements


### 2024.5.16 { id=2024.5.16 }

#### Feature Enhancements

- Entity Resolution Check
    - Introduced rule "Entity Resolution" to determine if multiple records reference the same real-world entity. This feature uses customizable fields and similarity settings to ensure accurate and tailored comparisons.

- Support for Rerunning Operations
    - Added an option to rerun operations from the operations listing, allowing users to reuse the configuration from previously executed operations.

#### General Fixes

- Export Operations
    - Fixed metadata export operations silently failing on writing to the enrichment datastores.

- Computed File/Table Creation
    - Resolved an issue that prevented the creation of computed files/tables with the same name as previously deleted ones, even though it is a valid action.

- General Fixes and Improvements

### 2024.5.13 { id=2024.5.13}

#### General Fixes

- Enhanced Quality Score Factors Computation
	- Addressed issues in quality score calculation and its associated factors ensuring accuracy

- General Fixes and Improvements

### 2024.5.11 { id=2024.5.11}

#### Feature Enhancements

- Introducing Quality Score Factors
	- This new feature allows users to control the quality score factor weights at the datastore and container levels.
		- Quality Score Detail Expansion: Users can now click on the quality score number to expand its details, revealing the contribution of each factor to the overall score. This enhancement aids in understanding what drives the quality score.
		- Insights Page Overhaul: The Insights page has been restructured to better showcase the quality score breakdown. This redesign aims to make the page more informative and focused on quality score metrics.
		- Customization of Factor Weights: Users can now customize the weights of different factors at the Datastore and Container levels. This feature is essential for adapting the quality score to meet specific user needs, such as disregarding the Timeliness factor for dimensional tables where it might be irrelevant.
		- Enhanced Inferred Checks: Introduced a new property in the Check Listing schema and a feature in the Check modal that displays validity metrics, which help quantify the accuracy of inferred checks. A timezone handling issue in the last_updated property of the Check model has also been addressed.

- Quality Score UI Enhancements
	- Enhancements have been made to the user interface to provide a clearer and more detailed view of the quality score metrics, including Completeness, Coverage, Conformity, Consistency, Precision, Timeliness, Volumetrics, and Accuracy. These changes aim to provide deeper insight into the components that contribute to the overall quality score.

#### General Fixes

- Fixes to JDBC Incremental Support
	- Updated the conditional logic in the catalog operation for update tables to ensure the incremental identifier is preserved if already established.

- General Fixes and Improvements

### 2024.5.2 { id=2024.5.2}

#### Feature Enhancements

- Datastore Connections:
    - Users can now create connections that can be shared across different datastores. This introduces a more flexible approach to managing connections, allowing users to streamline their workflow and reduce duplication of effort. With shared connections, users can easily reuse common elements such as hostname and credentials across various datastores, enhancing efficiency and simplifying management.

- File Container Header Configuration:
    - Adds support for setting the hasHeader boolean property on File Containers, enabling users to specify whether their flat file data sources include a header row. This enhances compatibility and flexibility when working with different file formats.

- Improved Error Handling in Delete Dialogs:
    - Error handling within delete dialogs has been revamped across the application. Error messages will now be displayed directly within the dialog itself, providing clearer feedback and preventing misleading success messages in case of deletion issues.

#### General Fixes

- Locked Template Field Editing:
    - Resolves an issue where selecting a new container in the check form would reset check properties, causing problems for locked templates. The fix ensures that checks derived from templates retain their properties, allowing users to modify the field_to_compare field as needed.

- General Fixes and Improvements

### 2024.4.25 { id=2024.4.25}

#### Feature Enhancements

- Profile Results Modal:
    - Introducing a detailed Results Modal for each profile operation. Users can now view comprehensive statistics about the produced container profiles and their partitions, enhancing their ability to analyze data effectively.

- Checks Synchronized Count:
    - The operations list now includes the count of synchronized checks for datastore and explore operations. This addition streamlines the identification of operations, improving user experience.

#### General Fixes

- General Fixes and Improvements

### 2024.4.23 { id=2024.4.23}

#### Feature Enhancements

- Introduction of Comparators for Quality Checks:
    - Launched new Comparator properties across several rule types, enhancing the flexibility in defining quality checks. Comparators allow users to set margins of error, accommodating slight variations in data validation:
        - Numeric Comparators: Enables numeric comparisons with a specified margin, which can be set as either a fixed absolute value or a percentage, accommodating datasets where minor numerical differences are acceptable.
        - Duration Comparators: Supports time-based comparisons with flexibility in duration differences, essential for handling time-based data with variable precision.
        - String Comparators: Facilitates string comparisons by allowing for variations in spacing, ideal for textual data where minor inconsistencies may occur.
    - Applicable to rule types such as Equal To, Equal To Field, Greater Than, Greater Than Field, Less Than, Less Than Field, and Is Replica Of.

- Introduced Row Comparison in the isReplicaOf Rule:
    - Improved the rule to support row comparison by id, enabling more precise anomaly detection by allowing users to specify row identifiers for unique row comparison. Key updates include:
        - Revamp of the source record presentation to highlight differences between the left and right containers at the cell level, enhancing visibility into anomalies.
        - New input for specifying unique row identifiers, transitioning from symmetric difference to row comparison when set.
        - The original behavior of symmetric comparison remains unchanged if no row identifiers are provided.

- New equalTo Rule Type for Direct Value Comparisons
    - Introduced the equalTo rule type, enabling precise assertions that selected fields match a specified value. This new rule not only simplifies the creation of checks for constant values across datasets but also supports the use of comparators, allowing for more flexible and nuanced data validation.

- Redirect Links for Requested Containers in Operation Details:
    - Introduced redirect links in the "Containers Requested" section of operation results. This enhancement provides direct links to the requested containers (such as tables or files), facilitating quicker navigation and streamlined access to relevant operational data.

- Enhanced Description Input with Expandable Option:
    - Implemented an expandable option for the Description input in the Check Form & Template Form. This enhancement allows users to more comfortably manage lengthy text entries, improving the usability of the form by accommodating extensive descriptions without compromising the interface's usability.

#### General Fixes

- Addressed Data Preview Timeout Issues:
    - Tackled the timeout problems in the data preview feature, ensuring that data retrieval processes complete successfully within the new extended timeout limits.

- General Fixes and Improvements

### 2024.4.12 { id=2024.4.12}

#### Feature Enhancements

- File Pattern Overrides:
    - We have added support in the UI to override a file pattern. Now, a file pattern overwritten by a user will replace the one that the system generated during the first catalog. To have a new file pattern in the UI, users need to perform a new catalog operation without prune.
- Batch Edit in the Check Templates Library::
    - We are now supporting batch edits for check templates in the Library. This enhancement will allow filters and tags.
- Improved Presentation of Incremental, Remediation, and Infer Constraints:
    - We have improved the presentation of Incremental, Remediation, and Infer Constraints in the operation listing for catalog, profile, and scan operations. The Incremental, Remediation, and Infer Constraints icons have been added to the list of items, and the visualization of these items has been enhanced.
- Default Placeholders for Computed File in UI:
    - We are now automatically populating the form dialog with fields from the selected container. This improvement simplifies the process for users, especially in scenarios where they wish to select or cast specific fields directly from the source container.

#### General Fixes

- Tree View Default Ordering:
    - We have updated the tree view default ordering. Datastore names are now grouped and presented in alphabetical order.

- General Fixes and Improvements

### 2024.4.6 { id=2024.4.6 }

#### Breaking Changes

- Remediation Naming Convention Update:
    - Updated the naming convention for remediation to `{enrich_container_prefix}_remediation_{container_id}`, standardizing remediation identifiers.

- Add file extension for DFS Enrichment:
    - Introduced `.delta` extension to files in the enrichment process on DFS, aligning with data handling standards.

#### Feature Enhancements

- Revamp Enrichment Datastore Main Page:
    - Tree View & Data Navigation: Enhanced the enrichment page with an updated tree view that now lists source datastores linked to enrichment datastores, improving navigability. A newly introduced page for enrichment datastore enables:
        - Data preview across enrichment, remediation, and metadata tables with the ability to apply "WHERE" filters for targeted insights.
        - Direct downloading of preview data as CSV.
    - UI Performance Optimization: Implemented UI caching to boost performance, reducing unnecessary network requests and smoothly preserving user-inputted filters and recent data views.

- User Sorting by Role:
    - Introduced a sorting feature in the Settings > Users tab, allowing users to be sorted by their roles in ascending or descending order, facilitating easier user management.

- Expanded Entity Interaction Options:
    - Enhanced entity lists and breadcrumbs with new direct action capabilities. Users can now right-click on an item to access useful functions: copy the entity's ID or name, open the entity's link in a new tab, and copy the entity's link. This enhancement simplifies data management by making essential actions more accessible.

#### General Fixes

- Record Quality Scores Overlap Correction:
    - Resolved a problem where multiple violations could be open for the same container simultaneously, contrary to logic. This fix ensures violations for containers are uniquely recorded, eliminating parallel open violations.

- Anomaly Details Text Overflow:
    - Corrected text overflow issues in the anomaly details' violation box, ensuring all content is properly contained and readable.

- Enhanced "Not Found" Warnings with Quick Filters:
    - Improved user guidance for Checks and Anomalies list filters by adding hints for "not found" items, suggesting users check the "all" group for unfiltered search results, clarifying navigation and search results.

- General Fixes and Improvements

### 2024.3.29 { id=2024.3.29}

#### Feature Enhancements

- Data Preview
    - Introducing the "Data Preview" tab, providing users with a streamlined preview of container data within the platform. This feature aims to enhance the user experience for tasks such as debugging checks, offering a grid view showcasing up to 100 rows from the container's source.
        - Data Preview Tab: Implemented a new tab for viewing container data, limited to displaying a maximum of 100 rows for improved performance.
        - Filter Support: Added functionality to apply filter clauses to the data preview, enabling users to refine displayed rows based on specific criteria.
        - UI Caching: Implemented a caching layer within the UI to enhance performance and reduce unnecessary network requests, storing the latest refreshed data along with applied filters.

- Enhanced Syntax Highlight Inputs
    - Improved the syntax highlight inputs for seamless inline editing, minimizing the friction of entering expressions. This feature includes a dual-mode capability, allowing users to type directly within the input field or utilize an expanded dialog for more complex entries, significantly improving user experience.

- Volumetric Measurements
    - Periodically measure container volumetrics for a more robust approach. This update focuses on measuring only containers without a volume measure in the last 24 hours and scheduling multiple runs of the job daily.

- Sort Tags by Color
    - Users can now sort tags by color, visually grouping similar colors for easier navigation and management.

- Download Source Records
    - Added a "Download Source Records" feature to the Anomaly view in the UI, allowing users to export data held in the enrichment store for that anomaly in CSV format.

- Check Templates Navigation
    - Implemented a breadcrumb trail for the Check Template page to improve user navigation.

#### General Fixes

- Fix Scheduling Issues
    - Resolved scheduling issues affecting specific sets of containers, particularly impacting scheduled profile and scan operations. Users must manually add new profiles after catalog operations or computed file/table creation for inclusion in existing scheduled operations.

- Fix Notifications Loading Issue on Large Screens
    - Fixed an issue where the infinity loading feature for the user notification list was not functioning properly on large screens. The fix ensures correct triggering of infinity loading regardless of screen size, allowing all notifications to be accessed properly.

- General Fixes and Improvements

### 2024.3.15 { id=2024.3.15}

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

- General Fixes and Improvements

### 2024.3.7 { id=2024.3.7}

#### General Fixes

- Corrected MatchesPattern Checks Inference:
    - Fixed an issue where the inference engine generated MatchesPattern checks that erroneously asserted false on more than 10% of training data. This resolution ensures all inferred checks now meet the 99% coverage criterion, aligning accurately with their training datasets.

- Fixed Multi-Field Check Parsing Error in DFS:
    - Addressed a bug in DFS environments that caused parsing errors for checks asserting against multiple fields, such as AnyNotNull and NotNull, when selected fields contained white spaces. This resolution ensures that checks involving multiple fields with spaces are now accurately parsed and executed.

- Volumetric Measurements Tracking Fix:
    - Addressed a bug that prevented the recording of volumetric measurements for containers without a last modified time. This fix corrects the problem by treating last_modification_time as nullable, ensuring that containers are now accurately tracked for volumetric measurements regardless of their modification date status.

- General Fixes and Improvements

### 2024.3.5 { id=2024.3.5}

#### Feature Enhancements

- Check Validation Improvement:
    - Enhanced the validation process for the "Is Replica Of" check. Previously, the system did not validate the field name and type, potentially leading to undetected issues until a Scan Operation was executed. Now, the validation process includes checking the field name and type, providing users with immediate feedback on any issues.

#### General Fixes

- Matches Pattern Data Quality Check Handling White Space:
    - Resolved a bug in the Matches Pattern data quality check that caused white space to be ignored during training. With this fix, the system now accounts for white space during training, ensuring accurate pattern inference even with data containing significant white space. If 1% or more of the training data contains blanks, the system will derive a pattern that includes blanks as a valid value, improving data quality assessment.

- General Fixes and Improvements

### 2024.2.28 { id=2024.2.28 }

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

- General Fixes and Improvements

### 2024.2.23 { id=2024.2.23 }

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

- General Fixes and Improvements

### 2024.2.19 { id=2024.2.19 }

#### Feature Enhancements

- Support for exporting Check Templates to the Enrichment Datastore:
    - Added the ability to export Check Library metadata to the enrichment datastore. This feature helps users export their Check Library, making it easier to share and analyze check templates.

- File Upload Size Limit Handling:
    - Implemented a user-friendly error message for file uploads that exceed the 20MB limit. This enhancement aims to improve user experience by providing clear feedback when the file size limit is breached, replacing the generic error message previously displayed.

#### General Fixes

- Resolved Parsing Errors in Expected Values Rule:
    - Fixed an issue where single quotes in the list of expected values caused parsing errors in the Analytics Engine, preventing the Expected Values rule from asserting correctly. This correction ensures values, including those with quotes or special characters, are now accurately parsed and asserted.

- General Fixes and Improvements

### 2024.2.17 { id=2024.2.17}

#### General Fixes

- Corrected Typing for Expected Values Check:
    - Resolved an issue with the expectedValues rule, where numeric comparisons were inaccurately processed due to a misalignment between the API and the analytics engine. This fix ensures numeric values are correctly typed and compared, enhancing the reliability of validations.

- Fixed Anomaly Filtering in Scan Results dialog:
    - Addressed a flaw where scan results did not consistently filter anomalies based on the operation ID. The fix guarantees that anomalies are only displayed once the operation ID parameter is accurately defined in the URL, ensuring more precise and relevant scan outcome presentations.

- Check Validation Sampling Behavior Adjustment:
    - Fixed intermittent validation issues encountered in specific source datastore types (DB2, Microsoft SQL Server). The problem, where validation could unpredictably fail or succeed based on container size, was corrected by fine-tuning the sampling method for these technologies, leading to consistent validation performance.

- General Fixes and Improvements

### 2024.2.15 { id=2024.2.15}

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

- General Fixes and Improvements

### 2024.2.10 { id=2024.2.10}

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

- General Fixes and Improvements

### 2024.2.2 { id=2024.2.2}

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

- General Fixes and Improvements

### 2024.1.30 { id=2024.1.30}

#### Feature Enhancements

- Enhanced External Scan Operations:
    - Improved data handling in External Scans by applying type casting to uploaded data using Spark. This update is particularly significant for date-time fields, which now expect and conform to ISO 8601 standards.

- Optimized DFS File Reading:
    - Streamlined file reading in DFS by storing and utilizing the 'file_format' identified during the Catalog operation. This change eliminates the need for repeated format inspection on each read, significantly reducing overhead, especially for partitioned file types.

#### General Fixes

- Resolved DFS Reading Issues with Special Character Headers:
    - Fixed a DFS reading issue where columns with headers containing special characters (like pipes |) adversely affected field profiling, including inaccuracies in histogram generation.

- General Fixes and Improvements

### 2024.1.26 { id=2024.1.26}

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

- General Fixes and Improvements

### 2024.1.23 { id=2024.1.23}

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

- General Fixes and Improvements

### 2024.1.11 { id=2024.1.11}

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

- General Fixes and Improvements

### 2024.1.4 { id=2024.1.4}

#### Feature Enhancements

- Enhanced Warnings for Schema Inconsistencies in Files Profiled
    - Improved the warning message for cases where the user profiles files with different schemas under a single glob pattern. This update ensures users receive clear, helpful information when files within a glob have inconsistent structures.

#### General Fixes

- Containers with 'Group By' settings Leading to Erroneous Profile Operation
    - Fixed an issue affecting profile operations which included containers with 'Group By' settings. Previously, running a profile without inferring checks resulted in all fields being erroneously removed from the field list.

- General Fixes and Improvements