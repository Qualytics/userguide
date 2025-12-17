# External Tag Propagation

External tags propagation in Qualytics serve as metadata labels that are automatically synchronized from an integrated data catalog, such as Atlan or Alation. This process helps maintain consistent data tagging across various platforms by using pre-existing tags from the data catalog.

Let’s get started 🚀

## Navigation

**Step 1:** Log in to your Qualytics account and click the **Settings** button on the left side panel of the interface.

![setting](../../../assets/integrations/catalog/external-tag-propagation/setting-light-1.png)

**Step 2:** You will be directed to the Settings page, then click on the **Integration** tab.

![integration](../../../assets/integrations/catalog/external-tag-propagation/integration-light-2.png)

**Step 3:** Click on the **Add Integration** button.

![Screenshot](../../../assets/integrations/catalog/external-tag-propagation/add-integration-light-3.png)

A modal window Add Integration will appear, providing you with the options to add integration.

![Screenshot](../../../assets/integrations/catalog/external-tag-propagation/modal-window-light-4.png)

| REF. | FIELDS | ACTIONS |
| :---- | :---- | :---- |
| 1. | Name  | Provide a detailed description of the integration. |
| 2. | Type | Choose the type of integration from the dropdown menu. Currently, 'Atlan' is selected |
| 3. | URL | The complete address for the Atlan instance, for example: [https://your-company.atlan.com](https://your-company.atlan.com/). |
| 4. | Token | Provide the authentication token needed to connect to Atlan. |
| 5. | Event Driven | If enabled, the integration sync will be activated by operations, archiving anomalies, and checks. |
| 6. | Overwrite Tags | If enabled, Atlan tags will have precedence over Qualytics tags in cases of conflicts (when tags with the same name exist on both platforms). |

![Screenshot](../../../assets/integrations/catalog/external-tag-propagation/detail-light-5.png)

For demonstration purposes we have selected **Atlan** integration type.

**Step 5**: Click on the **Save** button to set up the Atlan integration.

![Screenshot](../../../assets/integrations/catalog/external-tag-propagation/save-btn-light-6.png)

**Step 6**: Once the Atlan integration is set up with Qualytics, it will appear in Qualytics as a new integration.

![Screenshot](../../../assets/integrations/catalog/external-tag-propagation/atlan-7-light.png)

## Synchronization

 Synchronization supports both push and pull operations. This includes pulling metadata from one platform to Qualytics and pushing Qualytics metadata to the other platform. During the syncing process, the integration pulls tags assigned to data assets in the source platform and assigns them to Qualytics assets as an external tag.

For demonstration purposes we have selected **Atlan** synchronization.

!!! note
    Tag synchronization requires manual triggering. 
   
**Step 1:** To sync tags, simply click on the **Sync** button next to the relevant integration card.

![Screenshot](../../../assets/integrations/catalog/external-tag-propagation/sync-light-8.png)

**Step 2:** After clicking the **Sync** button, you will have the following options:

* **Pull Atlan Metadata**  
* **Push Qualytics Metadata**

Specify whether the synchronization will pull metadata, push metadata, or do both.

![Screenshot](../../../assets/integrations/catalog/external-tag-propagation/sync-option-light-9.png)

**Step 3:** After selecting the desired options, click on the **Start** button.

![Screenshot](../../../assets/integrations/catalog/external-tag-propagation/start-btn-light-10.png)

**Step 4:** After clicking the **Start** button, the synchronization process between Qualytics and Atlan begins. This process pulls metadata from Atlan and pushes Qualytics metadata, including tags, quality scores, anomaly counts, asset links, and many more.

![Screenshot](../../../assets/integrations/catalog/external-tag-propagation/sync-light-11.png)

**Step 5:** Review the logs to verify which assets were successfully mapped from Atlan to Qualytics.

![Screenshot](../../../assets/integrations/catalog/external-tag-propagation/review-logs-light-12.png)

**Step 6:** Once synchronization is complete, the mapped assets from **Atlan** will display an external tag.

![Screenshot](../../../assets/integrations/catalog/external-tag-propagation/external-tag-light-13.png)
