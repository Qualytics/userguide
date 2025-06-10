# Anomalies

An anomaly in Qualytics is a data set (record or column) that fails to meet specified data quality checks, indicating a deviation from expected standards or norms. These anomalies are detected when the data does not satisfy the applied validation criteria, which could include both inferred and authored checks.

Let’s get started 🚀

## Anomaly Detection Process

The anomaly detection process in Qualytics ensures data quality and reliability through a series of systematic steps as discussed below.

### 1. Create a Datastore and Connection

By setting up a datastore and establishing a connection to your data source (database or file system), you create a robust foundation for effective data management and analysis in Qualytics. This setup enables you to access, manipulate, and utilize your data efficiently, paving the way for advanced data quality checks, profiling, scanning, anomaly surveillance, and other analytics tasks.

!!! note
    For more information, please refer to the documentation on [Configuring Datastores](../quick-start-guide.md/#datastore)

### 2. Catalog Operation

The Catalog operation involves systematically collecting data structures along with their corresponding metadata. This process also includes a thorough analysis of the existing metadata within the datastore. This ensures a solid foundation for the subsequent Profile and Scan operations.

!!! note
    For more information, please refer to the documentation [Catalog Operation](../source-datastore/catalog.md)

### 3. Profile Operation

The Profile operation enables training of the collected data structures and their associated metadata values. This is crucial for gathering comprehensive aggregating statistics on the selected data, providing deeper insights, and preparing the data for quality assessment.

!!! note
    For more information, please refer to the documentation [Profile Operation](../source-datastore/profile.md)

### 4. Create Authored Checks

Authored Checks are manually created data quality checks in Qualytics, defined by users either through the user interface (UI) or via API. These checks encapsulate specific data quality check, along with additional context such as associated notifications, tags, filters, and tolerances.

Authored checks can range from simple, template-based checks to more complex rules implemented through SQL or user-defined functions (UDFs) in Scala. By allowing users to define precise criteria for data quality, authored checks enable detailed monitoring and validation of data within the datastore, ensuring that it meets the specified standards and requirements.

!!! note
    For more information, please refer to the documentation [Checks](../explore/checks.md)

### 5. Scan Operation

The Scan operation asserts rigorous quality checks to identify any anomalies within the data. This step ensures data integrity and reliability by recording the analyzed data in your configured enrichment datastore, facilitating continuous data quality improvement.

!!! note
    For more information, please refer to the documentation [Scan Operation](../source-datastore/scan.md)

### 6. Anomaly Analysis

An Anomaly is a data record or column that fails a data quality check during a Scan Operation. These anomalies are identified through both Inferred and Authored Checks and are grouped together to highlight data quality issues. This process ensures that any deviations from expected data quality standards are promptly identified and addressed.

!!! note
    For more information, please refer to the documentation [Anomalies](#source-records).

## Types of Anomalies

Anomaly detection is categorized into two main types: Record Anomalies and Shape Anomalies. Both types play a crucial role in maintaining data integrity by identifying deviations at different levels of the dataset.

### Record Anomaly

A record anomaly identifies a single record (row) as anomalous and provides specific details regarding why it is considered anomalous. The simplest form of a record anomaly is a row that lacks an expected value for a field.

**Example:** Consider a data quality check that requires the salary field to be greater than 40,000. Based on this rule, any record that does not meet this condition will be identified and labeled as a record anomaly by Qualytics. In the sample table illustrated below, the row with id 6 will be flagged as a record anomaly because the salary of 30,000 is less than the required 40,000. This precise identification allows for targeted investigation and correction of specific data issues.

| ID | Name        | Age | Salary |
| -- | ----------- | --- | ------ |
| 1  | John Doe    | 28  | 50000  |
| 2  | Jane Smith  | 35  | 75000  |
| 3  | Bob Johnson | 22  | 45000  |
| 4  | Alice Brown | 30  | 60000  |
| 5  | John Wick   | 29  | 70000  |
| 6  | David White | 45  | 30000  |

### Shape Anomaly

A shape anomaly identifies anomalous structure within the analyzed data. The simplest shape anomaly is a dataset that doesn't match the expected schema because it lacks one or more fields. Some shape anomalies only apply to a subset of the data being analyzed and can therefore produce a count of the number of rows that reflect the anomalous concern. Where that is possible, the shape anomaly's ```anomalous_record_count``` is populated.

!!! note
    Sometimes, shape anomalies only affect a subset of the dataset. This means that only certain rows exhibit the structural issue, rather than the entire dataset.

!!! note
    When a shape anomaly affects only a portion of the dataset, Qualytics can count the number of rows that have the structural problem. This count is stored in the **anomalous_record_count** field, providing a clear measure of how widespread the issue is within the dataset. Example: Imagine a dataset that is supposed to have columns for **id**, **name**, **age**, and **salary**. If some rows are missing the **salary** column, this would be flagged as a shape anomaly. If this issue only affects 50 out of 1,000 rows, the **anomalous_record_count** would be 50, indicating that 50 rows have a structural issue.

## Anomaly Status

Anomaly status is a crucial feature for managing and addressing data quality issues. It provides a structured way to track and resolve anomalies detected in your data, ensuring that data integrity is maintained. Here's a breakdown of the different anomaly statuses:

**Active:** This status indicates that the data anomaly has been detected and is currently unresolved, requiring attention to address the underlying issue.  

**Acknowledged:** This status indicates that the anomaly has been verified as a legitimate data quality concern but has not yet been resolved.  

**Resolved:** This status indicates that the anomaly was a legitimate data quality concern that has been addressed and fixed.

**Duplicate:** This status indicates that the anomaly is a duplicate of an existing one, meaning it has already been reported and does not require separate action.

**Invalid:** This status indicates that the anomaly is not a legitimate data quality concern, possibly due to it being a false positive or an error in the detection process.

## Anomaly Details

The anomaly identified during the scan operation illustrates the following details:

**1. Anomaly ID:** A numerical identifier (e.g. #75566) used for quick search and easy identification of anomalies within the Qualytics interface.

**2. Status:** Reflects the status of the Anomaly. It can be **active**, **acknowledged**, **resolved**, **duplicate** or **invalid**.

**3. Share:** Copy a shareable link to a specific anomaly. This can be shared with other users or stakeholders for collaboration.

**4. Anomaly UID:** A longer, standardized, and globally unique identifier, displayed as a string of hexadecimal characters. This can be copied to the clipboard.

**5. Fingerprint:** The fingerprint icon indicates whether an anomaly has an associated fingerprint. If present, clicking the icon copies the fingerprint number to the clipboard. Hovering over the icon displays a tooltip with a link to the user guide.

**6. Acknowledge:** Use this option to mark an anomaly as reviewed. Acknowledging an anomaly means it has been identified and noted, but it remains active until resolved.

**7. Archive:** Use this option to remove an anomaly from the active list. Archiving an anomaly does not delete it but stores it for historical tracking and future reference.

**8. Type:** This reflects the **type** to which the anomaly belongs (e.g. Record or Shape).

**9. Weight:** A metric that indicates the severity or importance of the anomaly. Higher weights indicate more critical issues.

**10. Detected:** Reflects the **timestamp** when the anomaly was first detected.

**11. Scan:** Click on this to view the outcome of a data quality scan. It includes the scan status, the time taken, the user who triggered it, the schedule status, and a detailed list of anomalies detected across various tables.

![anomalies-details](../assets/datastores/anomalies/anomalies-details-light.png#only-light)
![anomalies-details](../assets/datastores/anomalies/anomalies-details-dark.png#only-dark)

In addition to the above details, the users can also explore the following additional details of the Anomaly:  

**1. Name:** This indicates the name of the source datastore where the anomaly was detected.

!!! tip
    Clicking on the expand icon opens a detailed view and navigates to the dataset’s page, providing more information about the source datastore where the anomaly was found.

**2. Table Name:** This specifies the particular table within the dataset that contains the anomaly. It helps in pinpointing the exact location of the data quality issue.

!!! tip
    Clicking on the expand icon navigates to the table’s page, providing more in-depth information about the table structure and contents.

**3. Location:** Full path or location within the data hierarchy where the table resides. It gives a complete reference to the exact position of the data in the database or data warehouse.

![details](../assets/datastores/anomalies/details-light.png#only-light)
![details](../assets/datastores/anomalies/details-dark.png#only-dark)

## Anomaly Fingerprints

Anomalies are uniquely fingerprinted to allow the system to recognize duplicates. This fingerprinting mechanism helps streamline anomaly management by preventing redundant work on identical problems.

### Duplicate Handling Configuration

When configuring a scan operation to identify anomalies in your data, you can specify how duplicates should be treated:

- **Duplicate Status**: You can select to set the status of newly identified anomalies that are identical to existing open anomalies to "duplicate" so that they will be automatically archived in favor of the existing anomaly.
- **Re-opening Option**: You can also optionally re-open any identical anomalies that were previously identified but marked archived.

### Fingerprinting Criteria

#### Record Anomalies

When record anomalies are fingerprinted, the system considers:

- The identifying check
- All source data from the anomalous record

!!! note
    Identical rows will generate identical anomalies.

#### Shape Anomalies

When shape anomalies are fingerprinted, the system considers:

- The identifying check(s)
- The percentage of asserted records that failed the check(s)
- The maximum value of the incremental identifier in the scanned dataset

!!! tip
    A data asset must have an incremental identifier to support fingerprinting of shape anomalies. This is because the maximum value of that identifier in the scanned dataset is used to generate the shape anomaly's fingerprint. This requirement helps ensure that only shape anomalies derived from the same underlying data are considered identical. Shape anomalies with the same details derived from different ranges of data are not considered identical.

## Source Records

The **Source Records** section displays all the data and fields related to the detected anomaly from the dataset. It is an **Enrichment Datastore** that is used to store the analyzed results, including any anomalies and additional metadata in files, hence it is recommended to add/link an enrichment datastore with your connected source datastore.

If the Anomaly Type is **Shape**, you will find the highlighted column(s) having anomalies in the source record.

![source-record](../assets/datastores/anomalies/source-record-light.png#only-light)
![source-record](../assets/datastores/anomalies/source-record-dark.png#only-dark)

If the Anomaly Type is **Record**, you will find the highlighted row(s) in the source record indicating failed checks. In the snippet below, it can be observed that 7 checks have been failed in the row.

![record](../assets/datastores/anomalies/record-light.png#only-light)
![record](../assets/datastores/anomalies/record-dark.png#only-dark)

!!! note
    In anomaly detection, source records are displayed as part of the Anomaly Details. For a Record anomaly, the specific record is highlighted. For a Shape anomaly, 10 samples from the underlying anomalous records are highlighted.

## Comparison Source Records

Anomalies identified by the **Is Replica Of** data quality rule type, configured with Row Identifiers, are displayed with a detailed source record comparison. This visualization highlights differences between rows, making it easier to identify specific discrepancies.

![in-replica](../assets/datastores/anomalies/in-replica-light.png#only-light)
![in-replica](../assets/datastores/anomalies/in-replica-dark.png#only-dark)

Structure of the Comparison Source Records:

**1. Left and Right Fields:**

Each field in the table is split into two columns: the left column represents the target table/file, while the right column represents the reference table/file.

If the value in the right column (reference) differs from the value in the left column (target), the cell is highlighted to indicate an anomalous value.

**2. _qualytics_diff Column:** This column provides the status of each row, which can be one of the following:

**Added:** The row is missing on the left side (target) but found on the right side (reference).

**Removed:** The row is present on the left side (target) but missing on the right side (reference).

**Changed:** The row is present on both sides, but there is at least one field value that differs between the target and reference.

### Suggested Remediation

**Suggested Remediation** is a feature that offers users recommended values to correct data anomalies identified during quality checks. In the snippet below, the **FIRST_CAREUNIT** field has failed the check, and Qualytics suggests **CSRU** as the remedial value.

![suggestion-details](../assets/datastores/anomalies/suggestion-details-light.png#only-light)
![suggestion-details](../assets/datastores/anomalies/suggestion-details-dark.png#only-dark)

### Failed Check Description

This allows users to view detailed explanations of each failed check by hovering over the information icon, helping users better understand the nature of the violation.

![failed-check-description](../assets/datastores/anomalies/failed-check-description-light.png#only-light)
![failed-check-description](../assets/datastores/anomalies/failed-check-description-dark.png#only-dark)

### Download Source Records

Download and export all source records (up to 250MB in a compressed .csv) for further analysis or external use.

![download-source-records](../assets/datastores/anomalies/download-source-records-light.png#only-light)
![download-source-records](../assets/datastores/anomalies/download-source-records-dark.png#only-dark)

## Assign Tags

Assigning tags to an anomaly serves the purpose of labeling and grouping anomalies and driving downstream workflows.

**Step 1:** Click on the **Assign tags to this Anomaly** or **+** button.

![assign-tags](../assets/datastores/anomalies/assign-tags-light.png#only-light)
![assign-tags](../assets/datastores/anomalies/assign-tags-dark.png#only-dark)

**Step 2:** A dropdown menu will appear with existing tags. Scroll through the list and click on the tag you wish to assign.

![updated-existing-tags](../assets/datastores/anomalies/updated-existing-tags-light.png#only-light)
![updated-existing-tags](../assets/datastores/anomalies/updated-existing-tags-dark.png#only-dark)

## Anomaly Actions

You can update the status of anomalies by acknowledging them to confirm they are real issues, or by moving them to archive if they are false positives. This helps refine the system’s detection process and keeps your worklist focused on relevant issues.

![anomalies-action](../assets/datastores/anomalies/anomalies-action-light.png#only-light)
![anomalies-action](../assets/datastores/anomalies/anomalies-action-dark.png#only-dark)

### Acknowledge Anomalies

You can acknowledge anomalies to confirm that they represent real data issues that need attention. By acknowledging an anomaly, you provide feedback to the system, validating the detection and helping it improve future checks.

For more details on how to acknowledge anomalies, please refer to the documentation on [Acknowledge Anomalies](./manage-anomalies.md/#acknowledge).

### Archive Anomalies

You can archive the anomalies when they are determined to be false positives or not significant. Archiving helps the system adjust its checks to prevent similar issues from being flagged in the future, ensuring more accurate anomaly detection and keeping your worklist streamlined.

For instance, if an anomaly is marked as invalid, the tolerances of the checks that identified the anomaly will be updated to prevent similar false positives in the future. This continuous feedback loop enhances the accuracy and relevance of data quality checks over time.

For more details on how to archive anomalies, please refer to the documentation on [Archive Anomalies](./manage-anomalies.md/#archived)

## API Payload Examples  

### Retrieving Anomaly by UUID or Id

**Endpoint (Get)**

```/api/anomalies/{id} (get)```

**Example Result Response**

```json
{
  "id": 0,
  "created": "2024-06-10T21:29:42.695Z",
  "uuid": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "type": "shape",
  "is_new": true,
  "archived": true,
  "status": "Active",
  "source_enriched": true,
  "datastore": {
    "id": 0,
    "name": "string",
    "store_type": "jdbc",
    "type": "athena",
    "enrich_only": true,
    "enrich_container_prefix": "string",
    "favorite": true
  },
  "container": {
    "id": 0,
    "name": "string",
    "container_type": "table",
    "table_type": "table"
  },
  "partition": {
    "name": "string",
    "location": "string"
  },
  "weight": 0,
  "global_tags": [
    {
      "type": "external",
      "name": "string",
      "color": "string",
      "description": "string",
      "weight_modifier": 0,
      "integration": {
        "id": 0,
        "created": "2024-06-10T21:29:42.696Z",
        "name": "string",
        "type": "atlan",
        "api_url": "string",
        "overwrite": true,
        "last_synced": "2024-06-10T21:29:42.696Z",
        "status": "syncing"
      }
    },
    {
      "type": "external",
      "name": "string",
      "color": "string",
      "description": "string",
      "weight_modifier": 0,
      "integration": {
        "id": 0,
        "created": "2024-06-10T21:29:42.696Z",
        "name": "string",
        "type": "atlan",
        "api_url": "string",
        "overwrite": true,
        "last_synced": "2024-06-10T21:29:42.696Z",
        "status": "syncing"
      }
    }
  ],
  "anomalous_records_count": 0,
  "comments": [
    {
      "id": 0,
      "created": "2024-06-10T21:29:42.696Z",
      "message": "string",
      "user": {
        "id": 0,
        "created": "2024-06-10T21:29:42.696Z",
        "user_id": "string",
        "email": "string",
        "name": "string",
        "picture": "string",
        "role": "Member",
        "deleted_at": "2024-06-10T21:29:42.696Z",
        "teams": [
          {
            "id": 0,
            "name": "string",
            "permission": "Read"
          }
        ]
      }
    }
  ],
  "failed_checks": [
    {
      "quality_check": {
        "id": 0,
        "created": "2024-06-10T21:29:42.696Z",
        "fields": [
          {
            "id": 0,
            "created": "2024-06-10T21:29:42.696Z",
            "name": "string",
            "type": "Unknown",
            "completeness": 0,
            "weight": 0,
            "global_tags": [
              {
                "type": "global",
                "name": "string",
                "color": "string",
                "description": "string",
                "weight_modifier": 0
              },
              {
                "type": "external",
                "name": "string",
                "color": "string",
                "description": "string",
                "weight_modifier": 0,
                "integration": {
                  "id": 0,
                  "created": "2024-06-10T21:29:42.697Z",
                  "name": "string",
                  "type": "atlan",
                  "api_url": "string",
                  "overwrite": true,
                  "last_synced": "2024-06-10T21:29:42.697Z",
                  "status": "syncing"
                }
              }
            ],
            "latest_profile_id": 0,
            "quality_score": {
              "total": 0,
              "completeness": 0,
              "coverage": 0,
              "conformity": 0,
              "consistency": 0,
              "precision": 0,
              "timeliness": 0,
              "volumetrics": 0,
              "accuracy": 0
            }
          }
        ],
        "description": "string",
        "rule_type": "afterDateTime",
        "coverage": 0,
        "inferred": true,
        "template_locked": true,
        "is_new": true,
        "num_container_scans": 0,
        "filter": "string",
        "properties": {
          "allow_other_fields": true,
          "assertion": "string",
          "comparison": "string",
          "datetime": "2024-06-10T21:29:42.697Z",
          "expression": "string",
          "field_name": "string",
          "field_type": "Unknown",
          "id_field_names": [
            "string"
          ],
          "inclusive": true,
          "inclusive_max": true,
          "inclusive_min": true,
          "interval_name": "Yearly",
          "last_value": 0,
          "list": [
            "string"
          ],
          "max": 0,
          "max_size": 0,
          "max_time": "2024-06-10T21:29:42.697Z",
          "min": 0,
          "min_size": 0,
          "min_time": "2024-06-10T21:29:42.697Z",
          "pattern": "string",
          "ref_container_id": 0,
          "ref_datastore_id": 0,
          "tolerance": 0,
          "value": 0,
          "ref_expression": "string",
          "ref_filter": "string",
          "required_labels": [
            "road"
          ],
          "numeric_comparator": {
            "epsilon": 0,
            "as_absolute": true
          },
          "duration_comparator": {
            "millis": 0
          },
          "string_comparator": {
            "ignore_whitespace": false
          },
          "distinct_field_name": "string",
          "pair_substrings": true,
          "pair_homophones": true,
          "spelling_similarity_threshold": 0
        },
        "template_checks_count": 0,
        "anomaly_count": 0,
        "type": "global",
        "name": "string",
        "color": "string",
        "description": "string",
        "weight_modifier": 0
      },
      {
        "type": "external",
        "name": "string",
        "color": "string",
        "description": "string",
        "weight_modifier": 0,
        "integration": {
          "id": 0,
          "created": "2024-06-10T21:29:42.697Z",
          "name": "string",
          "type": "atlan",
          "api_url": "string",
          "overwrite": true,
          "last_synced": "2024-06-10T21:29:42.697Z",
          "status": "syncing"
        }
      }
    ],
    "latest_profile_id": 0,
    "quality_score": {
      "total": 0,
      "completeness": 0,
      "coverage": 0,
      "conformity": 0,
      "consistency": 0,
      "precision": 0,
      "timeliness": 0,
      "volumetrics": 0,
      "accuracy": 0
    }
  }
],
  "description": "string",
  "rule_type": "afterDateTime",
  "coverage": 0,
  "inferred": true,
  "template_locked": true,
  "is_new": true,
  "num_container_scans": 0,
  "filter": "string",
  "properties": {
    "allow_other_fields": true,
    "assertion": "string",
    "comparison": "string",
    "datetime": "2024-06-10T21:29:42.697Z",
    "expression": "string",
    "field_name": "string",
    "field_type": "Unknown",
    "id_field_names": [
      "string"
    ],
    "inclusive": true,
    "inclusive_max": true,
    "inclusive_min": true,
    "interval_name": "Yearly",
    "last_value": 0,
    "list": [
      "string"
    ],
    "max": 0,
    "max_size": 0,
    "max_time": "2024-06-10T21:29:42.697Z",
    "min": 0,
    "min_size": 0,
    "min_time": "2024-06-10T21:29
}
```

### Retrieving Anomaly Source Records

**Endpoint (Get)**
```/api/anomalies/{id}/source-record (get)```

**Example Result Response**

```json
{
  "source_record":"[{\"_qualytics_entity_id\":0,\"COLUMN_1\": VALUE 1,\"COLUMN_2\":\" VALUE 1\"},{\"_qualytics_entity_id\":1234,\"COLUMN_1\": VALUE 2,\"COLUMN 2\":\"VALUE 2\"},{\"_qualytics_entity_id\":5678}]",
  "created":"2024-06-10T21:24:34.617296Z"
}
```
