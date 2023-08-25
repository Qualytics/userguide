# BigQuery

## Steps to setup BigQuery

---
Fill the form with the credentials of your data source.

![Screenshot](../assets/datastores/bigquery/create-datastore-light.png#only-light){: style="width:450px;"}
![Screenshot](../assets/datastores/bigquery/create-datastore-dark.png#only-dark){: style="width:450px;"}

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

    ![Screenshot](../assets/enrichment/bigquery/create-enrichment-datastore-light.png#only-light){: style="width:450px"}
    ![Screenshot](../assets/enrichment/bigquery/create-enrichment-datastore-dark.png#only-dark){: style="width:450px"}

Once the form is completed, it's necessary to test the connection. A successful message will be shown:

![Screenshot](../assets/enrichment/test-connection-light.png#only-light){: style="width:450px;"}
![Screenshot](../assets/enrichment/test-connection-dark.png#only-dark){: style="width:450px;"}

!!! warning 
    By clicking on the `Finish` button, it will create the Datastore and link or create the Enrichment Datastore

---
## Fields

### `Name` <spam id='required'>`required`</spam>

* The datastore name  to be created in Qualytics App.
### `Project ID` <spam id='required'>`required`</spam>

* To locate your project ID:

    1. Go to the API Console.
    2. From the projects list, select Manage all projects. The names and IDs for all the projects you're a member of are displayed.

* For more information [access here.](https://support.google.com/googleapi/answer/7014113?hl=en&ref_topic=7014522)


### `Dataset ID` <spam id='required'>`required`</spam>

* You can list datasets in the following ways:
    1. Using the Google Cloud console.
    2. Using the `INFORMATION_SCHEMA` SQL query.
    3. Using the bq ls command in the bq `command-line tool`.
    4. Calling the `datasets.list` API method.
    5. Using the client libraries.
### `Temp Dataset ID` <spam id='not-required'>`optional`</spam>

* Default value: `_simba_jdbc` if the dataset for storing query results when using Legacy SQL are enabled.

* Value: `None`, if QueryDialect is set to SQL and no value is provided for `LargeResultTable`.

* For more information, see [here](https://usermanual.wiki/Document/Simba20JDBC20Driver20for20Google20BigQuery20Install20and20Configuration20Guide.1349395491/html#pf19).
### `Service Account Email`​ <spam id='required'>`required`</spam>
* A Google service account email address that has access to BigQuery application.
​

### `Service Account Key` <spam id='required'>`required`</spam>

* The service account key to access the Big Query application.

* You can download the private key file from the GoogleAPI console web page.
​
---

### `Datastore` BigQuery privileges permissions <spam id='required'>`required`</spam>


##### Read-Only Permission

Assign the `roles/bigquery.dataViewer` role to a service account or user for read-only access.

!!!role
    `roles/bigquery.dataViewer`: *Provides permissions to view table data and metadata.*

### `Enrichment Datastore` BigQuery privileges permissions <spam id='required'>`required`</spam>

##### Read-Write Permissions

Assign the combination of `roles/bigquery.dataEditor`, `roles/bigquery.dataViewer` and `roles/bigquery.jobUser` roles to a service account or user for read-write access.

!!!roles
    `roles/bigquery.dataEditor`: *Provides permissions to edit table data.*

    `roles/bigquery.dataViewer`: *Provides permissions to view table data and metadata.*

    `roles/bigquery.jobUser`: *Allows users to run jobs, including querying, loading data, exporting data, etc.*