# BigQuery

Adding and configuring BigQuery connection within Qualytics empowers the platform to build a symbolic link with your schema to perform operations like data discovery, visualization, reporting, cataloging, profiling, scanning, anomaly surveillance, and more.  

This documentation provides a step-by-step guide on adding BigQuery as both a source and enrichment datastore in Qualytics. It covers the entire process, from initial connection setup to testing and finalizing the configuration. 

By following these instructions, enterprises can ensure their BigQuery environment is properly connected with Qualytics, unlocking the platform's potential to help you proactively manage your full data quality lifecycle.

Let's get started 🚀

## BigQuery Setup Guide 

This guide explains how to create and use a temporary dataset with an expiration time in BigQuery. This dataset helps manage intermediate query results and temporary tables when using the Google BigQuery JDBC driver.

It is recommended for efficient data management, performance optimization, and automatic reduction of storage costs by deleting data when it is no longer needed.

### Access the BigQuery Console

**Step 1:** Navigate to the BigQuery console within your Google Cloud Platform (GCP) account.

![google-cloud-platform-page](../assets/datastores/bigquery/google-cloud-platform-page.png)

**Step 2:**  Click on the **vertical ellipsis**, it will open a popup menu for creating a dataset.
Click on the **Create dataset** to set up a new dataset.

![create-a-dataset](../assets/datastores/bigquery/create-a-dataset.png)

**Step 3:** Fill details for the following fields to create a new dataset.

!!! info 
    - **Dataset Location:** Select the location that aligns with where your other datasets reside to minimize data transfer delays.
    - **Default Table Expiration:** Set the expiration to `1 day` to ensure any table created in this dataset is automatically deleted one day after its creation.

![configure-dataset-details](../assets/datastores/bigquery/configure-dataset-details.png)
 
**Step 4:** Click the **Create Dataset** button to apply the configuration and create the dataset.

![create-dataset-button](../assets/datastores/bigquery/create-dataset-button.png)

**Step 5:** Navigate to the **created dataset** and find the **Dataset ID** in the **Dataset Info**.

![created-dataset-page](../assets/datastores/bigquery/created-dataset-page.png)

The dataset Info section contains the Dataset ID and other information related to the created dataset. This generated Dataset ID is used to configure the BigQuery datastore.

### BigQuery Roles and Permissions
 
This section explains the roles required for viewing, editing, and running jobs in BigQuery. To integrate BigQuery with Qualytics, you need specific roles and permissions. 

Assigning these roles ensures Qualytics can perform data discovery, management, and analytics tasks efficiently while maintaining security and access control.

#### BigQuery Roles 

- **BigQuery Data Editor (`roles/bigquery.dataEditor`)**
    Allows modification of data within BigQuery, including adding new tables and changing table schemas. It is suitable if you want to regularly update or insert data.

- **BigQuery Data Viewer (`roles/bigquery.dataViewer`)**
    Enables viewing datasets, tables, and the contents. It is essential if you need to read data structures and information.

- **BigQuery Job User (`roles/bigquery.jobUser`)**
    Allows creating and managing jobs in BigQuery, such as queries, data imports, and data exports. It is important if you want to run automated queries.

- **BigQuery Read Session User (`roles/bigquery.readSessionUser`)**
    Allows usage of the BigQuery Storage API for efficient retrieval of large data volumes. It provides capabilities to create and manage read sessions, facilitating large-scale data transfers.

### Datastore BigQuery Privileges

The following table outlines the privileges associated with BigQuery roles when configuring datastore connections in Qualytics:

#### Source Datastore Permissions (Read-Only)

Provides read access to view table data and metadata:

| REF | READ-ONLY PERMISSIONS | DESCRIPTION |
| --- | ---------------------- | ----------- |
| 1.  | `roles/bigquery.dataViewer` | Allows viewing of datasets, tables, and their data. |
| 2.  | `roles/bigquery.jobUser` | Enables running of jobs such as queries and data loading. |
| 3.  | `roles/bigquery.readSessionUser` | Facilitates the creation of read sessions for efficient data retrieval. |

