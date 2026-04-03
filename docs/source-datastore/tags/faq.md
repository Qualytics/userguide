# Datastore Tags FAQ

Answers to common questions about assigning, unassigning, and managing tags specifically on source datastores in Qualytics.

<!-- TODO: Update link to tags/overview-of-a-tag.md when the dedicated Tags overview page is created -->
!!! info "General Tags FAQ"
    For questions about creating, editing, or deleting tags globally (not specific to datastores), see the [Tags](../../tags/overview.md){:target="_blank"} documentation.

## Assigning and Unassigning

### What happens when I assign a tag to a datastore?

The tag is applied to the datastore and **automatically inherits** to all child assets — containers (tables/files), fields (columns), quality checks, and anomalies. You don't need to tag each asset individually.

### Can a datastore have multiple tags?

Yes. You can assign as many tags as needed to a single datastore. There is no maximum limit on the number of tags per datastore.

### Can I use the same tag across multiple datastores?

Yes. Tags are global — a single tag like `Production` can be assigned to any number of datastores across your organization.

### Does unassigning a tag delete it?

No. Unassigning a tag from a datastore only removes the association. The tag itself remains available in the system and can be assigned to other datastores.

### Can I create tags from the datastore view?

Yes. When assigning a tag, you can create a new tag directly from the tag selector menu by typing a name that doesn't exist yet. You need at least the **Editor** role to create new tags.

### Who can assign tags to datastores?

Users with the **Editor** role or above can assign and unassign tags on datastores. See the [Permissions](permissions.md){:target="_blank"} page for the full matrix.

## Inheritance

### If I assign a tag to a container directly, does it propagate up to the datastore?

No. Tag inheritance is **one-way (top-down only)**. Tags assigned at the datastore level cascade down to containers, fields, checks, and anomalies. But tags assigned directly to a container do **not** propagate up to the datastore.

### Do tags cascade to anomalies that already exist?

Yes. When you assign a tag to a datastore, the tag cascades immediately to **all existing** containers, fields, and checks within the datastore. Anomalies inherit tags through their associated checks — so existing anomalies linked to tagged checks will reflect the tag.

### Is tag inheritance immediate or delayed?

Immediate. Tag changes cascade synchronously within the same operation — there is no background processing or delay.

## Visibility and Tag Types

### When I assign a tag to a datastore, does everyone see it?

It depends on the tag type. **Global, External, Entity, and Lineage** tags are organization-wide — every user with access to the datastore will see them. **Personal** tags are private and visible only to you.

### What is the difference between Global, External, Entity, Lineage, and Personal tags?

- **Global** — User-created, organization-wide tags. The most common type.
- **External** — Tags synced from external integrations (data catalogs, governance platforms). Read-only.
- **Entity** — Pre-defined system classification tags.
- **Lineage** — Hierarchical tags that support parent-child relationships.
- **Personal** — User-specific private tags, visible only to the user who assigned them.

### What are External tags and where do they come from?

External tags are automatically synced from external integrations such as data catalogs and governance platforms (e.g., Atlan, Collibra). They are **read-only** — you cannot create or edit them manually. If an external tag becomes disassociated from all assets, it is automatically cleaned up.

## Operations

### Can I use tags to filter which containers are included in a Profile or Scan operation?

Yes. When running or scheduling a Profile or Scan operation, you can specify **container tags** to scope the operation to only those containers that have the specified tags.

### Can I combine tag filtering with container selection?

No. Tags and container selection are mutually exclusive in operations — you can filter by tags **or** by specific container names/IDs, but not both at the same time.

## Quality Score

### How does the tag weight modifier affect quality scores?

Each tag has a **weight modifier** (range: -10 to 10, default: 1). When tags are assigned to a datastore, the weight modifiers of all tags on each container are summed and used to calculate the relative importance of that container in the overall quality score. Higher-weighted containers have more impact on the datastore's quality score. See the [Weighting](../../weight/weighting.md){:target="_blank"} documentation for details.

### Does removing a tag recalculate quality scores?

Yes. When you unassign a tag that has a weight modifier, the quality scores for all containers in the datastore are automatically recalculated.

## Bulk Operations

### Can I assign tags to multiple datastores at once?

Yes, but only during **multi-schema creation**. When creating multiple datastores via the bulk creation flow (`POST /api/connections/{id}/datastores/bulk`), you can include a `tags` field — all datastores created in the batch will receive the same tags. See the [API](api.md#bulk-tag-assignment-multi-schema-creation){:target="_blank"} page for details.

### Can I remove tags from multiple datastores at once?

No. There is no dedicated bulk endpoint for removing tags from multiple existing datastores. You need to update each datastore individually via `PUT /api/datastores/{id}` with the updated tag list.

## API

### Is there a dedicated API endpoint for assigning tags?

No. Tags are managed through the `PUT /api/datastores/{id}` endpoint by passing the desired tag list in the `tags` field. See the [API](api.md){:target="_blank"} page for examples.

### What happens if I include a tag name that doesn't exist yet in the API?

Qualytics will automatically create it as a **Global** tag. This works for any user with the **Editor** role or above — no separate Admin permission is needed for auto-creation via the API.

### Are there rate limits on tag assignment via the API?

There are no tag-specific rate limits. Standard API rate limits apply to all endpoints, including `PUT /api/datastores/{id}`. See the [API docs](https://demo.qualytics.io/api/docs){:target="_blank"} for rate limit details.
