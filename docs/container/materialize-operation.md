# Materialize Operation

**Materialize Operation** captures snapshots of selected containers from a **source datastore** and exports them to an **enrichment datastore** for seamless data loading. Users can run it instantly or schedule it at set intervals, ensuring structured data is readily available for analysis and integration.

Let’s get started 🚀

**Step 1:** Select a source datastore from the side menu to capture and export containers for the Materialize Operation.

![select](../assets/container/materialize-operation/select-light.png#only-light)
![select](../assets/container/materialize-operation/select-dark.png#only-dark)

For demonstration purposes, we have selected the **“COVID-19 Data”** Snowflake source datastore.

![datastore](../assets/container/materialize-operation/datastore-light.png#only-light)
![datastore](../assets/container/materialize-operation/datastore-dark.png#only-dark)

**Step 2:** After selecting a datastore, a bottom-up menu appears on the right side of the interface. Click **Enrichment Operations** next to the Enrichment Datastore and select **Materialize**.

![material](../assets/container/materialize-operation/material-light.png#only-light)
![material](../assets/container/materialize-operation/material-dark.png#only-dark)

**Step 3:**  After clicking **Materialize** a modal window appears, allowing you to configure the data export settings for the Materialize Operation.

![window](../assets/container/materialize-operation/window-light.png#only-light)
![window](../assets/container/materialize-operation/window-dark.png#only-dark)

**Step 4:**  Select tables to materialize all tables, specific tables, or tables by tag, then click **Next**.

![next](../assets/container/materialize-operation/next-light.png#only-light)
![next](../assets/container/materialize-operation/next-dark.png#only-dark)

**Step 5:** Configure Record Limit: set the maximum number of records to be materialized per table.

![record](../assets/container/materialize-operation/record-light.png#only-light)
![record](../assets/container/materialize-operation/record-dark.png#only-dark)

## Run Now

Click **Run Now** to instantly materialize selected containers.

![run](../assets/container/materialize-operation/run-light.png#only-light)
![run](../assets/container/materialize-operation/run-dark.png#only-dark)

After clicking **Run Now**, a confirmation message appears stating **"Operation Triggered"**. Go to the Activity tab to see the progress of materialize operation.

![operation-triggered](../assets/container/materialize-operation/operation-triggered-light.png#only-light)
![operation-triggered](../assets/container/materialize-operation/operation-triggered-dark.png#only-dark)

## Schedule

**Step 1:** Click **Schedule** to configure scheduling options for the Materialize Operation.

![schedule](../assets/container/materialize-operation/schedule-light.png#only-light)
![schedule](../assets/container/materialize-operation/schedule-dark.png#only-dark)

**Step 2:** Configure the scheduling preferences for the Materialize Operation.

* **Hourly:** Runs every set number of hours at a specified minute. (e.g., Every 1 hour at 00 minutes).

* **Daily:** Runs once per day at a specific UTC time. (e.g., Every day at 00:00 UTC).

* **Weekly:** Runs on selected weekdays at a set time. (e.g., Every Sunday and Friday at 00:00 UTC).

* **Monthly:** Runs on a specific day of the month at a set time. (e.g., 1st day of every month at 00:00 UTC).

* **Advanced:** Use Cron expressions for custom scheduling. (e.g., `0 12 * * 1-5` runs at 12 PM, Monday to Friday).

![time](../assets/container/materialize-operation/time-light.png#only-light)
![time](../assets/container/materialize-operation/time-dark.png#only-dark)

**Step 3:** Define the Schedule Name to identify the scheduled Materialize Operation when it runs.

![name](../assets/container/materialize-operation/name-light.png#only-light)
![name](../assets/container/materialize-operation/name-dark.png#only-dark)

**Step 4:** Click **Schedule** to finalize and schedule the Materialize Operation.

![schedule2](../assets/container/materialize-operation/schedule2-light.png#only-light)
![schedule2](../assets/container/materialize-operation/schedule2-dark.png#only-dark)

After clicking **Schedule**, a confirmation message appears stating **"Operation Scheduled"**. Go to the Activity tab to see the progress of materialize operation.

![operation-scheduled](../assets/container/materialize-operation/operation-scheduled-light.png#only-light)
![operation-scheduled](../assets/container/materialize-operation/operation-scheduled-dark.png#only-dark)

## Review Materialized Data

**Step 1:** Once the selected containers are materialized, go to **Enrichment Datastores** from the left menu. 

![preview](../assets/container/materialize-operation/preview-light.png#only-light)
![preview](../assets/container/materialize-operation/preview-dark.png#only-dark)

**Step 2:** In the **Enrichment Datastores** section, select the datastore where you materialized the snapshot. The materialized containers will now be visible.

![data](../assets/container/materialize-operation/data-light.png#only-light)
![data](../assets/container/materialize-operation/data-dark.png#only-dark)

**Step 3:** Click on the materialized files to review the snapshot. For demonstration, we have selected the **"materialized_field_profiles"** file.

The materialized data is displayed in a table format, showing key details about the selected containers. It typically includes columns indicating data structure, completeness, and uniqueness. You can use this data for analysis, validation, and integration.

![preview2](../assets/container/materialize-operation/preview2-light.png#only-light)
![preview2](../assets/container/materialize-operation/preview2-dark.png#only-dark)