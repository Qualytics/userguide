# Anomaly Status

Anomaly status in Qualytics is a key feature for monitoring the lifecycle of detected data quality issues. It provides clear visibility into whether anomalies are new, acknowledged, or resolved, helping data teams efficiently prioritize, investigate, and take corrective action. By categorizing anomalies into various statuses, users can filter and manage them more effectively across the platform.

Let’s get started 🚀

## Anomaly Categories in Datastore

In the Datastore view, anomalies are grouped as **Open** (Active or Acknowledged) and **Archived** (Resolved, Duplicate, or Invalid). This helps users focus on unresolved issues while maintaining a record of past anomalies for reference and analysis.

**Step 1:** Log in to your Qualytics account and select the datastore from the left menu on which you want to manage your anomalies.

![datastore](../assets/datastores/manage-anomalies/datastore-light-1.png#only-light)
![datastore](../assets/datastores/manage-anomalies/datastore-dark-1.png#only-dark)

**Step 2:** Click on the **“Anomalies”** from the Navigation Tab.

![anomalies](../assets/datastores/manage-anomalies/anomalies-light-2.png#only-light)
![anomalies](../assets/datastores/manage-anomalies/anomalies-dark-2.png#only-dark)

### Open Anomalies

By selecting Open Anomalies, you can view anomalies that have been detected but remain unacknowledged or unresolved. These anomalies require attention and may need further investigation or corrective action.

![open-anomalies](../assets/datastores/anomalies-datastore/open-anomalies-light-2.png#only-light)
![open-anomalies](../assets/datastores/anomalies-datastore/open-anomalies-dark-2.png#only-dark)

This option helps focus on unaddressed issues while allowing seamless navigation to **All**, **Active**, or **Acknowledged** anomalies as needed.

**1. Active**: By selecting **Active Anomalies**, you can focus on anomalies that are currently unresolved or require immediate attention. These are the anomalies that are still in play and have not yet been acknowledged, archived, or resolved.

![active-anomalies](../assets/datastores/anomalies-datastore/active-anomalies-light-4.png#only-light)
![active-anomalies](../assets/datastores/anomalies-datastore/active-anomalies-dark-4.png#only-dark)

**2. Acknowledged**: By selecting **Acknowledged Anomalies**, you can see all anomalies that have been reviewed and marked as acknowledged. This status indicates that the anomalies have been noted, though they may still require further action.

![acknowledged-anomalies](../assets/datastores/anomalies-datastore/acknowledged-anomalies-light-5.png#only-light)
![acknowledged-anomalies](../assets/datastores/anomalies-datastore/acknowledged-anomalies-dark-5.png#only-dark)

**3. All**: By selecting **All Anomalies**, you can view the complete list of anomalies, regardless of their status. This option helps you get a comprehensive overview of all issues that have been detected, whether they are currently active, acknowledged, or archived.

![all-anomalies](../assets/datastores/anomalies-datastore/all-anomalies-light-3.png#only-light)
![all-anomalies](../assets/datastores/anomalies-datastore/all-anomalies-dark-3.png#only-dark)

### Archived Anomalies

By selecting **Archived Anomalies**, you can view anomalies that have been resolved or moved out of active consideration. Archiving anomalies allows you to keep a record of past issues without cluttering the active list.

![archived-anomalies](../assets/datastores/anomalies-datastore/archived-anomalies-light-6.png#only-light)
![archived-anomalies](../assets/datastores/anomalies-datastore/archived-anomalies-dark-6.png#only-dark)

You can also categorize the archived anomalies based on their status as **Resolved**, **Duplicate** and **Invalid**, to manage and review them effectively.

**1. Resolved**: This indicates that the anomaly was a legitimate data quality concern and has been addressed.

![resolved](../assets/datastores/anomalies-datastore/resolved-light-7.png#only-light)
![resolved](../assets/datastores/anomalies-datastore/resolved-dark-7.png#only-dark)

**2. Duplicate**: This indicates that the anomaly is a duplicate of an existing record and has already been addressed.

![duplicate](../assets/datastores/anomalies-datastore/duplicate-light.png#only-light)
![duplicate](../assets/datastores/anomalies-datastore/duplicate-dark.png#only-dark)

**3. Invalid**: This indicates that the anomaly is not a legitimate data quality concern and does not require further action.

![invalid](../assets/datastores/anomalies-datastore/invalid-light-8.png#only-light)
![invalid](../assets/datastores/anomalies-datastore/invalid-dark-8.png#only-dark)

**4. All**: Displays all archived anomalies, including those marked as Resolved, Duplicate, and Invalid, giving a comprehensive view of all past issues. 

![all](../assets/datastores/anomalies-datastore/all-light-9.png#only-light)
![all](../assets/datastores/anomalies-datastore/all-dark-9.png#only-dark)

## Anomaly Categories in Explore 

On the Explore page, anomaly statuses follow the same structure as Open and Archived but across multiple datastores. This centralized view allows quick access to unresolved issues and efficient tracking of archived anomalies across your data environment.

**Step 1:** Log in to your Qualytics account and click the **Explore** button on the left side panel of the interface.

![explore](../assets/explore/anomalies/explore-light.png#only-light)
![explore](../assets/explore/anomalies/explore-dark.png#only-dark)

**Step 2:** Click on the **"Anomalies"** from the Navigation Tab.

![anomalies](../assets/explore/anomalies/anomalies-light.png#only-light)
![anomalies](../assets/explore/anomalies/anomalies-dark.png#only-dark)

You will be navigated to the **Anomalies** tab, where you'll see a list of all the detected anomalies across various tables and fields from different source datastores, based on the applied data quality checks.

![all](../assets/explore/anomalies/all-anomalies-light.png#only-light)
![all](../assets/explore/anomalies/all-anomalies-dark.png#only-dark)

### Open

By selecting **Open Anomalies**, you can view anomalies that have been detected but remain unacknowledged or unresolved. These anomalies require attention and may need further investigation or corrective action. 

![open](../assets/explore/anomalies/open-light.png#only-light)
![open](../assets/explore/anomalies/open-dark.png#only-dark)

This option helps focus on unaddressed issues while allowing seamless navigation to **All**, **Active**, or **Acknowledged** anomalies as needed.

**1. Active**: By selecting **Active Anomalies**, you can focus on anomalies that are currently unresolved or require immediate attention. These are the anomalies that are still in play and have not yet been acknowledged, archived, or resolved.

![active](../assets/explore/anomalies/active-light.png#only-light)
![active](../assets/explore/anomalies/active-dark.png#only-dark)

**2. Acknowledge**: By selecting **Acknowledged Anomalies**, you can see all anomalies that have been reviewed and marked as acknowledged. This status indicates that the anomalies have been noted, though they may still require further action.

![acknowledge](../assets/explore/anomalies/acknowledge-light.png#only-light)
![acknowledge](../assets/explore/anomalies/acknowledge-dark.png#only-dark)

**3. All**: By selecting **All Anomalies**, you can view the complete list of anomalies, regardless of their status. This option helps you get a comprehensive overview of all issues that have been detected, whether they are currently active, acknowledged, or archived.

![all](../assets/explore/anomalies/all-light.png#only-light)
![all](../assets/explore/anomalies/all-dark.png#only-dark)

### Archived

By selecting **Archived Anomalies**, you can view anomalies that have been resolved or moved out of active consideration. Archiving anomalies allows you to keep a record of past issues without cluttering the active list.

![archived](../assets/explore/anomalies/archived-light.png#only-light)
![archived](../assets/explore/anomalies/archived-dark.png#only-dark)

You can also categorize the archived anomalies based on their status as **Resolved**, **Duplicate** and **Invalid**, to review them effectively.

**1. Resolved**: This indicates that the anomaly was a legitimate data quality concern and has been addressed.

![resolved](../assets/explore/anomalies/resolved-light.png#only-light)
![resolved](../assets/explore/anomalies/resolved-dark.png#only-dark)

**2. Duplicate**: This indicates that the anomaly is a duplicate of an existing record and has already been addressed.

![duplicate](../assets/explore/anomalies/duplicate-light.png#only-light)
![duplicate](../assets/explore/anomalies/duplicate-dark.png#only-dark)

**3. Invalid**: This indicates that the anomaly is not a legitimate data quality concern and does not require further action.

![invalid](../assets/explore/anomalies/invalid-light.png#only-light)
![invalid](../assets/explore/anomalies/invalid-dark.png#only-dark)

**4. All**: Displays all archived anomalies, including those marked as Resolved, Duplicate, and Invalid, giving a comprehensive view of all past issues.

![all](../assets/explore/anomalies/all-archived-light.png#only-light)
![all](../assets/explore/anomalies/all-archived-dark.png#only-dark)