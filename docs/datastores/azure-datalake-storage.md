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

- If you have an `Enrichment Datastore` already setup, you can link it by enable to use an existing Enrichment Datastore:

    ![Screenshot](../assets/enrichment/amazon-s3/associate-enrichment-datastore-light.png#only-light){: style="width:450px"}
    ![Screenshot](../assets/enrichment/amazon-s3/associate-enrichment-datastore-dark.png#only-dark){: style="width:450px"}

- If you don't have an `Enrichment Datastore`, you can create one at the same page:

    ![Screenshot](../assets/enrichment/amazon-s3/create-enrichment-datastore-light.png#only-light){: style="width:450px"}
    ![Screenshot](../assets/enrichment/amazon-s3/create-enrichment-datastore-dark.png#only-dark){: style="width:450px"}

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

* Click in `Access Keys` tab and copy the values.

![Screenshot](../assets/datastores/azure-datalake-storage/where-to-find-keys.png)