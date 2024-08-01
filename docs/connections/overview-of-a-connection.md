# Connections Overview

Connections facilitate the management of datastores by allowing you to share common connection parameters across multiple datastores.

## Setup a Connection

When you create your first datastore, a Connection is automatically generated using the parameters you provide. This Connection can then be used for other datastores with similar configuration needs.

![Screenshot](../assets/connections/add-datastore-connection-modal-light.png#only-light){: style="width:450px"}
![Screenshot](../assets/connections/add-datastore-connection-modal-dark.png#only-dark){: style="width:450px"}


**Example:**

1. Click on **Add Source Datastore**.
	
	![Screenshot](../assets/datastores/what-is/add-new-datastore-button-light.png#only-light)
	![Screenshot](../assets/datastores/what-is/add-new-datastore-button-dark.png#only-dark)

3. Enter the necessary connection parameters (e.g., hostname, database name, user credentials).
4. After saving, a Connection is created and linked to your datastore, ready for reuse.

### Reuse a Connection
For subsequent datastores that require the same connection parameters, you can reuse existing connections.

**Example:**

1. Open the **Create Datastore** form.
2. Select **Use an existing connection**.
	
	![Screenshot](../assets/connections/add-datastore-modal-light.png#only-light){: style="width:450px"}
    ![Screenshot](../assets/connections/add-datastore-modal-dark.png#only-dark){: style="width:450px"}

3. Pick the desired Connection from a dropdown list.

	![Screenshot](../assets/connections/connections-list-light.png#only-light){: style="width:450px"}
	![Screenshot](../assets/connections/connections-list-dark.png#only-dark){: style="width:450px"}

4. Provide any additional details required for the new datastore (e.g., database name, root path).

## Manage Connections

For managing the connections please see [Manage Connections](../settings/connections/manage-connections.md/).

## Conclusion
Using Connections optimizes datastore management by enabling the reuse of connection parameters, making the process more streamlined and organized.
