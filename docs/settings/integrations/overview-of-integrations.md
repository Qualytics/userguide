## Overview
This guide outlines the integration capabilities within the settings of the Qualytics Data Quality platform, designed to enhance data governance and quality management through synchronization with various data catalog platforms. These integrations allow users to manage and synchronize assets across multiple systems, streamlining data operations and ensuring consistency and quality across the data ecosystem.

## Integration Features

### Tag Sync

Sync tags from data catalogs to Qualytics to enable tag-based quality score reporting, notifications, and bulk data quality operations.

### Metadata Sync 

Synchronize metadata across systems, including asset URLs, total scores, and detailed quality factor scores such as completeness, coverage, conformity, consistency, precision, timeliness, volume, and accuracy.

### Alerts

Generate alerts to inform users about anomalies detected in data assets, enhancing proactive data quality management.

## Atlan Integration

### Creating an Atlan persona

Before initiating the integration process, it’s advisable to set up an Atlan persona. This persona enables you to grant the necessary access for Qualytics's API token to the metadata and data of the connections you plan to integrate. Although the persona can be created simultaneously with the API token, establishing it beforehand simplifies the process, allowing you to directly associate it with the token later.

Keep in mind that enabling Atlan for a data source requires that you first authorize the API token with access to the requisite metadata and data. This is done through policies set within the persona for the Atlan connection that matches the Qualytics data source, and it must be done for each data source you intend to integrate.

<screen-shot>


### Creating an Atlan Personal Access Token

After creating the persona, create the personal access token in Atlan 


<screen-shot>

### Creating the integration with Qualytics

1. Go to  settings section of Qualytics

<screen-shot>

2. Select `Integrations` tab and click in `Add Integration`

<screen-shot>

3. Type the name of the integration, select `Atlan` type, type the URL and the personal access token with the persona you created in Atlan

<screen-shot>

4. Click in `Sync` button and wait until Qualytics have created the external tags and set them to the respective qualytics assets.

5. You can look at the logs to investigate syncing issues

Note that the assets you want to sync need to have the right permissions in Atlan.

### Tag Syncing

Sync tags assigned to data assets in Atlan with the corresponding assets in Qualytics.


### Metadata Syncing

Automatically synchronize metadata between Atlan and Qualytics.

| Metadata Item         | Description                                         |
|-----------------------|-----------------------------------------------------|
| **Asset URL**         | Direct link to the corresponding asset in Qualytics |
| **Total Score**       | Overall data quality score                          |
| **Completeness**      | Required fields are all populated with values       |
| **Coverage**          | Availability and uniqueness of expected records     |
| **Conformity**        | Alignment of the content to the required standards  |
| **Consistency**       | Values are the same for all copies and representations |
| **Precision**         | Your data is of the expected defined resolution     |
| **Timeliness**        | Data is available when and where you expect it      |
| **Volumetrics**       | Data has the same size and shape across similar cycles |

### Custom Metadata in Atlan

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


## Elation Integration
- **Coming Soon**: Details about the integration with Elation will be added soon.