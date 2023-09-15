---
hide:
  - navigation
---

### 2023.09.15 { id=2023.09.15}

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

### 2023.09.06 { id=2023.09.06 }

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


### 2023.06.24 { id="2023.06.24 }

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


### 2023.06.20 { id="2023.06.20 }

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

### 2023.06.12 { id="2023.06.12" }

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

### 2023.06.02 { id="2023.06.02" }
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
    
### 2023.05.26 { id="2023.05.26" }
#### Usability

- Improved the navigation in the Activity tab’s side panel for easier and more intuitive browsing including exposing the ability to comment directly into an anomaly
- Added a redirect to the Activity tab when an operation is initiated for a smoother workflow.

#### Bug Fixes
- Resolved an issue where the date and time were not displaying correctly for the highest value in profiles.
- Fixed a problem with scheduled operations when the configured timing was corrupted.
- Addressed an issue where filtered checks were causing unexpected errors outside of the intended dataset.

### 2023.05.23 { id="2023.05.23" }
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


### 2023.04.19 { id="2023.04.19" }

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


### 2023.04.07 { id="2023.04.07" }

#### Feature Enhancements

- We've just deployed an MVP version of the Freshness Dashboard! This feature lets you create, manage, and monitor all of the SLAs for each of your datastores and their child files/tables/containers, all in one place. It's like having a birds-eye view of how your datastores are doing in relation to their freshness.
    - To access the Freshness Dashboard, just locate and click on the clock icon in the top navigation between Insights and Anomalies. By default, you'll see a rollup of all the datastores in a list view with their child files/tables/containers collapsed. Simply click on a datastore row to expand the list.
- We've also made some improvements to the UI, including more sorting and filtering options in Datastores, Files/Tables, Checks, and Anomalies. Plus, we've added the ability to search the description field in checks, making it easier to find what you're looking for.
- And last but not least, we've added a cool new feature to checks - the ability to archive ALL anomalies generated by a check. Simply click on the anomaly warning icon at the top of the check details box to bring up the archive anomalies dialog box.
