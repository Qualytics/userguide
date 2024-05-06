# Overview

The `Tags` allow users to categorize and organize entities effectively, while also providing the ability to assign weights for prioritization. They can drive notifications and downstream workflows, and users can configure tags, associate notifications based on `Tags`, and associate tags to specific properties.

### Key Points


* **Versatile Labeling**
    `Tags` can be applied to `Datastores`, `Profiles`, `Fields`, `Check's`, and/or `Anomalies`.
* **Notification and Workflow Integration**
    `Tags` are utilized to drive notifications and downstream workflows, enabling users to stay informed and take appropriate actions.
* **Weight Assignment**
    Users can assign weights to `Tags`, allowing for prioritization and emphasis on specific `Tags`.
* **Property Association**
    `Tags` can be associated with specific properties, allowing for targeted actions and efficient management of entities across multiple datastores.

### Tags View

1. Find the `Tag` section by clicking on `Settings` in the menu bar:
 
    ![Screenshot](../../assets/notifications/settings-tab-light.png#only-light){: style="width:300px;"}
    ![Screenshot](../../assets/notifications/settings-tab-dark.png#only-dark){: style="width:300px;"}

    ![Screenshot](../../assets/tags/tags-tab-light.png#only-light){: style="width:400px;"}
    ![Screenshot](../../assets/tags/tags-tab-dark.png#only-dark){: style="width:400px;"}

* View all the active `Tags` or click `Add Tag` in the upper right corner:

    ![Screenshot](../../assets/tags/tags-light.png#only-light)
    ![Screenshot](../../assets/tags/tags-dark.png#only-dark)

### Add a Tag

1. To add a `Tag`, start with navigating to the top right and find the `Add Tag` button.

    ![Screenshot](../../assets/tags/add-tag-light.png#only-light)
    ![Screenshot](../../assets/tags/add-tag-dark.png#only-dark)

* Clicking on the `Add` button will pop up a modal:

    ![Screenshot](../../assets/tags/tag-screen-light.png#only-light)
    ![Screenshot](../../assets/tags/tag-screen-dark.png#only-dark)

    * `Name` your `Tag`
    * Select a `Color`:
        * Click into Hexadecimal number or select by clicking on the dropper to open a color picker
    * Enter a description, if desired
    * Select a `Weight`
         * The weight value directly correlates with the level of importance, where a higher weight indicates higher significance.
         * Ranges from -10 to 10

### Applying a Tag

Once a `Tag` is created, it's ready to be associated with a `Datastore`, `Profile`, `Check`, `Notification` and ultimately an `Anomaly`.


#### Tag Inheritance

* When a `Tag` is applied to a data asset, all the descendents of that data asset also receive the `Tag`. 
    * For example, if a `Tag` named **Critical** is applied to a Datastore then all the Tables, Fields, and Checks under that Datastore also receive the `Tag`. 
* Likewise, if the **Critical** `Tag` is subsequently removed from one of the Tables in that Datastore, then all the Fields and Checks belonging to that Table will have the **Critical**  `Tag` removed as well.

* When a new data asset is created, it inherits the `Tags` from the owning data asset. For example, if a user creates a new Computed Table, it inherits all the `Tags` that are applied to the Datastore in which it is created.

#### Tagging Anomales

* Anomalies also inherit `Tags` at the time they are created. They inherit all the `Tags` of all the associated failed checks. 
* However, anomalies are treated as metadata, not as data assets, for the purposes of tagging. 
    * Thus Anomalies do not inherit subsequent tag changes from those checks. They only inherit checks one time - at creation time. 
* `Tags` can be directly applied to or removed from Anomalies at any time after creation.