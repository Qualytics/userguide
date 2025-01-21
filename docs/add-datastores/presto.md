# Presto

Adding and configuring a Presto connection within Qualytics empowers the platform to build a symbolic link with your schema to perform operations like data discovery, visualization, reporting, cataloging, profiling, scanning, anomaly surveillance, and more.

This documentation provides a step-by-step guide on how to add Presto as both a source and enrichment datastore in Qualytics. It covers the entire process, from initial connection setup to testing and finalizing the configuration.

By following these instructions, enterprises can ensure their Presto environment is properly connected with Qualytics, unlocking the platform's potential to help you proactively manage your full data quality lifecycle

Let’s get started 🚀

## Add a Source Datastore

A source datastore is a storage location used to connect to and access data from external sources. Presto is an example of a source datastore, specifically a type of JDBC datastore that supports connectivity through the JDBC API. Configuring the JDBC datastore enables the Qualytics platform to access and perform operations on the data, thereby generating valuable insights.

**Step 1**: Log in to your Qualytics account and click on the **Add Source Datastore** button located at the top-right corner of the interface.

![add](../assets/datastores/presto/add-light-1.png#only-light)
![add](../assets/datastores/presto/add-dark-2.png#only-dark)

**Step 2**: A modal window- **Add Datastore** will appear, providing you with the options to connect a datastore.

![detail](../assets/datastores/presto/detail-light-2.png#only-light)
![detail](../assets/datastores/presto/detail-dark-2.png#only-dark)

| REF. | FIELDS | ACTIONS |
| :---- | :---- | :---- |
| 1. | Name (Required) | Specify the name of the datastore. (e.g., The specified name will appear on the datastore cards.) |
| 2. | Toggle Button | Toggle ON to create a new source datastore from scratch, or toggle OFF to reuse credentials from an existing connection. |
| 3 | Connector (Required) | Select **Presto** from the dropdown list. |

### Option I: Create a Source Datastore with a new Connection

If the toggle for **Add New existing connection** is turned on, then this will prompt you to add and configure the source datastore from scratch without using existing connection details.

**Step 1**: Select the **Presto** connector from the dropdown list and add connection details such as Secret Management, host, port, username, database, and schema.

![connector](../assets/datastores/presto/connector-light-3.png#only-light)
![connector](../assets/datastores/presto/connector-dark-3.png#only-dark)

**Secrets Management**: This is an optional connection property that allows you to securely store and manage credentials by integrating with HashiCorp Vault and other secret management systems. Toggle it **ON** to enable Vault integration for managing secrets.

!!! note: Once the HashiCorp Vault is set up, use the $ format in Connection form to reference a Vault secret. 

| REF. | FIELDS | ACTION |
| :---- | :---- | :---- |
| 1. | Login URL | Enter the URL used to authenticate with HashiCorp Vault. |
| 2. | Credentials Payload | Input a valid JSON containing credentials for Vault authentication. |
| 3. | Token JSONPath | Specify the JSONPath to retrieve the client authentication token from the response (e.g., $.auth.client\_token). |
| 4. | Secret URL | Enter the URL where the secret is stored in Vault. |
| 5. | Token Header Name | Set the header name used for the authentication token (e.g., X-Vault-Token). |
| 6. | Data JSONPath | Specify the JSONPath to retrieve the secret data (e.g., $.data). |

![vault](../assets/datastores/presto/vault-light-4.png#only-light)
![vault](../assets/datastores/presto/vault-dark-4.png#only-dark)

**Step 2**: The configuration form will expand, requesting credential details before establishing the connection.

![detail](../assets/datastores/presto/detail-light-5.png#only-light)
![detail](../assets/datastores/presto/detail-dark-5.png#only-dark)

| REF. | FIELDS | ACTIONS |
| :---- | :---- | :---- |
| 1. | Host (Required) | Get **Hostname** from your Presto account and add it to this field. |
| 2. | Port (Required) | Specify the **Port** number. |
| 3. | User (Required) | Enter the **User** to connect. |
| 4. | Password (Required) | Enter the **password** to connect to the database. |
| 5. | Catalog (Required) | Add a **Catalog** to fetch data structures and metadata from the Databricks. |
| 6. | Schema (Required) | Define the schema within the database that should be used. |
| 7. | Teams (Required) | Select one or more teams from the dropdown to associate with this source datastore. |
| 8. | Initiate Cataloging (Optional) | Tick the checkbox to automatically perform catalog operation on the configured source datastore. |

**Step 3**: After adding the source datastore details, click on the **Test Connection** button to check and verify its connection.  

![test](../assets/datastores/presto/test-light-6.png#only-light)
![test](../assets/datastores/presto/test-dark-6.png#only-dark)

If the credentials and provided details are verified, a success message will be displayed indicating that the connection has been verified.

### Option II: Use an Existing Connection

If the toggle for **Add new connection** is turned off, then this will prompt you to configure the source datastore using the existing connection details.

**Step 1**: Select a **connection** to reuse existing credentials.

![detail](../assets/datastores/presto/detail-light-7.png#only-light)
![detail](../assets/datastores/presto/detail-dark-7.png#only-dark)

!!! note 
    If you are using existing credentials, you can only edit the details such as Database, Schema, Teams and Initiate Cataloging. 

**Step 2**: Click on the **Test Connection** button to verify the existing connection details. If connection details are verified, a success message will be displayed.  

![test](../assets/datastores/presto/test-light-8.png#only-light)
![test](../assets/datastores/presto/test-dark-8.png#only-dark)

!!! note 
    Clicking on the Finish button will create the source datastore and bypass the enrichment datastore configuration step. 

!!! info 
    It is recommended to click on the Next button, which will take you to the enrichment datastore configuration page. 

## Add Enrichment Datastore

Once you have successfully tested and verified your source datastore connection, you have the option to add the enrichment datastore (recommended). The enrichment datastore is used to store the analyzed results, including any anomalies and additional metadata in tables. This setup provides full visibility into your data quality, helping you manage and improve it effectively.

!!! warning 
    Qualytics does not support the Presto connector as an enrichment datastore, but you can point to a different enrichment datastore. 

**Step 1:** Whether you have added a source datastore by creating a new datastore connection or using an existing connection, click on the **Next** button to start adding the **Enrichment Datastore**.

![next](../assets/datastores/presto/next-light-9.png#only-light)
![next](../assets/datastores/presto/next-dark-9.png#only-dark)

**Step 2:** A modal window **Link Enrichment Datastore** will appear, providing you with the options to configure an **enrichment datastore**.

![enrichment](../assets/datastores/presto/enrichment-light-10.png#only-light)
![enrichment](../assets/datastores/presto/enrichment-dark-10.png#only-dark)

| REF. | FIELDS | ACTIONS |
| :---- | :---- | :---- |
| 1. | Prefix (Required) | Add a prefix name to uniquely identify tables/files when Qualytics writes metadata from the source datastore to your enrichment datastore. |
| 2. | Caret Down Button | Click the caret down to select either **Use Enrichment Datastore** or **Add Enrichment Datastore**. |
| 3. | Enrichment Datastore | Select an enrichment datastore from the dropdown list |

### Option I: Create an Enrichment Datastore with a new Connection

If the toggles **Add new connection** is turned on, then this will prompt you to add and configure the enrichment datastore from scratch without using an existing enrichment datastore and its connection details.

**Step 1**: Click on the caret button and select Add Enrichment Datastore.

![add](../assets/datastores/presto/add-light-11.png#only-light)
![add](../assets/datastores/presto/add-dark-11.png#only-dark)

A modal window **Link Enrichment Datastore** will appear. Enter the following details to create an enrichment datastore with a new connection.

![detail](../assets/datastores/presto/detail-light-12.png#only-light)
![detail](../assets/datastores/presto/detail-dark-12.png#only-dark)

| REF. | FIELDS | ACTIONS |
| :---- | :---- | :---- |
| 1. | Prefix | Add a prefix name to uniquely identify tables/files when Qualytics writes metadata from the source datastore to your enrichment datastore. |
| 2. | Name | Give a name for the enrichment datastore. |
| 3. | Toggle Button for add new connection | Toggle ON to create a new enrichment from scratch or toggle OFF to reuse credentials from an existing connection. |
| 4. | Connector | Select a datastore connector from the dropdown list. |

**Step 2:** Add connection details for your selected **enrichment datastore** connector.

![detail](../assets/datastores/presto/detail-light-13.png#only-light)
![detail](../assets/datastores/presto/detail-dark-13.png#only-dark)

!!! note 
    Qualytics does not support Presto as an enrichment datastore. Instead, you can select a different enrichment datastore for this purpose. For demonstration purposes, we are using Microsoft SQL Server as the enrichment datastore. You can use any other JDBC or DFS datastore of your choice for the enrichment datastore configuration. 

**Step 3:** Click on the **Test Connection** button to verify the selected enrichment datastore connection. If the connection is verified, a flash message will indicate that the connection with the datastore has been successfully verified.

![test](../assets/datastores/presto/test-light-14.png#only-light)
![test](../assets/datastores/presto/test-dark-14.png#only-dark)

**Step 4:** Click on the **Finish** button to complete the configuration process.

![finish](../assets/datastores/presto/finish-light-15.png#only-light)
![finish](../assets/datastores/presto/finish-dark-15.png#only-dark)

When the configuration process is finished, a modal will display a **success message** indicating that **your datastore has been successfully added**.

![success](../assets/datastores/presto/success-light-16.png#only-light)
![success](../assets/datastores/presto/success-dark-16.png#only-dark)

**Step 5:** Close the Success dialogue and the page will automatically redirect you to the **Source Datastore Details** page where you can perform data operations on your configured **source datastore**.

![overview](../assets/datastores/presto/overview-light-17.png#only-light)
![overview](../assets/datastores/presto/overview-dark-17.png#only-dark)

### Option II: Use an Existing Connection

If the **Use enrichment datastore** option is selected from the caret button, you will be prompted to configure the datastore using existing connection details.

**Step 1**: Click on the caret button and select **Use Enrichment Datastore**.

![use](../assets/datastores/presto/use-light-18.png#only-light)
![use](../assets/datastores/presto/use-dark-18.png#only-dark)

**Step 2**: A modal window **Link Enrichment Datastore** will appear. Add a prefix name and select an existing enrichment datastore from the dropdown list.

![link](../assets/datastores/presto/link-light-19.png#only-light)
![link](../assets/datastores/presto/link-dark-19.png#only-dark)

!!! note 
    Qualytics does not support Presto as an enrichment datastore. Instead, you can select a different enrichment datastore for this purpose. For demonstration purposes, we are using Microsoft SQL Server as the enrichment datastore. You can use any other JDBC or DFS datastore of your choice for the enrichment datastore configuration. 

| REF. | FIELDS | ACTIONS |
| :---- | :---- | :---- |
| 1. | Prefix | Add a prefix name to uniquely identify tables/files when Qualytics writes metadata from the source datastore to your enrichment datastore. |
| 2. | Enrichment Datastore | Select an enrichment datastore from the dropdown list. |

**Step 3:** After selecting an existing **enrichment datastore** connection, you will view the following details related to the selected enrichment:

* **Teams:** The team associated with managing the enrichment datastore is based on the role of public or private. For example, Marked as **Public** means that this datastore is accessible to all the users.  
* **Host:** This is the server address where the **Presto** instance is hosted. It is the endpoint used to connect to the Presto environment.  
* **Database:** Refers to the specific database within the **Presto** environment where the data is stored.  
* **Schema:** The schema used in the enrichment datastore. The schema is a logical grouping of database objects(tables, views, etc.).Each schema belongs to a single database.

![detail](../assets/datastores/presto/detail-light-20.png#only-light)
![detail](../assets/datastores/presto/detail-dark-20.png#only-dark)

**Step 4:** Click on the **Finish** button to complete the configuration process for the existing **enrichment datastore**.

![finish](../assets/datastores/presto/finish-light-21.png#only-light)
![finish](../assets/datastores/presto/finish-dark-21.png#only-dark)

When the configuration process is finished, a modal will display a **success message** indicating that **your data has been successfully added**.  

![success](../assets/datastores/presto/success-light-22.png#only-light)
![success](../assets/datastores/presto/success-dark-22.png#only-dark)

Close the success message and you will be automatically redirected to the **Source Datastore Details** page where you can perform data operations on your configured **source datastore**.  

![overview](../assets/datastores/presto/overview-light-23.png#only-light)
![overview](../assets/datastores/presto/overview-dark-23.png#only-dark)

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
