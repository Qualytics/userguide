# Synapse

## Steps to setup Synapse

---
Fill the form with the credentials of your data source.

![Screenshot](../assets/datastores/synapse/create-datastore-light.png#only-light){: style="height:auto;width:450px;"}
![Screenshot](../assets/datastores/synapse/create-datastore-dark.png#only-dark){: style="height:auto;width:450px;"}

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

    ![Screenshot](../assets/enrichment/synapse/create-enrichment-datastore-light.png#only-light){: style="width:450px"}
    ![Screenshot](../assets/enrichment/synapse/create-enrichment-datastore-dark.png#only-dark){: style="width:450px"}

Once the form is completed, it's necessary to test the connection. A successful message will be shown:

![Screenshot](../assets/enrichment/test-connection-light.png#only-light){: style="width:450px;"}
![Screenshot](../assets/enrichment/test-connection-dark.png#only-dark){: style="width:450px;"}

!!! warning 
    By clicking on the `Finish` button, it will create the Datastore and link or create the Enrichment Datastore

---
## Fields
### `Name` <spam id='required'>`required`</spam>

* The datastore name  to be created in Qualytics App

### `Host` <spam id='required'>`required`</spam>

* Host url to be connected.
* Hostname in the form 
```text
    https://yourserver.sql.azuresynapse.net
```

### `Port` <spam id='required'>`required`</spam>

* Port number to access the `Synapse` database.
* The default port is `1433`

### `Database` <spam id='required'>`required`</spam>

* The `database` name to be connected or which the account user has access to.

### `Schema` <spam id='required'>`required`</spam>

* The `schema` name to be connected or which the account user has access to.

### `User` <spam id='required'>`required`</spam>

* The `user` that has access to the `Synapse` application.

### `Password` <spam id='required'>`required`</spam>

* The `password` that has access to the `Synapse` application.

## Information on how to connect with Synapse

---

* [Synapse Connect Overview](https://learn.microsoft.com/en-us/azure/synapse-analytics/sql/connect-overview)

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
            "database": "synapse_database",
            "schema": "synapse_schema",
            "enrich_only": false,
            "trigger_catalog": true,
            "connection": {
                "name": "your_connection_name",
                "type": "synapse",
                "host": "synapse_host",
                "port": "synapse_port",
                "username": "synapse_username",
                "password": "synapse_password"
            }
        }
    ```
=== "Creating a datastore with an existing connection"
    ```json
        {
            "name": "your_datastore_name",
            "teams": ["Public"],
            "database": "synapse_database",
            "schema": "synapse_schema",
            "enrich_only": false,
            "trigger_catalog": true,
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
            "database": "synapse_database",
            "schema": "synapse_schema",
            "enrich_only": true,
            "connection": {
                "name": "your_connection_name",
                "type": "synapse",
                "host": "synapse_host",
                "port": "synapse_port",
                "username": "synapse_username",
                "password": "synapse_password"
            }
        }
    ```
=== "Creating an enrichment datastore with an existing connection"
    ```json
        {
            "name": "your_datastore_name",
            "teams": ["Public"],
            "database": "synapse_database",
            "schema": "synapse_schema",
            "enrich_only": true,
            "connection_id": connection-id
        }
    ``` 

### Linking Datastore to an Enrichment Datastore through API

#### Endpoint (Patch)

`/api/datastores/{datastore-id}/enrichment/{enrichment-id}` _(patch)_