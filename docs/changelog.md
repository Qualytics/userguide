# 2025

## Release Notes

### 2025.9.12 { id=2025.9.12 }

#### Feature Enhancements

- We are thrilled to introduce the Profiles Over Time for tracking field-level data changes
    - Users can now compare the current field profile with previous profiles to track changes.
    - Visual indicators highlight metrics that changed between selected profiles.
    - Interactive charts display numeric metric trends across profile history.
    - Easily identify data drift and type changes at the field level.
    - Special badges indicate when field types have changed between profiles.

- Introducing the `Data Diff` check as an enhancement of the Is Replica Of functionality.

- Enhanced File Profile visibility with file format display and improved handling of long names with tooltips.

- Improved hover contrast for list items in light mode for better visibility.

- Optimized slim profile logic to protect existing field typing from being overwritten by limited data samples.

- Added OAuth support to the Databricks connector.

#### General Fixes and Improvements

- Fixed broken enrichment datastore redirect link in the datastore tree footer.

- Corrected filter application in `Exists In` checks that was causing inaccurate anomaly detection.

- Fixed grouped inference checks to properly validate against filtered test data for each group combination.

- Resolved `Is Address` check failing to assert during scan.

- Removed `User Defined Function` check support.

- General Fixes and Improvements.

### 2025.9.4 { id=2025.9.4 }

#### Feature Enhancements

- Introducing Product Updates
    - Users can now view feature announcements directly within the application.
    - Read full posts by clicking the external link for each update.

- Enhanced filter clause display in readonly checks with copy functionality and improved text formatting.

#### General Fixes and Improvements

- Resolved an issue where the API allowed creation of quality checks with string fields for rules that don't support them.

- Corrected cache logic to avoid unnecessary data refresh in insights.

- Fixed input field overflow when entering long filter values that caused UI layout issues.

- Fixed Data Preview errors when filters return no records, now properly displays empty results instead of failing with a server error.

- Fixed activation failures for Exists In checks that reference computed fields.

- Fixed issue where rule type filter options did not appear on the check list page for Member users.

- Updated enrichment processing for more frequent and reliable data writes.

- General Fixes and Improvements.

### 2025.8.20 { id=2025.8.20 }

#### Feature Enhancements

- Introducing Bulk Quality Check Creation through Templates
    - Users can now create multiple quality checks from a single template.
    - Select multiple target containers across different datastores and apply the same template configuration.

- Announcing Pause Schedule operation
    - Users can now deactivate and reactivate schedules without losing configuration.
    - Added a new filter option to show only deactivated schedules.

- Introducing Test Connection capability for existing connections
    - Users can now verify connection changes before saving when editing a connection configurations.

- Improved isReplicaOf check to better handle incremental data comparisons.

- Added support for connecting to Kerberos-secured Hive datastores.

#### General Fixes and Improvements

- Fixed Data Preview filtering to properly indicate that computed fields are not supported in WHERE clauses and not exposing as auto complete options.

- Fixed issues related to ANSI SQL compliance in Spark 4.

- Fixed issues with nested data types in the Databricks connector.

- Corrected inconsistent formatting in operation details where containers read appeared larger than total containers.

- Resolved filter UI issues where selected items caused layout misalignment.

- General Fixes and Improvements.

### 2025.8.8 { id=2025.8.8 }

#### Feature Enhancements

- Enhanced Source Record visualization
    - Users can now view more source records with selectable limits (10, 100, 1000, or 10000 records).
    - Added sticky headers for easier navigation when scrolling through large datasets.

- Introducing Quality Check Migration
    - Users can now migrate quality checks from one container to another, even across different datastores.
        - Archived and inferred checks are excluded from migration.
    - Migrated checks are set to Draft status for users review before activation.

- Enhanced search functionality for datastores and flows
    - Users can now search by ID or name using a single search field.

#### General Fixes and Improvements

- Updated Dataplane to Spark 4

- Fixed Is Replica Of dry run validation to correctly handle filtered datasets.

- Resolved an issue where anomaly action buttons redirect to the details page instead of performing the intended action.

- Corrected the navigation issue when switching between the Checks and Observability tabs that prevented lists from rendering properly.

- General Fixes and Improvements.

#### API Changes

- The following endpoint `GET /operations` is affected:
    - Added `start_date` and `end_date` query parameters to filter operations by date range.

