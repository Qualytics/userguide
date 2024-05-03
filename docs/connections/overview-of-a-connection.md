# Overview

Connections facilitate the management of datastores by allowing you to share common connection parameters across multiple datastores.

## Setting Up Connections

### Creating a Connection
When you create your first datastore, a Connection is automatically generated using the parameters you provide. This Connection can then be used for other datastores with similar configuration needs.

![Screenshot](../assets/connections/add-datastore-connection-modal-light.png#only-light){: style="width:450px"}
![Screenshot](../assets/connections/add-datastore-connection-modal-dark.png#only-dark){: style="width:450px"}


**Example:**

1. Click on **Add Source Datastore**.
    - ![Screenshot](../assets/datastores/what-is/add-new-datastore-button-light.png#only-light)
      ![Screenshot](../assets/datastores/what-is/add-new-datastore-button-dark.png#only-dark)
3. Enter the necessary connection parameters (e.g., hostname, database name, user credentials).
4. After saving, a Connection is created and linked to your datastore, ready for reuse.

### Attaching a Datastore to an Existing Connection
For subsequent datastores that require the same connection parameters, you can attach them to an already existing Connection.

**Example:**

1. Open the **Create Datastore** form.
2. Select **Use an existing connection**.
    - ![Screenshot](../assets/connections/add-datastore-modal-light.png#only-light){: style="width:450px"}
      ![Screenshot](../assets/connections/add-datastore-modal-dark.png#only-dark){: style="width:450px"}
3. Pick the desired Connection from a dropdown list.
    - ![Screenshot](../assets/connections/connections-list-light.png#only-light){: style="width:450px"}
      ![Screenshot](../assets/connections/connections-list-dark.png#only-dark){: style="width:450px"}
4. Provide any additional details required for the new datastore (e.g., database name, root path).

## Managing Connections
The **Connections** section allows you to modify or delete your connections as your configuration needs evolve.

![Screenshot](../assets/connections/connections-tab-light.png#only-light){: style="width:450px"}
![Screenshot](../assets/connections/connections-tab-dark.png#only-dark){: style="width:450px"}

### Editing a Connection
1. Go to the **Connections** section.
    - ![Screenshot](../assets/connections/connections-table-light.png#only-light)
      ![Screenshot](../assets/connections/connections-table-dark.png#only-dark)
2. Choose the Connection you want to adjust and click in edit.
    - ![Screenshot](../assets/connections/connection-menu-button-light.png#only-light){: style="width:150px"}
      ![Screenshot](../assets/connections/connection-menu-button-dark.png#only-dark){: style="width:150px"}
3. Update the necessary fields and click **Save**.
    - ![Screenshot](../assets/connections/update-connection-light.png#only-light){: style="width:350px"}
      ![Screenshot](../assets/connections/update-connection-dark.png#only-dark){: style="width:350px"}


## Conclusion
Using Connections optimizes datastore management by enabling the reuse of connection parameters, making the process more streamlined and organized.
