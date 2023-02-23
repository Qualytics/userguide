# MariaDB

## Steps to setup MariaDB

---
Fill the form with the credentials of your data source.

![Screenshot](../assets/datastores/maria-db/create-datastore-light.png#only-light){: style="width:450px;"}
![Screenshot](../assets/datastores/maria-db/create-datastore-dark.png#only-dark){: style="width:450px;"}

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

    ![Screenshot](../assets/enrichment/maria-db/create-enrichment-datastore-light.png#only-light){: style="width:450px"}
    ![Screenshot](../assets/enrichment/maria-db/create-enrichment-datastore-dark.png#only-dark){: style="width:450px"}

Once the form is completed, it's necessary to test the connection. A successful message will be shown:

![Screenshot](../assets/enrichment/test-connection-light.png#only-light){: style="width:450px;"}
![Screenshot](../assets/enrichment/test-connection-dark.png#only-dark){: style="width:450px;"}

!!! warning 
    By clicking on the `Finish` button, it will create the Datastore and link or create the Enrichment Datastore

---
## Fields
### `Name` <spam id='required'>`required`</spam>

* The datastore name  to be created in Qualytics App.

### `Host` <spam id='required'>`required`</spam>

* The `host` to Connect to the MariaDB.

### `Port` <spam id='required'>`required`</spam>
* The TCP/IP port number to use for the connection. The default is `3306`.
### `Database` <spam id='required'>`required`</spam>

* The `database` name of the MariaDB you want to connect.
### `User` <spam id='required'>`required`</spam>

* The MariaDB user name to use when connecting to the server.
### `Password` <spam id='required'>`required`</spam>

* The password of the MariaDB account.


## Information on how to connect with MariaDB

---

* [Connecting to MariaDB](https://mariadb.com/kb/en/connecting-to-mariadb/)