### 2025.7.28 { id=2025.7.28 }

#### Feature Enhancements

- Improved Spark SQL autocomplete handling for complex field names
    - SQL autocomplete now automatically adds backticks to field names, preventing errors with special characters.

#### General Fixes and Improvements

- Resolved an issue where scheduled operations were not executing reliably under high load.

- Fixed last asserted timestamp accuracy for all check types.

- General Fixes and Improvements.

### 2025.7.23 { id=2025.7.23 }

#### Feature Enhancements

- Simplified Computed Join prefix management
    - Select expressions automatically adjust when prefixes change, eliminating manual field name updates.

- Added User Guide links to Check Creation form
    - Selecting a Rule Type provides a direct link to that specific rule's documentation in the User Guide.

#### General Fixes and Improvements

- Corrected Quality Check Update errors affecting `Greater Than Field`, `Less Than Field`, and `Equal To Field` rule types.

- Fixed source record display for high-precision decimal values
    - Source records now display full decimal precision on hover for truncated numeric values.

- General Fixes and Improvements.


### 2025.7.18 { id=2025.7.18 }

#### Feature Enhancements

- Introducing Computed Join for creating new containers by joining data across different datastores
    - Users can now create computed joins between two containers, even from different datastores, enabling cross-datastore data analysis.
    - Supports multiple join types: Inner Join, Left Join, Right Join, and Full Outer Join to accommodate various data combination needs.
    - Configure joins using intuitive left and right reference selections with field mapping and optional prefixes.
    - Add custom SELECT expressions and WHERE clauses to refine the joined data output.

- Introducing Dry Run operation for draft checks

- Enhanced Bulk Check Operations and Management Capabilities
    - Added metadata field to bulk update dialog, enabling users to update metadata across multiple checks simultaneously without opening each individually.
    - Extended bulk operations to support archived checks, previously limited to active only.
    - Bulk activate and draft actions now available for archived checks, expanding beyond the previous delete-only option.

- Added Subject Field to Email Notifications
    - Email notifications now support customizable subject lines, allowing users to add meaningful context to their messages.

- Enhanced Record Limit Configuration
    - Users can now manually input custom record limit values in Profile and Scan operations, as well as Flow operations through a text field, providing flexibility beyond the predefined options.
    - A dropdown menu provides quick access to common values (1M, 10M, 100M, All).

- Adding Unlink Enrichment Datastore
    - Users can now unlink enrichment datastores directly from the "Enrichment Datastore Settings" dialog.

- Improved Datastore Deletion Experience
    - Error messages during deletion now appear directly within the confirmation dialog instead of temporary toast notifications.
    - When deleting an Enrichment Datastore, the dialog now displays the number of linked source datastores and uses clear labeling to distinguish between datastore types.

- Enhanced catalog operation to properly recognize subdirectories within partitioned file structures, ensuring more accurate container identification for complex directory hierarchies.

#### General Fixes and Improvements

- Addressed modal dismissal issues across multiple dialogs where clicking outside or pressing ESC would cause accidental closure and data loss.

- Fixed "Open in new tab" and "Copy link" actions for checks and anomalies that were not functioning correctly.

- Fixed source record formatting for 'Is Replica Of' anomalies when check configuration changes after anomaly detection.

- Fixed an issue where anomaly URLs generated from check side panels were not functioning correctly when shared.

- Fixed incorrect redirection after creating checks from templates.

- Fixed an issue where source records weren't displaying correctly during dry run operations.

- Corrected cloning behavior to preserve tags from the check being cloned.

- Fixed scan operations failing after deleting or unlinking enrichment datastores.

- Corrected failed checks information in anomaly responses to accurately reflect the historical check version at the time the anomaly was detected, rather than showing the current check version.

- General Fixes and Improvements.

### 2025.7.2 { id=2025.7.2 }

#### Feature Enhancements

- Introduced Failed Check Version display, providing visibility into the exact check configuration that triggered each anomaly.
    - Failed Check now displays the specific check properties and configuration that were active when the anomaly was generated.

- Enhanced Check Activities visualization.
    - Users can now view historical check configurations directly from the timeline, including all properties and tags as they were at that point in time.

