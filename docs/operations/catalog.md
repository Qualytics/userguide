# Catalog Operation

The Catalog Operation is executed on a Datastore to import the named collections (e.g. tables, views, files, topics) of data available within it. The operation will also attempt to automatically identify the best way to support:

* incremental scanning
* data partitioning
* record identification

!!! note
    * These attributes of the named collection are recorded as special identifiers and can be manually overridden

---
# Operation Configuration

A Catalog Operation can be configured with the following options:

* Prune - remove any existing named collections that no longer appear in the datastore
* Recreate - restore any previously removed named collection that do currently appear in the database