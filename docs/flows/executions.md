# Flow Executions

**Executions** in Qualytics provide a global view of all the flow activities within your system. Each execution represents a triggered flow, displaying details like the flow name, status (Success, Failure, or Running), and the trigger type—whether it’s an operation completion, an anomaly detection, or a manual initiation.

This section helps you monitor your processes, track performance, and understand the events that trigger your flows. With this comprehensive overview, staying on top of your executions is simple and efficient.

Let’s get started 🚀


## Search Flow Executions

Quickly find a specific flow execution by entering its **Execution ID** in the search box.


## Sorting Options

Easily organize executions by **Created Date** or **Duration** in either ascending or descending order.


## Filtering Options

Narrow down your results using filters for flow name, execution status (Success, Failure, or Running), or trigger types, such as operations, anomalies, or manual triggers.


## Flow Execution Details

This page provides a detailed view of a specific flow execution, allowing you to monitor its progress, review logs, and access detailed information about each node and action execution within the flow.

### Node Status Overview

Each node in the flow displays a status indicator at the top, using color-coded bars to represent the execution status:

- **Green**: Success
- **Red**: Failure
- **Orange**: Aborted
- **Yellow**: Skipped
- **Blue**: Running
- **Gray**: Pending

If an operation is running, the node displays a dotted line animation to indicate that the step is in progress. Once finished, the Action box updates with a color on top to reflect its final state. 

A legend with all status colors is available in the bottom-right corner for reference.

### Real-Time Execution View

Users can view the flow execution in real time by clicking on a specific flow operation. This page mirrors the layout of the "Add New Flow" page but is read-only. While users cannot edit anything here, they can navigate the flow in the same way.


## Viewing Flow Execution Details

By clicking on the **Flow Execution** node (the first node), users can access detailed information about the execution, including:

1. **Flow Name**: **Data Sync Bronze to Silver**
2. **Flow Execution ID**: **#452**
3. **Status**: **Running**
4. **Triggered When**: **Operation Completes**
5. **Started At**: **Jan 17 2025, 10:15 AM (GMT-3)**
6. **Triggering Operation**: **#12879**

This detailed view provides valuable context for understanding the flow execution, including when it was triggered, its status, and the specific operation responsible for initiating the flow.

!!! info
    If any action execution fails, a log with error or warning details will be available for review. To view the specific log, click on the corresponding action execution node.


## Action Execution Details

Clicking on an **Action Execution** node allows users to:

- View details about the associated operation.
- Navigate to the specific Datastore Operation for further analysis.

!!! info
    For failed action executions, clicking the node will provide access to detailed logs that explain the issue.


## Deleting a Flow Execution

There are two ways to delete a flow execution:

1. **From the List:**  
   Click the **trash icon** to the right of the flow execution item in the list.

2. **From the Details Page:**  
   Click on the flow execution item to open the details page, then click the **gear icon** in the top-right corner. Select the **Delete** option from the menu.

!!! info
    An alert notification will appear, warning that this action cannot be undone.
