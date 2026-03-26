# DB2

Adding and configuring a DB2 connection within Qualytics empowers the platform to build a symbolic link with your schema to perform operations like data discovery, visualization, reporting, syncing, profiling, scanning, anomaly surveillance, and more.  

This documentation provides a step-by-step guide on how to add DB2 as both a source and enrichment datastore in Qualytics. It covers the entire process, from initial connection setup to testing and finalizing the configuration. 

By following these instructions, enterprises can ensure their DB2 environment is properly connected with Qualytics, unlocking the platform's potential to help you proactively manage your full data quality lifecycle. 

Let’s get started 🚀

## DB2 Setup Guide

Qualytics connects to DB2 through the **IBM DB2 JDBC driver**. It queries DB2 system catalogs (`SYSCAT.SCHEMATA`, `SYSCAT.TABLES`) to discover schemas and uses standard JDBC metadata APIs for tables, columns, and primary keys.

### Minimum DB2 Permissions (Source Datastore)

| Permission                                | Purpose                                                                     |
|-------------------------------------------|-----------------------------------------------------------------------------|
| `CONNECT ON DATABASE`                     | Allow the user to connect to the database                                   |
| `USAGE ON SCHEMA <schema_name>`           | Access objects within the target schema                                     |
| `SELECT ON ALL TABLES IN SCHEMA`          | Read data from all tables for profiling and scanning                        |
| `SELECT ON SYSCAT.SCHEMATA`               | Discover available schemas in the database                                  |
| `SELECT ON SYSCAT.TABLES`                 | Discover available tables and filter empty schemas                          |

### Additional Permissions for Enrichment Datastore

When using DB2 as an enrichment datastore, the following additional permissions are required for Qualytics to write metadata tables (e.g., `_qualytics_*`):

| Permission                                | Purpose                                                                     |
|-------------------------------------------|-----------------------------------------------------------------------------|
| `CREATETAB ON DATABASE`                   | Create enrichment tables (`_qualytics_*`)                                   |
| `CREATEIN ON SCHEMA <schema_name>`        | Create new objects within the schema                                        |
| `ALTERIN ON SCHEMA <schema_name>`         | Modify enrichment table schemas during version migrations                   |
| `INSERT ON ALL TABLES IN SCHEMA`          | Write anomaly records, scan results, and check metrics                      |
| `UPDATE ON ALL TABLES IN SCHEMA`          | Update enrichment records during rescans                                    |
| `DELETE ON ALL TABLES IN SCHEMA`          | Remove stale enrichment records                                             |

### Example: Source Datastore User (Read-Only)

Replace `<schema_name>` with your actual value.

```sql
-- Grant connection and schema access
GRANT CONNECT ON DATABASE TO USER qualytics_read;
GRANT USAGE ON SCHEMA <schema_name> TO USER qualytics_read;

-- Grant read access to all tables in the schema
GRANT SELECT ON ALL TABLES IN SCHEMA <schema_name> TO USER qualytics_read;
```

### Example: Enrichment Datastore User (Read-Write)

```sql
-- Grant connection and schema access
GRANT CONNECT ON DATABASE TO USER qualytics_readwrite;
GRANT USAGE ON SCHEMA <schema_name> TO USER qualytics_readwrite;

-- Grant full data manipulation on all tables
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA <schema_name> TO USER qualytics_readwrite;

-- Grant table creation and schema modification
GRANT CREATETAB ON DATABASE TO USER qualytics_readwrite;
GRANT CREATEIN ON SCHEMA <schema_name> TO USER qualytics_readwrite;
GRANT ALTERIN ON SCHEMA <schema_name> TO USER qualytics_readwrite;
```

### Troubleshooting Common Errors

| Error                                          | Likely Cause                                                                 | Fix                                                                                     |
|------------------------------------------------|------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| `SQL30082N: Security processing failed`        | Incorrect username or password                                               | Verify the credentials and ensure the user exists in the DB2 instance                   |
| `SQL1060N: User does not have the CONNECT privilege` | The user lacks `CONNECT` on the database                              | Run `GRANT CONNECT ON DATABASE TO USER <user>`                                          |
| `SQL0551N: User does not have the required authorization` | The user lacks `SELECT` or other required permissions on a table    | Grant the missing permission on the specific table or schema                            |
| `SQL0204N: Name is an undefined name`          | The schema or table does not exist, or the user cannot see it               | Verify the schema name matches exactly (DB2 stores unquoted schema names in uppercase by default) |
| `SQL0552N: User is not authorized to perform the requested command` | The enrichment user lacks `CREATETAB` or `CREATEIN`          | Run `GRANT CREATETAB ON DATABASE TO USER <user>` and `GRANT CREATEIN ON SCHEMA <schema_name> TO USER <user>` |

