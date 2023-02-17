# MySQL

## Steps to setup MySQL

---
Fill the form with the credentials of your data source.

![Screenshot](../assets/datastores/mysql/create-datastore-light.png#only-light){: style="width:450px;"}
![Screenshot](../assets/datastores/mysql/create-datastore-dark.png#only-dark){: style="width:450px;"}

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

### `Host` <spam id='required'>`required`</spam>

* The MySQL hostname that defines the location of your MySQL server and database
### `Port` <spam id='required'>`required`</spam>

* The port to access MySQL server. The default is `3306`.
### `Database` <spam id='required'>`required`</spam>

* The `database` name to be connected.

### `User` <spam id='required'>`required`</spam>

* The `user` that has access to the MySQL server.
### `Password` <spam id='required'>`required`</spam>

* The `password` that has access to the MySQL server.


## Information on how to connect with MySQL

---
[MySQL connection string](https://www.connectionstrings.com/mysql/)