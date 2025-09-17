# Amazon S3

Adding and configuring an Amazon S3 connection within Qualytics empowers the platform to build a symbolic link with your file system to perform operations like data discovery, visualization, reporting, cataloging, profiling, scanning, anomaly surveillance, and more.

This documentation provides a step-by-step guide on how to add Amazon S3 as both a source and enrichment datastore in Qualytics. It covers the entire process, from initial connection setup to testing and finalizing the configuration.

By following these instructions, enterprises can ensure their Amazon S3 environment is properly connected with Qualytics, unlocking the platform's potential to help you proactively manage your full data quality lifecycle.

Let’s get started 🚀

## Amazon S3 Setup Guide

This section provides a simple walkthrough for setting up Amazon S3, including retrieving URIs. It also explains how to retrieve the Access Key and Secret Key to configure datastore permissions.

By following the Amazon S3 setup process, you will ensure secure and efficient access to your stored data, allowing seamless datastore integration and proper access management in Qualytics.

### Retrieve the URI

The S3 URI is the unique resource identifier within the context of the S3 protocol. They follow this naming convention: `S3://bucket-name/key-name`

To retrieve the URL of an S3 object via the AWS Console, follow these steps:

1. Navigate to the **AWS S3 console** and click on your bucket's name (use the search input to find the object if necessary).
2. Click on the **checkbox** next to the object's name
3. Click on the **Copy S3 URI** button

![retrieve-the-uri](../assets/datastores/amazon-s3/retrieve-the-uri.png)

### Retrieve the Access Key and Secret Key

The access keys are long-term credentials for an IAM user or the AWS account root user. You can use these keys to sign programmatic requests to the AWS CLI or AWS API (directly or using the AWS SDK).

To retrieve the Access Key and Secret Access Key, follow these steps:

1. Open the **IAM console**.
2. From the navigation menu, click on the **Users**.
3. Select your **IAM user name**.
4. Click on the **User Actions**, and then click on the **Manage Access Keys**.
5. Click on the **Create Access Key**.
6. Your keys will look something like this:
    7. Access key ID example: `AKIAIOSFODNN7EXAMPLE`.
    8. Secret access key example: `wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY`.
9. Click on the **Download Credentials**, and store the keys in a secure location.

!!! warning
    Your Secret Access Key will be visible only once at the time of creation. Please ensure you copy and securely store it for future use.

### Datastore Privileges

If you are using a private bucket, authentication is required for the connection.

#### Source Datastore Permissions (Read-Only)

To create a policy, follow these steps:

1. Open the **IAM console**.
2. Navigate to **Policies** in the IAM dashboard and select **Create Policy**.
3. Go to the **JSON** tab and paste the provided **JSON** into the **Policy editor**.

!!! tip
    Ensure you replace `<bucket/path>` with your specific resource.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:ListBucket",
                "s3:ListBucketMultipartUploads",
                "s3:Get*"
            ],
            "Resource": [
                "arn:aws:s3:::<bucket>/*",
                "arn:aws:s3:::<bucket>"
            ]
        }
    ]
}
```
!!! warning
    Currently, object-level permissions alone are insufficient to authenticate the connection. Please ensure you also include bucket-level permissions as demonstrated in the example above.

#### Enrichment Datastore Permissions (Read-Write)

To create a policy, follow these steps:

1. Open the IAM console.
2. Navigate to **Policies** in the IAM dashboard and select **Create Policy**.
3. Go to the **JSON tab** and paste the provided **JSON** into the **Policy editor**.

!!! tip
    Ensure you replace `<bucket/path>` with your specific resource.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:Get*",
                "s3:ListBucket",
                "s3:ListBucketMultipartUploads",
                "s3:PutObject",
                "s3:DeleteObject",
                "s3:AbortMultipartUpload",
                "s3:ListMultipartUploadParts"
            ],
            "Resource": [
                "arn:aws:s3:::<bucket>/*",
                "arn:aws:s3:::<bucket>"
            ]
        }
    ]
}
```
!!! warning
    Currently, object-level permissions alone are insufficient to authenticate the connection. Please ensure you also include bucket-level permissions as demonstrated in the example above.

## Add a Source Datastore

A source datastore is a storage location used to connect and access data from external sources. Amazon S3 is an example of a source datastore, specifically a type of Distributed File System (DFS) datastore that is designed to handle data stored in distributed file systems. Configuring a DFS datastore enables the Qualytics platform to access and perform operations on the data, thereby generating valuable insights.

