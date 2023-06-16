# What is a Tag?

* Tags are user-defined labels that can be applied to data assets (Datastores, Tables, Files, Fields, etc..) and `Anomalies`.
* Tags are used to organize data assets for ease of inspection and reporting through [Global Explore](/docs/explore/global-explore.md)
* Tags are also used to drive `notifications` through notification rules that respond to events from tagged data assets and `Anomalies`.

Administrators can maange `Tags` under Settings.
---

* Find the `Tag` section by clicking on `Settings` in the menu bar:

  ![Screenshot](../assets/notifications/settings-tab-light.png#only-light)
  ![Screenshot](../assets/notifications/settings-tab-dark.png#only-dark)

* In `Settings` find the `Tag` tab:

  ![Screenshot](../assets/tags/tags-tab-light.png#only-light)
  ![Screenshot](../assets/tags/tags-tab-dark.png#only-dark)

* View all the active `tags` or `add` a new one:

  ![Screenshot](../assets/tags/tags-light.png#only-light)
  ![Screenshot](../assets/tags/tags-dark.png#only-dark)

---

# Create a Tag

* To create a `Tag`, start with navigating to the top right and find the `Add` button.

 ![Screenshot](../assets/tags/add-tag-light.png#only-light)
 ![Screenshot](../assets/tags/add-tag-dark.png#only-dark)

* Clicking on the `Add` button will pop up a modal:

 ![Screenshot](../assets/tags/tag-screen-light.png#only-light)
 ![Screenshot](../assets/tags/tag-screen-dark.png#only-dark)

* Details:
    * `Name` is the name of the tag.
    * `Color Pickup`:
        * Select any color for the specific Tag
        * Use Hexadecimal number or select by clicking on the color picker

* Once a tag is created, it's ready to be applied to a data asset or used in a notification rule.

# Applying a Tag

## Tag Inheritance
When a tag is applied to a data asset, all the descendents of that data asset also receive the tag. For example, if a tag named "Critical" is applied to a Datastore then all the Tables, Fields, and Checks under that Datastore also receive the tag.
Likewise, if the "Critical" tag is subsequently removed from one of the Tables in that Datastore, then all the Fields and Checks belonging to that Table will have the "Critical" tag removed as well.

When a new data asset is created, it inherits the tags from the owning data asset.  For example, if a user creates a new Computed Table, it inherits all the tags that are applied to the Datastore in which it is created.

## Tagging Anomales

Anomalies also inherit tags at the time they are created. They inherit all the tags of all the associated failed checks. However, anomalies are treated as metadata, not as data assets, for the purposes of tagging. Thus Anomalies do not inherit subsequent tag changes from those checks. They only inherit checks one time - at creation time.  Tags can be directly applied to or removed from Anomalies at any time after creation.

