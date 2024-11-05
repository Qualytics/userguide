# Oracle

Adding and configuring an Oracle connection within Qualytics empowers the platform to build a symbolic link with your schema to perform operations like data discovery, visualization, reporting, cataloging, profiling, scanning, anomaly surveillance, and more.

This documentation provides a step-by-step guide on how to add Oracle as both a source and enrichment datastore in Qualytics. It covers the entire process, from initial connection setup to testing and finalizing the configuration.

By following these instructions, enterprises can ensure their Oracle environment is properly connected with Qualytics, unlocking the platform's potential to help you proactively manage your full data quality lifecycle.

Let’s get started 🚀

## Add the Source Datastore

A source datastore is a storage location used to connect to and access data from external sources. Oracle, for example, is a type of JDBC datastore that supports connectivity through the JDBC API. Configuring the Oracle datastore allows the Qualytics platform to access and perform operations on the data, thereby generating valuable insights.

**Step 1:** Log in to your Qualytics account and click on the **Add Source Datastore** button located at the top-right corner of the interface.

![add-source-datastore](../assets/datastores/oracle/add-source-datastore-light.png#only-light)
![add-source-datastore](../assets/datastores/oracle/add-source-datastore-dark.png#only-dark)

**Step 2:** A modal window- **Add Datastore** will appear, providing you with the options to connect a datastore.

![add-datastore-details](../assets/datastores/oracle/add-datastore-details-light.png#only-light)
![add-datastore-details](../assets/datastores/oracle/add-datastore-details-dark.png#only-dark)

| Step | Description |
|------|-------------|
| 1️. | **Name** <br> Specify the name of the datastore (e.g., The specified name will appear on the datastore cards) |
| 2️. | **Toggle Button** <br> Toggle ON to create a new source datastore from scratch, or toggle OFF to reuse credentials from an existing connection. |
| 3️. | **Connector** <br> Select “Oracle” from the dropdown list. |

### Option I: Create a Source Datastore with a new Connection

If the toggle for **Add new connection** is turned on, then this will prompt you to add and configure the source datastore from scratch without using existing connection details.

**Step 1:** Select the **Oracle** connector from the dropdown list and add connection details such as such as Secret Management, host, port, username, sid, and schema.

![add-source-datastore-details](../assets/datastores/oracle/add-source-datastore-details-light.png#only-light)
![add-source-datastore-details](../assets/datastores/oracle/add-source-datastore-details-dark.png#only-dark)

**Secrets Management**: This is an optional connection property that allows you to securely store and manage credentials by integrating with HashiCorp Vault and other secret management systems. Toggle it **ON** to enable Vault integration for managing secrets.

!!! note 
    Once the **HashiCorp Vault** is set up, use the $<secret_name> format in Connection form to reference a Vault secret.

| REF | FIELDS               | ACTIONS                                                                 |
|-----|----------------------|-------------------------------------------------------------------------|
| 1.  | Login URL            | Enter the URL used to authenticate with HashiCorp Vault.                |
| 2.  | Credentials Payload  | Input a valid JSON containing credentials for Vault authentication.     |
| 3.  | Token JSONPath       | Specify the JSONPath to retrieve the client authentication token from the response (e.g., $.auth.client_token). |
| 4.  | Secret URL           | Enter the URL where the secret is stored in Vault.                      |
| 5.  | Token Header Name    | Set the header name used for the authentication token (e.g., X-Vault-Token). |
| 6.  | Data JSONPath        | Specify the JSONPath to retrieve the secret data (e.g., $.data).        |

![hashcorp-explain](../assets/datastores/oracle/hashcorp-explain-light.png#only-light)
![hashcorp-explain](../assets/datastores/oracle/hashcorp-explain-dark.png#only-dark)

**Step 2:** The configuration form will expand, requesting credential details before establishing the connection.

![add-datasource-details](../assets/datastores/oracle/add-data-source-details-light.png#only-light)
![add-datasource-details](../assets/datastores/oracle/add-data-source-details-dark.png#only-dark)

| REF. | FIELDS  | ACTIONS    |
|------|---------------|---------|
| 1️. | Host | Get “Hostname” from your Oracle account and add it to this field. |
| 2️. | Port | Specify the “Port” number.|
| 3️. | User | Enter the “User ID” to connect. |
| 4️. | Password | Enter the “password” to connect to the database. |
| 5️. | Database | Specify the database name.|
| 6️. | Schema | Define the schema within the database that should be used.|
| 7️. | Teams | Select one or more teams from the dropdown to associate with this source data     store. |
| 8️. | Initial Cataloging | Tick the checkbox to automatically perform catalog operation on the configured source datastore to gather data structures and corresponding metadata. |

**Step 3:** After adding the source datastore details, click on the **Test Connection** button to check and verify its connection.

![test-source-datastore](../assets/datastores/oracle/test-source-datastore-light.png#only-light)
![test-source-datastore](../assets/datastores/oracle/test-source-datastore-dark.png#only-dark)

If the credentials and provided details are verified, a success message will be displayed indicating that the connection has been verified.

### Option II: Use an Existing Connection

If the toggle for **add new connection** is turned off, then this will prompt you to configure the source datastore using the existing connection details.

**Step 1:** Select a **connection** to reuse existing credentials.

![existing-source-datastore](../assets/datastores/oracle/existing-source-datastore-light.png#only-light)
![existing-source-datastore](../assets/datastores/oracle/existing-source-datastore-dark.png#only-dark)

!!! note
    If you are using existing credentials, you can only edit the details such as Database, Schema, Teams, and Initiate Cataloging.

**Step 2:** Click on the **Test Connection** button to verify the existing connection details. If connection details are verified, a success message will be displayed.

![test-existing-connection](../assets/datastores/oracle/test-existing-connection-light.png#only-light)
![test-existing-connection](../assets/datastores/oracle/test-existing-connection-dark.png#only-dark)

!!! note
    Clicking on the **Finish** button will create the source datastore and bypass the **enrichment datastore** configuration step.

!!! tip
    It is recommended to click on the **Next** button, which will take you to the **enrichment datastore** configuration page.

## Add Enrichment Datastore

Once you have successfully tested and verified your source datastore connection, you have the option to add the enrichment datastore (recommended). The enrichment datastore is used to store the analyzed results, including any anomalies and additional metadata in tables. This setup provides full visibility into your data quality, helping you manage and improve it effectively.

!!! warning
    Qualytics does not support the Oracle connector as an enrichment datastore, but you can point to a different enrichment datastore.

**Step 1:** Whether you have added a source datastore by creating a new datastore connection or using an existing connection, click on the **Next** button to start adding the **Enrichment Datastore**.

![click-next-datastore](../assets/datastores/oracle/click-next-datastore-light.png#only-light)
![click-next-datastore](../assets/datastores/oracle/click-next-datastore-dark.png#only-dark)

**Step 2:** A modal window **Link Enrichment Datastore** will appear, providing you with the options to configure an **enrichment datastore**.

![add-enrichment](../assets/datastores/oracle/add-enrichment-light.png#only-light)
![add-enrichment](../assets/datastores/oracle/add-enrichment-dark.png#only-dark)

| REF. | FIELDS  | ACTIONS                                                                                                           |
|------|-----------------------|------------------------------------------------------------------------------------------------------------------|
| 1 | Prefix (Required) | Add a prefix name to uniquely identify tables/files when Qualytics writes metadata from the source datastore to your enrichment datastore. |
| 2 | Caret Down Button | Click the caret down to select either **Use Enrichment Datastore** or **Add Enrichment Datastore**.               |
| 3 | Enrichment Datastore | Select an enrichment datastore from the dropdown list.                                                           |

### Option I: Create an Enrichment Datastore with a new Connection

If the toggles **Add new connection** is turned on, then this will prompt you to add and configure the enrichment datastore from scratch without using an existing enrichment datastore and its connection details.

**Step 1**: Click on the caret button and select Add Enrichment Datastore.

![carret-button](../assets/datastores/oracle/add-enrichments-light.png#only-light)
![carret-button](../assets/datastores/oracle/add-enrichments-dark.png#only-dark)

A modal window **Link Enrichment Datastore** will appear. Enter the following details to create an enrichment datastore with a new connection.

![modal-window](../assets/datastores/oracle/add-enrichment-details-light.png#only-light)
![modal-window](../assets/datastores/oracle/add-enrichment-details-dark.png#only-dark)

| REF.              | FIELDS       | ACTIONS                                    |
|-------------------|--------------|--------------------------------------------|
| 1.                | Prefix       | Add a prefix name to uniquely identify tables/files when Qualytics writes metadata from the source datastore to your enrichment datastore. |
| 2.                | Name   | Give a name for the enrichment datastore.|
| 3.                |Toggle Button for add new connection | Toggle ON to create a new enrichment from scratch or toggle OFF to reuse credentials from an existing connection. |
| 4.                |Connector | Select a datastore connector from the dropdown list.|

**Step 2:** Add connection details for your selected **enrichment datastore** connector.

![select-enrichment](../assets/datastores/oracle/select-enrichment-light.png#only-light)
![select-enrichment](../assets/datastores/oracle/select-enrichment-dark.png#only-dark)

!!! note
    Qualytics does not support Oracle as an enrichment datastore. Instead, you can select a different enrichment datastore for this purpose. For demonstration purposes, we are using Microsoft SQL Server as the enrichment datastore. You can use any other JDBC or DFS datastore of your choice for the enrichment datastore configuration.

**Step 3:** Click on the **Test Connection** button to verify the selected enrichment datastore connection. If the connection is verified, a flash message will indicate that the connection with the datastore* has been successfully verified.

![test-datastore](../assets/datastores/oracle/test-datastore-light.png#only-light)
![test-datastore](../assets/datastores/oracle/test-datastore-dark.png#only-dark)

**Step 4:** Click on the **Finish** button to complete the configuration process.

![finish-datastore](../assets/datastores/oracle/finish-datastore-light.png#only-light)
![finish-datastore](../assets/datastores/oracle/finish-datastore-dark.png#only-dark)

When the configuration process is finished, a modal will display a **success  message** indicating that **your datastore has been successfully added**.

![sucess-datastore](../assets/datastores/oracle/success-datastore-light.png#only-light)
![sucess-datastore](../assets/datastores/oracle/success-datastore-dark.png#only-dark)

**Step 5:** Close the Success dialogue and the page will automatically redirect you to the **Source Datastore Details** page where you can perform data operations on your configured **source datastore**.

![new-datastore](../assets/datastores/oracle/new-datastore-light.png#only-light)
![new-datastore](../assets/datastores/oracle/new-datastore-dark.png#only-dark)

### Option II: Use an Existing Connection

If the **Use enrichment datastore** option is selected from the caret button, you will be prompted to configure the datastore using existing connection details.

**Step 1**: Click on the caret button and select **Use Enrichment Datastore**.

![use-enrichment-datastore](../assets/datastores/oracle/use-enrichment-light.png#only-light)
![use-enrichment-datastore](../assets/datastores/oracle/use-enrichment-dark.png#only-dark)

**Step 2**: A modal window **Link Enrichment Datastore** will appear. Add a prefix name and select an existing enrichment datastore from the dropdown list.

!!! note
    Qualytics does not support Oracle as an enrichment datastore. Instead, you can select a different enrichment datastore for this purpose. For demonstration purposes, we are using  Microsoft SQL Server as the enrichment datastore. You can use any other JDBC or DFS datastore of your choice for the enrichment datastore configuration.

![use-enrichment-datastore](../assets/datastores/oracle/use-enrichment-datastore-light.png#only-light)
![use-enrichment-datastore](../assets/datastores/oracle/use-enrichment-datastore-dark.png#only-dark)

| REF. | FIELDS | ACTIONS  |
|------|--------------|------|
| 1️. | Prefix  | Add a prefix name to uniquely identify tables/files when Qualytics writes metadata from the source datastore to your enrichment datastore. |
| 2.  | Enrichment Datastore | Select an enrichment datastore from the dropdown list.  |

**Step 3:** After selecting an existing **enrichment datastore** connection, you will view the following details related to the selected enrichment:

-   **Teams:** The team associated with managing the enrichment datastore is based on the role of public or private. For example, Marked as **Public** means that this datastore is accessible to all the users.
-   **Host:** This is the server address where the **Oracle** instance is hosted. It is the endpoint used to connect to the Oracle environment.
-   **Database:** Refers to the specific database within the **Oracle** environment where the data is stored.
-   **Schema:** The schema used in the enrichment datastore. The schema is a logical grouping of database objects(tables, views, etc.).Each schema belongs to a single database.

![select-enrichment-datastore](../assets/datastores/oracle/select-enrichment-datastore-light.png#only-light)
![select-enrichmentdatastore](../assets/datastores/oracle/select-enrichment-datastore-dark.png#only-dark)

**Step 4:** Click on the **Finish** button to complete the configuration process for the existing **enrichment datastore**.

![click-finish-datastore](../assets/datastores/oracle/click-finish-datastore-light.png#only-light)
![click-finish-datastore](../assets/datastores/oracle/click-finish-datastore-dark.png#only-dark)

When the configuration process is finished, a modal will display a **success message** indicating that **your data has been successfully added**.

![sucess-datastore](../assets/datastores/oracle/success-datastore-light.png#only-light)
![sucess-datastore](../assets/datastores/oracle/success-datastore-dark.png#only-dark)

Close the success message and you will be automatically redirected to the **Source Datastore Details** page where you can perform data operations on your configured **source datastore**.

![new-datastore](../assets/datastores/oracle/new-datastore-light.png#only-light)
![new-datastore](../assets/datastores/oracle/new-datastore-dark.png#only-dark)

## API Payload Examples

### Creating  Source a Datastore

This section provides a sample payload for creating a Oracle datastore. Replace the placeholder values with actual data relevant to your setup.

**Endpoint (Post)**: ```/api/datastores (post)```

=== "Creating a source datastore with a new connection"
    ```json
    {
        "name": "your_datastore_name",
        "teams": ["Public"],
        "database": "oracle_database",
        "schema": "oracle_schema",
        "enrich_only": false,
        "trigger_catalog": true,
        "connection": {
            "name": "your_connection_name",
            "type": "oracle",
            "host": "oracle_host",
            "port": "oracle_port",
            "username": "oracle_username",
            "password": "oracle_password",
            "parameters": {
                "sid": "orcl"
            }
        }
    }
    ```  
=== "Creating a datastore with an existing connection"
    ```json
    {
        "name": "your_datastore_name",
        "teams": ["Public"],
        "database": "oracle_database",
        "schema": "oracle_schema",
        "enrich_only": false,
        "trigger_catalog": true,
        "connection_id": "connection-id"
    }
    ```

### Link an Enrichment Datastore to a Source Datastore

**Endpoint Details:** ```/api/datastores/{datastore-id}/enrichment/{enrichment-id} (patch)```