# Azure DataLake Storage

## Steps to setup Azure DataLake Storage

---
Fill the form with the credentials of your data source.

![Screenshot](../assets/datastores/azure-datalake-storage/create-datastore-light.png#only-light){: style="width:450px;"}
![Screenshot](../assets/datastores/azure-datalake-storage/create-datastore-dark.png#only-dark){: style="width:450px;"}

Once the form is completed, it's necessary to test the connection to verify if Qualytics is able to connect to your source of data. A successful message will be shown:

![Screenshot](../assets/datastores/test-connection/test-connection-light.png#only-light){: style="width:450px;"}
![Screenshot](../assets/datastores/test-connection/test-connection-dark.png#only-dark){: style="width:450px;"}

!!! warning 
    By clicking on the `Finish` button, it will create the Datastore and skipping the configuration of an Enrichment Datastore.

    - To configure an Enrichment Datastore in another moment, please refer [to this section](/userguide/enrichment/create-enrichment-datastore/)

!!! note 
    It is important to associate an `Enrichment Datastore` with your new Datastore

    - The `Enrichment Datastore` will allow Qualytics to record `enrichment data`, copies of the source `anomalous data` and additional `metadata` for your `Datastore`

## Configuring an Enrichment Datastore

- If you have an `Enrichment Datastore` already setup, you can link it by enable to use an existing Enrichment Datastore and select from the list

- If you don't have an `Enrichment Datastore`, you can create one at the same page:

    ![Screenshot](../assets/enrichment/azure-datalake-storage/create-enrichment-datastore-light.png#only-light){: style="width:450px"}
    ![Screenshot](../assets/enrichment/azure-datalake-storage/create-enrichment-datastore-dark.png#only-dark){: style="width:450px"}

Once the form is completed, it's necessary to test the connection. A successful message will be shown:

![Screenshot](../assets/enrichment/test-connection-light.png#only-light){: style="width:450px;"}
![Screenshot](../assets/enrichment/test-connection-dark.png#only-dark){: style="width:450px;"}

!!! warning 
    By clicking on the `Finish` button, it will create the Datastore and link or create the Enrichment Datastore

---
## Fields

### `Name` <spam id='required'>`required`</spam>

* The datastore name to be created in Qualytics App.

### `URI` <spam id='required'>`required`</spam>

```text
    abfs[s]://<file_system>@<account_name>.dfs.core.windows.net/<path>
```

* `abfs[s]`: The `abfs[s]` protocol is used as the scheme identifier.

* `<file_system>`: The parent location that holds the files and folders. This is the same as Containers in the Azure Storage Blobs service.

* `<account-name>`: The name given to your storage account during creation.

* `<path>`: A forward slash delimited (/) representation of the directory structure.

* You can find more information [accessing here.](https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction-abfs-uri)

### `Account Name` and `Access Key` <spam id='required'>`required`</spam>

* Account Name and Access Key to access azure datalake storage.

* To get the `account_name` and `access_key` you need to access your local storage in Azure.

* Click on `Access Keys` tab and copy the values.

![Screenshot](../assets/datastores/azure-datalake-storage/where-to-find-keys.png)

## API Payload Examples

### Creating a Datastore

This section provides a sample payload for creating a datastore. Replace the placeholder values with actual data relevant to your setup.

#### Endpoint (Post)

`/api/datastores` _(post)_

=== "Creating a datastore with a new connection"
    ```json
        {
            "name": "your_datastore_name",
            "teams": ["Public"],
            "trigger_catalog": true,
            "root_path": "/azure_root_path",
            "enrich_only": false,
            "connection": {
                "name": "your_connection_name",
                "type": "abfs",
                "uri": "abfs://<container>@<account_name>.dfs.core.windows.net",
                "access_key": "azure_account_nme",
                "secret_key": "azure_access_key"
            }
        }
    ```
=== "Creating a datastore with an existing connection"
    ```json
        {
            "name": "your_datastore_name",
            "teams": ["Public"],
            "trigger_catalog": true,
            "root_path": "/azure_root_path",
            "enrich_only": false,
            "connection_id": connection-id
        }
    ```

### Creating an Enrichment Datastore

#### Endpoint (Post)

`/api/datastores` _(post)_

This section provides a sample payload for creating an enrichment datastore. Replace the placeholder values with actual data relevant to your setup.

=== "Creating an enrichment datastore with a new connection"
    ```json
        {
            "name": "your_datastore_name",
            "teams": ["Public"],
            "trigger_catalog": true,
            "root_path": "/azure_root_path",
            "enrich_only": true,
            "connection": {
                "name": "your_connection_name",
                "type": "abfs",
                "uri": "abfs://<container>@<account_name>.dfs.core.windows.net",
                "access_key": "azure_account_nme",
                "secret_key": "azure_access_key"
            }
        }
    ```
=== "Creating an enrichment datastore with an existing connection"
    ```json
        {
            "name": "your_datastore_name",
            "teams": ["Public"],
            "trigger_catalog": true,
            "root_path": "/azure_root_path",
            "enrich_only": true,
            "connection_id": connection-id
        }
    ``` 

### Linking Datastore to an Enrichment Datastore through API

#### Endpoint (Patch)

`/api/datastores/{datastore-id}/enrichment/{enrichment-id}` _(patch)_