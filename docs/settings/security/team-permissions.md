---
# We need as much horizontal space as possible
hide:
  - toc
---

# Team Permissions

Admins are not subject to Team permissions and can therefore access all data assets. By contrast, users assigned the Member and Manager roles are subject to Team permissions which control the data assets they can interact with. 

Team permissions are granted at the Datastore level and extend to all data assets under that Datastore (Tables/View/Files, Fields, Quality Checks, Anomalies, etc...)

## Permission Matrix

Legend:

* `X` Has permission to perform the Action
* `-` Does not have permission to perform the Action


### Source Datastores

| Permission    | Action                              | Reporter   | Viewer   | Drafter   | Author   | Editor        |
|:--------------|:------------------------------------|:-----------|:---------|:----------|:---------|:--------------|
| Create        |                                     | -          | -        | -         | -        | Managers Only |
| Delete        |                                     | -          | -        | -         | -        | -             |
| List          |                                     | X          | X        | X         | X        | X             |
| View          |                                     | X          | X        | X         | X        | X             |
| Open          |                                     |            |          |           |          |               |
|               | Edit Settings                       | -          | -        | -         | -        | X             |
|               | Switch Enrichment                   | -          | -        | -         | -        | X             |
|               | Add Enrichment                      | -          | -        | -         | -        | Managers Only |
|               | Edit Scoring                        | -          | -        | -         | -        | X             |
|               | Create/Delete Computed Asset        | -          | -        | -         | -        | X             |
|               | Run Operation                       | -          | -        | -         | -        | X             |
| Overview      |                                     | X          | X        | X         | X        | X             |
| Activity      |                                     |            |          |           |          |               |
|               | View                                | X          | X        | X         | X        | X             |
|               | Manage Operations                   | -          | -        | -         | -        | X             |
|               | Manage Schedule Operations          | -          | -        | -         | -        | X             |
| Profiles      |                                     |            |          |           |          |               |
|               | View                                | X          | X        | X         | X        | X             |
|               | Delete                              | -          | -        | -         | -        | X             |
| Observability |                                     |            |          |           |          |               |
|               | View                                | X          | X        | X         | X        | X             |
| Checks        |                                     |            |          |           |          |               |
|               | View                                | X          | X        | X         | X        | X             |
|               | Create                              | -          | -        | X         | X        | X             |
|               | Save to draft                       | -          | -        | X         | X        | X             |
|               | Restore to draft                    | -          | -        | X         | X        | X             |
|               | Activate / Validate / Change Status | -          | -        | -         | X        | X             |
|               | Edit Metadata                       | -          | -        | -         | X        | X             |
| Anomalies     |                                     |            |          |           |          |               |
|               | View                                | X          | X        | X         | X        | X             |
|               | View Source Records                 | -          | X        | X         | X        | X             |
|               | Change Status                       | -          | -        | -         | X        | X             |
|               | Add Comment                         | -          | X        | X         | X        | X             |
| Preview       |                                     | -          | X        | X         | X        | X             |

### Enrichment Datastores

| Permission    | Action                              | Reporter   | Viewer   | Drafter   | Author   | Editor        |
|:--------------|:------------------------------------|:-----------|:---------|:----------|:---------|:--------------|
| Create        |                                     | -          | -        | -         | -        | Managers Only |
| Delete        |                                     | -          | -        | -         | -        | -             |
| List          |                                     | X          | X        | X         | X        | X             |
| View          |                                     | -          | X        | X         | X        | X             |
| Preview       |                                     | -          | X        | X         | X        | X             |

### Explore

| Permission    | Action                              | Reporter   | Viewer   | Drafter   | Author   | Editor        |
|:--------------|:------------------------------------|:-----------|:---------|:----------|:---------|:--------------|
| Insights      |                                     | X          | X        | X         | X        | X             |
| Activity      |                                     | X          | X        | X         | X        | X             |
| Profiles      |                                     | X          | X        | X         | X        | X             |
| Observability |                                     | X          | X        | X         | X        | X             |
| Checks        |                                     | X          | X        | X         | X        | X             |
| Anomalies     |                                     | X          | X        | X         | X        | X             |
|               | View Source Records                 | -          | X        | X         | X        | X             |


## Add Team

You can create a new team for efficient and secure data management. Teams make it easier to control who has access to what, help people work together better, keep things secure with consistent rules, and simplify managing and expanding user groups. You can assign permissions to the team, such as Editor, Author, Drafter, Viewer and Reporter access, by selecting the datastore and enrichment datastore to which you want them to have access. This makes data management easier.


**Step 1**: Click on the **Add Team** button located in the top right corner.

