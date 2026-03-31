# Unassign a Tag from a Datastore

Removing a tag from a datastore is useful when a datastore no longer belongs to a particular category, compliance scope, or environment. When you unassign a tag, it is automatically removed from all child assets (containers, fields, checks, and anomalies) within the datastore.

!!! warning "Side Effects"
    When you unassign a tag from a datastore, the tag is **automatically removed** from all containers, fields, checks, and anomalies within the datastore. If the tag has a **weight modifier** configured, quality scores for all containers in the datastore will be **recalculated** to reflect the new weighting.

!!! note
    Unassigning a tag from a datastore does **not** delete the tag itself — it only removes the association. The tag remains available for use on other datastores.

## Steps

**Step 1**: Log in to your Qualytics account and select the **datastore** from the left menu from which you want to unassign a tag.

![select-datastore](../../assets/source-datastores/tags/shared/step-1-select-datastore.png)

**Step 2**: Click on **Assign tags to this datastore** located at the bottom-left corner of the interface to open the tag dropdown.

![assign-tags-button](../../assets/source-datastores/tags/unassign-tags/step-2-assign-tags-button.png)

**Step 3**: A drop-up menu will appear with the list of currently assigned tags. Click the **remove button** (X) next to the tag you want to unassign.

![remove-tag](../../assets/source-datastores/tags/unassign-tags/step-3-remove-tag.png)

**Step 4**: The tag will be unselected and instantly removed from the datastore. All related containers, fields, checks, and anomalies will be updated.

![tag-unselected](../../assets/source-datastores/tags/unassign-tags/step-4-tag-unselected.png)

!!! info "Assign a Tag"
    To learn how to assign a tag to a datastore, see the [Assign a Tag](assign-tags.md) documentation.