## Add a Source Datastore

A source datastore is a storage location used to connect to and access data from external sources. DB2 is an example of a source datastore, specifically a type of JDBC datastore that supports connectivity through the JDBC API. Configuring the JDBC datastore enables the Qualytics platform to access and perform operations on the data, thereby generating valuable insights.

**Step 1:** Log in to your Qualytics account and click on the **Add Source Datastore** button located at the top-right corner of the interface. 

![add-datastore](../../assets/source-datastores/add-datastores/db2/add-datastore.png)

**Step 2:** A modal window- **Add Datastore** will appear, providing you with the options to connect a datastore.

![select-a-connector](../../assets/source-datastores/add-datastores/db2/select-a-connector.png)

| REF.         | FIELDS       | ACTIONS                                                                 |
|--------------|--------------|-------------------------------------------------------------------------|
| 1.      | Name (Required)     | Specify the datastore name (e.g., This name will appear on the datastore cards) |
| 2.       | Toggle Button | Toggle ON to create a new source datastore from scratch, or toggle OFF to reuse credentials from an existing connection. |
| 3.      | Connector (Required)   | Select **DB2** from the dropdown list.                                      |

### Option I: Create a Source Datastore with a new Connection

If the toggle for **Add New connection** is turned on, then this will prompt you to add and configure the source datastore from scratch without using existing connection details.

**Step 1:** Select the **DB2** connector from the dropdown list and add connection details such as Secrets Management, host, port, user, password, SSL connection, database, and schema.

![add-datastore-credentials](../../assets/source-datastores/add-datastores/db2/add-datastore-credentials.png)

**Secrets Management**: This is an optional connection property that allows you to securely store and manage credentials by integrating with HashiCorp Vault and other secret management systems. Toggle it **ON** to enable Vault integration for managing secrets.

!!! note 
    After configuring **HashiCorp Vault** integration, you can use ${key} in any connection property to reference a key from the configured Vault secret. Each time the Connection is initiated, the corresponding secret value will be retrieved dynamically.

| REF | FIELDS               | ACTIONS                                                                 |
|-----|----------------------|-------------------------------------------------------------------------|
| 1.  | Login URL            | Enter the URL used to authenticate with HashiCorp Vault.                |
| 2.  | Credentials Payload  | Input a valid JSON containing credentials for Vault authentication.     |
| 3.  | Token JSONPath       | Specify the JSONPath to retrieve the client authentication token from the response (e.g., $.auth.client_token). |
| 4.  | Secret URL           | Enter the URL where the secret is stored in Vault.                      |
| 5.  | Token Header Name    | Set the header name used for the authentication token (e.g., X-Vault-Token). |
| 6.  | Data JSONPath        | Specify the JSONPath to retrieve the secret data (e.g., $.data).        |

![hashcorp-explain](../../assets/source-datastores/add-datastores/db2/hashcorp-explain.png)

**Step 2:** The configuration form will expand, requesting credential details before establishing the connection.

![add-datastore-credentials-explain](../../assets/source-datastores/add-datastores/db2/add-datastore-credentials-explain.png)

| REF.         | FIELDS               | ACTIONS                                                                                     |
|--------------|----------------------|---------------------------------------------------------------------------------------------|
| 1.       | Host (Required)             | Get **Hostname** from your DB2 account and add it to this field.                              |
| 2.       | Port (Required)           | Specify the **Port** number.                                                                   |
| 3.       | User (Required)             | Enter the **User** to connect.                                                              |
| 4.       | Password (Required)         | Enter the **password** to connect to the database.                                             |
| 5.       | SSL Connection    | Enable the SSL connection to ensure secure communication between Qualytics and the selected datastore. |
| 6.       | Database (Required)         | Specify the database name.                                                                   |
| 7.       | Schema (Required)           | Define the schema within the database that should be used.                                    |
| 8.       | Teams (Required)            | Select one or more teams from the dropdown to associate with this source datastore.           |
| 9.       | Initiate Sync | Tick the checkbox to automatically perform sync operation on the configured source datastore to detect new, changed, or removed containers and fields. |

**Step 3:** After adding the source datastore details, click on the **Test Connection** button to check and verify its connection.

![test-datastore-connection](../../assets/source-datastores/add-datastores/db2/test-datastore-connection.png)

If the credentials and provided details are verified, a success message will be displayed indicating that the connection has been verified. 

