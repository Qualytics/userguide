# Integrations Overview

Qualytics integrations provide data analysts with data quality insights derived from our platform’s data profiling and scanning features. These insights can be visualized directly in your preferred data catalog tool, enhancing your data management and monitoring capabilities.

## Key Features

* Leveraging data catalog tags

* Pushing alerts based on anomaly identification

* Sharing valuable data quality metrics

## Navigation

**Step 1:** Log in to your Qualytics account and click the **"Settings"** button on the left side panel of the interface.

![setting](../../assets/integrations/overview/setting-button-light.png#only-light)
![setting](../../assets/integrations/overview/setting-button-dark.png#only-dark)

**Step 2:** You will be directed to the **Settings** page, then click on the "**Integration**" tab.

![tab](../../assets/integrations/overview/tab-button-light.png#only-light)
![tab](../../assets/integrations/overview/tab-button-dark.png#only-dark)

**Step 3:** Click on the **Add Integration** button to add supported Data Catalog integrations.

![integration](../../assets/integrations/overview/add-integration-button-light.png#only-light)
![integration](../../assets/integrations/overview/add-integration-button-dark.png#only-dark)

## Supported Data Catalog Integrations 

Currently, Qualytics supports integration with the following data catalog tools:

* **Atlan**

* **Alation**

### Atlan

Integrating Atlan with Qualytics allows for easy push and pull of metadata between the two platforms. Specifically, Qualytics "pushes" its metadata to the data catalog and "pulls" metadata from the data catalog. Once connected, Qualytics automatically updates when key events happen in Atlan, such as metadata changes, anomaly updates, or archiving checks. This helps maintain data quality and consistency. During the sync process, Qualytics can either replace existing tags in Atlan or skip assets that have duplicate tags to avoid conflicts. Setting it up is simple—you just need to provide an API token to allow smooth communication between the systems.

For more details on Atlan, please refer to the [**Atlan**](./atlan.md) documentation.

### Alation

Integrating Alation with Qualytics, allows you to pull metadata from Alation to Qualytics and push Qualytics metadata to Alation. Once integrated, Qualytics can stay updated with key changes in Alation, like metadata updates and anomaly alerts which helps to ensure data quality and consistency. Qualytics updates only active checks, and metadata updates in Qualytics occur if the Event-Driven option is enabled or can be triggered manually using the **"Sync"** button. During sync, Qualytics can replace existing tags in Alation or skip duplicate tags to avoid conflicts. The setup is simple—just provide a refresh token for communication between the systems.

For more details on Alation, please refer to the [**Alation**](./alation.md) documentation.

## Synchronization Process 

Once an integration is set up, synchronization between Qualytics and your data catalog can be performed in two ways:

* **Manual Sync**

* **Event Driven**

### Manual Sync

Manual synchronization allows you to trigger a full sync of all matching assets between Qualytics and your data catalog manually. when the user clicks the Sync button located on the Settings page in the Integrations tab. Clicking it triggers a full sync of all matching assets.

![mannual](../../assets/integrations/overview/mannual-light.png#only-light)
![mannual](../../assets/integrations/overview/mannual-dark.png#only-dark)

For more details on how to perform a Manual Sync, follow the steps in the [**Synchronization**](atlan.md/#synchronization) section.

### Event Driven

Event-Driven Sync enables automatic synchronization based on specific user actions within the platform. Once the Event-Driven option is enabled, the system triggers synchronization whenever designated actions, such as running an operation or archiving anomalies and checks, are performed. This ensures that your data catalog stays up-to-date without manual intervention.

![event](../../assets/integrations/overview/event-light.png#only-light)
![event](../../assets/integrations/overview/event-dark.png#only-dark)

| Event  | Description |
| :---- | :---- |
| Run an Operation (Profile Or Scan) | Sync all target containers for the operation. |
| Archive an Anomaly (including bulk) | Sync the container in which the anomaly was identified. |
| Archive a Check ( including bulk) | Sync the container to which the check belongs. |