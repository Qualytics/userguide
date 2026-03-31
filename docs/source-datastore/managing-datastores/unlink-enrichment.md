# Unlink Enrichment Datastore

Unlinking an enrichment datastore removes the connection between the source datastore and the enrichment target. After unlinking, no new enrichment data will be written during future Scan operations.

!!! warning "Side Effects"
    When you unlink an enrichment datastore, the remediation strategy is automatically reset to **None** and no new scan results will be persisted in the enrichment target. Historical enrichment data is **preserved** — existing tables are not deleted.

!!! note
    Unlinking requires the **Admin** role. You cannot unlink if the source datastore has active **Export** or **Materialize** operations in flows or scheduled operations.

## Steps

**Step 1**: Navigate to your datastore overview and click the **Settings :material-cog-outline:** button located at the top-right corner of the interface.

![settings-button](../../assets/source-datastores/enrichment-datastore/managing/shared/step-1-settings-button.png)

**Step 2**: A dropdown menu will appear. Click on **Enrichment :material-database-import-outline:** to open the enrichment datastore settings.

![enrichment-menu](../../assets/source-datastores/enrichment-datastore/managing/shared/step-2-enrichment-menu.png)

**Step 3**: A modal window — **Enrichment Datastore Settings** — will appear. Click the **Unlink Enrichment Datastore :material-link-off:** button located on the right side of the Details section.

![unlink-button](../../assets/source-datastores/enrichment-datastore/managing/unlink-enrichment/step-3-unlink-button.png)

**Step 4**: A confirmation dialog will appear warning that this action cannot be undone. Click **Unlink** to confirm.

![confirm-unlink](../../assets/source-datastores/enrichment-datastore/managing/unlink-enrichment/step-4-confirm-unlink.png)

**Step 5**: A success message will confirm that the datastore has been updated successfully.

![success](../../assets/source-datastores/enrichment-datastore/managing/unlink-enrichment/step-5-success.png)

!!! info "Link Enrichment Datastore"
    To link an enrichment datastore to a source datastore, see the [Link Enrichment Datastore](link-enrichment.md) documentation.
