---
hide:
  - navigation
---

### 2023.06.24 { id="2023.06.24 }

#### Feature Enhancements

- Refactored Partiton Reads on JDBC 
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

- [**Explore**](/userguide/explore/global-explore/) is the new centralized view of Activities, Containers (Profiles, Tables, Computed Tables), Checks, Anomalies and Insights across ALL Datastores. This new view allows for filtering by Datastores & Tags, which will persist the filters across all of the submenu tabs. The goal is to help with Critical Data Elements and filtering out irrelevant information.
- Enhanced Navigation Features
    - The navigation tabs have been refined for increased user-friendliness.
    - Enhanced the Profile View and added toggle between card and list views.
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
- Catalog include filters
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
