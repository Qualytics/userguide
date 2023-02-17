# PostgreSQL

## Steps to setup PostgreSQL

---
Fill the form with the credentials of your data source.

![Screenshot](../assets/datastores/postgresql/create-datastore-light.png#only-light){: style="width:450px;"}
![Screenshot](../assets/datastores/postgresql/create-datastore-dark.png#only-dark){: style="width:450px;"}

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

* The PostgreSQL hostname that defines the location of your PostgreSQL server and database.
### `Port` <spam id='required'>`required`</spam>

* The PostgreSQL server `port` that connects to the server.
* The default `port` is `5432​`.

### `Database` <spam id='required'>`required`</spam>

* The `database` name to be connected.

### `Schema` <spam id='required'>`required`</spam>

* The `schema` name to be connected.

### `User` <spam id='required'>`required`</spam>

* The PostgreSQL user name to use when connecting to the server.
### `Password` <spam id='required'>`required`</spam>

* The password of the PostgreSQL server.


## More information on how to connect with PostgreSQL

---


[PostgreSQL configuration](https://jdbc.postgresql.org/documentation/use/)
[PostgreSQL Connection String](https://www.connectionstrings.com/postgresql/)