![add-team](../../assets/security/add-team-light-3.png#only-light)
![add-team](../../assets/security/add-team-dark-3.png#only-dark)

**Step 2**: A modal window will appear, providing the options for creating the team. Enter the required values to get started. 

| REF.     | FIELD        | ACTION     | EXAMPLE          |
|----------|--------------|------------|------------------|
|  1.      | Name         | Enter the name of the team  |   Data Insights Team  |
|  2.      | Description  |  Provide a brief description of the team.  |  Analyzes data to provide actionable insights, supporting data-driven decisions  |

![window](../../assets/security/description-light.png#only-light)
![window](../../assets/security/description-dark.png#only-dark)

### Permissions

Permissions decide what users can see, create, or manage based on their role. Each role is designed for specific tasks, giving users access to the tools and information they need without going beyond their limits. From Editors who manage advanced settings to Viewers with read-only access, these roles make it easy to use the system while keeping everything secure.

![permission](../../assets/security/permission-light.png#only-light)
![permission](../../assets/security/permission-dark.png#only-dark)

#### Editor

Editor role allows users to manage datastore functions comprehensively. They can handle tasks such as controlling enrichment, scoring, computed fields, and operations.

![editor](../../assets/security/editor-light.png#only-light)
![editor](../../assets/security/editor-dark.png#only-dark)

| Feature | Operation | Can View/Can Run | Can Manage |
| :---- | :---- | :---- | :---- |
| **Datastoes** | Add Datastore |  | **✓** |
|  | Edit Settings |  | **✓** |
| **Enrichment** | Add Enrichment |  | **✓** |
|  | Edit Enrichment |  | **✓** |
| **Scoring** | Edit Scoring |  | **✓** |
| **Computed Field** | Add Computed |  | **✓** |
| **Operation** | Run Operation | **✓** | **✓** |
|  | Manage Operation |  | **✓** |
|  | Manage Scheduled Operation |  | **✓** |
| **Profiles** | Add Computed |  | **✓** |
|  | Delete Computed |  | **✓** |
| **Field Context** | Edit Field Context |  | **✓** |
|  | Delete Field Context |  | **✓** |

#### Author

Author role focuses on managing checks within the system. Users can activate, validate, change the status of checks, and edit their metadata. It is specifically designed for handling these functions efficiently.

![author](../../assets/security/author-light.png#only-light)
![author](../../assets/security/author-dark.png#only-dark)

| Feature | Functionality | Can View/ Can Run | Can Edit |
| :---- | :---- | :---- | :---- |
| **Source Datastore** | Checks |  | **✓** |
|  | Activate Checks |  | **✓** |
|  | Validate Checks |  | **✓** |
|  | Change Status of Checks |  | **✓** |
|  | Edit Metadata |  | **✓** |
|  | Anomalies |  | **✓** |
| **Anomalies** | Change Status of Anomalies |  | **✓** |

#### Drafter

Drafter role is designed specifically for adding and saving data within the system. Users can create new, make edits to existing ones, and save their progress as drafts. It is focused on these basic functions without access to advanced features or management tasks.

![drafter](../../assets/security/drafter-light.png#only-light)
![drafter](../../assets/security/drafter-dark.png#only-dark)

| Feature | Functionality | Can View | Can Edit |
| :---- | :---- | :---- | :---- |
| **Source Datastore** | Open Datastore | **✓** |  |
|  | Add Checks |  | **✓** |
| **Profiles** | Add Check  |  | **✓** |
| **Checks** | Create as Draft |  | **✓** |
| **Field Context** | Add Check |  | **✓** |

#### Viewer

Viewer role is focused on viewing anomalies within the system and creating notes as needed. It offers read-only access while allowing users to add comments to document their observations.

![viewer](../../assets/security/viewer-light.png#only-light)
![viewer](../../assets/security/viewer-dark.png#only-dark)

| Features | Functionality | Can View | Can Edit |
| :---- | :---- | :---- | :---- |
| **Source Datastore** | Anomalies | **✓** |  |
|  | Add Comment | **✓** |  |
|  | Preview(Container) | **✓** |  |
| **Enrichment Datastore** | View | **✓** |  |
|  | Preview | **✓** |  |
| **Explore** | Anomalies | **✓** |  |
|  | Source Records | **✓** |  |

#### Reporter

Reporter role provides access to all report-related information, including dashboards, overviews, checks, anomalies, fields, containers, and datastores. It is intended for users who need to view and analyze data to generate reports.

![reporter](../../assets/security/reporter-light.png#only-light)
![reporter](../../assets/security/reporter-dark.png#only-dark)

| Feature | Operation | Can View | Can Edit |
| :---- | :---- | :---- | :---- |
| **Source Datastore** | List | **✓** |  |
|  | View | **✓** |  |
|  | Overview | **✓** |  |
|  | Activity | **✓** |  |
|  | Profiles | **✓** |  |
|  | Observability | **✓** |  |
|  | Checks | **✓** |  |
|  | Anomalies | **✓** |  |
|  | Fields(Containers)  | **✓** |  |
| **Enrichment Datastores** | List | **✓** |  |
| **Explore** | Insights | **✓** |  |
|  | Activity | **✓** |  |
|  | Profiles | **✓** |  |
|  | Observability | **✓** |  |
|  | Checks | **✓** |  |
|  | Anomalies | **✓** |  |

![team](../../assets/security/det-light.png#only-light)
![team](../../assets/security/det-dark.png#only-dark)

| REF.     | FIELD        | ACTION     | EXAMPLE          |
|----------|--------------|------------|------------------|  
|  4.      | Users | Add users to the team | John, Michael |
|  5.      | Source Datastores | Grant access to specific source datastores (single or multiple) for the team | Athena |
|  6.      | Enrichment Datastores | Add and grant access to additional enrichment datastores (single or multiple) for the team  | Bank Enrichment |

**Step 3**: Click on the **Save** button to save your team.

![save-new-team](../../assets/security/save-new-team-light-5.png#only-light)
![save-new-team](../../assets/security/save-new-team-dark-5.png#only-dark)

After clicking on the **Save** button, your team is created, and a success message will appear saying, **Team successfully created**.

![team-created](../../assets/security/team-created-light-6.png#only-light)
![team-created](../../assets/security/team-created-dark-6.png#only-dark)