#### Enrichment Datastore Permissions (Read-Write)

Grants read and write access for data editing and management:

| REF | WRITE-ONLY PERMISSIONS | DESCRIPTION |
| ----| ----------------------- | ----------- |
| 1.  | `roles/bigquery.dataEditor` | Provides editing permissions for table data and schemas. |
| 2.  | `roles/bigquery.dataViewer` | Allows viewing of datasets, tables, and their data. |
| 3.  | `roles/bigquery.jobUser` | Enables running of jobs such as queries and data loading. |
| 4.  | `roles/bigquery.readSessionUser` | Facilitates the creation of read sessions for efficient data retrieval. |

## Add a Source Datastore

A source datastore is a storage location used to connect to and access data from external sources. BigQuery is an example of a source datastore, specifically a type of JDBC datastore that supports connectivity through the JDBC API. Configuring the JDBC datastore enables the Qualytics platform to access and perform operations on the data, thereby generating valuable insights.

**Step 1:** Log in to your Qualytics account and click on the **Add Source Datastore** button located at the top-right corner of the interface. 

![add-datastore](../assets/datastores/bigquery/add-datastore-light.png#only-light)
![add-datastore](../assets/datastores/bigquery/add-datastore-dark.png#only-dark)

**Step 2:** A modal window- **Add Datastore** will appear, providing you with the options to connect a datastore.

![select-a-connector](../assets/datastores/bigquery/select-a-connector-light.png#only-light)
![select-a-connector](../assets/datastores/bigquery/select-a-connector-dark.png#only-dark)


| REF. | FIELDS          | ACTIONS                                                                                     |
|------|-----------------|---------------------------------------------------------------------------------------------|
| 1️.   | Name (Required)  | Specify the name of the datastore (e.g. The specified name will appear on the datastore cards.) |
| 2️.  | Toggle Button   | Toggle ON to reuse credentials from an existing connection, or toggle OFF to create a new source datastore from scratch. |
| 3.    | Connector (Required) | Select **BigQuery** from the dropdown list.                                                    |

### Option I: Create a Source Datastore with a new Connection

If the toggle for **Use an existing connection** is turned off, then this will prompt you to add and configure the source datastore from scratch without using existing connection details.

**Step 1:** Select the **BigQuery** connector from the dropdown list and add connection details such as temp dataset ID, service account key, project ID, and dataset ID.

![add-datastore-credentials](../assets/datastores/bigquery/add-datastore-credentials-light.png#only-light)
![add-datastore-credentials](../assets/datastores/bigquery/add-datastore-credentials-dark.png#only-dark)

**Step 2:** The configuration form will expand, requesting credential details before establishing the connection.

![add-datastore-credentials-explain](../assets/datastores/bigquery/add-datastore-credentials-explain-light.png#only-light)
![add-datastore-credentials-explain](../assets/datastores/bigquery/add-datastore-credentials-explain-dark.png#only-dark)

| REF. | FIELDS                               | ACTIONS                                                                                      |
|------|--------------------------------------|----------------------------------------------------------------------------------------------|
|   1.   | Temp Dataset ID (Optional)           | Enter a temporary Dataset ID for intermediate data storage during BigQuery operations.        |
|   2.   | [Service Account Key](https://cloud.google.com/iam/docs/keys-create-delete){:target="_blank"} (Required)   | Upload a JSON file that contains the credentials required for accessing BigQuery.             |
|   3.   | [Project ID](https://support.google.com/googleapi/answer/7014113?hl=en&ref_topic=7014522){:target="_blank"} (Required)                 | Enter the Project ID associated with BigQuery.                                                |
|   4.   | Dataset ID (Required)                | Enter the Dataset ID (schema name) associated with BigQuery.                                  |
|   5.   | Teams (Required)                     | Select one or more teams from the dropdown to associate with this source datastore.            |
|   6.   | Initial Cataloging (Optional)        | Tick the checkbox to automatically perform catalog operation on the configured source datastore to gather data structures and corresponding metadata. |

**Step 3:** After adding the source datastore details, click on the **Test Connection** button to check and verify its connection.

![test-datastore-connection](../assets/datastores/bigquery/test-datastore-connection-light.png#only-light)
![test-datastore-connection](../assets/datastores/bigquery/test-datastore-connection-dark.png#only-dark)

If the credentials and provided details are verified, a success message will be displayed indicating that the connection has been verified. 

### Option II: Use an Existing Connection

If the toggle for **Use an existing connection** is turned on, then this will prompt you to configure the source datastore using the existing connection details.

**Step 1:** Select a **connection** to reuse existing credentials.

![use-existing-datastore](../assets/datastores/bigquery/use-existing-datastore-light.png#only-light)
![use-existing-datastore](../assets/datastores/bigquery/use-existing-datastore-dark.png#only-dark)

!!! note
    If you are using existing credentials, you can only edit the details such as Project ID, Dataset ID, Teams, and Initiate Cataloging. 

**Step 2:** Click on the **Test Connection** button to verify the existing connection details. If connection details are verified, a success message will be displayed.

![test-connection-for-existing-datastore](../assets/datastores/bigquery/test-connection-for-existing-datastore-light.png#only-light)
![test-connection-for-existing-datastore](../assets/datastores/bigquery/test-connection-for-existing-datastore-dark.png#only-dark)

!!! note 
    Clicking on the **Finish** button will create the source datastore and bypass the **enrichment datastore** configuration step.

!!! tip
    It is recommended to click on the **Next** button, which will take you to the **enrichment datastore** configuration page.

## Add Enrichment Datastore

Once you have successfully tested and verified your source datastore connection, you have the option to add the enrichment datastore (recommended). The enrichment datastore is used to store the analyzed results, including any anomalies and additional metadata in tables. This setup provides full visibility into your data quality, helping you manage and improve it effectively.

**Step 1:** Whether you have added a source datastore by creating a new datastore connection or using an existing connection, click on the **Next** button to start adding the **Enrichment Datastore**.

![next-button-for-enrichment](../assets/datastores/bigquery/next-button-for-enrichment-light.png#only-light)
![next-button-for-enrichment](../assets/datastores/bigquery/next-button-for-enrichment-dark.png#only-dark)

**Step 2:** A modal window- **Add Enrichment Datastore** will appear, providing you with the options to configure to add an **enrichment datastore**.

![select-enrichment-connector](../assets/datastores/bigquery/select-enrichment-connector-light.png#only-light)
![select-enrichment-connector](../assets/datastores/bigquery/select-enrichment-connector-dark.png#only-dark)

| REF. | FIELDS                                           | ACTIONS                                                                                     |
|------|--------------------------------------------------|---------------------------------------------------------------------------------------------|
|   1.  | Prefix (Required)                                | Add a prefix name to uniquely identify tables/files when Qualytics writes metadata for your selected datastore. |
|   2.  | Toggle Button for existing enrichment datastore   | Toggle ON to link the source datastore to an existing enrichment datastore, or toggle OFF to link it to a brand new enrichment datastore. |
|   3.  | Name (Required)                                  | Give a name for the enrichment datastore.                                                   |
|   4.  | Toggle Button for using an existing connection   | Toggle ON to reuse credentials from an existing connection, or toggle OFF to create a new enrichment from scratch. |
|   5.   | Connector (Required)                             | Select a datastore connector as **BigQuery** from the dropdown list.                          |

### Option I: Create an Enrichment Datastore with a new Connection

If the toggles for **Use an existing enrichment datastore** and **Use an existing connection** are turned off, then this will prompt you to add and configure the enrichment datastore from scratch without using an existing enrichment datastore and its connection details.

**Step 1:** Add connection details for your selected **enrichment datastore** connector.

![enrichment-datastore-explain](../assets/datastores/bigquery/enrichment-datastore-explain-light.png#only-light)
![enrichment-datastore-explain](../assets/datastores/bigquery/enrichment-datastore-explain-dark.png#only-dark)

| REF. | FIELDS                           | ACTIONS                                                                                      |
|------|----------------------------------|----------------------------------------------------------------------------------------------|
|   1.   | Temp Dataset ID (Optional)       | Enter a temporary Dataset ID for intermediate data storage during BigQuery operations.        |
|   2.  | [Service Account Key](https://cloud.google.com/iam/docs/keys-create-delete){:target="_blank"} (Required)   | Upload a JSON file that contains the credentials required for accessing BigQuery.             |
|   3.   | [Project ID](https://support.google.com/googleapi/answer/7014113?hl=en&ref_topic=7014522){:target="_blank"} (Required)            | Enter the Project ID associated with BigQuery.                                                |
|   4.   | Dataset ID (Required)            | Enter the Dataset ID (schema name) associated with BigQuery.                                  |
|   5.   | Teams (Required)                 | Select one or more teams from the dropdown to associate with this source datastore.            |

**Step 2:** Click on the **Test Connection** button to verify the selected enrichment datastore connection. If the connection is verified, a flash message will indicate that the connection with the enrichment datastore has been successfully verified. 

![test-connection-for-enrichment-datastore](../assets/datastores/bigquery/test-connection-for-enrichment-datastore-light.png#only-light)
![test-connection-for-enrichment-datastore](../assets/datastores/bigquery/test-connection-for-enrichment-datastore-dark.png#only-dark)

**Step 3:** Click on the **Finish** button to complete the configuration process. 

![finish-configuration](../assets/datastores/bigquery/finish-configuration-light.png#only-light)
![finish-configuration](../assets/datastores/bigquery/finish-configuration-dark.png#only-dark)

When the configuration process is finished, a modal will display a **success message** indicating that **your datastore has been successfully added**.

![success-message](../assets/datastores/bigquery/success-message-light.png#only-light)
![success-message](../assets/datastores/bigquery/success-message-dark.png#only-dark)

**Step 4:** Close the Success dialogue and the page will automatically redirect you to the **Source Datastore Details** page where you can perform data operations on your configured **source datastore**.

![data-operation-page](../assets/datastores/bigquery/data-operation-page-light.png#only-light)
![data-operation-page](../assets/datastores/bigquery/data-operation-page-dark.png#only-dark)

### Option II: Use an Existing Connection

If the toggle for **Use an existing enrichment datastore** is turned on, you will be prompted to configure the datastore using existing connection details.

**Step 1:** Add a prefix name and select an existing enrichment datastore from the dropdown list.

![select-existing-enrichment-datastore](../assets/datastores/bigquery/select-existing-enrichment-datastore-light.png#only-light)
![select-existing-enrichment-datastore](../assets/datastores/bigquery/select-existing-enrichment-datastore-dark.png#only-dark)

| REF. | FIELDS                                           | ACTIONS                                                                                     |
|------|--------------------------------------------------|---------------------------------------------------------------------------------------------|
|   1.   | Prefix (Required)                                | Add a prefix name to uniquely identify tables/files when Qualytics writes metadata from the source datastore to your enrichment datastore. |
|  2.   | Toggle Button for existing enrichment datastore   | Toggle ON to link the source datastore to an existing enrichment datastore.                  |
|  3.  | Enrichment Datastore                             | Select an enrichment datastore from the dropdown list.                                       |

**Step 2:** After selecting an existing **enrichment datastore** connection, you will view the following details related to the selected enrichment: 

- **Teams:** The team associated with managing the enrichment datastore is based on the role of public or private. Example- Marked as **Public** means that this datastore is accessible to all the users. 

- **Host:** This is the server address where the **BigQuery** instance is hosted. It is the endpoint used to connect to the BigQuery environment. 

- **Database:** Refers to the specific database within the BigQuery environment where the data is stored.

- **Schema:** The schema used in the enrichment datastore. The schema is a logical grouping of database objects (tables, views, etc.). Each schema belongs to a single database.

![use-existing-enrichment-datastore](../assets/datastores/bigquery/use-existing-enrichment-datastore-light.png#only-light)
![use-existing-enrichment-datastore](../assets/datastores/bigquery/use-existing-enrichment-datastore-dark.png#only-dark)

**Step 3:** Click on the **Finish** button to complete the configuration process for the existing **enrichment datastore**.

![finish-configuration-for-existing-enrichment-datastore](../assets/datastores/bigquery/finish-configuration-for-existing-enrichment-datastore-light.png#only-light)
![finish-configuration-for-existing-enrichment-datastore](../assets/datastores/bigquery/finish-configuration-for-existing-enrichment-datastore-dark.png#only-dark)

When the configuration process is finished, a modal will display a **success message** indicating that **your data has been successfully added**.

![success-message](../assets/datastores/bigquery/success-message-light.png#only-light)
![success-message](../assets/datastores/bigquery/success-message-dark.png#only-dark)

Close the success message and you will be automatically redirected to the **Source Datastore Details** page where you can perform data operations on your configured **source datastore**.

![data-operation-page](../assets/datastores/bigquery/data-operation-page-light.png#only-light)
![data-operation-page](../assets/datastores/bigquery/data-operation-page-dark.png#only-dark)

## API Payload Examples

This section provides detailed examples of API payloads to guide you through the process of creating and managing datastores using Qualytics API. Each example includes endpoint details, sample payloads, and instructions on how to replace placeholder values with actual data relevant to your setup.

### Creating a Source Datastore

This section provides sample payloads for creating a BigQuery datastore. Replace the placeholder values with actual data relevant to your setup.

**Endpoint:** `/api/datastores (post)`

=== "Create a Datastore with a new Connection"
    ```json
        {
            "name": "your_datastore_name",
            "teams": ["Public"],
            "database": "your_project_id",
            "schema": "your_dataset_id",
            "enrich_only": false,
            "trigger_catalog": true,
            "connection": {
                "name": "your_connection_name",
                "type": "bigquery",
                "password": "your_service_account_key"
            }
        }
    ```
=== "Create a Source Datastore with an existing Connection"
    ```json
        {
            "name": "your_datastore_name",
            "teams": ["Public"],
            "database": "your_project_id",
            "schema": "your_dataset_id",
            "enrich_only": false,
            "trigger_catalog": true,
            "connection_id": connection-id
        }
    ```
### Creating an Enrichment Datastore

This section provides sample payloads for creating an enrichment datastore. Replace the placeholder values with actual data relevant to your setup.

**Endpoint:**  `/api/datastores (post)`

=== "Create an Enrichment Datastore with a new Connection"
    ```json
        {
            "name": "your_datastore_name",
            "teams": ["Public"],
            "database": "your_project_id",
            "schema": "your_enrichment_dataset_id",
            "enrich_only": true,
            "connection": {
                "name": "your_connection_name",
                "type": "bigquery",
                "password": "your_service_account_key"
            }
        }
    ```
=== "Create an Enrichment Datastore with an Existing Connection"
    ```json
        {
            "name": "your_datastore_name",
            "teams": ["Public"],
            "database": "your_project_id",
            "schema": "your_enrichment_dataset_id",
            "enrich_only": true,
            "connection_id": connection-id
        }
    ```
### Link an Enrichment Datastore to a Source Datastore

Use the provided endpoint to link an enrichment datastore to a source datastore: 

**Endpoint Details:** `/api/datastores/{datastore-id}/enrichment/{enrichment-id} (patch)`

