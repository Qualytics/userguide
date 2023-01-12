# BigQuery

## Steps to setup BigQuery

---

![Screenshot](../assets/datastores/bigquery/create-data-store-light.png#only-light){: style="height:auto;width:450px;"}
![Screenshot](../assets/datastores/bigquery/create-data-store-dark.png#only-dark){: style="height:auto;width:450px;"}


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
