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


## BigQuery Roles <spam id='required'>`required`</spam>

### BigQuery Data Editor (`roles/bigquery.dataEditor`):

This role extends beyond viewing capabilities and allows the user to modify data within existing tables and datasets in BigQuery. It includes permissions for altering data (such as `bigquery.tables.updateData`), adding new tables, and modifying table schemas (`bigquery.tables.update`). This role is suitable for applications and services that need to perform regular updates or insertions to data within BigQuery, including data management tasks via the JDBC driver.

### BigQuery Data Viewer (`roles/bigquery.dataViewer`):

This role grants permissions to view datasets, tables, and their data in BigQuery. It includes permissions like `bigquery.tables.get`, `bigquery.tables.list`, and `bigquery.datasets.get`. These are essential for the JDBC driver to read the schema and data of the tables.

### BigQuery Job User (`roles/bigquery.jobUser`):

This role allows the user to create and manage their own jobs, which includes query jobs, load jobs, and export jobs. The key permission here is `bigquery.jobs.create`. Since the JDBC driver needs to execute queries (including temporary query results), this permission is crucial for operations that involve processing and returning query results.

### BigQuery Read Session User (`roles/bigquery.readSessionUser`):

This role is particularly relevant when using the `BigQuery Storage API`, which can be leveraged by the JDBC driver for more efficient data retrieval. This role enables the creation and use of read sessions for the `BigQuery Storage API`, which are needed for large-scale data transfers and streaming read operations. It’s particularly useful for performance optimization in data reading scenarios.

### `Datastore` BigQuery privileges permissions <spam id='required'>`required`</spam>


#### Read-Only Permissions

!!!roles
    `roles/bigquery.dataViewer`: *Provides permissions to view table data and metadata.*

    `roles/bigquery.jobUser`: *Allows users to run jobs, including querying, loading data, etc.*

    `roles/bigquery.readSessionUser`: *Grants permissions to create read sessions for the BigQuery Storage API, enabling efficient, high-throughput data reads without broader data management capabilities.*

### `Enrichment Datastore` BigQuery privileges permissions <spam id='required'>`required`</spam>

#### Read-Write Permissions

Assign the combination of `roles/bigquery.dataEditor`, `roles/bigquery.dataViewer` and `roles/bigquery.jobUser` roles to a service account or user for read-write access.

!!!roles
    `roles/bigquery.dataEditor`: *Provides permissions to edit table data.*

    `roles/bigquery.dataViewer`: *Provides permissions to view table data and metadata.*

    `roles/bigquery.jobUser`: *Allows users to run jobs, including querying, loading data, etc.*

    `roles/bigquery.readSessionUser`: *Grants permissions to create read sessions for the BigQuery Storage API, enabling efficient, high-throughput data reads without broader data management capabilities.*

## Recommendations: Create a Temporary Dataset

Create a Temporary Dataset with Table Expiration Set to 1 Hour.

Using a temporary dataset in BigQuery is critical for managing intermediate query results and temporary tables created during query execution, especially when using the Google BigQuery JDBC driver. 

This setup ensures efficient data management, optimizes performance, and reduces storage costs by automatically deleting data that is no longer needed.

### Step 1: Create a Temporary Dataset

#### Access the BigQuery Console

Navigate to the BigQuery console within your Google Cloud Platform (GCP) account.

#### Create New Dataset
1. Project Selection: Ensure you are in the project where BigQuery is enabled.
2. Initiate Dataset Creation: Click on "Create Dataset" located on the right-hand side of the interface.
3. Configure Dataset: Dataset ID: Enter a name that indicates it is for temporary use, such as `temp_dataset`.

### Step 2: Set Default Table Expiration

When setting up the dataset, specify a default table expiration time. This setting automatically assigns a lifespan to all tables created within this dataset, ensuring they are deleted after the time elapses.

#### Set Dataset Info

- Dataset Location: Select the appropriate location that aligns with where your other datasets reside, minimizing data transfer delays.
- Default Table Expiration: Input `3600` seconds (`1 hour`) to ensure any table created under this dataset expires and is automatically deleted one hour after its creation.
#### Finalize Dataset Creation

##### Create Dataset

Click the "Create dataset" button to apply these settings and establish the temporary dataset.

### Step 3: Configure JDBC Driver

Configure the JDBC driver to utilize this temporary dataset. This typically involves modifying the JDBC URL or configuration settings to direct intermediate storage to this dataset.