- Enhanced flow nodes with improved visual design and contextual information display for better user experience.
    - Action nodes now show inline summaries with relevant details based on their type (e.g., datastore names for operation actions, channel names for Slack or Teams, URLs for webhooks, etc).
    - Export nodes now display asset types in their titles (e.g., "Export Anomalies").
    - Added filter tooltips to trigger nodes displaying applied conditions (tags, datastores, operation types) for quick configuration visibility.

- Supports Data Preview functionality for containers that haven't been profiled yet, removing the requirement to profile first before viewing data.

- Enhanced editing flexibility for Asserted Checks.
    - Users can now edit SparkSQL expressions that define calculated fields.
    - Row Identifiers and Passthrough Fields are now editable for Is Replica Of Check.

- Improving Computed Assets:
    - Users can now add Additional Metadata to computed Tables/files and computed fields.
    - Display the Last Editor information in the tree footer to provide context on who last modified the asset.

- Added Last Profile visibility in Field Overview and Field Details.
    - Users can now see the last time a field was profiled, helping clarify the timeframe of the metrics shown in the Profile section.

- Improved Anomaly Bulk Archive with comment support.
    - Similar to Acknowledge Anomaly, users can now add optional comments when bulk archiving anomalies.

- Improve dry run result message readability.

#### General Fixes and Improvements

- Fix a bug when user selected a date in Date Picker and this return user's timezone instead of UTC timezone.

- Fixed an issue with Metadata Checks Dry Run execution where status messages were not displaying properly.

- General Fixes and Improvements.

### 2025.6.20 { id=2025.6.20 }

#### Feature Enhancements

- Added Source Records Download for Check Dry Run: Users can now download the source records as a CSV file after executing a Dry Run.

- Improving Source Records Performance: Implemented caching for anomaly source records, significantly reducing load times and improving in user session level.

#### General Fixes and Improvements

- General Fixes and Improvements.

### 2025.6.13 { id=2025.6.13 }

#### Feature Enhancements

- Introducing Quality Check Dry Run: Users can now quickly assess the impact of a quality check without persisting results.
    - The Dry Run functionality is accessible directly from the Data Quality Check settings configuration, enabling users to test checks before scan assertion.
    - A comprehensive modal displays the execution results, presenting critical metrics including Dry Run status, operation time, and sampling limits.
    - Dedicated section display potential Anomalies and Source Records that would be generated by the check. When no issues are detected, users receive a clear confirmation message indicating no anomalies were identified.

- Enhancing Fingerprint Visualization: Users can now easily view and manage related anomalies that share the same fingerprint.
    - Clicking "View Related Anomalies" opens a right-side panel displaying all anomalies with matching fingerprints, including the total count of related anomalies.
    - The panel enables direct anomaly management, allowing users to acknowledge, archive, or click individual cards to view detailed anomaly information without navigating away.

- Introducing Sticky Navigation: Users can now maintain access to navigation elements and actions while scrolling through content-rich pages.
    - The sticky navigation feature ensures breadcrumb information and interaction buttons remain visible and accessible as users scroll down the page.

- Expanding Scan Operation Support for Iceberg Tables
    - Incremental scans now fully support Iceberg table formats, significantly expanding the range of asset types eligible for incremental scanning operations.

#### General Fixes and Improvements

- Resolved an issue where metric charts failed to display data when users accessed metric details.
- Fixed a bug that incorrectly allowed users to edit settings on computed fields inherited from parent computed files.
- Corrected the rendering logic for Authored Check Details that prevented information from displaying after tag update operations.
- General Fixes and Improvements.

### 2025.6.6 { id=2025.6.6 }

#### Feature Enhancements

- Introducing the new Quality Check dedicated page, enabling users to analyze check properties and metrics.
    - A Check Assert Visualization is provided to analyze assertions over time, helping users monitor assertion results, with the ability to hover over a timeline point to view the latest assertion and totals.
    - Displays key metrics such as Status, Rule Type, Last Asserted, Weight, Coverage, and Active Anomalies and including the check description.
    - Exposes all relevant check properties to provide a comprehensive view of each check's configuration without opening the edit modal.
    - Shows the full activity history for the check, including property updates, and exposes previous and new values when a check setting is modified.
    - Supports inline check tag editing by clicking the tag badge, allowing users to add or remove tags without opening a modal.

