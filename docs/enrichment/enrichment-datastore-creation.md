
# Add Enrichment Datastore

To add a new `Enrichment Datastore` navigate to `Datastores` page and click on the `Enrichment` tab.

![Screenshot](../assets/enrichment/create-new-enrichment-light.png#only-light){: style="width:300px"} ![Screenshot](../assets/enrichment/create-new-enrichment-dark.png#only-dark){: style="width:300px"}

    
![Screenshot](../assets/enrichment/enrichment-tab-light.png#only-light){: style="width:300px"}![Screenshot](../assets/enrichment/enrichment-tab-dark.png#only-dark){: style="width:300px"}
 
!!! info
    You can also add an `Enrichment Datastore` when you are adding a new `Datastore`

Configuring an Enrichment Datastore is a three-step process:

![Screenshot](../assets/enrichment/add-enrichment-datastore-light.png#only-light)![Screenshot](../assets/enrichment/add-enrichment-datastore-dark.png#only-dark)

1. *Ensure that the service account user has WRITE access to the datastore*
2.  Navigate to the Primary Datastore
3.  Associate the Enrichment Datastore to the Primary Datastore
 

# List of supported Enrichment Datastores

On the following links you can see how to setup each one of them:

* [Amazon S3](../../datastores/amazon-s3/#configuring-an-enrichment-datastore)
* [Azure Blob Storage](../../datastores/azure-blob-storage/#configuring-an-enrichment-datastore)
* [Azure Datalake Storage](../../datastores/azure-datalake-storage/#configuring-an-enrichment-datastore)
* [BigQuery](../../datastores/bigquery/#configuring-an-enrichment-datastore)
* [Databricks](../../datastores/databricks/#configuring-an-enrichment-datastore)
* [Google Cloud Storage](../../datastores/google-cloud-storage/#configuring-an-enrichment-datastore)
* [MariaDB](../../datastores/maria-db/#configuring-an-enrichment-datastore)
* [Microsoft SQL Server](../../datastores/microsoft-sql-server/#configuring-an-enrichment-datastore)
* [MySQL](../../datastores/mysql/#configuring-an-enrichment-datastore)
* [Oracle](../../datastores/oracle/#configuring-an-enrichment-datastore)
* [PostgreSQL](../../datastores/postgresql/#configuring-an-enrichment-datastore)
* [QFS](../../datastores/qfs/#configuring-an-enrichment-datastore)
* [Redshift](../../datastores/redshift/#configuring-an-enrichment-datastore)
* [Snowflake](../../datastores/snowflake/#configuring-an-enrichment-datastore)
* [Synapse](../../datastores/synapse/#configuring-an-enrichment-datastore)

# Configuration

* When the Datastore connection details are submitted, a synchronous `Connection Verification` operation will be initiated to verify that the indicated Datastore can be accessed appropriately from Compute Daemon. 

* The result of that operation will either return an error message to you on the new Datastore form view on failure, or mark the new Datastore as `Connected` and initiate an asynchronous `Catalog` operation on success.  

* If any future Operation is unable to establish a connection to the Datastore - the connected property of the Datastore will be set false. The UI will prompt the user to address any such Datastore connectivity issues.

* When an `Enrichment Datastore` is added, it’ll be populated in the main Enrichment Datastore listings along with other datastores:

 ![Screenshot](../assets/enrichment/main-page-light.png#only-light)
 ![Screenshot](../assets/enrichment/main-page-dark.png#only-dark)

* Clicking into a specific `Enrichment Datastore` will guide the user to the credentials page
