# Google Cloud Storage

## Steps to setup Cloud Storage

---
Fill the form with the credentials of your data source.

![Screenshot](../assets/datastores/google-cloud-storage/create-datastore-light.png#only-light){: style="width:450px;"}
![Screenshot](../assets/datastores/google-cloud-storage/create-datastore-dark.png#only-dark){: style="width:450px;"}

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

* The URI path to access the storage.

* To retrieve the Cloud Storage URI:

    1. Open the Cloud Storage console [here](https://console.cloud.google.com/).

    2. Browse to the location of the object (file) that contains the source data.

    3. At the top of the Cloud Storage console, note the path to the object. To compose the URI, replace gs://bucket/file with the appropriate path. 

```text
     gs://bucket/file.
```
* `bucket` is the Cloud Storage bucket name. 
* `file` is the name of the object (file) containing the data.


### `Access Key` and `Secret Key` <spam id='required'>`required`</spam>

* Account Name and Access Key to access google cloud storage.

## Information on how to retrieve the Access Key and Secret Key
---

1. Log in to your Google Cloud Storage Console or go directly to [Cloud Storage](https://console.cloud.google.com/storage/settings)

2. You will be asked to choose a project, select your project (the storage account we need to create the credentials for).

3. Then click on the Interoperability tab.

4. Click Create a key at the bottom of the screen under "Access keys for your user account".

5. A new Access Key and Secret key will be generated. Use these two values when adding your Google Cloud Storage account to SimpleBackups.
​
