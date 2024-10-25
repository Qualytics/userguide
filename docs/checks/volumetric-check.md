# Volumetrics Check

The Volumetric Check has been introduced to help users monitor and maintain the stability of data volumes across various datasets. This feature ensures that the size or volume of your data (either in terms of rows or bytes) remains within an acceptable range based on historical trends. It is designed to detect significant fluctuations by comparing the current data volume against a moving daily average.

### How It Works

The system automatically infers and maintains volumetric checks based upon observed daily, weekly, and monthly averages. These checks enable proactive management of data volume trends, ensuring that any unexpected deviations are identified as anomalies for review. 

### Automating Adaptive Volumetric Checks

The following Volumetric Checks are automatically inferred for data assets with automated volume measurements enabled:

* **Daily**: the expected daily volume expressed as an absolute minimum and maximum threshold.  The thresholds are calculated as standard deviations from the previous 7-day moving average. 

* **Weekly**: the expected weekly volume expressed as an absolute minimum and maximum threshold.  The thresholds are calculated as standard deviations from the previous four weeks’ weekly volume moving average.  

* **Monthly**: the expected 4-week volume expressed as an absolute minimum and maximum threshold.  The thresholds are calculated as standard deviations from the previous sixteen weeks’ 4-week volume moving average.

#### Scan Assertion and Anomaly Creation

Volumetric Checks are asserted during a [Scan Operation](https://userguide.qualytics.io/source-datastore/scan/) just like all other check types and enrichment of volumetric check anomalies is fully supported. This enables full support for custom scheduling of volumetric checks and remediation workflows of volumetric anomalies.

### Adaptive Thresholds and Human Adjustments

Each time a volume measurement is recorded for a data asset, the system will automatically infer and update any inferred Volumetric Checks for that asset.

By default, thresholds are set to 2 standard deviations from the moving average, but the system will adapt over time using inference weights to fine-tune these thresholds based on historical trends.

This feature is essential for maintaining data integrity and ensuring that any deviations from expected data volumes are quickly identified and addressed.

![volumetric-check](../assets/checks/volumetric-check/volumetric-check-light.png#only-light)
![volumetric-check](../assets/checks/volumetric-check/volumetric-check-dark.png#only-dark)