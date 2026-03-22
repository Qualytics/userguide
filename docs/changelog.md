# 2026

## Release Notes

### 2026.3.20 { id=2026.3.20 }

#### Feature Enhancements

- Renamed the Catalog operation to Sync, now performing delta-based processing that only analyzes changes instead of recalculating all container metadata.
    - The Sync operation processes only what has changed since the last run, significantly reducing execution time on large datastores.

- Introduced Field Masking to protect sensitive data such as PII and ePHI, allowing fields to be marked as masked so their values are scrubbed from all standard data responses.
    - Masked field values are replaced with a placeholder ***MASKED*** in container previews, source record retrievals, enrichment reads, and quality check dry runs.
    - Privileged users can request unmasked values through an explicit override, with all access recorded in an audit trail.
    - Fields serving as container identifiers (incremental, partition, or group-by fields) cannot be masked to preserve operational integrity.

- Display names and descriptions from data catalog integrations — When synced with a data catalog (Atlan, Alation, Microsoft Purview, Collibra, or DataHub), Qualytics automatically populates descriptions on datastores, and display names and descriptions on containers and fields from the catalog's asset metadata.
    - When a display name is set, it is shown across the entire platform in place of the source name, with the original name still accessible via an info icon.
    - Display names and descriptions can also be manually assigned directly in Qualytics, independently of any data catalog integration.

- Added multi-schema source datastore creation, allowing users to discover and select multiple schemas from a single connection and create all corresponding source datastores in one step.
    - Available catalogs and schemas are automatically discovered from the connection, letting users browse and select which ones to onboard.
    - An optional second step allows linking all newly created source datastores to a single enrichment datastore, either by selecting an existing one or creating a new one during the same flow.

- Enabled a Business Context configuration in the LLM integration, providing personalized Agent Q suggestions tailored to each organization's data governance responsibilities.
    - Administrators can describe their team's business focus and data quality scope in the LLM integration settings, providing Agent Q with relevant organizational context.
    - Agent Q suggestions now incorporate both the organization's business context and a summary of the user's most recent chat session for more relevant recommendations.

- Introduced team restriction mode, allowing administrators to view and interact with the platform from the perspective of a specific team.
    - Administrators can select a team from the profile dropdown to restrict their session, temporarily assuming a Manager role scoped to that team's permissions and visibility.
    - A visual indicator is displayed in the toolbar while a restriction is active, providing clear awareness of the current team context.
    - The restriction persists across navigation and page reloads until explicitly removed by the user.

#### General Fixes and Improvements

- Resolved computed join container previews returning empty results under certain key overlap conditions.

- Corrected timezone abbreviations not reflecting Daylight Saving Time, now dynamically displaying the correct label (e.g., EDT vs EST) based on the date being shown.

- Addressed Agent Q chat context and message content overflowing the input field when expanding long responses.

- Fixed freshness chart anomaly bars not displaying the correct highlight color and heatmap data reflecting all checks instead of only the selected one.

- Resolved a race condition during API startup that could cause intermittent authentication errors.

- Fixed stale scheduler jobs causing phantom flow executions after changing a flow's trigger type, now properly cleaning up scheduled jobs when the trigger type is modified or a flow is deleted.

- Resolved the Atlan integration not populating check and anomaly counts, now correctly synchronizing metadata for both new and existing installations.

- Corrected observability operations failing on datastores containing computed joins with computed fields.

- Resolved reference filters in quality checks not substituting check variables, causing validation and scan errors on checks using dynamic placeholder values.

- Added an Export as PDF option for Agent Q responses, allowing users to download individual messages as formatted PDFs that preserve the chat's visual layout.

- Optimized profiling performance for containers with large field counts, including more efficient correlation analysis, significantly reducing execution time on wide schemas.

- Enhanced datastore group visibility across the application, now displaying group information in breadcrumbs and adding management actions directly in the sidebar.

- Updated delete confirmation dialogs across the application to clearly communicate the impact of each action before proceeding.

- Improved Snowflake connection validation to surface warning messages about potential warehouse issues, such as undersized or suspended warehouses.

- Removed the five key-value pair limit from the additional metadata editor, now supporting unlimited entries with scrollable and collapsible views.

- General Fixes and Improvements.

### 2026.3.6 { id=2026.3.6 }

#### Feature Enhancements

- Introduced promote operation for copying computed assets and quality checks across datastores and containers.
    - Users can promote computed tables, computed files, and computed fields from one datastore or container to another, eliminating the need to manually recreate definitions across environments.
    - Promote enables environment-based management of computed assets and checks — each entity is matched by name on the destination and either created if missing, updated if the definition differs, or skipped if identical.
    - Quality checks can now be promoted across containers as active or draft, replacing the previous check migration feature that only supported creating checks as drafts.
    - Each promoted entity reports an individual result status (Created, Updated, Skipped, or Failed) with filterable results and expandable error details.
    - Promote operations appear in the Activity list with progress tracking.

- Introduced PagerDuty as a first-class alerting integration.
    - PagerDuty now appears in the Integrations page alongside Slack and Microsoft Teams, with a new additional details field for including custom context in incident notifications and an optional routing key override for directing incidents to a different service than the one configured at the integration level.

