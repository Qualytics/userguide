# Overview

With Qualytics integrations, data analysts can rely on the data quality insights produced by our platform data profiling and scanning. These insights can be visualized in your preferred data catalog tool.

Key features include:

- Leveraging data catalog tags
- Pushing alerts based on anomaly identification
- Sharing valuable data quality metrics

Supported data catalog integrations:

- [Atlan](./atlan.md)
- [Alation](./alation.md)

Once an integration is set up, the synchronization process can occur in two ways:

* **Manual Sync**: Manual sync occurs when the user clicks the Sync button located on the Settings page in the Integrations tab. Clicking it triggers a full sync of all matching assets. 

    ![Screenshot](../../assets/integrations/qualytics-sync-button.png){ width=80}

    !!!info
        Tags are only synchronized through a manual sync.

* **Event Driven**:
    Once the Event Driven option is enabled, triggering occurs automatically based on the listed action events executed by users. If any of the following actions occur, a sync is triggered.

    | Event                               | Description                                         |
    |-------------------------------------|-----------------------------------------------------|
    | Run an Operation (Profile or Scan)  | Sync all target containers for the operation |
    | Archive an Anomaly (including bulk) | Sync the container in which the anomaly was identified |
    | Archive a Check (including bulk)    | Sync the container to which the check belongs |