**Step 1**: Log in to your Qualytics account and click on the **Add Source Datastore** button located at the top-right corner of the interface.

![add-datastore](../assets/datastores/amazon-s3/add-datastore-light.png)

**Step 2**: A modal window - **Add Datastore** will appear, providing you with the options to connect a datastore.

![select-a-connector](../assets/datastores/amazon-s3/select-a-connector-light.png)

| REF. | FIELDS       | ACTIONS                                                                                           |
|------|--------------|---------------------------------------------------------------------------------------------------|
| 1.  | Name (Required)         | Specify the name of the datastore (e.g., The specified name will appear on the datastore cards.). |
| 2.  | Toggle Button| Toggle **ON** to create a new source datastore from scratch or toggle **OFF** to reuse credentials from an existing connection. |
| 3.  | Connector (Required)    | Select **Amazon S3** from the dropdown list. |

### Option I: Create a Source Datastore with a new Connection

If the toggle for **Add New connection** is turned on, then this will prompt you to add and configure the source datastore from scratch without using existing connection details.

**Step 1**: Select the **Amazon S3** connector from the dropdown list and add connection details such as Secrets Management, URI, access key, secret key, root path, and teams.

![add-datastore-credentials](../assets/datastores/amazon-s3/add-datastore-credentials-light.png)

**Secrets Management**: This is an optional connection property that allows you to securely store and manage credentials by integrating with HashiCorp Vault and other secret management systems. Toggle it **ON** to enable Vault integration for managing secrets.

!!! note
    After configuring **HashiCorp Vault** integration, you can use ${key} in any Connection property to reference a key from the configured Vault secret. Each time the Connection is initiated, the corresponding secret value will be retrieved dynamically.

| REF. | FIELDS               | ACTIONS                                                                 |
|-----|----------------------|-------------------------------------------------------------------------|
| 1.  | Login URL            | Enter the URL used to authenticate with HashiCorp Vault.                |
| 2.  | Credentials Payload  | Input a valid JSON containing credentials for Vault authentication.     |
| 3.  | Token JSONPath       | Specify the JSONPath to retrieve the client authentication token from the response (e.g., $.auth.client_token). |
| 4.  | Secret URL           | Enter the URL where the secret is stored in Vault.                      |
| 5.  | Token Header Name    | Set the header name used for the authentication token (e.g., X-Vault-Token). |
| 6.  | Data JSONPath        | Specify the JSONPath to retrieve the secret data (e.g., $.data).        |

![secret-management](../assets/datastores/amazon-s3/secret-management-light-04.png)

**Step 2**: The configuration form will expand, requesting credential details before establishing the connection.

![add-datastore-credentials-explain](../assets/datastores/amazon-s3/add-datastore-credentials-explain-light.png)

| REF. | FIELDS           | ACTIONS                                                                                       |
|------|------------------|-----------------------------------------------------------------------------------------------|
| 1.  | URI (Required)             | Enter the Uniform Resource Identifier (URI) of Amazon S3.                                  |
| 2.  | Access Key (Required)      | Input the access key provided for secure access.                                               |
| 3.  | Secret Key (Required)      | Input the secret key associated with the access key for secure authentication.                 |
| 4.  | Root Path (Required)       | Specify the root path where the data is stored.                                                |
| 5.  | Teams (Required)          | Select one or more teams from the dropdown to associate with this source datastore.            |
| 6.  | Initiate Cataloging (Optional)| Check the checkbox to automatically perform a catalog operation on the configured source datastore to gather data structures and corresponding metadata. |

**Step 3**: After adding the source datastore details, click on the **Test Connection** button to check and verify its connection.

![test-datastore-connection](../assets/datastores/amazon-s3/test-datastore-connection-light.png)

If the credentials and provided details are verified, a success message will be displayed indicating that the connection has been verified.

### Option II: Use an Existing Connection

If the toggle for **Add New connection** is turned off, then this will prompt you to configure the source datastore using the existing connection details.

**Step 1**: Select a **connection** to reuse existing credentials.

![use-existing-datastore](../assets/datastores/amazon-s3/use-existing-datastore-light.png)

!!! note
    If you are using existing credentials, you can only edit the details such as Root Path, Teams, and initiate Cataloging.

**Step 2**: Click on the **Test Connection** button to check and verify the source data connection. If connection details are verified, a success message will be displayed.

