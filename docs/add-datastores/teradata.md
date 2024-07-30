# Teradata

Adding and configuring a Teradata connection within Qualytics empowers the platform to build a symbolic link with your schema to perform operations like data discovery, visualization, reporting, cataloging, profiling, scanning, anomaly surveillance, and more.  

This documentation provides a step-by-step guide on adding Teradata as a source datastore in Qualytics. It covers the entire process, from initial connection setup to testing and finalizing the configuration. 

By following these instructions, enterprises can ensure their Teradata environment is properly connected with Qualytics, unlocking the platform's potential to help you proactively manage your full data quality lifecycle.

Let’s get started 🚀

## Add the Source Datastore

A source datastore is a storage location used to connect to and access data from external sources. Teradata is an example of such a datastore, specifically a type of JDBC datastore that supports connectivity through the JDBC API. Configuring the Teradata datastore allows the Qualytics platform to access and perform operations on the data, thereby generating valuable insights. 

**Step 1**: Log in to your Qualytics account and click on the **Add Source Datastore** button located at the top-right corner of the interface. 

![add-source-teradata](../assets/datastores/teradata/add-source-teradata-light-1.png#only-light)
![add-source-teradata](../assets/datastores/teradata/add-source-teradata-dark-1.png#only-dark)

**Step 2**: A modal window- **Add Datastore** will appear, providing you with the options to connect a datastore.

![add-teradata-connection](../assets/datastores/teradata/add-teradata-connection-light-2.png#only-light)
![add-teradata-connection](../assets/datastores/teradata/add-teradata-connection-dark-2.png#only-dark)

| REF.              | FIELDS       | ACTIONS                                    |
|-------------------|--------------|--------------------------------------------|
| 1.                | Name         | Specify the name of the datastore (e.g., The specified name will appear on the datastore cards) |
| 2.                | Toggle Button    | Toggle **ON** to reuse credentials from an existing connection, or toggle **OFF** to create a new source datastore from scratch. |
| 3.                | Connector        | Select **Teradata** from the dropdown list. | 


### Option I: Create a Datastore with a new Connection

If the toggle for **Use an existing connection** is turned off, then this will prompt you to add and configure the source datastore from scratch without using existing connection details.

**Step 1**: Select the **Teradata** connector from the dropdown list and add connection details such as host, port, username, etc. 

![add-connection-details](../assets/datastores/teradata/add-connection-details-light-3.png#only-light)
![add-connection-details](../assets/datastores/teradata/add-connection-details-dark-3.png#only-dark)

**Step 2**: The configuration form will expand, requesting credential details before establishing the connection.

![enter-teradata-details](../assets/datastores/teradata/enter-teradata-details-light-4.png#only-light)
![enter-teradata-details](../assets/datastores/teradata/enter-teradata-details-dark-4.png#only-dark)

| REF.              | FIELDS                  | ACTIONS                                    |
|-------------------|-------------------------|--------------------------------------------|
| 1.                | Host                    | Get **Hostname** from your Teradata account and add it to this field. |
| 2.                | Port                    | Specify the **Port** number. |
| 3.                | User                    | Enter the **User ID** to connect.|
| 4.                | Password                | Enter the **password** to connect to the database. |
| 5.                | Database                | Specify the database name. |
| 6.                | Teams                   | Select one or more teams from the dropdown to associate with this source datastore. |
| 7.                | Initial Cataloging      | Tick the checkbox to automatically perform catalog operation on the configured source datastore to gather data structures and corresponding metadata.|

**Step 3**: After adding the source datastore details, click on the **Test Connection** button to check and verify its connection.

![test-connection-success](../assets/datastores/teradata/test-connection-success-new-light-5.png#only-light)
![test-connection-success](../assets/datastores/teradata/test-connection-success-new-dark-5.png#only-dark)

If the credentials and provided details are verified, a success message will be displayed indicating that the connection has been verified. 

### Option II: Use an Existing Connection

If the toggle for **Use an existing connection** is turned on, then this will prompt you to configure the source datastore using the existing connection details.

**Step 1**: Select a **connection** to reuse existing credentials. 

![existing-connection](../assets/datastores/teradata/existing-connection-teradata-light-6.png#only-light)
![existing-connection](../assets/datastores/teradata/existing-connection-teradata-dark-6.png#only-dark)

!!! note 
    If you are using existing credentials, you can only edit the details such as Database, Teams, and Initiate Cataloging.

**Step 2**: Click on the **Test Connection** button to check and verify the source data connection. If connection details are verified, a success message will be displayed.

![test-connection-success-existing](../assets/datastores/teradata/test-connection-success-existing-light-7.png#only-light)
![test-connection-success-existing](../assets/datastores/teradata/test-connection-success-existing-dark-7.png#only-dark)
!!! note
    Clicking on the **Finish** button will create the source datastore and bypass the **enrichment datastore** configuration step.


!!! tip
    It is recommended to click on the **Next** button, which will take you to the **enrichment datastore** configuration page.


## Add Enrichment Datastore

After successfully testing and verifying your source datastore connection, you have the option to add an enrichment datastore (recommended). This data store is used to store analyzed results, including. This setup provides comprehensive visibility into your data quality, enabling you to manage and improve it effectively.


!!! warning
    Qualytics does not support the Teradata connector as an enrichment datastore, but you can point to a different connector.

**Step 1**: Whether you have added a source datastore by creating a new datastore connection or using an existing connection, click on the **Next** button to start adding the **Enrichment Datastore**.

![enrichment-next](../assets/datastores/teradata/enrichment-next-light-8.png#only-light)
![enrichment-next](../assets/datastores/teradata/enrichment-next-dark-8.png#only-dark)

**Step 2**: A modal window- **Add Enrichment Datastore** will appear, providing you with the options to configure an **enrichment datastore**.

![add-enrichment-details](../assets/datastores/teradata/add-enrichment-details-light-9.png#only-light)
![add-enrichment-details](../assets/datastores/teradata/add-enrichment-details-dark-9.png#only-dark)

| REF.              | FIELDS                  | ACTIONS                                    |
|-------------------|-------------------------|--------------------------------------------|
| 1.                | Prefix                  | Add a prefix name to uniquely identify tables/files when Qualytics writes metadata from the source datastore to your enrichment datastore. |
| 2.                | Toggle Button for existing enrichment datastore  | Toggle **ON** to link the source datastore to an existing enrichment datastore, or toggle **OFF** to link it to a brand new enrichment datastore. |
| 3.                | Name                    | Give a name for the enrichment datastore.|
| 4.                | Toggle Button for using an existing connection  | Toggle **ON** to reuse credentials from an existing connection, or toggle **OFF** to create a new enrichment from scratch. |
| 5.                | Connector                | Select a datastore connector as **Teradata** from the dropdown list. |

### Option I: Create an Enrichment Datastore with a new Connection

Suppose the toggles for **Use an existing enrichment datastore** and **Use an existing connection** are turned off. In that case, this will prompt you to add and configure the enrichment datastore from scratch without using an existing enrichment datastore and its connection details.

**Step 1**: Add connection details for your selected **enrichment datastore** connector. 

![enrichment-details-added](../assets/datastores/teradata/enrichment-details-added-light-10.png#only-light)
![enrichment-details-added](../assets/datastores/teradata/enrichment-details-added-dark-10.png#only-dark)

!!! note 
    Qualytics does not support Teradata as an enrichment datastore. Instead, you can select a different connector for this purpose. For demonstration purposes, we are using BigQuery as the enrichment datastore. You can use any other JDBC or QDS datastore of your choice for the enrichment datastore configuration.

**Step 2**: Click on the **Test Connection** button to verify the selected enrichment datastore connection. If the connection is verified, a flash message will indicate that the connection with the datastore has been successfully verified.        

If the connection is verified, a flash message will indicate that the connection with the datastore has been successfully verified.        

![test-enrichment-success](../assets/datastores/teradata/test-enrichment-success-light-11.png#only-light)
![test-enrichment-success](../assets/datastores/teradata/test-enrichment-success-dark-11.png#only-dark)

**Step 3**:  Click on the **Finish** button to complete the configuration process. 

![test-enrichment-finish](../assets/datastores/teradata/test-enrichment-finish-light-12.png#only-light)
![test-enrichment-finish](../assets/datastores/teradata/test-enrichment-finish-dark-12.png#only-dark)

When the configuration process is finished, a modal will display a **success message** indicating that **your datastore has been successfully added**.

![success-connection-teradata](../assets/datastores/teradata/success-connection-teradata-light-13.png#only-light)
![success-connection-teradata](../assets/datastores/teradata/success-connection-teradata-dark-13.png#only-dark)

**Step 4**: Close the Success dialogue and the page will automatically redirect you to the **Source Datastore Details** page where you can perform data operations on your configured **source datastore**.

![source-datastore-teradata](../assets/datastores/teradata/source-datastore-teradata-overview-light-14.png#only-light)
![source-datastore-teradata](../assets/datastores/teradata/source-datastore-teradata-overview-dark-14.png#only-dark)

### Option II: Use an Existing Connection

If the toggle for **Use an existing enrichment datastore** is turned on, you will be prompted to configure the enrichment datastore using existing connection details.

!!! note
    Qualytics does not support Teradata as an enrichment datastore. Instead, you can select a different connector for this purpose. For demonstration purposes, we are using BigQuery as the enrichment datastore. You can use any other JDBC or QFS datastore of your choice for the enrichment datastore configuration.

**Step 1**: Add a prefix name and select an existing enrichment datastore from the dropdown list.

![add-enrichment-details-existing](../assets/datastores/teradata/add-enrichment-details-existing-light-15.png#only-light)
![add-enrichment-details-existing](../assets/datastores/teradata/add-enrichment-details-existing-dark-15.png#only-dark)

| REF.              | FIELDS       | ACTIONS                                    |
|-------------------|--------------|--------------------------------------------|
| 1.                | Prefix         | Add a prefix name to uniquely identify tables/files when Qualytics writes metadata from the source datastore to your enrichment datastore. |
| 2.                | Toggle Button for existing enrichment datastore | Toggle **ON** to link the source datastore to an existing enrichment datastore. |
| 3.                | Enrichment Datastore  | Select an enrichment datastore from the dropdown list. | 

**Step 2**: After selecting an existing **enrichment datastore** connection, you will view the following details related to the selected enrichment: 

- **Teams**: The team associated with managing the enrichment datastore is based on the role of public or private. Example- Marked as **Public** means that this data store is accessible to all the users. 

- **Host**: This is the server address where the **Teradata** instance is hosted. It is the endpoint used to connect to the PostgreSQL environment. 

- **Database**: Refers to the specific database within the Teradata environment where the data is stored.

- **Schema**: The schema used in the enrichment datastore. The schema is a logical grouping of database objects (tables, views, etc.). Each schema belongs to a single database.

![enrichment-details-check](../assets/datastores/teradata/enrichment-details-check-light-16.png#only-light)
![enrichment-details-check](../assets/datastores/teradata/enrichment-details-check-dark-16.png#only-dark)

**Step 3**: Click on the **Finish** button to complete the configuration process for the existing **enrichment datastore**.

![enrichment-details-finish](../assets/datastores/teradata/enrichment-details-finish-light-17.png#only-light)
![enrichment-details-finish](../assets/datastores/teradata/enrichment-details-finish-dark-17.png#only-dark)

When the configuration process is finished, a modal will display a **success message** indicating that **your data has been successfully added**.

![enrichment-details-success](../assets/datastores/teradata/enrichment-details-success-light-18.png#only-light)
![enrichment-details-success](../assets/datastores/teradata/enrichment-details-success-dark-18.png#only-dark)

Close the success message and you will be automatically redirected to the **Source Datastore Details** page where you can perform data operations on your configured **source datastore**.

![teradata-source-overview](../assets/datastores/teradata/teradata-source-overview-light-19.png#only-light)
![teradata-source-overview](../assets/datastores/teradata/teradata-source-overview-dark-19.png#only-dark)

## API Payload Examples

=== "Create a Source Datastore with a New Connection"
    ```json
        {
            "name": "your_datastore_name",
            "teams": ["Public"],
            "schema": "schema_name",
            "enrich_only": false,
            "trigger_catalog": true,
            "connection": {
                "host": "teradata_host",
                "port": "teradata_port",
                "username": "teradata_user",
                "password": "teradata_password",
                "type": "teradata"
                }
        }
    ```
=== "Create a Source Datastore with an Existing Connection"
    ```json
        {
            "name": "your_datastore_name",
            "teams": ["Public"],
            "schema": "schema_name",
            "enrich_only": false,
            "trigger_catalog": true,
            "connection_id": connection_id
        }
    ```

