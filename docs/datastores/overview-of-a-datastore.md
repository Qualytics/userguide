# Overview of a datastore

* A `Datastore` can be any Apache Spark-compatible data source, such as:
    1. Traditional `RDBMS`.
    2. Raw files (`CSV`, `XLSX`, `JSON`, `Avro`, `Parquet`) on:
        1. AWS S3.
        2. Azure Blob Storage.
        3. GCP Cloud Storage.

*  A `Datastore` is a medium holding structured data. Qualytics supports Spark-compatible Datastores via the conceptual layers depicted below

    ![Screenshot](../assets/datastores/what-is/qualytics-architecture.png)

--- 
# Configuration


* The first step of configuring a Qualytics instance is to Add New Datastore:
    - In the `main` menu, select `Datastores` tab
    - Click on `Add New Datastore` button:
    
    - ![Screenshot](../assets/datastores/what-is/add-new-datastore-button-light.png#only-light)
      ![Screenshot](../assets/datastores/what-is/add-new-datastore-button-dark.png#only-dark)

    ![Screenshot](../assets/datastores/what-is/add-datastore-light.png#only-light){: style="width:450px"}
    ![Screenshot](../assets/datastores/what-is/add-datastore-dark.png#only-dark){: style="width:450px"}

    !!! info 
        * A datastore can be any Apache Spark-compatible data source:
            
            1. traditional RDBMS, 
            2. raw files (`CSV`, `XLSX`, `JSON`, `Avro`, `Parquet` etc...) on :
                3. `AWS S3`.
                4. `Azure Blob Storage`.
                5. `GCP Cloud Storage`

    ![Screenshot](../assets/datastores/what-is/listing-datastores-light.png#only-light){: style="width:450px"}
    ![Screenshot](../assets/datastores/what-is/listing-datastores-dark.png#only-dark){: style="width:450px"}


# Credentials
* Configuring a datastore will require you to enter configuration credentials dependent upon each datastore. Here is an example of a Snowflake datastore being added:


    ![Screenshot](../assets/datastores/what-is/add-snowflake-datastore-light.png#only-light){: style="width:450px"}
    ![Screenshot](../assets/datastores/what-is/add-snowflake-datastore-dark.png#only-dark){: style="width:450px"}

* When a datastore is added, it’ll be populated in the home screen along with other datastores:

    ![Screenshot](../assets/datastores/what-is/show-all-created-datastores-light.png#only-light)
    ![Screenshot](../assets/datastores/what-is/show-all-created-datastores-dark.png#only-dark)


* Clicking into a datastore will guide the user through the capabilities and operations of the platform. 

*When a user configures a datastore for the first time, they’ll see an empty Activity tab.*

![Screenshot](../assets/datastores/what-is/specific-datastore-light.png#only-light)
![Screenshot](../assets/datastores/what-is/specific-datastore-dark.png#only-dark)

* Heatmap view

![Screenshot](../assets/datastores/what-is/data-volume-light.png#only-light)
![Screenshot](../assets/datastores/what-is/data-volume-dark.png#only-dark)

# Running a Catalog of the Datastore
* The first operation of Catalog will automatically kick off. You can see this through the Activity tab. 
    * This operation typically takes a short amount of time to complete. 
    * After this is completed, they’ll need to run a Profile operation (under `Run` -> `Profile`) to generate metadata and infer data quality checks. 

    ![Screenshot](../assets/datastores/what-is/running-profile-menu-light.png#only-light)
    ![Screenshot](../assets/datastores/what-is/running-profile-menu-dark.png#only-dark)

    ![Screenshot](../assets/datastores/what-is/running-profile-light.png#only-light){: style="height:auto"}
    ![Screenshot](../assets/datastores/what-is/running-profile-dark.png#only-dark){: style="height:auto"}
