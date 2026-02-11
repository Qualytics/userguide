# Fabric Analytics

Adding and configuring a Fabric Analytics connection within Qualytics empowers the platform to build a symbolic link with your Microsoft Fabric SQL Analytics endpoint to perform operations like data discovery, visualization, reporting, cataloging, profiling, scanning, anomaly surveillance, and more.

This documentation provides a step-by-step guide on adding Fabric Analytics as a source datastore in Qualytics. It covers the entire process, from initial connection setup to testing and finalizing the configuration.

By following these instructions, enterprises can ensure their Microsoft Fabric environment is properly connected with Qualytics, unlocking the platform's potential to help you proactively manage your full data quality lifecycle.

Let's get started 🚀

## Fabric Analytics Setup Guide

Fabric Analytics connects to Microsoft Fabric's **SQL Analytics Endpoint**, which exposes a read-only T-SQL interface over your Fabric Lakehouse or Warehouse data. Unlike traditional username/password authentication, Fabric Analytics uses **Azure Active Directory (AAD) Service Principal** credentials for secure, token-based authentication.

!!! warning
    Fabric Analytics is a **read-only** connector. It does not support enrichment (write-back) operations. You will need to use a different connector type as your enrichment datastore.

### Prerequisites

Before configuring the connector in Qualytics, ensure you have the following:

| # | Requirement | Details |
| :---- | :---- | :---- |
| 1. | Microsoft Fabric Workspace | A Fabric Workspace with an active capacity (F2 or higher). |
| 2. | Lakehouse or Warehouse | A Lakehouse or Warehouse created in your workspace. |
| 3. | SQL Analytics Endpoint URL | Found in the Fabric portal under your Lakehouse/Warehouse settings. Format: `<workspace-guid>.datawarehouse.fabric.microsoft.com`. |
| 4. | Azure Entra ID App Registration | A Service Principal with a **Client ID**, **Client Secret**, and **Tenant ID**. |
| 5. | Workspace Access | The Service Principal must be added to the Fabric Workspace with at least **Contributor** role. |
| 6. | Tenant Setting | A Fabric Admin must enable **"Service principals can use Fabric APIs"** in the Fabric Admin Portal under Tenant settings → Developer settings. |

### Retrieve Connection Details

**SQL Analytics Endpoint:**