- Announcing the Anomaly exclusive page: This new page will allow users to get detailed information about Anomaly metrics, Failed Checks and Source Records.
    - Exposes detailed anomaly information, including Status, Anomalous Records, Total Failed Checks, Weight, Detected DateTime, and Scan Operation, as well as Source Datastore, Computed Table, and Location.
    - Lists the Failed Checks that were violated and led to the creation of the anomaly. Clicking on a failed check opens a right-side panel with the corresponding quality check information, eliminating the need to navigate to a different page.
    - Show Source Records from your data that failed the checks when available. Users can apply filters and sorting options to personalize the data display according to their preferences.
    - Displays the complete activity history, including all updates made to the anomaly over time. User comments are also shown, making it easier to follow discussions and decisions.
    - Similar to the dedicated Quality Check page, users can edit Anomaly Tags inline.

- Datastore Connection Status Visibility
    - A badge attached to the datastore icon now appears in both the breadcrumb and the tree view footer, clearly indicating the connection status of the datastore.

- Adding support for gzipped and .txt files in Catalog Operation
    - Users can now use gzipped (.gz) and .txt files in DFS Datastores for Catalog Operations.

#### General Fixes and Improvements

- General Fixes and Improvements.

### 2025.5.23 { id=2025.5.23 }

#### Feature Enhancements

- Atlan Integration
    - Users can now choose whether or not to receive notifications in the Atlan platform, giving more control over their notification preferences.

- Freshness Heatmap
    - The freshness chart has been redesigned for an improved user experience.
    - Milliseconds are now displayed in a more readable date/time format for better comprehension, while the underlying data still uses milliseconds.

#### General Fixes and Improvements

- Create User
    - Fixed a bug that occurred when creating a service user with automatic admin permission enabled.

- Rerun Operations
    - Catalog, export, and materialize operations will now only display rerun operations.

- General Fixes and Improvements.

### 2025.5.16 { id=2025.5.16 }

#### Feature Enhancements

- Anomaly
    - Users can now view the Anomaly Fingerprint directly in the Anomaly Details page.
    - A new button allows users to quickly copy the fingerprint value.
    - A link to the User Guide has been added to explain how this feature works.

- Datastore Connection
    - A new validation step was added to several connectors to verify if the specified schema exists.

#### General Fixes and Improvements

- Schedule Operation
    - Fixed a bug in scheduled operations that allowed `None` as a value for `max_records_analyzed_per_partition` when updating.

- Check
    - Fixed an issue where creating a metric check with a non-existent comparison value would fail..
    - Fixed a bug where checks would fail if the filtered set was empty — now the check will pass in this case.

- Catalog Operation
    - Fixed an issue in DB2 where evaluating the distribution of values caused an error.

- Scheduled Scan
    - Fixed an issue that occurred when adding connection retries related to the Secrets Manager.

- Anomaly
    - Fixed an issue where some triggered anomalies had no data available.

- General Fixes and Improvements.

### 2025.5.9 { id=2025.5.9 }

#### Feature Enhancements

- Microsoft Teams Integration
    - We're excited to announce a native integration with Microsoft Teams, bringing powerful collaboration features directly into your Teams workspace.
    - Users can now:
        - Share Qualytics links to datastores, containers, or fields and see rich previews directly in Teams.
        - Receive proactive notifications when:
            - An operation completes
            - An anomalous table or file is detected
            - A specific anomaly is triggered
        - Note that the message content and actions will adapt based on the trigger type defined in the Flow.
        - Manage anomalies without leaving Teams:
            - View, acknowledge, comment on, or archive anomalies from within the Teams UI
            - Click to open linked anomalies directly in Qualytics
    - The integration must be configured by a Qualytics admin. A dedicated setup guide is available in our User Guide.
    - As part of this rollout:
        - Any Flows previously configured to send Teams notifications via incoming webhooks or workflows (Teams) have been automatically migrated to the Webhook action.
        - The Teams notification action is now only available through the new integration.

- Tokens
    - Users can now view the last time a token was used.

- Session Expiration
    - Improved handling of session expiration for users who are logged in but inactive for an extended period.

#### General Fixes and Improvements

- Check Template
    - Fixed an issue with the message displayed when a user archives a check that has associated checks.

- General Fixes and Improvements.

### 2025.5.5 { id=2025.5.5 }

#### Feature Enhancements

- Tokens
    - Users can now view the last time a token was used, providing better visibility into token activity.

#### General Fixes and Improvements

- Is Replica Of Check
    - Fixed a bug where anomalies using pass-through fields on both the left and right side were not handled correctly.

