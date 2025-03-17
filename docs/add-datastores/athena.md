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
| 2.                | Toggle Button    | Toggle **ON** to create a new source datastore from scratch, or toggle **OFF** to reuse credentials from an existing connection |
| 3.                | Connector        | Select **Athena** from the dropdown list. |

### Option I: Create a Datastore with a new Connection

If the toggle for **Add New connection** is turned on, then this will prompt you to add and configure the source datastore from scratch without using existing connection details.

**Step 1**: Select the **Athena** connector from the dropdown list and add connection properties such as Secrets Management, host, port, username, and password, along with datastore properties like catalog, database, etc.

![add-source-datastore-details](../assets/datastores/athena/add-source-datastore-details-light-3.png#only-light)
![add-source-datastore-details](../assets/datastores/athena/add-source-datastore-details-dark-3.png#only-dark)

**Secrets Management**: This is an optional connection property that allows you to securely store and manage credentials by integrating with HashiCorp Vault and other secret management systems. Toggle it **ON** to enable Vault integration for managing secrets.

!!! note 
    After configuring **HashiCorp Vault** integration, you can use ${key} in any Connection property to reference a key from the configured Vault secret. Each time the Connection is initiated, the corresponding secret value will be retrieved dynamically.

| REF | FIELDS               | ACTIONS                                                                 |
|-----|----------------------|-------------------------------------------------------------------------|
| 1.  | Login URL            | Enter the URL used to authenticate with HashiCorp Vault.                |
| 2.  | Credentials Payload  | Input a valid JSON containing credentials for Vault authentication.     |
| 3.  | Token JSONPath       | Specify the JSONPath to retrieve the client authentication token from the response (e.g., $.auth.client_token). |
| 4.  | Secret URL           | Enter the URL where the secret is stored in Vault.                      |
| 5.  | Token Header Name    | Set the header name used for the authentication token (e.g., X-Vault-Token). |
| 6.  | Data JSONPath        | Specify the JSONPath to retrieve the secret data (e.g., $.data).        |

![secret-management](../assets/datastores/athena/secret-management-light-04.png#only-light)
![secret-management](../assets/datastores/athena/secret-management-dark-04.png#only-dark)

**Step 2**: The configuration form, requesting credential details before establishing the connection.

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

If the toggle for **Add New connection** is turned off, then this will prompt you to configure the source datastore using the existing connection details.

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

**Step 2**:  A modal window- **Link Enrichment Datastore** will appear, providing you with the options to configure an **enrichment datastore**.
  
![enrichment-details](../assets/datastores/athena/enrichment-details-light-9.png#only-light)
![enrichment-details](../assets/datastores/athena/enrichment-details-dark-9.png#only-dark)

| REF.              | FIELDS       | ACTIONS                                    |
|-------------------|--------------|--------------------------------------------|
| 1.                | Prefix       | Add a prefix name to uniquely identify tables/files when Qualytics writes metadata from the source datastore to your enrichment datastore. |
| 2.                | Caret Down Button   | Click the caret down to select either **Use Enrichment Datastore** or **Add Enrichment Datastore**.|
| 3.                | Enrichment Datastore         | Select an enrichment datastore from the dropdown list. |

### Option I: Create an Enrichment Datastore with a new Connection

If the toggles for **Add New connection is turned on**, then this will prompt you to add and configure the enrichment datastore from scratch without using an existing enrichment datastore and its connection details.

**Step 1**: Click on the caret button and select Add Enrichment Datastore.

![select-enrichment](../assets/datastores/athena/select-enrichment-light-10.png#only-light)
![select-enrichment](../assets/datastores/athena/select-enrichment-dark-10.png#only-dark)

A modal window **Link Enrichment Datastore** will appear. Enter the following details to create an enrichment datastore with a new connection

![enrichment-detail](../assets/datastores/athena/enrichment-details-light-11.png#only-light)
![enrichment-detail](../assets/datastores/athena/enrichment-details-dark-11.png#only-dark)

| REF.              | FIELDS       | ACTIONS                                    |
|-------------------|--------------|--------------------------------------------|
| 1.                | Prefix       | Add a prefix name to uniquely identify tables/files when Qualytics writes metadata from the source datastore to your enrichment datastore. |
| 2.                | Name   | Give a name for the enrichment datastore.|
| 3.                |Toggle Button for add new connection | Toggle ON to create a new enrichment from scratch or toggle OFF to reuse credentials from an existing connection. |
| 4.                |Connector | Select a datastore connector from the dropdown list.|

**Step 2**: Add connection details for your selected **enrichment datastore** connector. 

!!! note
    Qualytics does not support Athena as an enrichment datastore. Instead, you can select a different enrichment datastore for this purpose. For demonstration purposes, we are using BigQuery as the enrichment datastore. You can use any other JDBC or DFS datastore of your choice for the enrichment datastore configuration.

![add-enrichment-details](../assets/datastores/athena/add-enrichment-details-light-12.png#only-light)
![add-enrichment-details](../assets/datastores/athena/add-enrichment-details-dark-12.png#only-dark)

**Step 3**: Click on the **Test Connection** button to verify the selected enrichment datastore connection. If the connection is verified, a flash message will indicate that the connection with the datastore has been successfully verified.     
   
![test-enrichment-connection](../assets/datastores/athena/test-enrichment-connection-light-13.png#only-light)
![test-enrichment-connection](../assets/datastores/athena/test-enrichment-connection-dark-13.png#only-dark)

If the connection is verified, a flash message will indicate that the connection with the datastore has been successfully verified.        

**Step 4**:  Click on the **Finish** button to complete the configuration process. 

![enrichment-details-finish](../assets/datastores/athena/enrichment-details-finish-light-14.png#only-light)
![enrichment-details-finish](../assets/datastores/athena/enrichment-details-finish-dark-14.png#only-dark)

When the configuration process is finished, a modal will display a **success message** indicating that **your datastore has been successfully added**.

![success-connection](../assets/datastores/athena/success-connection-light-15.png#only-light)
![success-connection](../assets/datastores/athena/success-connection-dark-15.png#only-dark)

**Step 5**: Close the Success dialogue and the page will automatically redirect you to the **Source Datastore Details** page where you can perform data operations on your configured **source datastore**.

![athena-created](../assets/datastores/athena/athena-created-light-16.png#only-light)
![athena-created](../assets/datastores/athena/athena-created-dark-16.png#only-dark)

### Option II: Use an Existing Connection

If the toggle for **Use an existing enrichment datastore** is turned on, you will be prompted to configure the enrichment datastore using existing connection details.

**Step 1**: Click on the caret button and select **Use Enrichment Datastore**.

![select-enrichment-details](../assets/datastores/athena/select-enrichment-light-17.png#only-light)
![select-enrichment-details](../assets/datastores/athena/select-enrichment-dark-17.png#only-dark)

**Step 2**: A modal window **Link Enrichment Datastore** will appear. Add a prefix name and select an existing enrichment datastore from the dropdown list.

!!! note
    Qualytics does not support Athena as an enrichment datastore. Instead, you can select a different enrichment datastore for this purpose. For demonstration purposes, we are using BigQuery as the enrichment datastore. You can use any other JDBC or DFS datastore of your choice for the enrichment datastore configuration.

![add-enrichment-details](../assets/datastores/athena/add-enrichment-details-light-18.png#only-light)
![add-enrichment-details](../assets/datastores/athena/add-enrichment-details-dark-18.png#only-dark)

| REF.              | FIELDS       | ACTIONS                                    |
|-------------------|--------------|--------------------------------------------|
| 1.                | Prefix       | Add a prefix name to uniquely identify tables/files when Qualytics writes metadata from the source datastore to your enrichment datastore. |
| 2.                | Enrichment Datastore  | Select an enrichment datastore from the dropdown list. |

**Step 3**: After selecting an existing **enrichment datastore** connection, you will view the following details related to the selected enrichment: 

- **Teams**: The team associated with managing the enrichment datastore is based on the role of public or private. Example- Marked as **Public** means that this datastore is accessible to all the users. 

- **Host**: This is the server address where the **Athena** instance is hosted. It is the endpoint used to connect to the PostgreSQL environment. 

- **Database**: Refers to the specific database within the Athena environment where the data is stored.

- **Schema**: The schema used in the enrichment datastore. The schema is a logical grouping of database objects (tables, views, etc.). Each schema belongs to a single database.

![add-existing-enrichment](../assets/datastores/athena/add-existing-enrichment-light-19.png#only-light)
![add-existing-enrichment](../assets/datastores/athena/add-existing-enrichment-dark-19.png#only-dark)

**Step 4**: Click on the **Finish** button to complete the configuration process for the existing **enrichment datastore**.

![click-finish](../assets/datastores/athena/click-finish-light-20.png#only-light)
![click-finish](../assets/datastores/athena/click-finish-dark-20.png#only-dark)

When the configuration process is finished, a modal will display a **success message** indicating that **your data has been successfully added**.

![success-connection](../assets/datastores/athena/success-connection-light-21.png#only-light)
![success-connection](../assets/datastores/athena/success-connection-dark-21.png#only-dark)

Close the success message and you will be automatically redirected to the **Source Datastore Details** page where you can perform data operations on your configured **source datastore**.

![athena-existing-created](../assets/datastores/athena/athena-existing-light-22.png#only-light)
![athena-existing-created](../assets/datastores/athena/athena-existing-dark-22.png#only-dark)

## API Payload Examples

### Creating a Source Datastore

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
