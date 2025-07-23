# **Anomalies**

Anomalies in Qualytics represent data points that deviate from expected patterns or violate defined quality rules, often highlighting issues such as missing values, structural inconsistencies, or incorrect data. These anomalies are detected during scan operations through system-inferred or user-authored checks. 

## Anomaly Types

Qualytics classifies anomalies into two types: **Record Anomalies** and **Shape Anomalies**. Record anomalies flag rows with data issues like missing or invalid values, while shape anomalies detect structural problems such as missing columns or schema changes. Together, they ensure thorough data quality coverage at both the value and structure levels.

!!! note 
    For more information, please refer to the [Anomaly Types](anomaly-types.md) Documentation.

## Anomaly Detection Process

The anomaly detection process in Qualytics ensures data quality by identifying deviations from expected patterns through a structured workflow. It starts with configuring datastores, cataloging metadata, and profiling data to understand its structure. Users then apply quality checks—either authored or inferred—during Scan operations. Any failures are flagged as anomalies, enabling timely detection and resolution of data issues to maintain overall data integrity.

!!! note
    For more information, please refer to the [Anomaly Detection Process](anomaly-detection.md) Documentation.