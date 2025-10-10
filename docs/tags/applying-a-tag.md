## Applying a Tag
Once a Tag is created, it's ready to be associated with a ```Datastore```, ```Profile```, ```Check```, ```Notification``` and ultimately an ```Anomaly```.

### Tag Inheritance

- When a ```Tag``` is applied to a data asset, all the descendants of that data asset also receive the ```Tag```.

    - For example, if a ```Tag``` named **Critical** is applied to a Datastore then all the Tables, Fields, and Checks under that Datastore also receive the ```Tag```.

    !!! note

        Anomalies will inherit the tags if a scan has been run.

- Likewise, if the **Critical** ```Tag``` is subsequently removed from one of the Tables in that Datastore, then all the Fields and Checks belonging to that Table will have the **Critical** ```Tag``` removed as well.

- When a new data asset is created, it inherits the ```Tags``` from the owning data asset. For example, if a user creates a new Computed Table, it inherits all the ```Tags``` that are applied to the Datastore in which it is created.

### Tagging Anomalies

- Anomalies also inherit ```Tags``` at the time they are created. They inherit all the ```Tags``` of all the associated failed checks.

- Thus Anomalies do not inherit subsequent tag changes from those checks. They only inherit tags one time - at creation time.

- ```Tags``` can be directly applied to or removed from Anomalies at any time after creation.