- Action Operations
    - Fixed an issue where cloning an Action Operation could exceed the allowed action limit.

- Group By
    - Fixed a bug that occurred when users added single quotes to string columns in the Group By clause.

- Atlan Sync
    - Updated and created custom metadata objects to align with the latest schema.

- General Fixes and Improvements.

### 2025.4.24 { id=2025.4.24 }

#### Feature Enhancements

- Improved Filters
    - Tag Filter
        - Users will only see tag options corresponding to items currently visible in the list pages (Datastore List, Container List, and Filter List).
        - The same filtering behavior has been applied to Anomalies and Checks within the datastore context.
        - If no visible items contain a specific tag, a `No option found` message will be displayed in the filter dropdown.

- Scan Operation
    - Scan form
        - The scan form has been reorganized to improve the user experience.
        - Now, the following steps to configure the Scan Flow are Check Categories, Reading Settings and Scan Settings.
    - Enrichment Settings
        - The Remediation Strategy option is now in the Enrichment Datastore Settings.
        - The option will be a Datastore global value.
        - Also, the Anomaly Rollup Threshold and Source Record Limit can be configured as defaults.
        - During scan operations, these options will be pre-filled but can still be edited within the scan form.

- Tree View
    - The tree view layout is now adjustable, allowing users to customize it to their preferences.
    - The footer in the tree view can be expanded or collapsed based on user needs.

#### General Fixes and Improvements

- Filters
    - Fixed an issue where filters behaved inconsistently when navigating between different datastores.

- The container page is not loading
    - Fixed a bug that caused the container page to fail to load under certain conditions.

- General Fixes and Improvements.

#### API Changes

- Incoming Breaking Changes
    - REQUEST PAYLOAD: The fields `enrich_only` and `enrichment_only` will be replaced by `enrich_container_prefix` and `enrichment_prefix` and will affect the following endpoints:
        - `POST /datastores`
        - `PUT /datastores/{id}`
    - RESPONSE PAYLOAD: The fields `enrich_only` and `enrichment_only` will be replaced by `enrich_container_prefix` and `enrichment_prefix` and will affect the following endpoints:
        - `GET /anomalies/{id}`
        - `PUT /anomalies/{id}`
        - `POST /containers`
        - `GET /containers/{id}`
        - `PUT /containers/{id}`
        - `GET /containers/{id}/profile`
        - `GET /containers/{id}/scan`
        - `POST /containers/{id}/scan`
        - `PATCH /containers/{id}/favorite`
        - `GET /container-profiles/{id}`
        - `GET /container-scans/{id}`
        - `POST /datastores`
        - `PUT /datastores/{id}`
        - `GET /datastores/{id}`
        - `PATCH /datastores/{id}/favorite`
        - `PATCH /datastores/{datastore_id}/enrichment/{enrich_store_id}`
        - `GET /field-profiles/{id}`
        - `POST /operations/schedule`
        - `PUT /operations/schedule/{id}`
        - `GET /operations/schedule/{id}`
        - `GET /operations/{id}`
        - `POST /operations/run`
        - `PUT /operations/run/{id}`
        - `PUT /operations/rerun/{id}`
        - `PUT /operations/abort/{id}`
    - `POST /operations/run`, `POST /operations/schedule`, `PUT /operations/schedule/{id}`, `POST /flows, and PUT /flows/{id}`
        - DEPRECATE PARAMETER: `remediation` (To specify a remediation strategy going forward, use the new `enrichment_remediation_strategy` field available in the POST /datastores and PUT /datastores/{id} endpoints.)

### 2025.4.11 { id=2025.4.11 }

#### Feature Enhancements

- Anomalies and Checks Filter
    - The Rule filter is now dynamically populated based on the types present in the current view.
    - Each rule type displayed in the filter now includes a counter showing the total number of occurrences.

- Status Page
    - The Health page has been renamed to Status page.
    - Users can view additional information like Cloud Platform and Deployment Size.
    - Deployment size details are now displayed to provide better visibility into environment configurations.

#### General Fixes and Improvements

- Anomaly
    - Resolved a bug when handling `NaN` values in float-type data.

- General Fixes and Improvements.

### 2025.4.5 { id=2025.4.5 }

#### General Fixes and Improvements

- Quality Score
    - Enhanced the descriptions for each Factor Weight to provide clearer guidance on how they impact the overall score.

- General Fixes and Improvements.

