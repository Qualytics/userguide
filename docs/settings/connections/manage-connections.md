# Connections

The Connections Management section allows you to manage global configurations for various connections to different data sources. This provides you with a centralized interface for managing all the data connections, ensuring efficient data integration and enrichment processes. You can easily navigate and manage your connections by utilizing the search, sort, edit, and delete features.

Let's get started 🚀

## Navigation to Connection

**Step 1**: Log in to your Qualytics account and click the **Settings** button on the left side panel of the interface. 

![global-setting](../../assets/connections/global-setting-light-1.png#only-light)
![global-setting](../../assets/connections/global-setting-dark-1.png#only-dark)

**Step 2**: By default, you will be navigated to the **Tags** section. Click on the **Connection** tab.

![connections](../../assets/connections/connections-light-2.png#only-light)
![connections](../../assets/connections/connections-dark-2.png#only-dark)

## Manage Connection

You can effectively manage your connections by editing, deleting, and adding datastores to maintain accuracy and efficiency.

!!! warning
    Before deleting a connection, ensure that all associated datastores and enrichment datastores have been removed.

### Edit Connection

You can edit connections to update details like name, account, role, warehouse, and authentication to improve performance. This keeps connection settings up-to-date and suited to your data needs.

!!! note
    You can only edit the connection name and connection details, but you are not able to edit the connector itself.

**Step 1**: Click the **vertical ellipsis (⋮)** next to the connection that you want to edit, then click on **Edit** from the dropdown menu.

![edit](../../assets/connections/edit-light-3.png#only-light)
![edit](../../assets/connections/edit-dark-3.png#only-dark)

**Step 2**: **Edit** the connection details as needed.

!!! note 
    Connection details vary from connection to connection, which means that each connection may have its unique configuration settings.

![connection-details](../../assets/connections/connection-details-light-4.png#only-light)
![connection-details](../../assets/connections/connection-details-dark-4.png#only-dark)

**Step 3**: Once you have updated the values, click on the **Save** button to apply your changes.

![save-connection](../../assets/connections/save-connection-light-5.png#only-light)
![save-connection](../../assets/connections/save-connection-dark-5.png#only-dark)

**Step 4**: After clicking the **Save** button, your connection will be updated, and a success message will display saying **The Connection has been successfully updated**.

![connection-updated](../../assets/connections/connection-updated-light-6.png#only-light)
![connection-updated](../../assets/connections/connection-updated-dark-6.png#only-dark)

### Delete Connection

This allows you to remove outdated or unnecessary connections to maintain a clean and efficient network configuration.

**Step 1**: Click the **vertical ellipsis (⋮)** next to the connection that you want to delete, then click on **Delete** from the dropdown menu.

![delete](../../assets/connections/delete-light-7.png#only-light)
![delete](../../assets/connections/delete-dark-7.png#only-dark)

**Step 2**: A modal window **Delete Connection** will appear.

!!! warning 
    Source Datastores and Enrichment Datastores associated must be removed before deleting the connection

![delete-window](../../assets/connections/delete-window-light-8.png#only-light)
![delete-window](../../assets/connections/delete-window-dark-8.png#only-dark)

**Step 3**: Enter the **Name of the Connection** in the given field (confirmation check) and then click on the **I’M SURE, DELETE THIS CONNECTION** button to delete the connection.

![confirm-delete](../../assets/connections/confirm-delete-light-9.png#only-light)
![confirm-delete](../../assets/connections/confirm-delete-dark-9.png#only-dark)

### Add Datastore

You can add new or existing datastores and enrichment datastores directly from the connection, making it easy to manage and access your data while ensuring all sources are connected and available.

**Step 1**: Click the **vertical ellipsis (⋮)** next to the connection where you want to add a datastore, then click on **Add Datastore** from the dropdown menu.

![add-datastore](../../assets/connections/add-datastore-light-10.png#only-light)
![add-datastore](../../assets/connections/add-datastore-dark-10.png#only-dark)

A modal window labeled **Add Datastore** will appear, giving you options to connect a datastore. For more information on adding a datastore, please refer to the [Configuring Datastores](https://userguide.qualytics.io/quick-start-guide/#datastore:~:text=the%20Qualytics%20platform.-,Configuring%20Datastores,-Qualytics%20allows%20you) section.

Once you have successfully added a datastore to the connection, a success message will appear saying, **Your datastore has been successfully added.**

![datastore-added](../../assets/connections/datastore-added-light-11.png#only-light)
![datastore-added](../../assets/connections/datastore-added-dark-11.png#only-dark)

### View Connection

Once you have added a new datastore and enrichment datastore, you can view them in the connections list.

![view-connections](../../assets/connections/view-connections-light-12.png#only-light)
![view-connections](../../assets/connections/view-connections-dark-12.png#only-dark)

### Sort Connection

You can sort your connections by **Name** and **Created Date** to easily find and manage them.

![sort-connection](../../assets/connections/sort-connection-light-13.png#only-light)
![sort-connection](../../assets/connections/sort-connection-dark-13.png#only-dark)

### Filter Connection

You can filter connections by selecting specific data source types from the dropdown menu, making it easier to locate and manage the desired connections.

![filter](../../assets/connections/filter-light-14.png#only-light)
![filter](../../assets/connections/filter-dark-14.png#only-dark)