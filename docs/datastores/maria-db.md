# MariaDB

## Steps to setup MariaDB

---
Fill the form with the credentials of your data source.

![Screenshot](../assets/datastores/maria-db/create-datastore-light.png#only-light){: style="width:450px;"}
![Screenshot](../assets/datastores/maria-db/create-datastore-dark.png#only-dark){: style="width:450px;"}

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

