# Operation

Users can execute specific operations when the trigger activates. They can choose from the following options:

* Catalog.

* Profile.

* Scan.

* Export.

* Materialize.

![operations](../assets/flows/operations-light-24.png)

!!! Warning
    Only initialized datastores appear in the **Source Datastore** dropdown across all operation types. A datastore becomes initialized after it has successfully completed **Catalog**, **Profile**, and **Scan** runs at least once within the **Action Node Operation** section while setting up your flow.

![note](../assets/flows/note-flow.png)

## Catalog

**Step 1:** Click on **Catalog.**  

![catalog](../assets/flows/catalog-light-25.png)

A panel **Catalog Settings** will appear on the right-hand side. This window allows you to configure the catalog operation.

| No. |                 Field |                 Description |
| :---- | :---- | :---- |
| 1. | Source Datastore | Select the source datastore to catalog. |
| 2. | Prune | Checkbox to enable or disable the removal of named collections (tables, views, files, etc.) that no longer exist in the datastore. |
| 3. | Recreate | Checkbox to enable or disable the recreation of previously deleted named collections in Qualytics for the catalog. |
| 4. | Include | Checkboxes to select Tables, Views, or both, specifying the resources to include in the catalog. |

![catalog](../assets/flows/catalog-light-26.png)

**Step 2:** After configuring the settings, click Save to apply and proceed with the catalog operation.

![save](../assets/flows/save-light-8.png)

## Profile

**Step 1:** Click on **Profile.**  

![profile](../assets/flows/profile-light-28.png)

A panel **Profile Settings** will appear on the right-hand side. This window allows you to configure the Profile operation.

![profile](../assets/flows/profile-light-29.png)

| No. |                    Field |    Description |
| :---- | :---- | :---- |
| 1. | Source Datastore | Select the source datastore to profile. |
| 2. | Select Tables | Allows users to select all tables, specific tables, or tables associated with selected tags to profile. |
| 3. | Read Settings | Configure the starting point for profiling and set a maximum record limit per table for profiling. |
| 4. | Inference Settings | Set the level of automated checks and decide whether inferred checks should be saved in draft mode. |

![profile](../assets/flows/profile-light-30.png)

**Step 2:** Click Save to finalize the profile configuration.

![save](../assets/flows/save-light-8.png)

## Scan

**Step 1:** Click on **Scan.**

![scan](../assets/flows/scan-light-32.png)

A panel **Scan Settings** will appear on the right-hand side. This window allows you to configure the Scan operation.  

![scan](../assets/flows/scan-light-33.png)

**Source Datastore:** Select the datastore to be scanned.

![scan](../assets/flows/scan-light-34.png)

**Select Tables:** Choose all tables, specific tables, or tables associated with selected tags to include in the scan.

![scan](../assets/flows/scan-light-35.png)

**Select Check Categories:** Select categories of checks to include, such as table properties (Metadata) or value checks (Data Integrity).

![scan](../assets/flows/scan-light-36.png)

**Read Settings:** Define the scan strategy: incremental scans updated records; full scans process all records.

![scan](../assets/flows/scan-light-39.png)

**Starting Threshold:** Set a starting point for scanning based on an incremental identifier.

![scan](../assets/flows/scan-light-37.png)

**Record Limit:** Specify the maximum number of records to scan per table.

![scan](../assets/flows/scan-light-38.png)

**Scan Settings:** Choose how to manage duplicate or recurring anomalies by archiving overlaps or reactivating previously archived anomalies with fingerprint tracking.

![scan](../assets/flows/scan-settings-light.png)

**Anomaly Rollup Threshold:** Set the Rollup Threshold to limit how many anomalies are created per check. When the limit is reached, anomalies will be merged into one for easier management.

![rollup](../assets/flows/rollup-light-39.png)

**Enrichment Source Record Limit:** Define the number of source records to include in the enrichment operation.

![scan](../assets/flows/scan-light-40.png)

**Step 2:** Click Save to finalize the scan configuration.

![save](../assets/flows/save-light-43.png)

## Export

**Step 1:** Click on **Export.**

![export](../assets/flows/export-light.png)

A panel **Export Settings** will appear on the right-hand side. This window allows you to configure the Export settings.

![panel](../assets/flows/export-setting-light.png)

**Source Datastore:** Select the datastore to export data from.

![source](../assets/flows/source-light.png)

**Select file patterns to export:** **All** (all file patterns, including future ones), **Specific** (manually chosen file patterns), or **Tag** (file patterns based on selected tags).

![profile](../assets/flows/profiles-light.png)

**Select Metadata:** Choose metadata to export **anomalies**, **quality checks**, or **field profiles**. Anomalies detect data issues, quality checks validate data, and field profiles store field metadata.

![exportt](../assets/flows/exportt-light.png)

**Step 2:** Click Save to finalize the export configuration.

![save](../assets/flows/save-light-8.png)

Export nodes display the asset type in their titles (e.g., “Export Anomalies”) to help you identify the exported content easily.

![export-status](../assets/flows/export-status-light.png)

## Materialize

**Step 1:** Click on **Materialize.**

![materialize](../assets/flows/materialize-light.png)

A panel **Materialize Settings** will appear on the right-hand side. This window allows you to configure the Materialize settings.

![setting](../assets/flows/setting-light.png)

**Source Datastore:** Select the datastore to materialize data from.

![source](../assets/flows/sourcee-light.png)

**Select Tables:** Choose which tables (all, specific, or tagged) to extract from your source datastore and export to the enrichment datastore.

![select](../assets/flows/select-light.png)

**Read Settings:** Select the record limit to control how much data is materialized per table.

![read](../assets/flows/read-light.png)

**Step 2:** Click Save to finalize the materialize configuration.

![save](../assets/flows/saveee-light.png)