### Option II: Use an Existing Connection

If the toggle for **Add New connection** is turned off, then this will prompt you to configure the source datastore using the existing connection details.

**Step 1:** Select a **connection** to reuse existing credentials.

![use-existing-datastore](../../assets/source-datastores/add-datastores/db2/use-existing-datastore.png)

!!! note
     If you are using existing credentials, you can only edit the details such as Database, Schema, Teams, and Initiate Sync. 

**Step 2:** Click on the **Test Connection** button to verify the existing connection details. If connection details are verified, a success message will be displayed.

![test-connection-for-existing-datastore](../../assets/source-datastores/add-datastores/db2/test-connection-for-existing-datastore.png)

!!! note
    Clicking on the **Finish** button will create the source datastore and bypass the **enrichment datastore** configuration step.

!!! tip
    It is recommended to click on the **Next** button, which will take you to the **enrichment datastore** configuration page.

## Add Enrichment Datastore

Once you have successfully tested and verified your source datastore connection, you have the option to add the enrichment datastore (recommended). This datastore is used to store the analyzed results, including any anomalies and additional metadata in tables. This setup provides full visibility into your data quality, helping you manage and improve it effectively.

**Step 1:** Whether you have added a source datastore by creating a new datastore connection or using an existing connection, click on the **Next** button to start adding the **Enrichment Datastore**.

![next-button-for-enrichment](../../assets/source-datastores/add-datastores/db2/next-button-for-enrichment.png)

**Step 2:** A modal window- **Link Enrichment Datastore** will appear, providing you with the options to configure an **enrichment datastore**.

![select-enrichment-connector](../../assets/source-datastores/add-datastores/db2/select-enrichment-connector.png)

| REF. | FIELDS  | ACTIONS                                                                                                           |
|------|-----------------------|------------------------------------------------------------------------------------------------------------------|
| 1 | Prefix (Required) | Add a prefix name to uniquely identify tables/files when Qualytics writes metadata from the source datastore to your enrichment datastore. |
| 2 | Caret Down Button | Click the caret down to select either **Use Enrichment Datastore** or **Add Enrichment Datastore**.               |
| 3 | Enrichment Datastore | Select an enrichment datastore from the dropdown list.                                                           |

### Option I: Create an Enrichment Datastore with a new Connection

If the toggle **Add new connection** is turned on, then this will prompt you to add and configure the enrichment datastore from scratch without using an existing enrichment datastore and its connection details.

**Step 1**: Click on the caret button and select **Add Enrichment Datastore**.

![caret-button](../../assets/source-datastores/add-datastores/db2/add-enrichment.png)

A modal window **Link Enrichment Datastore** will appear. Enter the following details to create an enrichment datastore with a new connection.

![modal-window](../../assets/source-datastores/add-datastores/db2/add-enrichment-details.png)

| REF.              | FIELDS       | ACTIONS                                    |
|-------------------|--------------|--------------------------------------------|
| 1.                | Prefix       | Add a prefix name to uniquely identify tables/files when Qualytics writes metadata from the source datastore to your enrichment datastore. |
| 2.                | Name   | Give a name for the enrichment datastore.|
| 3.                |Toggle Button for add new connection | Toggle ON to create a new enrichment from scratch or toggle OFF to reuse credentials from an existing connection. |
| 4.                |Connector | Select a datastore connector from the dropdown list.|

**Step 2:** Add connection details for your selected **enrichment datastore** connector.

![modal-window](../../assets/source-datastores/add-datastores/db2/add-enrichment-detail.png)

**Secrets Management**: This is an optional connection property that allows you to securely store and manage credentials by integrating with HashiCorp Vault and other secret management systems. Toggle it **ON** to enable Vault integration for managing secrets.

!!! note
    Once the **HashiCorp Vault** is set up, use the ${key} format in Connection form to reference a Vault secret.

| REF | FIELDS               | ACTIONS                                                                 |
|-----|----------------------|-------------------------------------------------------------------------|
| 1.  | Login URL            | Enter the URL used to authenticate with HashiCorp Vault.                |
| 2.  | Credentials Payload  | Input a valid JSON containing credentials for Vault authentication.     |
| 3.  | Token JSONPath       | Specify the JSONPath to retrieve the client authentication token from the response (e.g., $.auth.client_token). |
| 4.  | Secret URL           | Enter the URL where the secret is stored in Vault.                      |
| 5.  | Token Header Name    | Set the header name used for the authentication token (e.g., X-Vault-Token). |
| 6.  | Data JSONPath        | Specify the JSONPath to retrieve the secret data (e.g., $.data).        |

