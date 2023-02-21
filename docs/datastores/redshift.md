# Amazon RedShift

## Steps to setup Amazon RedShift

---
Fill the form with the credentials of your data source.

![Screenshot](../assets/datastores/redshift/create-datastore-light.png#only-light){: style="height:auto;width:450px;"}
![Screenshot](../assets/datastores/redshift/create-datastore-dark.png#only-dark){: style="height:auto;width:450px;"}

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

* Host url to be connected.
* Hostname in the form 
```text
[name].[id].[region].redshift.amazonaws.com
```
### `Port` <spam id='required'>`required`</spam>

* Port to connect to the server .
* The default port is `5439`

### `Database` <spam id='required'>`required`</spam>

* The `database` name to be connected.
### `Schema` <spam id='required'>`required`</spam>

* The `schema` name to be connected.

### `User` <spam id='required'>`required`</spam>

* The `user` that has access to the redshift server.
### `Password` <spam id='required'>`required`</spam>

* The `password` that has access to the redshift server.
## Information on how to connect with Amazon RedShift

---

* [Amazon Redshift documentation](https://docs.dataform.co/warehouses/redshift)