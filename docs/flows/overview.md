# Flows: Overview

Flows in Qualytics allow users to create pipelines by chaining actions and configuring how they are trigerred. Triggers can be set based on predefined events and filters, offering a flexible and efficient way to automate processes. These actions can be notifications or operations, allowing users to inform various notification channels or execute tasks based on specific operations.

Let’s get started 🚀

## Navigation

Log in to your Qualytics account and click on the "**Flows**" button on the left side panel of the interface.

![flows-icon](../assets/flows/overview/flows-icon-light.png#only-light)
![flows-icon](../assets/flows/overview/flows-icon-dark.png#only-dark)

## Flow Page

Here, you can view a list of all the flow you've added to the system. From this interface, you can easily manage (add, deactivate, or delete) your flow as needed.

![flows-page](../assets/flows/overview/flows-page-light.png#only-light)
![flows-page](../assets/flows/overview/flows-page-dark.png#only-dark)

### Search a Flow

Also you can search the flow name using the **Search Box**

![flows-page-searchbox](../assets/flows/overview/flows-page-searchbox-light.png#only-light)
![flows-page-searchbox](../assets/flows/overview/flows-page-searchbox-dark.png#only-dark)

!!! tip
    The Search box only searches by flow name. The other flow data, like ID or description will not bring the expected results.

### Sort by Flow List

And sort the list by **Name** (ascending or descending) or **Creation Date** (ascending or descending)

![flows-page-filter](../assets/flows/overview/flows-page-filter-light.png#only-light)
![flows-page-filter](../assets/flows/overview/flows-page-filter-dark.png#only-dark)

## Add new Flow

**Setop 1:** Click on the "**Add Flow**" button located in the top right corner of the application. 

![flows-add-new-item-1](../assets/flows/overview/flows-add-new-item-1-light.png#only-light)
![flows-add-new-item-1](../assets/flows/overview/flows-add-new-item-2-dark.png#only-dark)

After being redirected them to the Add Flows page you can see 2 nodes "**Flow**" and "**Trigger**". 

![flows-add-new-item-2](../assets/flows/overview/flows-add-new-item-2-light.png#only-light)
![flows-add-new-item-2](../assets/flows/overview/flows-add-new-item-2-dark.png#only-dark)

### Setup the Flow Node

**Step 1:** Click on the "**Flow**" node. This will opens a panel on the right side of the application. 

![flows-setup-flow-node-1](../assets/flows/overview/flows-setup-flow-node-1-light.png#only-light)
![flows-setup-flow-node-1](../assets/flows/overview/flows-setup-flow-node-1-dark.png#only-dark)

**Step 2:** Fill out the Flow node form. After finishing the required fields, click on "**Save**" button.

![flows-setup-flow-node-2](../assets/flows/overview/flows-setup-flow-node-2-light.png#only-light)
![flows-setup-flow-node-2](../assets/flows/overview/flows-setup-flow-node-2-dark.png#only-dark)

| Field | Description |
|-------|--------|
| **Name*** | Add a flow name |
| **Description** | Add a flow description. This field is optional. |
| **Deactivated** | If checked this will deactivate this flow. The flow item will not until user uncheck this field  |

!!! warning
    * Required field

**Step 3:** After finishing the required fields, click on "**Save**" button.

![flows-setup-flow-node-save](../assets/flows/overview/flows-setup-flow-node-3-light.png#only-light)
![flows-setup-flow-node-save](../assets/flows/overview/flows-setup-flow-node-3-dark.png#only-dark)

### Setup the Trigger Node

**Step 1:** Click on the "**Trigger**" node. This will opens a panel on the right side of the application. 

![flows-setup-flow-trigger-1](../assets/flows/overview/flows-setup-flow-trigger-1-light.png#only-light)
![flows-setup-flow-trigger-1](../assets/flows/overview/flows-setup-flow-trigger-1-dark.png#only-dark)

**Step 2:** Select one of the three trigger event to activate this flow.

![flows-setup-flow-trigger-2](../assets/flows/overview/flows-setup-flow-trigger-2-light.png#only-light)
![flows-setup-flow-trigger-2](../assets/flows/overview/flows-setup-flow-trigger-2-dark.png#only-dark)

| Trigger Event | Description |
|-------|--------|
| **Operations Completes** | The flow is triggered when an operation is completed. |
| **Anomalous Table or File Detected** | The flow is triggered when an anomalous table or file is detected. |
| **Anonmaly Detect** | The flow is triggered when an anomaly is detected. |
| **Manual** | The flow is triggered when user press the "**Execute**" button. |

**Step 3-1:** **Using Operations Completes**. User can filter the Completed Operations just setting the filters below.

![flows-setup-flow-trigger-3](../assets/flows/overview/flows-setup-flow-trigger-3-light.png#only-light)
![flows-setup-flow-trigger-3](../assets/flows/overview/flows-setup-flow-trigger-3-dark.png#only-dark)

| Field | Description |
|-------|--------|
| **Source Datastore Tags** | Only Source Datastores that have all selected tags assigned will trigger the flow. |
| **Operation Types** | Only Operations that match one or more of the selected types will trigger the flow. |
| **Operation Status** | Only Operations matching the selected state will trigger the flow. |

!!! warning
    The user can optionally set filters to narrow which table or files should trigger a flow execution.

**Step 3-2:** **Using Anomalous Table or File Detected**. User can filter when a Anomalous Table or File is detected.

![flows-setup-flow-trigger-4](../assets/flows/overview/flows-setup-flow-trigger-4-light.png#only-light)
![flows-setup-flow-trigger-4](../assets/flows/overview/flows-setup-flow-trigger-4-dark.png#only-dark)

| Field | Description |
|-------|--------|
| **Tables / Files Tags** | Only Tables or Files that have all selected tags assigned will trigger the flow. |
| **Check Rule Types** | Only Anomalies identified by one or more of the selected check rule types will trigger the flow. |

**Step 3-3:** **Using Anonmaly Detect**. User can filter when an Anomaly is detected.

![flows-setup-flow-trigger-5](../assets/flows/overview/flows-setup-flow-trigger-5-light.png#only-light)
![flows-setup-flow-trigger-5](../assets/flows/overview/flows-setup-flow-trigger-5-dark.png#only-dark)

| Field | Description |
|-------|--------|
| **Anomaly's Tags** | Only Anomalies that have all selected tags assigned will trigger the flow. |
| **Check Rule Types** | Only Anomalies identified by one or more of the selected check rule types will trigger the flow. |
| **Anomaly Weight (Min)** | Only anomalies with a weight equal to or greater than this value will trigger the flow. |

!!! warning
    The user can optionally set filters to narrow which anomaly trigger a flow execution.

**Step 3-4:** **Using Manual**. User can run this flow manually pressing the "**Execute**" button.

![flows-setup-flow-trigger-6](../assets/flows/overview/flows-setup-flow-trigger-6-light.png#only-light)
![flows-setup-flow-trigger-6](../assets/flows/overview/flows-setup-flow-trigger-6-dark.png#only-dark)

**Step 4:** Fill out the Trigger node form. After finishing the required fields, click on "**Save**" button.

![flows-setup-flow-trigger-7](../assets/flows/overview/flows-setup-flow-trigger-7-light.png#only-light)
![flows-setup-flow-trigger-7](../assets/flows/overview/flows-setup-flow-trigger-7-dark.png#only-dark)

### Setup the Action Node

!!! warning
    The Action Node will be available when user finish to setup the Trigger Node.

**Step 1:** Click on the "**Action**" node. This will opens a panel on the right side of the application.

![flows-setup-action-1](../assets/flows/overview/flows-setup-action-1-light.png#only-light)
![flows-setup-action-1](../assets/flows/overview/flows-setup-action-1-dark.png#only-dark)

**Step 2:** Select the action.

![flows-setup-action-2](../assets/flows/overview/flows-setup-action-2-light.png#only-light)
![flows-setup-action-2](../assets/flows/overview/flows-setup-action-2-dark.png#only-dark)

!!! warning
    Chaining Action Notifications is not supported.

**Step 3:** Fill out the Action node form. After finishing the required fields, click on "**Save**" button.

![flows-setup-action-3](../assets/flows/overview/flows-setup-action-3-light.png#only-light)
![flows-setup-action-3](../assets/flows/overview/flows-setup-action-3-dark.png#only-dark)

### Publishing

After finishing to create the flow the user must save this flow clicking on "**Publish**" button.