# Presto

Adding and configuring a Presto connection within Qualytics empowers the platform to build a symbolic link with your schema to perform operations like data discovery, visualization, reporting, cataloging, profiling, scanning, anomaly surveillance, and more.

This documentation provides a step-by-step guide on adding Presto as a source datastore in Qualytics. It covers the entire process, from initial connection setup to testing and finalizing the configuration.

By following these instructions, enterprises can ensure their Presto environment is properly connected with Qualytics, unlocking the platform's potential to help you proactively manage your full data quality lifecycle.

Let’s get started 🚀

## Add the Source Datastore

A source datastore is a storage location used to connect to and access data from external sources. Presto is an example of such a datastore, specifically a type of JDBC datastore that supports connectivity through the JDBC API. Configuring the Presto datastore allows the Qualytics platform to access and perform operations on the data, thereby generating valuable insights.

**Step 1**: Log in to your Qualytics account and click on the **Add Source Datastore** button located at the top-right corner of the interface.

![datastore](../assets/datastores/presto/datastore-light.png#only-light)
![datastore](../assets/datastores/presto/datastore-dark.png#only-dark)

**Step 2**: A modal window- **Add Datastore** will appear, providing you with the options to connect a datastore.

![window](../assets/datastores/presto/window-light.png#only-light)
![window](../assets/datastores/presto/window-dark.png#only-dark)

| REF. | FIELDS | ACTIONS |
| :---- | :---- | :---- |
| 1. | Name | Specify the name of the datastore (e.g., The specified name will appear on the datastore cards) |
| 2. | Toggle Button | Toggle **ON** to create a new source datastore from scratch, or toggle **OFF** to reuse credentials from an existing connection |
| 3. | Connector | Select **Teradata** from the dropdown list. |

### Option I: Create a Datastore with a new Connection

If the toggle for **Add New connection** is turned on, then this will prompt you to add and configure the source datastore from scratch without using existing connection details.

**Step 1**: Select the **Presto** connector from the dropdown list and add connection details such as Secret Management, host, port, username, etc.

![presto](../assets/datastores/presto/presto-light.png#only-light)
![presto](../assets/datastores/presto/presto-dark.png#only-dark)

**Secrets Management**: This is an optional connection property that allows you to securely store and manage credentials by integrating with HashiCorp Vault and other secret management systems. Toggle it **ON** to enable Vault integration for managing secrets.

![Secret](../assets/datastores/presto/secret-light.png#only-light)
![Secret](../assets/datastores/presto/secret-dark.png#only-dark)

!!! note 
    Once the HashiCorp Vault is set up, use the $ format in Connection form to reference a Vault secret. 

| REF | FIELDS | ACTIONS |
| :---- | :---- | :---- |
| 1. | Login URL | Enter the URL used to authenticate with HashiCorp Vault. |
| 2. | Credentials Payload | Input a valid JSON containing credentials for Vault authentication. |
| 3. | Token JSONPath | Specify the JSONPath to retrieve the client authentication token from the response (e.g., $.auth.client\_token). |
| 4. | Secret URL | Enter the URL where the secret is stored in Vault. |
| 5. | Token Header Name | Set the header name used for the authentication token (e.g., X-Vault-Token). |
| 6. | Data JSONPath | Specify the JSONPath to retrieve the secret data (e.g., $.data). |

**Step 2**: The configuration form will expand, requesting credential details before establishing the connection.

![expand](../assets/datastores/presto/expand-datastore-light.png#only-light)
![expand](../assets/datastores/presto/expand-datastore-dark.png#only-dark)

| REF. | FIELDS | ACTIONS |
| :---- | :---- | :---- |
| 1. | Host | Get **Hostname** from your Teradata account and add it to this field. |
| 2. | Port | Specify the **Port** number. |
| 3. | User | Enter the **User ID** to connect. |
| 4. | Password | Enter the **password** to connect to the database. |
| 5. | Catalog | Enter the catalog name. In AWS Athena, this refers to the data catalog that contains database and table metadata. |
| 6. | Schema | Define the schema within the database that should be used. |
| 7. | Teams | Select one or more teams from the dropdown to associate with this source datastore. |
| 8. | Initial Cataloging | Tick the checkbox to automatically perform catalog operation on the configured source datastore to gather data structures and corresponding metadata. |

**Step 3**: After adding the source datastore details, click on the **Test Connection** button to check and verify its connection.

![test](../assets/datastores/presto/test-datastore-light.png#only-light)
![test](../assets/datastores/presto/test-datastore-dark.png#only-dark)

If the credentials and provided details are verified, a success message will be displayed indicating that the connection has been verified.

### Option II: Use an Existing Connection

If the toggle for **Use an existing connection** is turned off, then this will prompt you to configure the source datastore using the existing connection details.

**Step 1**: Select a **connection** to reuse existing credentials.

![connection](../assets/datastores/presto/connection-light.png#only-light)
![connection](../assets/datastores/presto/connection-dark.png#only-dark)

!!! note 
    If you are using existing credentials, you can only edit the details such as Database, Teams, and Initiate Cataloging. 

**Step 2**: Click on the **Test Connection** button to check and verify the source data connection. If connection details are verified, a success message will be displayed.

![connection](../assets/datastores/presto/test-datastore-light.png#only-light)
![connection](../assets/datastores/presto/test-datastore-dark.png#only-dark)

!!! note 
    Clicking on the Finish button will create the source datastore and bypass the enrichment datastore configuration step. 

!!! tip 
    It is recommended to click on the Next button, which will take you to the enrichment datastore configuration page. 

## Add Enrichment Datastore

After successfully testing and verifying your source datastore connection, you have the option to add an enrichment datastore (recommended). This datastore is used to store analyzed results, including. This setup provides comprehensive visibility into your data quality, enabling you to manage and improve it effectively.

!!! warning 
   Qualytics does not support the Presto connector as an enrichment datastore, but you can point to a different enrichment datastore. |

**Step 1**: Whether you have added a source datastore by creating a new datastore connection or using an existing connection, click on the **Next** button to start adding the **Enrichment Datastore**.

![next](../assets/datastores/presto/next-light.png#only-light)
![next](../assets/datastores/presto/next-dark.png#only-dark)

**Step 2**: A modal window- **Link Enrichment Datastore** will appear, providing you with the options to configure an **enrichment datastore**.

![window](../assets/datastores/presto/windoww-light.png#only-light)
![window](../assets/datastores/presto/windoww-dark.png#only-dark)

| REF. | FIELDS | ACTIONS |
| :---- | :---- | :---- |
| 1. | Prefix (Required) | Add a prefix name to uniquely identify tables/files when Qualytics writes metadata from the source datastore to your enrichment datastore. |
| 2. | Caret Down Button | Click the caret down to select either **Use Enrichment Datastore** or **Add Enrichment Datastore**. |
| 3. | Enrichment Datastore | Select an enrichment datastore from the dropdown list. |

### Option I: Create an Enrichment Datastore with a new Connection

If the toggles **Add new connection** is turned on, then this will prompt you to add and configure the enrichment datastore from scratch without using an existing enrichment datastore and its connection details.

**Step 1**: Click on the caret button and select Add Enrichment Datastore.

![caret](../assets/datastores/presto/caret-light.png#only-light)
![caret](../assets/datastores/presto/caret-dark.png#only-dark)

A modal window **Link Enrichment Datastore** will appear. Enter the following details to create an enrichment datastore with a new connection.

![modall](../assets/datastores/presto/modall-light.png#only-light)
![modall](../assets/datastores/presto/modall-dark.png#only-dark)

| REF. | FIELDS | ACTIONS |
| :---- | :---- | :---- |
| 1. | Prefix | Add a prefix name to uniquely identify tables/files when Qualytics writes metadata from the source datastore to your enrichment datastore. |
| 2. | Name | Give a name for the enrichment datastore. |
| 3. | Toggle Button for add new connection | Toggle ON to create a new enrichment from scratch or toggle OFF to reuse credentials from an existing connection. |
| 4. | Connector | Select a datastore connector from the dropdown list. |

**Step 2**: Add connection details for your selected **enrichment datastore** connector.

![enrichmentt](../assets/datastores/presto/enrichmentt-light.png#only-light)
![enrichmentt](../assets/datastores/presto/enrichmentt-dark.png#only-dark)

!!! note 
    Qualytics does not support Presto as an enrichment datastore. Instead, you can select a different enrichment datastore for this purpose. For demonstration purposes, we are using BigQuery as the enrichment datastore. You can use any other JDBC or DFS datastore of your choice for the enrichment datastore configuration. 

**Step 3:** Click on the Test Connection button to verify the selected enrichment datastore connection. If the connection is verified, a flash message will indicate that the connection with the datastore has been successfully verified.

![testt](../assets/datastores/presto/testt-light.png#only-light)
![testt](../assets/datastores/presto/testt-dark.png#only-dark)

If the connection is verified, a flash message will indicate that the connection with the datastore has been successfully verified.

**Step 4:** Click on the **Finish** button to complete the configuration process.

![finish](../assets/datastores/presto/finish-light.png#only-light)
![finish](../assets/datastores/presto/finish-dark.png#only-dark)

When the configuration process is finished, a modal will display a **success message** indicating that **your datastore has been successfully added**.

![success](../assets/datastores/presto/success-light.png#only-light)
![Success](../assets/datastores/presto/success-dark.png#only-dark)

**Step 5**: Close the Success dialogue and the page will automatically redirect you to the **Source Datastore Details** page where you can perform data operations on your configured **source datastore**.

![operation](../assets/datastores/presto/operation-light.png#only-light)
![operation](../assets/datastores/presto/operation-dark.png#only-dark)

### Option II: Use an Existing Connection

If the **Use enrichment datastore** option is selected from the caret button, you will be prompted to configure the datastore using existing connection details.

**Step 1**: Click on the caret button and select **Use Enrichment Datastore**.

![down](../assets/datastores/presto/down-light.png#only-light)
![down](../assets/datastores/presto/down-dark.png#only-dark)

!!! note 
    Qualytics does not support Presto as an enrichment datastore. Instead, you can select a different enrichment datastore for this purpose. For demonstration purposes, we are using BigQuery as the enrichment datastore. You can use any other JDBC or DFS datastore of your choice for the enrichment datastore configuration. 

**Step 2**: A modal window **Link Enrichment Datastore** will appear. Add a prefix name and select an existing enrichment datastore from the dropdown list.

![link](../assets/datastores/presto/create-datastore-light.png#only-light)
![link](../assets/datastores/presto/create-datastore-dark.png#only-dark)

| REF. | FIELDS | ACTIONS |
| :---- | :---- | :---- |
| 1. | Prefix | Add a prefix name to uniquely identify tables/files when Qualytics writes metadata from the source datastore to your enrichment datastore. |
| 2. | Enrichment Datastore | Select an enrichment datastore from the dropdown list. |

**Step 3**: After selecting an existing **enrichment datastore** connection, you will view the following details related to the selected enrichment:

* **Teams**: The team associated with managing the enrichment datastore is based on the role of public or private. Example- Marked as **Public** means that this datastore is accessible to all the users.  
* **Host**: This is the server address where the **Teradata** instance is hosted. It is the endpoint used to connect to the PostgreSQL environment.  
* **Database**: Refers to the specific database within the Teradata environment where the data is stored.  
* **Schema**: The schema used in the enrichment datastore. The schema is a logical grouping of database objects (tables, views, etc.). Each schema belongs to a single database.

![detail](../assets/datastores/presto/detail-light.png#only-light)
![Screenshot](../assets/datastores/presto/detail-dark.png#only-dark)

**Step 4**: Click on the **Finish** button to complete the configuration process for the existing **enrichment datastore**.

![finish](../assets/datastores/presto/finishh-light.png#only-light)
![finish](../assets/datastores/presto/finishh-dark.png#only-dark)

When the configuration process is finished, a modal will display a **success message** indicating that **your data has been successfully added**.

![success](../assets/datastores/presto/success-light.png#only-light)
![Success](../assets/datastores/presto/success-dark.png#only-dark)

Close the success message and you will be automatically redirected to the **Source Datastore Details** page where you can perform data operations on your configured **source datastore**.

![operation](../assets/datastores/presto/operation-light.png#only-light)
![operation](../assets/datastores/presto/operation-dark.png#only-dark)

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
            "database": "presto_database",
            "schema": "presto_schema",
            "enrich_only": false,
            "trigger_catalog": true,
            "connection": {
                "name": "your_connection_name",
                "type": "presto",
                "host": "presto_host",
                "port": "presto_port",
                "username": "presto_username",
                "password": "presto_password",
                "parameters":{
                    "ssl_truststore":"truststore.jks"
                },
            }
        }
    ```
=== "Creating a datastore with an existing connection"
    ```json
        {
            "name": "your_datastore_name",
            "teams": ["Public"],
            "database": "presto_database",
            "schema": "presto_schema",
            "enrich_only": false,
            "trigger_catalog": true,
            "connection_id": connection-id
        }
    ```

### Linking Datastore to an Enrichment Datastore through API

#### Endpoint (Patch)

`/api/datastores/{datastore-id}/enrichment/{enrichment-id}` _(patch)_