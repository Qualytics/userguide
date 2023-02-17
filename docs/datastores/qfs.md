# Qualytics File System (QFS)

## Steps to setup QFS

---
Fill the form with the credentials of your data source.

![Screenshot](../assets/datastores/qfs/create-datastore-light.png#only-light){: style="height:auto;width:450px;"}
![Screenshot](../assets/datastores/qfs/create-datastore-dark.png#only-dark){: style="height:auto;width:450px;"}

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

* The datastore name to be created in Qualytics App