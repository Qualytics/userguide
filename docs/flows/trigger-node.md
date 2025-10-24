# Trigger

**Step 1:** After completing the **"Flow"** node setup, users can click on the **"Trigger"** node.

![trigger](.././assets/flows/trigger-light-9.png)

A panel will appear on the right-hand side, enabling users to define when the flow should start. The panel provides four options for initiating the flow. Users can choose one of the following options:

* Operation Completes.

* Anomalous Table and File Detection.

* Anomaly Detected.

* Manual

![triggersetting](.././assets/flows/triggersetting-light-10.png)

## Operation Completes

This type of flow is triggered whenever an operation, such as a catalog, profile, or scan, is completed on a source datastore. Upon completion, teams are promptly notified through in-app messages and, if configured, via external notification channels such as email, Slack, Microsoft Teams, and others. For example, the team is notified whenever the catalog operation is completed, helping them proceed with the profile operation on the datastore.

![operation](.././assets/flows/operation-light-11.png)

**Filter Conditions**

Filters can be set to narrow down which operations should trigger the flow execution:

1. **Source Datastore Tags**: The flow is triggered only for source datastores that have all the selected tags assigned.

2. **Source Datastores**: The flow is triggered only for the selected source datastores.

3. **Operation Types**: The flow is triggered only for operations that match one or more of the selected types.

4. **Operation Status**: The flow is triggered for operations with a status of either Success or Failure.

![operation](.././assets/flows/operation-light-12.png)

After defining the conditions, users must click the **Save** button to finalize the trigger configuration.

![save](.././assets/flows/save-light-8.png)

## Anomalous Table and File Detected

This flow is triggered when anomalies are detected within a specific table, file and check rule types. It includes information about the number of anomalies found and the specific scan target within the datastore. This is useful for assessing the overall health of a particular datastore.  

![table](.././assets/flows/table-light-14.png)

**Filter Conditions**

Users can optionally set filters to specify which tables or files should trigger the flow execution.

1. **Tables / Files Tags**: Only tables or files with all the selected tags assigned will trigger the flow.

2. **Source Datastores**: The flow is triggered only for the selected source datastores.

3. **Check Rule Types**: Only anomalies identified by one or more of the selected check rule types will initiate the flow.

![table](.././assets/flows/table-light-15.png)

After defining the conditions, users must click the **Save** button to finalize the trigger configuration.  

![save](.././assets/flows/save-light-8.png)

## Anomaly Detected

This type of flow is triggered when any single anomaly is identified in the data. The flow message typically includes the type of anomaly detected and the datastore where it was found. It provides specific information about the anomaly type, which helps quickly understand the issue's nature.

![anomaly](.././assets/flows/anomaly-light-17.png)

**Filter Condition**

Users can define specific conditions to determine when the flow should be initiated.

1. **Anomaly’s Tags**: Only anomalies with all selected tags assigned will trigger the flow.

2. **Source Datastores**: Only triggered when anomalies are detected in the selected datastores.

3. **Check Rule Types**: Only anomalies identified by one or more of the selected check rule types will initiate the flow.

4. **Anomaly Weight (Min)**: Only anomalies with a weight equal to or greater than the specified value will trigger the flow.

![anomaly](.././assets/flows/anomaly-light-18.png)

**Step 2:** Once the filter conditions are set, users must click the **Save** button to finalize the configuration.

![save](.././assets/flows/save-light-8.png)

## Manual

The flow starts only when the user manually triggers it. It doesn’t depend on any automatic conditions or detections, giving the user full control.  

![manual](.././assets/flows/manual-light-20.png)

Once selected, users must click the **Save** button to confirm the manual trigger configuration.

![save](.././assets/flows/save-light-8.png)

Hover over the **filter tooltip** in trigger nodes to view the applied conditions such as tags, datastores, and operation types. This provides quick visibility into how each trigger is configured.

![filter-tooltip](.././assets/flows/filter-tooltip-light.png)