# Trino

Adding and configuring a Trino connection within Qualytics empowers the platform to build a symbolic link with your schema to perform operations like data discovery, visualization, reporting, syncing, profiling, scanning, anomaly surveillance, and more.

This documentation provides a step-by-step guide on adding Trino as a source datastore in Qualytics. It covers the entire process, from initial connection setup to testing and finalizing the configuration.

By following these instructions, enterprises can ensure their Trino environment is properly connected with Qualytics, unlocking the platform’s potential to help you proactively manage your full data quality lifecycle.

Let’s get started 🚀

## Trino Setup Guide

Qualytics connects to Trino through the **Trino JDBC driver**. It uses standard SQL queries for data profiling and scanning. Since Trino is a distributed query engine, permissions are determined by the underlying data source (connector) configured in the Trino catalog (e.g., Hive, Delta Lake, Iceberg, RDBMS).

### Minimum Trino Permissions (Source Datastore)

| Permission                                    | Purpose                                                                 |
|-----------------------------------------------|-------------------------------------------------------------------------|
| `SELECT` on target tables                     | Read data from tables for profiling and scanning                        |
| Access to the Trino catalog                   | Browse available schemas and tables                                     |
| Access to the Trino schema                    | Browse available tables and columns                                     |

### Additional Permissions for Enrichment Datastore

When using Trino as an enrichment datastore, the following additional permissions are required for Qualytics to write metadata tables (e.g., `_qualytics_*`):

| Permission                                    | Purpose                                                                 |
|-----------------------------------------------|-------------------------------------------------------------------------|
| `CREATE TABLE` in the schema                  | Create enrichment tables (`_qualytics_*`)                               |
| `INSERT` into tables                          | Write anomaly records, scan results, and check metrics                  |
| `DELETE` from tables                          | Remove stale enrichment records                                         |
| `ALTER TABLE` in the schema                   | Modify enrichment table schemas during version migrations               |
| `DROP TABLE` in the schema                    | Remove enrichment tables during cleanup or when the datastore is unlinked |

The actual permissions depend on the Trino security model configured for your deployment:

| Security Model              | How Permissions Are Managed                                                  |
|-----------------------------|------------------------------------------------------------------------------|
| **No security (default)**   | All users have full read/write access to all catalogs and schemas            |
| **File-based access control** | Permissions are defined in `rules.json` — ensure the Qualytics user has `SELECT` (and `INSERT`, `CREATE TABLE` for enrichment) on the target catalog and schema |
| **Connector-level security** | Permissions are delegated to the underlying data source — ensure the Qualytics user has read (and write for enrichment) access at the source level |

### Example: File-Based Access Control Configuration

If your Trino deployment uses file-based access control (`rules.json`), ensure the Qualytics user has appropriate access to the target catalog and schema:

```json
{
  "catalogs": [
    {
      "user": "qualytics_read",
      "catalog": "<catalog_name>",
      "allow": "read-only"
    }
  ]
}
```

For enrichment datastores, use `"allow": "all"` instead of `"read-only"` to enable write operations.

!!! note
    Trino permissions are managed through the underlying connector's security model (e.g., Hive, Delta Lake, Iceberg). Ensure the Trino user has the appropriate access to the backing data source.

### Troubleshooting Common Errors

| Error                                          | Likely Cause                                                                 | Fix                                                                                     |
|------------------------------------------------|------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| `Access Denied: Cannot select from table`      | The user lacks `SELECT` on the target table in the Trino access control rules or the underlying connector | Add `SELECT` permission for the user in `rules.json` or grant access in the underlying data source |
| `Access Denied: Cannot create table`           | The enrichment user lacks `CREATE TABLE` on the target schema                | Add `CREATE TABLE` permission in the access control rules or underlying data source     |
| `Catalog does not exist`                       | The catalog name in the connection form does not match a configured Trino catalog | Verify available catalogs with `SHOW CATALOGS` in Trino                               |
| `Schema does not exist`                        | The schema name does not exist in the specified catalog                       | Verify available schemas with `SHOW SCHEMAS FROM <catalog>`                             |
| `Connection refused`                           | The Trino coordinator is not reachable or the port (default 8080) is incorrect | Verify the host, port, and that the Trino coordinator is running                      |
| `Authentication failed`                        | Incorrect username or password, or the Trino server requires a different authentication method | Verify credentials and check if the Trino server uses LDAP, Kerberos, or password authentication |