![secret-management](../../assets/source-datastores/add-datastores/db2/secret-management.png)

**Step 3:** The configuration form, requesting credential details after selecting the **enrichment datastore** connector.

![enrichment-datastore-explain](../../assets/source-datastores/add-datastores/db2/enrichment-datastore-explain.png)

| REF.         | FIELDS         | ACTIONS                                                                                     |
|--------------|----------------|--------------------------------------------------------------------------------------------|
| 1.       | Host        | Get **Hostname** from your DB2 account and add it to this field.                              |
| 2.       | Port        | Specify the **Port** number.                                                                   |
| 3.       | User         | Enter the **User** to connect.                                                              |
| 4.       | Password   | Enter the **password** to connect to the database.                                             |
| 5.       | SSL Connection | Enable the SSL connection to ensure secure communication between Qualytics and the selected datastore. |
| 6.       | Database    | Specify the database name.                                                                   |
| 7.      | Schema       | Define the schema within the database that should be used.                                    |
| 8.       | Teams        | Select one or more teams from the dropdown to associate with this datastore.                 |


**Step 4:**  Click on the **Test Connection** button to verify the selected enrichment datastore connection. If the connection is verified, a flash message will indicate that the connection with the enrichment datastore has been successfully verified. 

![test-connection-for-enrichment-datastore](../../assets/source-datastores/add-datastores/db2/test-connection-for-enrichment-datastore.png)

**Step 5:** Click on the **Finish** button to complete the configuration process. 

![finish-configuration](../../assets/source-datastores/add-datastores/db2/finish-configuration.png)

When the configuration process is finished, a modal will display a success message indicating that your datastore has been successfully added.

**Step 6:** Close the Success dialog and the page will automatically redirect you to the **Source Datastore Details** page where you can perform data operations on your configured **source datastore**.

![data-operation-page](../../assets/source-datastores/add-datastores/db2/data-operation-page.png)

### Option II: Use an Existing Connection

If the **Use enrichment datastore** option is selected from the caret button, you will be prompted to configure the datastore using existing connection details. 

**Step 1**: Click on the caret button and select **Use Enrichment Datastore**.

![use-enrichment-datastore](../../assets/source-datastores/add-datastores/db2/use-enrichment.png)

**Step 2**: A modal window **Link Enrichment Datastore** will appear. Add a prefix name and select an existing enrichment datastore from the dropdown list.

![select-existing-enrichment-datastore](../../assets/source-datastores/add-datastores/db2/select-existing-enrichment-datastore.png)

| REF. | FIELDS                             | ACTIONS                                                                                                      |
|------|------------------------------------|--------------------------------------------------------------------------------------------------------------|
| 1  | Prefix (Required)                            | Add a prefix name to uniquely identify tables/files when Qualytics writes metadata from the source datastore to your enrichment datastore. |
| 2   | Enrichment Datastore               | Select an enrichment datastore from the dropdown list.                                                         |

**Step 3:** After selecting an existing **enrichment datastore** connection, you will view the following details related to the selected enrichment: 

- **Teams:** The team associated with managing the enrichment datastore is based on the role of public or private. Example- Marked as **Public** means that this datastore is accessible to all the users. 

 - **Host:** This is the server address where the DB2 instance is hosted. It is the endpoint used to connect to the DB2 environment. 

 - **Database:** Refers to the specific database within the DB2 environment where the data is stored.

 - **Schema:** The schema used in the enrichment datastore. The schema is a logical grouping of database objects (tables, views, etc.). Each schema belongs to a single database.

![use-existing-enrichment-datastore](../../assets/source-datastores/add-datastores/db2/use-existing-enrichment-datastore.png)

**Step 4:** Click on the **Finish** button to complete the configuration process for the existing **enrichment datastore**.

![finish-configuration-for-existing-enrichment-datastore](../../assets/source-datastores/add-datastores/db2/finish-configuration-for-existing-enrichment-datastore.png)

When the configuration process is finished, a modal will display a success message indicating that your data has been successfully added.

Close the success message and you will be automatically redirected to the **Source Datastore Details** page where you can perform data operations on your configured **source datastore**.

![data-operation-page](../../assets/source-datastores/add-datastores/db2/data-operation-page.png)

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
        "connection_id": connection_id
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
        "connection_id": connection_id
    }
    ``` 

### Link an Enrichment Datastore to a Source Datastore
Use the provided endpoint to link an enrichment datastore to a source datastore: 

**Endpoint Details:** ```/api/datastores/{datastore-id}/enrichment/{enrichment-id} (patch)```
