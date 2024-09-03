#  Export Metadata

Qualytics’ metadata export feature lets you capture the changing states of your data. You can export metadata for Quality Checks, Field Profiles, and Anomalies from selected profiles into an enrichment datastore so that you can perform deeper analysis, identify trends, detect issues, and make informed decisions based on your data.

To keep things organized, the exported files use specific naming patterns:

- **Anomalies:** Saved as `_<enrichment_prefix>_anomalies_export`.
- **Quality Checks:** Saved as `_<enrichment_prefix>_checks_export`.
- **Field Profiles:** Saved as `_<enrichment_prefix>_field_profiles_export`.

!!! note
    Ensure that an enrichment datastore is already set up and properly configured to accommodate the exported data. This setup is essential for exporting anomalies, quality checks, and field profiles successfully. 

Let’s get started 🚀

**Step 1:** Select a source datastore from the side menu from which you would like to export the metadata.

![select-source](../assets/container/export-metadata/select-source-light-1.png#only-light)
![select-source](../assets/container/export-metadata/select-source-dark-1.png#only-dark)

For demonstration purposes, we have selected the **“COVID-19 Data”** Snowflake source datastores.

![covid-19](../assets/container/export-metadata/covid-19-light-2.png#only-light)
![covid-19](../assets/container/export-metadata/covid-19-dark-2.png#only-dark)

**Step 2:** After selecting your preferred datastore, a bottom-up menu will appear on the right side of the interface. Click on **“Export Metadata”** alongside the Enrichment Datastore.

![export-metadata](../assets/container/export-metadata/export-metadata-light-3.png#only-light)
![export-metadata](../assets/container/export-metadata/export-metadata-dark-3.png#only-dark)

**Step 3:** After clicking **“Export Metadata,”** a modal window will appear providing you the options to select the assets you want to export to your Enrichment Datastore—whether it's **anomalies**, **quality checks**, or **field profiles**.

![modal-window](../assets/container/export-metadata/modal-window-light-4.png#only-light)
![modal-window](../assets/container/export-metadata/modal-window-dark-4.png#only-dark)

For demonstration purposes, we have opted to export all three assets: **Anomalies**, **Quality Checks**, and **Field Profiles**.

![modal-window](../assets/container/export-metadata/modal-window-light-5.png#only-light)
![modal-window](../assets/container/export-metadata/modal-window-dark-5.png#only-dark)

**Step 4:** Once you have selected the assets, click the **“Next”** button to continue.

![next-button](../assets/container/export-metadata/next-button-light-6.png#only-light)
![next-button](../assets/container/export-metadata/next-button-dark-6.png#only-dark)

**Step 5:** Select the profiles you wish to export. You can choose specific profiles or export them all at once. After selection, click on the **Export** button.

![export-button](../assets/container/export-metadata/export-button-light-7.png#only-light)
![export-button](../assets/container/export-metadata/export-button-dark-7.png#only-dark)

For demonstration purposes, we have checked the **“All”** option.

![all-option](../assets/container/export-metadata/all-option-light-8.png#only-light)
![all-option](../assets/container/export-metadata/all-option-dark-8.png#only-dark)

**Step 6:** After clicking **“Export,”** the process starts, and a message will confirm that the metadata will be available in your Enrichment Datastore shortly.

![message](../assets/container/export-metadata/message-light-9.png#only-light)
![message](../assets/container/export-metadata/message-dark-9.png#only-dark)

## Review Exported Metadata

**Step 1:** Once the metadata has been exported, navigate to the **“Enrichment Datastores”** located on the left menu.

![enrichment](../assets/container/export-metadata/enrichment-light-10.png#only-light)
![enrichment](../assets/container/export-metadata/enrichment-dark-10.png#only-dark)

**Step 8:** In the **“Enrichment Datastores”** section, select the datastore where you exported the metadata. The exported metadata will now be visible in the selected datastore.

![exported](../assets/container/export-metadata/exported-light-11.png#only-light)
![exported](../assets/container/export-metadata/exported-dark-11.png#only-dark)

**Step 9:** Click on the exported files to view the metadata. For demonstration purposes, we have selected the **“export_field_profiles”** file to review the metadata.

The exported metadata is displayed in a table format, showing key details about the field profiles from the datastore. It typically includes columns that indicate the uniqueness of data, the completeness of the fields, and the data structure. You can use this metadata to check data quality, prepare for analysis, ensure compliance, and manage your data.

![example](../assets/container/export-metadata/example-light-12.png#only-light)
![example](../assets/container/export-metadata/example-dark-12.png#only-dark)
