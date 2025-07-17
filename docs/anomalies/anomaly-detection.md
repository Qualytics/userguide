# Anomaly Detection Process

The anomaly detection process in Qualytics ensures data quality by identifying deviations from expected patterns through a structured workflow. It starts with configuring datastores, cataloging metadata, and profiling data to understand its structure. Users then apply quality checks—either authored or inferred—during Scan operations. Any failures are flagged as anomalies, enabling timely detection and resolution of data issues to maintain overall data integrity.

Let’s get started 🚀

**1. Create a Datastore and Connection**

By setting up a datastore and establishing a connection to your data source (database or file system), you create a robust foundation for effective data management and analysis in Qualytics. This setup enables you to access, manipulate, and utilize your data efficiently, paving the way for advanced data quality checks, profiling, scanning, anomaly surveillance, and other analytics tasks.

!!! note 
    For more information, please refer to the [Configuring Datasource](../add-datastores/overview-of-a-datastore.md#configuring-data-source) documentation.

**2. Catalog Operation**

The Catalog operation involves systematically collecting data structures along with their corresponding metadata. This process also includes a thorough analysis of the existing metadata within the datastore. This ensures a solid foundation for the subsequent Profile and Scan operations.

!!! note 
    For more information, please refer to the [Catalog Operation](../source-datastore/catalog.md) Documentation.

**3. Profile Operation**

The Profile operation enables training of the collected data structures and their associated metadata values. This is crucial for gathering comprehensive aggregated statistics on the selected data, providing deeper insights, and preparing the data for quality assessment.

!!! note 
    For more information, please refer to the documentation [Profile Operation](../source-datastore/profile.md).

**4. Create Authored Checks**

Authored Checks are manually created data quality checks in Qualytics, defined by users either through the user interface (UI) or via API. These checks encapsulate specific data quality check, along with additional context such as associated notifications, tags, filters, and tolerances.  
Authored checks can range from simple, template-based checks to more complex rules implemented through SQL or user-defined functions (UDFs) in Scala. By allowing users to define precise criteria for data quality, authored checks enable detailed monitoring and validation of data within the datastore, ensuring that it meets the specified standards and requirements.

!!! note
    For more information, please refer to the documentation [Authored Checks](../checks/authored-check.md). 

**5. Scan Operation**

The Scan operation asserts rigorous quality checks to identify any anomalies within the data. This step ensures data integrity and reliability by recording the analyzed data in your configured enrichment datastore, facilitating continuous data quality improvement.

!!! note 
    For more information, please refer to the documentation [Scan Operation](../source-datastore/scan.md). 

**6. Anomaly Analysis**

An Anomaly is a data record or column that fails a data quality check during a Scan Operation. These anomalies are identified through both Inferred and Authored Checks and are grouped together to highlight data quality issues. This process ensures that any deviations from expected data quality standards are promptly identified and addressed.

!!! note 
    For more information, please refer to the documentation [Anomalies Overview](anomalies.md).