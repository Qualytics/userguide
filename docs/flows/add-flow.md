# Create a New Flow

Flows allow you to automate actions based on data operations, anomaly detection, or manual execution. When you create a new Flow, Qualytics automatically adds the base nodes you need to begin configuring the automation.

!!! note
    To create a Flow, you must have **Manager** role. For more details, see the [Team Permissions guide](../settings/security/team-permissions.md){target="_blank"}.

**Step 1**: Click on the **Add Flow** button from the top right corner.

![addflow](.././assets/flows/addflow-light-4.png)

A modal window will appear, allowing you to create a new Flow.  
Every Flow begins with two default nodes:

- **Flow Node** – Defines the Flow’s name, description, and activation state  
- **Trigger Node** – Defines when the Flow will start

![flowchart](.././assets/flows/flowchart-light-5.png)

## What You Configure Next

A Flow consists of three main node types. After creating a new Flow, you will configure each one:

### **1. Flow Entry**

Defines the Flow’s general information such as its name and description.

!!! info
    For more detailed information, review the [Flow Entry Documentation](../flows/flow-entry.md){target="_blank"}

### **2. Trigger Node**

Controls *when* the Flow starts (operation completes, anomaly detected, manual, etc.).  

!!! info
    For more detailed information, review the [Trigger Node Documentation](../flows/trigger-node.md){target="_blank"}

### **3. Actions Node**

Defines *what happens* after the Flow is triggered (operations, notifications, HTTP calls, etc.).  

!!! info
    For more detailed information, review the [Actions Node Documentation](../flows/overview-action.md){target="_blank"}