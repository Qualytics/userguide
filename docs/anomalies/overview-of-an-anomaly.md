# Overview of an Anomaly

* An `Anomaly` is an anomalous data set (record or column) that asserted false to applied data quality check(s). Both `Inferred` and `Authored` Checks generate Anomalies, and are batched together when applied through a `Scan Operation` to highlight anomalies:

![Screenshot](../assets/anomalies/anomalies-tab-light.png#only-light)
![Screenshot](../assets/anomalies/anomalies-tab-dark.png#only-dark)

![Screenshot](../assets/anomalies/anomaly-table-light.png#only-light)
![Screenshot](../assets/anomalies/anomaly-table-dark.png#only-dark)


There are two types of anomalies in Qualytics: `Record` and `Shape`:

* A `Record` Anomaly is at the record-level, where a specific field or a combination of fields are anomalous. 
* A `Shape` Anomaly is at the column-level, where a field's shapes and patterns are being impacted at a higher level. 

!!! note
    In either anomaly type, source records are exposed as part of `Anomaly Details`. A Record anomaly will highlight the specific record, and a Shape anomaly will highlight 10 samples from underlying anomalous records.

* Shape Anomaly view

![Screenshot](../assets/anomalies/shape-anomaly-light.png#only-light)
![Screenshot](../assets/anomalies/shape-anomaly-dark.png#only-dark)

* Record Anomaly view

![Screenshot](../assets/anomalies/record-anomaly-light.png#only-light)
![Screenshot](../assets/anomalies/record-anomaly-dark.png#only-dark)



* When a [Scan](/userguide/operations/scan) is run, Qualytics will highlight anomalies with the following information:

    ![Screenshot](../assets/anomalies/anomalies-fields-light.png#only-light)
    ![Screenshot](../assets/anomalies/anomalies-fields-dark.png#only-dark)

    1. `Table`/`File`: the `Table` or `File` of the anomaly
    2. `Field`: the field(s) of the anomaly
    3. `Location`: fully qualified location of the anomaly
    4. `Rule`: `Infered` and/or `Authored` checks that failed assertions
    5. `Description`: human-readable, auto-generated description of the `Anomaly`

    ![Screenshot](../assets/anomalies/anomalies-status-light.png#only-light)
    ![Screenshot](../assets/anomalies/anomalies-status-dark.png#only-dark)

    1. `Status`: The status of the anomaly. If it's `active`, `acknowledged`, `resolved` or `invalid`
    2. `Type`: `Record` or `Shape`
    3. `Tag`: tag(s) / label(s) associated with an anomaly
    4. `Date time`: date/time when the anomaly was found

!!! note
    The <spam id='required'>`New`</spam> message means this is a new, active anomaly that has been found as part of the latest `Scan Operation`.
    
---
# Status

* The `Anomaly Status` can be set to `Active`, `Acknowledged`, `Resolved` and `Invalid`. While this enables users to better maintain a worklist through anomalies, it is also a mechanism of providing feedback to the system. Specifically, learning methods are tuned according to the feedback provided by the user - invalidating an anomaly will mean that the tolerances of the checks that caught the anomaly will be updated going forward.

    1. `Active`: The anomaly is active and needs to be addressed
    2. `Acknowledged`: The anomaly is valid, has been acknowledged but kept active in the Anomaly worklist
    3. `Resolved`: The anomaly is valid and has been resolved, therefore removed from the Anomaly worklist
    4. `Invalid`: The anomaly is not valid, removed from the Anomaly worklist and rules updates are suggested to inference engine.

