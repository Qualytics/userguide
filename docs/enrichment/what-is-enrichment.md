# What is an Enrichment Store?

* An `Enrichment Store` is also a `Datastore` and it is used for recording `e`nrichment data` for a `Datastore` as part of a Scan Operation. Any writable Datastore is a valid Enrichment Location, including the Datastore itself.

*  An `Enrichment Store` is a medium holding structured data. Qualytics supports Spark-compatible Data Stores via the conceptual layers.

* The add `Enrichment Store` flow should prompt to you for an Enrichment Location with three options:

    1. `In place` - the enrichment data will be written to the datastore itself. This requires the configured credentials to support writing.
    2. `External` - the enrichment data will be written to a separate datastore. 
    3. `None` - no enrichment data will be recorded for this datastore. This severely limits functionality.

---




# Running a Catalog of the Data Store
* The first operation of Catalog will automatically kick off. You can see this through the Operations tab. 
    * This operation typically takes a short amount of time to complete. 
    * After this is completed, they’ll need to run a Profile operation (under Run > Profile) to generate metadata and infer data quality checks. 

    ![Screenshot](../assets/datastores/what-is/running-profile.png)
