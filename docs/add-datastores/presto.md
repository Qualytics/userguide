# Presto

## Steps to setup Presto

---
Fill the form with the credentials of your data source.

![Screenshot](../assets/datastores/presto/create-datastore-light.png#only-light){: style="height:auto;width:450px;"}
![Screenshot](../assets/datastores/presto/create-datastore-dark.png#only-dark){: style="height:auto;width:450px;"}

Once the form is completed, it's necessary to test the connection to verify if Qualytics is able to connect to your source of data. A successful message will be shown:

![Screenshot](../assets/datastores/test-connection/test-connection-light.png#only-light){: style="width:450px;"}
![Screenshot](../assets/datastores/test-connection/test-connection-dark.png#only-dark){: style="width:450px;"}

!!! warning 
    By clicking on the `Finish` button, it will create the Datastore and skipping the configuration of an Enrichment Datastore.

    - To configure an Enrichment Datastore in another moment, please refer [to this section](enrichment/enrichment-datastore-creation/)

!!! note 
    It is important to associate an `Enrichment Datastore` with your new Datastore

    - The `Enrichment Datastore` will allow Qualytics to record `enrichment data`, copies of the source `anomalous data` and additional `metadata` for your `Datastore`

## Configuring an Enrichment Datastore


!!! warning 
    Qualytics does not support `Presto` connector as an enrichment datastore, but you can point to a different connector.

    - To configure an Enrichment Datastore in another moment, please refer [to this section](enrichment/enrichment-datastore-creation/)
- If you have an `Enrichment Datastore` already setup, you can link it by enable to use an existing Enrichment Datastore and select from the list

- If you don't have an `Enrichment Datastore`, you can create one at the same page.

Once the form is completed, it's necessary to test the connection. A successful message will be shown:

![Screenshot](../assets/enrichment/test-connection-light.png#only-light){: style="width:450px;"}
![Screenshot](../assets/enrichment/test-connection-dark.png#only-dark){: style="width:450px;"}

!!! warning 
    By clicking on the `Finish` button, it will create the Datastore and link or create the Enrichment Datastore
    
---
## Fields


### `Host` <spam id='required'>`required`</spam>

* The address of the server to connect to. This address can be a DNS or IP address.

### `Port` <spam id='required'>`required`</spam>

* The port to connect to on serverName. 
* The default is `8080`. 

    `Note: If you're using the default, you don't have to specify the port`


### `Catalog` <spam id='required'>`required`</spam>

* The `catalog` name to be connected.

### `Schema` <spam id='required'>`required`</spam>

* The `schema` name to be connected.
* The default is `default`. 

### `User` <spam id='required'>`required`</spam>

* The `user` to connect in Hive.

### `Password` <spam id='required'>`required`</spam>

* The `password` to connect in Hive.

### `SSL TrustStore` <spam id='required'>`required`</spam>

* A keystore file that contains certificates from other parties that you expect to communicate with or from Certificate Authorities that you trust to identify other parties

### Configuring Presto for Hive Table Access Control:
​
**Locate the Hive Connector Configuration File**:

- The configuration file for the Hive connector in Presto is typically named `hive.properties` and is located in the `etc/catalog` directory of your Presto installation.
​

**Modify the Configuration**:

- Open the `hive.properties` file in a text editor.
- Add or modify the line `hive.allow-drop-table=true` to allow dropping tables. If you set it to `false`, it will disallow dropping tables.
​

**Restart Presto**:
- After making changes to the configuration, you'll need to restart Presto for the changes to take effect.

```bash
sudo systemctl stop presto-server
sudo systemctl start presto-server
```

- Or, you can use the restart command to do it in one step:

```bash
sudo systemctl restart presto-server
```
   
!!! info
    The `hive.allow-drop-table` configuration is just one of the many configurations available. If you want to control more granular permissions, such as read/write access, you might need to look into using a combination of Hive's native permissions and the configurations available in Presto.

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
            "database": "presto_database",
            "schema": "presto_schema",
            "enrich_only": false,
            "trigger_catalog": true,
            "connection": {
                "name": "your_connection_name",
                "type": "presto",
                "host": "presto_host",
                "port": "presto_port",
                "username": "presto_username",
                "password": "presto_password",
                "parameters":{
                    "ssl_truststore":"truststore.jks"
                },
            }
        }
    ```
=== "Creating a datastore with an existing connection"
    ```json
        {
            "name": "your_datastore_name",
            "teams": ["Public"],
            "database": "presto_database",
            "schema": "presto_schema",
            "enrich_only": false,
            "trigger_catalog": true,
            "connection_id": connection-id
        }
    ```

### Linking Datastore to an Enrichment Datastore through API

#### Endpoint (Patch)

`/api/datastores/{datastore-id}/enrichment/{enrichment-id}` _(patch)_