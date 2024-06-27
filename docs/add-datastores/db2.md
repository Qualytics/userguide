# DB2

Adding and configuring a DB2 connection within Qualytics empowers the platform to build a symbolic link with your schema to perform operations like data discovery, visualization, reporting, cataloging, profiling, scanning, anomaly surveillance, and more.  

This documentation provides a step-by-step guide on how to add DB2 as both a source and enrichment datastore in Qualytics. It covers the entire process, from initial connection setup to testing and finalizing the configuration. 

By following these instructions, enterprises can ensure their DB2 environment is properly connected with Qualytics, unlocking the platform's potential to help you proactively manage your full data quality lifecycle. 

Let’s get started 🚀

## Add a Source Datastore

A source datastore is a storage location used to connect to and access data from external sources. DB2 is an example of a source datastore, specifically a type of JDBC datastore that supports connectivity through the JDBC API. Configuring the JDBC datastore enables the Qualytics platform to access and perform operations on the data, thereby generating valuable insights.

**Step 1:** Log in to your Qualytics account and click on the **Add Source Datastore** button located at the top-right corner of the interface. 

![add-datastore](../assets/datastores/db2/add-datastore-light.png#only-light)
![add-datastore](../assets/datastores/db2/add-datastore-dark.png#only-dark)

**Step 2:** A modal window- **Add Datastore** will appear, providing you with the options to connect a datastore.

![select-a-connector](../assets/datastores/db2/select-a-connector-light.png#only-light)
![select-a-connector](../assets/datastores/db2/select-a-connector-dark.png#only-dark)

| REF.         | FIELDS       | ACTIONS                                                                 |
|--------------|--------------|-------------------------------------------------------------------------|
| 1.      | Name (Required)     | Specify the datastore name (e.g., This name will appear on the datastore cards) |
| 2.       | Toggle Button | Toggle ON to reuse credentials from an existing connection, or toggle OFF to create a new source datastore from scratch. |
| 3.      | Connector (Required)   | Select **DB2** from the dropdown list.                                      |

### Option I: Create a Source Datastore with a new Connection

If the toggle for **Use an existing connection** is turned off, then this will prompt you to add and configure the source datastore from scratch without using existing connection details.

**Step 1:** Select the **DB2** connector from the dropdown list and add connection details such as host, port, user, password, SSL connection, database, and schema.

![add-datastore-credentials](../assets/datastores/db2/add-datastore-credentials-light.png#only-light)
![add-datastore-credentials](../assets/datastores/db2/add-datastore-credentials-dark.png#only-dark)

**Step 2:** The configuration form will expand, requesting credential details before establishing the connection.

![add-datastore-credentials-explain](../assets/datastores/db2/add-datastore-credentials-explain-light.png#only-light)
![add-datastore-credentials-explain](../assets/datastores/db2/add-datastore-credentials-explain-dark.png#only-dark)

| REF.         | FIELDS               | ACTIONS                                                                                     |
|--------------|----------------------|---------------------------------------------------------------------------------------------|
| 1.       | Host (Required)             | Get **Hostname** from your DB2 account and add it to this field.                              |
| 2.       | Port (Required)           | Specify the **Port** number.                                                                   |
| 3.       | User (Required)             | Enter the **User ID** to connect.                                                              |
| 4.       | Password (Required)         | Enter the **password** to connect to the database.                                             |
| 5.       | SSL Connection    | Enable the SSL connection to ensure secure communication between Qualytics and the selected datastore. |
| 6.       | Database (Required)         | Specify the database name.                                                                   |
| 7.       | Schema (Required)           | Define the schema within the database that should be used.                                    |
| 8.       | Teams (Required)            | Select one or more teams from the dropdown to associate with this source datastore.           |
| 9.       | Initial Catalog   | Tick the checkbox to automatically perform catalog operation on the configured source datastore to gather data structures and corresponding metadata. |

**Step 3:** After adding the source datastore details, click on the **Test Connection** button to check and verify its connection.

![test-datastore-connection](../assets/datastores/db2/test-datastore-connection-light.png#only-light)
![test-datastore-connection](../assets/datastores/db2/test-datastore-connection-dark.png#only-dark)

If the credentials and provided details are verified, a success message will be displayed indicating that the connection has been verified. 

### Option II: Use an Existing Connection

If the toggle for **Use an existing connection** is turned on, then this will prompt you to configure the source datastore using the existing connection details.

**Step 1:** Select a **connection** to reuse existing credentials.

![use-existing-datastore](../assets/datastores/db2/use-existing-datastore-light.png#only-light)
![use-existing-datastore](../assets/datastores/db2/use-existing-datastore-dark.png#only-dark)

!!!note
     If you are using existing credentials, you can only edit the details such as Database, Schema, Teams, and Initiate Cataloging. 

**Step 2:** Click on the **Test Connection** button to verify the existing connection details. If connection details are verified, a success message will be displayed.

![test-connection-for-existing-datastore](../assets/datastores/db2/test-connection-for-existing-datastore-light.png#only-light)
![test-connection-for-existing-datastore](../assets/datastores/db2/test-connection-for-existing-datastore-dark.png#only-dark)

!!!note
    Clicking on the **Finish** button will create the source datastore and bypass the **enrichment datastore** configuration step.

!!!tip
    It is recommended to click on the **Next** button, which will take you to the **enrichment datastore** configuration page.

## Add Enrichment Datastore

Once you have successfully tested and verified your source datastore connection, you have the option to add the enrichment datastore (recommended). This datastore is used to store the analyzed results, including any anomalies and additional metadata in tables. This setup provides full visibility into your data quality, helping you manage and improve it effectively.

**Step 1:** Whether you have added a source datastore by creating a new datastore connection or using an existing connection, click on the **Next** button to start adding the **Enrichment Datastore**.

![next-button-for-enrichment](../assets/datastores/db2/next-button-for-enrichment-light.png#only-light)
![next-button-for-enrichment](../assets/datastores/db2/next-button-for-enrichment-dark.png#only-dark)

**Step 2:** A modal window- **Add Enrichment Datastore** will appear, providing you with the options to configure an **enrichment datastore**.

![select-enrichment-connector](../assets/datastores/db2/select-enrichment-connector-light.png#only-light)
![select-enrichment-connector](../assets/datastores/db2/select-enrichment-connector-dark.png#only-dark)

| REF.         | FIELDS                                            | ACTIONS                                                                                     |
|--------------|---------------------------------------------------|---------------------------------------------------------------------------------------------|                                               
| 1.       | Prefix (Required)                                        | Add a prefix name to uniquely identify tables/files when Qualytics writes metadata from the source datastore to your enrichment datastore. |
| 2.      | Toggle Button for existing enrichment datastore | Toggle ON to link the source datastore to an existing enrichment datastore, or toggle OFF to link it to a brand new enrichment datastore. |
| 3.      | Name (Required)                                       | Give a name for the enrichment datastore.                                                    |
| 4.       | Toggle Button for using an existing connection | Toggle ON to reuse credentials from an existing connection, or toggle OFF to create a new enrichment from scratch. |
| 5.       | Connector (Required)                                   | Select a datastore connector as **DB2** from the dropdown list.                                |

### Option I: Create an Enrichment Datastore with a new Connection

If the toggles for **Use an existing enrichment datastore** and **Use an existing connection** are turned off, then this will prompt you to add and configure the enrichment datastore from scratch without using an existing enrichment datastore and its connection details.

**Step 1:** Add connection details for your selected **enrichment datastore** connector.

![enrichment-datastore-explain](../assets/datastores/db2/enrichment-datastore-explain-light.png#only-light)
![enrichment-datastore-explain](../assets/datastores/db2/enrichment-datastore-explain-dark.png#only-dark)

| REF.         | FIELDS         | ACTIONS                                                                                     |
|--------------|----------------|--------------------------------------------------------------------------------------------|
| 1.       | Host        | Get **Hostname** from your DB2 account and add it to this field.                              |
| 2.       | Port        | Specify the **Port** number.                                                                   |
| 3.       | User         | Enter the **User ID** to connect.                                                              |
| 4.       | Password   | Enter the **password** to connect to the database.                                             |
| 5.       | SSL Connection | Enable the SSL connection to ensure secure communication between Qualytics and the selected datastore. |
| 6.       | Database    | Specify the database name.                                                                   |
| 7.      | Schema       | Define the schema within the database that should be used.                                    |
| 8.       | Teams        | Select one or more teams from the dropdown to associate with this datastore.                 |


**Step 2:**  Click on the **Test Connection** button to verify the selected enrichment datastore connection. If the connection is verified, a flash message will indicate that the connection with the enrichment datastore has been successfully verified. 

![test-connection-for-enrichment-datastore](../assets/datastores/db2/test-connection-for-enrichment-datastore-light.png#only-light)
![test-connection-for-enrichment-datastore](../assets/datastores/db2/test-connection-for-enrichment-datastore-dark.png#only-dark)

**Step 3:** Click on the **Finish** button to complete the configuration process. 

![finish-configuration](../assets/datastores/db2/finish-configuration-light.png#only-light)
![finish-configuration](../assets/datastores/db2/finish-configuration-dark.png#only-dark)


When the configuration process is finished, a modal will display a **success message** indicating that **your datastore has been successfully added**.

![success-message](../assets/datastores/db2/success-message-light.png#only-light)
![success-message](../assets/datastores/db2/success-message-dark.png#only-dark)

**Step 4:** Close the Success dialog and the page will automatically redirect you to the **Source Datastore Details** page where you can perform data operations on your configured **source datastore**.

![data-operation-page](../assets/datastores/db2/data-operation-page-light.png#only-light)
![data-operation-page](../assets/datastores/db2/data-operation-page-dark.png#only-dark)

### Option II: Use an Existing Connection

If the toggle for **Use an existing enrichment datastore** is turned on, you will be prompted to configure the datastore using existing connection details.

**Step 1:** Add a prefix name and select an existing enrichment datastore from the dropdown list.

![select-existing-enrichment-datastore](../assets/datastores/db2/select-existing-enrichment-datastore-light.png#only-light)
![select-existing-enrichment-datastore](../assets/datastores/db2/select-existing-enrichment-datastore-dark.png#only-dark)

| REF. | FIELDS                             | ACTIONS                                                                                                      |
|------|------------------------------------|--------------------------------------------------------------------------------------------------------------|
| 1️.  | Prefix (Required)                            | Add a prefix name to uniquely identify tables/files when Qualytics writes metadata from the source datastore to your enrichment datastore. |
| 2️.   | Toggle Button for existing enrichment datastore | Toggle ON to link the source datastore to an existing enrichment datastore.                                    |
| 3️.   | Enrichment Datastore               | Select an enrichment datastore from the dropdown list.                                                         |

**Step 2:** After selecting an existing **enrichment datastore** connection, you will view the following details related to the selected enrichment: 

- **Teams:** The team associated with managing the enrichment datastore is based on the role of public or private. Example- Marked as **Public** means that this datastore is accessible to all the users. 

 - **Host:** This is the server address where the DB2 instance is hosted. It is the endpoint used to connect to the DB2 environment. 

 - **Database:** Refers to the specific database within the DB2 environment where the data is stored.

 - **Schema:** The schema used in the enrichment datastore. The schema is a logical grouping of database objects (tables, views, etc.). Each schema belongs to a single database.

 ![use-existing-enrichment-datastore](../assets/datastores/db2/use-existing-enrichment-datastore-light.png#only-light)
![use-existing-enrichment-datastore](../assets/datastores/db2/use-existing-enrichment-datastore-dark.png#only-dark)

**Step 3:** Click on the **Finish** button to complete the configuration process for the existing **enrichment datastore**.

![finish-configuration-for-existing-enrichment-datastore](../assets/datastores/db2/finish-configuration-for-existing-enrichment-datastore-light.png#only-light)
![finish-configuration-for-existing-enrichment-datastore](../assets/datastores/db2/finish-configuration-for-existing-enrichment-datastore-dark.png#only-dark)

When the configuration process is finished, a modal will display a **success message** indicating that **your data has been successfully added**.

![success-message](../assets/datastores/db2/success-message-light.png#only-light)
![success-message](../assets/datastores/db2/success-message-dark.png#only-dark)

Close the success message and you will be automatically redirected to the **Source Datastore Details** page where you can perform data operations on your configured **source datastore**.

![data-operation-page](../assets/datastores/db2/data-operation-page-light.png#only-light)
![data-operation-page](../assets/datastores/db2/data-operation-page-dark.png#only-dark)

## API Payload Examples

This section provides detailed examples of API payloads to guide you through the process of creating and managing datastores using Qualytics API. Each example includes endpoint details, sample payloads, and instructions on how to replace placeholder values with actual data relevant to your setup.

### Creating a Source Datastore

This section provides sample payloads for creating a DB2 datastore. Replace the placeholder values with actual data relevant to your setup.

**Endpoint:** ```/api/datastores (post)```

=== "Create a Source Datastore with a new Connection"
    ```json
    {
        "name": "your_datastore_name",
        "teams": ["Public"],
        "database": "db2_database",
        "schema": "db2_schema",
        "enrich_only": false,
        "trigger_catalog": true,
        "connection": {
            "name": "your_connection_name",
            "type": "db2",
            "host": "db2_host",
            "port": "db2_port",
            "username": "db2_username",
            "password": "db2_password",
            "parameters": {
                "ssl": true
            }
        }
    }
    ```
=== "Create a Source Datastore with an existing Connection"
    ```json
    {
        "name": "your_datastore_name",
        "teams": ["Public"],
        "database": "db2_database",
        "schema": "db2_schema",
        "enrich_only": false,
        "trigger_catalog": true,
        "connection_id": connection-id
    }
    ```

### Creating an Enrichment Datastore

This section provides sample payloads for creating an enrichment datastore. Replace the placeholder values with actual data relevant to your setup.

**Endpoint:**  ```/api/datastores (post)```

=== "Create an Enrichment Datastore with a new Connection"
    ```json
    {
        "name": "your_datastore_name",
        "teams": ["Public"],
        "database": "db2_database",
        "schema": "db2_enrichment_schema",
        "enrich_only": true,
        "connection": {
            "name": "your_connection_name",
            "type": "db2",
            "host": "db2_host",
            "port": "db2_port",
            "username": "db2_username",
            "password": "db2_password",
            "parameters": {
                "ssl": true
            }
        }
    }
    ```
=== "Create an Enrichment Datastore with an existing Connection"
    ```json
    {
        "name": "your_datastore_name",
        "teams": ["Public"],
        "database": "db2_database",
        "schema": "db2_enrichment_schema",
        "enrich_only": true,
        "connection_id": connection-id
    }
    ``` 

### Link an Enrichment Datastore to a Source Datastore
Use the provided endpoint to link an enrichment datastore to a source datastore: 

**Endpoint Details:** ```/api/datastores/{datastore-id}/enrichment/{enrichment-id} (patch)```
