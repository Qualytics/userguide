# Azure DataLake Storage

## Steps to setup Azure DataLake Storage

---
Fill the form with the credentials of your data source.

![Screenshot](../assets/datastores/azure-datalake-storage/create-datastore-light.png#only-light){: style="width:450px;"}
![Screenshot](../assets/datastores/azure-datalake-storage/create-datastore-dark.png#only-dark){: style="width:450px;"}

Once the form is completed, it's necessary to test the connection to verify if Qualytics is able to connect to your source of data. A successful message will be shown:

![Screenshot](../assets/datastores/test-connection/test-connection-light.png#only-light){: style="width:450px;"}
![Screenshot](../assets/datastores/test-connection/test-connection-dark.png#only-dark){: style="width:450px;"}

!!! info 
    It is important to associate an `Enrichment Datastore` with your new Datastore

    - The `Enrichment Datastore` will allow Qualytics to record `enrichment data`, copies of the source `anomalous data` and additional `metadata` for your `Datastore`

    - To configure an Enrichment Datastore, please refer [to this section](/userguide/enrichment/associate-enrichment-datastore/)

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