### Detailed Troubleshooting Notes

#### Authentication Errors

The error `Authentication failed` indicates that the credentials are incorrect or the authentication method does not match the server configuration.

Common causes:

- **Incorrect password** — the password does not match the one configured in the Trino server.
- **Wrong authentication method** — the Trino server uses LDAP or Kerberos, but the connection form provides basic username/password.
- **HTTPS required** — the Trino coordinator requires HTTPS connections, but the connection is using HTTP.

!!! note
    Trino authentication is configured at the coordinator level. Check the `password-authenticator.properties` file for the configured authentication method.

#### Permission Errors

The error `Access Denied: Cannot select from table` or `Access Denied: Cannot create table` means the user authenticated successfully but lacks access to the target resource.

Common causes:

- **File-based access control** — the `rules.json` file does not grant the required permissions to the Qualytics user.
- **Connector-level security** — the underlying data source does not grant the necessary access.
- **Missing enrichment permissions** — for enrichment datastores, the user lacks `CREATE TABLE` or `INSERT` permissions in addition to `SELECT`.

#### Connection Errors

The error `Connection refused` or `Catalog does not exist` indicates a connectivity or configuration issue.

Common causes:

- **Coordinator not reachable** — the Trino coordinator host or port (default 8080) is incorrect.
- **Wrong catalog name** — the catalog name in the connection form does not match a configured Trino catalog.
- **Coordinator not running** — the Trino coordinator process is not started.

!!! tip
    Start by confirming credentials are valid (authentication errors), then verify access control rules (permission errors), and finally check coordinator connectivity (connection errors).

## Add the Source Datastore

A source datastore is a storage location used to connect to and access data from external sources. Trino is an example of such a datastore, specifically a type of JDBC datastore that supports connectivity through the JDBC API. Configuring the Trino datastore allows the Qualytics platform to access and perform operations on the data, thereby generating valuable insights.

**Step 1:** Log in to your Qualytics account and click on the **Add Source Datastore** button located at the top-right corner of the interface.

![datastore](../../assets/source-datastores/add-datastores/trino/datastore.png)

**Step 2:** A modal window - **Add Datastore** will appear, providing you with the options to connect a datastore.

![connect](../../assets/source-datastores/add-datastores/trino/connect.png)

| REF. | FIELD | ACTIONS |
| :---- | :---- | :---- |
| 1. | Name | Specify the name of the datastore (e.g., the specified name will appear on the datastore cards) |
| 2. | Toggle Button | Toggle **ON** to create a new source datastore from scratch, or toggle **OFF** to reuse credentials from an existing connection |
| 3. | Connector | Select **Trino** from the dropdown list. |

### Option I: Create a Datastore with a new Connection

If the toggle for **Add new connection** is turned on, then this will prompt you to add and configure the source datastore from scratch without using existing connection details.

**Step 1**: Select the **Trino** connector from the dropdown list and add connection details such as Secret Management, host, port, username, etc.

![select](../../assets/source-datastores/add-datastores/trino/select.png)

**Secrets Management**: This is an optional connection property that allows you to securely store and manage credentials by integrating with HashiCorp Vault and other secret management systems. Toggle it **ON** to enable Vault integration for managing secrets.

!!! note
    After configuring HashiCorp Vault integration, you can use ${key} in any Connection property to reference a key from the configured Vault secret. Each time the Connection is initiated, the corresponding secret value will be retrieved dynamically.

| REF. | FIELDS | ACTIONS |
| :---- | :---- | :---- |
| 1. | Login URL | Enter the URL used to authenticate with HashiCorp Vault. |
| 2. | Credentials Payload | Input a valid JSON containing credentials for Vault authentication. |
| 3. | Token JSONPath | Specify the JSONPath to retrieve the client authentication token from the response (e.g., $.auth.client_token). |
| 4. | Secret URL | Enter the URL where the secret is stored in Vault. |
| 5. | Token Header Name | Set the header name used for the authentication token (e.g., X-Vault-Token). |
| 6. | Data JSONPath | Specify the JSONPath to retrieve the secret data (e.g., $.data). |

