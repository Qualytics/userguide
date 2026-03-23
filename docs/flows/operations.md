# Operation

Users can execute specific operations when the trigger activates. They can choose from the following options:

* Sync.

* Profile.

* Scan.

* Export.

* Materialize.

![operations](../assets/flows/actions-node/operations/operations.png)

!!! Warning
    Only initialized datastores appear in the **Source Datastore** dropdown across all operation types. A datastore becomes initialized after it has successfully completed **Sync**, **Profile**, and **Scan** runs at least once within the **Action Node Operation** section while setting up your flow.

![note](../assets/flows/actions-node/operations/note-flow.png)

## Sync

**Step 1:** Click on **Sync.**

![sync](../assets/flows/actions-node/operations/sync.png)

A panel **Sync Settings** will appear on the right-hand side. This window allows you to configure the sync operation.

| No. |                 Field |                 Description |
| :---- | :---- | :---- |
| 1. | Source Datastore | Select the source datastore to sync. |
| 2. | Prune | Checkbox to enable or disable the removal of named collections (tables, views, files, etc.) that no longer exist in the datastore. |
| 3. | Recreate | Checkbox to enable or disable the recreation of previously deleted named collections in Qualytics. |
| 4. | Include | Checkboxes to select Tables, Views, or both, specifying the resources to include in the sync. |

![sync](../assets/flows/actions-node/operations/sync-2.png)

**Step 2:** After configuring the settings, click Save to apply and proceed with the sync operation.

![save](../assets/flows/actions-node/operations/save-3.png)

## Profile

**Step 1:** Click on **Profile.**  

![profile](../assets/flows/actions-node/operations/profile.png)

A panel **Profile Settings** will appear on the right-hand side. This window allows you to configure the Profile operation.

![profile](../assets/flows/actions-node/operations/profile-2.png)

| No. |                    Field |    Description |
| :---- | :---- | :---- |
| 1. | Source Datastore | Select the source datastore to profile. |
| 2. | Select Tables | Allows users to select all tables, specific tables, or tables associated with selected tags to profile. |
| 3. | Read Settings | Configure the starting point for profiling and set a maximum record limit per table for profiling. |
| 4. | Inference Settings | Set the level of automated checks and decide whether inferred checks should be saved in draft mode. |

![profile](../assets/flows/actions-node/operations/profile-3.png)

**Step 2:** Click Save to finalize the profile configuration.

![save](../assets/flows/actions-node/operations/save-3.png)

## Scan

**Step 1:** Click on **Scan.**

![scan](../assets/flows/actions-node/operations/scan.png)

A panel **Scan Settings** will appear on the right-hand side. This window allows you to configure the Scan operation.  

![scan](../assets/flows/actions-node/operations/scan-2.png)

**Source Datastore:** Select the datastore to be scanned.

![scan](../assets/flows/actions-node/operations/scan-3.png)

**Select Tables:** Choose all tables, specific tables, or tables associated with selected tags to include in the scan.

![scan](../assets/flows/actions-node/operations/scan-4.png)

**Select Check Categories:** Select categories of checks to include, such as table properties (Metadata) or value checks (Data Integrity).

![scan](../assets/flows/actions-node/operations/scan-5.png)

**Read Settings:** Define the scan strategy: incremental scans updated records; full scans process all records.

![scan](../assets/flows/actions-node/operations/scan-8.png)

**Starting Threshold:** Set a starting point for scanning based on an incremental identifier.

![scan](../assets/flows/actions-node/operations/scan-6.png)

**Record Limit:** Specify the maximum number of records to scan per table.

![scan](../assets/flows/actions-node/operations/scan-7.png)

**Scan Settings:** Choose how to manage duplicate or recurring anomalies by archiving overlaps or reactivating previously archived anomalies with fingerprint tracking.

![scan](../assets/flows/actions-node/operations/scan-settings.png)

**Maximum Record Anomalies per Check:** Set the Rollup Threshold to limit how many anomalies are created per check. When the limit is reached, anomalies will be merged into one for easier management.

![rollup](../assets/flows/actions-node/operations/rollup.png)

**Maximum Source Examples per Anomaly:** Sets how many source records are kept per anomaly during a scan. **For example**, if this is set to **10**, only **10 records per anomaly will be saved or downloaded**. Increase this value before running the scan to access more records.

![scan](../assets/flows/actions-node/operations/scan-9.png)

**Step 2:** Click Save to finalize the scan configuration.

![save](../assets/flows/actions-node/operations/save.png)

## Export

**Step 1:** Click on **Export.**

![export](../assets/flows/actions-node/operations/export.png)

A panel **Export Settings** will appear on the right-hand side. This window allows you to configure the Export settings.

![panel](../assets/flows/actions-node/operations/export-setting.png)

**Source Datastore:** Select the datastore to export data from.

![source](../assets/flows/actions-node/operations/source.png)

**Select file patterns to export:** **All** (all file patterns, including future ones), **Specific** (manually chosen file patterns), or **Tag** (file patterns based on selected tags).

![profile](../assets/flows/actions-node/operations/profiles.png)

**Select Metadata:** Choose metadata to export **anomalies**, **quality checks**, or **field profiles**. Anomalies detect data issues, quality checks validate data, and field profiles store field metadata.

![exportt](../assets/flows/actions-node/operations/export-2.png)

**Step 2:** Click Save to finalize the export configuration.

![save](../assets/flows/actions-node/operations/save-3.png)

Export nodes display the asset type in their titles (e.g., “Export Anomalies”) to help you identify the exported content easily.

![export-status](../assets/flows/actions-node/operations/export-status.png)

## Materialize

**Step 1:** Click on **Materialize.**

![materialize](../assets/flows/actions-node/operations/materialize.png)

A panel **Materialize Settings** will appear on the right-hand side. This window allows you to configure the Materialize settings.

![setting](../assets/flows/actions-node/operations/setting.png)

**Source Datastore:** Select the datastore to materialize data from.

![source](../assets/flows/actions-node/operations/source-2.png)

**Select Tables:** Choose which tables (all, specific, or tagged) to extract from your source datastore and export to the enrichment datastore.

![select](../assets/flows/actions-node/operations/select.png)

**Read Settings:** Select the record limit to control how much data is materialized per table.

![read](../assets/flows/actions-node/operations/read.png)

**Step 2:** Click Save to finalize the materialize configuration.

![save](../assets/flows/actions-node/operations/save-2.png)