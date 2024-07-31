# Datastore Settings

Qualytics allows you to manage your datastore efficiently by editing source datastore information, linking an enrichment datastore for enhanced insights, establishing new connections to expand data sources, choosing connectors to integrate diverse data, adjusting the quality score to ensure data accuracy, and deleting the store. This ensures flexibility and control over your data management processes within the platform.

Let's get started 🚀

## Navigation to Settings 

**Step 1**: Select a source **datastore** from the side menu for which you would like to manage the settings. 

![add-datastore](../assets/datastore-settings/add-datastore-light-1.png#only-light)
![add-datastore](../assets/datastore-settings/add-datastore-dark-1.png#only-dark)

**Step 2**: Click on the **Settings** icon from the top right window. A drop-down menu will appear with the following options:

1. Edit
2. Enrichment
3. Score
4. Delete

![settings](../assets/datastore-settings/settings-light-2.png#only-light)
![settings](../assets/datastore-settings/settings-dark-2.png#only-dark)

## Edit Datastore

The **Edit Datastore** setting allows users to modify the connection details of the datastore. This includes updating the host, port, SID, username, password, schema, and any associated teams.

!!! note
    Connection details can vary based on the type of datastore being edited. For example, details for BigQuery will differ from Snowflake or Athena.

**Step 1**: Click on the **Edit** option

![edit-datastore](../assets/datastore-settings/edit-datastore-light-3.png#only-light)
![edit-datastore](../assets/datastore-settings/edit-datastore-dark-3.png#only-dark)

**Step 2**: After selecting the **Edit** option, a modal window will appear, displaying the connection details. This window allows you to modify any specific connection details. 

![connection-details](../assets/datastore-settings/connection-details-light-4.png#only-light)
![connection-details](../assets/datastore-settings/connection-details-dark-4.png#only-dark)

**Step 3**: After editing the connection details, click on the **Save** button. 

![save-datastore](../assets/datastore-settings/save-datastore-light-5.png#only-light)
![save-datastore](../assets/datastore-settings/save-datastore-dark-5.png#only-dark)

## Link Enrichment Datastore

An enrichment datastore is a database used to enhance your existing data by adding additional, relevant information. This helps you to provide more comprehensive insight into data and improve data accuracy.

You have the option to link an enrichment datastore to your existing source datastore. However, some datastores cannot be linked as enrichment datastores. For example, Oracle, Athena, and Timescale cannot be used for this purpose.

**Step 1**: Click on the **Enrichment** from the dropdown list.

![enrichment](../assets/datastore-settings/enrichment-light-6.png#only-light)
![enrichment](../assets/datastore-settings/enrichment-dark-6.png#only-dark)

**Step 2**: A modal window- **Link Enrichment Datastore** will appear, providing you with two options to link an **enrichment datastore**.

| REF.              | FIELDS                  | ACTIONS                                    |
|-------------------|-------------------------|--------------------------------------------|
| 1.                | Prefix                  | Add a prefix name to uniquely identify tables/files when Qualytics writes metadata from the source datastore to your enrichment datastore. |
| 2.                | Toggle Button for existing enrichment datastore  | Toggle **ON** to link the source datastore to an existing enrichment datastore, or toggle **OFF** to link it to a brand new enrichment datastore. |
| 3.                | Name                    | Give a name for the enrichment datastore.|
| 4.                | Toggle Button for using an existing connection  | Toggle **ON** to reuse credentials from an existing connection, or toggle **OFF** to create a new enrichment from scratch. |
| 5.                | Connector               | Select a datastore connector as **Teradata** from the dropdown list. |

![link-enrichment](../assets/datastore-settings/link-enrichment-light-7.png#only-light)
![link-enrichment](../assets/datastore-settings/link-enrichment-dark-7.png#only-dark)

### Option I: Link New Enrichment 

If the toggle for **Use an existing connection** is turned off, then this will prompt you to link a new enrichment datastore from scratch without using existing connection details.

**Step 1**: Select the **Enrichment** datastore from the connector dropdown list and add connection details such as URI, access key, secret key, root path, and teams. 

!!! note
    Connection details can vary from datastore to datastore. For illustration, we have demonstrated linking Amazon S3 as a new enrichment datastore.

![select-new-enrichment](../assets/datastore-settings/select-new-enrichment-light-8.png#only-light)
![select-new-enrichment](../assets/datastore-settings/select-new-enrichment-dark-8.png#only-dark)

**Step 2**: The configuration form will expand, requesting credential details before establishing the connection.

![connector-creds](../assets/datastore-settings/connector-creds-light-9.png#only-light)
![connector-creds](../assets/datastore-settings/connector-creds-dark-9.png#only-dark)

**Step 3**: After adding the source datastore details, click on the **Test Connection** button to check and verify its connection.

![test-connection](../assets/datastore-settings/test-connection-light-10.png#only-light)
![test-connection](../assets/datastore-settings/test-connection-dark-10.png#only-dark)

If the credentials and provided details are verified, a success message will be displayed indicating that the connection has been verified.

**Step 4**: Click on the **Save** button.

![save-enrichment](../assets/datastore-settings/save-enrichment-light-11.png#only-light)
![save-enrichment](../assets/datastore-settings/save-enrichment-dark-11.png#only-dark)

**Step 5**: After clicking on the **Save** button a modal window will appear  **Your Datastore has been successfully updated**

![success](../assets/datastore-settings/success-light-12.png#only-light)
![success](../assets/datastore-settings/success-dark-12.png#only-dark)

### Option II: Link Existing Connection

If the toggle for **Use an existing enrichment datastore** is turned on, you will be prompted to link the enrichment datastore using existing connection details.

**Step 1**: Select an existing enrichment datastore from the dropdown list. 

![existing-connection](../assets/datastore-settings/existing-connection-light-13.png#only-light)
![existing-connection](../assets/datastore-settings/existing-connection-dark-13.png#only-dark)

**Step 2**: View and check the connection details of the enrichment and click on the  **Save** button.

![save](../assets/datastore-settings/save-light-14.png#only-light)
![save](../assets/datastore-settings/save-dark-14.png#only-dark)

**Step 3**: After clicking on the **Save** button a modal window will appear **Your Datastore has been successfully updated**

![success](../assets/datastore-settings/success-light-15.png#only-light)
![success](../assets/datastore-settings/success-dark-15.png#only-dark)

## Quality Score Settings

Quality Scores are quantified measures of data quality calculated at the field and container levels recorded as time series to enable tracking of changes over time. Scores range from 0-100 with higher values indicating superior quality. These scores integrate eight distinct factors providing a granular analysis of the attributes that impact the overall data quality.

Each field receives a total quality score based on eight key factors each evaluated on a 0-100 scale. The overall score is a composite reflecting the relative importance and configured weights of these factors:

- **Completeness**: Measures the average completeness of a field across all profiles.

- **Coverage**: Assesses the adequacy of data quality checks for the field.

- **Conformity**: Checks alignment with standards defined by quality checks.

- **Consistency**: Ensures uniformity in type and scale across all data representations.

- **Precision**: Evaluates the resolution of field values against defined quality checks.

- **Timeliness**: Gauges data availability according to schedule inheriting the container's timeliness.

- **Volumetrics**: Analyzes consistency in data size and shape over time inheriting the container's volumetrics.

- **Accuracy**: Determines the fidelity of field values to their real-world counterparts.

The **Quality Score Settings** allow users to tailor the impact of each quality factor on the total score by adjusting their weights allowing the scoring system to align with your organization’s data governance priorities.

**Step 1**: Click on the **Score** option in the settings icon.

![score](../assets/datastore-settings/score-light-16.png#only-light)
![score](../assets/datastore-settings/score-dark-16.png#only-dark)

**Step 2**: A modal window "Quality Score Settings" will appear. 

![score-settings](../assets/datastore-settings/score-settings-light-17.png#only-light)
![score-settings](../assets/datastore-settings/score-settings-dark-17.png#only-dark)

**Step 3**: The **Decay Period** slider sets the time frame over which the system evaluates historical data to determine the quality score. The decay period for considering past data events defaults to 180 days but can be customized to fit your operational needs ensuring the scores reflect the most relevant data quality insights. 

![decay-period](../assets/datastore-settings/decay-period-light-18.png#only-light)
![decay-period](../assets/datastore-settings/decay-period-dark-18.png#only-dark)

**Step 4**: Adjust the **Factor Weights** using the sliding bar. The factor weights determine the importance of different data quality aspects. 

![factor-weights](../assets/datastore-settings/factor-weights-light-19.png#only-light)
![factor-weights](../assets/datastore-settings/factor-weights-dark-19.png#only-dark)

**Step 5**: Click on the **Save** button to save the quality score settings.

![score-save](../assets/datastore-settings/score-save-light-20.png#only-light)
![score-save](../assets/datastore-settings/score-save-dark-20.png#only-dark)

## Delete Datastore

The **Delete Datastore** action permanently removes a datastore and all associated profiles, checks, and anomalies. This action cannot be undone and requires confirmation by typing the datastore name before proceeding.

**Step 1**: Click on the **Delete** option in the settings icon.

![delete](../assets/datastore-settings/delete-light-21.png#only-light)
![delete](../assets/datastore-settings/delete-dark-21.png#only-dark)

**Step 2**: A modal window **Delete Datastore** will appear.

![delete-datastore](../assets/datastore-settings/delete-datastore-light-22.png#only-light)
![delete-datastore](../assets/datastore-settings/delete-datastore-dark-22.png#only-dark)

**Step 3**: Enter the **Name of the datastore** in the given field (confirmation check) and then click on the **I’M SURE, DELETE THIS DATASTORE** button to delete the datastore.

![confirm-delete](../assets/datastore-settings/confirm-delete-light-23.png#only-light)
![confirm-delete](../assets/datastore-settings/confirm-delete-dark-23.png#only-dark)
