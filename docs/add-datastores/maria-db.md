# MariaDB

Adding and configuring a MariaDB connection within Qualytics empowers the platform to build a symbolic link with your schema to perform operations like data discovery, visualization, reporting, cataloging, profiling, scanning, anomaly surveillance, and more.

This documentation provides a step-by-step guide on how to add MariaDB as both a source and enrichment datastore in Qualytics. It covers the entire process, from initial connection setup to testing and finalizing the configuration.

By following these instructions, enterprises can ensure their MariaDB environment is properly connected with Qualytics, unlocking the platform's potential to help you proactively manage your full data quality lifecycle.

Let’s get started 🚀

## Add a Source Datastore

A source datastore is a storage location used to connect to and access data from external sources. MariaDB is an example of a source datastore, specifically a type of JDBC datastore that supports connectivity through the JDBC API. Configuring the JDBC datastore enables the Qualytics platform to access and perform operations on the data, thereby generating valuable insights.

**Step 1:** Log in to your Qualytics account and click on the **Add Source Datastore** button located at the top-right corner of the interface.

![source](../assets/datastores/maria-db/datastore-light.png#only-light)
![source](../assets/datastores/maria-db/datastore-dark.png#only-dark)

**Step 2:** A modal window- **Add Datastore** will appear, providing you with the options to connect a datastore.

![source](../assets/datastores/maria-db/add-light.png#only-light)
![source](../assets/datastores/maria-db/add-dark.png#only-dark)

| REF. | FIELDS | ACTIONS |
| :---- | :---- | :---- |
| 1. | Name (Required) | Specify the datastore name (e.g., This name will appear on the datastore cards) |
| 2. | Toggle Button | Toggle ON to create a new source datastore from scratch, or toggle OFF to reuse credentials from an existing connection. |
| 3. | Connector (Required) | Select **MariaDB** from the dropdown list. |

### Option I: Create a Source Datastore with a new Connection

If the toggle for **Add New connection** is turned on, then this will prompt you to add and configure the source datastore from scratch without using existing connection details.

**Step 1:** Select the **MariaDB** connector from the dropdown list and add connection details such as Secrets Management, host, port, user, password, SSL connection, database, and schema.

![connector](../assets/datastores/maria-db/connector-light.png#only-light)
![connector](../assets/datastores/maria-db/connector-dark.png#only-dark)

**Secrets Management**: This is an optional connection property that allows you to securely store and manage credentials by integrating with HashiCorp Vault and other secret management systems. Toggle it **ON** to enable Vault integration for managing secrets.

!!! note 
    After configuring HashiCorp Vault integration, you can use ${key} in any Connection property to reference a key from the configured Vault secret. Each time the Connection is initiated, the corresponding secret value will be retrieved dynamically. 

![secret](../assets/datastores/maria-db/secret-light.png#only-light)
![secret](../assets/datastores/maria-db/secret-dark.png#only-dark)

| REF | FIELDS | ACTIONS |
| :---- | :---- | :---- |
| 1. | Login URL | Enter the URL used to authenticate with HashiCorp Vault. |
| 2. | Credentials Payload | Input a valid JSON containing credentials for Vault authentication. |
| 3. | Token JSONPath | Specify the JSONPath to retrieve the client authentication token from the response (e.g., $.auth.client\_token). |
| 4. | Secret URL | Enter the URL where the secret is stored in Vault. |
| 5. | Token Header Name | Set the header name used for the authentication token (e.g., X-Vault-Token). |
| 6. | Data JSONPath  | Specify the JSONPath to retrieve the secret data (e.g., $.data). |

**Step 2:** The configuration form will expand, requesting credential details before establishing the connection.

![form](../assets/datastores/maria-db/form-light.png#only-light)
![form](../assets/datastores/maria-db/form-dark.png#only-dark)

| REF. | FIELDS |     ACTIONS |
| :---- | :---- | :---- |
| 1. | Host | Get **Hostname** from your MariaDB account and add it to this field. |
| 2. | Port | Specify the **Port** number. |
| 3. | User | Enter the **User ID** to connect. |
| 4. | Password | Enter the **password** to connect to the database. |
| 5. | Database | Specify the database name. |
| 6. | Teams | Select one or more teams from the dropdown to associate wit this source datastore. |
| 7. | Initial Cataloging | Tick the checkbox to automatically perform catalog operation on the configured source to gather data structures and corresponding metadata. |

**Step 3:** After adding the source datastore details, click on the **Test Connection** button to check and verify its connection.

![test](../assets/datastores/maria-db/test-light.png#only-light)
![test](../assets/datastores/maria-db/test-dark.png#only-dark)

If the credentials and provided details are verified, a success message will be displayed indicating that the connection has been verified.

### Option II: Use an Existing Connection

If the toggle for **Add New connection** is turned off, then this will prompt you to configure the source datastore using the existing connection details.

**Step 1:** Select a **connection** to reuse existing credentials.

![connections](../assets/datastores/maria-db/connections-light.png#only-light)
![connections](../assets/datastores/maria-db/connections-dark.png#only-dark)

!!! note 
    If you are using existing credentials, you can only edit the details such as Database, Schema, Teams, and Initiate Cataloging. 

**Step 2:** Click on the **Test Connection** button to verify the existing connection details. If connection details are verified, a success message will be displayed.

![tests](../assets/datastores/maria-db/tests-light.png#only-light)
![tests](../assets/datastores/maria-db/tests-dark.png#only-dark)

!!! note 
    Clicking on the Finish button will create the source datastore and bypass the enrichment datastore configuration step. 

!!! tip 
    It is recommended to click on the Next button, which will take you to the enrichment datastore configuration page. 

## Add Enrichment Datastore

Once you have successfully tested and verified your source datastore connection, you have the option to add the enrichment datastore (recommended). This datastore is used to store the analyzed results, including any anomalies and additional metadata in tables. This setup provides full visibility into your data quality, helping you manage and improve it effectively.

**Step 1:** Whether you have added a source datastore by creating a new datastore connection or using an existing connection, click on the **Next** button to start adding the **Enrichment Datastore**.

![next](../assets/datastores/maria-db/next-light.png#only-light)
![next](../assets/datastores/maria-db/next-dark.png#only-dark)

**Step 2:** A modal window- **Link Enrichment Datastore** will appear, providing you with the options to configure an **enrichment datastore**.

![modal](../assets/datastores/maria-db/modal-light.png#only-light)
![modal](../assets/datastores/maria-db/modal-dark.png#only-dark)

| REF. | FIELDS | ACTIONS |
| :---- | :---- | :---- |
| 1. | Prefix (Required) | Add a prefix name to uniquely identify tables/files when Qualytics writes metadata from the source datastore to your enrichment datastore. |
| 2. | Caret Down Button | Click the caret down to select either **Use Enrichment Datastore** or **Add Enrichment Datastore**. |
| 3. | Enrichment Datastore | Select an enrichment datastore from the dropdown list. |

### Option I: Create an Enrichment Datastore with a new Connection

If the toggles **Add new connection** is turned on, then this will prompt you to add and configure the enrichment datastore from scratch without using an existing enrichment datastore and its connection details.

**Step 1**: Click on the caret button and select Add Enrichment Datastore.

![caret](../assets/datastores/maria-db/caret-light.png#only-light)
![caret](../assets/datastores/maria-db/caret-dark.png#only-dark)

A modal window **Link Enrichment Datastore** will appear. Enter the following details to create an enrichment datastore with a new connection.

![windoww](../assets/datastores/maria-db/windoww-light.png#only-light)
![windoww](../assets/datastores/maria-db/windoww-dark.png#only-dark)

| REF. |          FIELDS | ACTIONS |
| :---- | :---- | :---- |
| 1. | Prefix | Add a prefix name to uniquely identify tables/files when Qualytics writes metadata from the source datastore to your enrichment datastore. |
| 2. | Name | Give a name for the enrichment datastore. |
| 3. | Toggle Button For Add New Connection | Toggle ON to create a new enrichment from scratch or toggle OFF to reuse credentials from an existing connection. |
| 4. | Connector | Select a datastore connector from the dropdown list. |

**Step 2:** Add connection details for your selected **enrichment datastore** connector.

![details](../assets/datastores/maria-db/details-light.png#only-light)
![details](../assets/datastores/maria-db/details-dark.png#only-dark)

**Step 3:** Click on the **Test Connection** button to verify the selected enrichment datastore connection. If the connection is verified, a flash message will indicate that the connection with the datastore has been successfully verified.

![testss](../assets/datastores/maria-db/testss-light.png#only-light)
![testss](../assets/datastores/maria-db/testss-dark.png#only-dark)

**Step 4:** Click on the **“Finish”** button to complete the configuration process.

![finish](../assets/datastores/maria-db/finish-light.png#only-light)
![finish](../assets/datastores/maria-db/finish-dark.png#only-dark)

When the configuration process is finished, a modal will display a **success message** indicating that **your datastore has been successfully added**.

![msg](../assets/datastores/maria-db/msg-light.png#only-light)
![msg](../assets/datastores/maria-db/msg-dark.png#only-dark)

**Step 5:** Close the Success dialogue and the page will automatically redirect you to the **Source Datastore Details** page where you can perform data operations on your configured source datastore.

![operations](../assets/datastores/maria-db/operatons-light.png#only-light)
![operations](../assets/datastores/maria-db/operatons-dark.png#only-dark)

### Option II: Use an Existing Connection

If the **Use enrichment datastore** option is selected from the caret button, you will be prompted to configure the datastore using existing connection details.

**Step 1**: Click on the caret button and select **Use Enrichment Datastore**.

![carett](../assets/datastores/maria-db/carett-light.png#only-light)
![carett](../assets/datastores/maria-db/carett-dark.png#only-dark)

**Step 2:** A modal window **Link Enrichment Datastore** will appear. Add a prefix name and select an existing enrichment datastore from the dropdown list.

![windowww](../assets/datastores/maria-db/windowww-light.png#only-light)
![windowww](../assets/datastores/maria-db/windowww-dark.png#only-dark)

| REF. | FIELDS | ACTIONS |
| :---- | :---- | :---- |
| 1. | Prefix | Add a prefix name to uniquely identify tables/files when Qualytics writes metadata from the source datastore to your enrichment. |
| 2. | Enrichment Datastore | Select an enrichment datastore from the dropdown list. |

**Step 3:** After selecting an existing **enrichment datastore** connection, you will view the following details related to the selected enrichment:

* **Teams:** The team associated with managing the enrichment datastore is based on the role of public or private. Example- Marked as **Public** means that this datastore is accessible to all the users.  
* **Host:** This is the server address where the **TimescaleDB** instance is hosted. It is the endpoint used to connect to the PostgreSQL environment.  
* **Database:** Refers to the specific database within the TimescaleDB environment where the data is stored.  
* **Schema:** The schema used in the enrichment datastore. The schema is a logical grouping of database objects (tables, views, etc.). Each schema belongs to a single database.

![enrichment](../assets/datastores/maria-db/enrichmnet-light.png#only-light)
![enrichment](../assets/datastores/maria-db/enrichmnet-dark.png#only-dark)

**Step 4:** Click on the **Finish** button to complete the configuration process for the existing **enrichment datastore**.

![finishh](../assets/datastores/maria-db/finishh-light.png#only-light)
![finishh](../assets/datastores/maria-db/finishh-dark.png#only-dark)

When the configuration process is finished, a modal window will display and a **success flash message** stating that **your data has been successfully added**.

![msg](../assets/datastores/maria-db/msg-light.png#only-light)
![msg](../assets/datastores/maria-db/msg-dark.png#only-dark)

Close the success message and you will be automatically redirected to the **Source Datastore Details** page where you can perform data operations on your configured.

![operation](../assets/datastores/maria-db/operatons-light.png#only-light)
![operation](../assets/datastores/maria-db/operatons-dark.png#only-dark)

## API Payload Examples

### Creating a Datastore

This section provides a sample payload for creating a datastore. Replace the placeholder values with actual data relevant to your setup.

#### Endpoint (Post)

`/api/datastores` _(post)_

=== "Creating a datastore with a new connection"
    ```json
        {
            "name": "your_datastore_name",
            "teams": ["Public"],
            "database": "mariadb_database",
            "enrich_only": false,
            "trigger_catalog": true,
            "connection": {
                "name": "your_connection_name",
                "type": "mariadb",
                "host": "mariadb_host",
                "port": "mariadb_port",
                "username": "mariadb_username",
                "password": "mariadb_password"
            }
        }
    ```
=== "Creating a datastore with an existing connection"
    ```json
        {
            "name": "your_datastore_name",
            "teams": ["Public"],
            "database": "mariadb_database",
            "enrich_only": false,
            "trigger_catalog": true,
            "connection_id": connection-id
        }
    ```

### Creating an Enrichment Datastore

#### Endpoint (Post)

`/api/datastores` _(post)_

This section provides a sample payload for creating an enrichment datastore. Replace the placeholder values with actual data relevant to your setup.

=== "Creating an enrichment datastore with a new connection"
    ```json
        {
            "name": "your_datastore_name",
            "teams": ["Public"],
            "database": "mariadb_database",
            "enrich_only": true,
            "connection": {
                "name": "your_connection_name",
                "type": "mariadb",
                "host": "mariadb_host",
                "port": "mariadb_port",
                "username": "mariadb_username",
                "password": "mariadb_password",
            }
        }
    ```
=== "Creating an enrichment datastore with an existing connection"
    ```json
        {
            "name": "your_datastore_name",
            "teams": ["Public"],
            "database": "mariadb_database",
            "enrich_only": true,
            "connection_id": connection-id
        }
    ``` 

### Linking Datastore to an Enrichment Datastore through API

#### Endpoint (Patch)

`/api/datastores/{datastore-id}/enrichment/{enrichment-id}` _(patch)_
