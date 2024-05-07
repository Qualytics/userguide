# Anomaly Overview

An `Anomaly` is an anomalous data set (record or column) that asserted false to applied data quality check(s). Both `Inferred` and `Authored` Checks generate Anomalies, and are batched together when applied through a `Scan Operation` to highlight anomalies:

![Screenshot](../assets/anomalies/anomalies-tab-light.png#only-light)
![Screenshot](../assets/anomalies/anomalies-tab-dark.png#only-dark)



There are two types of anomalies in Qualytics: **Record** and **Shape**:

* A **Record** Anomaly is at the record-level, where a specific field or a combination of fields are anomalous. 
* A **Shape** Anomaly is at the column-level, where a field's shapes and patterns are being impacted at a higher level. 

!!! note
    In either anomaly type, source records are exposed as part of `Anomaly Details`. A Record anomaly will highlight the specific record, and a Shape anomaly will highlight 10 samples from underlying anomalous records.

## Shape Anomaly View

![Screenshot](../assets/anomalies/shape-anomaly-light.png#only-light)
![Screenshot](../assets/anomalies/shape-anomaly-dark.png#only-dark)

## Record Anomaly View

![Screenshot](../assets/anomalies/record-anomaly-light.png#only-light)
![Screenshot](../assets/anomalies/record-anomaly-dark.png#only-dark)

# Anomaly Status

The `Anomaly Status` enables users to better maintain a worklist through anomalies, it is also a mechanism of providing feedback to the system. Specifically, learning methods are tuned according to the feedback provided by the user - invalidating an anomaly will mean that the tolerances of the checks that caught the anomaly will be updated going forward.

* **Active**: The anomaly is active and needs to be addressed
* **Acknowledged**: The anomaly is valid, has been acknowledged but kept active in the Anomaly worklist
* **Resolved**: The anomaly is valid and has been resolved, therefore removed from the Anomaly worklist
* **Invalid**: The anomaly is not valid, removed from the Anomaly worklist and rules updates are suggested to inference engine.

