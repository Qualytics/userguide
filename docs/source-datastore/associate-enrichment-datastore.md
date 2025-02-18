
# Link Enrichment Datastore

An enrichment datastore is a database used to enhance your existing data by adding additional, relevant information. This helps you to provide more comprehensive insight into data and improve data accuracy. 

You have the option to link an enrichment datastore to your existing source datastore. However, some datastores cannot be linked as enrichment datastores. For example, Oracle, Athena, Dremio, and Timescale cannot be used for this purpose.

When selecting an enrichment datastore, it is important to consider compatibility. It is not advisable to use blob storage as an enrichment datastore.

Let's get started 🚀

**Step 1:** Select a source datastore from the side menu for which you would like to configure **Link Enrichment.**

![Screenshot](../assets/enrichment/link-datastore/datastore-light.png#only-light)
![Screenshot](../assets/enrichment/link-datastore/datastore-dark.png#only-dark)

**Step 2:** Click on the **Settings** icon from the top right window and select the **Enrichment** option from the dropdown menu. 

![Screenshot](../assets/enrichment/link-datastore/settings-light.png#only-light)
![Screenshot](../assets/enrichment/link-datastore/settings-dark.png#only-dark)

A modal window- **Link Enrichment Datastore** will appear, providing you with two options to link an **enrichment datastore**.

![Screenshot](../assets/enrichment/link-datastore/link-enrichment-datastore-light.png#only-light)
![Screenshot](../assets/enrichment/link-datastore/link-enrichment-datastore-dark.png#only-dark)

| REF. | FIELDS | ACTIONS |
| :---- | :---- | :---- |
| 1. | Prefix | Add a prefix name to uniquely identify tables/files when Qualytics writes metadata from the source datastore to your enrichment datastore. |
| 2. | Caret Down Button | Click the caret down to select either **Use Enrichment Datastore** or **Add Enrichment Datastore**. |
| 3. | Enrichment Datastore | Select an enrichment datastore from the dropdown list. |

## Option I: Link New Enrichment

If the toggle **Add new connection** is turned on, then this will prompt you to link a new enrichment datastore from scratch without using existing connection details.

!!! note
    Connection details can vary from datastore to datastore. For illustration, we have demonstrated linking BigQuery as a new enrichment datastore.

**Step 1**: Click on the caret button and select **Add Enrichment Datastore**.

![Screenshot](../assets/enrichment/link-datastore/add-datastore-light.png#only-light)
![Screenshot](../assets/enrichment/link-datastore/add-datastore-dark.png#only-dark)

A modal window **Link Enrichment Datastore** will appear. Enter the following details to create an enrichment datastore with a new connection.

![Screenshot](../assets/enrichment/link-datastore/new-datastore-light.png#only-light)
![Screenshot](../assets/enrichment/link-datastore/new-datastore-dark.png#only-dark)

| REF. | FIELDS | ACTIONS |
| :---- | :---- | :---- |
| 1 | Prefix | Add a prefix name to uniquely identify tables/files when Qualytics writes metadata from the source datastore to your enrichment datastore. |
| 2 | Name | Give a name for the enrichment datastore. |
| 3 | Toggle Button for add new connection | Toggle ON to create a new enrichment from scratch or toggle OFF to reuse credentials from an existing connection. |
| 4 | Connector | Select a datastore connector from the dropdown list. |

**Step 2:** Add connection details for your selected **enrichment datastore** connector.

![Screenshot](../assets/enrichment/link-datastore/details-datastore-light.png#only-light)
![Screenshot](../assets/enrichment/link-datastore/details-datastore-dark.png#only-dark)

**Step 3**: After adding the source datastore details, click on the **Test Connection** button to check and verify its connection.  

![Screenshot](../assets/enrichment/link-datastore/test-light.png#only-light)
![Screenshot](../assets/enrichment/link-datastore/test-dark.png#only-dark)

If the credentials and provided details are verified, a success message will be displayed indicating that the connection has been verified.

**Step 4:** Click on  **Save** button.

![Screenshot](../assets/enrichment/link-datastore/save-light.png#only-light)
![Screenshot](../assets/enrichment/link-datastore/save-dark.png#only-dark)

**Step 5**: After clicking on the **Save** button a modal window will appear **Your Datastore has been successfully updated.**

![Screenshot](../assets/enrichment/link-datastore/window-light.png#only-light)
![Screenshot](../assets/enrichment/link-datastore/window-dark.png#only-dark)

## Option II: Link Existing Connection

If the **Use an existing enrichment datastore** option is selected from the dropdown menu, you will be prompted to link the enrichment datastore using existing connection details.

**Step 1**: Click on the caret button and select **Use Enrichment Datastore**.

![Screenshot](../assets/enrichment/link-datastore/caret-light.png#only-light)
![Screenshot](../assets/enrichment/link-datastore/caret-dark.png#only-dark)

**Step 2:** A modal window **Link Enrichment Datastore** will appear. Add a prefix name and select an existing enrichment datastore from the dropdown list.

![Screenshot](../assets/enrichment/link-datastore/link-light.png#only-light)
![Screenshot](../assets/enrichment/link-datastore/link-dark.png#only-dark)

| REF. | FIELDS | ACTIONS |
| :---- | :---- | :---- |
| 1. | Prefix | Add a prefix name to uniquely identify tables/files when Qualytics writes metadata from the source datastore to your enrichment datastore. |
| 2. | Enrichment Datastore | Select an enrichment datastore from the dropdown list. |

**Step 3:** View and check the connection details of the enrichment and click on the **Save** button.

![Screenshot](../assets/enrichment/link-datastore/save2-light.png#only-light)
![Screenshot](../assets/enrichment/link-datastore/save2-dark.png#only-dark)

**Step 4:** After clicking on the **Save** button a modal window will appear **Your Datastore has been successfully updated.**

![Screenshot](../assets/enrichment/link-datastore/window-light.png#only-light)
![Screenshot](../assets/enrichment/link-datastore/window-dark.png#only-dark)

When an Enrichment Datastore is linked, you can see a **green** light showing that the connection between the **Datastore** and the Enrichment Datastore are stable or red if it's unstable.

![Screenshot](../assets/enrichment/link-datastore/signal-light.png#only-light)
![Screenshot](../assets/enrichment/link-datastore/signal-dark.png#only-dark)

## Endpoint (Patch)

`/api/datastores/{datastore-id}/enrichment/{enrichment-id}` _(patch)_