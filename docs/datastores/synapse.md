# Synapse

## Steps to setup Synapse

---

![Screenshot](../assets/datastores/synapse/create-datastore-light.png#only-light){: style="height:auto;width:450px;"}
![Screenshot](../assets/datastores/synapse/create-datastore-dark.png#only-dark){: style="height:auto;width:450px;"}

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