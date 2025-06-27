# Source Records

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

![tag](../assets/explore/anomalies/assign-light.png#only-light)
![tag](../assets/explore/anomalies/assign-dark.png#only-dark)

**Step 2:** A dropdown menu will appear with existing tags. Scroll through the list and click on the tag you wish to assign.

![scroll](../assets/explore/anomalies/tag-light.png#only-light)
![scroll](../assets/explore/anomalies/tag-dark.png#only-dark)