### 2025.3.28 { id=2025.3.28 }

#### Feature Enhancements

- Anomalies
    - The “Anomalies Identified” count now shows the sum of Open and Archived anomalies.
    - Anomalies are now categorized into two groups:
        - Open: anomalies currently active (Active, Acknowledged).
        - Archived: anomalies that have been archived (Resolved, Duplicated, Invalid).
    - Users can now view the total counts of Duplicate and Invalid anomalies in the Overview tab under the Explore page.
    - Users can now see the total counts of Open and Archived anomalies directly in Scan Operations.
    - The Scan Results modal now displays the totals for Open and Archived anomalies.
        - Users can filter anomalies by status using a new dropdown selector.

- Quality Checks
    - Users can now sort the Quality Checks list by the “Last Asserted” date.

#### General Fixes and Improvements

- Teams Permissions
    - Fixed an issue where users with the Drafter role were unable to restore a check as a draft.

- General Fixes and Improvements.

### 2025.3.23 { id=2025.3.23 }

#### Feature Enhancements

- Slack Integration
    - We are excited to introduce a major enhancement to our integration with Slack.
    - Users can now add the new Qualytics Slack App for enhanced capabilities.
        - Qualytics admins can configure the Slack Integration with two easy steps.
            - After configuring the integration, a Slack administrator must approve the Qualytics Slack App.
    - The Qualytics Slack App supports selecting specific Slack channels for receiving Qualytics notifications in the context of a Qualytics Flow.
        - Different types of messages will be sent for each trigger in Flow operations.
            - The text and actions will vary depending on the selected trigger.
            - The message state (Slack message color) will change based upon the message status.
    - The Qualytics Slack App allows users to interact with Qualytics from the Slack interface:
        - Interact with anomalies by acknowledging, commenting, or archiving them without leaving the Slack UI where the flow notification is received.
        - Click a link in Slack to be redirected to the Qualytics UI for more details regarding a specific notification.
        - View anomalous tables and files detected without leaving Slack.

- Anomaly Fingerprint
    - We are thrilled to introduce support for a new feature that will begin identifying duplicate anomalies.
    - Anomalies created after this release will be "fingerprinted" so that re-detection of that same anomaly can be readily identified as a duplicate detection.
        - New Scan Operation options allow users to define how detected duplicates should be handled.
        - This feature helps maintain the history and timeline of specific data errors, allowing users to track how long a specific issue has persisted and a log of detections over time.
        - Anomaly fingerprints will also be exposed in API responses and written to enrichment

#### General Fixes and Improvements

- External Scan
    - Users can now use and rerun external scans only from the activity listing for the targeted asset.
- Check Last Asserted
    - Fixed an issue where checks were still being marked as never asserted even after producing anomalies.

#### API Changes

- Integration Impacting Changes
    - POST & PUT api/integrations
        - REMOVED PARAMETERS: name and api_token
        - NEW PARAMETERS: api_access_token, api_refresh_token and api_service_token
    - POSTs to api/flows/actions/notifications/ endpoints
        - MODIFIED PARAMETERS: tokenized_message is now a json object instead of a string
    - All requests to api/datastores endpoints
        - REMOVED RESPONSE PROPERTY METRIC: The metric for archived_anomalies previously returned as metrics.archived_anomalies has been removed from responses

- Deprecation Notices
    - POST api/operations/run
        - DEPRECATED PARAMETER: archive_overlapping_anomalies (migrate to the new parameter archive_duplicate_anomalies for enhanced functionality)
    - POST api/operations/schedule
        - DEPRECATED PARAMETER: archive_overlapping_anomalies (migrate to the new parameter archive_duplicate_anomalies for enhanced functionality)

### 2025.3.17 { id=2025.3.17 }

#### Feature Enhancements

- Activity Operation
    - Added a column showing the anomaly rollup threshold.

- Export Operations
    - Added an option allowing users to schedule Export Operations.

- DFS Enrichment Datastore
    - Normalized delta file names to lowercase.

#### General Fixes and Improvements

- Anomaly Rollup Threshold
    - Fixed an issue where the field was not accepting the maximum value.

- Volumetric Tracking Observability
    - Fixed an issue where inferred check validation errors disrupted observability measurements.

- Export Operation
    - Updated wording on the Export dialog.

