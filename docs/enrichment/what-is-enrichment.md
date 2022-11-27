# What is an Enrichment Store?

* An `Enrichment Store` is also a `Datastore` and it is used for recording `enrichment data` for a `Datastore` as part of a Scan Operation. Any writable Datastore is a valid Enrichment Location, including the Datastore itself.

!!! info
    Before running a Scan Operation, the user needs to configure an Enrichment Store for each data store.

*  An `Enrichment Store` is a medium holding structured data. Qualytics supports Spark-compatible Data Stores via the conceptual layers.

* The add `Enrichment Store` flow should prompt to you for an Enrichment Location with three options:

    1. `In place` - the enrichment data will be written to the datastore itself. This requires the configured credentials to support writing.
    2. `External` - the enrichment data will be written to a separate datastore. 
    3. `None` - no enrichment data will be recorded for this datastore. This severely limits functionality.
