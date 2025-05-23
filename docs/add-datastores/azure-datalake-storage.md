# Azure Datalake Storage

Adding and configuring an Azure Datalake Storage connection within Qualytics empowers the platform to build a symbolic link with your file system to perform operations like data discovery, visualization, reporting, cataloging, profiling, scanning, anomaly surveillance, and more.

This documentation provides a step-by-step guide on how to add Azure Datalake Storage as both a source and enrichment datastore in Qualytics. It covers the entire process, from initial connection setup to testing and finalizing the configuration.

By following these instructions, enterprises can ensure their Azure Datalake Storage environment is properly connected with Qualytics, unlocking the platform's potential to help you proactively manage your full data quality lifecycle

Let’s get started 🚀

## Azure Datalake Storage Setup Guide

This setup guide details the process for retrieving the Account Name and Access Key of your Azure Datalake Storage account, essential for seamless configuration in Qualytics.

### Azure Datalake Storage URI

The Uniform Resource Identifier (URI) for Azure Datalake Storage is structured to uniquely identify resources within your storage account. The format of the URI is as follows:

```
abfs[s]://<file_system>@<account_name>.dfs.core.windows.net/<path>
```

 - `abfs[s]`: The `abfs` or `abfss` protocol is used as the scheme identifier.
 - `\<file_system>`: The parent location that holds the files and folders. This is similar to containers in the Azure Storage Blobs service.
 - `<account-name>`: The name assigned to your storage account during creation.
 - `<path>`: A forward slash delimited (/) representation of the directory structure.

## Retrieve the Account Name and Access Key

To configure Azure Datalake Storage Datastore in Qualytics, you need the account name and access key. Follow these steps to retrieve them:

1. To get the `account_name` and `access_key` you need to access your local storage in Azure.

2. Click on **Access Keys** tab and copy the values.

![get-azure-datalake-account-credentials](../assets/datastores/azure-datalake-storage/get-azure-datalake-account-credentials.png)

!!! tip
    Refer to the [**Azure Datalake Storage documentation**](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-keys-manage?tabs=azure-portal){:target="_blank"} for more information on how to retrieve the account name and access key of your storage account.

## Add a Source Datastore

A source datastore is a storage location used to connect and access data from external sources. Azure Datalake Storage is an example of a source datastore, specifically a type of Distributed File System (DFS) datastore that is designed to handle data stored in distributed file systems. Configuring a DFS datastore enables the Qualytics platform to access and perform operations on the data, thereby generating valuable insights.

**Step 1**: Log in to your Qualytics account and click on the **Add Source Datastore** button located at the top-right corner of the interface.