![test-connection-for-existing-datastore](../assets/datastores/amazon-s3/test-datastore-connection-light.png)

!!! note
    Clicking on the **Finish** button will create the source datastore and bypass the **enrichment datastore** configuration step.

!!!tip
    It is recommended to click on the **Next** button, which will take you to the **enrichment datastore** configuration page.

## Add Enrichment Datastore

Once you have successfully tested and verified your source datastore connection, you have the option to add the enrichment datastore (recommended). This datastore is used to store the analyzed results, including any anomalies and additional metadata in files. This setup provides full visibility into your data quality, helping you manage and improve it effectively.

**Step 1**: Whether you have added a source datastore by creating a new datastore connection or using an existing connection, click on the **Next** button to start adding the **Enrichment Datastore**.

![next-button-for-enrichment](../assets/datastores/amazon-s3/next-button-for-enrichment-light.png)

**Step 2**: A modal window - Link Enrichment Datastore will appear, providing you with the options to configure an enrichment datastore.

![select-enrichment-connector](../assets/datastores/amazon-s3/select-enrichment-connector-light.png)

| REF.              | FIELDS       | ACTIONS                                    |
|-------------------|--------------|--------------------------------------------|
| 1.                | Prefix       | Add a prefix name to uniquely identify tables/files when Qualytics writes metadata from the source datastore to your enrichment datastore. |
| 2.                | Caret Down Button   | Click the caret down to select either **Use Enrichment Datastore** or **Add Enrichment Datastore**.|
| 3.                | Enrichment Datastore         | Select an enrichment datastore from the dropdown list. |

### Option I: Create an Enrichment Datastore with a new Connection

If the toggle for **Add New connection is turned on**, then this will prompt you to add and configure the enrichment datastore from scratch without using an existing enrichment datastore and its connection details.

**Step 1**: Click on the caret button and select Add Enrichment Datastore.

![select-enrichment](../assets/datastores/amazon-s3/select-enrichment-light-10.png)

A modal window **Link Enrichment Datastore** will appear. Enter the following details to create an enrichment datastore with a new connection

![enrichment-detail](../assets/datastores/amazon-s3/enrichment-details-light-11.png)

| REF.              | FIELDS       | ACTIONS                                    |
|-------------------|--------------|--------------------------------------------|
| 1.                | Prefix       | Add a prefix name to uniquely identify tables/files when Qualytics writes metadata from the source datastore to your enrichment datastore. |
| 2.                | Name   | Give a name for the enrichment datastore.|
| 3.                |Toggle Button for add new connection | Toggle ON to create a new enrichment from scratch or toggle OFF to reuse credentials from an existing connection. |
| 4.                |Connector | Select a datastore connector from the dropdown list.|

**Step 2**: Add connection details for your selected **enrichment datastore** connector.

![enrichment-datastore-explain](../assets/datastores/amazon-s3/enrichment-datastore-explain-light.png)

| REF. | FIELDS         | ACTIONS                                                                 |
|------|----------------|-------------------------------------------------------------------------|
| 1.   | URI (Required)           | Enter the Uniform Resource Identifier (URI) for the Amazon S3. |
| 2.   | Access Key (Required)    | Input the access key provided for secure access. |
| 3.   | Secret Key (Required)    | Input the secret key associated with the access key for secure authentication. |
| 4.   | Root Path (Required)     | Specify the root path where the data is stored. |
| 5.   | Teams (Required)         | Select one or more teams from the dropdown to associate with this source datastore. |

**Step 3**: Click on the **Test Connection** button to verify the selected enrichment datastore connection. If the connection is verified, a flash message will indicate that the connection with the datastore has been successfully verified.

![test-connection-for-enrichment-datastore](../assets/datastores/amazon-s3/test-connection-for-enrichment-datastore-light.png)

**Step 4**: Click on the **Finish** button to complete the configuration process.

![finish-configuration](../assets/datastores/amazon-s3/finish-configuration-light.png)

When the configuration process is finished, a modal will display a success message indicating that your datastore has been successfully added.

**Step 5**: Close the Success dialog and the page will automatically redirect you to the **Source Datastore Details** page where you can perform data operations on your configured **source datastore**.

![data-operation-page](../assets/datastores/amazon-s3/data-operation-page-light.png)

### Option II: Use an Existing Connection

If the toggle for **Use an existing enrichment datastore** is turned on, you will be prompted to configure the enrichment datastore using existing connection details.

