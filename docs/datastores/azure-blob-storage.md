# Azure Blob Storage

## Steps to setup Azure Blob Storage

---
Fill the form with the credentials of your data source.

![Screenshot](../assets/datastores/azure-blob-storage/create-datastore-light.png#only-light){: style="width:450px;"}
![Screenshot](../assets/datastores/azure-blob-storage/create-datastore-dark.png#only-dark){: style="width:450px;"}

Once the form is completed, it's necessary to test the connection to verify if Qualytics is able to connect to your source of data. A successful message will be shown:

![Screenshot](../assets/datastores/test-connection/test-connection-light.png#only-light){: style="width:450px;"}
![Screenshot](../assets/datastores/test-connection/test-connection-dark.png#only-dark){: style="width:450px;"}

!!! info 
    We strongly recommend you to enforce an `Enrichment Datastore`

    - The `Enrichment Datastore` will allow Qualytics App to record `enrichment data`, `anomalous data` and `metadata` for your `Datastore`

    - To configure an Enrichment Datastore, please see more  [clicking here](/userguide/enrichment/associate-enrichment-datastore/)

---
## Fields

### `Name` <spam id='required'>`required`</spam>

* The datastore name  to be created in Qualytics App

### `URI` <spam id='required'>`required`</spam>

``` text
wasb[s]://<container-name>@<storage-account-name>.blob.core.windows.net/<path>
```

* `<container-name>`: the name of a container in your Azure Blob storage account.
* `<storage-account-name>`: the name of your Azure Blob storage account.
* `<path>`: A forward slash delimited (/) representation of the directory structure.
### `Account Name` and `Access Key` <spam id='required'>`required`</spam>

* Account Name and Access Key to access azure blob storage.

* To get the `account_name` and `access_key` you need to access your local storage in Azure.

* Click in `Access Keys` tab and copy the values.

![Screenshot](../assets/datastores/azure-blob-storage/where-to-find-keys.png)
