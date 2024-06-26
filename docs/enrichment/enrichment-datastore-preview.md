# Data Preview

The "Data Preview" in the Enrichment section provides users with a streamlined preview of the enrichment tables, remediation tables and metadata, offering a direct view into its structure and contents.

To access the Data Preview section and explore container data within the platform, follow these steps:

1. **Navigate to Enrichment tab**

    Begin by navigating to your enrichment datastore within the platform.

* **Select a Specific Enrichment**

    From your datastore, select the specific enrichment whose data you want to preview.

* **Access Data Preview Tab**

    Ensure the selected Enrichment Datastore has data in it, navigate to the Data Preview tab within the specific linked Datastore.

    ![Screenshot](../assets/enrichment/data-preview/data-preview-light.png#only-light)
    ![Screenshot](../assets/enrichment/data-preview/data-preview-dark.png#only-dark)

## Explore Data Preview Features

In the Data Preview tab, users can access various features to interact with the data:

### Enrichment Data Tables

Users are able to see the data visualization of `_FAILED_CHECKS`, `_SOURCE_RECORDS`, `_SCAN_OPERATIONS` tables.

![Screenshot](../assets/enrichment/data-preview/failed-checks-light.png#only-light)
![Screenshot](../assets/enrichment/data-preview/failed-checks-dark.png#only-dark)

### Remediation Data Tables

Users are able to see the data visualization of remediation tables: `_{ENRICHMENT_CONTAINER_PREFIX}_REMEDIATION_{CONTAINER_ID}`.

![Screenshot](../assets/enrichment/data-preview/remediation-table-light.png#only-light)
![Screenshot](../assets/enrichment/data-preview/remediation-table-dark.png#only-dark)

### Metadata 

Users are able to see the metadata visualization from export containers.

![Screenshot](../assets/enrichment/data-preview/metadata-light.png#only-light)
![Screenshot](../assets/enrichment/data-preview/metadata-dark.png#only-dark)

### Unlinked

Users have visibility into unlinked objects that lack an association with the enrichment datastore. These objects, often referred to as 'orphaned,' are presented for review or consideration.

![Screenshot](../assets/enrichment/data-preview/unlinked-light.png#only-light)
![Screenshot](../assets/enrichment/data-preview/unlinked-dark.png#only-dark)

### Filter Input and Refresh

To enable users to focus on specific subsets of data, the Data Preview tab incorporates filter functionality. Users can apply filter clauses to the displayed data, refining the rows based on specific criteria. This feature enhances data analysis capabilities and allows for more targeted insights.

Utilize the filter input to refine the displayed rows based on specific criteria and `Refresh` the data to ensure you are viewing the latest information.

![Screenshot](../assets/container/data-preview/filter-refresh-2-light.png#only-light)
![Screenshot](../assets/container/data-preview/filter-refresh-2-dark.png#only-dark)

### Select Specific Fields

Choose specific fields to display, focusing on relevant data for analysis.

![Screenshot](../assets/container/data-preview/fields-to-show-light.png#only-light){: style="width:540px"}
![Screenshot](../assets/container/data-preview/fields-to-show-dark.png#only-dark){: style="width:540px"}

### Download Records

Download the data for further analysis or external use.

![Screenshot](../assets/container/data-preview/download-source-records-light.png#only-light){: style="width:440px"}
![Screenshot](../assets/container/data-preview/download-source-records-dark.png#only-dark){: style="width:440px"}