1. Go to the [Microsoft Fabric portal](https://app.fabric.microsoft.com){:target="_blank"}.
2. Open your **Workspace** and select the **Lakehouse** or **Warehouse**.
3. Navigate to the **Settings** and locate the **SQL analytics endpoint** URL (e.g., `<workspace-guid>.datawarehouse.fabric.microsoft.com`).

**Service Principal Credentials:**

1. Go to the [Azure Portal](https://portal.azure.com){:target="_blank"} and navigate to **Microsoft Entra ID** → **App registrations**.
2. Select your app registration (or create a new one).
3. From the **Overview** page, copy the **Application (client) ID** and **Directory (tenant) ID**.
4. Under **Certificates & secrets**, create a new client secret and copy the **Value** immediately — it is only shown once.
5. In the Fabric portal, go to your workspace → **Manage access** → add the service principal with at least **Contributor** role.

## Add the Source Datastore

A source datastore is a storage location used to connect to and access data from external sources. Fabric Analytics is an example of such a datastore, specifically a type of JDBC datastore that supports connectivity through the JDBC API. Configuring the Fabric Analytics datastore allows the Qualytics platform to access and perform operations on the data, thereby generating valuable insights.

**Step 1**: Log in to your Qualytics account and click on the **Add Source Datastore** button located at the top-right corner of the interface.

![add-datastore](../assets/datastores/fabric-analytics/add-datastore-light.png)

**Step 2**: A modal window - **Add Datastore** will appear, providing you with the options to connect a datastore.

![select-a-connector](../assets/datastores/fabric-analytics/select-a-connector-light.png)

| REF. | FIELDS  | ACTIONS |
| :---- | :---- | :---- |
| 1. | Name (Required) | Specify the name of the datastore (e.g., the specified name will appear on the datastore cards). |
| 2. | Toggle Button | Toggle **ON** to create a new source datastore from scratch, or toggle **OFF** to reuse credentials from an existing connection. |
| 3. | Connector (Required) | Select **Fabric Analytics** from the dropdown list. |

### Option I: Create a Datastore with a new Connection

If the toggle for **Add New Connection** is turned on, then this will prompt you to add and configure the source datastore from scratch without using existing connection details.

**Step 1**: Select the **Fabric Analytics** connector from the dropdown list and add connection details such as Secret Management, host, port, client ID, client secret, tenant ID, and database.

![add-datastore-credentials](../assets/datastores/fabric-analytics/add-datastore-credentials-light.png)

**Secrets Management**: This is an optional connection property that allows you to securely store and manage credentials by integrating with HashiCorp Vault and other secret management systems. Toggle it **ON** to enable Vault integration for managing secrets.

!!! note
    After configuring **HashiCorp Vault** integration, you can use ${key} in any Connection property to reference a key from the configured Vault secret. Each time the Connection is initiated, the corresponding secret value will be retrieved dynamically.

| REF. | FIELDS | ACTIONS |
| :---- | :---- | :---- |
| 1. | Login URL | Enter the URL used to authenticate with HashiCorp Vault. |
| 2. | Credentials Payload | Input a valid JSON containing credentials for Vault authentication. |
| 3. | Token JSONPath | Specify the JSONPath to retrieve the client authentication token from the response (e.g., $.auth.client_token). |
| 4. | Secret URL | Enter the URL where the secret is stored in Vault. |
| 5. | Token Header Name | Set the header name used for the authentication token (e.g., X-Vault-Token). |
| 6. | Data JSONPath | Specify the JSONPath to retrieve the secret data (e.g., $.data). |

![hashcorp-explain](../assets/datastores/fabric-analytics/hashcorp-explain-light.png)

**Step 2**: The configuration form will expand, requesting credential details before establishing the connection.

![add-datastore-credentials-explain](../assets/datastores/fabric-analytics/add-datastore-credentials-explain-light.png)

| REF. | FIELDS | ACTIONS |
| :---- | :---- | :---- |
| 1. | Host (Required) | Enter the **SQL Analytics Endpoint** URL from your Fabric Lakehouse or Warehouse (e.g., `<workspace-guid>.datawarehouse.fabric.microsoft.com`). |
| 2. | Port (Optional) | Specify the **Port** number. The default is `1433`. |
| 3. | Client ID (Required) | Enter the **Application (client) ID** from your Azure Entra ID App Registration. |
| 4. | Client Secret (Required) | Enter the **Client Secret** value from your Azure Entra ID App Registration. |
| 5. | Tenant ID (Required) | Enter the **Directory (tenant) ID** from your Azure Entra ID App Registration. |
| 6. | Database (Required) | Specify the database name (your Lakehouse or Warehouse name in Fabric). |
| 7. | Schema (Required) | Define the schema within the database that should be used (default: `dbo`). |
| 8. | Teams (Required) | Select one or more teams from the dropdown to associate with this source datastore. |
| 9. | Initiate Cataloging (Optional) | Tick the checkbox to automatically perform catalog operation on the configured source datastore to gather data structures and corresponding metadata. |

**Step 3**: After adding the source datastore details, click on the **Test Connection** button to check and verify its connection.

![test-datastore-connection](../assets/datastores/fabric-analytics/test-datastore-connection-light.png)

If the credentials and provided details are verified, a success message will be displayed indicating that the connection has been verified.

### Option II: Use an Existing Connection

If the toggle for **Add new connection** is turned off, then this will prompt you to configure the source datastore using the existing connection details.

**Step 1**: Select a **connection** to reuse existing credentials.

![use-existing-datastore](../assets/datastores/fabric-analytics/use-existing-datastore-light.png)

!!! note
    If you are using existing credentials, you can only edit the details such as Database, Schema, Teams, and Initiate Cataloging.

**Step 2**: Click on the **Test Connection** button to verify the existing connection details. If connection details are verified, a success message will be displayed.

![test-connection-for-existing-datastore](../assets/datastores/fabric-analytics/test-connection-for-existing-datastore-light.png)

!!! note
    Clicking on the **Finish** button will create the source datastore and bypass the **enrichment datastore** configuration step.

!!! tip
    It is recommended to click on the **Next** button, which will take you to the **enrichment datastore** configuration page.

## Add Enrichment Datastore

After successfully testing and verifying your source datastore connection, you have the option to add an enrichment datastore (recommended). This datastore is used to store analyzed results, including any anomalies and additional metadata in tables. This setup provides comprehensive visibility into your data quality, enabling you to manage and improve it effectively.

!!! warning
    Qualytics does not support the Fabric Analytics connector as an enrichment datastore, but you can point to a different enrichment datastore.

**Step 1**: Whether you have added a source datastore by creating a new datastore connection or using an existing connection, click on the **Next** button to start adding the **Enrichment Datastore**.

![next-button-for-enrichment](../assets/datastores/fabric-analytics/next-button-for-enrichment-light.png)

**Step 2**: A modal window - **Link Enrichment Datastore** will appear, providing you with the options to configure an **enrichment datastore**.

![select-enrichment-connector](../assets/datastores/fabric-analytics/select-enrichment-connector-light.png)

| REF. | FIELDS | ACTIONS |
| :---- | :---- | :---- |
| 1. | Prefix (Required) | Add a prefix name to uniquely identify tables/files when Qualytics writes metadata from the source datastore to your enrichment datastore. |
| 2. | Caret Down Button | Click the caret down to select either **Use Enrichment Datastore** or **Add Enrichment Datastore**. |
| 3. | Enrichment Datastore | Select an enrichment datastore from the dropdown list. |

### Option I: Create an Enrichment Datastore with a new Connection

If the toggle **Add new connection** is turned on, then this will prompt you to add and configure the enrichment datastore from scratch without using an existing enrichment datastore and its connection details.

**Step 1**: Click on the caret button and select **Add Enrichment Datastore**.

![add-enrichment-datastore](../assets/datastores/fabric-analytics/add-enrichment-datastore-light.png)

A modal window **Link Enrichment Datastore** will appear. Enter the following details to create an enrichment datastore with a new connection.

![add-enrichment-details](../assets/datastores/fabric-analytics/add-enrichment-details-light.png)

| REF. | FIELDS | ACTIONS |
| :---- | :---- | :---- |
| 1. | Prefix | Add a prefix name to uniquely identify tables/files when Qualytics writes metadata from the source datastore to your enrichment datastore. |
| 2. | Name | Give a name for the enrichment datastore. |
| 3. | Toggle Button for Add New Connection  | Toggle ON to create a new enrichment datastore from scratch or toggle OFF to reuse credentials from an existing connection. |
| 4. | Connector | Select a datastore connector from the dropdown list. |

**Step 2**: Add connection details for your selected **enrichment datastore** connector.

![enrichment-datastore-connector](../assets/datastores/fabric-analytics/enrichment-datastore-connector-light.png)

**Step 3**: Click on the **Test Connection** button to verify the selected enrichment datastore connection. If the connection is verified, a flash message will indicate that the connection with the datastore has been successfully verified.

![test-connection-for-enrichment-datastore](../assets/datastores/fabric-analytics/test-connection-for-enrichment-datastore-light.png)

**Step 4**: Click on the **Finish** button to complete the configuration process.

![finish-configuration](../assets/datastores/fabric-analytics/finish-configuration-light.png)

When the configuration process is finished, a modal will display a success message indicating that your datastore has been successfully added.

**Step 5**: Close the Success dialog and the page will automatically redirect you to the **Source Datastore Details** page where you can perform data operations on your configured **source datastore**.

![data-operation-page](../assets/datastores/fabric-analytics/data-operation-page-light.png)

### Option II: Use an Existing Connection

If the **Use enrichment datastore** option is selected from the caret button, you will be prompted to configure the datastore using existing connection details.

**Step 1**: Click on the caret button and select **Use Enrichment Datastore**.

![use-enrichment-datastore](../assets/datastores/fabric-analytics/use-enrichment-datastore-light.png)

**Step 2**: A modal window **Link Enrichment Datastore** will appear. Add a prefix name and select an existing enrichment datastore from the dropdown list.

![link-enrichment-datastore](../assets/datastores/fabric-analytics/link-enrichment-datastore-light.png)

| REF. | FIELDS | ACTIONS |
| :---- | :---- | :---- |
| 1. | Prefix (Required) | Add a prefix name to uniquely identify tables/files when Qualytics writes metadata from the source datastore to your enrichment datastore. |
| 2. | Enrichment Datastore | Select an enrichment datastore from the dropdown list. |

**Step 3**: After selecting an existing **enrichment datastore** connection, you will view the following details related to the selected enrichment:

* **Teams**: The team associated with managing the enrichment datastore is based on the role of public or private. Example - Marked as **Public** means that this datastore is accessible to all the users.

* **Host**: This is the server address where the enrichment datastore instance is hosted. It is the endpoint used to connect to the enrichment datastore environment.

* **Database**: Refers to the specific database within the enrichment datastore environment where the data is stored.

* **Schema**: The schema used in the enrichment datastore. The schema is a logical grouping of database objects (tables, views, etc.). Each schema belongs to a single database.

![use-existing-enrichment-datastore](../assets/datastores/fabric-analytics/use-existing-enrichment-datastore-light.png)

**Step 4**: Click on the **Finish** button to complete the configuration process for the existing **enrichment datastore**.

![finish-configuration-existing](../assets/datastores/fabric-analytics/finish-configuration-existing-light.png)

When the configuration process is finished, a modal will display a success message indicating that your data has been successfully added.

Close the success message and you will be automatically redirected to the **Source Datastore Details** page where you can perform data operations on your configured **source datastore**.

![data-operation-page-2](../assets/datastores/fabric-analytics/data-operation-page-2-light.png)

## API Payload Examples

This section provides detailed examples of API payloads to guide you through the process of creating and managing datastores using Qualytics API.

Each example includes endpoint details, sample payloads, and instructions on how to replace placeholder values with actual data relevant to your setup.

### Creating a Source Datastore

This section provides sample payloads for creating a Fabric Analytics datastore. Replace the placeholder values with actual data relevant to your setup.

**Endpoint:** `/api/datastores (post)`

=== "Create a Source Datastore with a new Connection"
    ```json
    {
        "name": "your_datastore_name",
        "teams": ["Public"],
        "database": "fabric_database",
        "schema": "dbo",
        "enrich_only": false,
        "trigger_catalog": true,
        "connection": {
            "name": "your_connection_name",
            "type": "fabric_analytics",
            "host": "your-workspace-guid.datawarehouse.fabric.microsoft.com",
            "port": "1433",
            "username": "your_client_id",
            "password": "your_client_secret",
            "parameters": {
                "tenant_id": "your_tenant_id"
            }
        }
    }
    ```
=== "Create a Source Datastore with an existing Connection"
    ```json
    {
        "name": "your_datastore_name",
        "teams": ["Public"],
        "database": "fabric_database",
        "schema": "dbo",
        "enrich_only": false,
        "trigger_catalog": true,
        "connection_id": connection_id
    }
    ```

### Linking Datastore to an Enrichment Datastore

Use the provided endpoint to link an enrichment datastore to a source datastore:

**Endpoint Details:** `/api/datastores/{datastore-id}/enrichment/{enrichment-id} (patch)`
