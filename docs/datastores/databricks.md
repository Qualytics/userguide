# Databricks



## Steps to setup Databricks
---

![Screenshot](../assets/datastores/databricks/create-data-store-light.png#only-light){: style="height:auto;width:450px;"}
![Screenshot](../assets/datastores/databricks/create-data-store-dark.png#only-dark){: style="height:auto;width:450px;"}

### `Name` <spam id='required'>`required`</spam>

*   The datastore name  to be created in Qualytics App.

### `Server Hostname` <spam id='required'>`required`</spam>
    
* The address of the server to connect to.

### `Http Path` <spam id='required'>`required`</spam>

* The Databricks compute resources URL.
### `Catalog` <spam id='not-required'>`optional`</spam>

* The `Catalog` name to be accessed.

* You can return the list of `catalogs` running:

```text
    SHOW CATALOGS [ LIKE regex_pattern ]
```

### `Database` <spam id='not-required'>`optional`</spam>

* The `database` name to be accessed.

* You can return the list of `databases` running:

```text
    SHOW SCHEMAS [ LIKE regex_pattern ]
```
### `Personal Access Token` <spam id='required'>`required`</spam>

* The personal access token to access databricks.

* Get the token in [Authentication requirements](https://docs.databricks.com/integrations/jdbc-odbc-bi.html#authentication).



## Information on how to retrieve the connection details
---

This section explains how to retrieve the connection details that you need to connect to Databricks.

* Get connection details for a cluster
    1. Click `Compute` in the sidebar.
    2. Choose a cluster to connect to.
    3. Navigate to `Advanced Options`.
    4. Click on the `JDBC/ODBC` tab.
    5. Copy the connection details.

* Get connection details for a SQL warehouse
    1. Click `SQL Warehouses` in the sidebar.
    2. Choose a warehouse to connect to.
    3. Navigate to the `Connection Details` tab.
    4. Copy the connection details.