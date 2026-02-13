# 2026

## Release Notes

### 2026.2.13 { id=2026.2.13 }

#### Feature Enhancements

- Introduced Microsoft Fabric JDBC connector.
    - Added read-only connectivity to Microsoft Fabric's SQL Analytics Endpoint, enabling users to profile and monitor data quality on Fabric datasets.
    - Authentication is handled via Azure Active Directory Service Principal, with credentials securely managed through connection properties.

- Added Service Principal authentication support for ABFS datastores, allowing Azure Active Directory OAuth-based connections as an alternative to Shared Key authentication.

#### General Fixes and Improvements

- Fixed missing label text color in the bulk action menu on the Flows page when using dark theme.

- Corrected low-contrast tooltip icon on the check assertion timeline that was difficult to see in both light and dark modes.

- Optimized data catalog integration sync performance by replacing verbose per-asset logging with concise per-datastore summaries, reducing storage overhead in environments with large asset catalogs.

- General Fixes and Improvements.

### 2026.2.7 { id=2026.2.7 }

#### Feature Enhancements

- Introduced license management interface under Settings.
    - Administrators can now view the current license expiration date directly from the Settings Status page, with visual warnings when the license is nearing expiration.
    - Added the ability to generate a license request payload to send to a Qualytics account representative for license renewal.
    - Users can apply a new license directly through the interface, streamlining the license assignment process.

- Added bulk actions and validation improvements for flow executions.
    - Users can now select and abort multiple flow executions at once, eliminating the need to handle stuck executions one by one.
    - Introduced bulk delete for flow executions to streamline cleanup of completed or failed runs.
    - Added filter option for aborted status in the flow executions list for easier tracking.
    - Flows without actions are now validated and blocked from publishing to prevent incomplete workflow configurations.

- Added support for custom anomaly messages from source record fields.
    - Quality checks can now use a field value from the source record as the anomaly message, replacing the auto-generated violation text with business-specific context.
    - Custom anomaly message field can be configured in both individual check forms and bulk check creation workflows.
    - A field selector is available when container fields are loaded, with a manual text input fallback for flexible configuration.

- Added rule type filter to the Observability listing.
    - Users can now filter containers by observability rule type, choosing between Volumetric and Freshness checks for more focused monitoring.
    - Filter availability adapts to the current context, displaying relevant filter options across Explore, Datastore, and Container views.
    - Improved column alignment and heatmap display across different screen sizes for better readability.

#### General Fixes and Improvements

- Corrected auto-generated descriptions for multi-field Unique and Not Null checks to reference all selected fields instead of only the first one.

- Fixed anomalous field filter in the failed checks section where checkbox selections were not filtering results and layout elements were overlapping.

- Corrected tooltip icon contrast in the check assertion timeline that was not visible against the tooltip background in both light and dark modes.

- Fixed incorrect breadcrumb navigation when viewing checks that no longer reference the original field after field association changes.

- Improved platform reliability by automatically recovering flow executions and data catalog syncs that became stuck after environment restarts.

- Centralized internal field association logic to improve consistency and reliability across anomaly counts, filtering, and data catalog synchronization.

- General Fixes and Improvements.


### 2026.1.29 { id=2026.1.29 }

#### Feature Enhancements

- Introduced Anomaly Status Changed flow trigger.
    - Flows can now be triggered when anomaly statuses change, enabling automated workflows for status transitions.
    - Trigger settings support filtering by specific status values to target relevant transitions.

- Added notification support for Create Ticket and Update Ticket Status flow actions.
    - Introduced Create Ticket action to automatically generate tickets in connected ticketing systems when anomalies meet defined conditions.
    - Introduced Update Ticket Status action to synchronize status changes to linked tickets across integrated platforms.
    - Notifications can be sent to Slack and Microsoft Teams when ticketing actions execute.
    - Introduced status selection at ticket creation, allowing tickets to be created with a specific initial state.
    - Ticketing actions are validated to ensure compatibility with Anomaly or Anomaly Status Change triggers.
    - Improved handling when required ticketing integrations are unavailable during flow execution.

- Enhanced auto-generated check descriptions with context-aware, business-friendly language.
    - Descriptions now include field type context such as "numeric field", "timestamp field", or "text field" for clearer rule interpretation.
    - Expected values are summarized directly in descriptions, displaying the first three values with a total count indicator.
    - Filter clauses are translated into plain English for improved readability.
    - Range checks now specify inclusivity labels to clarify boundary behavior.
    - Common regex patterns are described in human-readable terms instead of raw expressions.
    - Cross-datastore rules include reference field and container context for better traceability.
    - Distinct count checks generate comparator-aware descriptions using phrases like "fewer than", "at most", "exactly", "at least", and "more than" based on the configured operator.

- Improved computed asset management with inline editing from check interfaces and field dependency protection.
    - Users can create, edit, and manage computed tables, files, joins, and fields directly from the check interface without navigating to datastore pages.
    - Added a warning dialog when computed asset updates would remove fields with active checks or anomalies, with options to cancel or proceed.
    - Introduced "E" keyboard shortcut to quickly edit computed containers from any context.
    - Enhanced command palette shortcuts to preselect the current container in profile and scan dialogs.

#### General Fixes and Improvements

- Improved error messages for network connectivity issues to provide clearer guidance when the API server is unreachable.

- Enhanced asserted check editing to support field modifications while preserving accurate quality score calculations.

- Improved anomaly descriptions with editable fields, version tracking, and enriched human-readable messaging.

- Enhanced tenant observability with build version information.

- Fixed tags and rule types not appearing in filter lists by aligning filter option counts with the current view perspective.

- Corrected distinct count anomaly messages that displayed negative values and incorrect expected values.

- Resolved Collibra integration authentication failures caused by OAuth token expiration with automatic token refresh.

- General Fixes and Improvements.

### 2026.1.14 { id=2026.1.14 }

#### Feature Enhancements

- Introduced the new Qualytics visual identity
    - Refreshed brand experience featuring a modern color palette, updated logo, and refined typography that reflects the platform’s evolution.
    - Redesigned Insights dashboard with enhanced quality score cards, vibrant chart gradients, and improved dimension visualizations for clearer data storytelling.
    - Modernized card layouts across datastores, containers, checks, anomalies, and templates with improved visual hierarchy and interaction states.
    - Streamlined iconography with consistent outline styling and neutral tones for a cleaner, more focused interface.
    - Enhanced chart styling with cyan monochromatic palettes, smooth gradients, and rounded segments across key visualizations such as data volume, observability metrics, heatmaps, and others.
    - Improved accessibility with better contrast ratios, theme-aware color utilities, and consistent styling across light and dark modes.
    - Refined sign-in experience with updated visual styling aligned to the new brand direction.

#### General Fixes

- Optimized container preview performance.

- Standardized enrichment datastore settings labels to ensure consistency with the scan operation options.

- Enhanced operation timeout behavior to ensure meaningful error responses for long-running sync operations.

- Fixed scan schedule update errors that occurred when anomaly reactivation settings were not explicitly configured.

- Resolved intermittent server errors affecting the Flows list page when scheduled information was present.

- Corrected server errors when publishing flows while action rearrangement was in progress.

- Resolved field exclusion behavior to properly skip problematic columns during initial data loading in SQL Server datastores.

- General Fixes and Improvements.