![secret](../../assets/source-datastores/add-datastores/trino/secret.png)

**Step 2**: The configuration form will expand, requesting credential details before establishing the connection.

![form](../../assets/source-datastores/add-datastores/trino/form.png)

| REF. | FIELDS | ACTIONS |
| :---- | :---- | :---- |
| 1. | Host | Get **Hostname** from your Trino account and add it to this field. |
| 2. | Port | Specify the **Port** number. |
| 3. | User | Enter the **User ID** to connect. |
| 4. | Password | Enter the **Password** to connect to the database. |
| 5. | Catalog | Add a **Catalog** to fetch data structures and metadata from Trino. |
| 6. | Schema | Define the schema within the database that should be used. |
| 7. | Teams | Select one or more teams from the dropdown to associate with this source datastore. |
| 8. | Initiate Sync | Tick the checkbox to automatically perform sync operation on the configured source datastore to detect new, changed, or removed containers and fields. |

**Step 3**: After adding the source datastore details, click on the **Test Connection** button to check and verify its connection.

![test](../../assets/source-datastores/add-datastores/trino/test.png)

If the credentials and provided details are verified, a success message will be displayed indicating that the connection has been verified.

### Option II: Use an Existing Connection

If the toggle for **Add new connection** is turned off, then this will prompt you to configure the source datastore using the existing connection details.

**Step 1**: Select a **connection** to reuse existing credentials.

![existing](../../assets/source-datastores/add-datastores/trino/existing.png)

!!! note
    If you are using existing credentials, you can only edit the details such as Database, Teams, and Initiate Sync.

**Step 2**: Click on the **Test Connection** button to check and verify the source datastore connection. If connection details are verified, a success message will be displayed.

![testt](../../assets/source-datastores/add-datastores/trino/testt.png)

!!! note
    Clicking on the **Finish** button will create the source datastore and bypass the **enrichment datastore** configuration step.

!!! tip
    It is recommended to click on the **Next** button, which will take you to the **enrichment datastore** configuration page.

## Add Enrichment Datastore

After successfully testing and verifying your source datastore connection, you have the option to add an enrichment datastore (recommended). This datastore is used to store analyzed results, including any anomalies and additional metadata in tables. This setup provides comprehensive visibility into your data quality, helping you manage and improve it effectively.

**Step 1**: Whether you have added a source datastore by creating a new datastore connection or using an existing connection, click on the **Next** button to start adding the **Enrichment Datastore**.

![next](../../assets/source-datastores/add-datastores/trino/next.png)

**Step 2**: A modal window - **Link Enrichment Datastore** will appear, providing you with the options to configure an **enrichment datastore**.

![window](../../assets/source-datastores/add-datastores/trino/window.png)

| REF. | FIELDS | ACTIONS |
| :---- | :---- | :---- |
| 1. | Prefix (Required) | Add a prefix name to uniquely identify tables/files when Qualytics writes metadata from the source datastore to your enrichment datastore. |
| 2. | Caret Down Button | Click the caret down to select either **Use Enrichment Datastore** or **Add Enrichment Datastore**. |
| 3. | Enrichment Datastore | Select an enrichment datastore from the dropdown list. |

### Option I: Create an Enrichment Datastore with a new Connection

If the toggle **Add new connection** is turned on, then this will prompt you to add and configure the enrichment datastore from scratch without using an existing enrichment datastore and its connection details.

**Step 1**: Click on the caret button and select **Add Enrichment Datastore**.

![caret](../../assets/source-datastores/add-datastores/trino/caret.png)

A modal window **Link Enrichment Datastore** will appear. Enter the following details to create an enrichment datastore with a new connection.

![windoww](../../assets/source-datastores/add-datastores/trino/windoww.png)

| REF. | FIELDS | ACTIONS |
| :---- | :---- | :---- |
| 1. | Prefix | Add a prefix name to uniquely identify tables/files when Qualytics writes metadata from the source datastore to your enrichment datastore. |
| 2. | Name | Give a name for the enrichment datastore. |
| 3. | Toggle Button for add new connection | Toggle ON to create a new enrichment datastore from scratch or toggle OFF to reuse credentials from an existing connection. |
| 4. | Connector | Select a datastore connector from the dropdown list. |