![add-datastore](../assets/datastores/azure-datalake-storage/add-datastore-light.png#only-light)
![add-datastore](../assets/datastores/azure-datalake-storage/add-datastore-dark.png#only-dark)

**Step 2**: A modal window- **Add Datastore** will appear, providing you with the options to connect a datastore.

![select-a-connector](../assets/datastores/azure-datalake-storage/select-a-connector-light.png#only-light)
![select-a-connector](../assets/datastores/azure-datalake-storage/select-a-connector-dark.png#only-dark)

| REF     | FIELDS    | ACTIONS          |
|---------|-----------|------------------|
| 1.      | Name (Required) | Specify the name of the datastore.(e.g., The specified name will appear on the datastore cards.) |
| 2.      | Toggle Button | Toggle **ON** to create a new source datastore from scratch, or toggle **OFF** to reuse credentials from an existing connection. |
| 3.      | Connector (Required)| Select **Azure Datalake Storage** from the dropdown list.|

### Option I: Create a Source Datastore with a new Connection

If the toggle for **Add New connection** is turned on, then this will prompt you to add and configure the source datastore from scratch without using existing connection details.

**Step 1**: Select the **Azure Datalake Storage** connector from the dropdown list and add connection details such as Secrets Management, URI, account name, access key, root path, and teams.

![add-datastore-credentials](../assets/datastores/azure-datalake-storage/add-datastore-credentials-light.png#only-light)
![add-datastore-credentials](../assets/datastores/azure-datalake-storage/add-datastore-credentials-dark.png#only-dark)

**Secrets Management**: This is an optional connection property that allows you to securely store and manage credentials by integrating with HashCorp Vault and other secret management systems. Toggle it **ON** to enable Vault integration for managing secrets.

!!! note 
    After configuring **HashCorp Vault** integration, you can use ${key} in any Connection property to reference a key from the configured Vault secret. Each time the Connection is initiated, the corresponding secret value will be retrieved dynamically.

| REF | FIELDS               | ACTIONS                                                                 |
|-----|----------------------|-------------------------------------------------------------------------|
| 1.  | Login URL            | Enter the URL used to authenticate with HashCorp Vault.                |
| 2.  | Credentials Payload  | Input a valid JSON containing credentials for Vault authentication.     |
| 3.  | Token JSONPath       | Specify the JSONPath to retrieve the client authentication token from the response (e.g., $.auth.client_token). |
| 4.  | Secret URL           | Enter the URL where the secret is stored in Vault.                      |
| 5.  | Token Header Name    | Set the header name used for the authentication token (e.g., X-Vault-Token). |
| 6.  | Data JSONPath        | Specify the JSONPath to retrieve the secret data (e.g., $.data).        |

![secret-management](../assets/datastores/azure-datalake-storage/secret-management-light-04.png#only-light)
![secret-management](../assets/datastores/azure-datalake-storage/secret-management-dark-04.png#only-dark)

**Step 2**: The configuration form will expand, requesting credential details before establishing the connection.

![add-datastore-credentials-explain](../assets/datastores/azure-datalake-storage/add-datastore-credentials-explain-light.png#only-light)
![add-datastore-credentials-explain](../assets/datastores/azure-datalake-storage/add-datastore-credentials-explain-dark.png#only-dark)

| REF | FIELDS | ACTIONS |
|-----|--------|---------|
| 1.  | URI (Required) | Enter the Uniform Resource Identifier (URI) of the Azure Datalake Storage. |
| 2.  | Account Name (Required) | Input the account name to access the Azure Datalake Storage. |
| 3.  | Access Key (Required) | Input the access key provided for secure access. |
| 4.  | Root Path (Required) | Specify the root path where the data is stored. |
| 5.  | Teams (Required) | Select one or more teams from the dropdown to associate with this source datastore. |
| 6.  | Initiate Cataloging (Optional) | Tick the checkbox to automatically perform catalog operation on the configured source datastore to gather data structures and corresponding metadata. |

**Step 3**: After adding the source datastore details, click on the **Test Connection** button to check and verify its connection.

![test-datastore-connection](../assets/datastores/azure-datalake-storage/test-datastore-connection-light.png#only-light)
![test-datastore-connection](../assets/datastores/azure-datalake-storage/test-datastore-connection-dark.png#only-dark)

If the credentials and provided details are verified, a success message will be displayed indicating that the connection has been verified.

### Option II: Use an Existing Connection

If the toggle for **Add New connection** is turned off, then this will prompt you to configure the source datastore using the existing connection details.

**Step 1**: Select a **connection** to reuse existing credentials.

![use-existing-datastore](../assets/datastores/azure-datalake-storage/use-existing-datastore-light.png#only-light)
![use-existing-datastore](../assets/datastores/azure-datalake-storage/use-existing-datastore-dark.png#only-dark)

!!! note
     If you are using existing credentials, you can only edit the details such as Root Path, Teams, and Initiate Cataloging.

**Step 2**: Click on the **Test Connection** button to verify the existing connection details. If connection details are verified, a success message will be displayed.

![test-connection-for-existing-datastore](../assets/datastores/azure-datalake-storage/test-datastore-connection-light.png#only-light)
![test-connection-for-existing-datastore](../assets/datastores/azure-datalake-storage/test-datastore-connection-dark.png#only-dark)

!!!note
    Clicking on the **Finish** button will create the source datastore and bypass the **enrichment datastore** configuration step.

!!!tip
    It is recommended to click on the **Next** button, which will take you to the **enrichment datastore** configuration page.

## Add Enrichment Datastore

Once you have successfully tested and verified your source datastore connection, you have the option to add the enrichment datastore (recommended). This datastore is used to store the analyzed results, including any anomalies and additional metadata in files. This setup provides full visibility into your data quality, helping you manage and improve it effectively. 

**Step 1**: Whether you have added a source datastore by creating a new datastore connection or using an existing connection, click on the **Next** button to start adding the **Enrichment Datastore**.

![next-button-for-enrichment](../assets/datastores/azure-datalake-storage/next-button-for-enrichment-light.png#only-light)
![next-button-for-enrichment](../assets/datastores/azure-datalake-storage/next-button-for-enrichment-dark.png#only-dark)

**Step 2**:  A modal window- **Link Enrichment Datastore** will appear, providing you with the options to configure an **enrichment datastore**.

![select-enrichment-connector](../assets/datastores/azure-datalake-storage/select-enrichment-connector-light.png#only-light)
![select-enrichment-connector](../assets/datastores/azure-datalake-storage/select-enrichment-connector-dark.png#only-dark)

| REF.              | FIELDS       | ACTIONS                                    |
|-------------------|--------------|--------------------------------------------|
| 1.                | Prefix       | Add a prefix name to uniquely identify tables/files when Qualytics writes metadata from the source datastore to your enrichment datastore. |
| 2.                | Caret Down Button   | Click the caret down to select either **Use Enrichment Datastore** or **Add Enrichment Datastore**.|
| 3.                | Enrichment Datastore         | Select an enrichment datastore from the dropdown list. |

### Option I: Create an Enrichment Datastore with a new Connection

If the toggles for **Add New connection is turned on**, then this will prompt you to add and configure the enrichment datastore from scratch without using an existing enrichment datastore and its connection details.

**Step 1**: Click on the caret button and select Add Enrichment Datastore.

![select-enrichment](../assets/datastores/azure-datalake-storage/select-enrichment-light-10.png#only-light)
![select-enrichment](../assets/datastores/azure-datalake-storage/select-enrichment-dark-10.png#only-dark)

A modal window **Link Enrichment Datastore** will appear. Enter the following details to create an enrichment datastore with a new connection

![enrichment-detail](../assets/datastores/azure-datalake-storage/enrichment-details-light-11.png#only-light)
![enrichment-detail](../assets/datastores/azure-datalake-storage/enrichment-details-dark-11.png#only-dark)

| REF.              | FIELDS       | ACTIONS                                    |
|-------------------|--------------|--------------------------------------------|
| 1.                | Prefix       | Add a prefix name to uniquely identify tables/files when Qualytics writes metadata from the source datastore to your enrichment datastore. |
| 2.                | Name   | Give a name for the enrichment datastore.|
| 3.                |Toggle Button for add new connection | Toggle ON to create a new enrichment from scratch or toggle OFF to reuse credentials from an existing connection. |
| 4.                |Connector | Select a datastore connector from the dropdown list.|

**Step 2**: Add connection details for your selected **enrichment datastore** connector.

![enrichment-datastore-explain](../assets/datastores/azure-datalake-storage/enrichment-datastore-explain-light.png#only-light)
![enrichment-datastore-explain](../assets/datastores/azure-datalake-storage/enrichment-datastore-explain-dark.png#only-dark)

| REF | FIELDS | ACTIONS |
|------|-------|---------|
| 1.   | URI (Required)        | Enter the Uniform Resource Identifier (URI) of the Azure Datalake Storage. |
| 2.   | Account Name (Required) | Input the account name to access the Azure Datalake Storage. |
| 3.   | Access Key (Required)  | Input the access key provided for secure access.         |
| 4.   | Root Path (Required)   | Specify the root path where the data is stored.          |
| 5.   | Teams (Required)       | Select one or more teams from the dropdown to associate with this source datastore. |

**Step 3**: Click on the **Test Connection** button to verify the selected enrichment datastore connection. If the connection is verified, a flash message will indicate that the connection with the datastore has been successfully verified.

![test-connection-for-enrichment-datastore](../assets/datastores/azure-datalake-storage/test-connection-for-enrichment-datastore-light.png#only-light)
![test-connection-for-enrichment-datastore](../assets/datastores/azure-datalake-storage/test-connection-for-enrichment-datastore-dark.png#only-dark)

**Step 4**: Click on the **Finish** button to complete the configuration process.

![finish-configuration](../assets/datastores/azure-datalake-storage/finish-configuration-light.png#only-light)
![finish-configuration](../assets/datastores/azure-datalake-storage/finish-configuration-dark.png#only-dark)

When the configuration process is finished, a modal will display a **success message** indicating that **your datastore has been successfully added**.

![success-message](../assets/datastores/azure-datalake-storage/success-message-light.png#only-light)
![success-message](../assets/datastores/azure-datalake-storage/success-message-dark.png#only-dark)

**Step 5**: Close the Success dialog and the page will automatically redirect you to the **Source Datastore Details** page where you can perform data operations on your configured **source datastore**.

![data-operation-page](../assets/datastores/azure-datalake-storage/data-operation-page-light.png#only-light)
![data-operation-page](../assets/datastores/azure-datalake-storage/data-operation-page-dark.png#only-dark)

### Option II: Use an Existing Connection

If the toggle for **Use an existing enrichment datastore** is turned on, you will be prompted to configure the enrichment datastore using existing connection details.

**Step 1**: Click on the caret button and select **Use Enrichment Datastore**.

![select-enrichment-details](../assets/datastores/azure-datalake-storage/select-enrichment-light-17.png#only-light)
![select-enrichment-details](../assets/datastores/azure-datalake-storage/select-enrichment-dark-17.png#only-dark)

**Step 2**: A modal window **Link Enrichment Datastore** will appear. Add a prefix name and select an existing enrichment datastore from the dropdown list.

![add-enrichment-details](../assets/datastores/azure-datalake-storage/add-enrichment-details-light-18.png#only-light)
![add-enrichment-details](../assets/datastores/azure-datalake-storage/add-enrichment-details-dark-18.png#only-dark)

| REF.              | FIELDS       | ACTIONS                                    |
|-------------------|--------------|--------------------------------------------|
| 1.                | Prefix       | Add a prefix name to uniquely identify tables/files when Qualytics writes metadata from the source datastore to your enrichment datastore. |
| 2.                | Enrichment Datastore  | Select an enrichment datastore from the dropdown list. |

**Step 3**: After selecting an existing **enrichment datastore** connection, you will view the following details related to the selected enrichment:

-   **Teams:** The team associated with managing the enrichment datastore is based on the role of public or private. Example- Marked as **Public** means that this datastore is accessible to all the users.

-   **URI:** Uniform Resource Identifier (URI) points to the specific location of the source data and should be formatted accordingly (e.g., ```abfss://storage-url``` for Azure Datalake Storage).

-   **Root Path:** Specify the root path where the data is stored. This path defines the base directory or folder from which all data operations will be performed.

![use-existing-enrichment-datastore](../assets/datastores/azure-datalake-storage/use-existing-enrichment-datastore-light.png#only-light)
![use-existing-enrichment-datastore](../assets/datastores/azure-datalake-storage/use-existing-enrichment-datastore-dark.png#only-dark)

**Step 4**: Click on the **Finish** button to complete the configuration process for the existing **enrichment datastore**.

![finish-configuration-for-existing-enrichment-datastore](../assets/datastores/azure-datalake-storage/finish-configuration-for-existing-enrichment-datastore-light.png#only-light)
![finish-configuration-for-existing-enrichment-datastore](../assets/datastores/azure-datalake-storage/finish-configuration-for-existing-enrichment-datastore-dark.png#only-dark)

When the configuration process is finished, a modal will display a **success message** indicating that **your data has been successfully added**.

![success-message](../assets/datastores/azure-datalake-storage/success-message-light.png#only-light)
![success-message](../assets/datastores/azure-datalake-storage/success-message-dark.png#only-dark)

Close the success message and you will be automatically redirected to the **Source Datastore Details** page where you can perform data operations on your configured **source datastore**.

![data-operation-page](../assets/datastores/azure-datalake-storage/data-operation-page-light.png#only-light)
![data-operation-page](../assets/datastores/azure-datalake-storage/data-operation-page-dark.png#only-dark)

## API Payload Examples

This section provides detailed examples of API payloads to guide you through the process of creating and managing datastores using Qualytics API. Each example includes endpoint details, sample payloads, and instructions on how to replace placeholder values with actual data relevant to your setup.

### Creating a Source Datastore

This section provides sample payloads for creating the Azure Datalake Storage datastore. Replace the placeholder values with actual data relevant to your setup.

**Endpoint:** ```/api/datastores (post)```

=== "Create a Source Datastore with a new Connection"
    ``` json
    {  
        "name": "your\_datastore\_name",  
        "teams": \["Public"\],  
        "trigger_catalog": true,  
        "root_path": "/azure\_root\_path",  
        "enrich_only": false,  
        "connection": {  
            "name": "your\_connection\_name",  
            "type": "abfs",  
            "uri": "abfs://<container>@<account_name>.dfs.core.windows.net",  
            "access_key": "azure\_account\_nme",  
            "secret_key": "azure\_access\_key" 
        }  
    }
    ```
=== "Create a Source Datastore with an existing Connection"
    ``` json 
    {  
        "name": "your\_datastore\_name",  
        "teams": \["Public"\],  
        "trigger_catalog": true,  
        "root_path": "/azure\_root\_path",  
        "enrich_only": false,  
        "connection_id": connection-id  
    }
    ```

### Creating an Enrichment Datastore

This section provides sample payloads for creating an enrichment datastore. Replace the placeholder values with actual data relevant to your setup.

**Endpoint:**  ```/api/datastores (post)```

=== "Create an Enrichment Datastore with a new Connection"
    ``` json
    {
        "name": "your\_datastore\_name",  
        "teams": \["Public"\],  
        "trigger_catalog": true,  
        "root_path": "/azure\_root\_path",  
        "enrich_only": true,  
        "connection": {  
            "name": "your\_connection\_name",  
            "type": "abfs",  
            "uri": "abfs://<container>@<account_name>.dfs.core.windows.net",  
            "access_key": "azure\_account\_nme",  
            "secret_key": "azure\_access\_key"  
        }  
    }
    ```
=== "Create an Enrichment Datastore with an Existing Connection"
    ```json
    {
        "name": "your\_datastore\_name",  
        "teams": \["Public"\],  
        "trigger_catalog": true,  
        "root_path": "/azure\_root\_path",  
        "enrich_only": true,  
        "connection_id": connection-id  
    }
    ```

### Link an Enrichment Datastore to a Source Datastore

Use the provided endpoint to link an enrichment datastore to a source datastore:

**Endpoint Details:** ```/api/datastores/{datastore-id}/enrichment/{enrichment-id} (patch)```
