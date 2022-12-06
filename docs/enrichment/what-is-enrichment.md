# What is an Enrichment Store?

* An `Enrichment Store` is a `Data Store` that is used to record `enrichment data` - `anomalies` and `metadata` for a `Data Store` as part of a Scan Operation. Any writable Data Store is a valid Enrichment Location, including the Primary Data Store being analyzed.

!!! info
    Before running a Scan Operation, the user should configure an Enrichment Store for each data store.

*  An `Enrichment Store` is a medium holding structured data. Qualytics supports Spark-compatible Data Stores via conceptual layers.

* The `Add Enrichment Store` flow will prompt the user for an Enrichment Location with three options:

    1. `In Place` - the enrichment data will be written to the datastore itself. This requires the configured credentials to support writing.
    2. `External` - the enrichment data will be written to a separate datastore. 
    3. `None` - no enrichment data will be recorded for this datastore. This severely limits functionality for anomaly detection.
