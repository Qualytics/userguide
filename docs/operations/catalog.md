# Catalog Operation

The `Catalog Operation` is run on a Datastore to import the named collections (e.g. tables, views, files, topics) of data available within it. The operation will also attempt to automatically identify the best way to support:

* Incremental scanning
* Data partitioning
* Record identification

!!! note
    The attributes of the named collection are recorded as special identifiers and can be manually overridden.

---
## Configuration


A `Catalog Operation` can be configured with the following options:

* **Prune**: Remove any existing named collections that no longer appear in the datastore
* **Recreate**: Restore any previously removed named collection that do currently appear in the database
* **Include**: Include Tables and Views
<br>

![Screenshot](../assets/operations/operation-catalog-light.png#only-light)
![Screenshot](../assets/operations/operation-catalog-dark.png#only-dark)

## API Payload Examples

### Running a Catalog operation

This section provides a sample payload for running a catalog operation. Replace the placeholder values with actual data relevant to your setup.

#### Endpoint (Post)

`/api/operations/run` _(post)_

=== "Running a catalog operation of a datastore"
    ```json
        {
            "type":"catalog",
            "datastore_id": datastore-id,
            "prune":false,
            "recreate":false,
            "include":[
                "table",
                "view"
            ]
        }
    ```

### Retrieving Catalog Operation Status

#### Endpoint (Get)

`/api/operations/{id}` _(get)_

=== "Example result response"
    ```json
        {
            "items": [
                {
                "id": 12345,
                "created": "YYYY-MM-DDTHH:MM:SS.ssssssZ",
                "type": "catalog",
                "start_time": "YYYY-MM-DDTHH:MM:SS.ssssssZ",
                "end_time": "YYYY-MM-DDTHH:MM:SS.ssssssZ",
                "result": "success",
                "message": null,
                "triggered_by": "user@example.com",
                "datastore": {
                    "id": 54321,
                    "name": "Datastore-Sample",
                    "store_type": "jdbc",
                    "type": "db_type",
                    "enrich_only": false,
                    "enrich_container_prefix": "_data_prefix",
                    "favorite": false
                },
                "schedule": null,
                "include": [
                    "table",
                    "view"
                ],
                "prune": false,
                "recreate": false
                }
            ],
            "total": 1,
            "page": 1,
            "size": 50,
            "pages": 1
        }
    ```
