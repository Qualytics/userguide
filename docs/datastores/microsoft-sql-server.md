# Microsoft SQL Server

## Steps to setup Microsoft SQL Server 

---
Fill the form with the credentials of your data source.

![Screenshot](../assets/datastores/microsoft-sql-server/create-datastore-light.png#only-light){: style="width:450px;"}
![Screenshot](../assets/datastores/microsoft-sql-server/create-datastore-dark.png#only-dark){: style="width:450px;"}

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

* The datastore name  to be created in Qualytics App

### `Host` <spam id='required'>`required`</spam>

* The address of the server to connect to. This address can be a DNS or IP address.
### `Port` <spam id='required'>`required`</spam>

* The port to connect to on serverName. 
* The default is 1433. 

    `Note: If you're using the default, you don't have to specify the port`

### `Database` <spam id='required'>`required`</spam>

* The `database` instance name to be connected.

### `Schema` <spam id='required'>`required`</spam>

* The `schema` name to be connected.

### `User` <spam id='required'>`required`</spam>

* The `user` to connect in Microsoft SQL Server
### `Password` <spam id='required'>`required`</spam>


* The `password` to connect in Microsoft SQL Server.

## More information on how to connect with Microsoft SQL Server

---

* [Building the connection URL](https://learn.microsoft.com/en-us/sql/connect/jdbc/building-the-connection-url?view=sql-server-ver16)

* [Setting the connection properties](https://learn.microsoft.com/en-us/sql/connect/jdbc/setting-the-connection-properties?view=sql-server-ver16)