- Scan and External Scan
    - Fixed an issue where schema checks were failing along with other checks but were not persisting in the enrichment of source records for anomalies.

- External Scan
    - Fixed an issue where CSV data was not being properly cast for non-text fields.

- Enrichment Datastore
    - Fixed a bug where exported tables were not appearing in the UI.

- General Fixes and Improvements.

### 2025.3.5 { id=2025.3.5 }

#### General Fixes and Improvements

- Tag Updating
    - Fixed an issue where some containers failed to receive tag changes when updating tags across multiple containers or performing bulk updates.

- Edit Scheduled Materialize Operation
    - Fixed an issue where the modal did not appear when users attempted to edit a scheduled materialize operation.

- Restart Analytics Engine
    - Fixed an issue where restarting the Analytics Engine did not take effect.

- Anomaly Count
    - Fixed an inconsistency in the anomaly count.

- General Fixes and Improvements.

### 2025.2.26 { id=2025.2.26 }

#### Feature Enhancements

- Enrichment Operations
    - Introducing Materialize Operation
        - This will "capture a snapshot" of selected containers from your source datastore and export them to the enrichment datastore for seamless data loading.
        - Users can define the maximum number of records to be materialized per table.
        - A schedule option is available for users to set up and schedule the operation according to their needs.
    - Introducing Export Operation
        - Users can extract metadata from selected assets in their source datastore and export it to the enrichment datastore for seamless integration.
        - Assets metadata options are available to export to the enrichment datastore. Users can export:
        - Anomalies
        - Quality checks
        - Field profiles
    - These operations are available in Flow Action.

- Flows
    - Introduced a cloning feature for actions in flow.
        - Users can now clone a simple action by clicking the vertical ellipses.

- Scan Operation
    - Introducing Anomaly Rollup Threshold
        - Users can now roll up anomalies that will be created per check before they are merged into a single rolled-up anomaly.

- Error Messages
    - Improved custom messages when users receive 502 and 503 status codes.

#### General Fixes and Improvements

- System Timestamp
    - Standardized timestamps across the platform.

- External Integrations
    - Fixed an issue where external tags should be updated instead of being deleted and dropped during sync.

- General Fixes and Improvements.

### 2025.2.13 { id=2025.2.13 }

#### Feature Enhancements

- Explore View
    - Users can now refresh the Insights data.
    - A label will indicate when the page was last refreshed.

- System Appearance
    - Users can now select the `System` theme.
        - This setting automatically adjusts based on the user's system theme, switching between dark and light mode.
    - Users can still manually select dark or light mode.

- Dismiss Popup Window
    - Users can now dismiss popup windows by pressing the `Esc` key, improving the user experience.

#### General Fixes and Improvements

- External Scan
    - Fixed an issue where attempting to run an external scan resulted in a "Request Failed" error message.

- Explore View
    - Fixed an issue causing excessively long loading times.

- General Fixes and Improvements.

### 2025.2.6 { id=2025.2.6 }

#### Feature Enhancements

- Overview Improvement
    - Added inferred and authored check totals
        - Users can now view the total number of inferred and authored checks, along with a comparison timeframe.
        - A redirect link allows users to access the checks directly, displaying only their current statuses.
    - Improved check assertion-related metrics to reflect assertions as of the report date.

- Team Permissions
    - Manager users can now update datastore teams.
        - Requires `Editor` permission within the team.

#### General Fixes and Improvements

- Flow Graph
    - Fixed an issue where the flow graph position was randomly changing when a user updated a flow-node.

- Observability Chart
    - Fixed an issue where threshold calculations incorrectly referenced measurement values that did not account for grouping.

- General Fixes and Improvements.

#### Breaking Changes

- Container Overview Tab
    - Refactored the Totals section to clarify that metrics are based on sampled data rather than the full dataset.
        - Added the sampling percentage next to the spark chart to indicate that derived metrics are based on this sampling percentage.
        - Updated titles and labels for better clarity.

### 2025.1.31 { id=2025.1.31 }

#### Feature Enhancements

- Freshness View
    - We are excited to introduce the "Freshness View" feature in Qualytics!
    - Users can now visualize both volumetric and freshness checks within the same tab.
    - The displayed data includes:
        - Unit: Day, Month, Hour, etc.
        - Maximum Age: Defines the maximum allowed time since the last data update.
        - Last Asserted: Indicates the last time the data was validated.

