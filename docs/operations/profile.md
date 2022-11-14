# Profile Operation

The Profile Operation is executed on a Datastore to analyze the named collections of data (e.g. tables, views, files, topics) within it. The operation will:

* identify the fields within the collection
* gather statistical data about each field according to its declared or inferred type
* submit that metadata to the Qualytics Inference Engine to produce appropriate data quality checks
* tested the inferred data quality checks against actual source data to tune desired sensitivities

!!! note
    * A new Profile Operation can be executed at any time to update the trained data quality checks produced by the Inference Engine

---
# Operation Configuration

A Profile Operation can be configured with the following options:

* Record limit - to profile only a subset of the available data
* Disable Check Inference - to update field metadata without adjusting or infering data quality checks
* Target selection - to target only a subset of the available named collections
