# Google Cloud Storage

## Steps to setup Cloud Storage

---

![Screenshot](../assets/datastores/google-cloud-storage/create-data-store-light.png#only-light){: style="height:auto;width:450px;"}
![Screenshot](../assets/datastores/google-cloud-storage/create-data-store-dark.png#only-dark){: style="height:auto;width:450px;"}

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
