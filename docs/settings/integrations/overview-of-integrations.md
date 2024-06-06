# Integrations

The integrations area supports the continuous synchronization of metadata between your Qualytics deployment and another system. 
Where `Notifications` can be used to push data from Qualytics into another system after a specified event, `Integrations` establish
an on-going two-way synchronization of data with another system.

## Data Catalogs

### Atlan Integration 

#### Creating an Atlan persona and Policy

Before initiating the integration process, it’s advisable to set up an Atlan persona. This persona enables you to grant the necessary access for Qualytics's API token to the metadata and data of the connections you plan to integrate. Although the persona can be created simultaneously with the API token, establishing it beforehand simplifies the process, allowing you to directly associate it with the token later.

Keep in mind that enabling Atlan for a data source requires that you first authorize the API token with access to the requisite metadata and data. This is done through policies set within the persona for the Atlan connection that matches the Qualytics data source, and it must be done for each data source you intend to integrate.

1. Go to `Governance` and `Personas`

    ![Screenshot](../../assets/integrations/atlan-governance-center.png){: style="height:450px"}

2. Click in `New Persona`

    ![Screenshot](../../assets/integrations/atlan-add-new-persona.png)

3. Add a name and decription and click in `Create`

    ![Screenshot](../../assets/integrations/atlan-create-new-persona.png)

4. You will see a section similar to this

    ![Screenshot](../../assets/integrations/atlan-new-persona-view.png)

5. Click on `Add policies` to add a new policy or create one if none exists

    ![Screenshot](../../assets/integrations/atlan-add-policies.png)

6. You will see the Policies section, click in `New Policy` and choose `Metadata policy`

    ![Screenshot](../../assets/integrations/atlan-new-policy-section.png)

7. Type the name, select the connection, and customize the permissions and assets that will have Qualytics access

    ![Screenshot](../../assets/integrations/atlan-policy-to-connection.png){: style="height:450px"}

    ![Screenshot](../../assets/integrations/atlan-metadata-policy-and-assets-configuration.png){: style="height:450px"}

8. After the policy creation, you can see that it is now included in the `Policy` section

    ![Screenshot](../../assets/integrations/atlan-policy-attached-to-persona.png)

#### Creating an Atlan Personal Access Token

After creating the persona, you need to create a personal access token

1. Go to `API tokens` in Admin center

    ![Screenshot](../../assets/integrations/atlan-admin-center.png){: style="height:450px"}

2. Click in `Generate API token`

    ![Screenshot](../../assets/integrations/atlan-generate-api-token.png)

3. Add a name, description and the `Persona` you created before

    ![Screenshot](../../assets/integrations/atlan-add-new-api-token.png)

4. Click the `Save` button and store it in a secure location

    ![Screenshot](../../assets/integrations/atlan-token-generated.png){: style="height:450px"}

#### Creating the integration with Qualytics

1. Go to the settings section of Qualytics and select the `Integrations` tab

    ![Screenshot](../../assets/integrations/qualytics-settings-section-light.png#only-light)
    ![Screenshot](../../assets/integrations/qualytics-settings-section-dark.png#only-dark)
    
2. Click the `Add Integration` button

    ![Screenshot](../../assets/integrations/qualytics-add-integration.png)

3. Give your new integration a descriptive name, select `Atlan` type, type the URL and the personal access token from the persona you created in Atlan

    ![Screenshot](../../assets/integrations/qualytics-add-atlan-integration-light.png#only-light)
    ![Screenshot](../../assets/integrations/qualytics-add-atlan-integration-dark.png#only-dark)

4. Click the `Save` button to create the Atlan integration. You will see the new integration created in Qualytics

    ![Screenshot](../../assets/integrations/qualytics-atlan-integration-created-light.png#only-light)
    ![Screenshot](../../assets/integrations/qualytics-atlan-integration-created-dark.png#only-dark)

#### Tag Syncing

During a sync, the Atlan integration pulls tags assigned to data assets in Atlan and assigns them as `external` tags on the corresponding assets in Qualytics. 

1. Click the Sync button and configure your desired settings
    
    ![Screenshot](../../assets/integrations/qualytics-sync-button.png)

    ![Screenshot](../../assets/integrations/qualytics-sync-modal-light.png#only-light)
    ![Screenshot](../../assets/integrations/qualytics-sync-modal-dark.png#only-dark)

2. Wait for Qualytics to create external tags and assign them to the respective Qualytics assets

    ![Screenshot](../../assets/integrations/qualytics-atlan-syncing-light.png#only-light)
    ![Screenshot](../../assets/integrations/qualytics-atlan-syncing-dark.png#only-dark)

3. Check the logs to review the assets that were mapped from Atlan to Qualytics

    ![Screenshot](../../assets/integrations/qualytics-atlan-logs-light.png#only-light)
    ![Screenshot](../../assets/integrations/qualytics-atlan-logs-dark.png#only-dark)

4. After synchronization, the mapped assets will display an external tag
    
    a. Datastore

    ![Screenshot](../../assets/integrations/qualytics-datastore-external-tag-light.png#only-light)
    ![Screenshot](../../assets/integrations/qualytics-datastore-external-tag-dark.png#only-dark)

    b. Table

    ![Screenshot](../../assets/integrations/qualytics-table-external-tag-light.png#only-light)
    ![Screenshot](../../assets/integrations/qualytics-table-external-tag-dark.png#only-dark)

    c. Field
    
    ![Screenshot](../../assets/integrations/qualytics-field-external-tag-light.png#only-light)
    ![Screenshot](../../assets/integrations/qualytics-field-external-tag-dark.png#only-dark)

!!!note
    In order for a data asset's tags to be synchronized, the token you used when creating the Qualytics integration must have the appropriate permissions (ability to read tags from that asset) in Atlan.
    

### Qualytics push of Data Quality Metadata into Atlan

The integration also supports pushing data quality metadata from Qualytics into Atlan, including asset URLs, total scores, and detailed quality factor scores such as completeness, coverage, conformity, consistency, precision, timeliness, volume, and accuracy.
This will happen automatically for any data asset where appropriate permissions have been grated to the integration token.

#### Atlan Alerts and Announcements

After synchronization, Qualytics will issue Atlan `alerts` for tables where anomalies have been identified.

##### Alert in a table

![Screenshot](../../assets/integrations/atlan-qualytics-table-notification.png)

##### Recent Announcements on the Main Page

![Screenshot](../../assets/integrations/atlan-qualytics-notification-announcements.png)

##### Qualytics Custom Metadata inside Atlan

![Screenshot](../../assets/integrations/atlan-qualytics-custom-metadata.png)

#### Table of custom metadata 

| Property Name                | Description |
|------------------------------|-------------|
| **URL**                      | Correspondent Qualytics asset URL |
| **Quality Score Total**      | The data quality score total |
| **Quality Score Completeness** | Required Fields are all populated with values |
| **Quality Score Coverage**     | Availability and uniqueness of expected records |
| **Quality Score Conformity**   | Alignment of the content to the required standards |
| **Quality Score Consistency**  | Values are the same for all copies and representations |
| **Quality Score Precision**    | Your data is of the expected defined resolution |
| **Quality Score Timeliness**   | Data is available when and where you expect it |
| **Quality Score Volumetrics**  | Data has the same size and shape across similar cycles |


### Alation Integration
- **Coming Soon**: Details about the integration with Alation will be added soon