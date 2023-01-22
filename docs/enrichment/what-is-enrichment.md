# What is an Enrichment Datastore?

* An `Enrichment Datastore` is a `Datastore` that is used to record `enrichment data` - `anomalies` and `metadata` for a `Datastore` as part of a Scan Operation. Any writable Datastore is a valid Enrichment Location, including the Primary Datastore being analyzed.

!!! info
    Before running a Scan Operation, the user should configure an Enrichment Datastore for each datastore.

*  An `Enrichment Datastore` is a medium holding structured data. Qualytics supports Spark-compatible Datastores via conceptual layers.

* The `Add Enrichment Datastore` flow will prompt the user for an Enrichment Location with three options:

    1. `In Place` - the enrichment data will be written to the datastore itself. This requires the configured credentials to support writing.
    2. `External` - the enrichment data will be written to a separate datastore. 
    3. `None` - no enrichment data will be recorded for this datastore. This severely limits functionality for anomaly detection.
