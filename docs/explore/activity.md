# Activity

**Activity** in Qualytics provides a comprehensive view of all operations, helping users monitor and analyze the performance and workflows across various source datastores. Activity are categorized into **Runs** and **Schedule** operations, offering distinct insights into executed and scheduled activities.

Let’s get started 🚀

## Navigation

**Step 1:** Log in to your Qualytics account and click the **Explore** button on the left side panel of the interface.

![explore](../assets/explore/activity/explore-light.png#only-light)
![explore](../assets/explore/activity/explore-dark.png#only-dark)

**Step 2:** Click on the **"Activity"** from the Navigation Tab.

![activity](../assets/explore/activity/activity-light.png#only-light)
![activity](../assets/explore/activity/activity-dark.png#only-dark)

You will be navigated to the **Activity** tab and here you'll see a list of operations [catalog](../source-datastore/catalog.md), [profile](../source-datastore/profile.md), [scan](../source-datastore/scan.md) and [external scan](../source-datastore/external-scan.md) across different source datastores.

![list](../assets/explore/activity/list-light.png#only-light)
![list](../assets/explore/activity/list-dark.png#only-dark)

## Activity Categories

Activity are divided into two categories Runs and Schedule Operation. Runs operation provides insights into the operations that have been performed, while Schedule operation provides insights into the schedule operations.

![categories](../assets/explore/activity/categories-light.png#only-light)
![categories](../assets/explore/activity/categories-dark.png#only-dark)

### Runs

Runs provide a complete record of all executed operations across various source datastores. This section enables users to monitor and review activities such as [catalog](../source-datastore/catalog.md), [profile](../source-datastore/profile.md), [scan](../source-datastore/scan.md), and [external scan](../source-datastore/external-scan.md). Each run displays key details like the operation type, status, execution time, duration, and triggering method, offering a clear overview of system performance and data processing workflows.

![run](../assets/explore/activity/runs-light.png#only-light)
![run](../assets/explore/activity/runs-dark.png#only-dark)

| No. | Field | Description |
| :---- | :---- | :---- |
| 1. | Select Source Datastore | Select specific source datastores to focus on their operations. |
| 2. | Search | This feature helps users quickly find specific identifiers. |
| 3. | Sort By | **Sort By** option helps users organize list of performed operations by criteria like Duration and Created Date for quick access. |
| 4. | Filter | The filter lets users easily refine list of performed operations by choosing specific Type[Scan](../source-datastore/scan.md), [Catalog](../source-datastore/catalog.md), [Profile](../source-datastore/profile.md), and [External Scan](../source-datastore/external-scan.md)  or Success(Success, Failure, Running, and aborted) to view. |
| 5. | Activity Heatmap | **Activity Heatmap** shows daily activity levels, with color intensity indicating operation counts. Hovering over a square reveals details for that day. |
| 6. | Operation List | Shows a list of performed operations[**catalog**](../source-datastore/catalog.md), [**profile**](../source-datastore/profile.md), [**scan**](../source-datastore/scan.md), and [**external scan**](../source-datastore/external-scan.md) performed across various source datastores. |

### Activity Heatmap

 Activity heatmap represents activity levels over a period, with each square indicating a day and the color intensity representing the number of operations or activities on that day. It is useful in tracking the number of operations performed on each day within a specific timeframe.

!!! note 
    You can click on any of the squares from the Activity Heatmap to filter operations.  

![heatmap](../assets/explore/activity/heatmap-light.png#only-light)
![heatmap](../assets/explore/activity/heatmap-dark.png#only-dark)

By hovering over each square, you can view additional details for that specific day, such as the exact **date**, and the total number of **operations** executed.

![hover](../assets/explore/activity/hover-light.png#only-light)
![hover](../assets/explore/activity/hover-dark.png#only-dark)

### Operation Details

**Step 1:** Click on any successfully performed operation from the list to view its details.

For demonstration purposes, we have selected the profile operation.

![profile](../assets/explore/activity/profile-light.png#only-light)
![profile](../assets/explore/activity/profile-dark.png#only-dark)

**Step 2:** After clicking, a dropdown will appear, displaying the details of the selected operation.

![drop-down](../assets/explore/activity/drop-light.png#only-light)
![drop-down](../assets/explore/activity/drop-dark.png#only-dark)

**Step 3:** Users can hover over abbreviated metrics to see the full value for better clarity. For demonstration purposes, we are hovering over the **Records Profiled** field to display the full value.

![record](../assets/explore/activity/record-light.png#only-light)
![record](../assets/explore/activity/record-dark.png#only-dark)

In the **Summary** section, users can view both profiled and non-profiled File Patterns or Tables by clicking on the search icon next to **File Patterns Profiled** or **Table Profiled**.

![profiled](../assets/explore/activity/profiled-light.png#only-light)
![profiled](../assets/explore/activity/profiled-dark.png#only-dark)

A modal window will appear, displaying a list of the profiled and non-profiled File Patterns or Tables.

![lists](../assets/explore/activity/lists-light.png#only-light)
![lists](../assets/explore/activity/lists-dark.png#only-dark)

### Schedule

Schedule provide a complete record of all scheduled operations across various source datastores. This section enables users to monitor and review scheduled operations such as [catalog](../source-datastore/catalog.md), [profile](../source-datastore/profile.md), and [scan](../source-datastore/scan.md) operation. Each scheduled operation includes key details like operation type, scheduled time, and triggering method, giving users a clear overview of system performance and data workflows.

![schedule](../assets/explore/activity/schedule-light.png#only-light)
![schedule](../assets/explore/activity/schedule-dark.png#only-dark)

| No. | Field | Description |
| :---- | :---- | :---- |
| 1 | Selected Source Datastores | Select specific source datastores to focus on their operations. |
| 2 | Search | This feature helps users quickly find specific identifiers. |
| 3 | Sort By | **Sort By** option helps users organize list of scheduled operations by criteria like Created Date and Operations for quick access. |
| 4 | Filter | The filter lets users easily refine list of scheduled operation by choosing specific [Scan](../source-datastore/scan.md), [Catalog](../source-datastore/catalog.md), and [Profile](../source-datastore/profile.md) to view. |
| 5. | Operation List | Shows a list of scheduled operations [catalog](../source-datastore/catalog.md), [profile](../source-datastore/profile.md), and [scan](../source-datastore/scan.md) performed across various source datastores. |