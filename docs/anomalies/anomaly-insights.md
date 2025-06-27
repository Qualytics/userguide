# Anomaly Insights

The Anomaly Insights view in Qualytics provides a comprehensive breakdown of each detected anomaly, offering both summary and in-depth context. It includes identifiers, status, type, source information, and metadata like fingerprints and severity. This detailed insight helps users understand, investigate, and take appropriate actions to resolve or track anomalies, all while maintaining data quality at scale.

Let’s get started 🚀

**Step 1:** Log in to your Qualytics account and click the **Explore** button on the left side panel of the interface.

![explore](../assets/explore/anomalies/explore-light.png#only-light)
![explore](../assets/explore/anomalies/explore-dark.png#only-dark)

**Step 2:** Click on the **"Anomalies"** from the Navigation Tab.

![anomalies](../assets/explore/anomalies/anomalies-light.png#only-light)
![anomalies](../assets/explore/anomalies/anomalies-dark.png#only-dark)

You will be navigated to the **Anomalies** tab, where you'll see a list of all the detected anomalies across various tables and fields from different source datastores, based on the applied data quality checks.

![all](../assets/explore/anomalies/all-anomalies-light.png#only-light)
![all](../assets/explore/anomalies/all-anomalies-dark.png#only-dark)

**Step 3**: Click on the anomaly that you want to see the details of.

The anomaly identified during the scan operation illustrates the following details:

**1. Anomaly ID:** A numerical identifier (e.g. #81366) used for quick search and easy identification of anomalies within the Qualytics interface.

**2. Status:** Reflects the status of the Anomaly. It can be **active**, **acknowledged**, **resolved**, **duplicate** or **invalid**.

**3. Share:** Copy a shareable link to a specific anomaly. This can be shared with other users or stakeholders for collaboration.

**4. Anomaly UID:** A longer, standardized, and globally unique identifier, displayed as a string of hexadecimal characters. This can be copied to the clipboard.

**5. Fingerprint:** The fingerprint icon indicates whether an anomaly has an associated fingerprint. If present, clicking the icon copies the fingerprint number to the clipboard. Hovering over the icon displays a tooltip with a link to the user guide.

**6. Acknowledge:** Use this option to mark an anomaly as reviewed. Acknowledging an anomaly means it has been identified and noted, but it remains active until resolved.

**7. Archive:** Use this option to remove an anomaly from the active list. Archiving an anomaly does not delete it but stores it for historical tracking and future reference.

**8. Type:** This reflects the **type** to which the anomaly belongs (e.g. Record or Shape).

**9. Weight:** A metric that indicates the severity or importance of the anomaly. Higher weights indicate more critical issues.

**10. Detected:** Reflects the **timestamp** when the anomaly was first detected.

**11. Scan:** Click on this to view the outcome of a data quality scan. It includes the scan status, the time taken, the user who triggered it, the schedule status, and a detailed list of anomalies detected across various tables.

![anomalies-details](../assets/datastores/anomalies/anomalies-details-light.png#only-light)
![anomalies-details](../assets/datastores/anomalies/anomalies-details-dark.png#only-dark)

!!! note
    Clicking on the expand icon navigates to the anomaly details page, providing key insights into a specific data anomaly.

In addition to the above details, the users can also explore the following additional details of the Anomaly:

**1. Name:** This indicates the name of the source datastore where the anomaly was detected.

!!! tip
    Clicking on the expand icon opens a detailed view and navigates to the dataset’s page, providing more information about the source datastore where the anomaly was found.

**2. Table Name:** This specifies the particular table within the dataset that contains the anomaly. It helps in pinpointing the exact location of the data quality issue.

!!! tip
    Clicking on the expand icon navigates to the table’s page, providing more in-depth information about the table structure and contents.

**3. Location:** Full path or location within the data hierarchy where the table resides. It gives a complete reference to the exact position of the data in the database or data warehouse.

![details](../assets/datastores/anomalies/details-light.png#only-light)
![details](../assets/datastores/anomalies/details-dark.png#only-dark)