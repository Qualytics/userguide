# TimescaleDB
Adding and configuring a TimescaleDB connection within Qualytics empowers the platform to build a symbolic link with your schema to perform operations like data discovery, visualization, reporting, cataloging, profiling, scanning, anomaly surveillance, and more.

This documentation provides a step-by-step guide on adding TimescaleDB as a source datastore in Qualytics. It covers the entire process, from initial connection setup to testing and finalizing the configuration.

By following these instructions, enterprises can ensure their TimescaleDB environment is properly connected with Qualytics, unlocking the platform’s potential to help you proactively manage your full data quality lifecycle.

Let’s get started 🚀

## Add the Source Datastore

A source datastore is a storage location used to connect to and access data from external sources. TimescaleDB is an example of such a datastore, specifically a type of JDBC datastore that supports connectivity through the JDBC API. Configuring the TimescaleDB datastore allows the Qualytics platform to access and perform operations on the data, thereby generating valuable insights.

**Step 1:** Log in to your Qualytics account and click on the **Add Source Datastore** button located at the top-right corner of the interface.

![add-datastore](../assets/datastores/timescale-db/add-datastore-light.png#only-light)
![add-datastore](../assets/datastores/timescale-db/add-datastore-dark.png#only-dark)

**Step 2:** A modal window- Add Datastore will appear, providing you with the options to connect a datastore.

![select-a-connector](../assets/datastores/timescale-db/select-a-connector-light.png#only-light)
![select-a-connector](../assets/datastores/timescale-db/select-a-connector-dark.png#only-dark)

| 1. | Name | Specify the name of the datastore (e.g., The specified name will appear on the datastore cards) |
| --- | --------------------- | --------------------- |
| 2. | Toggle Button | Toggle **ON** to create a new source datastore from scratch, or toggle **OFF** to reuse credentials from an existing connection |
| 3. | Connector | Select **TimescaleDB** from the dropdown list. |

### Option I: Create a Datastore with a new Connection

If the toggle for **Add New connection** is turned on, then this will prompt you to add and configure the source datastore from scratch without using existing connection details.

**Step 1 :** Select the **TimescaleDB** connector from the dropdown list and add connection details such as Secret Management, host, port, username, database, and schema.

![add-datastore-credentials](../assets/datastores/timescale-db/add-datastore-credentials-light.png#only-light)
![add-datastore-credentials](../assets/datastores/timescale-db/add-datastore-credentials-dark.png#only-dark)

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

![hashcorp-explain](../assets/datastores/timescale-db/hashcorp-explain-light.png#only-light)
![hashcorp-explain](../assets/datastores/timescale-db/hashcorp-explain-dark.png#only-dark)

**Step 2:** The configuration form will expand, requesting credential details before establishing the connection.

![add-datastore-credentials-explain](../assets/datastores/timescale-db/add-datastore-credentials-explain-light.png#only-light)
![add-datastore-credentials-explain](../assets/datastores/timescale-db/add-datastore-credentials-explain-dark.png#only-dark)

| REF. | FIELDS | ACTIONS |
| ----- | -------- | --------- |
| 1. | Host | Get **Hostname** from your TimescaleDB account and add it to this field. |
| 2. | Port | Specify the **Port** number. |
| 3. | User | Enter the **User ID** to connect. |
| 4. | Password | Enter the **password** to connect to the database. |
| 5. |  Database | Specify the database name. |
| 6. | Schema | Define the schema within the database that should be used.
| 7. | Teams  | Select one or more teams from the dropdown to associate with this source datastore. |
| 8. | Initial cataloging | Tick the checkbox to automatically perform catalog operation on the configured source to gather data structures and corresponding metadata. |                                                                                       

**Step 3 :** After adding the source datastore details, click on the **Test Connection** button to check and verify its connection.

![test-datastore-connection-light](../assets/datastores/timescale-db/test-datastore-connection-light.png#only-light)
![test-datastore-connection](../assets/datastores/timescale-db/test-datastore-connection-dark.png#only-dark)

If the credentials and provided details are verified, a success message will be displayed indicating that the connection has been verified.

### Option II: Use an Existing Connection

If the toggle for **Add New connection** is turned off, then this will prompt you to configure the source datastore using the existing connection details.

**Step 1:** Select a **connection** to reuse existing credentials.

![use-existing-datastore](../assets/datastores/timescale-db/use-existing-datastore-light.png#only-light)
![use-existing-datastore](../assets/datastores/timescale-db/use-existing-datastore-dark.png#only-dark)

**Step 2:** Click on the **Test Connection** button to check and verify the source data connection. If connection details are verified, a success message will be displayed.
![test-connection-for-existing-datastore](../assets/datastores/timescale-db/test-connection-for-existing-datastore-light.png#only-light)
![test-connection-for-existing-datastore](../assets/datastores/timescale-db/test-connection-for-existing-datastore-dark.png#only-dark)

!!! note
    Clicking on the **Finish** button will create the source datastore and bypass the **enrichment datastore** configuration step.

!!! tip
    It is recommended to click on the **Next**  button, which will take you to the **enrichment datastore** configuration page.

## Add Enrichment Datastore

After successfully testing and verifying your source datastore connection, you have the option to add an enrichment datastore (recommended). This datastore is used to store analyzed results, including. This setup provides comprehensive visibility into your data quality, enabling you to manage and improve it effectively.

!!! warning
    Qualytics does not support the TimescaleDB connector as an enrichment datastore, but you can point to a different enrichment datastore.

**Step 1:** Whether you have added a source datastore by creating a new datastore connection or using an existing connection, click on the **Next** button to start adding the **Enrichment Datastore**.

![next-button-for-enrichment](../assets/datastores/timescale-db/next-button-for-enrichment-light.png#only-light)
![next-button-for-enrichment](../assets/datastores/timescale-db/next-button-for-enrichment-dark.png#only-dark)

**Step 2:** A modal window- **Link Enrichment Datastore** will appear, providing you with the options to configure an **“enrichment datastore”**.

![select-enrichment-connector](../assets/datastores/timescale-db/select-enrichment-connector-light.png#only-light)
![select-enrichment-connector](../assets/datastores/timescale-db/select-enrichment-connector-dark.png#only-dark)

| REF. | FIELDS  | ACTIONS                                                                                                           |
|------|-----------------------|------------------------------------------------------------------------------------------------------------------|
| 1 | Prefix (Required) | Add a prefix name to uniquely identify tables/files when Qualytics writes metadata from the source datastore to your enrichment datastore. |
| 2 | Caret Down Button | Click the caret down to select either **Use Enrichment Datastore** or **Add Enrichment Datastore**.               |
| 3 | Enrichment Datastore | Select an enrichment datastore from the dropdown list.                                                           |

### Option I: Create an Enrichment Datastore with a new Connection

If the toggles **Add new connection** is turned on, then this will prompt you to add and configure the enrichment datastore from scratch without using an existing enrichment datastore and its connection details.

**Step 1**: Click on the caret button and select Add Enrichment Datastore.

![caret-button](../assets/datastores/timescale-db/add-enrichments-light.png#only-light)
![caret-button](../assets/datastores/timescale-db/add-enrichments-dark.png#only-dark)

A modal window **Link Enrichment Datastore** will appear. Enter the following details to create an enrichment datastore with a new connection.

![modal-window](../assets/datastores/timescale-db/add-enrichment-details-light.png#only-light)
![modal-window](../assets/datastores/timescale-db/add-enrichment-details-dark.png#only-dark)

| REF.              | FIELDS       | ACTIONS                                    |
|-------------------|--------------|--------------------------------------------|
| 1.                | Prefix       | Add a prefix name to uniquely identify tables/files when Qualytics writes metadata from the source datastore to your enrichment datastore. |
| 2.                | Name   | Give a name for the enrichment datastore.|
| 3.                |Toggle Button for add new connection | Toggle ON to create a new enrichment from scratch or toggle OFF to reuse credentials from an existing connection. |
| 4.                |Connector | Select a datastore connector from the dropdown list.|

**Step 2:** Add connection details for your selected **enrichment datastore** connector.

![enrichment-datastore-explain](../assets/datastores/timescale-db/enrichment-datastore-explain-light.png#only-light)
![enrichment-datastore-explain](../assets/datastores/timescale-db/enrichment-datastore-explain-dark.png#only-dark)

!!! note
    Qualytics does not support TimescaleDB as an enrichment datastore. Instead, you can select a different enrichment datastore for this purpose. For demonstration purposes, we are using Microsoft SQL Server as the enrichment datastore. You can use any other JDBC or DFS datastore of your choice for the enrichment datastore configuration.

**Step 3:** Click on the **Test Connection** button to verify the selected enrichment datastore connection. If the connection is verified, a flash message will indicate that the connection with the datastore has been successfully verified.

![test-connection-for-enrichment-datastore](../assets/datastores/timescale-db/timescale-dbtest-connection-light.png#only-light)
![test-connection-for-enrichment-datastore](../assets/datastores/timescale-db/timescale-dbtest-connection-dark.png#only-dark)

**Step 4:** Click on the **“Finish”** button to complete the configuration process.

![finish-configuration](../assets/datastores/timescale-db/finish-configuration-light.png#only-light)
![finish-configuration](../assets/datastores/timescale-db/finish-configuration-dark.png#only-dark)

When the configuration process is finished, a modal will display a **success message** indicating that **your datastore has been successfully added**.

**Step 5:** Close the Success dialogue and the page will automatically redirect you to the **Source Datastore Details** page where you can perform data operations on your configured source datastore.

![success-message](../assets/datastores/timescale-db/success-message-light.png#only-light)
![success-message](../assets/datastores/timescale-db/success-message-dark.png#only-dark)

### Option II: Use an Existing Connection

If the **Use enrichment datastore** option is selected from the caret button, you will be prompted to configure the datastore using existing connection details.

**Step 1**: Click on the caret button and select **Use Enrichment Datastore**.

![use-enrichment-datastore](../assets/datastores/timescale-db/use-enrichment-light.png#only-light)
![use-enrichment-datastore](../assets/datastores/timescale-db/use-enrichment-dark.png#only-dark)

**Step 2:** A modal window **Link Enrichment Datastore** will appear. Add a prefix name and select an existing enrichment datastore from the dropdown list.

!!! note
    Qualytics does not support Timescale as an enrichment datastore. Instead, you can select a different enrichment datastore for this purpose. For demonstration purposes, we are using Bank Enrichnment as the enrichment datastore. You can use any other JDBC or DFS datastore of your choice for the enrichment datastore configuration.

![select-existing-enrichment-datastore](../assets/datastores/timescale-db/select-enrichment-datastore-light.png#only-light)
![select-existing-enrichment-datastore](../assets/datastores/timescale-db/select-enrichment-datastore-dark.png#only-dark)

| REF. | FIELDS | ACTIONS |
| ------ | -------- | --------- |
| 1. | Prefix | Add a prefix name to uniquely identify tables/files when Qualytics writes metadata from the source datastore to your enrichment. |
 | 2. | Enrichment Datastore | Select an enrichment datastore from the dropdown list. |

**Step 3:** After selecting an existing **enrichment datastore** connection, you will view the following details related to the selected enrichment:

-   **Teams:** The team associated with managing the enrichment datastore is based on the role of public or private. Example- Marked as **Public** means that this datastore is accessible to all the users.
-   **Host:** This is the server address where the **TimescaleDB** instance is hosted. It is the endpoint used to connect to the PostgreSQL environment.
-   **Database:** Refers to the specific database within the TimescaleDB environment where the data is stored.
-   **Schema:** The schema used in the enrichment datastore. The schema is a logical grouping of database objects (tables, views, etc.). Each schema belongs to a single database.

![use-existing-enrichment-datastore](../assets/datastores/timescale-db/select-existing-datastore-light.png#only-light)
![use-existing-enrichment-datastore](../assets/datastores/timescale-db/select-existing-datastore-dark.png#only-dark)

**Step 4:** Click on the **Finish** button to complete the configuration process for the existing **enrichment datastore**.

![use-existing-enrichment-datastore](../assets/datastores/timescale-db/finish-datastore-light.png#only-light)
![use-existing-enrichment-datastore](../assets/datastores/timescale-db/finish-datastore-dark.png#only-dark)

When the configuration process is finished, a modal window will display and a **success flash message** stating that **your data has been successfully added**.

![success-message](../assets/datastores/timescale-db/success-message-light.png#only-light)
![success-message](../assets/datastores/timescale-db/success-message-dark.png#only-dark)

Close the success message and you will be automatically redirected to the **Source Datastore Details** page where you can perform data operations on your configured 

![data-operation-page](../assets/datastores/timescale-db/data-operation-page-light.png#only-light)
![data-operation-page](../assets/datastores/timescale-db/data-operation-page-dark.png#only-dark)

## API Payload Examples

### Creating a Source Datastore

This section provides a sample payload for creating a TimescaleDB datastore. Replace the placeholder values with actual data relevant to your setup.

**Endpoint (Post):** ```/api/datastores (post)```

=== "Creating a source datastore with a new connection"
    ```json
    {
        "name": "your_datastore_name",
        "teams": ["Public"],
        "database": "timescale_database",
        "schema": "timescale_schema",
        "enrich_only": false,
        "trigger_catalog": true,
        "connection": {
            "name": "your_connection_name",
            "type": "timescale",
            "host": "timescale_host",
            "port": "timescale_port",
            "username": "timescale_username",
            "password": "timescale_password"
        }
    }
    ```
=== "Creating a source datastore with an existing connection"
    ```json
    {
        "name": "your_datastore_name",
        "teams": ["Public"],
        "database": "timescale_database",
        "schema": "timescale_schema",
        "enrich_only": false,
        "trigger_catalog": true,
        "connection_id": connection-id,
    }
    ```
### Link an Enrichment Datastore to a Source Datastore

**Endpoint Details:** ```/api/datastores/{datastore-id}/enrichment/{enrichment-id} (patch)```
