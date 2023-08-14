# Quick Start Guide

Want to get started immediately with a high-level overview and typical defaults? This section is for you.

---

## Steps

#### Step 1: Connect a [Datastore](/userguide/glossary/#datastore)

Use the intuitive web app or API provided by Qualytics to connect your datastores. This allows the platform to connect and work with your data seamlessly.

![Add a Datastore](assets/datastores/form-light.png#only-light){: style="width:450px"}
![Add a Datastore](assets/datastores/form-dark.png#only-dark){: style="width:450px"}

We recommend adding at least one [Enrichment Datastore](/userguide/glossary/#enrichment-datastore), which helps in identifying and addressing anomalous data more easily.

![Screenshot](assets/enrichment/form-light.png#only-light){: style="width:450px"}
![Screenshot](assets/enrichment/form-dark.png#only-dark){: style="width:450px"}

After you've created a source datastore, the platform will automatically trigger a [Catalog operation](/userguide/glossary/#catalog-operation). This operation analyzes the source datastore's metadata and is an essential preparation for the upcoming Profile and Scan operations.

<br>

#### Step 2: [Profiling](/userguide/glossary/#profiling) the Datastore

Perform a Profile Operation on your chosen source datastore. This operation generates valuable metadata insights for all the data assets within the source datastore. It also automatically infers customized data quality checks based on the profiled data.

![Generate a Profile](assets/operations/operation-profile-light.png#only-light){: style="width:450px"}
![Generate a Profile](assets/operations/operation-profile-dark.png#only-dark){: style="width:450px"}

<br>

#### Step 3: [Scan](/userguide/glossary/#incremental-scan-operation) and Assert [Data Quality Checks](/userguide/glossary/#data-quality-check)

Initiate a scan of your source datastore to assert the automatically inferred checks (as well as any additional checks you create) against both historical and new data within the source datastore. This step ensures that your data is thoroughly evaluated for any anomalies.

![Run a Scan](assets/operations/operation-scan-light.png#only-light){: style="width:450px"}
![Run a Scan](assets/operations/operation-scan-dark.png#only-dark){: style="width:450px"}

<br>

#### Step 4: Review and Flag [Anomalies](/userguide/glossary/#anomaly)

After the scan, review the identified anomalies and flag them with the appropriate status. Qualytics learns from your business and preferences during this process, adapting its future operations to better suit your needs.

![Anonamlies](assets/anomalies/anomaly-table-light.png#only-light)
![Anomalies](assets/anomalies/anomaly-table-dark.png#only-dark)