**Step 2**: Add connection details for your selected **enrichment datastore** connector.

![selectedd](../../assets/source-datastores/add-datastores/trino/selectedd.png)

**Step 3**: Click on the **Test Connection** button to verify the selected enrichment datastore connection. If the connection is verified, a flash message will indicate that the connection with the datastore has been successfully verified.

![testtt](../../assets/source-datastores/add-datastores/trino/testtt.png)

**Step 4**: Click on the **Finish** button to complete the configuration process.

![Finishh](../../assets/source-datastores/add-datastores/trino/finish.png)

When the configuration process is finished, a modal will display a success message indicating that your datastore has been successfully added.

**Step 5**: Close the success dialog and the page will automatically redirect you to the **Source Datastore Details** page where you can perform data operations on your configured **source datastore**.

![operation](../../assets/source-datastores/add-datastores/trino/operation.png)

### Option II: Use an Existing Connection

If the **Use enrichment datastore** option is selected from the caret button, you will be prompted to configure the datastore using existing connection details.

**Step 1**: Click on the caret button and select **Use Enrichment Datastore**.

![carett](../../assets/source-datastores/add-datastores/trino/carett.png)

**Step 2**: A modal window **Link Enrichment Datastore** will appear. Add a prefix name and select an existing enrichment datastore from the dropdown list.

![modall](../../assets/source-datastores/add-datastores/trino/modall.png)

| REF. | FIELDS | ACTIONS |
| :---- | :---- | :---- |
| 1. | Prefix | Add a prefix name to uniquely identify tables/files when Qualytics writes metadata from the source datastore to your enrichment datastore. |
| 2. | Enrichment Datastore | Select an enrichment datastore from the dropdown list. |

**Step 3**: After selecting an existing **enrichment datastore** connection, you will view the following details related to the selected enrichment:

* **Teams**: The team associated with managing the enrichment datastore is based on the role of public or private. Example - Marked as **Public** means that this datastore is accessible to all the users.  
* **Host**: This is the server address where the **Trino** instance is hosted. It is the endpoint used to connect to the **Trino** environment.  
* **Database**: Refers to the specific database within the Trino environment where the data is stored.  
* **Schema**: The schema used in the enrichment datastore. The schema is a logical grouping of database objects (tables, views, etc.). Each schema belongs to a single database.

![detail](../../assets/source-datastores/add-datastores/trino/detail.png)

**Step 4**: Click on the **Finish** button to complete the configuration process for the existing **enrichment datastore**.

![finishh](../../assets/source-datastores/add-datastores/trino/finishh.png)

When the configuration process is finished, a modal will display a success message indicating that your datastore has been successfully added.

Close the success message and you will be automatically redirected to the **Source Datastore Details** page where you can perform data operations on your configured **source datastore**.

![operation](../../assets/source-datastores/add-datastores/trino/operation.png)

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
            "database": "trino_database",
            "schema": "trino_schema",
            "enrich_only": false,
            "trigger_catalog": true,
            "connection": {
                "name": "your_connection_name",
                "type": "trino",
                "host": "trino_host",
                "port": "trino_port",
                "username": "trino_username",
                "password": "trino_password",
                "parameters":{
                    "ssl_truststore":"truststore.jks"
                }
            }
        }
    ```
=== "Creating a datastore with an existing connection"
    ```json
        {
            "name": "your_datastore_name",
            "teams": ["Public"],
            "database": "trino_database",
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
            "database": "trino_database",
            "schema": "trino_schema",
            "enrich_only": true,
            "connection": {
                "name": "your_connection_name",
                "type": "trino",
                "host": "trino_host",
                "port": "trino_port",
                "username": "trino_username",
                "password": "trino_password",
                "parameters":{
                    "ssl_truststore":"truststore.jks"
                }
            }
        }
    ```
=== "Creating an enrichment datastore with an existing connection"
    ```json
        {
            "name": "your_datastore_name",
            "teams": ["Public"],
            "database": "trino_database",
            "schema": "trino_schema",
            "enrich_only": true,
            "connection_id": connection-id
        }
    ``` 

### Linking Datastore to an Enrichment Datastore through API

#### Endpoint (Patch)

`/api/datastores/{datastore-id}/enrichment/{enrichment-id}` _(patch)_
