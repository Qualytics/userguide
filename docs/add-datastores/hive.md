# Hive

## Steps to setup Hive

---
Fill the form with the credentials of your data source.

![Screenshot](../assets/datastores/hive/create-datastore-light.png#only-light){: style="width:450px;"}
![Screenshot](../assets/datastores/hive/create-datastore-dark.png#only-dark){: style="width:450px;"}

Once the form is completed, it's necessary to test the connection to verify if Qualytics is able to connect to your source of data. A successful message will be shown:

![Screenshot](../assets/datastores/test-connection/test-connection-light.png#only-light){: style="width:450px;"}
![Screenshot](../assets/datastores/test-connection/test-connection-dark.png#only-dark){: style="width:450px;"}

!!! warning 
    By clicking on the `Finish` button, it will create the Datastore and skipping the configuration of an Enrichment Datastore.

    - To configure an Enrichment Datastore in another moment, please refer [to this section](/enrichment/enrichment-datastore-creation/)

!!! note 
    It is important to associate an `Enrichment Datastore` with your new Datastore

    - The `Enrichment Datastore` will allow Qualytics to record `enrichment data`, copies of the source `anomalous data` and additional `metadata` for your `Datastore`

## Configuring an Enrichment Datastore


!!! warning 
    Qualytics does not support `Hive` connector as an enrichment datastore, but you can point to a different connector.

    - To configure an Enrichment Datastore in another moment, please refer [to this section](/enrichment/enrichment-datastore-creation/)
- If you have an `Enrichment Datastore` already setup, you can link it by enable to use an existing Enrichment Datastore and select from the list

- If you don't have an `Enrichment Datastore`, you can create one at the same page.

Once the form is completed, it's necessary to test the connection. A successful message will be shown:

![Screenshot](../assets/enrichment/test-connection-light.png#only-light){: style="width:450px;"}
![Screenshot](../assets/enrichment/test-connection-dark.png#only-dark){: style="width:450px;"}

!!! warning 
    By clicking on the `Finish` button, it will create the Datastore and link or create the Enrichment Datastore
    
---
## Fields
### `Name` <spam id='required'>`required`</spam>

* The datastore name  to be created in Qualytics App

### `Hostname` <spam id='required'>`required`</spam>

* The address of the server to connect to. This address can be a DNS or IP address.

### `Port` <spam id='required'>`required`</spam>

* The port to connect to on serverName. 
* The default is `10000`. 

    `Note: If you're using the default, you don't have to specify the port`

### `Schema` <spam id='required'>`required`</spam>

* The `schema` name to be connected.

### `User` <spam id='required'>`required`</spam>

* The `user` to connect in Hive.

### `Password` <spam id='required'>`required`</spam>

* The `password` to connect in Hive.



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
            "database": "hive_database",
            "schema": "hive_schema",
            "enrich_only": false,
            "trigger_catalog": true,
            "connection": {
                "name": "your_connection_name",
                "type": "hive",
                "host": "hive_host",
                "port": "hive_port",
                "username": "hive_username",
                "password": "hive_password",
                "parameters": {
                    "zookeeper": false
                }
            }
        }
    ```
=== "Creating a datastore with an existing connection"
    ```json
        {
            "name": "your_datastore_name",
            "teams": ["Public"],
            "database": "hive_database",
            "schema": "hive_schema",
            "enrich_only": false,
            "trigger_catalog": true,
            "connection_id": connection-id
        }
    ```

### Linking Datastore to an Enrichment Datastore through API

#### Endpoint (Patch)

`/api/datastores/{datastore-id}/enrichment/{enrichment-id}` _(patch)_