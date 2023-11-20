# Export Metadata

Qualytics's metadata export feature is specifically designed to capture the mutable states of various data entities. This functionality enables the export of Quality Checks, Field Profiles, and Anomalies metadata from selected profiles into a designated enrichment datastore. For easy identification and organization, the exported metadata follows distinct naming patterns:

- **Anomalies**: stored as `_<datastore_name>_anomalies`.
- **Quality Checks**: stored as `_<datastore_name>_checks`.
- **Field Profiles**: stored as `_<datastore_name>_field_profiles`.

## Prerequisites

Before exporting, ensure the following prerequisite is met:

- **Enrichment Datastore Configured**: Have an enrichment datastore already set up and configured, capable of accommodating the exported data. This setup is required to enable the export process of anomalies, quality checks, and field profiles.

## Exporting to an Enrichment Datastore

Follow these steps to export the metadata:

1. **Access the Datastore Page**: Go to the Datastore page and locate the 'Enrichment Datastore' section, which should be present right below the breadcrumbs.
2. **Open Export Dialog**: In the Enrichment Datastore section, click on the 'Export Metadata' button to open the dialog.

    ![Screenshot](../assets/datastores/enrichment-datastore-export-icon-light.png#only-light){: style="width:676px"}
    ![Screenshot](../assets/datastores/enrichment-datastore-export-icon-dark.png#only-dark){: style="width:676px"}

3. **Choose Data to Export**: In the dialog, specify whether you want to export anomalies, quality checks, or field profiles.

    ![Screenshot](../assets/container/export-options-light.png#only-light){: style="width:676px"}
    ![Screenshot](../assets/container/export-options-dark.png#only-dark){: style="width:676px"}

4. **Profiles Selection**: Choose the profiles from which you wish to export data.

    ![Screenshot](../assets/container/export-profiles-light.png#only-light){: style="width:676px"}
    ![Screenshot](../assets/container/export-profiles-dark.png#only-dark){: style="width:676px"}

6. **Confirm Export**: Click the "Export" button in the dialog to begin the export process into the enrichment datastore.

    ![Screenshot](../assets/container/export-success-light.png#only-light){: style="width:676px"}
    ![Screenshot](../assets/container/export-success-dark.png#only-dark){: style="width:676px"}