- Added container-level default variables for quality checks and computed containers.
    - Containers now support additional metadata key-value pairs that serve as default variable values during scans, configurable from the container settings page.
    - Scan operations include a Scan Variables section in advanced options, allowing users to override container defaults on a per-scan basis.
    - Variable resolution follows a defined priority: container metadata provides defaults, scan-level variables override those, and system profile variables take highest precedence.

- Enhanced Agent Q chat experience with background streaming, session management, and infinite scrolling.
    - Chat sessions now support archiving, restoring, and permanent deletion, giving users full control over their conversation history.
    - Chats continue generating responses when navigating away from the session, with a visual indicator for ongoing or interrupted streams.
    - Infinite scrolling is now supported for chat messages, the chat history sidebar, and archived sessions, replacing manual pagination.
    - Floating chat mode now includes a chat history dropdown for switching between sessions without leaving the floating interface.

- Added a force refresh option for anomaly source records, allowing users to bypass the cache and fetch the latest available data directly from the API, with a tooltip displaying the last updated timestamp.

#### General Fixes and Improvements

- Resolved an error when favoriting a datastore, container, or quality check for the first time when no other assets had been previously favorited.

- Corrected performance regressions in known pattern detection during profiling that caused redundant regex evaluations, significantly reducing constraint suggestion time on large datasets.

- Addressed Aggregation Comparison check validation failing when using expression-only aggregations like `count(*)` with no explicit field references.

- Fixed fields with "missing" status appearing in the sidebar tree view after schema changes, now showing only active fields to keep the navigation uncluttered.

- Resolved computed join container previews returning empty results when sampled join keys from each side did not overlap.

- Corrected inaccurate freshness check results on JDBC datastores caused by silent DATE-to-Timestamp coercion that applied the local timezone instead of UTC.

- Addressed field profile metric preview charts that appeared empty on hover.

- Resolved Expected Values checks rendering empty value lists in certain scenarios, such as numeric values, while other types displayed correctly.

- Corrected BigQuery export and materialize operations displaying raw JDBC error messages on write failures, now providing user-actionable messages for common issues like quota limits, missing datasets, and permission errors.

- Optimized Redshift write performance by aligning the JDBC batch insert size with the driver configuration, reducing overhead during data operations.

- Improved dataDiff checks with granular change type filtering, allowing users to specify whether added, removed, or changed rows should trigger anomalies, with at least one type required and all three selected by default.

- Enhanced the asset timeline with Agent Q co-authorship attribution, allowing users to identify which changes were made through AI-assisted workflows, with the Agent Q avatar and client name displayed on co-authored entries.

- Improved the command palette with unified search and expanded asset support.
    - Asset search is now integrated directly into the command palette alongside command search, replacing the previous standalone Search Assets shortcut.
    - Assets can now be filtered by ID in addition to name, allowing users to jump directly to a specific item.
    - Added support for new searchable asset types: quality checks, check templates, and anomalies.

- General Fixes and Improvements.

### 2026.2.27 { id=2026.2.27 }

#### Feature Enhancements

- Introduced field status management to preserve historical data when source schema changes occur.
    - Fields removed or renamed at the source are now marked as "missing" instead of being permanently deleted, preserving all associated quality checks, anomalies, and metadata.
    - Added merge capability for renamed fields, allowing users to transfer all dependencies — including checks and anomalies — from a missing field to its active counterpart in a single action.
    - Field exclusion now assigns a dedicated "excluded" status to individual fields, while remaining accessible from both the field level and the container settings for pre-profile exclusion workflows.
    - Excluded fields can be restored to active status without requiring a new profile run.
    - Added status indicators, filtering tabs, and a dedicated status filter across field listing pages for clear visibility into active, missing, and excluded fields.

- Introduced Datastore Grouping for organized sidebar navigation.
    - Users can now create custom groups to organize datastores in the sidebar by environment, purpose, or any preferred category.
    - Groups support custom icons and names, with a dedicated management menu for renaming and deleting groups.
    - Datastores can be assigned to groups directly from the tree view, with grouped datastores visually organized under collapsible sections.
    - Added group-based filtering on the datastore listing page for focused browsing across large deployments.
    - Group icons are displayed alongside datastore identifiers in card and list views for quick visual identification.

- Introduced floating chat interface for Agent Q, accessible from any page in the platform.
    - A persistent floating action button allows users to open Agent Q without navigating away from their current workflow.
    - The assistant automatically detects the current page context — including datastore, container, field, check, and anomaly — and injects relevant metadata into conversations for context-aware responses.
    - Supports paste attachments for large clipboard content, enabling users to share text snippets directly in the chat.
    - Added `Q` keyboard shortcut for quick access to the floating chat from anywhere in the application.
    - Chat history sessions are accessible from both the floating panel and the full-page Agent Q experience.

