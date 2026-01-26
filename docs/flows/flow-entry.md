# Flow Entry

The **Flow Entry** is the starting point of every Flow in Qualytics. Think of it as the “root” of your automation — it defines the Flow’s name, purpose, and whether it is active. Once this node is set, you can continue building the rest of the Flow (Triggers, Actions, etc.).

## Trigger Types

A Flow begins when one of its Triggers activates. Here are the five available trigger types:

| Trigger Type | Description |
|--------------|-------------|
| [**Schedule**](../flows/trigger-node.md#schedule){target="_blank"} | Starts the Flow automatically based on a defined schedule (hourly, daily, weekly, monthly, or custom cron). |
| [**Operation Completes**](../flows/trigger-node.md#operation-completes){target="_blank"} | Starts the Flow when a catalog, scan, or profile operation finishes. |
| [**Anomalous Table or File Detected**](../flows/trigger-node.md#anomalous-table-or-file-detected){target="_blank"} | Starts the Flow when anomalies are detected in a table or file. |
| [**Anomaly Detected**](../flows/trigger-node.md#anomaly-detected){target="_blank"} | Starts the Flow when a single anomaly event occurs. |
| **Anomaly Status Changed** | Starts the Flow when an anomaly’s status changes to a specified state. |
| [**Manual**](../flows/trigger-node.md#manual){target="_blank"} | Starts the Flow only when the user manually executes it. |

## Configure the Flow Node

**Step 1:** Click on the **Flow** node.  

![flow](../assets/flows/flow-light-6.png)

A panel will appear on the right-hand side, allowing you to:

| No. |             Field Name |                         Description |
| :---- | :---- | :---- |
| 1. |              **Name** | Enter the name for the flow. |
| 2. |            **Description** | Provide a brief description of the flow (optional) to clarify its purpose or functionality. |
| 3. |            **Deactivated** | Check the box to deactivate the flow. If selected, the flow won't start even if the trigger conditions are met. |

![flow](../assets/flows/flowsetting-light-7.png)

**Step 2:** Once the details are filled in, click the **Save** button to save the flow settings.  

![save](../assets/flows/save-light-8.png)