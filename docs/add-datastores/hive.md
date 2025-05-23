# Hive

Adding and configuring a Hive connection within Qualytics empowers the platform to build a symbolic link with your schema to perform operations like data discovery, visualization, reporting, cataloging, profiling, scanning, anomaly surveillance, and more.

This documentation provides a step-by-step guide on how to add Hive as both a source and enrichment datastore in Qualytics. It covers the entire process, from initial connection setup to testing and finalizing the configuration.

By following these instructions, enterprises can ensure their Hive environment is properly connected with Qualytics, unlocking the platform's potential to help you proactively manage your full data quality lifecycle.

Let’s get started 🚀

## Add a Source Datastore

A source datastore is a storage location used to connect to and access data from external sources. Hive is an example of a source datastore, specifically a type of JDBC datastore that supports connectivity through the JDBC API. Configuring the JDBC datastore enables the Qualytics platform to access and perform operations on the data, thereby generating valuable insights.

**Step 1:** Log in to your Qualytics account and click on the **Add Source Datastore** button located at the top-right corner of the interface.

![source](../assets/datastores/hive/source-datastore-light.png#only-light)
![source](../assets/datastores/hive/source-datastore-dark.png#only-dark)

**Step 2:** A modal window- **Add Datastore** will appear, providing you with the options to connect a datastore.

![window](../assets/datastores/hive/window-datastore-light.png#only-light)
![window](../assets/datastores/hive/window-datastore-dark.png#only-dark)

| REF. | FIELDS | ACTIONS                               |
| :---- | :---- | :---- |
| 1. | Name (Required) | Specify the datastore name (e.g., This name will appear on the datastore cards) |
| 2. | Toggle Button | Toggle ON to create a new source datastore from scratch, or toggle OFF to reuse credentials from an existing connection. |
| 3. | Connector (Required) | Select **Hive** from the dropdown list. |

### Option I: Create a Source Datastore with a new Connection

If the toggle for **Add New connection** is turned on, then this will prompt you to add and configure the source datastore from scratch without using existing connection details.

**Step 1:** Select the **Hive** connector from the dropdown list and add connection details such as Secret Management, host, port, username, password, and database.

![connector](../assets/datastores/hive/connector-datastore-light.png#only-light)
![connector](../assets/datastores/hive/connector-datastore-dark.png#only-dark)

**Secrets Management**: This is an optional connection property that allows you to securely store and manage credentials by integrating with HashiCorp Vault and other secret management systems. Toggle it **ON** to enable Vault integration for managing secrets.

!!! note 
    After configuring HashiCorp Vault integration, you can use ${key} in any Connection property to reference a key from the configured Vault secret. Each time the Connection is initiated, the corresponding secret value will be retrieved dynamically. 

| REF | FIELDS | ACTIONS |
| :---- | :---- | :---- |
| 1. | Login URL | Enter the URL used to authenticate with HashiCorp Vault. |
| 2. | Credentials Payload | Input a valid JSON containing credentials for Vault authentication. |
| 3. | Token JSONPath | Specify the JSONPath to retrieve the client authentication token from the response (e.g., $.auth.client\_token). |
| 4. | Secret URL | Enter the URL where the secret is stored in Vault. |
| 5. | Token Header Name | Set the header name used for the authentication token (e.g., X-Vault-Token). |
| 6. | Data JSONPath | Specify the JSONPath to retrieve the secret data (e.g., $.data). |

![Secrets](../assets/datastores/hive/secret-datastore-light.png#only-light)
![Secrets](../assets/datastores/hive/secret-datastore-dark.png#only-dark)

**Step 2**: The configuration form will expand, requesting credential details before establishing the connection.

| REF. |             FIELDS |                 ACTIONS |
| :---- | :---- | :---- |
| 1. | Host(Required) | Get **Hostname** from your account and Hive add it to this field. |
| 2. | Port(Required) | Specify the **Port** number. |
| 3. | User(Required) | Enter the **User ID** to connect. |
| 4. | Password(Required) | Enter the **password** to connect to the database. |
| 5. | Scheme(Required) | Define the schema within the database that should be used. |
| 6. | Teams(Required) | Select one or more teams from the dropdown to associate with this source datastore. |
| 7. | Initial Cataloging(Optional) | Tick the checkbox to automatically perform catalog operation on the configured source datastore to gather data structures and corresponding metadata. |

![form](../assets/datastores/hive/form-datastore-light.png#only-light)
![form](../assets/datastores/hive/form-datastore-dark.png#only-dark)

**Step 3:** After adding the source datastore details, click on the **Test Connection** button to check and verify its connection.

![test](../assets/datastores/hive/test-datastore-light.png#only-light)
![test](../assets/datastores/hive/test-datastore-dark.png#only-dark)

If the credentials and provided details are verified, a success message will be displayed indicating that the connection has been verified.

### Option II: Use an Existing Connection

If the toggle for **Add new connection** is turned off, then this will prompt you to configure the source datastore using the existing connection details.

**Step 1:** Select a **connection** to reuse existing credentials.

![connections](../assets/datastores/hive/connection-datastore-light.png#only-light)
![connections](../assets/datastores/hive/connection-datastore-dark.png#only-dark)

!!! note 
    If you are using existing credentials, you can only edit the details such as Database, Schema, Teams, and Initiate Cataloging. 

**Step 2:** Click on the **Test Connection** button to verify the existing connection details. If connection details are verified, a success message will be displayed.

![test](../assets/datastores/hive/test-datastore-light.png#only-light)
![test](../assets/datastores/hive/test-datastore-dark.png#only-dark)

!!! note 
    Clicking on the Finish button will create the source datastore and bypass the enrichment datastore configuration step. 

!!! tip 
    It is recommended to click on the Next button, which will take you to the enrichment datastore configuration page. 

## Add Enrichment Datastore

Once you have successfully tested and verified your source datastore connection, you have the option to add the enrichment datastore (recommended). The enrichment datastore is used to store the analyzed results, including any anomalies and additional metadata in tables. This setup provides full visibility into your data quality, helping you manage and improve it effectively.

!!! warning 
    Qualytics does not support the Hive connector as an enrichment datastore, but you can point to a different enrichment datastore. 

**Step 1:** Whether you have added a source datastore by creating a new datastore connection or using an existing connection, click on the **Next** button to start adding the **Enrichment Datastore**.

![next](../assets/datastores/hive/next-datastore-light.png#only-light)
![next](../assets/datastores/hive/next-datastore-dark.png#only-dark)

**Step 2:** A modal window- **Link Enrichment Datastore** will appear, providing you with the options to configure to add an **enrichment datastore**.

![link](../assets/datastores/hive/link-datastore-light.png#only-light)
![link](../assets/datastores/hive/link-datastore-dark.png#only-dark)

| REF. | FIELDS | ACTIONS |
| :---- | :---- | :---- |
| **1.** | Prefix (Required) | Add a prefix name to uniquely identify tables/files when Qualytics writes metadata from the source datastore to your enrichment datastore. |
| **2.** | Caret Down Button | Click the caret down to select either **Use Enrichment Datastore** or **Add Enrichment Datastore**. |
| **3.** | Enrichment Datastore | Select an enrichment datastore from the dropdown list. |

### Option I: Create an Enrichment Datastore with a new Connection

If the toggles **Add new connection** is turned on, then this will prompt you to add and configure the enrichment datastore from scratch without using an existing enrichment datastore and its connection details.

**Step 1**: Click on the caret button and select Add Enrichment Datastore.

![caret](../assets/datastores/hive/caret-datastore-light.png#only-light)
![caret](../assets/datastores/hive/caret-datastore-dark.png#only-dark)

A modal window **Link Enrichment Datastore** will appear. Enter the following details to create an enrichment datastore with a new connection.

![enrichment](../assets/datastores/hive/enrichment-datastore-light.png#only-light)
![enrichment](../assets/datastores/hive/enrichment-datastore-dark.png#only-dark)

| REF. | FIELDS | ACTIONS |
| :---- | :---- | :---- |
| 1. | Prefix | Add a prefix name to uniquely identify tables/files when Qualytics writes metadata from the source datastore to your enrichment datastore. |
| 2. | Name | Give a name for the enrichment datastore. |
| 3. | Toggle Button for add new connection | Toggle ON to create a new enrichment from scratch or toggle OFF to reuse credentials from an existing connection. |
| 4. | Connector | Select a datastore connector from the dropdown list. |

**Step 2:** Add connection details for your selected **enrichment datastore** connector.

!!! note 
    Qualytics does not support Hive as an enrichment datastore. Instead, you can select a different enrichment datastore for this purpose. For demonstration purposes, we are using BigQuery as the enrichment datastore. You can use any other JDBC or DFS datastore of your choice for the enrichment datastore configuration. 

![datastore](../assets/datastores/hive/datastore-light.png#only-light)
![datastore](../assets/datastores/hive/datastore-dark.png#only-dark)

**Step 3:** Click on the **Test Connection** button to verify the selected enrichment datastore connection. If the connection is verified, a flash message will indicate that the connection with the datastore has been successfully verified.

![test](../assets/datastores/hive/create-test-light.png#only-light)
![test](../assets/datastores/hive/create-test-dark.png#only-dark)

**Step 4:** Click on the **Finish** button to complete the configuration process.

![test](../assets/datastores/hive/tests-datastore-light.png#only-light)
![test](../assets/datastores/hive/tests-datastore-dark.png#only-dark)

When the configuration process is finished, a modal will display a **success message** indicating that **your datastore has been successfully added**.

![success](../assets/datastores/hive/success-datastore-light.png#only-light)
![success](../assets/datastores/hive/success-datastore-dark.png#only-dark)

**Step 5:** Close the Success dialog and the page will automatically redirect you to the **Source Datastore Details** page where you can perform data operations on your configured **source datastore**.

![dialog](../assets/datastores/hive/operation-datastore-light.png#only-light)
![dialog](../assets/datastores/hive/operation-datastore-dark.png#only-dark)

### Option II: Use an Existing Connection

If the **Use enrichment datastore** option is selected from the caret button, you will be prompted to configure the datastore using existing connection details.

**Step 1**: Click on the caret button and select **Use Enrichment Datastore**.

![caret](../assets/datastores/hive/carett-datastore-light.png#only-light)
![caret](../assets/datastores/hive/carett-datastore-dark.png#only-dark)

**Step 2:**: A modal window **Link Enrichment Datastore** will appear. Add a prefix name and select an existing enrichment datastore from the dropdown list.

![link](../assets/datastores/hive/linkk-datastore-light.png#only-light)
![link](../assets/datastores/hive/linkk-datastore-dark.png#only-dark)

| REF. | FIELDS | ACTIONS |
| :---- | :---- | :---- |
| **1.** | Prefix (Required) | Add a prefix name to uniquely identify tables/files when Qualytics writes metadata from the source datastore to your enrichment datastore. |
| **2.** | Enrichment Datastore | Select an enrichment datastore from the dropdown list. |

**Step 3:** After selecting an existing **enrichment datastore** connection, you will view the following details related to the selected enrichment:

* **Teams:** The team associated with managing the enrichment datastore is based on the role of public or private. Example- Marked as **Public** means that this datastore is accessible to all the users.  
* **Host:** This is the server address where the Hive instance is hosted. It is the endpoint used to connect to the Hive  environment.  
* **Database:** Refers to the specific database within the Hive environment where the data is stored.  
* **Schema:** The schema used in the enrichment datastore. The schema is a logical grouping of database objects (tables, views, etc.). Each schema belongs to a single database.

![enrichment](../assets/datastores/hive/enrichmentt-datastore-light.png#only-light)
![enrichment](../assets/datastores/hive/enrichmentt-datastore-dark.png#only-dark)

**Step 4:** Click on the **Finish** button to complete the configuration process for the existing **enrichment datastore**.

![finish](../assets/datastores/hive/finishh-datastore-light.png#only-light)
![finish](../assets/datastores/hive/finishh-datastore-dark.png#only-dark)

When the configuration process is finished, a modal will display a **success message** indicating that **your data has been successfully added**.

![window](../assets/datastores/hive/success-datastore-light.png#only-light)
![window](../assets/datastores/hive/success-datastore-dark.png#only-dark)

Close the success message and you will be automatically redirected to the **Source Datastore Details** page where you can perform data operations on your configured **source datastore**.

![operation](../assets/datastores/hive/operation-datastore-light.png#only-light)
![operation](../assets/datastores/hive/operation-datastore-dark.png#only-dark)

## API Payload Examples

This section provides detailed examples of API payloads to guide you through the process of creating and managing datastores using Qualytics API.

Each example includes endpoint details, sample payloads, and instructions on how to replace placeholder values with actual data relevant to your setup.

### Creating a Datastore

This section provides a sample payload for creating a datastore. Replace the placeholder values with actual data relevant to your setup.

#### Endpoint (Post)

`/api/datastores` _(post)_

=== "Creating a datastore with a new connection"
    ```json
        {
            "name": "your_datastore_name",
            "teams": ["Public"],
            "database": "hive_database",
            "schema": "hive_schema",
            "enrich_only": false,
            "trigger_catalog": true,
            "connection": {
                "name": "your_connection_name",
                "type": "hive",
                "host": "hive_host",
                "port": "hive_port",
                "username": "hive_username",
                "password": "hive_password",
                "parameters": {
                    "zookeeper": false
                }
            }
        }
    ```
=== "Creating a datastore with an existing connection"
    ```json
        {
            "name": "your_datastore_name",
            "teams": ["Public"],
            "database": "hive_database",
            "schema": "hive_schema",
            "enrich_only": false,
            "trigger_catalog": true,
            "connection_id": connection-id
        }
    ```

### Linking Datastore to an Enrichment Datastore through API

#### Endpoint (Patch)

`/api/datastores/{datastore-id}/enrichment/{enrichment-id}` _(patch)_
