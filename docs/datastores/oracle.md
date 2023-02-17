# Oracle

## Steps to setup Oracle

---
Fill the form with the credentials of your data source.

![Screenshot](../assets/datastores/oracle/create-datastore-light.png#only-light){: style="width:450px;"}
![Screenshot](../assets/datastores/oracle/create-datastore-dark.png#only-dark){: style="width:450px;"}

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

* The datastore name  to be created in Qualytics App.

### `Host` <spam id='required'>`required`</spam>

* The Oracle hostname that defines the location of your Oracle server and database.
### `Port` <spam id='required'>`required`</spam>

* The Oracle server `port` that connects to the server.
* The default `port` is `1521`.
### `SID` <spam id='required'>`required`</spam>

* Oracle SID is the unique name that uniquely identifies your instance/database.

### `Schema` <spam id='required'>`required`</spam>

* The `schema` name to be connected.

### `User` <spam id='required'>`required`</spam>

* The `user` name to be connected.
### `Password` <spam id='required'>`required`</spam>

* The `password` to be connected.

​
## Information on how to connect with Oracle

---

* [How to find Oracle SID](http://www.rebellionrider.com/how-to-find-out-the-sid-and-db-home-in-oracle-database/)

* [Oracle Connection](https://www.connectionstrings.com/oracle/)