- Enhanced Agent Q with chat history management, expanded tool capabilities, and performance optimizations.
    - Chat conversations are now persisted and accessible through a searchable sidebar, allowing users to resume previous sessions and review past interactions.
    - Introduced five new assistant capabilities: tag management, operation execution, notification delivery, ticket creation, and integration listing — enabling broader task automation through natural language.
    - Added per-user rate limiting and prompt injection defenses for improved security and resource protection.
    - Added `G + Q` keyboard shortcut for quick access to the Agent Q page from anywhere in the application.
    - Optimized agent performance with singleton caching, deferred tool loading, and conversation summarization to reduce token overhead across sessions.

#### General Fixes and Improvements

- Corrected percentage value conversion in Volumetric check templates where min and max values for Percentage Change comparisons were sent as whole numbers instead of decimal format.

- Resolved misleading warning logs during computed file profiling that incorrectly reported fields as missing from the source container when they were intentionally removed from the computed file's SELECT statement.

- Resolved profile operation failures on Oracle datastores caused by undetected XMLType columns, now properly handling XML data by serializing it as readable text during profiling.

- Optimized anomaly and field-profile query performance for large-scale deployments, significantly reducing load times for anomaly listings and field profile pages in datastores with high anomaly volumes.

- Improved Aggregation Comparison anomaly messages to display evaluated values alongside expression names, making violation details immediately actionable without requiring manual investigation.

- Reduced Agent Q token consumption through conversation compaction and deferred tool loading, lowering per-request overhead and extending effective conversation length within model context limits.

- Improved database connection error messages with clearer root cause identification and actionable remediation guidance when connection pool limits are reached.

- Improved authentication error handling to display clear, user-friendly messages on the login page when access is denied due to group authorization restrictions.

- General Fixes and Improvements.

### 2026.2.21 { id=2026.2.21 }

#### Feature Enhancements

- Introduced support for Complex Datatypes for DFS.
    - Profiling and quality checks now support Array and Struct field types, expanding coverage to nested and multi-valued data structures.
    - Array fields are profiled with element-level context, allowing quality checks to validate each element individually using supported rule types such as Expected Values, Matches Pattern, and Min/Max Length.
    - Struct fields are automatically flattened into individual scalar columns during profiling, enabling full data quality rule inference and monitoring on nested data.
    - Flattening supports recursive traversal up to a configurable depth, with path-based naming conventions for generated columns.
    - Quality check rule selection adapts to complex field types, showing applicable rules based on whether the check targets the array or its individual elements.
    - Field tree views and profile pages display nested field hierarchies with updated iconography for clear identification of complex field types.
    - Source record tables and container previews display raw complex values, allowing users to inspect nested and array data directly during anomaly investigation.

- Introduced MCP-powered AI assistant with built-in chat interface and Bring Your Own Key LLM support.
    - Added an interactive chat interface directly in the platform, enabling users to perform data quality tasks through natural language conversations with AI-powered assistance.
    - Users can configure their preferred LLM provider and API key under Settings, with support for OpenAI, Anthropic, Google, AWS Bedrock, Cohere, Groq, Mistral, and Hugging Face models.
    - The assistant leverages MCP tools to explore datastores, validate queries, create computed assets, manage quality checks, investigate anomalies, and analyze quality scores within a guided workflow.
    - Chat responses include real-time tool step progress indicators, displaying each action the assistant performs with expandable input and output details.
    - Suggested prompts guide users toward common workflows such as building computed tables, creating quality checks, and analyzing data quality trends.

- Introduced version history for containers.
    - Users can now view a timeline of changes made to any container directly from the container overview page, displaying the editor and timestamp for each modification.
    - Computed tables include a side-by-side diff visualization of query changes, making it easy to compare before and after states for troubleshooting.

- Added n8n workflow integration as a flow action.
    - Users can configure n8n webhook URLs and secrets directly on each flow action, enabling automated workflows triggered by flow executions.
    - Supports operation-completed, anomaly, and anomaly status change triggers, sending full context payloads to n8n for downstream automation.

- Added Service Principal authentication support for SQL Server datastores.
    - Enables Azure Active Directory OAuth-based connections using tenant ID, client ID, and client secret or certificate credentials as an alternative to username and password authentication.

#### General Fixes and Improvements

- Fixed missing loading indicators on the Explore fields list and Activity page tabs.

- Corrected container creation returning a generic server error instead of a proper conflict response when a container with the same name already existed in the datastore.

- Resolved incremental ID timezone parsing issue that applied local timezone instead of UTC, causing inaccurate freshness metrics when incremental filtering was enabled.

- Corrected data catalog sync summary to only count assets that were successfully synced, preventing misleading totals when individual asset syncs failed.

- Fixed quality check API updates not persisting referenced fields when expressions were modified, ensuring field associations stay consistent with the check expression.

- Resolved deep link URLs being lost during SSO authentication, ensuring users are redirected to the intended resource after login.

- Enhanced ticket creation through flows to use the anomaly description as the ticket description, providing richer context for ServiceNow and Jira incidents.

- Improved Insights data reliability with a force refresh option, allowing users to manually trigger on-demand data updates for the latest quality metrics.

- Enhanced Observability tooltips with a day-over-day change indicator, displaying row count differences from the previous day for faster trend analysis.

- General Fixes and Improvements.

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


