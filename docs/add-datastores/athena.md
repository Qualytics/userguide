# Athena

Adding and configuring an Amazon Athena connection within Qualytics empowers the platform to build a symbolic link with your schema to perform operations like data discovery, visualization, reporting, cataloging, profiling, scanning, anomaly surveillance, and more.  

This documentation provides a step-by-step guide on adding Athena as a source datastore in Qualytics. It covers the entire process, from initial connection setup to testing and finalizing the configuration. 

By following these instructions, enterprises can ensure their Athena environment is properly connected with Qualytics, unlocking the platform's potential to help you proactively manage your full data quality lifecycle.  

Let’s get started 🚀

## Add the Source Datastore

A source datastore is a storage location used to connect to and access data from external sources. Athena is an example of such a datastore, specifically a type of JDBC datastore that supports connectivity through the JDBC API. Configuring the Athena datastore allows the Qualytics platform to access and perform operations on the data, thereby generating valuable insights. 

**Step 1**: Log in to your Qualytics account and click on the **Add Source Datastore** button located at the top-right corner of the interface. 

![add-source-datastore](../assets/datastores/athena/add-source-datastore-light-1.png#only-light)
![add-source-datastore](../assets/datastores/athena/add-source-datastore-dark-1.png#only-dark)

**Step 2**: A modal window- **Add Datastore** will appear, providing you with the options to connect a datastore.

![add-datastore-details](../assets/datastores/athena/add-datastore-details-light-2.png#only-light)
![add-datastore-details](../assets/datastores/athena/add-datastore-details-dark-2.png#only-dark)

| REF.              | FIELDS       | ACTIONS                                    |
|-------------------|--------------|--------------------------------------------|
| 1.                | Name         | Specify the name of the datastore (e.g., The specified name will appear on the datastore cards) |
| 2.                | Toggle Button    | Toggle **ON** to reuse credentials from an existing connection, or toggle **OFF** to create a new source datastore from scratch. |
| 3.                | Connector        | Select **Athena** from the dropdown list. |

### Option I: Create a Datastore with a new Connection

If the toggle for **Use an existing connection** is turned off, then this will prompt you to add and configure the source datastore from scratch without using existing connection details.

**Step 1**: Select the **Athena** connector from the dropdown list and add connection details such as host, port, username, password, catalog, database, etc. 

![add-source-datastore-details](../assets/datastores/athena/add-source-datastore-details-light-3.png#only-light)
![add-source-datastore-details](../assets/datastores/athena/add-source-datastore-details-dark-3.png#only-dark)

**Step 2**: The configuration form will expand, requesting credential details before establishing the connection.

![add-configutre-details](../assets/datastores/athena/add-configutre-details-light-4.png#only-light)
![add-configutre-details](../assets/datastores/athena/add-configutre-details-dark-4.png#only-dark)

| REF.              | FIELDS       | ACTIONS                                    |
|-------------------|--------------|--------------------------------------------|
| 1.                | Host         | Get **Hostname** from your account and Athena add it to this field. |
| 2.                | Port         | Specify the **Port** number. |
| 3.                | User         | Enter the **User ID** to connect. |
| 4.                | Password     | Enter the **password** to connect to the database. |
| 5.                | S3 Output Location   | Define the S3 bucket location where the output will be stored. This is specific to AWS Athena and specifies where query results are saved. |
| 6.                | Catalog      | Enter the catalog name. In AWS Athena, this refers to the data catalog that contains database and table metadata. |
| 7.                | Database     | Specify the database name. |
| 8.                | Teams        | Select one or more teams from the dropdown to associate with this source datastore. |
| 9.                | Initial Cataloging  | Tick the checkbox to automatically perform catalog operation on the configured source datastore to gather data structures and corresponding metadata. |

**Step 3**: After adding the source datastore details, click on the **Test Connection** button to check and verify its connection.

![test-source-connection](../assets/datastores/athena/test-source-connection-light-5.png#only-light)
![test-source-connection](../assets/datastores/athena/test-source-connection-dark-5.png#only-dark)

If the credentials and provided details are verified, a success message will be displayed indicating that the connection has been verified. 

### Option II: Use an Existing Connection

If the toggle for **Use an existing connection** is turned on, then this will prompt you to configure the source datastore using the existing connection details.

**Step 1**: Select a **connection** to reuse existing credentials. 

![add-datastore-details-existing](../assets/datastores/athena/add-datastore-details-existing-light-6.png#only-light)
![add-datastore-details-existing](../assets/datastores/athena/add-datastore-details-existing-dark-6.png#only-dark)

!!! note 
    If you are using existing credentials, you can only edit the details such as **Catalog**, **Database**, **Teams**, and **Initiate Cataloging**.

**Step 2**: Click on the **Test Connection** button to check and verify the source data connection. If connection details are verified, a success message will be displayed.

![test-existing-enrichment-connection](../assets/datastores/athena/test-existing-enrichment-connection-light-7.png#only-light)
![test-existing-enrichment-connection](../assets/datastores/athena/test-existing-enrichment-connection-dark-7.png#only-dark)

!!! note
    Clicking on the **Finish** button will create the source datastore and bypass the **enrichment datastore** configuration step.

!!! tip
    Click on the **Next** button, which will take you to the **enrichment datastore** configuration page.

## Add Enrichment Datastore

After successfully testing and verifying your source datastore connection, you have the option to add an enrichment datastore (recommended). This datastore is used to store analyzed results, including. This setup provides comprehensive visibility into your data quality, enabling you to manage and improve it effectively.  

!!! warning
    Qualytics does not support the Athena connector as an enrichment datastore, but you can point to a different enrichment datastore.

**Step 1**: Whether you have added a source datastore by creating a new datastore connection or using an existing connection, click on the **Next** button to start adding the **Enrichment Datastore**.

![click-source](../assets/datastores/athena/click-source-light-8.png#only-light)
![click-source](../assets/datastores/athena/click-source-dark-8.png#only-dark)

**Step 2**: A modal window- **Add Enrichment Datastore** will appear, providing you with the options to configure an **enrichment datastore**.  

![enrichment-details](../assets/datastores/athena/enrichment-details-light-9.png#only-light)
![enrichment-details](../assets/datastores/athena/enrichment-details-dark-9.png#only-dark)

| REF.              | FIELDS       | ACTIONS                                    |
|-------------------|--------------|--------------------------------------------|
| 1.                | Prefix       | Add a prefix name to uniquely identify tables/files when Qualytics writes metadata from the source datastore to your enrichment datastore. |
| 2.                | Toggle Button for existing enrichment datastore   | Toggle **ON** to link the source datastore to an existing enrichment datastore, or toggle **OFF** to link it to a brand new enrichment datastore. |
| 3.                | Name         | Give a name for the enrichment datastore. |
| 4.                | Toggle Button for using an existing connection  | Toggle **ON** to reuse credentials from an existing connection, or toggle **OFF** to create a new enrichment from scratch. |
| 5.                | Connector | Select a datastore connector as **Athena** from the dropdown list. |

### Option I: Create an Enrichment Datastore with a new Connection

If the toggles for **Use an existing enrichment datastore** and **Use an existing connection** are turned off, then this will prompt you to add and configure the enrichment datastore from scratch without using an existing enrichment datastore and its connection details.

**Step 1**: Add connection details for your selected **enrichment datastore** connector. 

!!! note
    Qualytics does not support Athena as an enrichment datastore. Instead, you can select a different enrichment datastore for this purpose. For demonstration purposes, we are using BigQuery as the enrichment datastore. You can use any other JDBC or DFS datastore of your choice for the enrichment datastore configuration.

![add-enrichment-details](../assets/datastores/athena/add-enrichment-details-light-10.png#only-light)
![add-enrichment-details](../assets/datastores/athena/add-enrichment-details-dark-10.png#only-dark)

**Step 2**: Click on the **Test Connection** button to verify the selected enrichment datastore connection. If the connection is verified, a flash message will indicate that the connection with the datastore has been successfully verified.     
   
![test-enrichment-connection](../assets/datastores/athena/test-enrichment-connection-light-11.png#only-light)
![test-enrichment-connection](../assets/datastores/athena/test-enrichment-connection-dark-11.png#only-dark)

If the connection is verified, a flash message will indicate that the connection with the datastore has been successfully verified.        

**Step 3**:  Click on the **Finish** button to complete the configuration process. 

![enrichment-details-finish](../assets/datastores/athena/enrichment-details-finish-light-12.png#only-light)
![enrichment-details-finish](../assets/datastores/athena/enrichment-details-finish-dark-12.png#only-dark)

When the configuration process is finished, a modal will display a **success message** indicating that **your datastore has been successfully added**.

![success-connection](../assets/datastores/athena/success-connection-light-13.png#only-light)
![success-connection](../assets/datastores/athena/success-connection-dark-13.png#only-dark)

**Step 4**: Close the Success dialogue and the page will automatically redirect you to the **Source Datastore Details** page where you can perform data operations on your configured **source datastore**.

![athena-created](../assets/datastores/athena/athena-created-light-14.png#only-light)
![athena-created](../assets/datastores/athena/athena-created-dark-14.png#only-dark)

### Option II: Use an Existing Connection

If the toggle for **Use an existing enrichment datastore** is turned on, you will be prompted to configure the enrichment datastore using existing connection details.

**Step 1**: Add a prefix name and select an existing enrichment datastore from the dropdown list.

!!! note
    Qualytics does not support Athena as an enrichment datastore. Instead, you can select a different enrichment datastore for this purpose. For demonstration purposes, we are using BigQuery as the enrichment datastore. You can use any other JDBC or DFS datastore of your choice for the enrichment datastore configuration.

![add-enrichment-details](../assets/datastores/athena/add-enrichment-details-light-15.png#only-light)
![add-enrichment-details](../assets/datastores/athena/add-enrichment-details-dark-15.png#only-dark)

| REF.              | FIELDS       | ACTIONS                                    |
|-------------------|--------------|--------------------------------------------|
| 1.                | Prefix       | Add a prefix name to uniquely identify tables/files when Qualytics writes metadata from the source datastore to your enrichment datastore. |
| 2.                | Toggle Button for existing enrichment datastore   | Toggle **ON** to link the source datastore to an existing enrichment datastore |
| 3.                | Enrichment Datastore  | Select an enrichment datastore from the dropdown list. |

**Step 2**: After selecting an existing **enrichment datastore** connection, you will view the following details related to the selected enrichment: 

- **Teams**: The team associated with managing the enrichment datastore is based on the role of public or private. Example- Marked as **Public** means that this datastore is accessible to all the users. 

- **Host**: This is the server address where the **Athena** instance is hosted. It is the endpoint used to connect to the PostgreSQL environment. 

- **Database**: Refers to the specific database within the Athena environment where the data is stored.

- **Schema**: The schema used in the enrichment datastore. The schema is a logical grouping of database objects (tables, views, etc.). Each schema belongs to a single database.

![add-existing-enrichment](../assets/datastores/athena/add-existing-enrichment-light-16.png#only-light)
![add-existing-enrichment](../assets/datastores/athena/add-existing-enrichment-dark-16.png#only-dark)

**Step 3**: Click on the **Finish** button to complete the configuration process for the existing **enrichment datastore**.

![click-finish](../assets/datastores/athena/click-finish-light-17.png#only-light)
![click-finish](../assets/datastores/athena/click-finish-dark-17.png#only-dark)

When the configuration process is finished, a modal will display a **success message** indicating that **your data has been successfully added**.

![success-connection](../assets/datastores/athena/success-connection-light-18.png#only-light)
![success-connection](../assets/datastores/athena/success-connection-dark-18.png#only-dark)

Close the success message and you will be automatically redirected to the **Source Datastore Details** page where you can perform data operations on your configured **source datastore**.

![athena-existing-created](../assets/datastores/athena/athena-existing-created-light-19.png#only-light)
![athena-existing-created](../assets/datastores/athena/athena-existing-created-dark-19.png#only-dark)

## API Payload Examples

This section provides a sample payload for creating a Athena datastore. Replace the placeholder values with actual data relevant to your setup.

**Endpoint (Post)**: ```/api/datastores (post)```

=== "Create a Source Datastore with a new Connection"
    ```json
    {
        "name": "your_datastore_name",
        "teams": ["Public"],
        "database": "athena_catalog",
        "schema": "athena_database",
        "enrich_only": false,
        "trigger_catalog": true,
        "connection": {
            "host": "athena_host",
            "port": 443,
            "username": "athena_user",
            "password": "athena_password",
            "parameters": { "output": "s3://<bucket_name>" },
            "type": "athena"
        }
    }
    ```
=== "Create a Source Datastore with an existing Connection"
    ```json 
    {
        "name": "your_datastore_name",
        "teams": ["Public"],
        "database": "athena_catalog",
        "schema": "athena_database",
        "enrich_only": false,
        "trigger_catalog": true,
        "connection": connection_id
    }
    ``` 

### Link an Enrichment Datastore to a Source Datastore

**Endpoint Details:** ```/api/datastores/{datastore-id}/enrichment/{enrichment-id} (patch)```