- Datastore Filter Condition in Flows
    - Users can now configure datastore filter conditions in triggers for flows, enhancing control over triggered actions.

- Treat Empty Value as Null for DFS
    - A new option allows users to enable "Empty value as null" as the default behavior for File Patterns, improving data consistency.

#### General Fixes and Improvements

- General Fixes and Improvements.

### 2025.1.24 { id=2025.1.24 }

#### Feature Enhancements

- Introducing Freshness Tracking in Containers
    - Users can now enable a freshness tracking option for containers to measure and record the last time data was added or updated in a data asset. This helps ensure data timeliness and identifies pipeline delays.

- Private Routes on Analytics Engine
    - Customers using private routes can now view their IP addresses along with relevant messages displayed in the Analytics Engine for improved transparency.

- Clone a Flow
    - Users can duplicate existing flows, streamlining the process of reusing and modifying flow configurations for similar scenarios.

- Additional Option to Execute Manual Flows
    - A new "Start a Manual Flow" option has been added to the vertical ellipsis menu, providing users with enhanced flexibility for executing manual flows.

- Cancel Action for Unpublished Flows
    - A "Cancel" action has been introduced in the flow builder, allowing users to reset the graph to its initial state for unpublished flows. This update also addresses issues related to the execute button and read-only state logic.

- "Is Replica Of" Passthrough
    - The `IsReplicaOf` rule now supports a passthrough property, allowing users to exclude specific fields from assertions. Fields listed under this property are no longer flagged as anomalous.

- Enhancement for Volumetric Rule Type
    - Volumetric checks now include a `comparison` property, ensuring consistency with metric checks and offering greater flexibility in rule configurations.

#### General Fixes

- General Fixes and Improvements.

### 2025.1.20 { id=2025.1.20 }

#### Feature Enhancements

- Enhanced behavior for "All" in Schedule Operations
    - The "All" option in Schedule Operations has been updated to include future containers automatically. Previously, if you created a schedule with the "All" option and added new tables or containers later, the schedule would not include these new additions.

- Validate Button for Enrichment Datastore Connections
    - Users can now validate their data when creating or editing an enrichment datastore connection, improving reliability and confidence in datastore setups.

#### General Fixes

- Inaccurate Check Assertion Details
    - Resolved an issue where some checks were being marked as never asserted despite producing anomalies, ensuring more accurate reporting.

- General Fixes and Improvements.

### 2025.1.16 { id=2025.1.16 }

#### Feature Enhancements

- Flows
    - Introducing Flows: Users can now create automated pipelines by chaining actions and configuring triggers based on predefined events and filters.
        - Triggers: Configurable based on events, filters, and operation conditions.
        - Actions: Include notifications (Email, Slack, PagerDuty, etc.) and operations (catalog, profile, and scan).
        - Real-Time Execution: Monitor execution history and real-time progress in the Flow Executions tab.

    - Setup Made Simple
        - Add and configure flows using the “Add Flow” button in the top-right corner.
        - Deactivate, delete or edit flows via the vertical ellipses or node configurations.

    - Enhanced Triggering Options
        - Operations Complete, Anomalous Table/File Detected, and Anomaly Detected triggers provide flexible, event-driven automation.
        - Fine-tune triggers using filters like tags, rule types, or anomaly weights.

    - Diverse Action Support
        - Notify through in-app messages, Emails, Slack, Microsoft Teams, PagerDuty, and custom HTTP actions
        - Trigger operational tasks across cataloging, profiling, and scanning.

    - Flow Identification on Activity Tab
        - Operations executed by flows are marked in the new `Flow` column, displaying the associated flow name.
        - Users can navigate directly to the flow execution view from this tab.

#### General Fixes

- Duplicate Anomalies on Scan Schedule Operations
    - Fixed an issue where duplicate anomalies were not being archived during scan operations despite user selection.

- BigQuery Message Size
    - Enhanced default batch insertion size to improve performance and reliability.

- Anomalous Record Integer out of Range
    - Updated check metrics to use BigInteger, addressing large value handling.

- Fix the Last Asserted Date
    - Resolved inconsistencies in the Last Asserted Date logic for partition and container scans.

- General Fixes and Improvements.

#### Breaking Changes

- Notification Rules Replaced by Flows.
    - Existing notification rules have been migrated to Flows and will continue to function as before.
    - For new notifications, the users must create a flow leveraging the Flows functionality.
