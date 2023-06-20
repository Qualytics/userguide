# What is a Tag?

* `Tags` in our system allow users to categorize and organize entities effectively, while also providing the ability to assign weights for prioritization. They can drive notifications and downstream workflows, and users can configure tags, associate notifications based on tags, and associate tags to specific properties.

#### Key Points


* **Versatile Labeling**
    * `Tags` can be applied to `Datastores`, `Profiles`, `Fields`, `Check's`, and/or `Anomalies`.
* **Notification and Workflow Integration**
    * `Tags` are utilized to drive notifications and downstream workflows, enabling users to stay informed and take appropriate actions.
* **Weight Assignment**
    * Users can assign weights to tags, allowing for prioritization and emphasis on specific `Tags`.
* **Property Association**
    * `Tags` can be associated with specific properties, allowing for targeted actions and efficient management of entities across multiple datastores.
---
#### View Tags

* Find the `Tag` section by clicking on `Settings` in the menu bar:
 
  ![Screenshot](../assets/notifications/settings-tab-light.png#only-light)
  ![Screenshot](../assets/notifications/settings-tab-dark.png#only-dark)

* `Tags` is now the default tab:
 
  ![Screenshot](../assets/tags/tags-tab-light.png#only-light)
  ![Screenshot](../assets/tags/tags-tab-dark.png#only-dark)

* View all the active `Tags` or click `Add Tag` in the upper right corner:

  ![Screenshot](../assets/tags/tags-light.png#only-light)
  ![Screenshot](../assets/tags/tags-dark.png#only-dark)

---

#### Add a Tag

* To add a `Tag`, start with navigating to the top right and find the `Add Tag` button.

 ![Screenshot](../assets/tags/add-tag-light.png#only-light)
 ![Screenshot](../assets/tags/add-tag-dark.png#only-dark)

* Clicking on the `Add` button will pop up a modal:

 ![Screenshot](../assets/tags/tag-screen-light.png#only-light)
 ![Screenshot](../assets/tags/tag-screen-dark.png#only-dark)

* Details:
    * `Name` your `Tag`
    * Select a `Color`:
        * Click into Hexadecimal number or select by clicking on the dropper to open a color picker
    * Enter a description, if desired
    * Select a `Weight`
         * The weight value directly correlates with the level of importance, where a higher weight indicates higher significance.
         * Ranges from -10 to 10

    
    
* Once a tag is created, it's ready to be associated with a `Datastore`, `Profile`, `Check`, `Notification` and ultimately an `Anomaly` in order to drive a Notification to a user. For more details of Tag association, please refer to [tag association](/userguide/checks/what-is-an-authored-check/#add-a-new-data-quality-check).