**Step 1**: Click on the caret button and select **Use Enrichment Datastore**.

![select-enrichment-details](../assets/datastores/amazon-s3/select-enrichment-light-17.png)

**Step 2**: A modal window **Link Enrichment Datastore** will appear. Add a prefix name and select an existing enrichment datastore from the dropdown list.

![add-enrichment-details](../assets/datastores/amazon-s3/add-enrichment-details-light-18.png)

| REF.              | FIELDS       | ACTIONS                                    |
|-------------------|--------------|--------------------------------------------|
| 1.                | Prefix       | Add a prefix name to uniquely identify tables/files when Qualytics writes metadata from the source datastore to your enrichment datastore. |
| 2.                | Enrichment Datastore  | Select an enrichment datastore from the dropdown list. |

**Step 3**: After selecting an existing **enrichment datastore** connection, you will view the following details related to the selected enrichment:

-   **Teams**: The team associated with managing the enrichment datastore is based on the role of public or private. Example - Marked as **Public** means that this datastore is accessible to all the users.

-   **URI**: The Uniform Resource Identifier (URI) points to the specific location of the source data and should be formatted accordingly (e.g., ```s3://bucket-name``` for Amazon S3).

-   **Root Path**: Specify the root path where the data is stored. This path defines the base directory or folder from which all data operations will be performed.

![use-existing-enrichment-datastore](../assets/datastores/amazon-s3/use-existing-enrichment-datastore-light.png)

**Step 4**: Click on the **Finish** button to complete the configuration process for the existing **enrichment datastore**.

![finish-configuration-for-existing-enrichment-datastore](../assets/datastores/amazon-s3/finish-configuration-for-existing-enrichment-datastore-light.png)

When the configuration process is finished, a modal will display a success message indicating that your datastore has been successfully added.

Close the success message and you will be automatically redirected to the **Source Datastore Details** page where you can perform data operations on your configured **source datastore**.

![data-operation-page](../assets/datastores/amazon-s3/data-operation-page-light.png)

## API Payload Examples

This section provides detailed examples of API payloads to guide you through the process of creating and managing datastores using Qualytics API. Each example includes endpoint details, sample payloads, and instructions on how to replace placeholder values with actual data relevant to your setup.

### Creating a Source Datastore

This section provides sample payloads for creating the Amazon S3 datastore. Replace the placeholder values with actual data relevant to your setup.

**Endpoint:** ```/api/datastores (post)```

=== "Create a Source Datastore with a new Connection"
    ```json
    {
        "name": "your_datastore_name",
        "teams": ["Public"],
        "trigger_catalog": true,
        "root_path": "/s3_root_path",
        "enrich_only": false,
        "connection": {
            "name": "your_connection_name",
            "type": "s3",
            "uri": "s3://<bucket_name>",
            "access_key": "s3_access_key",
            "secret_key": "s3_secret_key"
        }
    }
    ```
=== "Create a Source Datastore with an existing Connection"
    ```json
    {
        "name": "your_datastore_name",
        "teams": ["Public"],
        "trigger_catalog": true,
        "root_path": "/s3_root_path",
        "enrich_only": false,
        "connection_id": connection-id
    }
    ```

### Creating an Enrichment Datastore

This section provides sample payloads for creating an enrichment datastore. Replace the placeholder values with actual data relevant to your setup.

**Endpoint:** ```/api/datastores (post)```

=== "Create an Enrichment Datastore with a new Connection"
    ```json
    {
        "name": "your_datastore_name",
        "teams": ["Public"],
        "trigger_catalog": true,
        "root_path": "/s3_root_path",
        "enrich_only": true,
        "connection": {
            "name": "your_connection_name",
            "type": "s3",
            "uri": "s3://<bucket_name>",
            "access_key": "s3_access_key",
            "secret_key": "s3_secret_key"
        }
    }
    ```
=== "Create an Enrichment Datastore with an existing Connection"
    ```json
    {
        "name": "your_datastore_name",
        "teams": ["Public"],
        "trigger_catalog": true,
        "root_path": "/s3_root_path",
        "enrich_only": true,
        "connection_id": connection-id
    }
    ```

### Link an Enrichment Datastore to a Source Datastore
Use the provided endpoint to link an enrichment datastore to a source datastore:

**Endpoint Details:** ```/api/datastores/{datastore-id}/enrichment/{enrichment-id} (patch)```
