# 2025 

## Release Notes

### 2025.03.17 { id=2025.03.17 }

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

### 2025.03.05 { id=2025.03.05 }

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

### 2025.02.26 { id=2025.02.26 }

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

### 2025.02.13 { id=2025.02.13 }

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

### 2025.02.06 { id=2025.02.06 }

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
    - Fixed an issue where the flow graph position was randomly changing when a user updated a flow node.

- Observability Chart
    - Fixed an issue where threshold calculations incorrectly referenced measurement values that did not account for grouping.

- General Fixes and Improvements.

#### Breaking Changes

- Container Overview Tab
    - Refactored the Totals section to clarify that metrics are based on sampled data rather than the full dataset.
        - Added the sampling percentage next to the spark chart to indicate that derived metrics are based on this sampling percentage.
        - Updated titles and labels for better clarity.

### 2025.01.31 { id=2025.01.31 }

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

### 2025.01.24 { id=2025.01.24 }

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

### 2024.01.20 { id=2024.12.20 }

#### Feature Enhancements

- Enhanced behavior for "All" in Schedule Operations
    - The "All" option in Schedule Operations has been updated to include future containers automatically. Previously, if you created a schedule with the "All" option and added new tables or containers later, the schedule would not include these new additions.

- Validate Button for Enrichment Datastore Connections
    - Users can now validate their data when creating or editing an enrichment datastore connection, improving reliability and confidence in datastore setups.

#### General Fixes

- Inaccurate Check Assertion Details
    - Resolved an issue where some checks were being marked as never asserted despite producing anomalies, ensuring more accurate reporting.

- General Fixes and Improvements.

### 2025.01.16 { id=2025.01.16 }

#### Feature Enhancements

- Flows
    - Introducing Flows: Users can now create automated pipelines by chaining actions and configuring triggers based on predefined events and filters.
        - Triggers: Configurable based on events, filters, and operation conditions.
        - Actions: Include notifications (Email, Slack, PagerDuty, etc.) and operations (catalog, profile, and scan).
        - Real-Time Execution: Monitor execution history and real-time progress in the Flow Executions tab.

    - Setup Made Simple
        - Add and configure flows using the “Add Flow” button in the top-right corner.
        - Deactivate, delete, or edit flows via the vertical ellipses or node configurations.

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

- Fix Last Asserted Date
    - Resolved inconsistencies in the Last Asserted Date logic for partition and container scans.

- General Fixes and Improvements.

#### Breaking Changes

- Notification Rules Replaced by Flows.
    - Existing notification rules have been migrated to Flows and will continue to function as before.
    - For new notifications the users must create a flow leveraging the Flows functionality.