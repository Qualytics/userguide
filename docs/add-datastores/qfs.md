# Qualytics File System (QFS)

Configuring a Qualytics File System (QFS) datastore provides a managed solution for users who prefer not to set up or maintain their own datastores.

QFS allows seamless integration with the Qualytics platform, enabling users to upload files in supported formats, such as Excel, CSV, and JSON, directly through the user interface. This functionality is ideal for organizations seeking a hassle-free approach to store and analyze data without additional infrastructure setup.

This guide offers a step-by-step walkthrough for utilizing the QFS datastore, ensuring a smooth process for uploading, managing, and analyzing Qualytics-readable files within the platform.

Let’s get started 🚀

## Add a Source Datastore 

A Qualytics File System (QFS) datastore serves as a managed storage solution for users who prefer to avoid the complexity of setting up and maintaining their own datastores. QFS is designed to seamlessly integrate with the Qualytics platform, enabling efficient storage and analysis of data.

**Step 1:** Log in to your Qualytics account and click on the **Add Source Datastore** button located at the top-right corner of the interface.

![add-datastore](../assets/datastores/qfs/add-datastore-light.png#only-light)
![add-datastore](../assets/datastores/qfs/add-datastore-dark.png#only-dark)

**Step 2:** A modal window- **Add Datastore** will appear, providing you with the options to connect a datastore.

![source-datastore](../assets/datastores/qfs/source-datastore-light.png#only-light)
![source-datastore](../assets/datastores/qfs/source-datastore-dark.png#only-dark)

| REF. | FIELDS | ACTION |
| :---- | :---- | :---- |
| 1. | Name (Required) | Specify the name of the datastore. Example: The specified name will appear on the datastore cards. |
| 2. | Toggle Button | Toggle **ON** to create a new source datastore from scratch, or toggle **OFF** to reuse credentials from an existing connection. |
| 3. | Connector (Required) | Select **Qualytics File System (QFS)** from the dropedown list. |

### Option I: Create a Source Datastore with a new Connection

If the toggle for **Add New connection** is turned on, then this will prompt you to add and configure the source datastore from scratch without using existing connection details.

**Step 1:** Select the **Qualytics File System (QFS)** connector from the dropdown list and add connection details such as Secrets Management, URI, account name, access key, root path, and teams.

![add-connection](../assets/datastores/qfs/add-connection-light.png#only-light)
![add-connection](../assets/datastores/qfs/add-connection-dark.png#only-dark)

**Secrets Management**: This is an optional connection property that allows you to securely store and manage credentials by integrating with HashCorp Vault and other secret management systems. Toggle it **ON** to enable Vault integration for managing secrets.

!!! note
    After configuring HashCorp Vault integration, you can use ${key} in any Connection property to reference a key from the configured Vault secret. Each time the Connection is initiated, the corresponding secret value will be retrieved dynamically. 


| REF. | FIELDS | ACTIONS |
| :---- | :---- | :---- |
| 1. | Login URL | Enter the URL used to authenticates with HashCrops Vault. |
| 2. | Credentials Payload | Input a valid JSON containing credentials for Vaults authentication. |
| 3. | Token JSONPath | Specify the JSONPath to retrieve the client authentication token from the response (e.g., $.auth.client_token). |
| 4. | Secret URL | Enter the URL where the secret is stored in Vault. |
| 5. | Token Header Name | Set the header name used for the authentication token (e.g., X-Vault-Token). |
| 6. | Data JSONPath | Specify the JSONPath to retrieve the secret data (e.g., $.data).  |

![secrets-management](../assets/datastores/qfs/secrets-management-light.png#only-light)
![secrets-management](../assets/datastores/qfs/secrets-management-dark.png#only-dark)

**Step 2:** The configuration form will expand, requesting credential details before establishing the connection.

![datastore-properties](../assets/datastores/qfs/datastore-properties-light.png#only-light)
![datastore-properties](../assets/datastores/qfs/datastore-properties-dark.png#only-dark)

| REF. | FIELDS | ACTIONS |
| :---- | :---- | :---- |
| 1. | Root Path (Required) | Specify the root path where the data is stored. |
| 2. | Team (Required) | Select one or more teams from the dropdown to associate with this source datastore. |
| 3. | Initiate Cataloging (Optional) | Tick the checkbox to automatically perform catalog operation on the configured source datastore to gather data structures and corresponding metadata. |

**Step 3:** After adding the source datastore details, click on the **Test Connection** button to check and verify its connection.

![test](../assets/datastores/qfs/test-light.png#only-light)
![test](../assets/datastores/qfs/test-dark.png#only-dark)

If the credentials and provided details are verified, a success message will be displayed indicating that the connection has been verified.

### Option II: Use an Existing Connection

If the toggle for **Add New connection** is turned off, then this will prompt you to configure the source datastore using the existing connection details.

**Step 1:** Select a **connection** to reuse existing credentials.

![existing-credential](../assets/datastores/qfs/existing-credential-light.png#only-light)
![existing-credential](../assets/datastores/qfs/existing-credential-dark.png#only-dark)

!!! note
    If you are using existing credentials, you can only edit the details such as Root Path, Teams and Initiate Cataloging. |


**Step 2:** Click on the **Test Connection** button to verify the existing connection details. If connection details are verified, a success message will be displayed.

![test-2](../assets/datastores/qfs/test-2-light.png#only-light)
![test-2](../assets/datastores/qfs/test-2-dark.png#only-dark)

!!! note
    Clicking on the Finish button will create the source datastore and bypass the enrichment datastore configuration step.

!!! tip
    It is recommended to click on the Next button, which will take you to the enrichment datastore configuration page. 


## Add Enrichment Datastore

Once you have successfully tested and verified your source datastore connection, you have the option to add the enrichment datastore (recommended). The enrichment datastore is used to store the analyzed results, including any anomalies and additional metadata in files. This setup provides full visibility into your data quality, helping you manage and improve it effectively.

**Step 1:** Whether you have added a source datastore by creating a new datastore connection or using an existing connection, click on the **Next** button to start adding the **Enrichment Datastore**.

![next](../assets/datastores/qfs/next-light.png#only-light)
![next](../assets/datastores/qfs/next-dark.png#only-dark)

**Step 2**: A modal window- **Link Enrichment Datastore** will appear, providing you with the options to configure an **enrichment datastore**.

![link-enrichment-datastore](../assets/datastores/qfs/link-enrichment-datastore-light.png#only-light)
![link-enrichment-datastore](../assets/datastores/qfs/link-enrichment-datastore-dark.png#only-dark)

| REF. | FIELDS | ACTIONS |
| :---- | :---- | :---- |
| 1. | Prefix | Add a prefix name to uniquely identify tables/files when Qualytics writes metadata from the source datastore to your enrichment datastore. |
| 2. | Caret Down Button | Click the caret down to select either **Use Enrichment Datastore** or **Add Enrichment Datastore**. |
| 3. | Enrichment Datastore | Select an enrichment datastore from the dropdown list. |
 
### Option I: Create an Enrichment Datastore with a new Connection

If the toggles for **Add New connection is turned on**, then this will prompt you to add and configure the enrichment datastore from scratch without using an existing enrichment datastore and its connection details.

**Step 1**: Click on the caret button and select Add Enrichment Datastore.

![add-enrichment-datastore](../assets/datastores/qfs/add-enrichment-datastore-light.png#only-light)
![add-enrichment-datastore](../assets/datastores/qfs/add-enrichment-datastore-dark.png#only-dark)

A modal window **Link Enrichment Datastore** will appear. Enter the following details to create an enrichment datastore with a new connection.

![link-enrichment-datastore-2](../assets/datastores/qfs/link-enrichment-datastore-2-light.png#only-light)
![link-enrichment-datastore-2](../assets/datastores/qfs/link-enrichment-datastore-2-dark.png#only-dark)

| REF. | FIELDS | ACTIONS |
| :---- | :---- | :---- |
| 1. | Prefix | Add a prefix name to uniquely identify tables/files when Qualytics writes metadata from the source datastore to your enrichment datastore. |
| 2. | Name  | Give a name for the enrichment datastore. |
| 3. | Toggle Button for add new connection | Toggle ON to create a new enrichment from scratch or toggle OFF to reuse credentials from an existing connection. |
| 4. | Connector |  Select a datastore connector from the dropdown list. |

**Step 2:** Add connection details for your selected **enrichment datastore** connector.

![datastore](../assets/datastores/qfs/datastore-light.png#only-light)
![datastore](../assets/datastores/qfs/datastore-dark.png#only-dark)

| REF. | FIELDS | ACTIONS |
| :---- | :---- | :---- |
| 1. | Root Path (Required) | Specify the root path where the data is stored. |
| 2. | Team (Required) | Select one or more teams from the dropdown to associate with this source datastore. |

**Step 3:** Click on the **Test Connection** button to verify the selected enrichment datastore connection. If the connection is verified, a flash message will indicate that the connection with the datastore has been successfully verified.

![test-3](../assets/datastores/qfs/test-3-light.png#only-light)
![test-3](../assets/datastores/qfs/test-3-dark.png#only-dark)

**Step 4:** Click on the **Finish** button to complete the configuration process

![finish](../assets/datastores/qfs/finish-light.png#only-light)
![finish](../assets/datastores/qfs/finish-dark.png#only-dark)

When the configuration process is finished, a modal will display a **success message** indicating that **your datastore has been successfully added**.

![success](../assets/datastores/qfs/success-light.png#only-light)
![success](../assets/datastores/qfs/success-dark.png#only-dark)

**Step 4:** Close the Success dialog and the page will automatically redirect you to the **Source Datastore Details** page where you can perform data operations on your configured **source datastore**.

![overview](../assets/datastores/qfs/overview-light.png#only-light)
![overview](../assets/datastores/qfs/overview-dark.png#only-dark)

### Option II: Use an Existing Connection

If the toggle for **Use an existing enrichment datastore** is turned on, you will be prompted to configure the enrichment datastore using existing connection details.

**Step 1**: Click on the caret button and select **Use Enrichment Datastore**.

![use-enrichment-datastore](../assets/datastores/qfs/use-enrichment-datastore-light.png#only-light)
![use-enrichment-datastore](../assets/datastores/qfs/use-enrichment-datastore-dark.png#only-dark)

**Step 2**: A modal window **Link Enrichment Datastore** will appear. Add a prefix name and select an existing enrichment datastore from the dropdown list.

![link-enrichment-datastore-3](../assets/datastores/qfs/link-enrichment-datastore-3-light.png#only-light)
![link-enrichment-datastore-3](../assets/datastores/qfs/link-enrichment-datastore-3-dark.png#only-dark)

| REF. | FIELDS | ACTIONS |
| :---- | :---- | :---- |
| 1. | Prefix | Add a prefix name to uniquely identify tables/files when Qualytics writes metadata from the source datastore to your enrichment datastore. |
| 2. | Enrichment Datastore | Select an enrichment datastore from the dropdown list. | 

**Step 3:** After selecting an existing **enrichment datastore** connection, you will view the following details related to the selected enrichment:

- **Teams:** The team associated with managing the enrichment datastore is based on the role of public or private. Example- Marked as **Public** means that this datastore is accessible to all the users.

- **URI:** Uniform Resource Identifier (URI) points to the specific location of the source data and should be formatted accordingly (e.g., `wasbs://storage-url` for Qualytics File System (QFS)).

- **Root Path:** Specify the root path where the data is stored. This path defines the base directory or folder from which all data operations will be performed.

![detail](../assets/datastores/qfs/detail-light.png#only-light)
![detail](../assets/datastores/qfs/detail-dark.png#only-dark)

**Step 4:** Click on the **Finish** button to complete the configuration process for the existing **enrichment datastore**.

![finish-2](../assets/datastores/qfs/finish-2-light.png#only-light)
![finish-2](../assets/datastores/qfs/finish-2-dark.png#only-dark)

When the configuration process is finished, a modal will display a **success message** indicating that **your data has been successfully added**.

![success-2](../assets/datastores/qfs/success-2-light.png#only-light)
![success-2](../assets/datastores/qfs/success-2-dark.png#only-dark)

Close the success message and you will be automatically redirected to the **Source Datastore Details** page where you can perform data operations on your configured **source datastore**.  

![overview-2](../assets/datastores/qfs/overview-2-light.png#only-light)
![overview-2](../assets/datastores/qfs/overview-2-dark.png#only-dark)
