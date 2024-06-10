# Google Cloud Storage

## Steps to setup Cloud Storage

---
Fill the form with the credentials of your data source.

![Screenshot](../assets/datastores/google-cloud-storage/create-datastore-light.png#only-light){: style="width:450px;"}
![Screenshot](../assets/datastores/google-cloud-storage/create-datastore-dark.png#only-dark){: style="width:450px;"}

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

    ![Screenshot](../assets/enrichment/google-cloud-storage/create-enrichment-datastore-light.png#only-light){: style="width:450px"}
    ![Screenshot](../assets/enrichment/google-cloud-storage/create-enrichment-datastore-dark.png#only-dark){: style="width:450px"}

Once the form is completed, it's necessary to test the connection. A successful message will be shown:

![Screenshot](../assets/enrichment/test-connection-light.png#only-light){: style="width:450px;"}
![Screenshot](../assets/enrichment/test-connection-dark.png#only-dark){: style="width:450px;"}

!!! warning 
    By clicking on the `Finish` button, it will create the Datastore and link or create the Enrichment Datastore

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
            "root_path": "/gcs_root_path",
            "enrich_only": false,
            "connection": {
                "name": "your_connection_name",
                "type": "gcs",
                "uri": "gs://<bucket_name>",
                "secret_key": "gcs_service_account_key"
            }
        }
    ```
=== "Creating a datastore with an existing connection"
    ```json
        {
            "name": "your_datastore_name",
            "teams": ["Public"],
            "trigger_catalog": true,
            "root_path": "/gcs_root_path",
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
            "root_path": "/gcs_root_path",
            "enrich_only": true,
            "connection": {
                "name": "your_connection_name",
                "type": "gcs",
                "uri": "gs://<bucket_name>",
                "secret_key": "gcs_service_account_key"
            }
        }
    ```
=== "Creating an enrichment datastore with an existing connection"
    ```json
        {
            "name": "your_datastore_name",
            "teams": ["Public"],
            "trigger_catalog": true,
            "root_path": "/gcs_root_path",
            "enrich_only": true,
            "connection_id": connection-id
        }
    ``` 

### Linking Datastore to an Enrichment Datastore through API

#### Endpoint (Patch)

`/api/datastores/{datastore-id}/enrichment/{enrichment-id}` _(patch)_