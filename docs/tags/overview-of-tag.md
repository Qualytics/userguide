# Tags

Tags allow users to categorize and organize data assets effectively and provide the ability to assign weights for prioritization. They drive notifications and downstream workflows, enabling users to stay informed and take appropriate actions. Tags can be configured and associated with specific properties, allowing for targeted actions and efficient management of entities across multiple datastores. 

Tags can be applied to Datastores, Profiles, Fields, Checks, and Anomalies, streamlining data management and improving workflow efficiency. Overall, tags enhance organization, prioritization, and decision-making.

Let’s get started 🚀

## Navigation to Tags

**Step 1**: Log in to your Qualytics account and click on the **Tags** on the left side panel of the interface. 

![tags](../assets/tags/tags-light-1.png#only-light)
![tags](../assets/tags/tags-dark-1.png#only-dark)

You will be navigated to the **Tags** section, where you can view all the tags available in the system.

![tags-section](../assets/tags/tags-section-light-2.png#only-light)
![tags-section](../assets/tags/tags-section-dark-2.png#only-dark)

## Add Tag

**Step 1**: Click on the **Add Tag** button from the top right corner.

![add-tag](../assets/tags/add-tag-light-3.png#only-light)
![add-tag](../assets/tags/add-tag-dark-3.png#only-dark)

**Step 2**: A modal window will appear, providing the options to create the tag. Enter the required values to get started. 

| REF. | FIELD | ACTION | EXAMPLE |
|------|-----------------|-------------------|----------------|
| 1.   | Preview | This shows how the tag will appear to users. | Preview |
| 2.   | Name | Assign a name to your tag. | Sensitive  |
| 3.   | Color | A color picker feature is provided, allowing you to select a color using its hex code.|  #E74C3C |
| 4.   | Description | Explain the nature of your tag. | Maintain data that is highly confidential and requires strict access controls.|
| 5.   | Category | Choose an existing category or create a new one to group related tags for easier organization.|Demo2|
| 6.   | Weight Modifier | Adjust the tag's weight for prioritization, where a higher value represents greater significance. The range is between -10 and 10.| 10 |

![tag-details](../assets/tags/tag-details-light-4.png#only-light)
![tag-details](../assets/tags/tag-details-dark-4.png#only-dark)

**Step 3**: Click on the **Save** button to save your tag.

![save-tag](../assets/tags/save-tag-light-5.png#only-light)
![save-tag](../assets/tags/save-tag-dark-5.png#only-dark)

## View Created Tags

Once you have created a tag, you can view it in the tags list.

![view-tag](../assets/tags/view-tag-light-6.png#only-light)
![view-tag](../assets/tags/view-tag-dark-6.png#only-dark)

## Filter and Sort 

Qualytics allows you to sort and filter your tags so that you can easily organize and find the most relevant tags according to your criteria, improving data management and workflow efficiency.

### Sort

You can sort your tags by **Color**, **Created Date**, **Name**, and **Weight** to easily organize and prioritize them according to your needs.

![sort-tag](../assets/tags/sort-tag-light-7.png#only-light)
![sort-tag](../assets/tags/sort-tag-dark-7.png#only-dark)

### Filter 

You can filter your tags by type and category, which allows you to categorize and manage them more effectively. 
 
#### Filter by Type

 Filter by Type allows you to view and manage tags based on their origin. You can filter between **Global tags** created within the platform and **External tags** imported from integrated systems like Atlan or Alation.

1. **External Tags**: External tags are metadata labels imported from an integrated data catalog system, such as Atlan or Alation, into Qualytics. These tags are synchronized automatically via API integrations and cannot be created or edited manually within Qualytics. They help ensure consistency in data tagging across different platforms by using the same tags already established in the data catalog. **Example**: If Atlan has a tag named **Customer,** once integrated, this tag will automatically be synchronized and added to Qualytics as an external tag.

2. **Global Tags**: Global tags are metadata labels that are created and managed directly within Qualytics. These tags are not influenced by external integrations and are used internally within the Qualytics platform to organize and categorize data according to the users' requirements. **Example**: A tag created within Qualytics to mark datasets that need internal review. This tag is fully managed within the Qualytics platform and remains unaffected by external data catalog systems unless the Overwrite Tags option is enabled in the Integration configuration.

![filter-tag](../assets/tags/filter-tag-light-8.png#only-light)
![filter-tag](../assets/tags/filter-tag-dark-8.png#only-dark)

#### Filter by Category

**Filter by Category** allows you to organize and manage tags based on predefined groups or categories. By applying this filter, you can quickly locate tags that belong to a specific category, improving searchability and making it easier to manage large volumes of data.

![filter-tag](../assets/tags/filter-tag-light-88.png#only-light)
![filter-tag](../assets/tags/filter-tag-dark-88.png#only-dark)

## Manage Tags

You can easily manage your tags by keeping them updated with current information and removing outdated or unnecessary tags. This ensures that your data remains organized and relevant, enhancing overall efficiency and workflow. By efficiently managing tags, you improve data handling and ensure high data standards across the platform.

### Edit Tags

This allows you to keep your tags updated with current information and relevance.

**Step 1**: Click the **vertical ellipsis (⋮)** next to the tag that you want to edit, then click on **Edit** from the dropdown menu.

![edit-tag](../assets/tags/edit-tag-light-9.png#only-light)
![edit-tag](../assets/tags/edit-tag-dark-9.png#only-dark)

**Step 2**: Edit the tag's **name**, **color**, **description**, **category** and **weight** as needed.

![edit-details](../assets/tags/edit-details-light-10.png#only-light)
![edit-details](../assets/tags/edit-details-dark-10.png#only-dark)

**Step 3**: Click the **Save** button to apply your changes.

![save-edit](../assets/tags/save-edit-light-11.png#only-light)
![save-edit](../assets/tags/save-edit-dark-11.png#only-dark)

### Delete Tags

This allows you to remove outdated or unnecessary tags to maintain a clean and efficient tag system.

**Step 1**: Click the **vertical ellipsis (⋮)** next to the tag that you want to delete, then click on **Delete** from the dropdown menu.

![delete](../assets/tags/delete-light-12.png#only-light)
![delete](../assets/tags/delete-dark-12.png#only-dark)

**Step 2**: After clicking the **Delete** button, your tag will be removed from the system, and a success message saying **Tag successfully deleted**.

![tag-deleted](../assets/tags/tag-deleted-light-13.png#only-light)
![tag-deleted](../assets/tags/tag-deleted-dark-13.png#only-dark)

## Applying a Tag
Once a Tag is created, it's ready to be associated with a ```Datastore```, ```Profile```, ```Check```, ```Notification``` and ultimately an ```Anomaly```.

### Tag Inheritance

- When a ```Tag``` is applied to a data asset, all the descendents of that data asset also receive the ```Tag```.

    - For example, if a ```Tag``` named **Critical** is applied to a Datastore then all the Tables, Fields, and Checks under that Datastore also receive the ```Tag```.

    !!! note

        Anomalies will inherit the tags if a scan has been run.

- Likewise, if the **Critical** ```Tag``` is subsequently removed from one of the Tables in that Datastore, then all the Fields and Checks belonging to that Table will have the **Critical** ```Tag``` removed as well.

- When a new data asset is created, it inherits the ```Tags``` from the owning data asset. For example, if a user creates a new Computed Table, it inherits all the ```Tags``` that are applied to the Datastore in which it is created.

### Tagging Anomales

- Anomalies also inherit ```Tags``` at the time they are created. They inherit all the ```Tags``` of all the associated failed checks.

- Thus Anomalies do not inherit subsequent tag changes from those checks. They only inherit checks one time - at creation time.

- ```Tags``` can be directly applied to or removed from Anomalies at any time after creation.
